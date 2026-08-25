#!/usr/bin/env python3
"""Validate A01 light_region_summary completeness for ALG-A02 evidence."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = ["title_area", "body_area", "image_area", "info_layer", "safe_margin", "visual_text_priority", "post_text_method"]
EMPTY_HINTS = ["empty background", "pure atmosphere", "only background", "空背景", "纯氛围", "只有背景"]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def is_present(value) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, tuple, dict)):
        return bool(value)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Check A01 no-text layout skeleton light_region_summary.")
    parser.add_argument("input_json", type=Path)
    args = parser.parse_args()
    data = load_json(args.input_json)
    summary = data.get("light_region_summary", data)
    missing = [field for field in REQUIRED_FIELDS if not is_present(summary.get(field))]
    combined = json.dumps(summary, ensure_ascii=False).lower()
    empty_background_risk = any(hint in combined for hint in EMPTY_HINTS)
    pass_check = not missing and not empty_background_risk
    result = {
        "check": "A01_light_region_summary",
        "pass": pass_check,
        "missing_fields": missing,
        "empty_background_risk": empty_background_risk,
        "suggestion": "pass" if pass_check else "return_to_A_line_or_manual_confirm",
        "note": "This checks light_region_summary only; it does not restore editable_layout_spec.",
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if pass_check else 2


if __name__ == "__main__":
    raise SystemExit(main())
