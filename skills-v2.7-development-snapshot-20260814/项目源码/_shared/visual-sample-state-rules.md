# Visual Sample State Rules

## States
```text
not_generated
visual_sample_generated
visual_sample_rejected
visual_sample_confirmed
revision_required
delivery_preparation_allowed
```

## Hard Rules
- C-line GPT Image output enters `visual_sample_generated` only.
- C-line must not mark any sample as final.
- Only the user can move `visual_sample_generated` to `visual_sample_confirmed`.
- Post-edit text correction or delivery preparation requires `visual_sample_confirmed`.
- Rejected samples may be used for failure diagnosis, not as style references unless the user says so.

## Output Phrase
Use `视觉样张`, not `最终稿`, `定稿`, `最终交付页`, or `正式成图`.
