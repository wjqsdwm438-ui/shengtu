# 《企业内部全流程物流体系》A线页面方向预判与正式交接

## 1. 状态与阶段边界

- 当前阶段：A线正式产物。
- 唯一S线输入：`E:\shengtu\skills-v2.7-development-snapshot-20260814\企业全流程_S线媒介路由.md`。
- 处理范围：仅QL-01～QL-23；EF-01与EF-21维持Non-A。
- 页数与顺序：23页连续冻结，不合并、不拆分、不重排。
- 用户确认方案：**方案二：精品升级版**。
- 阶段边界：本文件完成A线冻结与B线接收准备；不进入B/T/C线，不写平台提示词，不生成图像。

## 2. 用户可读结论

### 当前判断

本课是“总览—四章五页—对照—迁移”的系列课程。四章统一采用“定义→流程→问题→数字化方案→口诀”，核心任务是在固定课程母版内建立稳定但不机械重复的五类主体框原型。

### 主要问题

1. 四章结构相似，若只换字会产生明显复制感。
2. 流程、问题、方案和口诀的内容关系不同，不能共用一种主体排法。
3. 数字化页面需要科技气质，但版式2和新增样张均为扁平PNG，不能冒充分层母版或承诺像素锁定。
4. 标题不计入正文预算；正文必须足以支撑约40秒讲解，不机械压缩到平均20字。

### 三版方案与确认

- **方案一：稳妥优化版**：固定框架内做必要调整，稳定但重复感较强。
- **方案二：精品升级版**：固定外层身份，主体框按教学动作采用成熟信息原型；兼顾统一、辨识度和制作可行性。
- **方案三：现代重排版**：保留课程身份但大幅开放主体区，冲击力强、制作成本高。
- 三版怎么选：稳定优先选一，品质与统一兼顾选二，接受大幅重排选三。
- 我建议的优先选择：方案二。
- 用户确认的最终方案：**方案二：精品升级版**。
- 最终方案确认依据：用户先确认方案二，随后确认新增目录作为系列成品样张/主体框排版参考库，不替代版式1 PSD。

## 3. 参考体系与模板身份

- `reference_set_id`：`RS-EnterpriseFlow-20260827-v2`。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `reference_folder`：`E:\shengtu\智能物流\样片版式`。
- 新增系列样张库：`E:\shengtu\智能物流\生图输出\参考`。
- 补充构图参考：`E:\shengtu\智能物流\样片版式\补充\微课截图`。
- `template_id`：`WL-L1`。
- `template_version`：`WL-L1-EnterpriseFlow-v2.0`；因新增系列成品样张库而建立新参考版本，不静默迁移其他课程页面。
- `layered_master_available`：yes；PSD只用于理解和继承固定外层边界。
- `flattened_png_fallback_gate`：not required；主母版PSD存在。版式2及新增样张仅作非分层参考，不声明可编辑层或像素级锁定。
- `reference_selection_confirmation`：confirmed。

### 3.1 六类参考分类

1. 固定外层母版：版式1.psd。
2. 母版预览：版式1位置、变化、纯背景及通用标题PNG。
3. 内层排版参考：新增生图输出样张；按左图右文、流程路径、问题诊断、输入—动作—结果、分类决策、总览全景选用。
4. 内容或素材参考：本轮无必须保留的真实内容素材；参考页中的车辆、食品、仓库只说明载体类型。
5. 失败诊断图：无。文件名含`raw`不自动判定为失败图。
6. 无关或拒绝参考：参考页原文、原知识结论、异课程产品素材、播放器/字幕/教师窗及生成瑕疵。

### 3.2 统一继承与禁止继承

- `reference_inherit`：固定标题系统、浅蓝物流课程身份、外框与安全边距；局部继承主体框的信息结构、图文比例、路径方向、证据—结论层级。
- `reference_forbid_inherit`：原页标题正文、原课程事实、具体产品或运输策略、异课程颜色字体与装饰、教师小窗、字幕、播放器控件、生成错误和文字描边瑕疵。
- 每页一个主要外层母版，最多一个局部样张参考；不使用‘综合吸收’或不受控混合。

## 4. 系列级冻结策略

- `internal_page_type_top1`：`A16_既有母版套新内容型`。理由：用户要求沿用既有母版，同时更换本课内容和主体框信息结构。
- `internal_page_type_top2`：`A15_系列模板改字型`。未成为主选：本课并非只改标题正文，流程、诊断、机制和分支页都需要新的主体视觉关系。
- `production_mode`：`reference_locked`。
- `output_target`：`full_page_with_text`。
- `text_generation_strategy`：`带字`。
- `material_policy`：不保留参考页原学科素材；允许围绕本课业务对象进行AI重绘，但必须服从版式与内容事实。
- `keep_real_material`：no；`allow_ai_redraw_subject`：yes；`need_no_text_layout_skeleton`：no。
- 标题系统：沿用本门课程固定标题资产；标题不计入正文预算。
- 正文策略：以完整教学句、关系标签和必要结论共同上屏；根据教学动作动态控制，不死板追求统一字数。
- 标点策略：中文全角标点；流程统一使用`→`；引号内核心词保持原意。
- 系列节奏：定义页强调边界，流程页强调方向，问题页强调诊断，方案页强调机制，口诀页强调记忆锚点。

