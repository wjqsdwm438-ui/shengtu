# Algorithm Lite Rules

Algorithms are lightweight rule aids only. They do not train models, install dependencies, run ML, or override user explicit requirements or frozen items.

## ALG-S01_字幕语义段合并与媒介分流
Input: SRT timecodes, subtitle lines, script paragraphs, teaching cues.
Logic: merge adjacent subtitle lines by same teaching function, same object, and continuous meaning; do not split every subtitle sentence into a page. Route to S01-S08 by media need.
Output: segment_id, segment_time_metadata, semantic summary, S-route, enter_A_line true/false, reason, pass/return/manual-confirm suggestion.

## ALG-A01_教学关系与语义载体检查
Input: S-line S07 segment, teaching goal, teaching relation, must-show items, visual teaching task, material/reference needs.
Logic: verify that the stated teaching relation and visual task are supported by the source. It may suggest a semantic carrier but must not choose an inner layout, template variation, image proportion, or legacy A01-A21 page type. Prevent mechanical mappings such as comparison=two columns, three types=three cards, no-text=empty background.
Output: teaching_relation_evidence, semantic_carrier_suggestion, unsupported_assumptions, risk, Gate suggestion. Legacy A01-A21 labels are migration metadata only and cannot freeze design.

## ALG-A02_文字预算与版式区域校验
Input: planned on-screen text only, not voiceover; teaching relation; text accuracy need.
Logic: <=60 low risk, 61-120 medium, 121-180 high but sample allowed, >180 enters original-keypoint-onscreen dynamic Gate. Validate that the plan reserves workable title, body, visual-carrier, information, and safe regions; these regions are qualitative responsibilities and must not be converted into fixed image-area percentages.
Output: text_budget_level, risk, compress/split/post-edit/no-text recommendation.

## ALG-A03_页面复杂度与版式风险轻量评分
Input: on-screen text count, visual object count, info layers, reference image count/conflict, material retention need, text generation risk.
Logic: score overload, PPT risk, reference pollution risk, post-edit burden, and sample failure risk.
Output: risk_score 0-100, risk_items, pass/return/manual-confirm suggestion.

## ALG-B01_生产可行性证据检查
Input: shared page brief A-section, B-line single primary plan, actual template/reference paths, realization evidence, batch contract, text budget, and material policy.
Logic: verify what each real asset proves and does not prove, the highest implementation risk, representative-page calibration need, and any skeleton-reuse teaching-relation proof. Do not manufacture a score or approve a design whose A-section cannot be preserved.
Output: evidence gaps, pass_to_C_adapter true/false, required_fix, return-A/return-B/manual-confirm suggestion.

## ALG-C01_失败类型分类器
Input: generated visual sample or user feedback, frozen A/B basis, compiled C-adapter contract, local revision request.
Logic: classify content, structure, aesthetic, text, material, inheritance, scope, or model-boundary failure.
Output: failure_type, keep_items, change_only_items, forbidden_changes, minimal_revision_prompt, pass/local-fix/return-B/return-A suggestion.
