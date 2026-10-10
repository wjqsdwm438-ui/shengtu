# A 分页记录与只读机器校验合同

## 用途与权威边界

默认阶段为 `A → B → C_adapter → C_generate → assembly`。A 自己完成输入整理、全文教学分析、实际承载、明确页界/页数及内部复核；S 只兼容旧输入整理，独立审者只在用户明确请求时参与，不是固定阶段。本合同不另定独立审者触发条件。

**记录仍属于现有 A 分析产物。** 正常工作可用自然语言、既有表格表达以下信息；只有实际机器检查时才提供 JSON。允许直接内嵌在既有共享简报的 `a_pagination_plan`，也允许只将该对象作为临时校验输入。不要求用户手填 JSON，不新增全局 Manifest、登记表、持久化状态文件或固定九页方案。

正文证据独立于早期 `page_id`。既有九单元、既有通过记录和旧 `s_section`/`a_review_status` 只能作待检验候选或历史上下文，不能自动成为本次分页有效凭据。未改原文不重新清洗；变更输入、页界或实质分析时升版并重新内部复核，仍沿用现有产物目录。

## 最小 JSON 字段

根对象（共享简报内名为 `a_pagination_plan`）：

```text
schema: "course_visual_a_pagination/v1"
plan_id: 非空方案编号
plan_version: 正整数版本
source_evidence:
  sources: [{source_id, path, version, version_date, order}]
  approved_body_spans: [Span]
  annotation_spans: [Span]  # 无批注时明确 []
  approval: {status: "confirmed", record: 既有有效处理范围/分类授权记录}
pages:
  - page_id: A 最终页编号
    order: 最终源序（从 1 连续）
    owned_spans: [Span]
    context_refs: [Span]  # 无回指时 []
    capacity_basis:
      teaching_task: 具体教学任务
      required_text_and_labels: [必须同屏的正文、标签、图注等实际文字]
      approved_assets: [{path, approval_record, usable_space_and_limits}]
      asset_applicability_reason: 适用依据；无适用资产时明确不适用及理由
      same_screen_reason: 为什么这些内容必须/可以同屏
      cross_page_reason: 跨页取舍与必要上下文关系
      visual_carrier_feasibility: 必要视觉载体及其承载可行性依据
      unverified_limits: 尚未实测、不能证明的边界
non_a_dispositions:
  - {disposition_id, owned_spans: [Span], reason, target}
split_merge_comparisons:
  - comparison_id: 唯一比较编号
    source_spans: [Span]
    alternatives: [{candidate_id, proposed_page_spans: [[Span], ...], reason}]
    no_reasonable_alternative_reason: 没有合理替代时记录具体判断；有替代时可省
    selected_page_ids: [最终页编号]
    decision_reason: 拆分/合并/保持方案的具体比较结论
internal_review:
  plan_id: 当前方案编号
  plan_version: 当前版本
  status: "completed"
  reviewed_page_spans: [{page_id, owned_spans: [Span]}]
  checks: [{item, result: "pass", evidence_refs: [引用]}]
  unresolved_issues: []
```

- `sources.path` 为真实 UTF-8 文本文件，绝对路径或相对当前 JSON 所在目录；`version` 是可归因版本记录，`version_date` 用 `YYYY-MM-DD`，`order` 为多源原始顺序（从 1 连续）。不能为同一真实路径注册多个 source_id 重复正文。不读取网络来源。
- `approval` 只记录已有效的处理正文范围及批注分类，不意味着新 Non-A 制作路线、最终执行分页、生图、代表页、扩批或定稿已经批准。程序不能认证这条授权真实有效；实际 Gate 仍按上游授权记录和项目规则。
- `approved_body_spans` 指本次已批准处理范围内的全部正文，包含分别获准的 A 正文和 Non-A 正文，不是只录入 A 正文。`approval.record` 引用各自有效范围记录，不把范围合并记录解释为新增或扩大授权；否则漏录的 Non-A 不能被后续覆盖检查发现。
- `approved_assets` 只能引用本任务已获准的真实模板/素材，程序只核实可读存在。无适用资产时可 `[]`，但必须写明不适用理由，不能把未知或未读取资产写作承载已证实。`required_text_and_labels` 明确文字负荷；可以无文字而用 `[]`，不得用固定字数阈值、主载体标签枚举或固定图片占比代替承载分析。
- 每条比较记录精确覆盖其 `selected_page_ids` 的正文；重点记录实际争议或负荷风险，不强迫所有页各写候选清单。整套页界由内部复核覆盖。`alternatives` 中每个 `proposed_page_spans` 给出具体页面分组，页数直接从分组派生；必须无漏重、保源序地覆盖同一比较范围，允许同页数而页界不同。`alternatives:[]` 合法，但需 `no_reasonable_alternative_reason` 记录为何没有合理替代；不得编造另一页数凑数。至少保留一条具体方案判断，不规定候选数量。程序只核查安排映射和记录存在，既不以字段非空“证明”理由合理，也不要求每个局部范围都同时存在可合并和可拆分方案。
- 当前分组可以一并列入比较，但全是当前页界的同义复制不算真正替代；若没有任何不同页界，必须明确 `no_reasonable_alternative_reason`，不能冒充已比较不同方案。实际必呈文字/标签/图注与原文的术语对应及语义仍由 A 内部逐项复核，程序不凭文字清单非空认证其来源；既有 A/B 必显文字一致性检查继续保留。
- `checks.item` 恰含 `source_coverage`、`source_order`、`boundaries`、`capacity`、`split_merge`、`non_a_retention` 六项，每项一次。`evidence_refs` 用 `source:来源ID`、`page:页ID`、`comparison:比较ID`、`non_a:去向ID`，必须能在本方案解析；旧通过日志不属于有效引用。`reviewed_page_spans` 保存整套当前页界映射而非重复整篇原文。