## 5. 主体框原型与亮区规则

| 原型 | 名称 | 内容关系 | 主视觉载体 | 第一焦点 | 第二焦点 | light_region_summary |
|---|---|---|---|---|---|---|
| P1 | 系列总览/全景闭环型 | 多模块并列后汇入一个企业物流闭环 | 四模块节点、方向箭头与中心闭环/企业经营结果 | 四类物流构成的闭环主图 | 各模块分工及共同结果 | 顶部保留固定标题区；主体以大面积浅色全景区承载闭环；说明文字靠近对应节点；保留外框安全边距。 |
| P2 | 概念边界左图右文型 | 业务场景/对象与定义、边界、价值并列解释 | 左侧物流场景或对象组图，右侧三层解释 | 左侧业务对象与物流场景 | 右侧定义边界与价值结论 | 固定标题下方保留完整浅色主体框；左侧为主图浅区，右侧为三段文字浅区；结论保持最高文字对比。 |
| P3 | 完整流程/路径型 | 不可拆分的时序链或连续物流路径 | 节点图标、方向箭头、路径与终点结果 | 从起点到终点的连续路径 | 流程结果或关键控制句 | 主体框内优先留给连续路径；节点标签置于浅色承载区；起点、终点与关键结果保持清晰间隔。 |
| P4 | 问题诊断型 | 多个业务痛点并列，并共同指向经营后果 | 问题场景/图标组、分层问题文字和结果带 | 痛点组及其差异 | 共同根因或业务后果 | 主体分为问题证据区和解释区；问题标签保持等权；底部或末端保留共同后果浅色结论带。 |
| P5 | 数字化机制输入—动作—结果型 | 业务输入或问题，经系统能力处理，形成可验证结果 | 三阶段面板、系统图标、连接关系和结果区 | 系统能力如何处理业务问题 | 数字化结果与管理价值 | 标题下保留三阶段浅色信息区；中部系统动作最突出；输入与结果分别置于两侧或上下游，避免面板等权。 |
| P6 | 独立口诀大结论型 | 单一记忆结论加一条解释支撑 | 大结论框、关键词和单一代表图形 | 完整口诀 | 口诀对应的业务意义 | 固定标题下设置单一大结论浅区；代表图形只作辅助；禁止教师小窗、字幕条和多卡片竞争。 |
| P7 | 分类决策/对照型 | 输入分类后分支处置，或多类型同页对照辨析 | 分类输入、判断节点、分支出口及总结带 | 分类判断与分支方向 | 各分支结果或判断方法 | 主体浅区按输入、判断、输出建立清晰层次；分支出口保持同级；底部总结带承载判断规则。 |

## 6. 逐页正式A线交接卡

### QL-01｜企业四大物流闭环

- `source_segment_id`：EF-02。
- `page_function / teaching_action`：建立供应、生产、销售、回收四大物流与企业闭环的认知地图。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用系列总览/全景闭环型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**企业四大物流闭环**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`企业四大物流闭环`
  - 正文：
    - `供应物流：源头进货，保障生产`
    - `生产物流：内部流转，提质降本`
    - `销售物流：终端出货，链接市场`
    - `回收物流：逆向闭环，盘活资源`
    - `四者环环相扣，共同影响生产成本、交付效率与资源利用率`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：82字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：多模块并列后汇入一个企业物流闭环。
- `carrier_method / main_visual_carrier`：四模块节点、方向箭头与中心闭环/企业经营结果。
- `first_visual_focus`：四类物流构成的闭环主图。
- `second_visual_focus`：各模块分工及共同结果。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：全景构图、节点间方向关系、图文比例和总分层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：顶部保留固定标题区；主体以大面积浅色全景区承载闭环；说明文字靠近对应节点；保留外框安全边距。
- `internal_risk_points`：四模块视觉等权会削弱闭环方向；必须用箭头和中心关系建立阅读顺序。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-02｜供应物流管什么

