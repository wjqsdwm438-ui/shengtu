"""Read-only final verification; evidence goes outside the source directory."""
from pathlib import Path
import json
import os
import subprocess
import sys

HERE = Path(__file__).resolve().parent
WORKSPACE = HERE.parent.parent
SOURCE = WORKSPACE / 'skills-v2.7-development-snapshot-20260814' / '项目源码'


def snapshot():
    files = {}
    directories = []
    for path in SOURCE.rglob('*'):
        relative = path.relative_to(SOURCE).as_posix()
        if path.is_file():
            files[relative] = (path.read_bytes(), path.stat().st_mtime_ns)
        elif path.is_dir():
            directories.append(relative)
    return files, sorted(directories)


before, before_dirs = snapshot()
env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
commands = [
    ('run_all_checks', ['run_all_checks.py']),
    ('unit_tests', ['-m', 'unittest', 'discover', '-s', 'tests', '-p', 'test_*.py']),
    ('pagination_example', ['scripts/validate_pagination_plan.py', 'tests/pagination_plan_valid.json']),
    ('workflow_svg_check', ['scripts/export_workflow_diagrams.py', '--check']),
]
results = []
for name, arguments in commands:
    result = subprocess.run([sys.executable, '-B', *arguments], cwd=SOURCE,
                            env=env, capture_output=True, text=True, encoding='utf-8')
    (HERE / f'final-{name}.stdout.txt').write_text(result.stdout, encoding='utf-8')
    (HERE / f'final-{name}.stderr.txt').write_text(result.stderr, encoding='utf-8')
    results.append({'name': name, 'arguments': arguments, 'exit_code': result.returncode})
    print(f'{name}: exit {result.returncode}')
    print((result.stdout + result.stderr)[-2200:])

after, after_dirs = snapshot()
changed = [p for p in before.keys() & after.keys() if before[p] != after[p]]
new = sorted(after.keys() - before.keys())
removed = sorted(before.keys() - after.keys())
report = {
    'scope': str(SOURCE),
    'commands': results,
    'files_compared': len(before),
    'comparison': 'exact bytes and st_mtime_ns, plus complete directory names',
    'changed_files': sorted(changed),
    'new_files': new,
    'removed_files': removed,
    'new_directories': sorted(set(after_dirs) - set(before_dirs)),
    'removed_directories': sorted(set(before_dirs) - set(after_dirs)),
    'all_checks_passed': all(r['exit_code'] == 0 for r in results),
    'source_directory_unchanged': before == after and before_dirs == after_dirs,
}
(HERE / 'final-verification.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
sys.exit(0 if report['all_checks_passed'] and report['source_directory_unchanged'] else 1)
