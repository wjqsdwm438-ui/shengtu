# Shared Page Brief — A Section

A 线必须在 S 线创建的同一份 `page_brief` 中追加 `a_section`。下列 `s_section` 是只读引用，不得摘要、重述或改写。

```yaml
schema: course_visual_page_brief/v2.7
page_brief:
  page_id:
  original_course_order:
  s_section: <preserve_verbatim_from_S>
  a_section:
    status: draft / confirmed / needs_user_gate
    teaching_goal:
      learner_outcome:
      source_evidence:
    teaching_relation:
      relation_kind: 比较 / 步骤 / 因果 / 组成 / 映射 / 场景解释 / 其他
      participants:
      direction_or_logic:
      source_evidence:
    must_show_items:
      exact_text:
      exact_numbers:
      exact_terms:
      required_real_materials:
    image_pedagogical_task:
      learner_should_see_or_compare:
      task_reason:
    forbidden_semantic_drift:
      -
    intentionally_not_decided_by_A:
      - template
      - layout_or_composition
      - image_or_text_ratio
      - visual_carrier
      - cross_page_skeleton_inheritance
      - production_batch
      - generation_prompt
    unresolved_semantic_gate:
      needed: yes / no
      question:
    evidence_notes:
    a_review_status: pending / passed / local_patch / returned_to_A
  b_section:
    status: pending
  c_section:
    status: pending
```

## 交接不变式

- `s_section` 必须与 S 线确认版一致。
- `a_section` 只记录教学语义和事实硬约束，不得出现页型、主次视觉焦点、布局区域、图片占比、模板变体或多套视觉方案。
- B 只追加 `b_section`；需改变 A 语义时必须退回 A。

## 填写说明

- `teaching_relation.relation_kind` 的示例是开放提示，不是互斥枚举；可写复合关系，并在 `participants`、`direction_or_logic`、`source_evidence` 分清对象、条件、方向和必要跨页依赖，不为套版强行二选一。
- `must_show_items` 区分必须逐字的屏显文字、数值、术语与真实素材，不改原旁白；具体专业约束及来源可写入 `evidence_notes`，注明对象/标注/图例和依赖页，不以学科名替代证据。
- `forbidden_semantic_drift` 写当前内容不能省略、颠倒、混同的具体条件与关系；专业约束可复合，视觉实现留 B。已有节点的语义用路径、版本/日期、定位及确认范围核对后沿用，只补缺项，未验证不写已验证。

## 教学分组复核阶段
本模板用于正式页面A区，不限制前期A分析的准入：只有已批准文字范围和S候选切分时，先分析教学分组，不要求最终页数已确认。分组拆合的理由、逐字边界、原候选到新单元映射和必要衔接记录在已授权分析/修订说明；正式写入前保护原S证据，不用重述原文或原地重编号替代迁移方案。
