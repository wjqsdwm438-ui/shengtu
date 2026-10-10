# C线执行适配与反馈卡

```yaml
状态: C线执行适配 / 代表页待确认 / 批量首轮执行 / 局部修改 / 已退回
页面:
  page_id:
  original_course_order:
  shared_brief_path:
批次:
  batch_id:
  production_order:
  representative_page_id:
  is_representative: yes/no
  representative_generation_authorized: pending/confirmed/not_applicable
  representative_result_confirmed: pending/confirmed/not_applicable
  batch_first_pass_authorized_pages: []
  isolated_context_id:

adapter_preflight:
  entry_mode: representative_calibration / batch_expansion / single_page
  source_evidence_complete: yes/no
  A_internal_review_complete: yes/no
  a_pagination_plan_complete: yes/no # 含当前A/B分页引用与页界一致性
  a_section_complete: yes/no
  b_section_complete: yes/no
  main_execution_plan_present: yes/no
  implementation_evidence:
    asset_used_complete: yes/no
    excluded_assets_and_reason_checked: yes/no
    what_it_proves_present: yes/no
    what_it_does_not_prove_present: yes/no
    highest_risk_present: yes/no
    representative_calibration_required_present: yes/no
    calibration_reason_checked: yes/no
    calibration_covered_by_representative_page_checked: yes/no/not_applicable
  source_batch_calibration:
    state: calibrating / representative_generated / representative_confirmed / frozen_for_execution
    human_confirmation: pending / confirmed
  source_C_adapter_handoff:
    readiness: ready_for_representative_calibration / ready_for_C / not_ready_for_C
    selected_reference_paths_match: yes/no/not_applicable
    preserve_items_present: yes/no
    change_items_present: yes/no
    unresolved_blockers_empty: yes/no
  concrete_canvas_size_present: yes/no
  main_execution_plan_outer_template:
    identity_present: yes/no
    description_present: yes/no
    evidence_reference_id_present: yes/no
  main_execution_plan_main_visual_description_present: yes/no
  declared_assets_exist_and_readable: yes/no/not_applicable
  reference_mapping_matches_attachments: yes/no/not_applicable
  unresolved_design_open_items_absent: yes/no
  placeholders_or_truncated_sentences_absent: yes/no
  contradictions_absent: yes/no
  representative_gate_passed_or_calibration_exception_valid: yes/no/not_applicable
  result: pass / stop_return_A / stop_return_B
  blocking_evidence:

skeleton_inheritance:
  decision: inherit_local_skeleton / no_inheritance
  source_page_id:
  same_teaching_relation_reason:
  same_semantic_carrier:
  inherited_parts:
  required_changes:
  validation_note:
  evidence_complete: yes/no/not_applicable

compiled_execution_contract:
  target_capability: GPT Image
  requested_model: gpt-image-2
  actual_model: 未报告
  execution_type: standard / reference_locked_full_page / remotion_transparent_foreground / remotion_split_layer
  template_identity:
    template_id:
    template_version:
    evidence_reference_id:
    master_asset_path:
    master_asset_exists_and_readable: yes/no
  realization_evidence:
    asset_proves:
    asset_does_not_prove:
    highest_execution_risk:
    representative_calibration_required: yes/no
  page_task:
    teaching_goal:
    teaching_relation:
    semantic_visual_carrier:
  preserve:
    master_and_core_skeleton:
    title_system_and_safe_area:
    must_show_text_verbatim:
    course_style:
  change_or_generate:
    permitted_region:
    subject_and_content_boundary:
  references:
    - path:
      role: primary / secondary
      must_inherit:
      must_not_inherit:
      exists_and_readable: yes/no
      actually_attached: yes/no
  context_isolation:
    entire_folder_attached: no
    previous_page_image_included: no
    previous_conversation_images_included: no
    failed_images_included: no
    other_batch_context_included: no
  technical_parameters:
    size:
    quality:
    background: opaque / transparent
    format: png / webp
    opaque_fallback: allowed / forbidden
  chinese_execution_prompt:
  chinese_negative_constraints:
  local_revision_boundary:
    preserve:
    change_only:
    forbid_change:
    minimum_instruction:

execution_record:
  prompt_version:
  generation_authorization: pending/confirmed
  reference_paths_actually_attached: []
  output_path:
  actual_model_receipt: 未报告
  visual_sample_state: visual_sample_generated / full_page_candidate / final_course_visual
  result: pass / local_fix / text_generation_failure / alpha_generation_failure / return_A / return_B

result_review:
  image_serves_teaching_task: yes/no
  focus_matches_learning_goal: yes/no
  text_complete_accurate_readable: yes/no
  information_relation_and_reading_order_clear: yes/no
  background_or_decoration_competes: yes/no
  master_and_core_skeleton_preserved: yes/no
  required_content_fits: yes/no
  mechanical_ratio_rule_used: no

local_revision:
  target_image:
  preserve:
  change_only:
  forbid_change:
  reference_basis:
  complete_executable_prompt:
  local_revision_count: 0 / 1 / 2
  requires_upstream_change: none / S / A / B
```

> 空尺寸、空母版、空主视觉、缺失已声明素材、矛盾或未决设计项必须停止，不得由 C线补设计。代表页未经人工确认，不得展开该批其他页面。

## 填写说明（不增加机器字段）

- `adapter_preflight` 同时核对真实路径、获准项目/用途/范围与实际附件；待批、禁用、未选素材即停止，缺口写 `blocking_evidence`，不能用字段 pass 冒称已核实真实批准、教学正确或审美。纯编译/注入错误留 C修正后重新检查，现有 stop_return 值只用于确需上游处理的责任。
- `批次.isolated_context_id` 标明同批共用的 C对话，跨批隔离。`context_isolation` 的历史图片项记录有无作为输入或隐式参考，不把“对话仍保留历史”误填成“历史均获准”。上一页/代表页图仅在 B明确选为本页骨架参考且继承证明完整时如实记录并附加；历史不是新指令或授权，固定基准不得滚动更新。
- `representative_result_confirmed` 只记录本批展开前提；`batch_first_pass_authorized_pages` 与 `execution_record.generation_authorization` 依据真实授权单独填写，不从代表页通过推导剩余页已授权、定稿或图像继承。共同基准只引用 B维护版。
- `execution_record` 按实际执行填附件、提示版本、输出与回执；未生成不虚填输出或成图状态，未报告模型保持“未报告”。只记录失败不自动重生成；仅本页失败且共享依据无误才继续其他已授权页，共因/影响不明先停相关依赖页并记录责任与范围。
- `result_review` 必须查看实际图像、逐图对照原文与 A/B要求，核对数字术语、关系方向、文字可读及裁切遗漏。B方案自评不是本次验收；批后共同基准检查在现有反馈正文另注明代表/边界/后续页对照、必须差异、通过/问题页及影响范围，不另造评分系统，也不替代全页检查或用户定稿。
- `local_revision` 只写获授权的目标、保留项、仅修改项与禁止项；文字首轮后最多两次局部文字修订，不能以允许次数充当修订授权。共同依据错误按最早责任回 A/B，纯执行偏差留 C；修复后只复核相关页。
