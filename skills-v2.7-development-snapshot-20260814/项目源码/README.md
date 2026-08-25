# 课程视觉生产工具 V2.7.1

本目录是项目的**真正源码根目录**。外层目录仅保存 2026-08-14 开发快照的交接包装、清单与来源证据，不是运行根目录。

## 当前状态

- 版本定位：V2.7.1 开发基线收口。
- 部署状态：仅供本地开发和验证，**未安装或注册为全局 Skill**。
- 依赖边界：检查工具仅使用 Python 标准库；本次基线不安装第三方依赖、不修改全局配置、不推送远程，也不直接接入需要密钥或费用的 API。
- 路径约定：文档、脚本和 Skill 只使用相对项目根的路径，不依赖固定盘符或固定安装位置。

## 流程与职责

主流程为：

```text
S线 -> A线 -> A审 -> B线 -> T线 -> C线 -> 用户确认视觉样张
```

| 阶段 | 目录 | 主要职责 |
| --- | --- | --- |
| S线 | `stage-sline-srt-media-routing/` | SRT 与媒体路由、片段卡生成 |
| A线 / A审 | `stage-aline-course-visual-routing/` | 页面视觉路由、结构判断及审核 |
| B线 | `stage-bline-production-handoff/` | 生产交接与候选方案收敛 |
| T线 | `stage-tline-prompt-translation/` | 将选定方案转换为 GPT Image 中文专用执行提示词 |
| C线 | `stage-cline-gpt-image-execution-feedback/` | GPT Image 视觉样张执行反馈及最小修改闭环 |
| Algorithm Lite | `stage-algorithm-lite-companion/` | 为各阶段提供轻量、非越权的确定性检查 |

Algorithm Lite 是伴随检查层，不替代 S/A/A审/B/T/C 的业务判断，也不恢复可编辑版式规格。

## 渐进式读取机制

- 每个阶段默认只读取当前 `SKILL.md`、用户输入和该阶段必需的上游交接。
- references、templates、examples/anti_examples 按“规则判断、正式结构、失败证据”分别触发，不得整组预读。
- 每次只围绕一个未决问题扩展一个来源；读取关键术语后立即确认当前含义、直接证据和剩余未决项。
- 当前阶段判断充分、到达阶段边界或需要用户作出选择时立即停止，不自动预读下一阶段。
- 完整审计规则见 `_shared/progressive-reading-protocol.md`；普通业务任务不需要默认加载该文件。

## GPT Image 合同

- 主流程能力名称为 **GPT Image**，当前请求模型为 `gpt-image-2`。
- T线默认只输出一套中文执行提示词，不再生成英文版或三平台版。
- “请求模型”不等于“实际执行模型”。只有执行工具或 API 的回执明确报告模型时，才能记录实际执行模型；未报告时必须写“未报告”。
- 完整课程视觉页默认使用不透明背景。
- 素材层、人物或物体抠图、可叠加组件等任务可按需请求透明背景，并使用支持 Alpha 的 PNG 或 WebP。透明背景能力按当前合同标记为 preview，不应表述为所有任务的默认能力。
- 即梦、nanobanana 与旧三平台提示材料已降级为历史证据，位于 `legacy/platform-prompts-v2.7.0/`，不属于当前 T线运行依赖。

## 参考锁定带字页与Remotion资产

- 参考文件夹可作为正式输入；B线选择一张主版式参考和最多两张辅助参考，并由用户确认一次后冻结到系列任务。
- 固定版式任务路由为 `A16_既有母版套新内容型`，使用单一 `方案A_参考锁定版`，不强制生成探索版。
- T/C线必须保留并实际附加选定参考图的真实路径，禁止只凭“参考原图”文字重构或自动带入历史会话图片。
- 第一版由 GPT Image 直接生成完整带字画布；文字必须逐字准确，初次生成后最多进行两次局部修订，不使用确定性文字覆盖。
- 通过检查的完整页先进入 `full_page_candidate`，只有用户确认后才成为 `final_course_visual`。
- 项目可为外部Remotion流程准备透明前景和按需拆层合同，但不生成Remotion代码或执行视频渲染。
- 透明前景只能从已确认成品派生并经过显性Gate；Alpha失败不得降级为不透明图。

## 本地检查

在本目录中运行：

```powershell
python run_all_checks.py
```

默认检查应保持只读，临时产物写入系统临时目录。只有在确需刷新仓库验证证据时才显式运行：

```powershell
python run_all_checks.py --update-evidence
```

检查范围包括现有四个 Python 工具及正反例、Skill frontmatter、`agents/openai.yaml` 最小 schema、渐进式读取入口约束、参考锁定/Remotion合同用例、固定旧路径、当前 GPT Image 契约、历史目录边界和 UTF-8 编码。任何失败均应返回非零退出码。

## 版本与回滚

- 原始开发快照标签：`v2.7.0-dev-snapshot-20260814`
- V2.7.1 收口标签：`v2.7.1-baseline`

标签仅用于本地版本追溯。回滚前应先保存未提交工作，再从相应标签创建检查分支；不要通过改写外层交接材料或 `SNAPSHOT_MANIFEST` 来模拟回滚。

变更说明见 `CHANGELOG.md`，迁移边界见 `MIGRATION_V2.7.1.md`，验证记录见 `V2.7.1_VALIDATION.md`。
