# GPT Image 执行适配器规则

## 单一编译输出

C线只把 B区 `main_execution_plan` 编译为一套中文 GPT Image 执行合同。不得选择候选、补充视觉方向或产生第二套方案。

## 完整性硬 Gate

提交生成前必须确认：

- 源引用及A当前分页/内部复核完整，A/B pagination_ref与当前plan_id/plan_version及owned_spans一致；页面ID、课程原始顺序、教学目标/关系、必呈项和main_execution_plan完整；
- 尺寸是完整具体值；
- `main_execution_plan.outer_template.identity`、`description`、`evidence_reference_id` 和 `main_visual_description` 完整；
- 所有声明使用的素材存在且可读；
- 没有占位符、空句、截断句、矛盾或尚未决定的核心设计/当前状态文字分配；完整主方案的效果待验证不等于核心决策空白；
- `implementation_evidence` 五个核心字段完整；
- `C_adapter_handoff` 已明确素材、保留项、变化项且无 blocker；
- 批次代表页 Gate 和骨架继承证据满足当前页面条件。

任一项不通过即停止。执行适配器不得把默认值、上一页结果或自身推测当作补全。

无外部资产须由B显式声明 `asset_used: []` 和 `outer_template.evidence_reference_id: no_external_asset`；C `template_identity.evidence_reference_id`/`master_asset_path` 同为 `no_external_asset`、`master_asset_exists_and_readable: no`，选定参考与编译references均空。若已有执行回执则 `reference_paths_actually_attached: []`，未执行不虚填回执；既有description/证据说明理由。token不是路径，不豁免主视觉、校准或授权，不能绕过已声明文件缺失或参考锁定所需真实主参考。

## 提示结构

中文提示词按“页面任务—保留项—仅修改或生成项—参考用途—技术参数—负面约束—局部修改边界”组织。保留与修改范围必须清晰分开，禁止把解释性笔记写进图像可见文字。

负面约束只列 3—5 条与当前页面直接相关的硬禁项，不堆叠泛化风格词。不得使用固定图片占比或面积区间代替教学和阅读判断。

## Reference Inputs

逐个复制 B区选定的真实文件路径，并在执行回执中记录实际附加路径。禁止只写“参考原图”，禁止附加整个目录、联系表、待批/禁用/未选参考、失败图或隐式最近对话图片；上一页/代表页图仅在 B明确选为本页骨架参考且继承证明完整时例外附加，获准用途/范围须与实际附件一致。

`reference_locked_full_page` 必须实际附加已确认主要参考，禁止纯文本执行。每个参考分别写明必须继承和不得继承的内容。

## Verbatim Text

先核对A区 `must_show_items` 在B既有 `reading_order`、`text_realization_strategy`、`main_visual_description` 中已完整映射到全部状态、其他状态去向明确；B `main_execution_plan.must_show_text_verbatim` 仅列**当前实际状态**的准确文字子集，C逐字编译该子集。不得改写、混入批注或把其他状态内容统统塞入同图。必呈不等于全时同屏；当前状态/分配不明退B澄清，不由C猜测、删除教学要求或用“动画稍后再补”掩盖设计空白。当前状态全部文字由 GPT Image 直接生成；初次生成后最多两次局部文字修订，禁止确定性文字覆盖。

页、状态、镜头不自动一一对应。当前静态样张按该实际状态逐图验收，未生成状态、状态切换、运动与跨状态阅读效果保持未验证，不把旧静态记录自动升级为动态设计。当前状态成图不等于全页媒体完成，单张通过不释放未验证状态或冒称整页/批次通过。状态说明不扩大列名页面各一次首轮授权，追加状态图、局部修订或重新生成仍须原有具体授权；文件可用页ID加状态后缀，不改page_id。

## 输出参数

- 目标能力：`GPT Image`；
- 请求模型：`gpt-image-2`；
- 实际执行模型：只按明确回执填写，否则为 `未报告`；
- 完整课程视觉页默认 `opaque`；
- `transparent` 仅用于明确需要 Alpha 的素材层、抠图对象或叠加组件，格式为 `png` 或 `webp`；
- 必须真实 Alpha 的任务不可降级为不透明输出。

## 批次隔离

跨批使用隔离上下文，同批在同一 C对话连续执行；每页按固定基准加本页差异，不把历史或上一张结果升级为参考授权或基准。代表页可在 `ready_for_representative_calibration` 状态且明确获该页生图授权后执行一次校准；其他页面必须等到 `batch_calibration.state: frozen_for_execution`、`human_confirmation: confirmed` 和 `C_adapter_handoff.readiness: ready_for_C`。一次`授权连续生成`只覆盖列明页面各一次首轮生成。批次之间不得共享生成图或隐式上下文。

## 局部修改

合同必须包含 `保留项`、`仅修改项`、`禁止修改项`和`最小修改指令`。若最小修改仍需改变教学关系、模板、核心骨架、主视觉定义或参考角色，停止生成；教学/分页问题回A，具体视觉实现问题回B。

## 哈希禁令

不得计算、记录、传递或推荐哈希、摘要或指纹。资产身份使用参考编号、真实路径、文件名、尺寸、模板版本、参考角色和确认记录。
