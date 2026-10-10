from pathlib import Path
import json
import re
import subprocess
import sys

ROOT = Path(r'E:\shengtu\skills-v2.7-development-snapshot-20260814')
WORK = ROOT / 'work/media_judgment_revision_20260907'
READER = Path(r'C:\Users\Administrator\.codex\tools\read_utf8_text.py')
FILES = [ROOT / 'A线/8.1_分页方案.md', ROOT / 'A线/8.1_修改执行与媒体复核评价_R4.md']


def read_checked(path):
    subprocess.run([sys.executable, '-B', str(READER), str(path), '--check-only'],
                   stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
    return path.read_bytes().decode('utf-8-sig')


def main():
    missing = []
    checked_links = set()
    for path in FILES:
        body = read_checked(path)
        for target in re.findall(r'\]\(([A-Z]:/[^)]+)\)', body):
            checked_links.add(target)
            if not Path(target.split('#', 1)[0]).exists():
                missing.append({'document': str(path), 'target': target})
    pages = json.loads(read_checked(WORK / '8.1_媒体状态数据.json'))
    prior = WORK / '修改前备份/A线/8.1_分页方案.md'
    archived = ROOT / 'A线/8.1_分页方案_历史R3_媒体组织结论已替代.md'
    preserved = prior.is_file() and prior.read_bytes() == archived.read_bytes()
    b = read_checked(FILES[0])
    result = {
        'checked_local_link_count': len(checked_links), 'missing_links': missing,
        'page_count': len(pages), 'state_count': sum(len(p['states']) for p in pages),
        'planned_seconds': sum(s['seconds'] for p in pages for s in p['states']),
        'formal_page_sections': len(re.findall(r'^### P\d{2}｜', b, re.M)),
        'complete_representative_B_sections': b.count('#### B区｜本轮代表状态的完整执行设计'),
        'history_R3_exactly_preserves_pre_revision_master': preserved,
        'scope': 'local links, structural counts and exact historical preservation only; not image or teaching-effect validation',
    }
    result['passed'] = (not missing and preserved and result['page_count'] == 11
                        and result['state_count'] == 30 and result['planned_seconds'] == 360
                        and result['formal_page_sections'] == 11
                        and result['complete_representative_B_sections'] == 2)
    (WORK / '交付文件检查.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))
    raise SystemExit(0 if result['passed'] else 2)


if __name__ == '__main__':
    main()
