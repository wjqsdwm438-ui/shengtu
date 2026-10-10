"""One-time, scoped XML edits for the approved media-judgment revision."""
from pathlib import Path
import xml.etree.ElementTree as ET

ROOT = Path(r'E:\shengtu\skills-v2.7-development-snapshot-20260814\skills-v2.7-development-snapshot-20260814\项目源码')
path = ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio'
tree = ET.parse(path)
cells = {c.get('id'): c for c in tree.iter('mxCell')}
roots = {d.get('id'): d.find('mxGraphModel/root') for d in tree.findall('diagram')}

def label(cid, value):
    cells[cid].set('value', value)

def geometry(cid, **values):
    cells[cid].find('mxGeometry').attrib.update({k: str(v) for k, v in values.items()})

def route(cid, points=(), **style):
    cell = cells[cid]
    current = dict(p.split('=', 1) if '=' in p else (p, '1')
                   for p in cell.get('style', '').split(';') if p)
    current.update({k: str(v) for k, v in style.items()})
    cell.set('style', ';'.join(k+'='+v for k,v in current.items())+';')
    g = cell.find('mxGeometry')
    for old in list(g):
        g.remove(old)
    if points:
        array = ET.SubElement(g, 'Array', {'as': 'points'})
        for x, y in points:
            ET.SubElement(array, 'mxPoint', {'x': str(x), 'y': str(y)})

def node(cid, value, x, y, w, h, color='#FFF7ED', stroke='#EA580C', shape='rounded=1', diagram='business-flow'):
    if cid in cells:
        raise ValueError('refusing duplicate node '+cid)
    c = ET.SubElement(roots[diagram], 'mxCell', dict(id=cid, value=value, vertex='1', parent='1',
        style=f'{shape};whiteSpace=wrap;html=1;fillColor={color};strokeColor={stroke};strokeWidth=2;fontSize=14;align=center;verticalAlign=middle;'))
    ET.SubElement(c, 'mxGeometry', {'as': 'geometry', 'x': str(x), 'y': str(y), 'width': str(w), 'height': str(h)})
    cells[cid] = c

def edge(cid, source, target, value='', points=(), color='#16A34A', **style):
    c = ET.SubElement(roots['business-flow'], 'mxCell', dict(id=cid, source=source, target=target, value=value, edge='1', parent='1',
        style=f'edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeWidth=2;endArrow=block;endFill=1;fontSize=13;labelBackgroundColor=#FFFFFF;strokeColor={color};'))
    ET.SubElement(c, 'mxGeometry', {'relative': '1', 'as': 'geometry'})
    cells[cid] = c
    route(cid, points, **style)

# Overview: summarize decisions without creating another entry or stage.
label('ov-a-work', '整理输入与源文证据\n分析理解顺序、正文归属与教学关系\n内容驱动核验模板、素材与动态适配\nA 总分页内统筹页 / 状态 / 镜头展开\n必呈项不等于全时同屏；不做精细构图')
label('ov-ar', 'A 内部复核\n检查理解顺序与总分页\n核对静态或分步承载依据\n不是独立阶段或停止点')
label('ov-b', 'B｜内容驱动的视觉实现\n落实 A 总分页内的分步展开\n真实外壳证据 + 唯一完整主方案\n无匹配内构案例可代表页校准\n纯实现留 B；分页 / 教学问题回 A')
label('ov-t', 'C线｜执行适配器\n校验简报 / 素材 / 当前状态文字\n失败按责任回 A 或 B\n编译提示但不新增设计')
label('ov-c', 'C线｜生成与局部修改\n代表页确认后核对非代表首轮授权\n列名授权有效才扩展本批\n候选 / 样张组装不等于定稿')
geometry('ov-c', height=145)
label('ov-user-gate', '授权 / 定稿 Gate\n代表确认 ≠ 非代表生图批准\n候选 ≠ final_course_visual\n最终定稿须明确确认')
label('ov-manifest', '产物与交接说明（无统一 Manifest）\n核对具体目标、范围和改旧文件影响\n已有写入授权：告知后写\n未覆盖才询问；不自动追加上游')
node('ov-authority', '有效 Markdown 规则为执行依据，图须同步；SVG 为派生预览，冲突需修正，不以图替代规则。',
     120, 1095, 1560, 28, shape='text', diagram='project-overview')

