# B-Line Page Brief — B区

> 本模板追加到A已明确分页并完成当前版本内部复核的同一页面简报；不要求独立A审通过。只填写一份主执行方案。代表页可在必填项完整后进入一次校准执行；其他成员必须等代表页获人工确认并冻结批次后才能进入 C线。

```yaml
status: B线可执行设计
source_page_brief:
  brief_id:
  original_course_order:
  a_pagination_plan_reference: # 现有A方案路径/版本；不复制其教学分析
  internal_review_reference: # 当前方案internal_review记录，不是独立审者

pagination_ref:
  plan_id:
  plan_version:
  page_id:
  owned_spans: [] # 与A计划逐项一致；每项source_id/line/start_char/end_char/start_text/end_text
pagination_feedback: [] # 无问题为空；涉及分页时提供实际证据并交A，不自行改页界

implementation_evidence:
  asset_used:
    - reference_id:
      real_path:
      file_name:
      dimensions:
      template_version:
      reference_role: outer_shell / title_anchor / content_container / layout_evidence / content_material / success_evidence / failure_evidence / model_capability_evidence
      user_confirmation: pending / confirmed / not_required
  excluded_assets_and_reason:
  what_it_proves:  # 分清真实外壳、局部结构、内容资产和已观察成功能力
  what_it_does_not_prove:  # PNG非参数模板；静态样张不证明动态/跨次稳定性
  highest_risk:  # 完整设计可待首轮校准，效果未验证不等于设计空白
  representative_calibration_required: yes / no
  calibration_reason:
  calibration_covered_by_representative_page: not_applicable

main_execution_plan:
  plan_id:
  outer_template:
    identity:
    description:
    evidence_reference_id:
  content_container:
  semantic_visual_carrier:
  main_visual_description:  # 当前执行状态的完整主视觉，全页其他状态去向明确
  reading_order:  # 落实A状态分配、先后/并现、全部必呈项逐字映射及当前执行状态
  first_visual_focus:
  visual_space_rationale:
  text_realization_strategy:  # 各状态文字去向明确，不以“动画稍后再补”掩盖设计空白
  reference_mapping:
  must_show_text_verbatim:  # 当前图准确文字子集；全部A必呈项在既有状态说明中完整映射
  must_preserve:
  allowed_to_change:
  open_for_calibration:  # 非核心微观细节/未验证效果，不得留空主视觉或核心决策
  hard_bans:
  technical_output_spec:
    dimensions:
    file_format:
    transparency_requirement:

skeleton_inheritance:
  decision: inherit_local_skeleton / no_inheritance
  source_page: not_applicable
  same_teaching_relation_reason: not_applicable
  inherited_parts: not_applicable
  required_changes: not_applicable
  validation_note:

batch_assignment:
  batch_id:
  member_original_course_orders:
  shared_outer_template_basis:
  shared_teaching_relation_basis:
  shared_semantic_visual_carrier_basis:
  shared_reference_and_generation_basis:
  within_batch_required_differences:
  representative_page:
  representative_selection_reason:
  independent_C_context_required: yes
  include_other_batches_context: no
  include_previous_page_output_by_default: no
  final_assembly_order: use_original_course_order

batch_calibration:
  state: calibrating / representative_generated / representative_confirmed / frozen_for_execution
  non_representative_pages: blocked_until_representative_confirmed / released
  human_confirmation: pending / confirmed
  confirmation_record:
  frozen_batch_core:

qualitative_visual_checks:
  image_has_teaching_task: pass / fail
  primary_focus_matches_learning_goal: pass / fail
  text_and_reading_order_clear: pass / fail
  teaching_relation_recognizable: pass / fail
  background_and_decoration_non_competing: pass / fail
  required_information_has_space: pass / fail

C_adapter_handoff:
  readiness: ready_for_representative_calibration / ready_for_C / not_ready_for_C
  selected_reference_paths:
  preserve_items:
  change_items:
  unresolved_blockers:
```

## 填写约束

- 每批都必须校准并人工确认一张代表页。代表页的 `representative_calibration_required` 必须为 `yes`；非代表页只有明确填写本批 `calibration_covered_by_representative_page` 时才可为 `no`。
- `decision: inherit_local_skeleton` 时，来源页、教学关系相同原因、继承项、必须变化项全部必填；“效果好/同课程/同章节/保持统一”不合格。
- `outer_template.identity`、`outer_template.description` 或 `main_visual_description` 为空时必须停止；C线不得补写母版或主视觉。
- 不填写图片百分比、固定占比区间或预设批次数量。
- `ready_for_representative_calibration` 只允许代表页在 `calibrating + pending` 时使用，且仅满足一次代表页校准的交接前提，仍需该页明确生图授权；其他成员仍为阻塞。
- `ready_for_C` 只允许出现在 `frozen_for_execution + confirmed` 且无空必填字段的记录中。
- 无匹配成功案例不阻塞B内容驱动设计，不要求用户补模板；明确无外部资产的机器写法为 `implementation_evidence.asset_used: []`、`outer_template.evidence_reference_id: no_external_asset`、`selected_reference_paths: []`，既有 `identity`/`description` 及证据说明理由，主视觉仍完整。C对应 `template_identity.evidence_reference_id`/`master_asset_path` 均为 `no_external_asset`、`master_asset_exists_and_readable: no`、编译references/实际附件空，未执行不虚填回执；不得用此token掩盖声明资产缺失，参考锁定任务仍须真实主参考。成熟复用省重复实现，不省A判断；校准和授权不豁免。
- B必须写完整主视觉、核心结构、阅读顺序和文字安排；首轮未验证效果写在现有证据/开放项，以完整主方案进入代表页校准，不把核心决策交给C。静态样张不证明动态效果，失败可留B调整结构，涉及分页/教学则附证据回A。
- 页面、页内状态与镜头不自动一一对应，必呈不等于全时同屏。状态分配写现有 `reading_order`，不增加schema；旧记录不自动重释为已验证动态设计。当前状态不明时先由B澄清，新增状态图也不自动获得授权。
- `reading_order`/`text_realization_strategy`/`main_visual_description` 合起来覆盖当前执行状态、其他状态去向、全部A必呈项逐字映射和观察顺序；`must_show_text_verbatim` 仅当前图文字。单张通过不释放未验证状态，也不冒称整页媒体/批次已通过；输出可用页ID加状态后缀，不改page_id。

## 批次与校准填写说明

- `batch_assignment` 四项共同依据须逐项可核对；非相邻页机制接近可同批，同章节但机制不同须拆批。同批同一 C对话连续执行，跨批隔离；`independent_C_context_required` 指批次之间的隔离，不要求同批逐页新开对话。
- `frozen_batch_core` 由 B在代表页实际通过后维护固定共同项；`within_batch_required_differences` 与各页 `allowed_to_change` 保留本页对象、数值、文字、图片及必要区别。改变共同机制则拆批/回 B，不能滚动把上一张结果升级为基准。
- `confirmation_record` 引用实际确认的来源、版本/日期、适用范围及能力边界。代表页应覆盖典型关系与密度，确认仅满足展开前提，`released`/`ready_for_C` 均不等于其余页已获首轮生图授权，不自动定稿或授权代表图继承。
- `qualitative_visual_checks` 只记录 B方案可行性判断；实际图像逐图验收及批后横向检查留在 C现有反馈，不能用本组字段冒称成图通过。
