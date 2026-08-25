---
name: stage-aline-course-visual-routing
description: V2.7 Stage A-line course visual page routing for Stage Activity Planning. Use after S-line routes a segment as S07_AI课程视觉页型, or when a user explicitly asks for V2.7 A线页面方向预判, A审, page type selection A01-A21, light_region_summary, text budget, reference inheritance preparation, user-readable page diagnosis, three option planning, or course visual handoff.
---

# Stage A-Line Course Visual Routing

## 渐进式读取

### 必读
- 当前 `SKILL.md`，以及已确认的 S07 片段卡；用户明确指定 A线时可使用其单页内容代替 S07 卡。
- 不默认重读 S线、共享总控、全部页型表、模板或示例。

### 按需读取路由
- 一次只允许由当前唯一未决问题触发一个来源；读取后先执行快速确认，再决定是否扩展下一项。
- A01-A21 候选含义或相邻页型仍不明确：只读 `references/page_type_rules.md` 的相关条目。
- 需要计算计划上屏文字或触发 180 字 Gate：读 `references/onscreen_text_rules.md`。
- 内容关系可能被误写成固定版式：读 `references/layout_decoupling_rules.md`。
- 已选择 A01 或正在判断“空背景”风险：读 `references/no_text_layout_skeleton_rules.md`。
- 用户提供必须保留的真实素材：读 `references/material_retention_rules.md`。
- 存在参考图：读 `_shared/reference-image-inheritance-rules.md`；没有参考图时不得读取。
- 用户要求Remotion适配、透明前景或动画拆层：只读 `_shared/remotion-asset-handoff-rules.md` 的相关Gate。
- 只有需要正式 A线交接卡或 A审报告时，分别读取对应 template。
- examples/anti_examples 只在对应判断仍不稳定或已出现同类失败时读取一个直接匹配项。

### 快速确认
每次读取后立即确认：教学动作、必显文字、内容关系、主载体、Top1/Top2 页型及唯一未决 Gate。Top1 有直接证据且新增资料不会改变决定时停止读取。

### 停止规则
A线交接或 Gate 结论完成后停止，不自动读取 B/T/C。页面不应进入 A线时立即退回 S线，不通过继续读取 A线资料来挽救错误路由。

## Responsibility
A-line only handles content admitted by S-line as `S07_AI课程视觉页型`. It predicts page direction, explains the page problem in user-readable language, proposes three user-facing options, freezes a handoff card, and may run A-review. It does not write platform prompts and does not generate images.

## Inputs
S-line S07 segment card, V2.7 page content, migrated V2.6 page card, user-confirmed A-line target, single reference image, or reference folder.

## Required Workflow
S0 input recognition -> S1 material boundary -> S2 teaching action -> S3 page/density -> S4 content relation -> S5 on-screen text -> S6 visual carrier interface -> S7 foreground/background layer relation -> S8 risk blocking -> S9 key Gate -> S10 user-readable options -> S11 frozen handoff.

## User-Facing Output
Default user-facing A-line output must use this structure instead of leading with A01-A21 codes:

1. `当前判断`: explain what kind of page this is, what the core teaching/visual task is, and what user constraints must be preserved.
2. `主要问题`: directly name real page problems such as old courseware feel, inconsistent main color, fragmented modules, weak information rhythm, low visual hierarchy, reference/material conflict, text overload, or unclear focus.
3. `三版方案`: output exactly these user-readable option names by default:
   - `方案一：稳妥优化版`
   - `方案二：精品升级版`
   - `方案三：现代重排版`
4. For each option, include `适合方向`, `核心思路`, `具体改法`, and `视觉结果`.
5. End with `三版怎么选` and `我建议的优先选择`.

Do not use A01-A21 type names as the primary user-facing expression unless the user asks for internal routing details.

## Internal Page Types
Use A01-A21 exactly for internal judgment, routing, logs, tests, handoff, and T-line translation support. Keep these fields in the handoff/log layer: `internal_page_type_top1`, `internal_page_type_top2`, `internal_routing_reason`, and `internal_risk_points`. Always explain why the internal top choice is selected, why the second choice is not primary, carrier method, main risk, and whether user Gate is needed.

## Text Budget
Count only planned on-screen text. <=60 low, 61-120 medium, 121-180 high but sample allowed, >180 enters original-keypoint-onscreen dynamic Gate. For uncompressible must-show text, split pages first.

## A01/A02
A01 is a no-text layout skeleton with visible title/body/image/info regions, frame, separator, safe margin, and visual focus. It is not empty background. A02 is pure atmosphere background for opener/transition/teacher background/light title only; never use it for formal multi-text course pages.

## Reference-Locked Series Page
If the user provides a reference folder and asks to preserve its layout while replacing course content, choose `A16_既有母版套新内容型` as Top1 and A15 as the adjacent choice. A17 is Top1 only when layout redesign is allowed.

Freeze `reference_folder`, master package availability, template identity, template layer manifest, exact visible text, and `text_generation_strategy: 带字`. The primary deliverable is a single-canvas full page; do not redirect it to no-text skeleton or post-text composition without a user Gate.

When PSD is unavailable, return the one-time flattened-PNG fallback Gate from `_shared/reference-image-inheritance-rules.md`. Do not claim pixel locking.

## Must Output
用户可读诊断或 Gate 只输出当前任务需要的字段，不读取模板。只有需要正式 A线交接卡时，才读取 `templates/a_line_page_handoff_card.md`，并包含 user-readable judgment, problem diagnosis, three options, selection advice, internal page type fields, title strategy, on-screen text, text budget, first/second visual focus, material policy, reference inheritance fields, frozen items, risk, Gate result, and `light_region_summary`。

## Prohibitions
Do not process S01-S06 material as A-line. Do not output exact PPT/Figma coordinates, `editable_layout_spec`, platform prompts, GPT Image instructions, or final sample claims. Do not turn content relation into fixed layout automatically. Do not make internal page type codes the default headline of the user-facing answer.

## A-Review
普通 A审结论不读取模板；只有需要正式审查报告时才读取 `templates/a_review_report.md`。A-review outputs only pass, local补卡, or return to A-line. It never outputs prompts.

## Failure / Return
Return to S-line if the segment should not have entered A-line. Return to user Gate if page type, must-show text, reference role, material redraw permission, or over-180 text Gate is unresolved.

## Minimal Example
Examples are evidence-only. A01 判断不稳定时最多读取一个成功或失败示例，不得连读整个 examples/anti_examples 目录。
