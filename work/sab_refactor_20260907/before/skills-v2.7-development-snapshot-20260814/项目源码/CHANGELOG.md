# 变更记录

## Unreleased

- 主流程重构为 `S -> A -> A审 -> B（动态分批） -> C执行适配器 -> C生成/局部修改 -> 按原顺序组装`，取消独立 T线；提示编译、素材注入和参数校验迁入 C线前置适配器。
- 新增单一页面简报合同，S/A/B/C 只追加各自分区，不再通过多份候选卡和提示转译文档重复改写设计意图。
- B线改为基于真实模板和成败案例形成唯一主方案；动态决定批次数量，每批先确认代表页，并隔离不同批次的 C线对话上下文。
- 跨页局部骨架继承新增教学关系与语义视觉载体证明；禁止以效果好、风格统一、页码相邻或同一课程作为替代理由。
- 移除固定图片占比作为设计或合规门槛，改为检查教学任务、视觉焦点、可读性、信息关系、背景竞争和必呈内容空间。
- 新增 `_shared/template-realization-evidence-rules.md`，记录版式1/2真实样片能证明和不能证明的能力边界，防止由空白外壳推导复杂内层设计。
- 明确返工路由：输入问题回 S、教学语义问题回 A、模板/骨架/参考/可行性问题回 B，同结构执行偏差留 C；禁止用重复整页重抽掩盖设计问题。
- 将五个活动 Skill 的读取策略统一为“必读、按需读取路由、快速确认、停止规则”四段式入口。
- 新增 `_shared/progressive-reading-protocol.md`，规定单步扩展、术语确认、阶段边界和用户 Gate 的区别。
- 移除共享总控、整组 references、模板与示例的默认预读，避免 S07 等阶段结果自动触发下一阶段读取。
- 在 `run_all_checks.py` 中加入渐进式读取合同检查，防止入口重新退化为 eager reading。
- 新增参考文件夹、PSD优先母版包、主参考图确认、参考锁定唯一主方案和模板版本合同；旧 A01–A21 标签不再参与设计路由。
- B/C线强制传递、校验并实际附加选定参考路径，隔离历史会话图片，完整带字页最多进行两次GPT局部修字。
- 新增 `full_page_candidate -> final_course_visual` 用户确认状态，以及Remotion透明前景和二次拆层Gate。
- 新增Alpha硬验收：透明前景禁止不透明降级、保持完整画布和统一左上角原点。
- 增加 `tests/reference_remotion_contract_cases.json` 与统一合同回归检查。

## V2.7.1 — 开发基线收口

### 契约

- 将当前生图能力统一命名为 GPT Image，并把当前请求模型记录为 `gpt-image-2`。
- T线改为 GPT Image 中文专用合同：默认只交付一套中文执行提示词、中文负面约束、输出设置及局部修改模板。
- 区分请求模型与实际执行模型；实际模型只能依据工具或 API 回执记录。
- 完整视觉页默认不透明；仅素材层、抠图或可叠加组件按需启用 PNG/WebP Alpha，并将透明背景能力标记为 preview。
- 即梦、nanobanana 及旧三平台材料迁移至 `legacy/platform-prompts-v2.7.0/`，不再作为当前执行路径。

### 结构与元数据

- C线由 `stage-cline-image2-execution-feedback/` 重命名为 `stage-cline-gpt-image-execution-feedback/`。
- 不保留重复的旧名转发 Skill；旧名映射由迁移文档和 Git 历史承担。
- 统一六个 Skill 的 `agents/openai.yaml` 最小结构，并保持 `allow_implicit_invocation: false`。
- 清理旧固定绝对路径，改用项目相对路径或从脚本位置推导路径。

### 验证与工程基线

- 增加统一检查入口 `run_all_checks.py`；默认只读，显式使用 `--update-evidence` 时才更新仓库证据。
- 检查入口仅依赖 Python 标准库，不安装外部包。
- 将受管测试日志统一为 UTF-8 无 BOM、LF 换行。
- 增加项目 README、迁移说明和 V2.7.1 验证记录。
- 将三个 Draw.io/SVG 流程资产纳入 Git 基线，同时保持外层原始交接材料和 `SNAPSHOT_MANIFEST` 不变。

### 版本节点

- 原始快照：`v2.7.0-dev-snapshot-20260814`
- 收口基线：`v2.7.1-baseline`

> 本文件描述 V2.7.1 的目标变更集；最终验证状态以 `V2.7.1_VALIDATION.md` 和实际 Git 标签为准。
