# A Independent Review Report — Explicit Request Only

本文件路径兼容旧 A 审报告，**只在用户明确要求独立复核时使用**。不设置固定独立 A 审阶段、额外 Gate、自动触发条件或默认停止点。正常 A 必须自己完成的内部复核见 a_line_page_handoff_card.md 和统一 a_pagination_plan.internal_review，不能因为本报告未启用而跳过。

```yaml
review_kind: user_requested_independent_review
user_request_record:
plan_id:
plan_version:
reviewed_page_ids: []
source_and_existing_decision_refs: []
conclusion: 通过 / 局部补卡 / 退回A线
checks:
  source_roles_and_scope_preserved:
  verbatim_body_coverage_and_non_a_retained:
  exact_source_mapping_and_order:
  whole_scope_goals_relations_priorities_dependencies:
  all_boundaries_and_adjacent_merge_reviewed:
  reasonable_split_merge_alternatives_compared:
  same_screen_need_and_cross_page_continuity:
  required_text_labels_captions_capacity:
  approved_template_space_and_real_material_limits:
  necessary_visual_carrier_feasibility_and_limits:
  must_show_text_numbers_terms_source_faithful:
  required_real_material_semantic_role_preserved:
  image_task_and_forbidden_drift:
  prior_effective_decisions_and_unresolved_gates:
  no_precise_design_or_user_delegated_design_judgment:
required_fix:
return_target: A / none
```

## 使用说明

- 每项结论写可核验源定位、方案版本、页面/比较及承载证据；不以字段非空、旧 confirmed、旧九单元通过或 a_review_status 判本版通过。
- 复核整套页界、所有相邻关系、合理替代及正文覆盖，不只是单页卡片齐全。依用户请求的范围查证，不预设必须改页数；原界有证据可以保留。
- 原文、时间码、批注/媒体关联、Non-A 路由、页界/正文归属及教学关系问题统一由 A 对应职责局部修正；具体 required_fix 标明证据、责任及受影响页，不返回独立 S，不代写替代原稿。
- 原文忠实性和视觉表达一致性仍检查，不新增脚本外部真实性或实时专业审校。未核对资料如实标缺口，不把真实素材可读当作外部事实已证实。
- 不评选精细构图、尺寸、风格或图片占比；但必须核对 A 分页所需的实际承载依据，不能借“不审美”放过明显负荷/关系断裂。
- 不重问已有有效范围、参考或生产授权；关键用户专属决定缺失或有效决定冲突才问一个必要问题。报告写入仍须在已授权范围内。
- 本报告不创建/替代 a_pagination_plan 的正常内部复核，也不能以自身 conclusion 解锁生图、代表页、扩批或定稿；原 Gate 保留。
