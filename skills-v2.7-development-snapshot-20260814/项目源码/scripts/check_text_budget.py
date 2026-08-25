#!/usr/bin/env python3
"""Check planned on-screen text budget for ALG-A02 evidence."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def count_chars(text: str) -> int:
    return sum(1 for ch in text if not ch.isspace())


def classify(count: int) -> dict:
    if count <= 60:
        return {"text_budget_level": "低", "risk": "low", "recommendation": "sample_allowed"}
    if count <= 120:
        return {"text_budget_level": "中", "risk": "medium", "recommendation": "sample_allowed_with_post_check"}
    if count <= 180:
        return {"text_budget_level": "高", "risk": "high", "recommendation": "visual_sample_allowed_but_post_edit_required"}
    return {"text_budget_level": "超过180", "risk": "gate", "recommendation": "user_gate_split_or_no_text_layout"}


def main() -> int:
    parser = argparse.ArgumentParser(description="Classify V2.7 on-screen text budget.")
    parser.add_argument("input", help="Text string or path to a UTF-8 text file.")
    args = parser.parse_args()
    path = Path(args.input)
    text = path.read_text(encoding="utf-8-sig") if path.exists() else args.input
    count = count_chars(text)
    result = {"char_count_no_space": count, **classify(count), "final_decision": "recommendation_only_not_a_frozen_item"}
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
