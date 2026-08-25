# Legacy V2.6 Migration

## Boundary
This file adapts old V2.6 materials into V2.7. It never lets old C-line prompts execute directly.

## Mapping
- V2.6 page request card -> S-line lightweight input recognition -> A-line page handoff if S07.
- V2.6 class-JSON -> B-line production basis after A-line fields are normalized.
- `screen_text_levels` -> visual sample text hierarchy and post-edit verification list.
- `visual_semantics` -> visual support, material retention, and reference inheritance policy.
- `最终交付课程页成图` -> visual sample / GPT Image Chinese prompt contract / post-edit object.

## Prohibitions
Old V2.6 C-line prompt must not be sent directly to GPT Image. Old final-output wording must not become V2.7 final state. If migration cannot preserve meaning or frozen fields, return to A-line or user Gate.
