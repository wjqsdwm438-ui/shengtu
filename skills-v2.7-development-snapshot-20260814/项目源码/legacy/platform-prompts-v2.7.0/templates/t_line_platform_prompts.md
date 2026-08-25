# T-Line Platform Prompts

## Default Image2-First Output

```yaml
status: T线Image2优先提示词转译
mode: image2_first_default
selected_candidate_id: 方案A_稳妥版 / 方案B_探索版
selection_reason:
image2_en:
  image2_execution_prompt:
  negative_prompt:
  revision_prompt_template:
    keep_items:
    change_only_items:
    forbidden_changes:
    minimal_revision_instruction:
backup_candidate_not_translated:
expansion_available_on_request: 即梦 / nanobanana / full_prompt package
```

## Expanded Multi-Platform Output

Use only when the user explicitly requests multi-platform, 即梦, nanobanana, full prompt, or complete prompt package.

```yaml
status: T线多平台完整提示词转译
mode: expanded_multi_platform_on_request
candidate_id: 方案A_稳妥版 / 方案B_探索版
platform_prompts:
  jimeng_cn:
    full_prompt:
    short_execution_prompt:
    negative_prompt:
    revision_prompt_template:
      keep_items:
      change_only_items:
      forbidden_changes:
      minimal_revision_instruction:
  image2_en:
    full_prompt:
    short_execution_prompt:
    negative_prompt:
    revision_prompt_template:
      keep_items:
      change_only_items:
      forbidden_changes:
      minimal_revision_instruction:
  nanobanana_en:
    full_prompt:
    short_execution_prompt:
    negative_prompt:
    revision_prompt_template:
      keep_items:
      change_only_items:
      forbidden_changes:
      minimal_revision_instruction:
```
