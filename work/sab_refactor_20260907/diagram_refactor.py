"""Apply the authorized S/A/B diagram topology change, preserving C semantics."""
from pathlib import Path
import xml.etree.ElementTree as ET

BASE = Path(__file__).resolve().parents[2] / 'skills-v2.7-development-snapshot-20260814' / '项目源码'
PATH = BASE / '课程视觉生产工具V2.7_项目节点与流程.drawio'
tree = ET.parse(PATH)
mxfile = tree.getroot()
mxfile.set('modified', '2026-09-07T00:00:00.000Z')
mxfile.set('agent', 'Codex; authorized S/A/B refactor')

def scope(did, width, height):
    global root, cells
    diagram = mxfile.find(f"diagram[@id='{did}']")
    model = diagram.find('mxGraphModel')
    model.set('pageWidth', str(width)); model.set('pageHeight', str(height))
    root = model.find('root')
    cells = {c.get('id'): c for c in root.findall('mxCell')}

def node(cid, value=None, box=None, parent='1', shape=None, color=None, dashed=False, font=14):
    c = cells.get(cid)
    if c is None:
        c = ET.SubElement(root, 'mxCell', id=cid, vertex='1', parent=parent)
        cells[cid] = c
        ET.SubElement(c, 'mxGeometry', {'as': 'geometry'})
    c.set('parent', parent)
    if value is not None: c.set('value', value)
    if box:
        g = c.find('mxGeometry')
        for key, number in zip(('x','y','width','height'), box): g.set(key, str(number))
    if shape or color:
        fill, stroke = color or ('#DCFCE7', '#16A34A')
        st = f'{shape or "rounded=1"};whiteSpace=wrap;html=1;fillColor={fill};strokeColor={stroke};strokeWidth=2;fontSize={font};align=center;verticalAlign=middle;'
        if shape == 'swimlane': st += 'startSize=40;swimlaneFillColor=#FFFFFF;fontStyle=1;'
        if dashed: st += 'dashed=1;'
        c.set('style', st)
    return c

def remove(*ids):
    for cid in ids:
        c = cells.pop(cid, None)
        if c is not None: root.remove(c)

