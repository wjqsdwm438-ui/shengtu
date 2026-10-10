#!/usr/bin/env python3
"""Build deterministic SRT timeline and semi-manual routing index.

This script supports ALG-S01 evidence only. It does not decide final S-line
routes, create A-line pages, or generate prompts.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path

TIMECODE_RE = re.compile(r"(?P<start>\d\d:\d\d:\d\d,\d{3})\s+-->\s+(?P<end>\d\d:\d\d:\d\d,\d{3})")


@dataclass
class Caption:
    index: int
    start: str
    end: str
    text: str


def parse_srt(path: Path) -> list[Caption]:
    raw = path.read_text(encoding="utf-8-sig")
    blocks = re.split(r"\r?\n\s*\r?\n", raw.strip()) if raw.strip() else []
    captions: list[Caption] = []
    for block in blocks:
        lines = [line.strip() for line in block.splitlines() if line.strip()]
        if len(lines) < 2:
            continue
        try:
            idx = int(lines[0])
            time_line = lines[1]
            text_lines = lines[2:]
        except ValueError:
            idx = len(captions) + 1
            time_line = lines[0]
            text_lines = lines[1:]
        match = TIMECODE_RE.search(time_line)
        if not match:
            continue
        text = " ".join(text_lines).strip()
        captions.append(Caption(idx, match.group("start"), match.group("end"), text))
    return captions


def time_to_seconds(value: str) -> float:
    hh, mm, rest = value.split(":")
    ss, ms = rest.split(",")
    return int(hh) * 3600 + int(mm) * 60 + int(ss) + int(ms) / 1000


def make_segments(captions: list[Caption], block_seconds: int) -> list[dict]:
    if not captions:
        return []
    segments: list[dict] = []
    current: list[Caption] = []
    current_start = time_to_seconds(captions[0].start)
    for cap in captions:
        cap_start = time_to_seconds(cap.start)
        should_split = current and (cap_start - current_start >= block_seconds)
        if should_split:
            segments.append(segment_from_captions(current, len(segments) + 1, block_seconds))
            current = []
            current_start = cap_start
        current.append(cap)
    if current:
        segments.append(segment_from_captions(current, len(segments) + 1, block_seconds))
    return segments


def segment_from_captions(captions: list[Caption], number: int, block_seconds: int) -> dict:
    text = " ".join(cap.text for cap in captions).strip()
    return {
        "segment_id": f"seg_{number:03d}",
        "start_time": captions[0].start,
        "end_time": captions[-1].end,
        "source_line_ids": [cap.index for cap in captions],
        "subtitle_count": len(captions),
        "merged_text": text,
        "merge_reason": f"Deterministic {block_seconds}s block for manual semantic review; final S-route must be confirmed by S-line.",
        "manual_review_required": True,
    }


def write_outputs(srt_path: Path, out_dir: Path, segments: list[dict]) -> dict:
    out_dir.mkdir(parents=True, exist_ok=True)
    stem = srt_path.stem
    jsonl_path = out_dir / f"{stem}.timeline.jsonl"
    md_path = out_dir / f"{stem}.timeline.md"
    index_path = out_dir / f"{stem}.srt_index.md"

    with jsonl_path.open("w", encoding="utf-8") as fh:
        for segment in segments:
            fh.write(json.dumps(segment, ensure_ascii=False) + "\n")

    md_lines = ["# SRT Timeline", "", f"Source: `{srt_path}`", ""]
    for segment in segments:
        md_lines.extend([
            f"## {segment['segment_id']} {segment['start_time']} - {segment['end_time']}",
            f"- source_line_ids: {segment['source_line_ids']}",
            f"- subtitle_count: {segment['subtitle_count']}",
            f"- merged_text: {segment['merged_text']}",
            f"- merge_reason: {segment['merge_reason']}",
            "",
        ])
    md_path.write_text("\n".join(md_lines), encoding="utf-8")

    index_lines = ["# SRT Semi-Manual Routing Index", "", "This file is evidence for ALG-S01 only. It is not the final S-line result.", ""]
    for segment in segments:
        index_lines.extend([
            f"## {segment['segment_id']}",
            f"- 时间段: {segment['start_time']} - {segment['end_time']}",
            f"- 字幕编号: {segment['source_line_ids']}",
            f"- 语义合并理由: {segment['merge_reason']}",
            f"- 字幕摘要: {segment['merged_text']}",
            "- 教学动作: ",
            "- 推荐 S线: ",
            "- 是否适合进入 A线: ",
            "- 是否适合拆成视觉页: ",
            "- 是否需要拆页: ",
            "- 是否需要上屏文字: ",
            "- 备注: ",
            "",
        ])
    index_path.write_text("\n".join(index_lines), encoding="utf-8")

    return {"timeline_jsonl": str(jsonl_path), "timeline_md": str(md_path), "srt_index_md": str(index_path)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Build SRT index outputs for V2.7 ALG-S01 evidence.")
    parser.add_argument("input_srt", type=Path)
    parser.add_argument("--out-dir", type=Path)
    parser.add_argument("--block-seconds", type=int, default=60)
    args = parser.parse_args()

    captions = parse_srt(args.input_srt)
    segments = make_segments(captions, max(10, args.block_seconds))
    out_dir = args.out_dir or args.input_srt.parent
    outputs = write_outputs(args.input_srt, out_dir, segments)
    print(json.dumps({"caption_count": len(captions), "segment_count": len(segments), "outputs": outputs}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
