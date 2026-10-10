"""A-line capacity evidence; read approved PNGs, measure text, do not edit images."""
from pathlib import Path
import json, re, sys, shutil
from PIL import Image, ImageFont

ROOT=Path(r'E:\shengtu\skills-v2.7-development-snapshot-20260814')
DIR=ROOT/'A线'
TARGET=DIR/'8.1_分页方案.md'
ASSETS=Path(r'E:\shengtu\智能网联\版式x\tu1')
SOURCE=Path(r'E:\shengtu\智能网联\8.1正文.md')
BACKUP=DIR/'8.1_分页方案_历史R2_承载结论撤回.md'
REPORT=DIR/'8.1_A线版式承载核验_R3.md'
CHECK=DIR/'8.1_A线R3_校验结果.json'
source_before=SOURCE.read_bytes()
if not BACKUP.exists():
    old=TARGET.read_text(encoding='utf-8')
else:
    old=BACKUP.read_text(encoding='utf-8').split('<!-- R2 ORIGINAL -->\n',1)[-1]
plan=json.loads(old.split('```json\n',1)[1].split('\n```',1)[0])['a_pagination_plan']
assert plan['plan_version']==2
pages=plan['pages']
approved='用户本轮明确指定“E:\\shengtu\\智能网联\\版式x，这是版式”，授权用于本课A分页的版式约束与承载核验；不授权复制旧课事实内容或启动生图。'
observations={
'空白.png':'上方为题头与细线，其下连续留白；约x80—1200、y130—660为正文可用包络。旧题头“车道保持辅助（LKA）”不是本课文字，不能照搬。',
'幻灯片1.PNG':'封面图，包含旧课题目、学校与任务号；不是正文承载样本，本课不追加封面页或继承身份信息。',
'幻灯片3.PNG':'照片约x57—592、y169—608；解释区约x616—1212、y170—608，容纳两项分类及解释。支持一个实体对象与比较文字共存，不证明所有两类都应拆卡。',
'幻灯片4.PNG':'左侧四个配图概念约x58—613、y130—660；右侧论述约x700—1220、y130—657，含结论、补充解释和两组区分。证明分类与论述可以共同占有正文，不把四宫格或L1/L2内容迁入本课。',
'幻灯片5.PNG':'左侧多模态解释、品牌项与补充标签，右侧中控实图，底部有总结条；展示多个命名项与一个实物的层次关系。品牌标志、车内功能不属于8.1必用素材。',
'幻灯片6.PNG':'左侧约x78—657、y189—625为说明与强调区域；右侧约x694—1203、y164—627为道路主图。主图中的车辆与探测标线在约478×423的内图范围可辨；不能拿此图证明V2X通信或复制LKA机理。',
'幻灯片7.PNG':'左侧约x83—613、y165—659容纳分类标题、四类短名和四条说明；右侧约x643—1200、y165—658为说明与实图。证明多个完整信息组在约半幅宽、近全正文高的区域可读，并非必须保留四条容器。',
'幻灯片8.PNG':'左侧四项阶段及解释约x75—662、y182—509，下面另有强调句；右侧约x694—1203、y174—636有车辆/道路主图。支持因果或步骤关系与一个空间对象同时呈现，不将四步AEB过程挪用为本课机制。',
'幻灯片9.PNG':'左侧约x80—561、y195—541为实景；右侧约x583—1228、y192—545为三组解释，底部另有总结。证明多项文字对应空间对象的可读性，不使用图中真实座舱显示作为本课事实证据。',
'幻灯片10.PNG':'主图约x85—624、y206—490；三个属性关系约x658—1181、y227—469；底部宽条约y532—614。属性标签与对应内容直接关联，不能把场景中的65 mph当本课数据。',
'幻灯片13.PNG':'主图约x83—725、y190—657；右侧约x763—1208、y190—657包含完整长标题及多项短名。证明约440像素宽的命名区与较大主图可共存；不强制六块结构或泊车动作。'
}
inventory=[]
for name,note in observations.items():
    path=ASSETS/name
    with Image.open(path) as im:
        im.load(); assert im.size==(1280,720)
        inventory.append(dict(path=str(path),width=im.width,height=im.height,mode=im.mode,observation=note))

