#!/usr/bin/env python3
"""Score page complexity risk for ALG-A03 evidence."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def clamp(value: int) -> int:
    return max(0, min(100, value))


def main() -> int:
    parser = argparse.ArgumentParser(description="Score V2.7 page complexity and layout risk.")
    parser.add_argument("input_json", type=Path)
    args = parser.parse_args()
    data = json.loads(args.input_json.read_text(encoding="utf-8-sig"))

    text_count = int(data.get("on_screen_text_chars", 0))
    image_count = int(data.get("image_count", 0))
    info_layers = int(data.get("info_layer_count", 0))
    reference_count = int(data.get("reference_image_count", 0))
    reference_conflict = bool(data.get("reference_conflict", False))
    material_retention = bool(data.get("material_retention_need", False))
    text_generation_risk = str(data.get("text_generation_risk", "low")).lower()

    score = 0
    risk_items = []
    if text_count > 180:
        score += 35; risk_items.append("on_screen_text_over_180_gate")
    elif text_count > 120:
        score += 22; risk_items.append("high_text_budget")
    elif text_count > 60:
        score += 10; risk_items.append("medium_text_budget")
    if image_count > 4:
        score += 20; risk_items.append("too_many_images")
    elif image_count > 2:
        score += 10; risk_items.append("multi_image_load")
    if info_layers > 3:
        score += 15; risk_items.append("too_many_info_layers")
    elif info_layers > 1:
        score += 7; risk_items.append("multi_info_layer")
    if reference_count > 1:
        score += 10; risk_items.append("multi_reference_pollution_risk")
    if reference_conflict:
        score += 18; risk_items.append("reference_conflict")
    if material_retention:
        score += 10; risk_items.append("material_retention_constraints")
    if text_generation_risk == "high":
        score += 18; risk_items.append("high_text_generation_risk")
    elif text_generation_risk == "medium":
        score += 8; risk_items.append("medium_text_generation_risk")

    score = clamp(score)
    if score >= 70:
        suggestion = "manual_confirm_or_return_A_line"
    elif score >= 40:
        suggestion = "high_attention_before_B_line"
    else:
        suggestion = "pass_as_recommendation"
    result = {"risk_score": score, "risk_items": risk_items, "suggestion": suggestion, "final_decision": "recommendation_only_not_a_frozen_item"}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