# Business flow: content-first analysis and responsibility-preserving returns.
tree.find("diagram[@id='business-flow']/mxGraphModel").set('pageHeight', '2260')
label('fl-a-stage', 'A｜全文教学分析与理解顺序 → 内容驱动承载适配 → 总分页内统筹展开 → 内部复核')
label('fl-abound', 'A：全文教学分析\n明确理解顺序与教学关系\n分析正文归属、必呈项和展开节奏\n不沿用 S 候选页数作前提')
label('fl-agate', 'A：内容驱动承载核验\n比较静态总览、分步展开与镜头\n在真实限制内验证适配，不静态装箱\n必呈项不等于全时同屏')
label('fl-atype', 'A：统一总分页方案\n统筹执行页 / 页内状态 / 镜头展开\n明确页界、正文归属、各页任务\n前向预览不转移原旁白正文归属')
label('fl-layout-confirm', 'A：分页前约束核验\n核验获准模板、素材与可用空间\n按教学关系判断适配而非套框\n新增参考用途歧义才问\n不静默降级 PSD；不精细构图')
label('fl-areview', 'A 内部复核（不是独立 Gate）\n核对全文覆盖、理解顺序与总分页\n检查静态 / 分步承载和拆合依据\n不通过仅在 A 内修正后继续')
label('fl-bline', 'B｜内容驱动的具体视觉实现\n落实 A 总分页内的状态与镜头\n唯一完整主方案 + 真实外壳证据\n无匹配内构案例可进入代表页校准')
label('fl-bgate', 'B 实现核验\n构图 / 层级 / 动态适配等由 B 解决\n影响理解顺序、分页或教学关系\n附证据局部回 A 统一修正\n不重跑 S → A → B')
label('fl-select', 'B线批次合同\n按内容机制分批并保留原课程序号\n代表页先验证待校准的内构\n无成功案例不是一概准入阻塞')
label('fl-tline', 'C线执行适配器\n校验简报、素材与具体参数\n逐字编译当前状态必呈文字\n不得新增设计或铺满全页所有文字')
label('fl-tgate', 'C适配完整性 Gate\n尺寸、方案、当前文字、素材完整？\n空值、矛盾或缺文件立即停止\n失败按 A / B 责任退回')
node('fl-adapter-return', 'C适配失败责任分流\nA：源文 / 理解顺序 / 分页 / 教学\nB：模板 / 构图 / 素材等纯实现\n附具体证据，仅修受影响部分', 785, 920, 295, 155,
     color='#FEF2F2', stroke='#DC2626')
cells['fl-e23'].set('target', 'fl-adapter-return')
label('fl-e23', '否：附证据分流')
route('fl-e23', [(1302.5, 1145), (932.5, 1145)], exitX=.5, exitY=0, entryX=.5, entryY=1)
geometry('fl-e23', x=0, y=-12)
edge('fl-adapter-to-b', 'fl-adapter-return', 'fl-bline', 'B 纯实现问题',
     [(1100, 997.5), (1100, 875), (1290, 875)], color='#9333EA', dashed=1,
     exitX=1, exitY=.5, entryX=.467, entryY=1)
edge('fl-adapter-to-a', 'fl-adapter-return', 'fl-abound', 'A 责任问题',
     [(932.5, 895), (1105, 895), (1105, 355), (692.5, 355)], color='#16A34A', dashed=1,
     exitX=.5, exitY=0, entryX=.5, entryY=1)
