# 《企业内部全流程物流体系》QL-01｜B线重设计交接 BR2

```yaml
status: B线生产交接已就绪
page_scope: QL-01
revision_id: BR2
source_A_line_card: E:\shengtu\skills-v2.7-development-snapshot-20260814\企业全流程_A线页面方向预判.md
candidate_policy: reference_locked_single_candidate
user_selected_T_line_candidate: 方案A_参考锁定版·知识主导型
user_selection_confirmation: confirmed
confirmation_date: 2026-08-28
```

## 1. BR2核心纠偏

- 本页第一焦点改为五条已经提炼完成的重点知识，不再把企业全景设为第一焦点。
- 企业物流场景降为第二焦点，只负责解释和支撑五条知识。
- 五条知识必须进入白色主体框的核心视觉区，禁止放在页面边缘充当图片注释。
- 五条知识处于同一页面层级；每条内部使用“领句科技蓝粗体＋解释深蓝常规体”的层级。
- 整体说明与四类物流说明同级，不制作成结论带、重点框或放大句。
- BR1及C线v01、v02、v03均为失败依据，不得进入新的T/C线参考上下文。

## 2. 参考选择与模板身份

```yaml
reference_selection:
  folder_path: E:\shengtu\智能物流\生图输出\参考
  primary_layout_reference: E:\shengtu\智能物流\样片版式\版式1.psd
  secondary_references:
    - E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png
  primary_role: 固定外层母版、唯一标题系统
  secondary_role: 一体化企业空间、场景景深、图文穿插空间感及蓝白3D质感
  rejected_reference_content: KP-22标题框、原标题、原文字、原知识层级、食品冷链、云端卫星及生成瑕疵
  user_confirmation: confirmed
template_identity:
  template_id: WL-L1
  template_version: WL-L1-EnterpriseFlow-v2.0-QL01-BR2
```

### 非哈希参考清单

| reference_id | 真实路径 | 文件名 | 尺寸 | 模板版本 | 参考角色 | 用户确认 |
|---|---|---|---|---|---|---|
| QL01-BR2-MASTER | `E:\shengtu\智能物流\样片版式\版式1.psd` | `版式1.psd` | 1920×1080 | WL-L1-EnterpriseFlow-v2.0-QL01-BR2 | 固定外层母版、唯一标题系统 | confirmed |
| QL01-BR2-SCENE | `E:\shengtu\智能物流\生图输出\参考\KP-22_方案A_一体化物流全景_v02.png` | `KP-22_方案A_一体化物流全景_v02.png` | 1920×1080 | WL-L1-EnterpriseFlow-v2.0-QL01-BR2 | 企业场景与图文穿插辅助参考 | confirmed |

不得计算、记录或传递文件哈希、摘要或指纹。

## 3. 模板层清单与上下文隔离

```yaml
template_layer_manifest:
  fixed_master: 标题框、标题位置、浅蓝背景、白色主体框、安全边界、底部装饰带
  variable_content: 五条重点知识、连续企业物流场景、图文穿插关系
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
  explicitly_excluded_inputs:
    - 企业全流程_QL-01_B线重设计交接.md
    - 企业全流程_QL-01_T线重设计交接.md
    - 企业全流程_QL-01_方案A_参考锁定版_v01.png
    - 企业全流程_QL-01_方案A_参考锁定版_v02.png
    - 企业全流程_QL-01_方案A_参考锁定版_v03.png
```

## 4. 唯一候选｜方案A_参考锁定版·知识主导型

