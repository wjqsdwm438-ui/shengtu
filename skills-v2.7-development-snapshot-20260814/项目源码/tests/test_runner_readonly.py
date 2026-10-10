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
            paths = [path for directory in ('tests', 'test_logs', 'scripts')
                     for path in (ROOT / directory).rglob('*')
                     if path.is_file() and '__pycache__' not in path.parts]
            paths += list(ROOT.glob('*.drawio')) + list(ROOT.glob('*.drawio.svg'))
            return {path: (path.read_bytes(), path.stat().st_mtime_ns) for path in paths}

        before = state()
        # The normal CLI must not depend on the caller setting UTF-8 first.
        for mode in ('utf8', 'unset', 'legacy_gbk'):
            with self.subTest(environment=mode):
                env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
                env.pop('PYTHONUTF8', None)
                env.pop('PYTHONIOENCODING', None)
                if mode == 'utf8':
                    env.update(PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
                elif mode == 'legacy_gbk':
                    env.update(PYTHONUTF8='0', PYTHONIOENCODING='gbk')
                result = subprocess.run([sys.executable, '-B', str(ROOT / 'run_all_checks.py')],
                    cwd=ROOT, env=env, capture_output=True, text=True, encoding='utf-8', check=False)
                self.assertEqual(0, result.returncode, result.stdout + result.stderr)
                self.assertIn('[PASS] diagrams:drawio_svg_readonly_sync', result.stdout)
                self.assertIn('[PASS] interaction:gate_contract', result.stdout)
        after = state()
        self.assertEqual(set(before), set(after), 'default run created or removed managed inputs/evidence')
        changed = [str(path.relative_to(ROOT)) for path in before if before[path] != after[path]]
        self.assertEqual([], changed, 'default run rewrote managed input/evidence')
        self.assertFalse(list(ROOT.glob('.run_all_checks_tmp-*')), 'temporary runner output not cleaned up')
        self.assertFalse(list(ROOT.glob('.pagination-test-*')), 'temporary synthetic source not cleaned up')
        self.assertFalse(list(ROOT.glob('.workflow-test-*')), 'temporary diagram source not cleaned up')


if __name__ == '__main__':
    unittest.main()
