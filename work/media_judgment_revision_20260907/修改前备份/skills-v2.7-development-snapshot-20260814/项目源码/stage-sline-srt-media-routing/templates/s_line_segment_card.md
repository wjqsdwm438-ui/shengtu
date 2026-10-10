# Source Input Record — S Compatibility

本模板只用于用户明确请求的单独输入整理，或识别历史 S 区。默认 A 直接在现有分析产物中记录输入证据，不要求独立 S 文件。以下是可沿用的源字段，不是新的分页 schema，也不是必须请用户填的表。

**不创建 page_id，不创建 page_brief 或待填 A/B/C 页面，不预交一套教学候选分页。** segment_id 仅作源寻址；源记录的数量不代表页数。

```yaml
segment_id:
original_course_order:
segment_time_metadata:
  source_type:
  start_time:
  end_time:
  source_line_ids:
  source_continuity_note:
source_text:
  verbatim:
  source_path:
  source_version:
  source_version_date:
  source_locator:
  input_role: 旁白正文 / 屏显文字 / 制作批注 / 素材需求 / 实际媒体
verified_facts:
  - fact:
    evidence: 仅说明原文对应及忠实性核对，不等于外部真实性审校
available_materials:
  - path_or_id:
    material_type:
    availability: available / missing / unverified
    source_note:
visual_assistance_need:
  needed: yes / no / uncertain
  learner_difficulty_to_support:
  reason:
s_route:
recommended_medium:
enter_A_line: yes / no
routing_reason:
if_not_enter_A_line:
  recommended_production_method:
  material_type:
  search_keywords:
  teacher_on_camera:
  screenshot_or_clip_needed:
  subtitle_highlight_needed:
  post_packaging_needed:
  image_generation_forbidden_reason:
scope_evidence:
  processing_scope_and_record:
  non_a_scope_and_record:
  a_body_scope_and_record:
  unresolved_scope_items:
```

## 原文、素材与有效范围

- source_text.verbatim 保留原旁白，不把屏显、批注或制作需求并入正文。source_locator 写源文件行号/段落/页码、逐字起止（均含），以及必要的图锚点/批注范围；不只按解包媒体序号配文。
- 正式 A 分页中需机器验证的源范围统一使用 `_shared/pagination-plan-contract.md` 的 Span，不另造摘要、指纹或不同坐标体系。本输入记录不是“一个记录对应一个页面”的映射。
- source_note 记录媒体所对应内容、用途、原文件/链接位置、核对边界。已有节点以原路径、版本/日期和批准范围引用，不复制更正稿；链接、缓存图和实际媒体分开。
- available 只用于真实文件可读、内容与定位已核对；无文件记 missing，关联/用途/内容未核对记 unverified。可用状态不等于参考/生产用途获批，也不等于专业事实已外部验证。
- 无时间轴任务的时间字段注明“不适用”与业务理由；路由确有依赖才补时间证据，不估算时长、不强要音频。未核验 DOC 排版/裁切/关联写在来源说明，只影响相应内容。
- scope_evidence 分开引用处理范围、Non-A、A 正文及各自有效决定，未决差异如实保留。不以一个 confirmed 推导页数、制作方式、生图或成品授权。有效相同范围不重复确认。

## 历史 S 区与下游

历史 s_section 保留原文及已有决定，作为 A 的源引用或旧候选比较依据；旧 page_id、original_course_order 和 confirmed 不自动成为新分页。A 从全文重新分析并实际比较拆合，有证据可以保留原边界；在方案收敛时建立新 page_id 和明确映射。B/C 不改源文或自行改页界，输入/正文归属/分页问题提交证据给 A 局部修正，不要求重启独立 S。

输入整理不得添加 layout、composition、image_ratio、image_area、template_change、production_card、prompt、visual_option、title_candidate、text_budget_hint 或教学候选分页。
