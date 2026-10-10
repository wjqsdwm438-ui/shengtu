# Failure Diagnosis Rules

## Failure Types
- content_failure: core content not expressed.
- structure_failure: layout or region structure is wrong.
- aesthetic_failure: PPT feel, poster feel, cheap template feel.
- text_failure: typo, fake text, placeholder text, unreadable text.
- material_failure: real material was redrawn or replaced.
- inheritance_failure: reference image inherited wrong parts.
- scope_failure: local edit became full-image redraw.
- model_boundary_failure: request exceeds stable model capability.
- reference_input_missing: selected real reference path was not attached to generation.
- reference_context_leak: unselected, historical, or conversation images affected execution.
- text_generation_failure: exact visible text still fails after the allowed local revisions.
- alpha_generation_failure: required real Alpha still fails after the allowed local revisions; opaque fallback is forbidden.
- remotion_alignment_failure: transparent or split assets changed canvas, origin, scale, or position.
- source_failure: source text, subtitle span, fact basis, or material input is wrong; return to A input preparation; do not rewrite the source without authorization.
- teaching_semantics_failure: teaching goal, teaching relationship, must-show content, or semantic boundary is wrong; return to A-line.
- design_feasibility_failure: template, core skeleton, reference mapping, batch assignment, or realization evidence is wrong; return to B-line.
- adapter_validation_failure: required field is blank, referenced asset is missing, or the page brief contains a contradiction; C-line adapter stops without guessing.
- batch_context_leak: another batch's image, failure, prompt, or history influenced current execution.
- unjustified_skeleton_inheritance: local skeleton was reused without proving the same teaching relationship and semantic visual carrier.

## revision_contract
```yaml
revision_scope:
keep_items:
change_only_items:
forbidden_changes:
reference_basis:
minimal_revision_prompt:
needs_user_confirmation: yes/no
```

## Rule
Diagnose before changing prompts. Local revision must preserve the frozen A/B basis and only modify declared items. Prompt compilation, asset injection, transparency, size, or local generation deviation can remain in C-line only while the teaching relationship, template, and core skeleton stay unchanged. If a frozen basis must change, stop retrying: pagination/teaching changes return to A-line and template/core-skeleton realization changes to B-line; do not use repeated full-page redraws to hide an upstream design problem.

Routing is determined by the earliest incorrect responsibility: source-evidence/material-mapping and pagination/teaching problems return to A-line; template/skeleton/reference/batch/feasibility problems return to B-line; adapter and same-structure local execution problems remain in C-line. There is no independent T-line return target.

## 失败影响范围

先定位最早错误责任，再决定是否继续：只有证据确认仅本页局部失败且共享依据无误，才可登记失败并继续其他已授权页；失败记录不是重新生成授权，不自动 v02。若共同图例、方向、模板或参考依据有误，或影响尚不清楚，先暂停可能依赖同一错误的页面，回 A/B/C 对应责任，不默认全课重启；不依赖该错误且已授权的页无需牵连。

修复后只复核受影响页及必要衔接。固定基准优先于对话惯性；被污染时只依据同一冻结基准恢复干净上下文，不借机改设计或扩大授权。实际回执未报告模型时写“未报告”，不能推断。既有局部文字修订上限与每次修订授权仍保留，禁止无限重试。

## 分页异议的局部责任
原文/准入不变时不重跑S。A统一负责源证据与页界、页数、正文归属、教学关系及衔接，B只修分页语义不变的具体实现；B提出跨页拆合必须提供新旧原文边界和实现证据，由A局部修正并内部复核。用户不满意先定位对象，不自动重启S→A→B。只失效依赖该差异的结论；详见 `pagination-authority-rules.md`。A内部维护源定位，不恢复S独立阶段，不重新索取整课有效准入批准。
