# 《企业内部全流程物流体系》QL-01｜B线重设计交接

```yaml
status: B线生产交接已就绪
page_scope: QL-01
source_A_line_card: E:\shengtu\skills-v2.7-development-snapshot-20260814\企业全流程_A线页面方向预判.md
candidate_policy: reference_locked_single_candidate
user_selected_T_line_candidate: 方案A_参考锁定版
user_selection_confirmation: confirmed
```

## 1. 本轮纠偏结论

- 本页重新设计内层图文关系，不沿用旧QL-01 B线中的“分散式文字锚点”描述。
- `KP-22_方案A_一体化物流全景_v02.png`只承担企业全景场景骨架，不承担标题框、文字位置、文字层级或装饰继承。
- 固定标题框、课程背景、白色主体框、安全边界和底部装饰只由`版式1.psd`控制。
- C线失败样张v01、v02只作为失败证据，不得进入T线或C线参考上下文。
- 页面只设置一个主视觉：单一企业物流园区全景。五段正文是同一解释层，不建立“总结句高于四类物流”的错误层级。

## 2. 参考选择与模板身份

```yaml
reference_selection:
  folder_path: E:\shengtu\智能物流\生图输出\参考
  discovered_images: 根目录发现14张栅格参考；本页只选择KP-22作为场景辅助参考
  primary_layout_reference: E:\shengtu\智能物流\样片版式\版式1.psd
  secondary_references:
    - E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png
  selection_reason: 固定母版提供唯一课程外层身份；KP-22仅提供成熟企业全景的景深、空间比例与场景载体
  rejected_references: 其他参考多为左图右文、流程、卡片或机制页，不符合本页单一企业全景；v01、v02为失败诊断图
  user_confirmation: confirmed
template_identity:
  template_id: WL-L1
  template_version: WL-L1-EnterpriseFlow-v2.0-QL01-BR1
```

### 非哈希参考清单

| reference_id | 真实路径 | 文件名 | 尺寸 | 模板版本 | 参考角色 | 用户确认 |
|---|---|---|---|---|---|---|
| QL01-MASTER | `E:\shengtu\智能物流\样片版式\版式1.psd` | `版式1.psd` | 1920×1080 | WL-L1-EnterpriseFlow-v2.0-QL01-BR1 | 固定外层母版、唯一标题系统 | confirmed |
| QL01-SCENE | `E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png` | `KP-22_方案A_一体化物流全景_v02.png` | 1920×1080 | WL-L1-EnterpriseFlow-v2.0-QL01-BR1 | 企业全景场景辅助参考 | confirmed |

不得计算、记录或传递文件哈希、摘要或指纹。

## 3. 参考继承边界

### 固定母版必须继承

- 1920×1080完整画布。
- `版式1.psd`的固定标题框、标题位置与课程标题系统。
- 浅蓝物流课程背景、白色主体框、安全边界及底部蓝色装饰带。
- 固定外层的空间比例和课程身份。

### KP-22仅允许继承

- 横向企业全景的空间景深。
- 左侧进场、中部作业、右侧企业建筑及右下前景的场景比例。
- 货物、车辆、仓库、生产作业区的前后景关系。
- 单一企业场景的统一光线、透视与蓝白科技质感。

### KP-22明确禁止继承

- KP-22标题框、标题位置、标题样式及标题文字。
- KP-22全部正文位置、文字锚点、字号关系和原排版层级。
- 原课程知识、原结论、原产品、冷链食品、云端与卫星图标。
- 品牌、伪文字、播放器、字幕、教师窗口及生成瑕疵。

## 4. 模板层清单与执行隔离

```yaml
template_layer_manifest:
  fixed_master: 标题框、标题位置、浅蓝背景、白色主体框、安全边界、底部装饰带
  variable_content: 企业物流园区全景、四类业务对象、五段带字说明
  optional_animation_layers: none
  user_confirmation: confirmed
flattened_png_fallback_gate:
  required: yes
  known_limitations: GPT Image使用受支持的无损栅格预览；PSD只用于理解并锁定外层边界，不承诺图层级或像素级一致
  user_confirmation: confirmed
context_isolation:
  explicit_reference_paths_only: yes
  include_previous_conversation_images: no
  include_failed_images_automatically: no
  include_entire_reference_folder: no
  explicitly_excluded_images:
    - 企业全流程_QL-01_方案A_参考锁定版_v01.png
    - 企业全流程_QL-01_方案A_参考锁定版_v02.png
```

## 5. 唯一候选｜方案A_参考锁定版

```yaml
production_goal: 固定课程母版内的完整带字企业物流全景页
page_type: A16_既有母版套新内容型
production_mode: reference_locked
output_target: full_page_with_text
primary_layout_reference: E:\shengtu\智能物流\样片版式\版式1.psd
secondary_references:
  - E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png
reference_attachment_required_in_C: yes
text_only_execution_forbidden: yes
text_generation_strategy: 带字
maximum_local_text_revisions: 2
deterministic_text_overlay_forbidden: yes
user_confirmation: confirmed
```

### 5.1 教学动作

在一个企业全景中识别供应、生产、销售、回收四类物流，并理解四者共同影响生产成本、交付效率与资源利用率。

### 5.2 主视觉与场景结构

- 主体框中心只保留一个连续的企业物流园区全景，不拆成四张图片或四张业务卡片。
- 左侧进场区域：原材料、零部件、供应车辆与收货月台，表达供应物流。
- 中部厂内区域：厂内转运、生产线与半成品流转，表达生产物流。
- 右上仓配区域：成品仓、装车月台与面向市场的出库车辆，表达销售物流。
- 右下返厂区域：退货箱、可回收包装、废旧物资与返厂搬运，表达回收物流。
- 四区通过同一企业园区的空间连续性自然建立联系；不使用中央圆环、圆形节点或复杂关系线。