- `source_segment_id`：EF-03。
- `page_function / teaching_action`：识别供应物流的源头定位、对象和业务边界。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A14_流程路径信息图型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内改用“厂内六节点连续路径”；本页教学动作同时要求看清企业内部边界、业务范围和价值，旧左图右文结构只能解释概念，不能直观看出货物从原料仓到成品库的连续流转。
- `title_strategy / main_title_candidate`：结论先行的短标题；**供应物流管什么**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`供应物流管什么`
  - 正文：
    - `服务生产前端，负责原材料、零部件、辅助物资和设备耗材的采购、运输、验收、入库与仓储保管。`
    - `核心边界：从物资需求形成，到合格物资进入库存。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：67字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：企业内部边界统领六节点业务流程，完整定义与价值结论分别作为上下两级解释。
- `carrier_method / main_visual_carrier`：剖面式厂房内部场景、六个等距3D节点和一条连续蓝青色流线；节点依次为原料仓出库、搬运、工序流转、半成品暂存、组装、成品入库。
- `first_visual_focus`：六节点厂内物流连续路径，必须一眼读出“从仓库出库到成品入库”。
- `second_visual_focus`：顶部“企业内部”边界句与底部“生产效率与成本”价值结论。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-03_方案A_左图右文最终版_v04.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：左图右文比例、三层信息节奏、结论强调方式；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下方保留完整浅色主体框；左侧为主图浅区，右侧为三段文字浅区；结论保持最高文字对比。
- `internal_risk_points`：对象过多容易变成素材堆砌；主图只表达‘生产前端进货’。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-03｜供应物流五步作业链

- `source_segment_id`：EF-04。
- `page_function / teaching_action`：建立需求、采购、运输、验收、入库五步作业链。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用2×3六分区图文型；顺序由编号和冻结文字表达，不再额外绘制节点间关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**供应物流五步作业链**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`供应物流五步作业链`
  - 正文：
    - `物资需求→采购订单→供应商发货运输→质检点数验收→合格物资分类入库`
    - `结果：形成库存储备，等待生产领用`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：49字，低密度；仅计算上述正文，标题不计入。
- `content_relation`：六个节点按编号和冻结文字自然排序；不额外可视化节点间关系。
- `carrier_method / main_visual_carrier`：2×3六分区图文模块；每区只用一个对应业务场景解释自身节点含义。
- `first_visual_focus`：六个清晰、独立、可数的节点部分。
- `second_visual_focus`：底部主线结论。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-05 已逐页生成.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：路径组织、节点层级、箭头方向和阶段揭示顺序；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体框内优先留给连续路径；节点标签置于浅色承载区；起点、终点与关键结果保持清晰间隔。
- `internal_risk_points`：五节点名称较长；不得缩小到难以阅读，也不得把验收和入库合并。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-04｜传统供应物流四类痛点

- `source_segment_id`：EF-05A。
- `page_function / teaching_action`：识别盲目采购、物资积压、物料短缺、验收低效四类痛点。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用问题诊断型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**传统供应物流四类痛点**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`传统供应物流四类痛点`
  - 正文：
    - `盲目采购：需求判断不准`
    - `物资积压：库存占用资金`
    - `物料短缺：影响生产连续性`
    - `验收低效：到货核查耗时`
    - `根因：需求、到货与库存信息彼此割裂`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：62字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：多个业务痛点并列，并共同指向经营后果。
- `carrier_method / main_visual_carrier`：问题场景/图标组、分层问题文字和结果带。
- `first_visual_focus`：痛点组及其差异。
- `second_visual_focus`：共同根因或业务后果。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-13_方案A_参考锁定版_v01.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：问题分组、场景证据与结果结论的层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体分为问题证据区和解释区；问题标签保持等权；底部或末端保留共同后果浅色结论带。
- `internal_risk_points`：四项问题容易被画成四个无关系图标；必须增加共同根因结论。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-05｜供应物流数字化升级

- `source_segment_id`：EF-05B。
- `page_function / teaching_action`：说明采购系统、WMS和供应商平台如何支持预判、追踪和预警。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用数字化机制输入—动作—结果型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**供应物流数字化升级**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`供应物流数字化升级`
  - 正文：
    - `采购管理系统：智能预判物资需求`
    - `WMS：记录入库与库存变化，自动预警`
    - `供应商协同平台：追踪订单与到货轨迹`
    - `形成“需求可预测、到货可追踪、库存可预警”的供应协同机制`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：78字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：业务输入或问题，经系统能力处理，形成可验证结果。
- `carrier_method / main_visual_carrier`：三阶段面板、系统图标、连接关系和结果区。
- `first_visual_focus`：系统能力如何处理业务问题。
- `second_visual_focus`：数字化结果与管理价值。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-16_方案A_参考锁定版_v01_raw.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：输入—处理—输出结构、阶段顺序、能力与结果对应关系；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：标题下保留三阶段浅色信息区；中部系统动作最突出；输入与结果分别置于两侧或上下游，避免面板等权。
- `internal_risk_points`：系统名称不能只做装饰标签；每个系统必须与能力、结果形成对应。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-06｜供应物流核心口诀

- `source_segment_id`：EF-06。
- `page_function / teaching_action`：记住供应物流的核心分工与价值。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用独立口诀大结论型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**供应物流核心口诀**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`供应物流核心口诀`
  - 正文：
    - `供应物流管“进货”，守住企业生产的第一道关口。`
    - `先保障物资按质、按量、按时到位，生产活动才有稳定起点。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：50字，低密度；仅计算上述正文，标题不计入。
