# Visual Sample State Rules

## States
```text
not_generated
visual_sample_generated
visual_sample_rejected
visual_sample_confirmed
revision_required
delivery_preparation_allowed
full_page_candidate
final_course_visual
transparent_foreground_pending_gate
transparent_foreground_generated
split_layer_pending_gate
remotion_asset_handoff_ready
```

## Hard Rules
- Ordinary C-line output enters `visual_sample_generated`. A complete reference-locked with-text page that passes C-line checks enters `full_page_candidate`.
- C-line must not mark a candidate as final automatically.
- Only the user can move `full_page_candidate` to `final_course_visual` or `visual_sample_generated` to `visual_sample_confirmed`.
- Post-edit text correction or delivery preparation requires `visual_sample_confirmed`.
- Rejected samples may be used for failure diagnosis, not as style references unless the user says so.
- A transparent foreground may only derive from `final_course_visual` after `transparent_foreground_pending_gate` is explicitly confirmed.
- Optional split layers require a separate `split_layer_pending_gate` confirmation.

## Output Phrase
Before confirmation use `视觉样张` or `带字成品候选`. After explicit confirmation, `正式课程视觉成品` is allowed for the confirmed `final_course_visual` only.
