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
Diagnose before changing prompts. Local revision must preserve frozen A/B/T basis and only modify declared items. Do not turn a local fix into full redo unless user asks.
