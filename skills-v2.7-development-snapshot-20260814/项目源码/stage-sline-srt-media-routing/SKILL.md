---
name: stage-sline-srt-media-routing
description: V2.7 Stage S-line media routing for Stage Activity Planning course visual production. Use when Codex receives .srt subtitles, scripts, voiceover text, single-page content, or mixed teaching material and must decide whether content should become teacher-on-camera, existing video/image material, screen recording, subtitle/annotation packaging, AI course visual page, or manual confirmation before A-line.
---

# Stage S-Line SRT Media Routing

## 渐进式读取

### 必读
- 当前 `SKILL.md`。
- 先盘点并查看当前课程的“版式”目录、母版、母版预览和参考图；只有完成这一步，才读取用户提供的 SRT、讲稿或单页内容并做路由判断。已有上游确认的版式分类时直接继承，不得自行改类。
- 不默认读取共享总控、A/B/T/C Skill 或任何示例。

### 按需读取路由
- 一次只允许由当前唯一未决问题触发一个来源；读取后先执行快速确认，再决定是否扩展下一项。
- 只有 S01-S08 相邻路由仍无法区分时，读取 `references/srt_media_routing_rules.md` 中对应路由条目。
- 只有用户明确要求时间线索引、确定性证据或 ALG-S01 时，读取 `_shared/algorithm-lite-rules.md` 的 ALG-S01 小节并执行对应脚本。
- 只有需要输出正式片段卡时，读取 `templates/s_line_segment_card.md`。
- 只有已经出现字幕过切风险时，读取 `anti_examples/srt_over_split_failure.md`；已经出现跳过用户确认或用估算替代用户决定时，读取 `anti_examples/pagination_confirmation_skipped_failure.md`；规则读取后仍不能确认 S07 时，才读取 `examples/srt_to_s07_course_page_example.md`。

### 快速确认
读取路由术语后立即确认：当前教学功能、候选路由、直接证据、唯一未决项。一个路由已有充分证据且不存在用户控制项时，停止读取。

### 停止规则
输出当前 S线结果后停止。即使结果为 `S07_AI课程视觉页型`，也不得自动读取或执行 A线；只有用户明确要求继续到 A线或端到端流程时才跨阶段。

## 阅读与单问题确认顺序

- 本地材料能够消除的信息差先通过只读检查消除；不得把可从版式、母版、预览、参考图、SRT 或讲稿中查明的问题转给用户。
- 缺少音频、实际时长或时间码时，依次单独询问“音频依据”“实际时长依据”“时间码依据”。一次回复只允许出现一个待确认问题；当前问题未回答，不得询问下一项，也不得用估算结果继续冻结片段或分页。
- 证据齐备后，依次把“需要处理的片段范围”“Non-A 范围”“进入 A线的片段清单”“分页方案”交给用户确认。每次只确认其中一项，当前项未确认不得进入下一项。
- 模型可以说明依据并给出建议，但用户未明确确认时，不得把建议、继续询问或后续指令解释为对上述事项的确认。
- 用户未明确确认分页方案时，不得输出冻结分页或正式 S线交接产物。

## 正式产物与交接

写入正式产物前，先用自然语言说明：本线准备生成什么、准备写到哪个文件、是否会修改已有文件、下一线实际需要接收什么、哪些分析或验证记录不属于正式交付。说明后只问：`是否按上述产物与交接方案执行？`

只有用户明确确认后才写入；一次确认只授权一个已说明的产物。写完立即停止，不得顺带追加 A/B/T/C 内容、进入下一线，或把“输入交接文件”理解为应继续向该文件追加。用户要求调整时，一次只追问一个修改方向。

## Responsibility
S-line is not image generation and not A-line. It merges SRT/script text by semantic teaching segment, chooses the best media route, and decides whether a segment enters A-line. Only `S07_AI课程视觉页型` enters A-line by default.

## Inputs
`.srt`, script, voiceover text, teaching paragraph, single-page idea, old V2.6 material after migration, or user request asking for S线/分镜/媒介分流.

## Routes
`S01_教师出镜型`, `S02_教师出镜+课程页辅助型`, `S03_视频/现成素材展示型`, `S04_图片/现成素材展示型`, `S05_软件界面/屏幕录制型`, `S06_后期字幕/标注包装型`, `S07_AI课程视觉页型`, `S08_人工确认型`.

## Must Rules
- Do not split `.srt` sentence by sentence into pages.
- Merge adjacent subtitles by semantic function, object, and continuity; preserve `segment_time_metadata`.
- Do not force visually unnecessary material into AI image generation.
- Pure transition or teacher-explainable content should not enter A-line.
- Real event, brand case, live performance, exhibition space, software operation, screenshots, and subtitle packaging usually do not enter A-line.
- Enter A-line only for long-stay course main pages, case explanation pages, structured visual pages, and series course pages.

## Prohibitions
Do not write A-line page cards, B-line production cards, T-line prompts, or C-line GPT Image instructions. Do not call non-A material a failed page; it is a valid media route.

## Output Contract
普通路由结论可直接使用本段列出的字段，不需要读取模板。只有用户需要正式片段卡或机器可复用结构时，才读取 `templates/s_line_segment_card.md`。正式卡必须包含 `segment_id`, `segment_time_metadata`, original subtitle/script summary, teaching function, recommended medium, S-route, whether it enters A-line, reason, and next production suggestion。Non-A output must include production method, material type, search keywords, teacher-on-camera need, screenshot/video fragment need, subtitle highlight need, packaging need, and reason to forbid image generation.

## Failure / Return
Use `S08_人工确认型` when material is ambiguous, media evidence is missing, or forcing a route may waste production effort. Ask only for the current missing decision. 一个问题不得同时询问音频、时长、时间码、片段范围或分页中的多项。

## Minimal Example
Examples are evidence-only and follow the conditional routes above; they are never default reading.