font=ImageFont.truetype(r'C:\Windows\Fonts\msyh.ttc',24)
def wrap(t,width=440):
    result=['']
    for ch in t:
        if font.getlength(result[-1]+ch)>width:
            cut=result[-1].rfind('、')
            if cut>=0:
                tail=result[-1][cut+1:]+ch
                result[-1]=result[-1][:cut+1]
                result.append(tail)
            else: result.append(ch)
        else: result[-1]+=ch
    return result

mechanics=[]
for page in pages:
    groups=[wrap(t) for t in page['capacity_basis']['required_text_and_labels']]
    count=sum(map(len,groups)); height=count*32+(len(groups)-1)*8
    assert height<=480
    mechanics.append(dict(page_id=page['page_id'],text_group_count=len(groups),line_count=count,measured_text_block_height=height,remaining_height=480-height,wrapped_groups=groups))

assert mechanics[2]['measured_text_block_height']+mechanics[3]['measured_text_block_height']+8==656
assert mechanics[4]['measured_text_block_height']+mechanics[5]['measured_text_block_height']+8==752
assert mechanics[6]['measured_text_block_height']+mechanics[7]['measured_text_block_height']+8==472

# 图像/关系核验是对现有样张逐张目视后的独立判断，不能从上面的文字高度自动推导。
relations=[
('CAP01',[6,8], '一个遮挡对象、两种信息来源及“补充”方向；没有为天气、弯道、路口各展开一个场景。',
 '样张6与8在独立道路图中能够辨认车辆及探测/风险作用范围，旁侧仍保有解释空间。本页所需的是遮挡边界、被遮挡对象、外部信息路径，比复现三套场景少一层事件负荷；232像素文字压力块之外仍有248像素纵向余量，主场景空间不被文字侵占。',
 '保留P01独立。与P02合并会在场景解释外新增两种分类轴；定义与补充机制不拆开。'),
('CAP02',[4,10], '三领域为并列集合；三级为有序集合；只在“信息交互”上说明连接车内外的作用，不画三对三连线。',
 '样张4已容纳分类对象与论述，样张10显示属性关系可独立命名。这里六个概念名称均为短标签，不需要六张场景图；全部10项必显文本压力高度392，余88，完整层级最长“网联协同决策与控制”在24像素测试中无需换行。两个集合的类型不同可以用明确文字“领域”“网联化程度”辨认；增加两条辅助短提示仍不耗尽余量，不靠补三级机制解释占页。',
 '保留P02合页。拆成两页会使仅有名称与序关系的三级成为孤立讲解；合入P01则需同时解释遮挡因果和分类依据，故采用目前边界。'),
('CAP03',[7,13], '同一本车与五类外部对象之间的五条归属关系；每条连接绑定一组交换信息，没有五套场景或网络中转层。',
 '样张7的分类加信息组和样张13的约440像素命名区说明：多个对象名与一处主要视觉可以共存。全清单实测12行、456像素；V2I与V2N清单各分成两行，按列举分隔符换行保持术语完整，其余条目不换行，完整词组跨行但不删词。余量24像素，故本页不再添加开头定义、用途说明或装饰性长标题。图像只需本车及五个来源的关联，标签使用已有V2缩写，不对15项交换内容分别造小图；五条向共同车辆的关系没有原文要求的支路间互连，避免线网交叉负荷。相比样张4的四幅独立场景，本页不是五幅场景缩小拼图。',
 '保留P03五类同页，但明确它是五类连接/信息归属解释，不追加应用场景。逐类或两两拆分会失去五类全貌并造成V2I/V2R跨页查对；把P04并进来需另加信息融合的空间变化和五项文字，按相同440像素压力条件总高度656，超过480，故综合作用仍独立。'),
('CAP04',[6,10], '同一道路空间中，本车已有信息与外部信息共同补充认识，并指向应用可能性。',
 '样张6/10主图能区分车辆、空间范围与关联信息。本页只展开路口语境，弯道保留用途名，不再画第二场景；五项文字192像素，余288，可容纳必要的来源标认，而无需挤掉主图。引用P03的五类知识，不复制其完整交换清单。',
 '保留P04。P01是定义中单一信息补充的解释，本页的学习增量是多方关联和用途；与P05路线对照不存在需要同屏记忆的相同对象。'),
('CAP05',[3,4], '两条路线各自连接其基础与特点；比较是定性的，不增加平行量化指标。',
 '样张3同时区分两类并放下长解释，样张4在论述中继续区别两种系统。本页使用完整专名及短特点，10项文本高度392，余88；IEEE 802.11p和LTE-V（即 C-V2X）均未拆坏，最长优势短语仍能在440像素压力宽中呈现。两条路线不是两个完整道路场景，可以在已查看的正文包络内维持各自信息归属，不必给缺项补齐对称数据。',
 '保留P05两路线同屏。若与自主论证合并，文字压力高度752并新增理由—行动关系；只拆两条路线又提高记忆比较成本。'),
('CAP06',[4,7], '外部接轨立场与自主掌握同时成立；三个核心技术对象共同支撑标准建设、自主研发和技术主动权的论证。',
 '样张4右侧在约520×527范围呈现结论、补充句及两项区分，样张7也支持分类—说明的有主次表达。P06完整九项必显文字压力高度352，余128；国际接轨两项文字没有删去。三个技术对象只作为理由的完整并列列举，不各自首次讲机制；论证仅需理由、标准要求、行动目标三层关系，接轨是共同立场，不增加第二套时间流程。因此不需要另页重复三个对象。',
 '保留P06合页。按旧版把理由与行动拆开，后页必须回显三个技术对象才能解释依据；真实样张空间和完整文字实测不支持必须拆开的判断。'),
('CAP07',[8,9], '数据集合可遭遇三类威胁，进而影响车辆与交通体系；不建立数据种类与威胁种类的一一配对。',
 '样张8支持多项作用关系加空间对象，样张9支持三组解释与一个场景。本页五项文字压力高度192，余288；图像只表达数据被取得、联系受扰、内容被改变这三类概念异常，不复现三个攻击现场。影响范围以关系标认表达，不另画灾难案例，因此保留了看清风险关系的空间。',
 '保留P07。与P08合并时文字压力总高度472，仅余8像素；虽未超出480，但还要增加保护覆盖关系，容易误读为三威胁对应三维度。'),
('CAP08',[7,10], '三个数据维度共同受起点内嵌的保护要求约束；5G连接性能是支撑而非安全充分条件。',
 '样张7展示多个类别与共同解释，样张10展示三个属性及总结。本页七项文字压力高度272，余208；三个保护维度可以在同一数据概念下标认，无需重复P07的三威胁。5G只作为带“重要支撑”限定的条件，不另扩网络拓扑，故内容与关系都能在已查看的正文范围中成立。',
 '保留P08三维度与前置原则同屏，不再为5G单开一页；结尾沿用Non-A。')
]

