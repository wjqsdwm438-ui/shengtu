#!/usr/bin/env python3
"""Run the V2.7.1 offline baseline checks.

The default mode is read-only: command outputs are created under a temporary
directory and removed at exit.  Pass ``--update-evidence`` explicitly to
replace the checked-in ``test_logs`` evidence after every check passes.
Only the Python standard library is used.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SCRIPTS = {
    "srt": ROOT / "scripts" / "build_srt_index.py",
    "layout": ROOT / "scripts" / "check_layout_skeleton.py",
    "budget": ROOT / "scripts" / "check_text_budget.py",
    "complexity": ROOT / "scripts" / "score_page_complexity.py",
}
SKILL_DIRS = (
    "stage-sline-srt-media-routing",
    "stage-aline-course-visual-routing",
    "stage-bline-production-handoff",
    "stage-tline-prompt-translation",
    "stage-cline-gpt-image-execution-feedback",
    "stage-algorithm-lite-companion",
)
TEXT_SUFFIXES = {
    ".md", ".txt", ".json", ".jsonl", ".yaml", ".yml", ".py",
    ".srt", ".drawio", ".svg",
}


@dataclass
class Report:
    failures: list[str] = field(default_factory=list)
    passes: list[str] = field(default_factory=list)

    def check(self, condition: bool, label: str, detail: str = "") -> None:
        if condition:
            self.passes.append(label)
            print(f"[PASS] {label}")
        else:
            message = f"{label}: {detail}" if detail else label
            self.failures.append(message)
            print(f"[FAIL] {message}")


def load_utf8(path: Path) -> str:
    """Read UTF-8 text and reject either form of UTF-16 BOM."""
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        raise ValueError("UTF-16 BOM is forbidden")
    return raw.decode("utf-8-sig")


def write_json_lf(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as stream:
        stream.write(json.dumps(value, ensure_ascii=False, indent=2))
        stream.write("\n")


def run_json(script: Path, *arguments: str) -> tuple[int, dict, str]:
    env = os.environ.copy()
    env["PYTHONUTF8"] = "1"
    completed = subprocess.run(
        [sys.executable, str(script), *arguments],
        cwd=ROOT,
        env=env,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8",
        errors="strict",
        check=False,
    )
    try:
        payload = json.loads(completed.stdout)
    except json.JSONDecodeError as exc:
        raise RuntimeError(
            f"{script.name} did not emit valid JSON (exit {completed.returncode}): "
            f"{completed.stderr.strip() or completed.stdout.strip()}"
        ) from exc
    return completed.returncode, payload, completed.stderr


def check_script_syntax(report: Report) -> None:
    for name, script in SCRIPTS.items():
        try:
            source = load_utf8(script)
            compile(source, str(script), "exec")
            report.check(True, f"syntax:{name}")
        except (OSError, UnicodeError, SyntaxError, ValueError) as exc:
            report.check(False, f"syntax:{name}", str(exc))


def check_algorithm_examples(report: Report, work: Path) -> tuple[dict[str, object], dict[str, bytes]]:
    evidence: dict[str, object] = {}
    srt_files: dict[str, bytes] = {}

    budgets = (
        ("low", 7, "low"),
        ("medium", 105, "medium"),
        ("high", 174, "high"),
        ("over_180", 333, "gate"),
    )
    for stem, count, risk in budgets:
        try:
            code, data, stderr = run_json(
                SCRIPTS["budget"], f"tests/text_budget_{stem}.txt"
            )
            ok = code == 0 and data.get("char_count_no_space") == count and data.get("risk") == risk
            report.check(ok, f"example:text_budget_{stem}", stderr.strip() or repr(data))
            evidence[f"text_budget_{stem}.stdout.json"] = data
        except (OSError, RuntimeError) as exc:
            report.check(False, f"example:text_budget_{stem}", str(exc))

    for stem, expected_code, expected_pass in (("pass", 0, True), ("fail", 2, False)):
        try:
            code, data, stderr = run_json(
                SCRIPTS["layout"], f"tests/layout_skeleton_{stem}.json"
            )
            ok = code == expected_code and data.get("pass") is expected_pass
            if stem == "fail":
                ok = ok and data.get("empty_background_risk") is True and bool(data.get("missing_fields"))
            report.check(ok, f"example:layout_skeleton_{stem}", stderr.strip() or repr(data))
            evidence[f"layout_skeleton_{stem}.stdout.json"] = data
        except (OSError, RuntimeError) as exc:
            report.check(False, f"example:layout_skeleton_{stem}", str(exc))

    for stem, score in (("low", 0), ("high", 100)):
        try:
            code, data, stderr = run_json(
                SCRIPTS["complexity"], f"tests/complexity_{stem}.json"
            )
            ok = code == 0 and data.get("risk_score") == score
            report.check(ok, f"example:complexity_{stem}", stderr.strip() or repr(data))
            evidence[f"complexity_{stem}.stdout.json"] = data
        except (OSError, RuntimeError) as exc:
            report.check(False, f"example:complexity_{stem}", str(exc))

    try:
        output_dir = work / "srt_sample"
        code, data, stderr = run_json(
            SCRIPTS["srt"],
            "tests/sample_short.srt",
            "--out-dir",
            str(output_dir),
            "--block-seconds",
            "18",
        )
        expected_names = (
            "sample_short.timeline.jsonl",
            "sample_short.timeline.md",
            "sample_short.srt_index.md",
        )
        files_exist = all((output_dir / name).is_file() for name in expected_names)
        ok = code == 0 and data.get("caption_count") == 4 and data.get("segment_count") == 2 and files_exist
        report.check(ok, "example:build_srt_index", stderr.strip() or repr(data))
        evidence_data = dict(data)
        evidence_data["outputs"] = {
            "timeline_jsonl": "test_logs/srt_sample/sample_short.timeline.jsonl",
            "timeline_md": "test_logs/srt_sample/sample_short.timeline.md",
            "srt_index_md": "test_logs/srt_sample/sample_short.srt_index.md",
        }
        evidence["build_srt_index.stdout.json"] = evidence_data
        if files_exist:
            srt_files = {name: (output_dir / name).read_bytes() for name in expected_names}
            index_text = load_utf8(output_dir / "sample_short.srt_index.md")
            verify = {
                "contains_expected_chinese": "今天我们先看舞台活动策划里的核心问题" in index_text,
                "contains_mojibake_marker": "\ufffd" in index_text,
                "path": "test_logs/srt_sample/sample_short.srt_index.md",
            }
            report.check(
                verify["contains_expected_chinese"] and not verify["contains_mojibake_marker"],
                "example:srt_utf8_content",
            )
            evidence["verify_srt_utf8.stdout.json"] = verify
    except (OSError, RuntimeError, UnicodeError, ValueError) as exc:
        report.check(False, "example:build_srt_index", str(exc))

    return evidence, srt_files


def parse_frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("missing opening ---")
    try:
        end = next(index for index in range(1, len(lines)) if lines[index].strip() == "---")
    except StopIteration as exc:
        raise ValueError("missing closing ---") from exc
    values: dict[str, str] = {}
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line[:1].isspace() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip("\"'")
    return values


def parse_minimal_openai_yaml(text: str) -> tuple[dict[str, str], dict[str, str]]:
    sections: dict[str, dict[str, str]] = {}
    current: str | None = None
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        if "\t" in raw_line:
            raise ValueError("tabs are not allowed in the minimal YAML subset")
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        if indent == 0 and raw_line.rstrip().endswith(":"):
            current = raw_line.strip()[:-1]
            if current in sections:
                raise ValueError(f"duplicate section: {current}")
            sections[current] = {}
            continue
        if indent == 2 and current and ":" in raw_line:
            key, raw_value = raw_line.strip().split(":", 1)
            key = key.strip()
            raw_value = raw_value.strip()
            if key in sections[current]:
                raise ValueError(f"duplicate key in {current}: {key}")
            if current == "interface":
                try:
                    value = json.loads(raw_value)
                except json.JSONDecodeError as exc:
                    raise ValueError(f"{current}.{key} must be a double-quoted string") from exc
                if not isinstance(value, str) or not value:
                    raise ValueError(f"{current}.{key} must be a non-empty string")
            elif current == "policy" and key == "allow_implicit_invocation":
                if raw_value != "false":
                    raise ValueError("policy.allow_implicit_invocation must be the boolean false")
                value = raw_value
            else:
                raise ValueError(f"unsupported field: {current}.{key}")
            sections[current][key] = value
            continue
        raise ValueError(f"unsupported or top-level scalar line: {raw_line!r}")
    if set(sections) != {"interface", "policy"}:
        raise ValueError(f"expected only interface/policy sections, got {sorted(sections)}")
    return sections["interface"], sections["policy"]


def check_skill_contracts(report: Report) -> None:
    actual = {path.name for path in ROOT.glob("stage-*") if path.is_dir()}
    expected = set(SKILL_DIRS)
    report.check(actual == expected, "contract:six_skill_directories", f"expected {sorted(expected)}, got {sorted(actual)}")

    for dirname in SKILL_DIRS:
        directory = ROOT / dirname
        skill = directory / "SKILL.md"
        metadata = directory / "agents" / "openai.yaml"
        try:
            values = parse_frontmatter(load_utf8(skill))
            ok = values.get("name") == dirname and bool(values.get("description"))
            report.check(ok, f"contract:frontmatter:{dirname}", repr(values))
        except (OSError, UnicodeError, ValueError) as exc:
            report.check(False, f"contract:frontmatter:{dirname}", str(exc))
        try:
            interface, policy = parse_minimal_openai_yaml(load_utf8(metadata))
            required = {"display_name", "short_description", "default_prompt"}
            ok = set(interface) == required and all(interface.get(key) for key in required)
            ok = ok and set(policy) == {"allow_implicit_invocation"}
            ok = ok and policy.get("allow_implicit_invocation", "").lower() == "false"
            report.check(ok, f"contract:openai_yaml:{dirname}", f"interface={interface!r}, policy={policy!r}")
        except (OSError, UnicodeError, ValueError) as exc:
            report.check(False, f"contract:openai_yaml:{dirname}", str(exc))


def check_progressive_reading_contracts(report: Report) -> None:
    """Keep stage entrypoints progressive instead of eagerly loading the tree."""
    protocol = ROOT / "_shared" / "progressive-reading-protocol.md"
    try:
        protocol_text = load_utf8(protocol)
        protocol_markers = (
            "## 四层来源",
            "## 单步扩展循环",
            "## 快速确认",
            "## 停止规则",
            "这不是可持久化状态、Schema 或统一工作流字段",
            "每次只扩展一个",
            "阶段边界",
        )
        missing = [marker for marker in protocol_markers if marker not in protocol_text]
        report.check(
            not missing,
            "reading:shared_progressive_protocol",
            f"missing={missing}",
        )
    except (OSError, UnicodeError, ValueError) as exc:
        report.check(False, "reading:shared_progressive_protocol", str(exc))

    required_sections = (
        "## 渐进式读取",
        "### 必读",
        "### 按需读取路由",
        "### 快速确认",
        "### 停止规则",
    )
    eager_phrases = (
        "Read shared control first",
        "Read shared control and",
        "先读共享总控",
        "Read `<项目根目录>\\_shared\\course-visual-production-v2.7.md` first",
    )
    stage_boundaries = {
        "stage-sline-srt-media-routing": "不得自动读取或执行 A线",
        "stage-aline-course-visual-routing": "不自动读取 B/T/C",
        "stage-bline-production-handoff": "不自动进入 T线",
        "stage-tline-prompt-translation": "不读取 C线",
        "stage-cline-gpt-image-execution-feedback": "不触发 A/B/T 全链重读",
        "stage-algorithm-lite-companion": "不继续读取生产规则",
    }
    for dirname in SKILL_DIRS:
        path = ROOT / dirname / "SKILL.md"
        try:
            text = load_utf8(path)
            missing = [section for section in required_sections if section not in text]
            eager = [phrase for phrase in eager_phrases if phrase in text]
            has_stop_signal = any(
                marker in text
                for marker in ("阶段边界", "不自动", "停止读取", "立即执行", "立即回到调用阶段")
            )
            has_single_step = "一次只允许由当前唯一未决问题触发一个来源" in text
            has_stage_boundary = stage_boundaries[dirname] in text
            report.check(
                not missing and not eager and has_stop_signal and has_single_step and has_stage_boundary,
                f"reading:progressive_entrypoint:{dirname}",
                f"missing={missing}, eager={eager}, has_stop_signal={has_stop_signal}, "
                f"has_single_step={has_single_step}, has_stage_boundary={has_stage_boundary}",
            )
        except (OSError, UnicodeError, ValueError) as exc:
            report.check(False, f"reading:progressive_entrypoint:{dirname}", str(exc))


def check_reference_remotion_contracts(report: Report) -> None:
    """Validate reference-locked full-page and Remotion handoff invariants."""
    fixture = ROOT / "tests" / "reference_remotion_contract_cases.json"
    try:
        data = json.loads(load_utf8(fixture))
        cases = {case["id"]: case for case in data.get("cases", [])}
        required_ids = {
            "reference_locked_full_page",
            "flattened_png_requires_gate",
            "remotion_transparent_foreground",
            "split_layers_require_second_gate",
        }
        report.check(
            data.get("schema_version") == 1 and set(cases) == required_ids,
            "contract:reference_remotion_fixture",
            f"cases={sorted(cases)}",
        )

        full_page = cases["reference_locked_full_page"]["expected"]
        full_page_ok = (
            full_page.get("page_type") == "A16_既有母版套新内容型"
            and full_page.get("candidate_policy") == "reference_locked_single_candidate"
            and full_page.get("output_target") == "full_page_with_text"
            and full_page.get("text_generation_strategy") == "带字"
            and full_page.get("reference_attachment_required") is True
            and full_page.get("text_only_execution_forbidden") is True
            and full_page.get("maximum_local_text_revisions") == 2
            and full_page.get("deterministic_text_overlay_forbidden") is True
        )
        report.check(full_page_ok, "contract:reference_locked_full_page_case", repr(full_page))

        fallback = cases["flattened_png_requires_gate"]["expected"]
        fallback_ok = (
            fallback.get("fidelity_level") == "strong_visual_lock"
            and fallback.get("user_confirmation") == "pending"
            and fallback.get("pixel_identity_claim") is False
        )
        report.check(fallback_ok, "contract:flattened_png_gate_case", repr(fallback))

        alpha = cases["remotion_transparent_foreground"]["expected"]
        alpha_ok = (
            alpha.get("derived_from_confirmed_final") is True
            and alpha.get("background") == "transparent"
            and alpha.get("format") == "png"
            and alpha.get("alpha_required") is True
            and alpha.get("opaque_fallback_forbidden") is True
            and alpha.get("coordinate_origin") == "top_left"
            and alpha.get("crop_to_content_forbidden") is True
            and alpha.get("maximum_local_alpha_revisions") == 2
        )
        report.check(alpha_ok, "contract:remotion_alpha_case", repr(alpha))

        split = cases["split_layers_require_second_gate"]["expected"]
        split_ok = (
            split.get("second_user_gate_required") is True
            and split.get("full_canvas_required") is True
            and split.get("coordinate_origin") == "top_left"
            and split.get("crop_to_content_forbidden") is True
        )
        report.check(split_ok, "contract:remotion_split_gate_case", repr(split))
    except (OSError, UnicodeError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        report.check(False, "contract:reference_remotion_fixture", str(exc))

    contract_files = {
        ROOT / "_shared" / "reference-image-inheritance-rules.md": (
            "固定外层母版", "失败诊断图", "非哈希参考清单", "A16_既有母版套新内容型"
        ),
        ROOT / "_shared" / "remotion-asset-handoff-rules.md": (
            "transparent_foreground_gate:", "final_course_visual", "opaque", "split_layer_pending_gate"
        ),
        ROOT / "stage-bline-production-handoff" / "templates" / "b_line_production_card.md": (
            "reference_locked_single_candidate", "方案A_参考锁定版", "must_show_text_verbatim:"
        ),
        ROOT / "stage-tline-prompt-translation" / "templates" / "t_line_gpt_image_prompt.md": (
            "reference_inputs:", "text_only_execution_forbidden", "maximum_local_text_revisions: 2"
        ),
        ROOT / "stage-cline-gpt-image-execution-feedback" / "templates" / "c_line_feedback_card.md": (
            "reference_paths_actually_attached:", "full_page_candidate", "alpha_generation_failure"
        ),
    }
    for path, markers in contract_files.items():
        try:
            text = load_utf8(path)
            missing = [marker for marker in markers if marker not in text]
            report.check(
                not missing,
                f"contract:reference_remotion_markers:{path.parent.name}/{path.name}",
                f"missing={missing}",
            )
        except (OSError, UnicodeError, ValueError) as exc:
            report.check(False, f"contract:reference_remotion_markers:{path.name}", str(exc))


def iter_active_text_files():
    roots = [ROOT / "scripts", ROOT / "_shared"]
    roots.extend(ROOT / name for name in SKILL_DIRS)
    legacy = ROOT / "legacy"
    for base in roots:
        if not base.exists():
            continue
        for path in base.rglob("*"):
            if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
                continue
            if legacy in path.parents:
                continue
            yield path
    for pattern in ("*.drawio", "*.drawio.svg"):
        yield from (path for path in ROOT.glob(pattern) if path.is_file())


def check_active_contract_text(report: Report) -> None:
    old_root = re.compile(r"d:(?:\\+|/+)codex(?:\\+|/+)skills-v2\.7", re.IGNORECASE)
    hardcoded: list[str] = []
    for path in iter_active_text_files():
        try:
            text = load_utf8(path)
        except (OSError, UnicodeError, ValueError):
            continue  # The repository-wide encoding check reports this separately.
        if old_root.search(text):
            hardcoded.append(str(path.relative_to(ROOT)))
    report.check(not hardcoded, "contract:no_hardcoded_legacy_root", ", ".join(hardcoded))

    old_c_entry = "stage-cline-image2-execution-feedback"
    stale_c_entry: list[str] = []
    for path in iter_active_text_files():
        try:
            if old_c_entry in load_utf8(path):
                stale_c_entry.append(str(path.relative_to(ROOT)))
        except (OSError, UnicodeError, ValueError):
            continue
    report.check(
        not stale_c_entry,
        "contract:no_active_legacy_c_line_entry",
        ", ".join(stale_c_entry),
    )

    old_default = re.compile(
        r"three[ -]platform|\u4e09\u5e73\u53f0|\u5373\u68a6|nanobanana|image\s*2[- ]first|image2[- ]first|image2 english|\bimage2\b",
        re.IGNORECASE,
    )
    stale: list[str] = []
    for path in iter_active_text_files():
        try:
            if old_default.search(load_utf8(path)):
                stale.append(str(path.relative_to(ROOT)))
        except (OSError, UnicodeError, ValueError):
            continue
    report.check(not stale, "contract:no_active_legacy_platform_mode", ", ".join(stale))

    prompt_template = ROOT / "stage-tline-prompt-translation" / "templates" / "t_line_gpt_image_prompt.md"
    try:
        prompt_text = load_utf8(prompt_template)
        required_fields = (
            "目标能力: GPT Image",
            "请求模型: gpt-image-2",
            "实际执行模型:",
            "中文执行提示词:",
            "中文负面约束:",
            "输出设置:",
            "中文局部修改模板:",
            "保留项:",
            "仅修改项:",
            "禁止修改项:",
            "最小修改指令:",
        )
        legacy_fields = (
            "image2_en:",
            "full_prompt:",
            "short_execution_prompt:",
            "negative_prompt:",
            "revision_prompt_template:",
        )
        missing = [field for field in required_fields if field not in prompt_text]
        forbidden = [field for field in legacy_fields if field in prompt_text]
        report.check(
            not missing and not forbidden,
            "contract:gpt_image_chinese_prompt_template",
            f"missing={missing}, forbidden={forbidden}",
        )
    except (OSError, UnicodeError, ValueError) as exc:
        report.check(False, "contract:gpt_image_chinese_prompt_template", str(exc))


def check_encoding(report: Report) -> None:
    bad: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            load_utf8(path)
        except (OSError, UnicodeError, ValueError) as exc:
            bad.append(f"{path.relative_to(ROOT)} ({exc})")
    report.check(not bad, "encoding:all_text_utf8_not_utf16", "; ".join(bad))

    bad_logs: list[str] = []
    log_dir = ROOT / "test_logs"
    for path in log_dir.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        try:
            raw = path.read_bytes()
            load_utf8(path)
            if raw.startswith(b"\xef\xbb\xbf"):
                raise ValueError("UTF-8 BOM found; evidence must be UTF-8 without BOM")
            if path.name.endswith(".stdout.json"):
                json.loads(raw.decode("utf-8"))
            if b"\r" in raw:
                raise ValueError("CR byte found; expected LF line endings")
        except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as exc:
            bad_logs.append(f"{path.name} ({exc})")
    report.check(not bad_logs, "encoding:test_logs_utf8_no_bom_lf", "; ".join(bad_logs))


def check_legacy_archive(report: Report) -> None:
    legacy = ROOT / "legacy" / "platform-prompts-v2.7.0"
    report.check(legacy.is_dir(), "legacy:platform_prompt_archive_exists", str(legacy))
    readme = legacy / "README.md"
    try:
        text = load_utf8(readme)
        report.check(bool(text.strip()), "legacy:archive_readme", "README.md is empty")
    except (OSError, UnicodeError, ValueError) as exc:
        report.check(False, "legacy:archive_readme", str(exc))


def update_evidence(evidence: dict[str, object], srt_files: dict[str, bytes]) -> None:
    log_dir = ROOT / "test_logs"
    for name, value in sorted(evidence.items()):
        write_json_lf(log_dir / name, value)
    output_dir = log_dir / "srt_sample"
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, data in sorted(srt_files.items()):
        normalized = data.removeprefix(b"\xef\xbb\xbf").replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        text = normalized.decode("utf-8")
        text = "\n".join(line.rstrip() for line in text.split("\n"))
        (output_dir / name).write_text(text, encoding="utf-8", newline="\n")


def check_checked_in_evidence(
    report: Report,
    evidence: dict[str, object],
    srt_files: dict[str, bytes],
) -> None:
    mismatches: list[str] = []
    log_dir = ROOT / "test_logs"
    for name, value in sorted(evidence.items()):
        expected = (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
        path = log_dir / name
        if not path.is_file() or path.read_bytes() != expected:
            mismatches.append(name)
    for name, data in sorted(srt_files.items()):
        normalized = data.removeprefix(b"\xef\xbb\xbf").replace(b"\r\n", b"\n").replace(b"\r", b"\n")
        text = normalized.decode("utf-8")
        expected = "\n".join(line.rstrip() for line in text.split("\n")).encode("utf-8")
        path = log_dir / "srt_sample" / name
        if not path.is_file() or path.read_bytes() != expected:
            mismatches.append(f"srt_sample/{name}")
    report.check(
        not mismatches,
        "evidence:checked_in_matches_fresh_run",
        ", ".join(mismatches),
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the V2.7.1 offline development-baseline checks.")
    parser.add_argument(
        "--update-evidence",
        action="store_true",
        help="replace test_logs only after every check succeeds (default: read-only)",
    )
    args = parser.parse_args()

    report = Report()
    check_script_syntax(report)
    work_dir = ROOT / ".run_all_checks_tmp"
    if work_dir.exists():
        shutil.rmtree(work_dir)
    work_dir.mkdir(parents=True, exist_ok=False)
    try:
        evidence, srt_files = check_algorithm_examples(report, work_dir)
    finally:
        if work_dir.exists():
            shutil.rmtree(work_dir)
    check_skill_contracts(report)
    check_progressive_reading_contracts(report)
    check_reference_remotion_contracts(report)
    check_active_contract_text(report)
    check_encoding(report)
    check_legacy_archive(report)

    if not args.update_evidence:
        check_checked_in_evidence(report, evidence, srt_files)

    if report.failures:
        print(f"\nFAILED: {len(report.failures)} failure(s), {len(report.passes)} pass(es).")
        return 1
    if args.update_evidence:
        update_evidence(evidence, srt_files)
        print("[UPDATED] test_logs evidence (UTF-8 without BOM, LF).")
        check_checked_in_evidence(report, evidence, srt_files)
        if report.failures:
            print(f"\nFAILED: {len(report.failures)} failure(s), {len(report.passes)} pass(es).")
            return 1
    print(f"\nPASSED: {len(report.passes)} check(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
