# Algorithm Lite Rules

Algorithms are lightweight rule aids only. They do not train models, install dependencies, run ML, or override user explicit requirements or frozen items.

## ALG-S01_字幕语义段合并与媒介分流
Input: SRT timecodes, subtitle lines, script paragraphs, teaching cues.
Logic: merge adjacent subtitle lines by same teaching function, same object, and continuous meaning; do not split every subtitle sentence into a page. Route to S01-S08 by media need.
Output: segment_id, segment_time_metadata, semantic summary, S-route, enter_A_line true/false, reason, pass/return/manual-confirm suggestion.

## ALG-A01_页面类型匹配
Input: S-line S07 segment, teaching function, text budget, material/reference needs.
Logic: recommend one A01-A21 type; explain why adjacent types are not selected; prevent mechanical mappings such as comparison=two columns, three types=three cards, no-text=empty background.
Output: recommended_page_type, reasons, rejected_adjacent_types, carrier, risk, Gate suggestion.

## ALG-A02_文字预算与无字版式骨架校验
Input: planned on-screen text only, not voiceover; page type; text accuracy need.
Logic: <=60 low risk, 61-120 medium, 121-180 high but sample allowed, >180 enters original-keypoint-onscreen dynamic Gate. Validate A01 has title/body/image/info regions, not empty background.
Output: text_budget_level, risk, compress/split/post-edit/no-text recommendation.

## ALG-A03_页面复杂度与版式风险轻量评分
Input: on-screen text count, image count, info layers, reference image count/conflict, material retention need, text generation risk.
Logic: score overload, PPT risk, reference pollution risk, post-edit burden, and sample failure risk.
Output: risk_score 0-100, risk_items, pass/return/manual-confirm suggestion.

## ALG-B01_生产可行性评分
Input: A-line frozen handoff,方案A/方案B draft, reference rules, text budget, material policy.
Logic: score aesthetic tone, learning task, student load, media division, text controllability, material preservation, and failure risk. Do not pass if frozen items cannot be preserved.
Output: candidate_score, pass_to_T_line true/false, required_fix, risk notes.

## ALG-C01_失败类型分类器
Input: generated visual sample or user feedback, B/T frozen basis, local revision request.
Logic: classify content, structure, aesthetic, text, material, inheritance, scope, or model-boundary failure.
Output: failure_type, keep_items, change_only_items, forbidden_changes, minimal_revision_prompt, pass/local-fix/return-B/return-A suggestion.