def edge(cid, source, target, label='', dashed=False, color='#475569', exit=(1,.5), entry=(0,.5), points=(), labelpos=None):
    c = cells.get(cid)
    if c is None:
        c = ET.SubElement(root, 'mxCell', id=cid)
        cells[cid] = c
    c.attrib.update(edge='1', parent='1', source=source, target=target, value=label)
    c.set('style', f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;endArrow=block;endFill=1;fontSize=13;labelBackgroundColor=#FFFFFF;strokeColor={color};exitX={exit[0]};exitY={exit[1]};entryX={entry[0]};entryY={entry[1]};' + ('dashed=1;' if dashed else ''))
    for child in list(c): c.remove(child)
    g=ET.SubElement(c, 'mxGeometry', {'relative':'1','as':'geometry'})
    if points:
        arr=ET.SubElement(g, 'Array', {'as':'points'})
        for x,y in points: ET.SubElement(arr, 'mxPoint', x=str(x), y=str(y))
    if labelpos:
        # Relative edge geometry x chooses position along the path, y its normal offset.
        g.set('x', str(labelpos[0])); g.set('y', str(labelpos[1]))

scope('project-overview', 1800, 1150)
node('ov-title', box=(230,20,1300,50)); node('ov-subtitle','默认：输入 → A → B → C；虚线表示兼容输入、伴随证据或局部反馈', (280,65,1200,30))
node('ov-input','输入材料与有效批准\n原文 / 事实 / 素材\n证据独立于页界和页数',(40,175,250,120))
node('ov-a','A｜输入整理、全文教学分析与分页',(360,135,580,280),shape='swimlane')
node('ov-a-work','整理输入与源文证据\n分析全文目标、正文归属与关系\n先核验获准模板空间、真实素材\n检查必要视觉载体与实际承载\n给出明确页界、页数与教学方案\n本阶段不做精细构图',(20,65,325,190),'ov-a',shape='rounded=1')
node('ov-ar','A 内部复核\n检查证据、承载与分页\n不通过在 A 内修正\n不是独立阶段或停止点',(370,90,190,140),'ov-a',shape='rounded=1',color=('#ECFDF5','#059669'),font=13)
node('ov-b','B｜具体视觉设计与生产组织\n唯一主方案、真实资产与实现反馈\n纯实现问题由 B 解决\n动态分批；每批指定典型代表页',(1030,175,300,170))
node('ov-t',box=(1420,185,290,130)); node('ov-c',box=(1420,430,290,130))
node('ov-user-gate',box=(1060,445,270,165)); node('ov-state',box=(700,470,300,115))
node('ov-s','S｜非默认兼容输入工具\n仅处理字幕索引或既有 S 产物\n不创建提前 page_id\n不决定页界、页数或教学关系',(40,365,250,155),shape='rounded=1',color=('#EFF6FF','#60A5FA'),dashed=True,font=13)
node('ov-shared','共享最小规则\ncourse-visual-production-v2.7.md\n内容先证据；有效批准复用\n用户 Gate 只处理真实未决授权',(380,655,380,135))
node('ov-alg','Algorithm Lite｜伴随证据，不替代阶段决策\n字幕索引独立于页面身份\n文字预算 / 骨架 / 复杂度仅提供辅助证据\nALG-B01、ALG-C01 当前为人工规则清单',(815,655,465,135))
node('ov-manifest',box=(40,655,285,135)); node('ov-cross',box=(1340,655,370,135))
node('ov-artifacts',box=(40,850,1670,240))
for cid,box in {'ov-asset-skills':(20,65,235,135),'ov-asset-shared':(290,65,240,135),'ov-asset-content':(565,65,240,135),'ov-asset-scripts':(840,65,240,135),'ov-asset-tests':(1115,65,240,135),'ov-todo':(1390,55,255,155)}.items(): node(cid,box=box,parent='ov-artifacts')
node('ov-asset-skills','生产入口：A / B / C\nS 为兼容工具目录\nAlgorithm Lite 为证据辅助',parent='ov-artifacts')
node('ov-asset-scripts','Python 辅助脚本\n索引｜承载证据｜简报校验\n流程图标准库同步导出',parent='ov-artifacts')
node('ov-asset-tests','验证资产\n固定样例与自动校验\n历史日志不等于当前验证',parent='ov-artifacts')
edge('ov-e1','ov-input','ov-a','默认进入 A',color='#16A34A')
edge('ov-e2','ov-input','ov-s','仅需兼容时',True,exit=(.5,1),entry=(.5,0))
edge('ov-e3','ov-s','ov-a','证据输入；不预分页',True,color='#60A5FA',exit=(1,.5),entry=(0,.8),points=((325,442.5),(325,359)),labelpos=(-.35,-12))
edge('ov-e4','ov-a-work','ov-ar','内部复核',color='#059669')
edge('ov-e5','ov-a','ov-b','分页方案与 A 区',color='#16A34A')
edge('ov-e6','ov-b','ov-t',color='#9333EA')
edge('ov-e7','ov-t','ov-c',color='#DB2777',exit=(.5,1),entry=(.5,0))
edge('ov-e8','ov-c','ov-user-gate',color='#E11D48',exit=(0,.5),entry=(1,.5))
edge('ov-e9','ov-user-gate','ov-state',color='#EA580C',exit=(0,.5),entry=(1,.5))
edge('ov-e10','ov-shared','ov-a','伴随规则',True,exit=(.5,0),entry=(.3,1),points=((570,625),(534,625)))
edge('ov-e11','ov-alg','ov-a','辅助证据',True,exit=(.15,0),entry=(.55,1),points=((884.75,615),(660,615),(660,450),(679,450)),labelpos=(-.1,-10))
edge('ov-e12','ov-alg','ov-b','实现证据',True,exit=(.65,0),entry=(.5,1),points=((1117.25,630),(1370,630),(1370,380),(1180,380)),labelpos=(-.65,-12))
edge('ov-e13','ov-alg','ov-c','执行证据',True,exit=(1,.65),entry=(.7,1),points=((1305,742.75),(1305,630),(1623,630)))
edge('ov-e14','ov-manifest','ov-shared',dashed=True,color='#059669')
edge('ov-b-pagination','ov-b','ov-a','影响分页：附证据局部回 A；不重跑 S → A → B',True,color='#DC2626',exit=(.5,0),entry=(.75,0),points=((1180,115),(795,115)),labelpos=(-.3,-12))

scope('business-flow',2050,1910)
node('fl-title',box=(380,15,1290,50))
node('fl-legend','实线：默认生产链　虚线：兼容工具、证据或局部反馈　绿色容器：A 的内部工作；不是独立审核阶段',(390,70,1280,38))
node('fl-a-stage','A｜输入整理 → 全文教学分析 → 实际承载核验 → 明确分页方案 → 内部复核',(260,145,1600,450),shape='swimlane')
node('fl-start',box=(40,215,170,80))
node('fl-recognize','A：输入整理\n读取全文、事实、素材与批准\n保留来源行 / 时间范围\n原文证据不依赖页界或页数',(40,65,230,130),'fl-a-stage',shape='rounded=1',color=('#E0F2FE','#0284C7'))
node('fl-abound','A：全文教学分析\n统一本课目标与教学关系\n分析正文归属及必须呈现项\n不沿用 S 候选页数作前提',(315,65,235,130),'fl-a-stage',shape='rounded=1')
node('fl-layout-confirm','A：分页前约束核验\n查看获准模板的真实可用空间\n核对真实素材与必要视觉载体\n参考用途有新增歧义才问\n不静默降级 PSD；不精细构图',(595,65,260,130),'fl-a-stage',shape='rounded=1',font=13)
node('fl-agate','A：实际承载核验\n把必要正文、关系和视觉载体\n放入真实限制内检验可承载性\n字数等单项检查不能代替核验',(900,65,270,130),'fl-a-stage',shape='rounded=1')
node('fl-atype','A：明确分页方案\n统一页界、正文归属与教学关系\n给出页数、各页任务及拆合依据\n页面身份随后生成；不从字幕预建',(1215,65,315,130),'fl-a-stage',shape='rounded=1')
node('fl-areview','A 内部复核（不是独立 Gate）\n核对全文覆盖、页界、教学关系\n以及真实限制下的承载证据\n不通过仅在 A 内修正后继续',(1220,260,310,135),'fl-a-stage',shape='rounded=1',font=14)
node('fl-aoutput','共享页面简报 A 区\n明确分页方案、教学关系与约束\n记录实际承载核验依据\n批准状态与内部核验分开记录',(890,260,280,135),'fl-a-stage',shape='rounded=1',color=('#ECFDF5','#059669'))
node('fl-a-confirm','A 内部工作不代替真实授权\n复用原文证据与现有有效批准\n关键语义或参考用途歧义才问用户\n内部复核不自动变成分页执行获批',(40,260,355,135),'fl-a-stage',shape='rounded=1',color=('#F0FDF4','#86EFAC'),font=13)
node('fl-localcard','独立审者不是默认回路\n仅用户明确要求时执行\n本轮不定义自动触发条件\n不能因设计推断不足让用户补做设计',(455,260,375,135),'fl-a-stage',shape='rounded=1',color=('#F0FDF4','#86EFAC'),font=13)
node('fl-smerge','S｜非默认兼容工具\n字幕索引 / 既有 S 输入\n保留源文证据\n不创建提前 page_id\n不决定分页或教学关系',(40,395,170,175),shape='rounded=1',color=('#EFF6FF','#60A5FA'),dashed=True,font=13)
remove('fl-sroute','fl-s08','fl-s07','fl-e3','fl-e4','fl-e5','fl-e6','fl-e7','fl-e14','fl-e15','fl-e16','fl-e13b')
node('fl-nona','可保留的非生成承载方式\n教师出镜 / 现成素材 / 录屏\n字幕标注与后期包装\n纳入 A 全文分析和 B 生产组织\n不是必经的 S 路由',(40,655,340,145),shape='rounded=1',color=('#EFF6FF','#60A5FA'),font=13)
node('fl-userclarify','必要追问 Gate（仅真实未决事项）\n先读本地并复用有效批准\n提交具体方案与未决差异\n说明回答会改变哪个动作\n不让用户代做分页或视觉设计',(1640,695,285,165),font=13)
node('fl-bline','B｜具体视觉设计与生产组织\n构图、层级、素材与执行参数\n基于 A 方案提出唯一可执行设计\n用实际实现结果反馈，不转嫁给用户',(1150,700,300,145))
node('fl-bgate','B 实现核验\n纯实现问题由 B 解决\n影响分页时附证据局部回 A\nA 统一改页界 / 正文归属 / 教学关系\n不重跑 S → A → B',(1155,910,295,175),shape='rhombus',color=('#F3E8FF','#9333EA'),font=13)
for cid,box in {
 'fl-select':(1510,930,280,135),'fl-tline':(1510,1190,280,145),'fl-tgate':(1155,1180,295,170),
 'fl-predict':(815,1200,290,130),'fl-c-pregen-confirm':(475,1180,290,170),'fl-gpt-image':(475,1440,290,125),
 'fl-confirm':(820,1420,275,175),'fl-delivery':(1150,1430,290,160),'fl-diagnose':(815,1650,300,130),
 'fl-revision':(1180,1650,300,130),'fl-return':(1550,1640,270,170),
 'fl-manifest':(40,890,340,145),'fl-alg':(40,1190,340,180),'fl-todo':(40,1470,340,130)}.items(): node(cid,box=box)
node('fl-alg','Algorithm Lite｜按需调用，只提供证据\nSRT 索引不定义页面身份\n文字预算 / 骨架 / 复杂度：辅助 A、B\n不能仅凭字数跳过实际承载核验\nALG-B01 / C01 当前为人工规则清单')
node('fl-feedback-note','A / B 责任边界\n原文证据独立保存；A 统一页界、正文归属、教学关系\nB 内部解决构图、层级、素材适配等纯实现问题\n若实现证据改变分页，只带受影响页与依据局部回 A\n不重跑整链，不把具体方案留给用户补做',(440,700,650,145),shape='rounded=1',color=('#FAF5FF','#A855F7'),font=14)
edge('fl-e1','fl-start','fl-recognize',color='#0284C7')
edge('fl-e2','fl-recognize','fl-abound',color='#16A34A')
edge('fl-e2b','fl-abound','fl-layout-confirm',color='#16A34A')
edge('fl-e8','fl-layout-confirm','fl-agate',color='#16A34A')
edge('fl-e9','fl-agate','fl-atype',color='#16A34A')
edge('fl-e12','fl-atype','fl-areview',color='#16A34A',exit=(.5,1),entry=(.5,0))
edge('fl-e13','fl-areview','fl-aoutput','内部复核完成',color='#059669',exit=(0,.5),entry=(1,.5))
edge('fl-e17','fl-aoutput','fl-bline','明确方案与批准状态交接',color='#9333EA',exit=(.5,1),entry=(.5,0),points=((1290,650),(1300,650)),labelpos=(0,-14))
edge('fl-a-internal-fix','fl-areview','fl-atype','不通过：A 内局部修正',True,color='#059669',exit=(1,.5),entry=(1,.5),points=((1830,472.5),(1830,275)),labelpos=(0,-14))
edge('fl-e10','fl-areview','fl-userclarify','仅真实未决授权或关键歧义',True,color='#D97706',exit=(.75,1),entry=(.5,0),points=((1712.5,650),(1782.5,650)),labelpos=(.4,-14))
edge('fl-e11','fl-userclarify','fl-atype','必要决定已确认',True,color='#D97706',exit=(1,.5),entry=(1,.5),points=((1950,777.5),(1950,275)),labelpos=(.4,-14))
edge('fl-s-optional','fl-start','fl-smerge','仅需兼容时',True,color='#60A5FA',exit=(.5,1),entry=(.5,0))
edge('fl-s-input','fl-smerge','fl-recognize','兼容证据输入',True,color='#60A5FA',exit=(1,.5),entry=(0,.8),points=((235,482.5),(235,314)),labelpos=(0,-10))
edge('fl-e18','fl-bline','fl-bgate',color='#9333EA',exit=(.5,1),entry=(.5,0))
edge('fl-e19','fl-bgate','fl-atype','影响分页：附证据局部回 A',True,color='#DC2626',exit=(1,.2),entry=(.2,1),points=((1465,945),(1465,365),(1538,365)),labelpos=(.25,-14))
edge('fl-b-implementation','fl-bgate','fl-bline','纯实现问题：留 B',True,color='#9333EA',exit=(0,.5),entry=(0,.5),points=((1120,997.5),(1120,772.5)),labelpos=(0,-12))
edge('fl-e20','fl-bgate','fl-select','可执行',color='#9333EA')
edge('fl-e21','fl-select','fl-tline',color='#DB2777',exit=(.5,1),entry=(.5,0))
edge('fl-e22','fl-tline','fl-tgate',color='#DB2777',exit=(0,.5),entry=(1,.5))
edge('fl-e23','fl-tgate','fl-bline','否：退回 B线',True,color='#DC2626',exit=(1,.25),entry=(1,.7),points=((1485,1222.5),(1485,801.5)),labelpos=(-.4,-12))
edge('fl-e24','fl-tgate','fl-predict','是',color='#E11D48',exit=(0,.5),entry=(1,.5))
edge('fl-e25','fl-predict','fl-c-pregen-confirm',color='#E11D48',exit=(0,.5),entry=(1,.5))
edge('fl-e25b','fl-c-pregen-confirm','fl-gpt-image','当前具体生图授权有效',color='#475569',exit=(.5,1),entry=(.5,0),labelpos=(0,-14))
edge('fl-e26','fl-gpt-image','fl-confirm',color='#E11D48')
edge('fl-e27','fl-confirm','fl-delivery','是',color='#16A34A')
edge('fl-e28','fl-confirm','fl-diagnose','否 / 修改',color='#F43F5E',exit=(.5,1),entry=(.5,0))
edge('fl-e29','fl-diagnose','fl-revision',color='#F43F5E')
edge('fl-e30','fl-revision','fl-return',color='#F43F5E')
edge('fl-e31','fl-return','fl-predict','局部修复：回 C线',True,color='#E11D48',exit=(.2,1),entry=(0,.5),points=((1604,1840),(790,1840),(790,1265)),labelpos=(-.45,-12))
edge('fl-e32','fl-return','fl-bline','模板 / 骨架 / 参考等纯实现：回 B',True,color='#9333EA',exit=(1,.5),entry=(.6,0),points=((1980,1725),(1980,665),(1330,665)),labelpos=(-.2,-120))
edge('fl-e33','fl-return','fl-abound','源输入 / 分页 / 教学关系 / 授权冲突：回 A',True,color='#16A34A',exit=(1,.75),entry=(.5,0),points=((2010,1767.5),(2010,120),(692.5,120)),labelpos=(-.445,-180))
edge('fl-e34','fl-manifest','fl-recognize',dashed=True,color='#059669',exit=(0,.3),entry=(0,.3),points=((20,933.5),(20,180),(280,180),(280,249)))
edge('fl-e35','fl-alg','fl-smerge',dashed=True,color='#475569',exit=(1,.2),entry=(1,.9),points=((410,1226),(410,620),(235,620),(235,552.5)))
edge('fl-e36','fl-alg','fl-agate',dashed=True,color='#475569',exit=(1,.5),entry=(.5,0),points=((420,1280),(420,635),(1885,635),(1885,130),(1295,130)))
edge('fl-e37','fl-alg','fl-bgate',dashed=True,color='#475569',exit=(1,.75),entry=(.3,1),points=((440,1325),(440,1130),(1243.5,1130)))
edge('fl-e38','fl-alg','fl-diagnose',dashed=True,color='#475569',exit=(.5,1),entry=(0,.5),points=((210,1400),(400,1400),(400,1715)))
# Render containers before descendants, and edges before foreground labels.
for diagram in mxfile.findall('diagram'):
    r = diagram.find('mxGraphModel/root')
    allcells=list(r)
    for c in allcells: r.remove(c)
    groups=[c for c in allcells if c.get('vertex')=='1' and 'swimlane;' in c.get('style','')]
    for c in allcells:
        if c.get('vertex')!='1' and c.get('edge')!='1': r.append(c)
    for c in groups: r.append(c)
    for c in allcells:
        if c.get('vertex')=='1' and c not in groups: r.append(c)
    for c in allcells:
        if c.get('edge')=='1': r.append(c)
ET.indent(tree,space='  ')
tree.write(PATH,encoding='UTF-8',xml_declaration=True)
print('Updated',PATH)