geometry('fl-adapter-to-a', x=-.45, y=-12)
label('fl-gpt-image', 'C：生成代表页候选\n仅执行当前具体代表页首轮授权\n批内只携带必要上下文')
label('fl-confirm', '用户确认本批代表页？\n确认只冻结本批执行合同\n不等于非代表生图或最终定稿')
label('fl-delivery', '非代表页首轮生图授权 Gate\n逐一列名页面及各一次首轮范围\n已有有效授权不重复索批\n未覆盖才问；未获授权不得扩展')
node('fl-expand', 'C：扩展本批列名页面\n仅在当前首轮授权范围执行\n逐页校验当前状态与实际附件\n修改另按局部修订授权', 1510, 1430, 280, 160,
     color='#FFE4E6', stroke='#E11D48')
node('fl-assembly-candidate', '组装候选 / 样张\n按原课程序号检查全套呈现\nfull_page_candidate / sample\n此时不是 final_course_visual', 1510, 1680, 280, 155,
     color='#ECFDF5', stroke='#059669')
node('fl-final-gate', '最终定稿 Gate\n明确本次具体页面 / 全套版本\n用户是否确认最终定稿？\n代表页确认不能替代', 1150, 1665, 290, 185,
     shape='rhombus', color='#FFEDD5', stroke='#EA580C')
node('fl-final', '已确认最终定稿\nfinal_course_visual\n仅记录获准版本与页面范围\n不自动另启后续派生生产', 815, 1690, 290, 145,
     color='#DCFCE7', stroke='#16A34A')
edge('fl-expand-authorized', 'fl-delivery', 'fl-expand', '列名授权有效', exitX=1, exitY=.5, entryX=0, entryY=.5)
edge('fl-expand-candidate', 'fl-expand', 'fl-assembly-candidate', '完成当前授权范围', exitX=.5, exitY=1, entryX=.5, entryY=0)
edge('fl-candidate-final-gate', 'fl-assembly-candidate', 'fl-final-gate', '', exitX=0, exitY=.5, entryX=1, entryY=.5)
edge('fl-final-confirmed', 'fl-final-gate', 'fl-final', '明确确认', exitX=0, exitY=.5, entryX=1, entryY=.5)
geometry('fl-diagnose', y=1980)
geometry('fl-revision', y=1980)
geometry('fl-return', y=1970)
edge('fl-final-revision', 'fl-final-gate', 'fl-diagnose', '否 / 需修改：仍为候选',
     [(1295, 1910), (965, 1910)], color='#F43F5E', exitX=.5, exitY=1, entryX=.5, entryY=0)
geometry('fl-final-revision', x=0, y=-12)
route('fl-e28', [(957.5, 1620), (780, 1620), (780, 1950), (965, 1950)],
      exitX=.5, exitY=1, entryX=.5, entryY=0)
geometry('fl-e28', x=-.3, y=-12)
route('fl-e31', [(1604, 2180), (790, 2180), (790, 1265)], exitX=.2, exitY=1, entryX=0, entryY=.5)
route('fl-e32', [(1980, 2055), (1980, 665), (1330, 665)], exitX=1, exitY=.5, entryX=.6, entryY=0)
route('fl-e33', [(2010, 2097.5), (2010, 120), (692.5, 120)], exitX=1, exitY=.75, entryX=.5, entryY=0)
geometry('fl-e32', x=.65, y=-12)
geometry('fl-e33', x=.58, y=10)
route('fl-e38', [(210, 1400), (400, 1400), (400, 2045)], exitX=.5, exitY=1, entryX=0, entryY=.5)
label('fl-manifest', '产物与交接写入核对（无 Manifest）\n先告知具体产物 / 路径 / 改旧影响\n已有写入授权覆盖：告知后写\n未覆盖才问；不自动追加上游文件')
node('fl-authority', '有效 Markdown 规则为执行依据，图须同步；SVG 派生，冲突需修正。静态检查不证明教学判断或真实会话已验证。',
     180, 2200, 1690, 30, shape='text')

ET.indent(tree, space='  ')
tree.write(path, encoding='UTF-8', xml_declaration=True)