- `content_relation`：单一记忆结论加一条解释支撑。
- `carrier_method / main_visual_carrier`：大结论框、关键词和单一代表图形。
- `first_visual_focus`：完整口诀。
- `second_visual_focus`：口诀对应的业务意义。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\样片版式\补充\微课截图\118.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：大结论层级、关键词强调和留白比例；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下设置单一大结论浅区；代表图形只作辅助；禁止教师小窗、字幕条和多卡片竞争。
- `internal_risk_points`：口诀页不得退化成字幕页；解释句不能抢夺口诀焦点。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-07｜生产物流管什么

- `source_segment_id`：EF-07。
- `page_function / teaching_action`：识别生产物流的企业内部边界及效率、成本价值。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A14_流程路径信息图型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内改用“厂内六节点连续路径”；本页教学动作同时要求看清企业内部边界、业务范围和价值，旧左图右文结构只能解释概念，不能直观看出货物从原料仓到成品库的连续流转。
- `title_strategy / main_title_candidate`：结论先行的短标题；**生产物流管什么**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`生产物流管什么`
  - 正文：
    - `生产物流发生在企业内部，负责原材料和零部件从仓库出库后，在工序、工位之间流转、搬运、暂存和组装，直至成品入库。`
    - `它不创造新产品，却直接影响生产效率与成本。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：76字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：企业内部边界统领六节点业务流程，完整定义与价值结论分别作为上下两级解释。
- `carrier_method / main_visual_carrier`：剖面式厂房内部场景、六个等距3D节点和一条连续蓝青色流线；节点依次为原料仓出库、搬运、工序流转、半成品暂存、组装、成品入库。
- `first_visual_focus`：六节点厂内物流连续路径，必须一眼读出“从仓库出库到成品入库”。
- `second_visual_focus`：顶部“企业内部”边界句与底部“生产效率与成本”价值结论。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\成品\KP-10_方案A_S形动态冷链路径_v01.png`（只借鉴连续路径与节点节奏）；`E:\shengtu\智能物流\生图输出\成品\KP-22_方案A_一体化物流全景_v02.png`（只借鉴等距物流对象与蓝白材质）。
- `reference_inherit`：固定母版标题、外框、浅蓝课程身份和安全边距；借鉴成熟成品的连续流线、等距3D对象、蓝青主色与结论强调，不继承其配送知识和对象语义。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下先放“生产物流发生在企业内部”短定义；中部用厂房剖面承载六节点连续路径；底部左侧放完整范围说明，底部右侧放高对比价值结论。
- `internal_risk_points`：一是不得把六节点画成彼此孤立的六张卡片，必须由连续流线串联；二是不得出现公路、长途货车和对外配送；三是生产设备只能作环境，不能把主题误画成智能制造；四是六个节点标签与冻结正文必须逐字复核。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文；固定母版不降级；两张补充参考分工明确且不继承知识内容；流程载体能直接支撑“边界—范围—价值”教学动作。

### QL-08｜生产物流六节点流转

- `source_segment_id`：EF-08。
- `page_function / teaching_action`：建立原料出库至成品入库的内部流转链。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用完整流程/路径型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**生产物流六节点流转**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`生产物流六节点流转`
  - 正文：
    - `库存原料按需出库→车间智能转运→各工序加工流转→半成品临时仓储→成品组装质检→成品入库`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：42字，低密度；仅计算上述正文，标题不计入。
- `content_relation`：六个节点按编号和冻结文字自然排序；不额外可视化节点间关系。
- `carrier_method / main_visual_carrier`：2×3六分区图文模块；每区只用一个对应业务场景解释自身节点含义。
- `first_visual_focus`：六个清晰、独立、可数的节点部分。
- `second_visual_focus`：各节点标题与对应业务场景的清晰匹配。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1纯背景.png`。
- `secondary_references`：`E:\shengtu\智能物流\样片版式\版式1位置.png`（锁定标题与内容版心）；`E:\shengtu\智能物流\样片版式\通用标题.png`（锁定标题条资产）。
- `reference_inherit`：固定底板、白色主体框、底部蓝栏及装饰短线、标题条位置与造型；主体内部采用2×3统一模块、清晰编号和单模块图文对应。明确禁止参考QL-07。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体框内使用两行三列六个缩小后的独立图文区；删除主线结论，主体区底部留白并保持固定蓝色底栏不漂移。
- `internal_risk_points`：不得添加箭头、连线、道路、轨道、传送带、时间轴、流线或折返路径；不得参考或继承QL-07；六区图片只解释各自文字含义。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-09｜传统生产物流四类瓶颈

- `source_segment_id`：EF-09A。
- `page_function / teaching_action`：识别动线混乱、物料堆积、搬运低效和工序断层。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用1×4横向四分区诊断型；四类瓶颈各自用独立插图解释，结果另设窄文字区，不额外绘制跨区关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**传统生产物流四类瓶颈**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`传统生产物流四类瓶颈`
  - 正文：
    - `动线混乱：运输路线相互干扰`
    - `物料堆积：工序前后节拍失衡`
    - `人工搬运低效：耗时且差错风险高`
    - `工序衔接断层：等待时间拉长`
    - `结果：生产周期延长，人工与仓储损耗增加`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：73字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：四类业务瓶颈并列呈现；经营后果仅由底部结果文字说明，不增加汇聚关系示意。
- `carrier_method / main_visual_carrier`：1×4横向独立图文分区；每区上部为轻写实等距插图，下部为编号、瓶颈名称和解释文字；四区下方为窄结果文字区。
- `first_visual_focus`：四个等权、清晰可数的瓶颈分区。
- `second_visual_focus`：底部共同结果文字。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1纯背景.png`。
- `secondary_references`：`E:\shengtu\智能物流\样片版式\版式1位置.png`（锁定标题与内容版心）；`E:\shengtu\智能物流\样片版式\通用标题.png`（锁定标题条）；`E:\shengtu\智能物流\生图输出\成品\智慧物流运输与配送_C线样张_KP-19_方案A_左图右文道路纠偏场景版_v01_raw.png`（只借鉴插图质感与局部异常强调，不继承左图右文结构）。
- `reference_inherit`：固定底板、白色主体框、底部蓝栏、标题条位置与造型；主体采用1×4统一插图风格、统一图文比例和窄结果文字区。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：白色主体框内横向排列四个独立图文区，每区插图约65%、文字约35%；四区下方设置窄结果文字区；固定底部蓝栏不承载文字。
- `internal_risk_points`：四列文字不得溢出；插图必须统一视角、人物比例、线条与光影；图片只解释本区内容；禁止箭头、连线、汇聚线和跨区场景；橙色只作局部异常强调。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-10｜智慧工厂打通内部流转