report=['''# 8.1｜A线版式与实际承载核验 R3

本报告是本轮A内部承载证据，不是B设计方案、课程成图或独立A审通过报告。对应方案标识 `A81-20260907-R2` 的 **v3**（修订简称R3）；页界经本次重审保持，因此沿用A81R2-P01—P08的页面身份，不以名称中的R2误判为旧结论。

## 1. 授权、读取范围和资产角色

用户本轮明确指定 `E:\\shengtu\\智能网联\\版式x` 为版式。已逐张打开查看其11张PNG，并解码核对均为1280×720。仅借用实际正文空间与信息承载条件，不迁移旧课车辆技术、学校身份、车标、性能数字或素材事实。PNG是扁平参考，不是PPT/PSD图层；没有宣称取得可编辑母版，也未静默转换或降级PSD。

原稿保持48行；主体四段、引入和结尾的原文与R2相同。全课目标仍为高职认知层面的含义、对象、路线、自主与安全，不新增机制教学。

## 2. 逐张查看记录

下列坐标是1280×720原图中的**目视近似测量**，用于描述已存在空间，不是给B的精确布局、比例、容器或位置指令。空白底板也不是要求B只能选择它，A不选具体母版变体。

|文件|观察与适用边界|
|---|---|
''']
for x in inventory:
    report.append(f"|[{Path(x['path']).name}]({x['path'].replace(chr(92),'/')})|{x['observation']}|\n")
