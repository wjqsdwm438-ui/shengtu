from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / 'skills-v2.7-development-snapshot-20260814' / '项目源码'

def edit(rel, replacements):
    p=SRC/rel
    text=p.read_text(encoding='utf-8-sig')
    for old,new in replacements:
        if old not in text:
            raise ValueError(f'missing replacement in {rel}: {old[:70]}')
        text=text.replace(old,new)
    p.write_text(text,encoding='utf-8',newline='\n')

edit('stage-bline-production-handoff/SKILL.md', [
 ('description: V2.7 Stage B-line executable-design handoff for course visuals. Use after A-line/A-review passes to ground one main plan in real templates and generation evidence, organize pages into dynamic production batches, calibrate a representative page, and hand a frozen executable design to the C-line execution adapter.', 'description: V2.7 Stage B-line visual-production design after A owns and internally reviews an explicit pagination plan. Realize one main visual plan, organize dynamic batches and representative calibration, and return pagination-impacting evidence to A without becoming a second pagination decision center.'),
 ('当前 `SKILL.md`、已通过的 A线页面简报及 A审结果。', '当前 `SKILL.md`、A明确分页方案及对应页面简报、当前版本内部复核记录；不要求独立A审报告或独立S阶段。'),
 ('先确认 S/A区和 A审完整', '先确认当前源引用、A分页版本及内部复核完整且未撤回'),
 ('它接收已通过 A审的教学语义，不重新切分原文，不改写事实，不重新定义教学关系。', '它接收A已明确分页并完成内部复核的方案，沿用可核验的教学与承载依据，不重新解释全部教学内容，不重新切分原文，不改写事实或教学关系。'),
 ('- 查阅当前页实际可用的模板、参考素材、相关成功/失败案例及已知生成能力；', '- 沿用A分页时已经核对的获准资产与承载依据；查阅当前页具体实现仍需要的模板、参考素材和直接相关案例，不把首次承载判断推迟至本阶段；'),
 ('- S区的页面编号、原始课程序号、原文/时间码、事实与可用素材；', '- A形成的页面编号、原始课程序号及独立源证据引用；旧S区可以只读引用，但不作为新分页批准；'),
 ('- A审通过记录；', '- 对应当前plan_id/plan_version及具体页界的A内部复核记录；旧a_review_status不能代替；'),
 ('- S区原文、时间码、事实或素材登记错误：退回 S线。', '- 原文定位、时间码、来源一致性或素材登记错误：回A输入整理，只修受影响证据，不改原稿。'),
 ('- A区教学目标、教学关系、必须呈现项或语义边界错误/缺失：退回 A线。', '- 页界、页数、正文归属、教学目标/关系、必呈项或衔接错误/缺失：附具体实现证据交A局部修正并内部复核。'),
 ('- 不覆盖 S/A 冻结项，不向上游文件追加独立 B/C产物。', '- 不覆盖源证据和A分页/教学决定，不复制上游正文或另造A摘要，不向输入原稿追加独立B/C产物。'),
])

p=SRC/'stage-bline-production-handoff/SKILL.md'
t=p.read_text(encoding='utf-8')
t=t.replace('## Inputs\n', '''## 分页引用与反馈（不是第二轮分页）

- B区的 `pagination_ref` 必须匹配A计划的 `plan_id`、`plan_version`、`page_id` 和 `owned_spans`，不得另行建立B页界。
- 必要载体、模板空间或素材风险已在A分页时进入判断；B在其范围内细化具体容器、主视觉、精确位置与尺寸、文字实现和参考映射，不重复补一套教学理由字段。
- 纯实现问题由B局部修正；涉及页界、页数、正文归属或教学关系时，`pagination_feedback` 记录问题、实际证据、受影响页及 `requested_owner: A`，由A完成修正后B再落实。
- A只重查受影响页和必要相邻衔接；B同步新版本引用，不重启S→A→B，不把未完成的设计判断交给用户。
- 数据校验规则见 `_shared/pagination-plan-contract.md`。反馈无问题时用空数组；待决反馈只影响相关下游，不据此重开独立A审或全课停止。

## Inputs
''')
p.write_text(t,encoding='utf-8',newline='\n')