- `source_segment_id`：EF-09B。
- `page_function / teaching_action`：说明AGV、智能动线和数字调度如何实现精准配送与工序衔接。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用数字化机制输入—动作—结果型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**智慧工厂打通内部流转**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`智慧工厂打通内部流转`
  - 正文：
    - `AGV搬运机器人：按任务精准配送`
    - `智能动线规划：优化车间运输路径`
    - `数字化生产调度：协调物料与工序节拍`
    - `实现物料精准到位、工序无缝衔接，缩短生产周期并降低损耗`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：75字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：业务输入或问题，经系统能力处理，形成可验证结果。
- `carrier_method / main_visual_carrier`：三阶段面板、系统图标、连接关系和结果区。
- `first_visual_focus`：系统能力如何处理业务问题。
- `second_visual_focus`：数字化结果与管理价值。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-16_方案A_参考锁定版_v01_raw.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：输入—处理—输出结构、阶段顺序、能力与结果对应关系；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：标题下保留三阶段浅色信息区；中部系统动作最突出；输入与结果分别置于两侧或上下游，避免面板等权。
- `internal_risk_points`：技术图标容易喧宾夺主；必须突出‘技术如何改变流转’而非设备陈列。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-11｜生产物流核心口诀

- `source_segment_id`：EF-10。
- `page_function / teaching_action`：记住生产物流的核心分工与价值。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用独立口诀大结论型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**生产物流核心口诀**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`生产物流核心口诀`
  - 正文：
    - `生产物流管“内部流转”，是企业降本增效的关键。`
    - `物料流转越顺畅，工序等待越少，生产效率才能持续提升。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：49字，低密度；仅计算上述正文，标题不计入。
- `content_relation`：单一记忆结论加一条解释支撑。
- `carrier_method / main_visual_carrier`：大结论框、关键词和单一代表图形。
- `first_visual_focus`：完整口诀。
- `second_visual_focus`：口诀对应的业务意义。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\样片版式\补充\微课截图\118.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：大结论层级、关键词强调和留白比例；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下设置单一大结论浅区；代表图形只作辅助；禁止教师小窗、字幕条和多卡片竞争。
- `internal_risk_points`：关键词较长；‘内部流转’与‘降本增效’需要形成主次而非等权。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-12｜销售物流管什么

- `source_segment_id`：EF-11。
- `page_function / teaching_action`：识别销售物流的订单履约边界和市场价值。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用概念边界左图右文型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**销售物流管什么**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`销售物流管什么`
  - 正文：
    - `销售物流连接企业库存与市场，负责成品从订单处理、打包分拣、出库运输、终端配送到客户签收的履约过程。`
    - `核心价值：把库存商品转化为按时、准确的客户交付。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：73字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：业务场景/对象与定义、边界、价值并列解释。
- `carrier_method / main_visual_carrier`：左侧物流场景或对象组图，右侧三层解释。
- `first_visual_focus`：左侧业务对象与物流场景。
- `second_visual_focus`：右侧定义边界与价值结论。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-17_方案A_左图右文场景版_v04_raw.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：左图右文比例、三层信息节奏、结论强调方式；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下方保留完整浅色主体框；左侧为主图浅区，右侧为三段文字浅区；结论保持最高文字对比。
- `internal_risk_points`：不要把销售物流画成销售业务；主图必须表达成品履约与终端交付。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-13｜销售物流六步履约闭环