report.append('''
## 3. 真实空间中的文字压力核验

**条件来源：**空白底板在题头下给出约1120×530正文包络；样张7、13展示近半幅宽的命名/解释区，样张6、8另保有约500×460的空间主图。取440像素文本净宽、480像素纵向空间作为一次保守压力检查，与底板正文包络核对不会侵入题头或越出边缘；不是从1280×720直接推导图文比例，也不把这块区域固定给B。

**测量方法：**用本机 `C:\\Windows\\Fonts\\msyh.ttc` 的24像素字体读取实际字形宽度，逐字测宽并优先在列举分隔符换行，行步长32、条目间隔8，每个必须项独立起行。该字号是核验取值，处于所见样张正文的相近阅读尺度；PNG不能证明原作者的字体/字号，所以不宣称提取了原始字号。未用缩写、漏词、固定字符上限或缩小到脚注字号来通过测试；条目逐字来自本页源文。长词组跨行仍按同一完整条目处理，不拆归属。

这只证明文字在指定测试条件下的占用，**不单独证明教学或图像承载**。下一节逐页另外核对关系参与者、图像复杂度、样张实际空间和替代页界，两个证据合用。本测试不要求生成课程页，不冻结B的字号、布局、配色或模板选择。

|页|必显组数|实测行数|文本高度/480|剩余纵向空间|文字结果|
|---|---:|---:|---:|---:|---|
''')
for m in mechanics: report.append(f"|{m['page_id']}|{m['text_group_count']}|{m['line_count']}|{m['measured_text_block_height']}|{m['remaining_height']}|完整保留、无裁切需求|\n")
report.append('''
P03余量最小，不能沿用“还可以再加场景和解释”的假设；P02/P05也不能扩写三级机制或路线性能指标。这不是对全课设定统一文字上限，而是本次内容在已给版式条件下的实测结果。

## 4. 图像关系与逐页拆合复核
''')
for m,(cid,refs,rel,basis,decision) in zip(mechanics,relations):
    report.append(f"\n### {cid}｜{m['page_id']}\n\n**对照样张：**"+'、'.join(f'幻灯片{n}.PNG' for n in refs)+f"；共同核对空白.png。\n\n**必要关系载体：**{rel}\n\n**实际承载判断：**{basis}\n\n**页界结论：**{decision}\n\n**文字实测明细（不是B排版）：**\n")
    for g in m['wrapped_groups']: report.append('- '+' ⏎ '.join(g)+'\n')
report.append('''
## 5. 实际比较后的整套页界

|相邻页界|本次核对|决定|
|---|---|---|
|P01/P02|空间中的信息补充机制不能与两种分类轴同时首次展开；P02内部的完整名称负荷已实测|保留分界，P02不再拆三级|
|P02/P03|两个分类轴与五类连接是不同分类依据；合并除名称过载外还新增五组交换内容|保留分界|
|P03/P04|同条件完整文字压力合计656像素，且要增加信息融合的空间解释|保留分界；五类本身不拆|
|P04/P05|共同交通空间的补充信息与协议路线比较不是同一查对任务；合并增加路线基础/特点归属|保留分界|
|P05/P06|同条件完整文字压力合计752像素，且叠加技术比较与自主论证；P06内部352像素有128余量|保留分界，自主论证不拆|
|P06/P07|自主论证中安全架构只是三项核心对象之一；后页新增数据—威胁—影响，合并打断论证主次|保留分界，不搬走“安全架构”|
|P07/P08|同条件完整文字压力合计472像素、仅余8像素，还增加三维保护覆盖关系；“因此”是自然论证转折|保留分界|

合并压力高度按所有必显项在相同条件下独立起行重算，包含两页之间的一次条目间隔，不是简单相加后四舍五入。它是比较的辅助证据，最终取舍同时考虑同屏必要性、跨页成本和关系复杂度。主体仍为8页是本次复核结果，不是预设页数。

## 6. 结论与限制

- A需要的版式读取、实际正文空间核对、完整必显文字测量、必要视觉关系分析和拆合比较已完成。P02/P03/P06有本轮具体证据，不再沿用R2的无资产推断。
- 保留源文、Non-A、8页边界及现有页面身份；主方案升为v3，所有承载结论更新为本版。R2的承载完成结论撤回，不能再作为生产凭据。
- 未生成8张课程成图，未验证真实课堂投影、最终母版、最终字体或生成模型效果；这些不能伪装为已完成。B负责实际设计，若其新增条件改变A页界则带证据局部返A；不是让B补做本轮首次承载判断。
- 不修改原稿和11张版式PNG，不复用旧课技术图作为V2X事实证据，不启动生图，不请求用户决定分几页。
''')