### 5.3 五个固定文字锚点

企业全景是第一焦点。五段正文设置在主体框预留的干净外围白区，不覆盖车辆、厂房、生产线或关键作业对象：

```text
〔供应物流〕                       〔销售物流〕

                 企业全景

〔生产物流〕   〔四者环环相扣……〕   〔回收物流〕
```

- 左上锚点：供应物流。
- 右上锚点：销售物流。
- 左下锚点：生产物流。
- 下中锚点：整体说明。
- 右下锚点：回收物流。
- 五个锚点使用统一基线、统一边距和一致的视觉语言；不加卡片、底框、图标或编号。
- 锚点位置必须预留清晰留白，禁止把裸文字随意压在复杂图像上。

### 5.4 文字内部层级

五段正文处于同一页面层级，但每段内部按照已经冻结的语言结构排版：

- `供应物流：`、`生产物流：`、`销售物流：`、`回收物流：`使用相同的科技蓝粗体。
- 四段冒号后的作用说明使用相同的深蓝常规体。
- `四者环环相扣，`使用与四个物流名称一致的科技蓝粗体。
- 整体说明的其余文字使用与四段作用说明一致的深蓝常规体。
- 不得把整体说明制作成结论条、重点框、放大句或高亮区域。

### 5.5 必须逐字上屏的文字

- 标题：`企业四大物流闭环`
- `供应物流：源头进货，保障生产`
- `生产物流：内部流转，提质降本`
- `销售物流：终端出货，链接市场`
- `回收物流：逆向闭环，盘活资源`
- `四者环环相扣，共同影响生产成本、交付效率与资源利用率`

整体说明必须按以下位置换行，换行不改变原文：

```text
四者环环相扣，共同影响生产成本、
交付效率与资源利用率
```

### 5.6 强视觉锁定

```yaml
strong_visual_lock:
  canvas_ratio: 1920×1080完整不透明画布
  major_panel_structure: 固定标题区＋白色主体框＋中央企业全景＋五个外围定点文字锚点
  title_system: 只继承版式1固定标题框；禁止KP-22标题框进入页面
  information_region_relationship: 五段正文同级；每段内部采用领句粗体与解释常规体
  image_text_relationship: 全景负责四区识别，文字锚点负责名称与作用说明；文字不得形成侧栏或文字墙
  visual_hierarchy: 标题为唯一文字一级；企业全景为第一视觉焦点；五段正文为同级解释层
  palette_family: 固定母版浅蓝、科技蓝、深蓝与白色体系
```

### 5.7 硬禁令

1. 禁止继承KP-22标题框、标题样式、原文字位置或分散式文字锚点。
2. 禁止右侧文字墙、五行机械列表、五张卡片或底部大结论带。
3. 禁止自由散落的裸文字、文字覆盖关键业务对象或五段正文相互争抢焦点。
4. 禁止圆环、圆形节点、复杂关系线、四图拼贴及新增课程文字。
5. 禁止品牌、数据、伪文字、软件界面、播放器、字幕、教师窗口及失败图上下文泄漏。

### 5.8 风险与生产控制

- 主要风险：五个锚点被模型生成成五张卡片；通过“只用文字排版、无容器、无图标、无编号”抑制。
- 主要风险：整体说明因两行而被误判为结论；通过相同字号、相同内部字重规则和相同颜色体系保持同级。
- 主要风险：KP-22错误标题框再次泄漏；C线必须同时附加固定母版栅格预览与KP-22，并明确两张图的互斥职责。
- 主要风险：场景出现伪文字；建筑、车辆、设备、道路、包装和容器表面必须保持无字、无品牌。
- 文字准确度高风险：六处文字须逐字复核；初次生成后最多允许两次带同一参考集的局部文字修订。

```yaml
failure_risk: medium_high
feasibility_score: 7.5/10
model_recommendation: yes
model_recommendation_reason: 版式关系已明确、主视觉单一、文字内部层级可执行；风险主要集中在生成式中文与参考继承边界
remotion_asset_handoff_required: no
```

## 6. 四项Gate

| Gate | 结果 | 依据 |
|---|---|---|
| 审美气质 | pass | 固定母版控制课程身份，企业全景作为唯一主视觉，正文不做卡片墙或宣传海报 |
| 学习任务 | pass | 场景直接呈现四类物流，五段正文只承担名称、作用与共同影响 |
| 学生负荷 | pass | 四条短句单行、整体说明两行；无新增知识、图标标签或数据 |
| 媒介分工 | pass | 场景负责业务空间识别，文字负责提炼后的教学判断，二者不重复堆砌 |

## 7. 六项生产检查

| 检查项 | 结果 | 依据 |
|---|---|---|
| 页面类型稳定 | pass | A16固定母版完整带字页，外层身份不变，只重做内层图文关系 |
| 审美气质明确 | pass | 浅蓝科技课程体系＋单一企业全景＋克制文字排版 |
| 信息承载可生产 | pass | 五段文字均已提炼，位置、内部字重与换行规则明确 |
| 主视觉方向单一 | pass | 单一企业园区全景，不拆卡片、不画中央关系图 |
| 文字层级可控 | pass | 标题一级；五段正文同级；每段内部为领句粗体＋解释常规体 |
| 生成稳定性足够 | conditional_pass | 版式稳定；中文逐字准确与伪文字仍需C线Text Accuracy Gate验证 |

## 8. B线停止边界

- 本卡为QL-01新的唯一B线依据。
- T线不得继续读取旧B线QL-01中的“分散式文字锚点”描述。
- 本卡不包含GPT Image执行提示词，不进入T线或C线，不生成图像。
- 用户已确认唯一候选；本卡可交给T线单独重建QL-01合同。