- `source_segment_id`：EF-12。
- `page_function / teaching_action`：建立订单处理至客户签收的履约闭环。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用完整流程/路径型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**销售物流六步履约闭环**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`销售物流六步履约闭环`
  - 正文：
    - `接收客户订单→成品拣货打包→智能分拣出库→干线运输或同城配送→终端交付签收→订单闭环`
    - `客户体验取决于每个节点的速度、准确性与可视性`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：64字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：不可拆分的时序链或连续物流路径。
- `carrier_method / main_visual_carrier`：节点图标、方向箭头、路径与终点结果。
- `first_visual_focus`：从起点到终点的连续路径。
- `second_visual_focus`：流程结果或关键控制句。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-10_方案A_S形动态冷链路径_v01.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：路径组织、节点层级、箭头方向和阶段揭示顺序；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体框内优先留给连续路径；节点标签置于浅色承载区；起点、终点与关键结果保持清晰间隔。
- `internal_risk_points`：S形路径只继承阅读方向；禁止继承冷链产品和温控主题。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-14｜传统销售物流履约痛点

- `source_segment_id`：EF-13A。
- `page_function / teaching_action`：识别销售物流的履约问题与客户后果。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用问题诊断型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**传统销售物流履约痛点**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`传统销售物流履约痛点`
  - 正文：
    - `人工分拣低效：爆单时容易积压`
    - `配送时效不稳：延迟影响客户体验`
    - `订单轨迹不透明：异常难以及时处理`
    - `错发漏发：增加补发与售后成本`
    - `结果：履约成本上升，企业口碑受损`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：75字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：多个业务痛点并列，并共同指向经营后果。
- `carrier_method / main_visual_carrier`：问题场景/图标组、分层问题文字和结果带。
- `first_visual_focus`：痛点组及其差异。
- `second_visual_focus`：共同根因或业务后果。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-19_方案A_左图右文道路纠偏场景版_v01_raw.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：问题分组、场景证据与结果结论的层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体分为问题证据区和解释区；问题标签保持等权；底部或末端保留共同后果浅色结论带。
- `internal_risk_points`：不能把全部问题压成道路异常；分拣、轨迹和错漏必须各有证据。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-15｜销售物流数字化履约

- `source_segment_id`：EF-13B。
- `page_function / teaching_action`：说明TMS、智能分拣、AI路径规划和可视追踪如何提升履约。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用数字化机制输入—动作—结果型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**销售物流数字化履约**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`销售物流数字化履约`
  - 正文：
    - `TMS：统一运输调度与运力匹配`
    - `智能分拣设备：提高出库速度与准确率`
    - `AI路径规划：优化配送路线`
    - `可视化追踪：实时掌握订单状态`
    - `实现快速、准确、可视的全链路履约`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：75字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：业务输入或问题，经系统能力处理，形成可验证结果。
- `carrier_method / main_visual_carrier`：三阶段面板、系统图标、连接关系和结果区。
- `first_visual_focus`：系统能力如何处理业务问题。
- `second_visual_focus`：数字化结果与管理价值。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-15_四层拆分_v01\KP-15_四层重组预览_v01.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：输入—处理—输出结构、阶段顺序、能力与结果对应关系；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：标题下保留三阶段浅色信息区；中部系统动作最突出；输入与结果分别置于两侧或上下游，避免面板等权。
- `internal_risk_points`：四项能力较多；应建立从订单输入到履约结果的主线，避免功能列表化。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-16｜销售物流核心口诀

- `source_segment_id`：EF-14。
- `page_function / teaching_action`：记住销售物流的核心分工与价值。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用独立口诀大结论型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**销售物流核心口诀**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`销售物流核心口诀`
  - 正文：
    - `销售物流管“出货交付”，是企业链接市场、创造收益的桥梁。`
    - `只有把正确的商品按时送到客户手中，销售才真正完成。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：53字，低密度；仅计算上述正文，标题不计入。
- `content_relation`：单一记忆结论加一条解释支撑。
- `carrier_method / main_visual_carrier`：大结论框、关键词和单一代表图形。
- `first_visual_focus`：完整口诀。
- `second_visual_focus`：口诀对应的业务意义。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\样片版式\补充\微课截图\118.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：大结论层级、关键词强调和留白比例；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下设置单一大结论浅区；代表图形只作辅助；禁止教师小窗、字幕条和多卡片竞争。
- `internal_risk_points`：桥梁隐喻只作辅助；不能替代出货交付的业务含义。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-17｜回收物流管什么

- `source_segment_id`：EF-15。
- `page_function / teaching_action`：识别回收物流的逆向边界、处理对象和闭环作用。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用概念边界左图右文型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**回收物流管什么**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`回收物流管什么`
  - 正文：
    - `回收物流也叫逆向物流，处理客户退换货、残次产品、生产废料、包装耗材和滞销库存。`
    - `它负责回收、运输、质检、分类及复用或报废处置，把单向交付补成企业物流闭环。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：76字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：业务场景/对象与定义、边界、价值并列解释。
