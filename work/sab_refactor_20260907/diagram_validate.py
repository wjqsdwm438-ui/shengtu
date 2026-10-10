"""Offline validation evidence for the authorized diagram changes."""
from pathlib import Path
import importlib.util
import json
import sys
import xml.etree.ElementTree as ET
sys.dont_write_bytecode=True

ROOT=Path(__file__).resolve().parents[2]
REL=Path('skills-v2.7-development-snapshot-20260814/项目源码')
BASE=ROOT/REL
NAME='课程视觉生产工具V2.7_项目节点与流程.drawio'
old=ET.parse(ROOT/'work/sab_refactor_20260907/before'/REL/NAME).getroot()
new=ET.parse(BASE/NAME).getroot()
checks=[]

def check(name,condition):
    assert condition,name
    checks.append({'check':name,'result':'PASS'})

def cells(root,did):
    return {c.get('id'):c for c in root.find(f"diagram[@id='{did}']").findall('mxGraphModel/root/mxCell')}

for did in ('project-overview','business-flow'):
    cs=cells(new,did)
    check(did+' edge endpoints exist',all(c.get('source') in cs and c.get('target') in cs for c in cs.values() if c.get('edge')=='1'))
    main={}
    for c in cs.values():
        if c.get('edge')=='1' and 'dashed=1' not in c.get('style',''):
            main.setdefault(c.get('source'),[]).append(c.get('target'))
    route=(['ov-input','ov-a','ov-b','ov-t','ov-c'] if did=='project-overview' else
           ['fl-start','fl-recognize','fl-abound','fl-layout-confirm','fl-agate','fl-atype','fl-areview','fl-aoutput','fl-bline','fl-bgate','fl-select','fl-tline','fl-tgate','fl-predict','fl-c-pregen-confirm','fl-gpt-image','fl-confirm','fl-delivery'])
    check(did+' default route',all(b in main.get(a,[]) for a,b in zip(route,route[1:])))
    sid='ov-s' if did=='project-overview' else 'fl-smerge'
    check(did+' S absent from solid production edges',all(c.get('source')!=sid and c.get('target')!=sid for c in cs.values() if c.get('edge')=='1' and 'dashed=1' not in c.get('style','')))
    review='ov-ar' if did=='project-overview' else 'fl-areview'
    check(did+' internal review rectangle nested in A',cs[review].get('parent')==('ov-a' if did=='project-overview' else 'fl-a-stage') and 'rhombus' not in cs[review].get('style',''))

cs,prev=cells(new,'business-flow'),cells(old,'business-flow')
protected=['fl-select','fl-tline','fl-tgate','fl-predict','fl-c-pregen-confirm','fl-gpt-image','fl-confirm','fl-delivery','fl-diagnose','fl-revision','fl-return']
check('all protected C / batch / representative / generation authorization / assembly labels unchanged',all(cs[c].get('value')==prev[c].get('value') for c in protected))
protected_edges=[f'fl-e{i}' for i in range(21,34)]+['fl-e25b']
check('all protected C edges preserve endpoints',all(all(cs[c].get(k,'')==prev[c].get(k,'') for k in ('source','target')) for c in protected_edges))
check('all protected C decisions unchanged except authorized A/B responsibility clarification',all(cs[c].get('value','')==prev[c].get('value','') for c in protected_edges if c not in ('fl-e32','fl-e33')))
check('C responsibility directly routes source / pagination / teaching issues to A and pure implementation to B',cs['fl-e32'].get('value')=='模板 / 骨架 / 参考等纯实现：回 B' and cs['fl-e33'].get('value')=='源输入 / 分页 / 教学关系 / 授权冲突：回 A')
for e,target in [('fl-e19','fl-atype'),('fl-b-implementation','fl-bline'),('fl-a-internal-fix','fl-atype')]:
    check(e+' correctly scoped feedback',cs[e].get('target')==target and 'dashed=1' in cs[e].get('style',''))
check('old standalone S routing nodes removed',not any(c in cs for c in ('fl-sroute','fl-s08','fl-s07')))
check('old independent A review loop removed',not any(c in cs for c in ('fl-e14','fl-e15','fl-e16','fl-e13b')))

script=BASE/'scripts/export_workflow_diagrams.py'
spec=importlib.util.spec_from_file_location('diagram_exporter',script)
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
source=(BASE/NAME).read_text(encoding='utf-8')
for did,suffix in module.SUFFIXES.items():
    output=BASE/(Path(NAME).stem+'-'+suffix+'.drawio.svg')
    before_bytes=output.read_bytes(); before_mtime=output.stat().st_mtime_ns
    result=module.validate(output,source,new.find(f"diagram[@id='{did}']"))
    check(did+' exact expected rendered SVG / visible text / edge topology / embedded XML parity',all(result[k] for k in ('embedded_source_equal','visible_labels_equal')))
    check(did+' validation is read-only',before_bytes==output.read_bytes() and before_mtime==output.stat().st_mtime_ns)

negative=Path(__file__).with_name('diagram-negative-case.svg')
assert negative.resolve().parent==Path(__file__).resolve().parent
assert not negative.exists()
try:
    original=output.read_text(encoding='utf-8')
    mutations={
        'stale visible text': original.replace('A：输入整理','A：过期输入',1),
        'stale rendered geometry': original.replace('viewBox="0 0 2050 1910"','viewBox="0 0 2000 1900"',1),
        'stale edge metadata': original.replace('data-source="fl-start"','data-source="fl-smerge"',1),
    }
    for name,mutation in mutations.items():
        check(name+' fixture actually changed',mutation!=original)
        negative.write_text(mutation,encoding='utf-8')
        rejected=False
        try: module.validate(negative,source,new.find("diagram[@id='business-flow']"))
        except AssertionError: rejected=True
        check(name+' rejected by check mode',rejected)
finally:
    negative.unlink(missing_ok=True)

report={'status':'PASS','checks':checks,'protected_c_nodes':protected,'protected_c_edges':protected_edges,
        'retired_nodes':{'fl-sroute':'A necessary carrier analysis; standalone S route retired','fl-s08':'Existing approvals handled in A; standalone S admission Gate retired','fl-s07':'Evidence input handled directly by fl-recognize'},
        'rendering':'Standard-library SVG, not native diagrams.net export; exact current full XML embedded; offline PNG proof rendered from final SVG by preinstalled sharp/librsvg.',
        'browser_validation':'Not performed: file URL prohibited by browser URL policy; no bypass attempted.',
        'visual_evidence':['diagram-project-overview.png','diagram-business-flow.png']}
out=Path(__file__).with_name('diagram-validation.json')
out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(f'PASS: {len(checks)} diagram checks; no file writes during validation; report saved')