plan['plan_version']=3
for p,m,(cid,refs,rel,basis,decision) in zip(pages,mechanics,relations):
    cap=p['capacity_basis']
    cap['approved_assets']=[dict(path=str(ASSETS/name),approval_record=approved,usable_space_and_limits=observations[name]) for name in ['空白.png']+[f'幻灯片{n}.PNG' for n in refs]]
    cap['asset_applicability_reason']='本轮用户明确指定版式，已解码与目视核验；用既有PNG的正文空间、标签/主图承载方式核对，不复用旧课事实。详见8.1_A线版式承载核验_R3.md。'
    cap['visual_carrier_feasibility']=f'{cid}：{rel} {basis} 页界取舍：{decision}'
    cap['unverified_limits']='本轮已核对1280×720样张实际正文包络、24像素核验字体的完整文本占用及必要关系复杂度；未生成课程成图，未认证真实课堂投影、最终母版或模型效果。测量区域和字号不是B精确设计指令；PNG无可编辑图层不等于PSD已降级。'
plan['internal_review']['plan_version']=3
plan['internal_review']['reviewed_page_spans']=[dict(page_id=p['page_id'],owned_spans=p['owned_spans']) for p in pages]
for c in plan['split_merge_comparisons']:
    extra={'CMP01':'CAP01/CAP02：已查看样张4/6/8/10；P02全称实测392/480，三级仅名称和序关系，不需要新机制场景。',
           'CMP02':'CAP03/CAP04：五类全清单12行456/480，保留五条归属，不能扩为五场景；合入综合作用后同条件656，且新增空间信息融合关系。',
           'CMP03':'CAP05/CAP06：路线与自主论证分别392/480、352/480；合页同条件752；P06保留完整接轨立场、理由与行动后仍有128余量，无需拆开重复回指。',
           'CMP04':'CAP07/CAP08：分别192/480、272/480；合页同条件472、仅余8像素，并增加另一组三维覆盖关系，保留“因此”处分界。'}[c['comparison_id']]
    c['decision_reason']+=' 本轮真实版式证据：'+extra

