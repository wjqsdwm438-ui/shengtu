# Algorithm Lite Rules

Algorithms are lightweight rule aids only. They do not train models, install dependencies, run ML, or override user explicit requirements or frozen items.

## ALG-S01_字幕语义段合并与媒介分流
Input: SRT timecodes, subtitle lines, script paragraphs, teaching cues.
Logic: merge adjacent subtitle lines by same teaching function, same object, and continuous meaning; do not split every subtitle sentence into a page. Route to S01-S08 by media need.
Output: source locator, segment_time_metadata and media disposition as optional input assistance within A (or explicit S-only request); not a page plan, fixed page identity or mandatory separate gate.

## ALG-A01_教学关系与语义载体检查
Input: A-admitted source evidence and explicit pagination analysis, teaching goal/relation, must-show items, visual teaching task, and approved material constraints; independent S is not required.
Logic: verify that the stated teaching relation and visual task are supported by the source. It may suggest a semantic carrier but must not choose an inner layout, template variation, image proportion, or legacy A01-A21 page type. Prevent mechanical mappings such as comparison=two columns, three types=three cards, no-text=empty background.
Output: teaching_relation_evidence, semantic_carrier_suggestion, unsupported_assumptions, risk, Gate suggestion. Legacy A01-A21 labels are migration metadata only and cannot freeze design.

## ALG-A02_文字预算与版式区域校验
Input: the current actual display state's planned on-screen text, not the whole voiceover or all sequential states combined; teaching relation, text accuracy need and A/B state allocation.
Logic: use character counts and any existing script risk bands only as descriptive diagnostics, never as a fixed pagination limit, automatic split, approval condition or new user Gate. Capacity also includes necessary diagrams, observation order and actual material limits, not only font size or text fit. Validate workable title, body, visual-carrier, information and safe regions; these are qualitative responsibilities, not fixed image-area percentages.
Output: text_budget_level, risk and evidence-only recommendations. A/B decide whether the actual content requires changes; required terms/data/text cannot be silently compressed or removed, and pagination issues return to A.

## ALG-A03_页面复杂度与版式风险轻量评分
Input: on-screen text count, visual object count, info layers, reference image count/conflict, material retention need, text generation risk.
Logic: describe overload, PPT risk, reference pollution risk, post-edit burden and sample failure risk. Any existing numeric score is a diagnostic signal, not evidence of teaching quality, a business threshold or an automatic Gate.
Output: existing risk_score and risk_items with evidence-only interpretation; any pass/return/manual-confirm suggestion is advisory and cannot replace A/B responsibility or create user confirmation work.

## ALG-B01_生产可行性证据检查
Input: shared page brief A-section, B-line single primary plan, actual template/reference paths, realization evidence, batch contract, text budget, and material policy.
Logic: verify what each real asset proves and does not prove, the highest implementation risk, representative-page calibration need, and any skeleton-reuse teaching-relation proof. Do not manufacture a score or approve a design whose A-section cannot be preserved.
Output: evidence gaps, pass_to_C_adapter true/false, required_fix, return-A/return-B/manual-confirm suggestion.

## ALG-C01_失败类型分类器
Input: generated visual sample or user feedback, frozen A/B basis, compiled C-adapter contract, local revision request.
Logic: classify content, structure, aesthetic, text, material, inheritance, scope, or model-boundary failure.
Output: failure_type, keep_items, change_only_items, forbidden_changes, minimal_revision_prompt, pass/local-fix/return-B/return-A suggestion.
