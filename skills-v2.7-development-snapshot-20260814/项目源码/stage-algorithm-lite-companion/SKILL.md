---
name: stage-algorithm-lite-companion
description: V2.7 Algorithm Lite companion for explicit testing and evidence logging. Use only when the user or a V2.7 stage explicitly asks to run deterministic ALG-S01, ALG-A02, or ALG-A03 checks, create test logs, validate SRT indexing, text budget, A01 light_region_summary, or page complexity risk without taking over S/A/B/T/C production decisions.
---

# Stage Algorithm Lite Companion

## Position
This is a companion Skill, not a sixth production line. Use it only by explicit request. It runs deterministic scripts and records evidence for V2.7 Algorithm Lite.

## 渐进式读取

### 必读
- 当前 `SKILL.md`、调用方明确指定的 ALG 检查名和输入文件。
- 已能从 Script Map 唯一选择脚本时，不默认读取共享总控或完整 Algorithm Lite 规则。

### 按需读取路由
- 一次只允许由当前唯一未决问题触发一个来源；读取后先执行快速确认，再决定是否扩展下一项。
- ALG 名称、阈值或返回含义不明确：只读 `_shared/algorithm-lite-rules.md` 的对应 ALG 小节。
- ALG-B01 或 ALG-C01：只读各自 reference/checklist；不得连读另一套清单。
- 需要正式证据日志时，读取 `templates/algorithm_test_log.md`。
- 只有调用阶段明确要求示例证据时才读取其对应示例，不读取其他生产阶段示例。

### 快速确认
确认 ALG 名称、唯一脚本或清单、输入路径、预期证据字段和“仅证据”边界。映射唯一后立即执行，不继续读取生产规则。

### 停止规则
返回检查证据后立即回到调用阶段。脚本结果需要业务解释时由调用阶段处理，Algorithm Lite 不扩展读取来接管业务决定。

## Allowed Work
- Run root scripts from `<项目根目录>\scripts`.
- Use samples in `<项目根目录>\tests`.
- Write test evidence under `<项目根目录>\test_logs`.
- Return recommendation, risk, pass/return/manual-confirm suggestion.

## Hard Boundaries
- Do not override user explicit requirements or frozen items.
- Do not write final S-line, A-line, B-line, T-line, or C-line deliverables.
- Do not generate prompts, images, PPTX, HTML, MP4, Remotion, MCP, or install dependencies.
- Do not restore `editable_layout_spec`; validate `light_region_summary` only.
- Do not call GPT Image output final, 定稿, or delivery.

## Script Map
- ALG-S01: run `scripts\build_srt_index.py` for SRT timeline and semi-manual routing index.
- ALG-A02 text budget: run `scripts\check_text_budget.py`.
- ALG-A02 A01 skeleton: run `scripts\check_layout_skeleton.py`.
- ALG-A03: run `scripts\score_page_complexity.py`.
- ALG-B01 and ALG-C01: use references/templates only in first round; do not script them yet.

## Output Contract
简短检查结果可直接报告，不读取模板。只有需要保存或交付正式证据日志时，才读取 `templates\algorithm_test_log.md`。正式日志必须包含 input path, script path, command summary, result summary, recommendation, and whether it is evidence-only。

## Return Rules
Return to the calling stage when script output needs human interpretation. Ask the user only when the result would require changing frozen structure, entering a Gate, or deciding between split/no-text/post-edit paths.
