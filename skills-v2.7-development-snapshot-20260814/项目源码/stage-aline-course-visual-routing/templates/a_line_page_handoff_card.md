# A Analysis And Shared Page Handoff

默认 A 自己完成输入整理、全文教学分析、必要承载核验、明确分页与全套内部复核。本模板是模型在现有 A 分析产物中记录工作的方式，不要求用户填表，也不强制新增文件。自然语言可表达同等信息；仅需机器检查时才按 `_shared/pagination-plan-contract.md` 提供完整 JSON。

源引用/Non-A 与分页方案分开：源接入时不创建 page_id，不从旧 S 区的 confirmed、旧单元数或旧页数推导新页界。旧方案可作为待检验比较基线，有证据可保留；必须实际比较合理拆合，不为证明重审而硬改页数。

## 现有 A 分析产物应记录什么

1. **输入与有效范围**：源文件路径、版本/日期、顺序、精确定位及原文角色；原旁白、屏显文字、批注、素材需求与真实媒体分开。保留实际时间证据或不适用理由；素材 available/missing/unverified 按真实可读性与对应内容核对。处理范围、Non-A/A 正文及其批准分别引用，不重复索批。
2. **全文教学分析**：全文学习目标、主次、关系及前后依赖，哪些对象必须并现、哪些可页内先后显现或跨页，禁止丢失/反转/混同的条件；区分页、状态和镜头，不先套旧单元逐页补理由，总分预览/回显按教学作用判断。
3. **必要承载核验**：各实际状态具体必显文字、术语、标签和图注负荷，已获准模板的实际可用空间，真实素材不可裁切/重画等限制、必要图解及观察顺序，不只测字号。写出依据与未核验边界；不提前设计精细构图、尺寸或风格，不用固定字数/页速/比例代替证据，无匹配案例不要求用户补模板。
4. **实际拆合比较**：合理拆分、邻接合并、保持原界或跨页承接方案的源范围、利弊和取舍，不机械凑固定数量的候选，也不仅填写“已比较”。A 自行作出明确分页，不让用户补做设计判断。
5. **收敛方案与映射**：方案标识/版本、每页正文归属、精确起止、源序、上下文回指、Non-A 去向及旧新对应。此时才建立新 page_id；页界保留的简报与有效结论继续沿用，变更页按映射迁移，历史源证据不覆写。
6. **内部复核**：按下表核对整套当前版本，有问题由 A 局部修正。正常流程不读取独立 A 审报告，不要求 a_review_status 通过或新增 Gate。

## 默认内部复核记录（必须实际执行）

| 统一检查项 | 必须核对的内容 | 记录 |
|---|---|---|
| source_coverage | 原文正文恰一次归属 A 页或 Non-A，无遗漏、越界、无说明重复；批注/需求不混入正文；必显文句、数字、术语保持原意与应有逐字内容 | 具体源定位/页引用、结论、待修项 |
| source_order | 原始顺序可追溯，主次与前后依赖完整；上下文回指不伪装新增正文覆盖 | 源序与关系证据 |
| boundaries | 全文目标与整套页界相符；逐一查相邻页可否合理合并/拆分或调整正文归属；同屏必要性、跨页衔接及禁止偏移已明确，非只审单页卡片 | 涉及页界、关系依据及保留/改动理由 |
| capacity | 各状态必显文字/标签/图注、真实素材、必要图解与观察顺序在获准条件下有实际承载依据；必呈不是全时同屏；图像教学任务服务目标，切换/运动等未实测边界诚实记录 | 模板/素材路径与批准依据、具体限制 |
| split_merge | 实际比较的合理替代与最终页集相符，未采纳理由明确；旧界经检验而非默认继承，未为改页数硬凑结果 | 比较记录及受影响页 |
| non_a_retention | Non-A 逐字范围、路由与有效决定完整保留，未吞并到 A 或默认扩大制作/生图授权 | 去向、源范围与批准记录 |

“检查通过”须有证据，不能靠字段非空。完整复核覆盖当前方案所有页面；记录当前版本和整套页界映射。计划改动后重核受影响页界及相邻依赖，最终复核记录对应更新后的整套方案。只在用户专属决定、有效决定冲突或缺失授权时提问。

## 机器结构定位（统一合同，不另造 schema）

最外层 `a_pagination_plan` 与 `schema`、既有 `workflow`、`page_briefs` 同级；不是单页 page_brief 内字段。以下占位需以实际证据填写，不是可直接标记通过的默认数据。根计划字段与 Span 定义以共享合同为准。