### Span：真实定位，不以摘要代替原文

```json
{"source_id":"source-1","line":1,"start_char":1,"end_char":4,"start_text":"甲","end_text":"丁"}
```

原文件第一行为 `甲乙丙丁` 时，上例覆盖四个字符。`line`、`start_char`、`end_char` 均为**逐行、1 基、闭区间**；以 Python Unicode 字符计数，不用字节、UTF-16 单元、渲染列宽或分词数。换行符不归正文；空行无可拥有字符。跨行内容拆成逐行 Span。起止短锚点必须与所选原文实际起止逐字一致，且不得超出该 Span。

批准正文每个字符必须恰一次属于某个 A 页面 `owned_spans` 或 `non_a_dispositions.owned_spans`：禁止遗漏、重叠、越界、把批注当正文或删除 Non-A。允许一片源文分成多页、一页合并多个源片，以及多对多拆合；原始源序保留，页数由方案派生，没有九页或九单元目标。上下文 `context_refs` 只能回指前页已拥有的正文，可重复出现，但不增加正文覆盖，不拿它掩盖漏文；批注不作为正文回指。

## 与 A/B/C 简报对齐

共享简报继续使用 `course_visual_page_brief/v2.7`；只保留旧 S/A 审字段而缺少本合同，会明确返回“旧合同不就绪”。`page_briefs` 必须与 A 最终页集恰好对应，`original_course_order` 必须等于 A 的 `order`。

每页 `a_section.pagination_ref` 与 `b_section.pagination_ref` 均为：

```text
{plan_id, plan_version, page_id, owned_spans: [Span]}
```

两个引用必须逐字段与根计划当前页相同；B 不能据制作方便独立重分页。A 内部复核仅存在根计划，不另造 `a_section.internal_review_status`。

`b_section.pagination_feedback` 正常为 `[]`。有局部承载/分页问题时记录 `{feedback_id, page_ids, issue, requested_owner:"A", status:"pending"}`，只带具体问题和证据局部回 A；这时简报不就绪。A 处理后记 `status:"resolved_by_A", resolution_plan_version:当前A版本`。纯实现问题留 B，不假装成为分页反馈。`issue` 需写出实际观察证据，而非空泛“太密”。

C `adapter_preflight` 使用 `source_evidence_complete`、`A_internal_review_complete`、`a_pagination_plan_complete` 均为 `yes`，取代旧 `s_section_complete`；仍保留 A/B 完整、真实素材、主执行计划、代表页 Gate、技术参数、参考附件与骨架继承等所有原有硬检查。机器通过不自动授权 C 生图。

## 只读命令及证据限制

```powershell
python scripts/validate_pagination_plan.py tests/pagination_plan_valid.json
python scripts/validate_page_brief.py tests/page_brief_contract_valid.json
python -B -m unittest discover -s tests -p test_pagination_contract.py
python -B run_all_checks.py
```

前两条标准输出 JSON，成功退出 0、合同失败退出 2；不写输入或正式产物。集成默认只读，不刷新历史 `test_logs`；刷新证据需要显式 `--update-evidence`。测试使用合成原文而非真实课程原稿，不运行生图或联网。

**程序能验证**：文件读取、坐标与短锚点、声明范围的覆盖/重复/顺序、批注隔离、Non-A 留存、上下文归属、方案与内部复核版本/整套页界映射、A/B 对齐和局部反馈路由、承载/比较记录结构及现有 B/C 硬 Gate。

**程序不能证明**：实际教学分组合理性、真实视觉效果、审阅人确实完成思考、授权真实性、版本日期真实性、来源锚点之间的全部编辑或未升版的语义变更。`pass` 只表示机械检查通过；输出固定标记 `mechanical_validation_only:true`、`pedagogical_quality_verified:false`。不计算、保存或传递哈希、摘要指纹或任何替代指纹。必须保留这些证据边界，不能凭字符串非空、旧九单元测试或本脚本通过声称真实生产已验证。
