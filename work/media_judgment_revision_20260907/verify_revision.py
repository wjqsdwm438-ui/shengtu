from pathlib import Path
from datetime import datetime, timezone
import json
import subprocess
import sys
import time

ROOT = Path(r'E:\shengtu\skills-v2.7-development-snapshot-20260814')
CODE = ROOT/'skills-v2.7-development-snapshot-20260814/项目源码'
WORK = ROOT/'work/media_judgment_revision_20260907'
SOURCE = Path(r'E:\shengtu\智能网联\8.1正文.md')
READER = Path(r'C:\Users\Administrator\.codex\tools\read_utf8_text.py')


def snapshot():
    return {str(p.relative_to(CODE)): (p.read_bytes(), p.stat().st_mtime_ns)
            for p in CODE.rglob('*') if p.is_file()}


def main():
    before = snapshot()
    source_before = (SOURCE.read_bytes(), SOURCE.stat().st_mtime_ns)
    started = time.monotonic()
    commands = [
        ('all_checks', [sys.executable,'-B','run_all_checks.py']),
        ('unittest', [sys.executable,'-B','-m','unittest','discover','-s','tests','-p','test_*.py']),
        ('diagram_sync', [sys.executable,'-B','scripts/export_workflow_diagrams.py','--check']),
        ('a81_pagination', [sys.executable,'-B','scripts/validate_pagination_plan.py',str(ROOT/'A线/8.1_A线R4_校验输入.json')]),
    ]
    results=[]
    for name,cmd in commands:
        t=time.monotonic()
        result=subprocess.run(cmd,cwd=CODE,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=180)
        stdout=result.stdout.decode('utf-8'); stderr=result.stderr.decode('utf-8')
        (WORK/(name+'.stdout.txt')).write_text(stdout,encoding='utf-8')
        (WORK/(name+'.stderr.txt')).write_text(stderr,encoding='utf-8')
        results.append(dict(name=name,command=cmd,returncode=result.returncode,seconds=round(time.monotonic()-t,3),stdout=stdout,stderr=stderr))
        print(name, result.returncode, stdout[-450:].strip(), stderr[-200:].strip())
    after=snapshot()
    added=sorted(after.keys()-before.keys()); removed=sorted(before.keys()-after.keys())
    changed=sorted(k for k in before.keys()&after.keys() if before[k]!=after[k])
    baseline=WORK/'修改前备份'
    modified=[]; new=[]; utf8=[]; inventory_excluded=[]
    for p in CODE.rglob('*'):
        if not p.is_file(): continue
        if '__pycache__' in p.parts:
            # Baseline backup deliberately excluded caches; existence now cannot
            # establish that they were introduced in this revision. The full
            # before/after readonly snapshot above still includes these files.
            inventory_excluded.append(str(p.relative_to(CODE)))
            continue
        old=baseline/p.relative_to(ROOT)
        if not old.exists(): new.append(str(p.relative_to(CODE)))
        elif p.read_bytes()!=old.read_bytes(): modified.append(str(p.relative_to(CODE)))
        if p.suffix.lower() in ('.md','.py','.drawio','.svg','.json','.yaml','.txt'):
            check=subprocess.run([sys.executable,str(READER),str(p),'--check-only'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
            if check.returncode: utf8.append(str(p))
    result=dict(checked_at=datetime.now(timezone.utc).isoformat(),commands=results,
        readonly_check=dict(added=added,removed=removed,byte_or_mtime_changed=changed,passed=not(added or removed or changed)),
        original_source_unchanged_during_verification=source_before==(SOURCE.read_bytes(),SOURCE.stat().st_mtime_ns),
        utf8_failures=utf8,modified_code_files=sorted(modified),new_code_files=sorted(new),
        baseline_inventory_excluded_caches=sorted(inventory_excluded),
        image_calls=0,image_output_files=[],image_status='not_executed_awaiting_named_authorization',
        source_bytes=len(source_before[0]),seconds=round(time.monotonic()-started,3))
    result['passed']=all(r['returncode']==0 for r in results) and result['readonly_check']['passed'] and result['original_source_unchanged_during_verification'] and not utf8
    (WORK/'最终验证结果.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    a_result=json.loads(next(x['stdout'] for x in results if x['name']=='a81_pagination'))
    (ROOT/'A线/8.1_A线R4_校验结果.json').write_text(json.dumps(a_result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('passed','readonly_check','original_source_unchanged_during_verification','utf8_failures','seconds')},ensure_ascii=False))
    raise SystemExit(0 if result['passed'] else 2)


if __name__=='__main__':main()
