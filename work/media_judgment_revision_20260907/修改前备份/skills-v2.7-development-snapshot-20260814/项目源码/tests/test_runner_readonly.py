"""Integration proof that default checks leave input/evidence files untouched."""
from pathlib import Path
import os
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]


class RunnerReadOnlyTests(unittest.TestCase):
    def test_default_runner_preserves_fixtures_and_checked_in_evidence(self):
        def state():
            return {path: (path.read_bytes(), path.stat().st_mtime_ns)
                    for directory in ('tests', 'test_logs', 'scripts')
                    for path in (ROOT / directory).rglob('*')
                    if path.is_file() and '__pycache__' not in path.parts}

        before = state()
        env = dict(os.environ, PYTHONUTF8='1', PYTHONDONTWRITEBYTECODE='1')
        result = subprocess.run([sys.executable, '-B', str(ROOT / 'run_all_checks.py')],
            cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8', check=False)
        self.assertEqual(0, result.returncode, result.stdout + result.stderr)
        after = state()
        self.assertEqual(set(before), set(after), 'default run created or removed managed inputs/evidence')
        changed = [str(path.relative_to(ROOT)) for path in before if before[path] != after[path]]
        self.assertEqual([], changed, 'default run rewrote managed input/evidence')
        self.assertFalse(list(ROOT.glob('.run_all_checks_tmp-*')), 'temporary runner output not cleaned up')
        self.assertFalse(list(ROOT.glob('.pagination-test-*')), 'temporary synthetic source not cleaned up')


if __name__ == '__main__':
    unittest.main()
