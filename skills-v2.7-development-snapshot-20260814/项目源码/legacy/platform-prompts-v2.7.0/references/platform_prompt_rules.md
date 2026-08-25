# Platform Prompt Rules

## Default: Image2 English
Default T-line output is Image2-first and concise. Translate only one preferred B-line scheme marked `recommend_to_T_line: yes`. Output `image2_execution_prompt`, `negative_prompt`, and a compact `revision_prompt_template`.

Image2 prompt requirements:
- English only.
- Prefer concise image-production language.
- Include layout, visual focus, material policy, text policy, reference inheritance, and sample-state caveat only when they affect execution.
- Do not output both full and short prompt by default.
- Keep negative prompt to 3-5 hard bans.

## Revision Template
Every default output includes a short revision template with:
- `keep_items`
- `change_only_items`
- `forbidden_changes`
- `minimal_revision_instruction`

The revision template prevents local C-line edits from changing frozen A/B-line basis or becoming a full redraw.

## Expanded Platforms On Request
Only when the user explicitly requests multi-platform, 即梦, nanobanana, full prompt, complete prompt package, or all platform prompts:

### 即梦中文
Use natural Chinese and platform-friendly visual wording. Keep prompt scope aligned to B-line.

### Image2 English
English only. Expanded mode may include both `full_prompt` and `short_execution_prompt`.

### nanobanana English
English only. Avoid Chinese labels. Keep the same frozen items and hard bans.