human=old.split('## 七、内嵌a_pagination_plan',1)[0]
human=human.replace('修订版 R2','修订版 R3').replace('`plan_version: 2`','`plan_version: 3`')
human=human.replace('A线分析和内部复核已完成，提交人工审阅；不冒充用户已批准执行，也不冒充独立A审已通过。','已依据本轮指定版式完成承载复核和A内部复核，提交人工审阅；具体分页尚未获用户执行批准，未启动B/C。')
human=human.replace('- 方案：`A81-20260907-R2`，`plan_version: 3`；交付日期：2026-09-07。','- 方案标识沿用 `A81-20260907-R2`，当前 `plan_version: 3`（修订简称R3）；交付日期：2026-09-07。源界未变，A81R2-P01—P08的身份保留，不能把ID中的R2误当成本版状态。\n- R2承载完成结论已撤回，历史全文保留在 `8.1_分页方案_历史R2_承载结论撤回.md`。本版逐页接收本轮版式证据，不再使用“无获准资产”作为承载依据。')
human=human.replace('本文件的R2与A81R2-P01—P08','本文件的v3与A81R2-P01—P08')
human=human.replace('R2不沿用旧页ID。','R2建立的页面身份在本版保留，旧12页仍不沿用。')
start=human.index('### 1.2 素材、时间和工具证据')
end=human.index('## 二、全文教学分析',start)
human=human[:start]+'''### 1.2 素材、版式、时间和工具证据

- 原稿 `E:\\shengtu\\智能网联\\8.1正文.md` 已再次全文读取，仍为48行；无嵌入媒体，源文未修改。约7分钟是元数据，不编造各页时间码。
- 本轮用户明确指定 `E:\\shengtu\\智能网联\\版式x` 为版式；已逐张查看其 `tu1` 内11张PNG，全部1280×720、可解码，状态为`available`。用途为本课分页前的正文空间、命名/解释负荷和必要视觉载体核验，不复制旧课事实或启动生图。
- 这些是扁平PNG，不是PPT/PSD源文件；未声称可编辑图层可用，不静默降级PSD。样张课名、学校、车标、LKA/AEB/ACC内容、65 mph数值不得作为本课事实继承。
- L44是图示制作需求，不是现成配图；未指定的DOCX、音视频等仍为`unverified`，不因同目录存在而使用。无必须依赖的真实V2X照片或截图。
- 已读取样张正文实际包络，逐项测量本课必显文字，并单独核对图像关系复杂度。详见 [版式承载核验R3](8.1_A线版式承载核验_R3.md) 的11张观察表、8页实测表和CAP01—CAP08；本节不以字数替代承载。
- 本机指定Python3.10与Everything路径不可用，使用已存在的Codex Python3.12与指定UTF-8读取脚本；未安装工具或修改配置。字体测量仅作A承载证据，不生成课程图，不冻结B布局。
- 未作外部实时专业审校；五类连接、LTE-V/C-V2X口径、5G支撑按原稿表达，不擅改或声称已外部证实。

### 1.3 本轮版式约束与承载结果

空白底板题头下约x80—1200、y130—660为正文包络；样张7/13显示近半幅宽的命名区可与主视觉共存，样张6/8保留约500×460的道路主图。以上为既有图片的近似观察坐标，不是分配给新页面的设计位置。

在此范围内用440净宽、480纵向空间、微软雅黑24像素、32行步长和8条目间隔做压力核验：P01—P08分别需要232、392、456、192、392、352、192、272像素。完整术语无删除；P03最长两条清单需换行，余量最小，不能再叠加应用场景。数字只证明该条件下文字占用；每页另以样张可见的关系/主图空间核对图像任务，再作页界取舍。

'''+human[end:]
human=human.replace('## 三、分页总览与实际拆合比较','## 三、分页总览与实际拆合比较（R3已按真实版式重核）')
human=human.replace('共同状态：A分析完成、','共同状态：本轮版式核验及A分析完成、')
human=human.replace('/ v2 /','/ v3 /')
for p,(cid,refs,rel,basis,decision) in zip(pages,relations):
    idx=human.index('｜'+p['page_id'],human.index('## 四、'))
    a=human.index('**实际承载依据：**',idx);b=human.index('**同屏必要性：**',a)
    human=human[:a]+f'**实际承载依据（{cid}）：**{basis}\n\n**本轮版式下的拆合决定：**{decision}\n\n'+human[b:]
    a=human.index('**证据与未核验边界：**',idx);b=human.index('\n',a)
    human=human[:a]+f'**证据与未核验边界：**本轮用户指定的空白.png及'+ '、'.join(f'幻灯片{n}.PNG' for n in refs)+f'已实际查看。{cid}给出完整文字实测与必要关系核验；未生成课程成图，不认证最终投影效果。不冻结B的具体模板、字号、布局或构图。'+human[b:]

human=human.replace('旧12页到R2八页','旧12页到当前八页').replace('|R2去向|','|当前去向|')
human=human.replace('当前唯一接收版本为R2。','当前唯一接收版本为v3（R3）；本轮R2→R3全部owned_spans、context_refs、页ID与原课程序号保持相同，仅更新真实版式证据、承载判断和复核版本。')
human=human.replace('`A81-20260907-R2 / v2`','`A81-20260907-R2 / v3`')
oldrow=next(x for x in human.splitlines() if x.startswith('|capacity|'))
human=human.replace(oldrow,'|capacity|通过（本轮A条件）|已逐张查看11张PNG；正文包络、8页完整文字测量及CAP01—CAP08关系核验见承载报告；P02/P03/P06分别392/456/352像素，结合样张实际关系空间复核。未把机械通过或“无资产”当作承载证据，不宣称课程成图或课堂投影已验证|')
human=human.replace('CAP01—CAP08关系核验见承载报告','CAP01—CAP08关系核验见承载报告')
# 总览比较中的原论述保留，但补入本轮证据，不能只修改单页。
for c in plan['split_merge_comparisons']:
    marker='#### '+c['comparison_id']
    idx=human.index(marker); end=human.find('\n#### ',idx+1)
    if end<0: end=human.index('### 3.2',idx)
    human=human[:end]+'\n**R3实证补核：**'+c['decision_reason'].split('本轮真实版式证据：',1)[1]+'\n\n'+human[end:]
