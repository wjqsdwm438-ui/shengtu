# A-Line Page Type Rules

A01-A21 are internal routing labels. Keep them for judgment, logs, tests, handoff, and downstream translation support. Do not make them the default first-level user-facing expression.

## Internal Page Types
A01_无字版式骨架型; A02_纯氛围底图型; A03_氛围图+后期文字层型; A04_主视觉融合型; A05_课程展示卡片型; A06_教学摘录单元型; A07_多文字编辑排版型; A08_案例拼贴型; A09_双图错列/双案例对照型; A10_次级案例卡片型; A11_核心判断/结论锚点型; A12_关系收束型; A13_简化流程/时间线/甘特局部示意型; A14_微任务/学生操作指引型; A15_系列模板改字型; A16_既有母版套新内容型; A17_参考图质感迁移型; A18_页面美化精修型; A19_图像包装/边框适配型; A20_素材保留+外层课程页化型; A21_特殊标题系统型.

## A15/A16/A17 Boundary
- A15: reuse an already confirmed series template and change page content within the same template contract.
- A16: a reference image or reference folder is the layout authority; generate one complete with-text page with strong visual locking and real reference attachment.
- A17: inherit aesthetic qualities while allowing layout redesign. Never use A17 to weaken an explicit fixed-layout request.

## User-Facing Rule
Default A-line user output should describe the page in plain language: what page it is, what task it solves, what constraints are fixed, what real problems exist, and which of the three options should be chosen. Use user-readable option names: `方案一：稳妥优化版`, `方案二：精品升级版`, and `方案三：现代重排版`.

## Internal Output Rule
For each choice, preserve: `internal_page_type_top1`, `internal_page_type_top2`, `internal_routing_reason`, `internal_risk_points`, carrier method, user Gate need, and adjacent-type reasoning when needed. These fields belong in the handoff/log layer, not the first user-facing headline.
