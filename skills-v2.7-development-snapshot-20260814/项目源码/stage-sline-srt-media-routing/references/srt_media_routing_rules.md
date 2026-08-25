# SRT Media Routing Rules

## Segment Merge
Merge subtitle lines when they share the same teaching object, teaching function, and likely visual carrier. Preserve time range and source line IDs in `segment_time_metadata`.

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
