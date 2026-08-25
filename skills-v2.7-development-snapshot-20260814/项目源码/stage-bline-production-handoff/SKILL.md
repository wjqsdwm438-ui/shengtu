---
name: stage-bline-production-handoff
description: V2.7 Stage B-line production handoff for course visuals. Use after A-line/A-review passes to produce standard two-candidate handoffs or one reference-locked A16 candidate, select and confirm reference-folder inputs, preserve exact text and template identity, and prepare T-line input without writing prompts directly.
---

# Stage B-Line Production Handoff

## 渐进式读取

### 必读
- 当前 `SKILL.md`、已通过的 A线冻结交接卡及 A审结果。
- 输入字段完整时，不默认读取共享总控、预设库、模板或示例。

### 按需读取路由
- 一次只允许由当前唯一未决问题触发一个来源；读取后先执行快速确认，再决定是否扩展下一项。
- 四个 Gate、六项检查或退回条件仍有歧义：读 `references/production_handoff_rules.md` 的相关小节。
- 需要为候选方案选择审美预设：只定位并读取 `_shared/page_preset_bank.md` 中与当前页面类型相符的条目，不全文扩展其他预设。
- A线卡中确有参考图：读 `_shared/reference-image-inheritance-rules.md`；无参考图时不得读取。
- 固定母版任务需要Remotion资产交接：读 `_shared/remotion-asset-handoff-rules.md`，但不读取或生成Remotion代码。
- 只有用户或当前阶段明确要求 ALG-B01 证据时，读取相应 Algorithm Lite 规则或清单。
- 只有需要生成正式生产卡时，读取 `templates/b_line_production_card.md`。
- 两方案差异仍不真实时，读取一个直接匹配的成功或失败示例。

### 快速确认
先确认冻结项完整性、四 Gate 结果、两方案的真实差异维度和首选候选。以上信息足够时停止读取；缺失字段直接退回 A线，不通过读取更多预设猜测。

### 停止规则
B线卡或退回报告完成后停止，不自动进入 T线，也不为“备用”目的提前读取提示词规则。

## Responsibility
B-line receives a passed A-line handoff and runs four gates and six checks. Standard tasks output `方案A_稳妥版` and `方案B_探索版`; an explicit fixed-master A16 task outputs one `方案A_参考锁定版`. It does not re-split source text, add course knowledge, overwrite frozen items, or write platform prompts.

## Inputs
A-line frozen handoff card and A-review pass/local补卡 completion. If A-review did not pass, return to A-line.

## Four Gates
审美气质, 学习任务, 学生负荷, 媒介分工.

## Six Checks
页面类型是否稳定, 审美气质是否明确, 信息承载是否可生产, 主视觉方向是否单一, 文字层级是否后期可控, 生成稳定性是否足够.

## Candidate Rules
- 方案A_稳妥版: more stable, readable, material-safe, lower model risk.
- 方案B_探索版: visibly different structure or aesthetic exploration, but must not become poster-like, travel-promo-like, empty atmosphere, or pure style play.
- A and B must differ in at least one real dimension: structure, material policy, composition, visual rhythm, main visual focus, or risk control.
- Each scheme must include `difference_from_other_scheme`; do not use synonym rewrites as the difference.
- Hard bans are 3-5 items only.
- For `A16_既有母版套新内容型` with `production_mode: reference_locked`, use `candidate_policy: reference_locked_single_candidate`; do not create an exploration candidate.
- Inventory the reference folder, select one primary layout reference and no more than two secondary references, explain rejected candidates, and obtain one user confirmation per reference set.
- Carry real paths, exact visible text, template identity, layer manifest, and flattened-PNG fallback Gate. Do not replace them with descriptive summaries.

## Output Contract
Gate 未通过时直接输出退回依据，不读取生产卡模板。正式标准交接输出两个方案；正式参考锁定交接只输出一个 `方案A_参考锁定版`。所有正式交接必须给出唯一首选 T线候选。

## Prohibitions
Do not write GPT Image execution prompts or any historical-platform prompts. Do not bypass text Gate or reference inheritance. Do not erase A-line frozen items. Do not output pseudo-final prompts.

## Failure / Return
If frozen fields are missing, reference inheritance is vague, text Gate unresolved, or ALG-B01 says production cannot preserve the A-line basis, output B-line gate report and return to A-line. Do not output pseudo-final prompts.

## Minimal Example
示例只作为证据。固定母版单候选仍不明确时读 `examples/reference_locked_single_candidate_success.md`；标准两方案差异失败时只读一个匹配项。
