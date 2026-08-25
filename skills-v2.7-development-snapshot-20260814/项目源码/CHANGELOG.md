# 变更记录

## Unreleased

- 将六个阶段 Skill 的读取策略统一为“必读、按需读取路由、快速确认、停止规则”四段式入口。
- 新增 `_shared/progressive-reading-protocol.md`，规定单步扩展、术语确认、阶段边界和用户 Gate 的区别。
- 移除共享总控、整组 references、模板与示例的默认预读，避免 S07 等阶段结果自动触发下一阶段读取。
- 在 `run_all_checks.py` 中加入渐进式读取合同检查，防止入口重新退化为 eager reading。

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
