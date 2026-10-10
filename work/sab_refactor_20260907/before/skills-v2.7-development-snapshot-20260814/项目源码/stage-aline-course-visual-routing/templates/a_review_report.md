# A-Review Report

```yaml
status: A审教学与事实闸口
page_id:
conclusion: 通过 / 局部补卡 / 退回A线
checks:
  s07_entry_supported:
  teaching_goal_supported_by_source:
  teaching_relation_clear_and_directionally_correct:
  must_show_text_complete_and_exact:
  numbers_and_terms_verified:
  required_real_materials_complete:
  image_task_serves_teaching_goal:
  forbidden_semantic_drift_complete:
  unresolved_semantic_gate_closed:
  no_layout_or_ratio_decision_in_A:
  no_aesthetic_option_selection_in_A:
required_fix:
return_target: S / A / none
```

A 审不评选配色、构图、模板、图片占比、页面美观度或生成效果。如果问题属于原文、时间码、事实或素材证据，`return_target` 必须为 S；如果属于教学目标或关系，必须为 A。

## 填写说明

- `checks` 的结论须依据源定位、已有节点产物的版本/日期、页面对应、确认范围和未决项，不是字段非空检查。完整匹配的产物核对后可通过，不能因旧文件存在就免审；未验证的数字术语和媒体关联如实保留缺口。
- `required_fix` 只写具体缺项、证据冲突、所属分区和受影响页，不写新 S 摘要、替代更正稿或视觉方案。局部补卡由所属阶段在原分区修正后复核，不绕过原错误。
- `return_target` 是实际退回责任：源文/事实/素材问题填 S，教学语义填 A，无需退回填 none。保留既有 `conclusion` 取值；其中“退回A线”是既有退回结论标签，不覆盖 `return_target: S` 的责任定位。
- 已有证据足以支持且与已确认目标一致时自行核对闭合；关键语义无依据或冲突才问一个必要问题，写入仍遵守授权范围。
