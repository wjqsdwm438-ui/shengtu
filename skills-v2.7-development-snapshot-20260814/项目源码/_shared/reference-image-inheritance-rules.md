# Reference Image Inheritance Rules

## Single Reference Template
```yaml
reference_id:
reference_role: content / layout / style / series / sample / edit_target / failure_diagnosis
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

## Multi Reference Rule
Declare priority for every reference image. Do not write vague terms such as `综合参考`, `整体融合`, or `自动吸收`. If references conflict, preserve user frozen items and the project design system first.

## Failure Image Rule
A failed image is for diagnosis only. It does not become a style reference unless the user explicitly says so.

## Frozen Item Rule
Reference inheritance must not override frozen title position, image count, text policy, material retention, or user-confirmed structure.
