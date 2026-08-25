# Reference Image Inheritance Rules

## Reference Set Input
Reference folders are first-class inputs. Inventory supported image files, then select one primary layout reference and no more than two secondary references. Never pass an entire folder to generation or use vague labels such as `综合参考`.

```yaml
reference_set:
  reference_set_id:
  folder_path:
  layered_master:
    psd_path:
    available: yes/no
  master_preview_path:
  discovered_images:
  primary_layout_reference:
  secondary_references:
  selection_reason:
  rejected_references:
  user_confirmation: pending / confirmed
```

The primary selection is a user Gate once per series. Reuse it until the reference set or template version changes.

## Layered Master Gate
Prefer PSD, a full-size PNG preview, reference pages, and a manifest. GPT Image uses supported raster references; PSD is for understanding layer boundaries.

If no layered master exists, return a one-time template Gate instead of claiming pixel locking:

```yaml
layered_master_available: no
fallback_reference: flattened_png
fidelity_level: strong_visual_lock
known_limitations:
  - 不能读取真实图层结构
  - 不能承诺母版像素完全一致
  - 透明派生和拆层风险更高
user_confirmation: pending
```

After confirmation, reuse the fallback decision for the same template version.

## Single Reference Template
```yaml
reference_id:
reference_role: content / layout / style / series / sample / edit_target / failure_diagnosis
path:
content_hash:
inherit:
  composition: yes/no/local
  color: yes/no/local
  texture: yes/no/local
  title_system: yes/no/local
  image_packaging: yes/no/local
  background_atmosphere: yes/no/local
  border_material: yes/no/local
forbid_inherit:
  content_subjects:
  layout:
  text_content:
  unrelated_objects:
  poster_like_elements:
priority:
```

## Reference-Locked Full Page
When the user requests an existing layout with new course content, route to `A16_既有母版套新内容型`. Use A15 only as the adjacent series-template choice; A17 is primary only when layout redesign is allowed.

Generate the full page as one canvas. Strongly lock canvas ratio, major panels, title system, information-region relationship, image/text relationship, hierarchy, and palette. Do not promise pixel identity for generative full-page work.

Every selected reference path must survive B-line and T-line and be actually attached by C-line. Text-only reconstruction is forbidden.

## Template Version
```yaml
template_identity:
  template_id:
  template_version:
  psd_hash:
  preview_hash:
  reference_set_hash:
  layer_manifest_hash:
```

Changing the PSD, preview, reference set, or layer manifest creates a new version. Existing pages remain pinned unless the user explicitly migrates them.

## Multi Reference Rule
Declare priority for every reference image. Do not write vague terms such as `综合参考`, `整体融合`, or `自动吸收`. If references conflict, preserve user frozen items and the project design system first.

## Failure Image Rule
A failed image is for diagnosis only. It does not become a style reference unless the user explicitly says so.

## Frozen Item Rule
Reference inheritance must not override frozen title position, image count, text policy, material retention, or user-confirmed structure.