edit('stage-bline-production-handoff/references/production_handoff_rules.md', [
 ('B线读取同一页面简报中已通过 A审的 S区与 A区，只向其 B区追加一份 `main_execution_plan`。', 'B线读取当前源引用、A明确分页与内部复核，只向同一页面简报B区追加一份 `main_execution_plan`。B的pagination_ref必须匹配当前A计划，不要求独立S或A审报告。'),
 ('- S输入错误退回 S；A语义错误退回 A。', '- 源输入证据、页界/页数、正文归属或教学语义错误归A；B提供证据、影响页和问题，不自行重分页。'),
 ('要求 A审通过、实现依据五项完整', '要求当前A分页内部复核完成且版本/页界匹配、实现依据五项完整'),
 ('B线通过以下问题说明安排：', 'A已在分页期间核对同屏需要、文字/标签/图注负荷与实际空间；B沿用有效依据，只就具体安排通过以下问题补充说明：'),
])
edit('stage-bline-production-handoff/templates/b_line_production_card.md', [
 ('本模板追加到已通过 A审的同一页面简报。', '本模板追加到A已明确分页并完成当前版本内部复核的同一页面简报；不要求独立A审通过。'),
 ('  a_review_status: passed', '''  a_pagination_plan_reference: # 现有A方案路径/版本；不复制其教学分析
  internal_review_reference: # 当前方案internal_review记录，不是独立审者

pagination_ref:
  plan_id:
  plan_version:
  page_id:
  owned_spans: [] # 与A计划逐项一致；每项source_id/line/start_char/end_char/start_text/end_text
pagination_feedback: [] # 无问题为空；涉及分页时提供实际证据并交A，不自行改页界'''),
])
edit('stage-bline-production-handoff/agents/openai.yaml', [
 ('基于真实证据形成唯一主方案、动态批次与代表页校准。', '承接A明确分页，落实视觉设计、批次与代表页校准。'),
 ('使用 V2.7 B线在页面简报中形成唯一可执行主方案，依据真实模板与案例动态分批，并在代表页人工确认后冻结批次。', '使用 V2.7 B线承接A明确分页及内部复核，在当前页界内落实唯一视觉主方案和生产批次；涉及分页的新承载问题附证据回A，代表页授权与确认规则不变。'),
])
edit('stage-bline-production-handoff/anti_examples/cross_stage_single_file_append_failure.md', [
 ('B线读取 S/A区并填写 B区', 'B线引用稳定源证据和A分页/教学区，仅填写B区'),
])

edit('_shared/page-brief-batch-execution-rules.md', [
 ('以一份页面简报承载一页从 S 到 C 的必要决定', '在A形成明确分页后，以一份页面简报承载该页从A到C的必要决定；源证据不绑定接入时的候选页面身份'),
 ('  s_section:                 # 原文/时间码、事实、素材、视觉辅助需要和媒体路由\n  a_section:                 # teaching_goal、teaching_relation、must_show_items、image_pedagogical_task、forbidden_semantic_drift、a_review_status', '''  # 独立源证据与整套分页保存在现有A分析产物；机器校验载荷用a_pagination_plan引用/承载
  a_section:                 # pagination_ref、教学目标/关系、必呈项、图像任务及禁止偏移；内部复核在当前A计划中
  # 旧s_section只作只读历史源引用，不要求新任务创建或冻结S区'''),
 ('  b_section:\n    implementation_evidence:', '  b_section:\n    pagination_ref:          # plan_id/plan_version/page_id/owned_spans与A相同\n    pagination_feedback: []  # 新分页问题归A；纯实现问题留B\n    implementation_evidence:'),
 ('- S/A/B 分区齐全且无互相冲突；', '- 源证据引用、当前A分页/内部复核和B区齐全且无冲突，A/B的pagination_ref与有效方案一致；旧S/A审通过不能替代新方案；'),
 ('原文、时间码、事实或素材错误退回 S线；教学目标、教学关系或必须呈现项错误退回 A线。', '原文定位、时间码、素材对应及页界/页数、正文归属、教学目标/关系或必须项错误回A；纯模板、骨架与参考实现问题回B。'),
 ('回 S/A/B/C', '回 A/B/C'),
 ('源/语义错误回 S/A', '源证据/分页/语义错误回A'),
 ('源材料回 S，跨页语义回 A', '源材料证据与跨页分页/语义回A'),
])
p=SRC/'_shared/page-brief-batch-execution-rules.md'
t=p.read_text(encoding='utf-8')
t=t.replace('## 动态批次\n', '''## 分页计划和旧合同兼容

整套分页记录放在现有A分析产物中，页面简报仅引用本页所需的源跨度、教学要求与当前版本；不另建全阶段正文总表。`pagination-plan-contract.md` 定义机器检查时的 `a_pagination_plan` 与页级 `pagination_ref`，JSON是可选检查载荷，不是用户必填台账。

新默认workflow为 `A → B → C_adapter → C_generate → assembly`，输入整理与内部复核均在A中。旧S区、旧A审passed和旧固定S/A_review工作流作为历史保留，不自动迁移成已就绪；需要A基于原文和有效范围完成当前方案及内部复核。旧确认只沿用其实际批准对象。

A变更页界时在本阶段维护plan_version、源跨度/旧新页映射和受影响下游状态；B不能另行重分。未变页面只同步必要版本引用并保留有效依据，不因此重审整课。源文件内容未经授权不改写；上下文回指不计作正文二次归属。

## 动态批次
''')
p.write_text(t,encoding='utf-8',newline='\n')

