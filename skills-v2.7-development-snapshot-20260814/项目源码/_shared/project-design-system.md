# Project Design System

Use this file to record the course series design system. It borrows only lightweight design-system thinking from external projects; it is not an implementation dependency.

## Required Fields
- course_series_name:
- design_tone:
- title_system:
- color_system:
- border_and_frame_system:
- image_packaging_style:
- typography_preference:
- background_policy:
- sample_state_policy: GPT Image output remains visual sample until user confirmation.

## Priority
Within the style domain only: user current explicit request > confirmed project design system > reference image inheritance fields > platform default aesthetics. This ordering cannot override teaching goals, content relationships, accurate must-show content, or A's pagination authority. If a confirmed style cannot carry the teaching requirements, B first proposes a compatible implementation; pagination or semantic changes return to A, and only affected user-owned decisions require a Gate.

The model may compare options and recommend one, but the user makes the final decision on layout, visual direction, reference inheritance, text policy, prompt direction, and image-generation choice. A recommendation is never an automatic freeze. Ask only one decision question at a time.

## Conflict Rule
When a reference image conflicts with the series design system, do not fully inherit the reference image. State which series items stay frozen and which reference items may migrate.

Shared responsibilities, contracts, authorization and state rules are defined by `course-visual-production-v2.7.md` and its corresponding shared contracts. Resolve conflicting clauses explicitly; do not use this style file as a higher-level workflow authority. A design-system entry, preset or asset existing in inventory is not automatic activation or permission to use it.

## Non-Ratio Rule

The design system may define canvas size, title system, color, frame, typography, and background policy, but it must not define a fixed image-area percentage for a page type. Image space is decided per page from teaching purpose, information relationship, legibility, visual focus, background competition, and room required by must-show content.

A confirmed series style does not authorize cross-page skeleton inheritance. B-line must still prove that the source and target pages share the same teaching relationship and semantic visual carrier.
