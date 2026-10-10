# Source Media Routing Rules (A Default / S Compatibility)

默认由 A 输入整理使用这些兼容路由；只有用户明确请求时才独立运行 S。路由记录不是页面，不生成 page_id 或一套教学候选分页。

## Segment Merge
Preserve continuous source text, actual time ranges and source line IDs in `segment_time_metadata`. Source grouping is for traceability, not teaching pagination. Do not use each subtitle line, presumed layout, template, old segment count or visual carrier as a page boundary. A determines boundaries after whole-scope teaching analysis, capacity checks and actual split/merge comparison.

## Route Criteria
- S01: teacher can explain with simple subtitle or no visual page.
- S02: teacher remains main view; course page is minor support.
- S03: real video, event footage, official clip, live performance, exhibition, brand case video.
- S04: existing image/photo/material evidence should be shown.
- S05: software UI, platform operation, screen recording, screenshot annotation.
- S06: subtitle highlight, label packaging, lower-risk post-production annotation.
- S07: long-stay AI course visual page needed for main concept, case explanation, structured page, or series course page.
- S08: insufficient evidence or high ambiguity.

## Non-A Production Fields
recommended_production_method, material_type, search_keywords, teacher_on_camera, screenshot_or_clip_needed, subtitle_highlight_needed, post_packaging_needed, image_generation_forbidden_reason.

## Input Handoff Boundary
In source records, record source evidence, source-faithful facts, available materials, input roles and the learning difficulty that needs visual support. Do not add page IDs, teaching-page candidates, page titles, layout directions, image ratios, template changes, B-line production cards or generation prompts. A's subsequent teaching/pagination work is not a separate S07-entry Gate.

Non-A 保留逐字范围、源定位、路由理由及其批准依据，不混入 A 正文、不默认已批准其具体制作方式。真实文件可读且对应内容已核对才记 available；制作需求不是实际素材。外部真实性/实时专业审校不在此新增。
