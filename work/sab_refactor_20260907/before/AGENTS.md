# 生图生视频：项目默认规则入口

## 课程视觉生产与测试

本项目使用仓库内 `skills-v2.7-development-snapshot-20260814/项目源码` 的修改版规则。处理课程视觉任务时，以这些项目规则为准，不用全局同名旧技能替代，也不把旧独立 T线作为当前生产入口。无需用户每次粘贴规则路径。

- 用户要求全流程或测试时，先读 `skills-v2.7-development-snapshot-20260814/项目源码/_shared/course-visual-production-v2.7.md`；按任务需要读取共享简报与批次规则。
- S阶段：`skills-v2.7-development-snapshot-20260814/项目源码/stage-sline-srt-media-routing/SKILL.md`。
- A与A审：`skills-v2.7-development-snapshot-20260814/项目源码/stage-aline-course-visual-routing/SKILL.md`。
- B阶段：`skills-v2.7-development-snapshot-20260814/项目源码/stage-bline-production-handoff/SKILL.md`。
- C阶段：`skills-v2.7-development-snapshot-20260814/项目源码/stage-cline-gpt-image-execution-feedback/SKILL.md`。
- 只加载当前阶段和必要上游文件；现有模板、参考规则按对应SKILL的渐进式读取要求使用，不一次加载全部文件。

## 正常多对话使用

用户可以在本项目内照常新建对话，分别开展阶段或批次工作；不要求留在某一对话、使用分叉功能、重新切分支或指定内部文件。跨对话读取已有项目产物及确认记录续接，沿用同一页面简报，各阶段只维护所属分区；不要求用户重新清洗原稿或反复确认有效决定。延续用户现有产物目录，不为接入规则另造工作流。

同批C页面在同一对话连续执行，跨批隔离。既有生图授权、参考用途、修订和定稿Gate仍按项目规则执行；待批AE归档不自动启用。项目入口配置不代表真实图像效果已经验证。