edit('stage-cline-gpt-image-execution-feedback/SKILL.md', [
 ('贯穿 S/A/B 的页面简报', '包含源引用、A明确分页及B视觉设计的页面简报'),
 ('当前页共享页面简报中的 S、A、B 区', '当前页源证据引用、A分页及内部复核引用、B区'),
 ('S/A/B 全链重读', 'A/B全链重读或恢复独立S'),
 ('- **S区**：页面 ID、课程原始顺序、原文或时间码、事实信息、可用素材；\n- **A区**：教学目标、教学关系、必须逐字呈现内容、图像任务、不得偏移的语义；', '- **源证据引用**：原文路径/版本、精确跨度、必要时间码和素材对应；旧S区仅只读引用，不要求新任务先跑S；\n- **A区与当前A计划**：A确定的页面ID/课程顺序、pagination_ref、教学目标/关系、必呈项、图像任务及内部复核记录；'),
 ('C线不得复制或改写 S/A/B 区。', 'C线不得复制或改写源证据、A分页/教学区或B区。'),
 ('1. 页面 ID、课程原始顺序、教学目标、教学关系、必须呈现项或 `main_execution_plan` 为空；', '1. 页面ID、课程原始顺序、源证据、A当前分页/内部复核、教学要求或 `main_execution_plan` 缺失，或A/B pagination_ref与当前方案版本/页界不匹配；'),
 ('退回规则：原文、时间码、事实或素材清单错误退 S；教学目标、内容关系、必须呈现项或语义边界错误退 A；', '退回规则：原文定位、时间码、素材对应、页界/页数、正文归属、教学目标/关系、必须项或衔接错误回A；'),
 ('回 S/A/B/C', '回 A/B/C'),
 ('不向 S/A/B 区回写', '不向源证据、A/B区回写'),
])
edit('stage-cline-gpt-image-execution-feedback/references/gpt_image_execution_adapter_rules.md', [
 ('- 页面 ID、课程原始顺序、教学目标、教学关系、必须呈现项和 `main_execution_plan` 完整；', '- 源引用及A当前分页/内部复核完整，A/B pagination_ref与当前plan_id/plan_version及owned_spans一致；页面ID、课程原始顺序、教学目标/关系、必呈项和main_execution_plan完整；'),
])
edit('stage-cline-gpt-image-execution-feedback/templates/c_line_feedback_card.md', [
 ('  s_section_complete: yes/no', '  source_evidence_complete: yes/no\n  current_A_pagination_and_internal_review_complete: yes/no\n  A_B_pagination_reference_matches: yes/no'),
 ('回 S/A/B', '回 A/B'),
])

edit('_shared/failure-diagnosis-rules.md', [
 ('return to S-line.', 'return to A input preparation; do not rewrite the source without authorization.'),
 ('source/fact/material problems return to S-line; teaching semantics return to A-line;', 'source-evidence/material-mapping and pagination/teaching problems return to A-line;'),
 ('回 S/A/B/C', '回 A/B/C'),
 ('A负责教学分组与关系问题，B负责不改变语义的承载问题；B提出跨页拆合必须提供新旧原文边界和实现证据，由A复核受影响单元及必要相邻衔接。', 'A统一负责源证据与页界、页数、正文归属、教学关系及衔接，B只修分页语义不变的具体实现；B提出跨页拆合必须提供新旧原文边界和实现证据，由A局部修正并内部复核。'),
 ('S局部更新定位不等于重新索取整课准入批准。', 'A内部维护源定位，不恢复S独立阶段，不重新索取整课有效准入批准。'),
])
edit('_shared/algorithm-lite-rules.md', [
 ('Input: S-line S07 segment, teaching goal, teaching relation, must-show items, visual teaching task, material/reference needs.', 'Input: A-admitted source evidence and explicit pagination analysis, teaching goal/relation, must-show items, visual teaching task, and approved material constraints; independent S is not required.'),
 ('Output: segment_id, segment_time_metadata, semantic summary, S-route, enter_A_line true/false, reason, pass/return/manual-confirm suggestion.', 'Output: source locator, segment_time_metadata and media disposition as optional input assistance within A (or explicit S-only request); not a page plan, fixed page identity or mandatory separate gate.'),
])

print('Updated B handoff, shared brief, C source references and return ownership; generation gates retained.')