```yaml
schema: course_visual_page_brief/v2.7
# 已有 workflow 及其他项目字段按原合同保留，不在此重定义。
a_pagination_plan:
  schema: course_visual_a_pagination/v1
  plan_id:
  plan_version: 1  # 实际版本；输入/页界/实质分析变更时升版
  source_evidence:
    sources:
      - source_id:
        path:
        version:
        version_date:
        order:
    approved_body_spans: []  # 已授权处理正文；含待路由 A/Non-A，不仅是 A 页
    annotation_spans: []     # 明确批注范围；无批注才为空
    approval:
      status: confirmed     # 仅可引用真实有效的处理范围/分类批准
      record:
  pages:
    - page_id:
      order:
      owned_spans: []
      context_refs: []  # 本次A页已归属原文的视觉回显/预览，不新增旁白或正文覆盖
      capacity_basis:
        teaching_task:
        required_text_and_labels: []  # 本页各状态必呈文字，不要求全时同屏
        approved_assets: []  # 项目为 {path, approval_record, usable_space_and_limits}
        asset_applicability_reason:
        same_screen_reason:  # 必须并现/可以先后显现的理由及状态分配
        cross_page_reason:  # 跨页预览/回显方向、作用与非新增旁白说明
        visual_carrier_feasibility:  # 含必要图解、观察顺序，不只测字号
        unverified_limits:  # 如实记录静态/切换/运动等未实测条件
  non_a_dispositions: []  # 项目为 {disposition_id, owned_spans, reason, target}
  split_merge_comparisons:
    - comparison_id:
      source_spans: []
      alternatives: []  # 项目为 {candidate_id, proposed_page_spans: [[Span], ...], reason}
      no_reasonable_alternative_reason:  # alternatives 为空时必须写具体依据；有合理替代时可省略
      selected_page_ids: []
      decision_reason:
  internal_review:
    plan_id:
    plan_version:
    status: completed  # 只有本版全套实际复核闭合后才能写 completed
    reviewed_page_spans: []  # 整套 {page_id, owned_spans}，与本版 pages 精确相同
    checks:
      - item: source_coverage
        result: pass  # 仅在对应实际核对通过后填 pass；有问题不得交付为完成态
        evidence_refs: []
      - item: source_order
        result: pass
        evidence_refs: []
      - item: boundaries
        result: pass
        evidence_refs: []
      - item: capacity
        result: pass
        evidence_refs: []
      - item: split_merge
        result: pass
        evidence_refs: []
      - item: non_a_retention
        result: pass
        evidence_refs: []
    unresolved_issues: []  # 尚有未闭合问题时不能填空
page_briefs:
  - page_brief:
      page_id:
      original_course_order:  # 等于本版计划 pages.order
      # 历史 s_section 存在则保留只读源引用；新页不伪造独立 S 阶段。
      a_section:
        status: draft / confirmed / needs_user_gate
        pagination_ref:
          plan_id:
          plan_version:
          page_id:
          owned_spans: []
        teaching_goal:
          learner_outcome:
          source_evidence:
        teaching_relation:
          relation_kind: 比较 / 步骤 / 因果 / 组成 / 映射 / 场景解释 / 其他
          participants:
          direction_or_logic:
          source_evidence:
        must_show_items:
          exact_text:
          exact_numbers:
          exact_terms:
          required_real_materials:
        image_pedagogical_task:
          learner_should_see_or_compare:
          task_reason:
        forbidden_semantic_drift: []
        intentionally_not_decided_by_A:
          - precise_layout_or_composition
          - precise_size_or_position
          - image_or_text_ratio
          - template_selection_or_variant
          - visual_style_options
          - cross_page_skeleton_inheritance
          - production_batch
          - generation_prompt
        unresolved_semantic_gate:
          needed: yes / no
          question:
        evidence_notes:
      b_section:
        status: pending
      c_section:
        status: pending
```

### 精确字段约束

- 每个 Span 为 `{source_id,line,start_char,end_char,start_text,end_text}`，逐行、Unicode 字符、1 基闭区间；跨行拆成逐行 Span，起止锚点必须逐字对应真实原文，不是摘要或指纹。源文件与精确坐标不清时先局部核对，不编造。
- 批准正文每个字符恰一次属于 pages.owned_spans 或 non_a_dispositions.owned_spans；context_refs 可引用本次A页拥有的正文，用于前页回显或后页视觉预览，须在 cross_page_reason 或可读正文说明方向、作用及非新增旁白，不增加覆盖、不改原旁白顺序、不掩盖漏文，不引用Non-A/批注/批准外文字。机器字段、校验方法和已知限制按共享合同，不声称程序证明教学或视觉质量。
- checks 必为上述六项；evidence_refs 使用真实的 source:来源ID、page:页ID、comparison:比较ID、non_a:去向ID。复核不另造 a_section.internal_review_status，也不要求旧 a_review_status。
- 比较记录只针对实际拆合判断，不要求每页各凑一套候选；整套页集由内部复核覆盖。每个替代方案给出真实 proposed_page_spans 分组，页数由分组派生，可以比较同页数但不同页界的方案；确无合理替代时写具体依据，不编造为了改变页数的候选。记录的源范围与 selected_page_ids 的正文对应，不靠摘要标签证明覆盖。
- source_evidence.approval 仅是现有处理范围与批注分类依据，不代表新 Non-A 制作路线或最终执行分页、生图等授权已批准。分页的具体执行批准仍按既有决定记录和交互 Gate 核对；字段非空不能替代授权。
- 分页引用必须与当前根计划逐字段一致；B 只在该分页内落实视觉设计。B 页界/页数/正文归属/教学关系问题通过 b_section.pagination_feedback 给具体证据，requested_owner 为 A，由 A 局部修正；B/C 不自行拆合。
- teaching_relation 的类型是开放提示，可复合、可跨页；分清参与者、方向、条件和必要依赖，不能为套版强行二选一。must_show_items 保留本页各状态应逐字文字、数据、术语及真实素材，不改旁白；必呈不等于全时同屏。用既有 same_screen_reason/cross_page_reason 写先后/并现，B在 reading_order 落实，不新增字段类型/版本或自动把旧静态记录重释为已验证动态设计。
- 专业约束记录具体对象/标注/图例、条件和依赖页；既有节点以路径、版本/日期、定位及有效范围核对后沿用，不把源忠实性核对升级为脚本外部真实性/实时审校。

## 交接不变式

A 交付完整收敛分页和本版内部复核；不能把承载与页界判断留到 B。历史 S 源证据不覆写，有依据的旧决定继续有效。B/C 维护所属分区，受影响教学/源输入/分页问题归 A 局部修正，不整链重启。用户随时可介入；具体分页、参考用途、设计变更、生图、代表页、定稿 Gate 保持原授权规则。

独立复核不是本模板的后置必经阶段；仅用户明确请求时才用同目录 a_review_report.md。
