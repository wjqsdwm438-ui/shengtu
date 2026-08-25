# B-Line Production Handoff Rules

## Input
A-line frozen handoff card and A-review pass result.

## Output
Two production handoff cards: `方案A_稳妥版` and `方案B_探索版`.

## Difference Requirement
The two schemes must differ in at least one of: structure, material policy, composition, visual strategy, or risk profile. They must not be synonym rewrites.

## Stop Conditions
Return to A-line when frozen items are missing, reference inheritance is unclear, text budget Gate is unresolved, material preservation conflicts with AI redraw, or ALG-B01 says a candidate cannot preserve the A-line basis.

## Handoff To T-Line
Only candidates marked `recommend_to_T_line: yes` enter T-line. B-line does not write platform prompts.