human=human.replace('批注/需求不混入正文','批注/需求不混入正文')
human=human.replace('本轮A内容、明确分页、教学语义、源映射、拆合论证及内部复核均已完成','本轮A内容、真实版式约束核验、明确分页、教学语义、源映射、拆合论证及内部复核均已完成')
human=human.replace('没有用“待B确定能否装下”替代A判断。','本次有真实版式观察、全文字测量和独立关系检查，不再以“没有模板”替代核验。')
human=human.replace('[版式承载核验R3](8.1_A线版式承载核验_R3.md)',f'[版式承载核验R3]({str(REPORT).replace(chr(92),"/")})')
human+='''## 七、内嵌a_pagination_plan（当前v3）

批准字段仅指处理范围；版式用途批准来自本轮用户指令，不等于执行分页或生图获批。以下机器合同可核对坐标和结构，不能代替上文承载证据。

<details>
<summary>展开只读机器合同</summary>

```json
'''+json.dumps({'a_pagination_plan':plan},ensure_ascii=False,indent=2)+'\n```\n\n</details>\n'

# 检查所有精确正文、必显词、引用和本轮资产；比较前后源界完全相同。
sys.path.insert(0,str(ROOT/'skills-v2.7-development-snapshot-20260814/项目源码/scripts'))
from validate_pagination_plan import validate_pagination_plan
errors,derived=validate_pagination_plan(plan,TARGET)
assert not errors, [e.__dict__ for e in errors]
oldplan=json.loads(old.split('```json\n',1)[1].split('\n```',1)[0])['a_pagination_plan']
assert [(p['page_id'],p['owned_spans'],p['context_refs']) for p in pages]==[(p['page_id'],p['owned_spans'],p['context_refs']) for p in oldplan['pages']]
lines=SOURCE.read_text(encoding='utf-8-sig').splitlines()
for page in pages:
    body=''.join(lines[s['line']-1][s['start_char']-1:s['end_char']] for s in page['owned_spans'])
    assert '> '+body in human
    for t in page['capacity_basis']['required_text_and_labels']: assert t in body
assert all(x not in human for x in ['approved_assets: []','没有本任务已确认必用的模板','/ v2 /','当前唯一接收版本为R2'])
assert SOURCE.read_bytes()==source_before
if not BACKUP.exists(): BACKUP.write_text('# 历史R2｜承载完成结论已撤回\n\n以下原记录仅供追溯，不得作为当前生产或通过依据；当前版见8.1_分页方案.md的v3。\n\n<!-- R2 ORIGINAL -->\n'+old,encoding='utf-8')
REPORT.write_text(''.join(report),encoding='utf-8')
TARGET.write_text(human,encoding='utf-8')
saved=TARGET.read_text(encoding='utf-8')
savedplan=json.loads(saved.split('```json\n',1)[1].split('\n```',1)[0])['a_pagination_plan']
errors,derived=validate_pagination_plan(savedplan,TARGET);assert not errors
result=dict(plan_id=plan['plan_id'],plan_version=3,page_count=8,pagination_contract_pass=True,error_count=0,source_unchanged=SOURCE.read_bytes()==source_before,page_boundaries_unchanged=True,approved_png_count=11,capacity_probe=mechanics,inventory=inventory,mechanical_validation_only=True,pedagogical_quality_verified=False,limits='字形测量只证明给定压力条件内的文字占用；视觉关系与实际样张观察见CAP01—CAP08，不等于已生成课程成图或独立审核通过。')
CHECK.write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(dict(plan_version=3,page_count=8,errors=0,approved_pngs=11,text_heights=[x['measured_text_block_height'] for x in mechanics],written=[str(TARGET),str(REPORT),str(CHECK),str(BACKUP)]),ensure_ascii=False,indent=2))