```yaml
production_goal: 固定课程母版内的完整带字知识主导页
page_type: A16_既有母版套新内容型
production_mode: reference_locked
output_target: full_page_with_text
preset_basis: reference-locked-full-page-with-text
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

### 4.1 教学动作

通过五条高度提炼的文字直接建立供应、生产、销售、回收四类物流及其共同影响；企业场景只负责帮助学生理解文字所对应的业务空间。

### 4.2 12栏知识主导型编辑网格

白色主体框内部采用12栏编辑网格。五条知识全部进入核心视觉区，不设置外围注释区：

```text
┌──────────── 固定母版标题 ────────────┐
│                                      │
│  供应物流        生产物流       销售物流 │
│  源头进货        内部流转       终端出货 │
│  保障生产        提质降本       链接市场 │
│                                      │
│       连续企业物流场景穿插其中         │
│                                      │
│  回收物流        四者环环相扣，共同影响 │
│  逆向闭环        生产成本、交付效率与   │
│  盘活资源        资源利用率             │
└──────────────────────────────────────┘
```

以上仅表示空间骨架；正式上屏文字必须保持冻结原句和指定换行，不得拆字或改写。

- 第一排使用三个同级知识区：供应物流、生产物流、销售物流，各占4栏。
- 第二排使用两个同级知识区：回收物流占4栏，整体说明因文字长度自然占8栏。
- 整体说明占用更宽空间只为容纳文字，不代表层级提升。
- 五个知识区不加卡片、边框、标题条、图标、编号、色块底或独立容器。
- 使用字号、字重、留白、对齐和跨栏宽度形成现代编辑排版。
- 五条知识应形成页面的第一观看焦点，不能被企业场景压缩、遮挡或分散。

### 4.3 五条知识的内部文字层级

- `供应物流：`、`生产物流：`、`销售物流：`、`回收物流：`使用完全一致的科技蓝粗体。
- 四个冒号后的作用说明使用完全一致的深蓝常规体。
- `四者环环相扣，`使用与四个物流名称一致的科技蓝粗体。
- 整体说明其余文字使用与四条作用说明一致的深蓝常规体。
- 五条知识使用相同的字号体系、领句字重、解释字重、基线、字距和行距。
- 整体说明不得放大、整句加粗、添加底色、制作结论条或成为独立重点。

### 4.4 必须逐字上屏的文字

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

### 4.5 第二焦点：连续企业物流场景

- 企业场景不是占满页面的大幅主图，而是穿插在五个知识区留白中的连续视觉层。
- 四类业务场景共享同一地面、透视、光线和企业环境，不拆成四张独立插图。
- 供应车辆与收货区对应供应物流；厂内转运与生产线对应生产物流；成品仓与出库车辆对应销售物流；返厂物资与回收区对应回收物流。
- 场景可跨越知识区之间的留白，但不得进入文字安全区、压住文字或比文字更醒目。
- 图像的饱和度、对比度、对象尺度和细节密度均低于五条知识的文字权重。
- 禁止把企业场景重新扩张为页面第一焦点。

### 4.6 参考继承边界

#### 固定母版必须继承

- 1920×1080完整画布。
- `版式1.psd`的标题框、标题位置和标题系统。
- 浅蓝科技物流背景、白色主体框、安全边界与底部蓝色装饰带。

#### KP-22允许继承

- 一体化企业空间与统一景深。
- 货物、车辆、厂房和作业区的尺度关系。
- 蓝白3D质感、统一透视和图文穿插的空间感。

#### KP-22禁止继承

- KP-22标题框、标题样式、标题位置和原标题。
- 原文字、原知识层级、原文字锚点及原排版结论。
- 食品、冷链、云端、卫星、品牌、伪文字和生成瑕疵。

### 4.7 强视觉锁定

```yaml
strong_visual_lock:
  canvas_ratio: 1920×1080完整不透明画布
  major_panel_structure: 固定标题区＋白色主体框＋12栏中央知识网格＋穿插式企业场景
  title_system: 只继承版式1固定标题框；禁止KP-22标题框进入页面
  information_region_relationship: 第一排三组、第二排两组；五条知识同级，整体说明因长度自然跨8栏
  image_text_relationship: 文字是第一焦点，企业场景是第二焦点并穿插于文字留白
  visual_hierarchy: 标题为课程标题层；五条知识为核心内容层；场景为解释支撑层
  palette_family: 固定母版浅蓝、科技蓝、深蓝与白色体系
```

### 4.8 硬禁令

1. 禁止把企业全景做成页面最大主体或第一视觉焦点。
2. 禁止把五条重点知识放到页面边缘、底部窄条或右侧文字墙。
3. 禁止五张卡片、五个底框、五个图标标签或五行机械列表。
4. 禁止突出整体说明、弱化四类物流或改变五条知识的同级关系。
5. 禁止继承KP-22标题框、原文字、原产品和原知识层级。
6. 禁止品牌、数据、伪文字、软件界面、播放器、字幕、教师窗口及新增课程知识。

### 4.9 风险与控制

- 风险：模型仍把企业全景放大。控制：明确文字占据核心12栏网格，场景只穿插留白并降低对比度与细节密度。
- 风险：五个知识区生成卡片墙。控制：禁止容器、边框、底色、图标和编号，仅以文字、留白和对齐分组。
- 风险：整体说明因跨8栏而被突出。控制：保持与其他四组完全一致的字号、字重、颜色和基线体系。
- 风险：场景碎裂为四图。控制：所有业务对象必须共享同一企业空间、地面、透视和光线。
- 风险：中文或伪文字错误。控制：六处冻结文字逐字核对，建筑、车辆、设备、道路和包装表面保持无字。

```yaml
failure_risk: medium_high
feasibility_score: 7.5/10
model_recommendation: yes
model_recommendation_reason: 五条知识的视觉优先级、12栏结构和企业场景的从属关系均已冻结；主要风险为模型对知识网格与场景权重的执行稳定性
remotion_asset_handoff_required: no
```

## 5. 四项Gate

| Gate | 结果 | 依据 |
|---|---|---|
| 审美气质 | pass | 固定课程母版＋无卡片的编辑式知识排版＋低权重连续企业场景 |
| 学习任务 | pass | 五条知识直接进入核心视觉区，学生先读知识再借助场景理解 |
| 学生负荷 | pass | 文案均已提炼；三加二网格分散阅读压力，无新增解释、数据或标签 |
| 媒介分工 | pass | 文字承担教学判断，场景承担业务语境和对象识别，不以图片替代知识 |

## 6. 六项生产检查

| 检查项 | 结果 | 依据 |
|---|---|---|
| 页面类型稳定 | pass | A16固定母版完整带字页，外层身份不变，内层改为知识主导关系 |
| 审美气质明确 | pass | 12栏编辑排版、克制留白、无卡片容器、连续蓝白企业场景 |
| 信息承载可生产 | pass | 第一排三组、第二排两组，文字及换行均已明确 |
| 主视觉方向单一 | pass | 五条重点知识共同构成唯一第一焦点 |
| 文字层级可控 | pass | 五条同级；每条内部为领句科技蓝粗体＋解释深蓝常规体 |
| 生成稳定性足够 | conditional_pass | 结构与参考职责明确；场景权重、中文准确及伪文字仍需C线验证 |

## 7. B线停止边界

- 本文件是QL-01新的唯一B线依据，优先级高于BR1及原QL-01 B线描述。
- T线只能读取本BR2文件重建QL-01合同。
- 本文件不包含GPT Image执行提示词，不进入T/C线，不生成图像。
- 用户已确认唯一候选；本卡可交给T线单独生成BR2执行合同。
