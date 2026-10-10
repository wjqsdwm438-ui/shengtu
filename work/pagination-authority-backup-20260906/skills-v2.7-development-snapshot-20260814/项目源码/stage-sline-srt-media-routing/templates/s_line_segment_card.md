# Shared Page Brief — S Section

S 线创建共享页面简报并只填写 `s_section`。`a_section`由 A 线在同一份对象中追加；B/C 同理。不得复制或改写上游区域。

```yaml
schema: course_visual_page_brief/v2.7
page_brief:
  page_id:
  original_course_order:
  s_section:
    status: confirmed
    segment_id:
    segment_time_metadata:
      source_type:
      start_time:
      end_time:
      source_line_ids:
      merge_reason:
    source_text:
      verbatim:
      source_path:
      source_locator:
    teaching_function: 导入 / 定义 / 案例 / 过渡 / 总结 / 任务 / 操作 / 展示
    verified_facts:
      - fact:
        evidence:
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
  a_section:
    status: pending
  b_section:
    status: pending
  c_section:
    status: pending
```

## S 线不得添加的字段

`layout`、`composition`、`image_ratio`、`image_area`、`template_change`、`production_card`、`prompt`、`visual_option`、`title_candidate`、`text_budget_hint`。

## 填写说明（沿用现有字段）

- `source_text.verbatim` 保留原旁白；`source_locator` 写段落/页码或字幕行、相关图的关系与锚点、批注范围，注明正文/屏显/制作批注/素材需求的角色，不能把批注并入旁白，也不能只按解包图片序号配文。
- `source_note` 记录媒体对应的段落或批注、用途、原文件/链接位置及核对边界；已有节点产物用原路径、版本/日期和确认范围引用，不复制更正稿。链接、缓存图、实际媒体分开记录。
- `availability`：真实文件可读且内容与定位已核对才填 available；仅有需求、无文件填 missing；位置、用途或内容尚未核对填 unverified。可用状态不等于专业事实已验证或使用已获批准。
- 无时间轴任务在 `segment_time_metadata` 的时间字段注明“不适用：当前文档路由不依赖时间轴”；有业务依赖才补对应时间证据，不估算、不强要音频。未验证的旧 DOC 排版/裁切/关联写入 `source_note` 或 `source_locator`，只阻塞相关片段。