- `carrier_method / main_visual_carrier`：左侧物流场景或对象组图，右侧三层解释。
- `first_visual_focus`：左侧业务对象与物流场景。
- `second_visual_focus`：右侧定义边界与价值结论。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-18_方案A_左图右文冷链场景版_v01_raw.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：左图右文比例、三层信息节奏、结论强调方式；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下方保留完整浅色主体框；左侧为主图浅区，右侧为三段文字浅区；结论保持最高文字对比。
- `internal_risk_points`：只继承左图右文结构；禁止继承冷链场景，主图改为多类逆向返回物。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-18｜回收物流分类处置链

- `source_segment_id`：EF-16。
- `page_function / teaching_action`：建立回运、质检、分类及多分支处置决策链。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用分类决策/对照型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**回收物流分类处置链**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`回收物流分类处置链`
  - 正文：
    - `退货申请→取件回运→仓库质检分类`
    - `完好商品→重新入库`
    - `瑕疵商品→维修复用`
    - `破损商品→合规报废`
    - `生产废料→回收再利用`
    - `关键动作：先质检分类，再决定去向`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：69字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：输入分类后分支处置，或多类型同页对照辨析。
- `carrier_method / main_visual_carrier`：分类输入、判断节点、分支出口及总结带。
- `first_visual_focus`：分类判断与分支方向。
- `second_visual_focus`：各分支结果或判断方法。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-14_四层拆分_v03\KP-14_四层重组预览_v03.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：分类—判断—输出结构、对照列关系和总结层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体浅区按输入、判断、输出建立清晰层次；分支出口保持同级；底部总结带承载判断规则。
- `internal_risk_points`：全课结构最复杂；主干与四分支必须同页可见且不发生箭头歧义。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-19｜传统回收物流三类痛点

- `source_segment_id`：EF-17A。
- `page_function / teaching_action`：识别流程混乱、处理缓慢和资源浪费等逆向物流痛点。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用问题诊断型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**传统回收物流三类痛点**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`传统回收物流三类痛点`
  - 正文：
    - `流程混乱：退货状态难追踪`
    - `处理缓慢：商品长期滞留`
    - `资源浪费：可复用物资未被识别`
    - `进一步造成库存失真、经营损耗增加和合规风险。`
    - `根因：逆向信息、质检和库存处置没有形成统一闭环`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：82字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：多个业务痛点并列，并共同指向经营后果。
- `carrier_method / main_visual_carrier`：问题场景/图标组、分层问题文字和结果带。
- `first_visual_focus`：痛点组及其差异。
- `second_visual_focus`：共同根因或业务后果。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-19_方案A_左图右文道路纠偏场景版_v01_raw.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：问题分组、场景证据与结果结论的层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体分为问题证据区和解释区；问题标签保持等权；底部或末端保留共同后果浅色结论带。
- `internal_risk_points`：问题与后果层级较多；必须突出三类痛点，根因与后果降为第二焦点。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-20｜回收物流数字化闭环

- `source_segment_id`：EF-17B。
- `page_function / teaching_action`：说明溯源、智能质检和自动回仓如何形成经营与合规闭环。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用数字化机制输入—动作—结果型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**回收物流数字化闭环**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`回收物流数字化闭环`
  - 正文：
    - `逆向物流平台：统一退货任务与状态`
    - `全程溯源：记录商品返回路径`
    - `智能质检：快速判断处置方式`
    - `自动回仓：同步更新可售与待处理库存`
    - `实现缩短周期、盘活库存、回收资源并满足合规要求`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：82字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：业务输入或问题，经系统能力处理，形成可验证结果。
- `carrier_method / main_visual_carrier`：三阶段面板、系统图标、连接关系和结果区。
- `first_visual_focus`：系统能力如何处理业务问题。
- `second_visual_focus`：数字化结果与管理价值。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\智慧物流运输与配送_C线样张_KP-20_方案A_参考锁定版_v01.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：输入—处理—输出结构、阶段顺序、能力与结果对应关系；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：标题下保留三阶段浅色信息区；中部系统动作最突出；输入与结果分别置于两侧或上下游，避免面板等权。
- `internal_risk_points`：闭环箭头必须回到库存与处置体系，不能只做线性四步流程。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-21｜回收物流核心口诀

