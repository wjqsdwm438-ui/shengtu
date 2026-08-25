# B-Line Production Card

```yaml
status: B线生产交接
source_A_line_card:
candidate_policy: standard_two_candidates / reference_locked_single_candidate
reference_selection:
  folder_path:
  discovered_images:
  primary_layout_reference:
  secondary_references:
  selection_reason:
  rejected_references:
  user_confirmation: pending / confirmed
template_identity:
  template_id:
  template_version:
  psd_hash:
  preview_hash:
  reference_set_hash:
  layer_manifest_hash:
template_layer_manifest:
  fixed_master:
  variable_content:
  optional_animation_layers:
  user_confirmation: pending / confirmed
flattened_png_fallback_gate:
  required: yes/no
  known_limitations:
  user_confirmation: pending / confirmed / not_applicable
context_isolation:
  explicit_reference_paths_only: yes
  include_previous_conversation_images: no
  include_failed_images_automatically: no
  include_entire_reference_folder: no
four_gates:
  aesthetic_tone:
  learning_task:
  student_load:
  media_division:
six_checks:
  page_type_stable:
  aesthetic_clear:
  information_producible:
  single_main_visual:
  text_layer_post_editable:
  generation_stability:
方案A_稳妥版:
  production_goal:
  page_type:
  preset_basis:
  difference_from_other_scheme:
  difference_dimension: structure / material_policy / composition / visual_rhythm / main_visual_focus / risk_control
  first_visual_focus:
  second_visual_focus:
  title_area:
  body_area:
  image_area:
  info_layer:
  safe_margin:
  reference_inherit:
  reference_forbid_inherit:
  text_generation_strategy:
  material_strategy:
  positive_visual_goal:
  creative_authorization:
  hard_bans:
  post_text_fix_cost:
  failure_risk:
  feasibility_score:
  recommend_to_T_line: yes/no
方案A_参考锁定版:
  production_goal: 固定版式带字课程成品
  page_type: A16_既有母版套新内容型
  production_mode: reference_locked
  output_target: full_page_with_text
  primary_layout_reference:
  secondary_references:
  reference_attachment_required_in_C: yes
  text_only_execution_forbidden: yes
  strong_visual_lock:
    canvas_ratio:
    major_panel_structure:
    title_system:
    information_region_relationship:
    image_text_relationship:
    visual_hierarchy:
    palette_family:
  must_show_text_verbatim:
    title:
    subtitle:
    lead:
    section_titles:
    body:
    labels:
    numbers:
    english_terms:
    punctuation:
  text_generation_strategy: 带字
  maximum_local_text_revisions: 2
  deterministic_text_overlay_forbidden: yes
  hard_bans:
  failure_risk:
  feasibility_score:
  recommend_to_T_line: yes
方案B_探索版:
  production_goal:
  page_type:
  preset_basis:
  difference_from_other_scheme:
  difference_dimension: structure / material_policy / composition / visual_rhythm / main_visual_focus / risk_control
  first_visual_focus:
  second_visual_focus:
  title_area:
  body_area:
  image_area:
  info_layer:
  safe_margin:
  reference_inherit:
  reference_forbid_inherit:
  text_generation_strategy:
  material_strategy:
  positive_visual_goal:
  creative_authorization:
  hard_bans:
  post_text_fix_cost:
  failure_risk:
  feasibility_score:
  recommend_to_T_line: yes/no
preferred_T_line_candidate:
preferred_reason:
remotion_asset_handoff_required: yes/no
```
