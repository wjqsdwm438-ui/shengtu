# Anti Example: Missing Revision Template

Wrong: T-line outputs only one Image2 execution prompt with no revision safeguards.

Why wrong: even in default Image2-first mode, the output must include compact `revision_prompt_template` fields: `keep_items`, `change_only_items`, `forbidden_changes`, and `minimal_revision_instruction`.

Also wrong: T-line outputs 即梦, Image2, and nanobanana full prompt packages by default.

Why wrong: multi-platform and full prompt packages are expanded mode only, triggered by explicit user request.