- `source_segment_id`：EF-18。
- `page_function / teaching_action`：记住回收物流的核心分工与价值。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用独立口诀大结论型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**回收物流核心口诀**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`回收物流核心口诀`
  - 正文：
    - `回收物流管“逆向闭环”，盘活企业资源，降低经营损耗。`
    - `让可售商品重新入库、可用物资再次利用、报废物资合规退出。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：54字，低密度；仅计算上述正文，标题不计入。
- `content_relation`：单一记忆结论加一条解释支撑。
- `carrier_method / main_visual_carrier`：大结论框、关键词和单一代表图形。
- `first_visual_focus`：完整口诀。
- `second_visual_focus`：口诀对应的业务意义。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\样片版式\补充\微课截图\118.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：大结论层级、关键词强调和留白比例；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：固定标题下设置单一大结论浅区；代表图形只作辅助；禁止教师小窗、字幕条和多卡片竞争。
- `internal_risk_points`：口诀包含三个价值动作；主标题仍以‘逆向闭环’为唯一核心。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-22｜四大物流分工对照

- `source_segment_id`：EF-19。
- `page_function / teaching_action`：对照四大物流的核心分工并形成辨析方法。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用分类决策/对照型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**四大物流分工对照**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`四大物流分工对照`
  - 正文：
    - `供应物流：进货，保障生产`
    - `生产物流：内部流转，提质降本`
    - `销售物流：出货交付，链接市场`
    - `回收物流：逆向闭环，盘活资源`
    - `判断方法：看物资处于进入、内部、输出还是返回企业的哪一段`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：82字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：输入分类后分支处置，或多类型同页对照辨析。
- `carrier_method / main_visual_carrier`：分类输入、判断节点、分支出口及总结带。
- `first_visual_focus`：分类判断与分支方向。
- `second_visual_focus`：各分支结果或判断方法。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\kp06.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：分类—判断—输出结构、对照列关系和总结层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：主体浅区按输入、判断、输出建立清晰层次；分支出口保持同级；底部总结带承载判断规则。
- `internal_risk_points`：四项必须同级对照；不得因图形大小造成某一物流被误判为主流程。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

### QL-23｜从线性作业到企业物流闭环

- `source_segment_id`：EF-20。
- `page_function / teaching_action`：建立四模块相互依存及智能化、标准化、闭环化升级观。
- `standalone_page_worthy`：yes；页序与教学动作已由S线冻结。
- `internal_page_type_top1`：`A16_既有母版套新内容型`。
- `internal_page_type_top2`：`A15_系列模板改字型`。
- `internal_routing_reason`：固定外层母版不变，在主体框内采用系列总览/全景闭环型；Top2不足以表达新的内容关系。
- `title_strategy / main_title_candidate`：结论先行的短标题；**从线性作业到企业物流闭环**。
- `subtitle_or_lead_needed`：no。
- `must_show_text_verbatim`：
  - 标题：`从线性作业到企业物流闭环`
  - 正文：
    - `供应物流提供生产起点，生产物流完成内部转化，销售物流兑现市场交付，回收物流让资源返回体系。`
    - `四大模块相互依存，推动传统人工物流向智能化、标准化、闭环化升级。`
- `optional_on_screen_text`：无；不得用新增解释扩大S线教学动作。
- `do_not_show_content`：原讲稿中的过渡话、教师口语、参考页原文和非本页知识点。
- `text_budget`：77字，中密度；仅计算上述正文，标题不计入。
- `content_relation`：多模块并列后汇入一个企业物流闭环。
- `carrier_method / main_visual_carrier`：四模块节点、方向箭头与中心闭环/企业经营结果。
- `first_visual_focus`：四类物流构成的闭环主图。
- `second_visual_focus`：各模块分工及共同结果。
- `primary_layout_reference`：`E:\shengtu\智能物流\样片版式\版式1.psd`。
- `secondary_references`：`E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png`；每页仅绑定这一张局部样张。
- `reference_inherit`：全景构图、节点间方向关系、图文比例和总分层级；同时继承固定母版标题、外框、浅蓝课程身份和安全边距。
- `reference_forbid_inherit`：样张原文字、原课程事实、具体学科素材、异课程装饰、教师窗、字幕、播放器及生成瑕疵。
- `material_policy`：替换为本页物流业务对象的AI重绘示意；参考图只提供载体和结构。
- `light_region_summary`：顶部保留固定标题区；主体以大面积浅色全景区承载闭环；说明文字靠近对应节点；保留外框安全边距。
- `internal_risk_points`：不得与QL-01重复；本页重点是升级方向与相互依存，而不是再次介绍四个定义。
- `frozen_items`：页码、顺序、教学动作、标题、正文、固定外层母版、局部参考角色、带字完整页目标。
- `user_gate_needed`：no。
- `risk_level`：medium（生产阶段按本页风险核对即可）。
- `gate_result`：pass；无超过180字正文，无母版降级或参考角色冲突。

## 7. 全局校验与交接结论

- 页面数量：23；QL-01～QL-23连续且唯一。
- 正文预算：最少49字，最多82字，平均68.7字；低密度6页，中密度17页，高密度0页，超过180字0页。
- 标题均未计入正文预算；文字长度随教学动作变化，没有机械统一为固定字数。
- 固定外层母版：23页全部使用版式1 PSD体系。版式2及新增样张只承担主体框结构或科技气质参考。
- 参考绑定：每页一个固定母版，至多一个局部样张；不存在多图不受控融合。
- 四条口诀：QL-06、QL-11、QL-16、QL-21均为独立完整课程页。
- Non-A边界：EF-01、EF-21未进入本文件逐页生产卡。
- `A_line_status`：complete。
- `B_line_handoff_ready`：yes。B线应接收本文件的系列级冻结策略、23页逐页必显文字、参考路径、主体原型、焦点、风险和Gate结果。
- 停止点：A线到此结束；本轮未进入B/T/C线。
