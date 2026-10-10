"""Static contract checks; not a substitute for live conversation evaluation."""
from pathlib import Path
import os
import subprocess
import sys
from uuid import uuid4
import unittest
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]

class InteractionGateContract(unittest.TestCase):
    def test_all_stage_entries_have_necessity_filter_and_limits(self):
        for stage in ('stage-sline-srt-media-routing', 'stage-aline-course-visual-routing',
                      'stage-bline-production-handoff', 'stage-cline-gpt-image-execution-feedback'):
            with self.subTest(stage=stage):
                t = (ROOT / stage / 'SKILL.md').read_text(encoding='utf-8')
                for text in ('先判必要性，再提问', '不能说明回答将改变什么，不得阻塞',
                             '用户拒绝重复回答不是同意待决方案', '未覆盖才询问',
                             'interaction-gate-rules.md'):
                    self.assertIn(text, t)

    def test_sline_does_not_require_serial_approval(self):
        t = (ROOT / 'stage-sline-srt-media-routing/SKILL.md').read_text(encoding='utf-8')
        self.assertNotIn('当前项未确认不得进入下一项', t)
        self.assertTrue('默认课程视觉流程不设置独立 S' in t)
        self.assertTrue('本入口不输出冻结分页或教学候选分页' in t)
        self.assertTrue('已批准范围直接由 A 分析' in t)
        self.assertNotIn('不得输出冻结分页或正式 S 区', t)

    def test_progressive_protocol_matches_content_first(self):
        t = (ROOT / '_shared/progressive-reading-protocol.md').read_text(encoding='utf-8')
        self.assertNotIn('一次只确认一个类别', t)
        self.assertNotIn('再读取脚本并作路线', t)
        self.assertTrue('不由版式反推教学内容关系' in t)
        self.assertTrue('A在分页期间读取获准模板/素材的必要承载证据' in t)

    def test_drawio_gate_is_substantive(self):
        tree = ET.parse(ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio')
        nodes = {c.get('id'): c for c in tree.iter('mxCell')}
        cells = {key: c.get('value', '') for key, c in nodes.items()}
        edges = {(c.get('source'), c.get('target')) for c in nodes.values() if c.get('edge') == '1'}
        for removed in ('fl-s08', 'fl-s07', 'fl-sroute'):
            self.assertNotIn(removed, nodes)
        self.assertIn(('ov-input', 'ov-a'), edges)
        self.assertIn(('ov-a', 'ov-b'), edges)
        for node in ('fl-recognize', 'fl-abound', 'fl-layout-confirm', 'fl-agate',
                     'fl-atype', 'fl-areview', 'fl-aoutput'):
            self.assertEqual('fl-a-stage', nodes[node].get('parent'), node)
        for node in ('fl-agate', 'fl-atype', 'fl-areview'):
            self.assertNotIn('rhombus', nodes[node].get('style', ''), node)
        for edge, source, target in (('fl-e13', 'fl-areview', 'fl-aoutput'),
                                     ('fl-e17', 'fl-aoutput', 'fl-bline'),
                                     ('fl-e19', 'fl-bgate', 'fl-atype'),
                                     ('fl-b-implementation', 'fl-bgate', 'fl-bline')):
            self.assertEqual((source, target), (nodes[edge].get('source'), nodes[edge].get('target')))
        for edge in ('fl-s-optional', 'fl-s-input', 'fl-e19', 'fl-b-implementation'):
            self.assertIn('dashed=1', nodes[edge].get('style', ''))
        self.assertTrue('端到端授权内持续推进' in cells['ov-state'])
        self.assertTrue('不静默降级PSD' in cells['fl-layout-confirm'].replace(' ', ''))
        for value in cells.values():
            self.assertNotIn('逐项确认后', value)
            self.assertNotIn('逐类确认后', value)

    def test_scenario_contract_keeps_real_gates(self):
        t = (ROOT / '_shared/interaction-gate-rules.md').read_text(encoding='utf-8')
        for text in ('制作方式保持未定', '不推定8页方案获批', '不偷写文件',
                     '新增第9页', '代表页生成/扩批/最终定稿', '不能证明真实会话行为已稳定'):
            self.assertIn(text, t)

    def test_c_adapter_failure_returns_to_actual_responsible_stage(self):
        nodes = {c.get('id'): c for c in ET.parse(
            ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio').iter('mxCell')}
        for edge, source, target in (
            ('fl-e23', 'fl-tgate', 'fl-adapter-return'),
            ('fl-adapter-to-a', 'fl-adapter-return', 'fl-abound'),
            ('fl-adapter-to-b', 'fl-adapter-return', 'fl-bline'),
        ):
            self.assertEqual((source, target), (nodes[edge].get('source'), nodes[edge].get('target')))
        self.assertIn('立即停止', nodes['fl-tgate'].get('value'))
        self.assertIn('A：', nodes['fl-adapter-return'].get('value'))
        self.assertIn('B：', nodes['fl-adapter-return'].get('value'))

    def test_representative_confirmation_neither_authorizes_expansion_nor_finalizes(self):
        nodes = {c.get('id'): c for c in ET.parse(
            ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio').iter('mxCell')}
        edges = {(c.get('source'), c.get('target')) for c in nodes.values() if c.get('edge') == '1'}
        for pair in (
            ('fl-confirm', 'fl-delivery'), ('fl-delivery', 'fl-expand'),
            ('fl-expand', 'fl-assembly-candidate'), ('fl-assembly-candidate', 'fl-final-gate'),
            ('fl-final-gate', 'fl-final'), ('fl-final-gate', 'fl-diagnose'),
        ):
            self.assertIn(pair, edges)
        for pair in (('fl-confirm', 'fl-expand'), ('fl-confirm', 'fl-final'),
                     ('fl-delivery', 'fl-final'), ('fl-assembly-candidate', 'fl-final')):
            self.assertNotIn(pair, edges)
        self.assertIn('不等于非代表生图或最终定稿', nodes['fl-confirm'].get('value'))
        self.assertIn('不推定未验证状态通过', nodes['fl-confirm'].get('value'))
        self.assertIn('逐一列名页面及各一次首轮范围', nodes['fl-delivery'].get('value'))
        self.assertIn('未获授权不得扩展', nodes['fl-delivery'].get('value'))
        self.assertIn('不是 final_course_visual', nodes['fl-assembly-candidate'].get('value'))
        self.assertIn('用户是否确认最终定稿', nodes['fl-final-gate'].get('value'))

    def test_workflow_writing_gate_reuses_valid_authorization(self):
        nodes = {c.get('id'): c for c in ET.parse(
            ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio').iter('mxCell')}
        for cid in ('fl-manifest', 'ov-manifest'):
            text = nodes[cid].get('value')
            self.assertIn('已有写入授权', text)
            self.assertIn('告知后写', text)
            self.assertRegex(text, '未覆盖才(?:询)?问')
            self.assertNotIn('用户确认后才写', text)

    def test_diagrams_state_rule_authority_and_content_driven_expansion(self):
        nodes = {c.get('id'): c for c in ET.parse(
            ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio').iter('mxCell')}
        for cid in ('ov-authority', 'fl-authority'):
            text = nodes[cid].get('value')
            for marker in ('Markdown', '执行依据', '图须同步', 'SVG', '派生', '冲突需修正'):
                self.assertIn(marker, text)
        for cid, marker in (('fl-abound', '理解顺序'), ('fl-atype', '总分页'),
                            ('fl-atype', '状态'), ('fl-atype', '镜头'),
                            ('fl-agate', '不静态装箱'), ('fl-agate', '必呈项不等于全时同屏'),
                            ('fl-bline', '无匹配内构案例可进入代表页校准')):
            self.assertIn(marker, nodes[cid].get('value'))

    def test_limited_rule_wording_and_state_allocation_entrypoints(self):
        # These anchors catch known regressions only. They neither reconcile
        # arbitrary rule prose nor validate teaching, motion or rendered text.
        markers = {
            '_shared/course-visual-production-v2.7.md': (
                '规则权威与同步维护', '公共职责', '业务审阅视图', '派生展示',
                '必呈不等于全时同屏', 'same_screen_reason', 'cross_page_reason', 'reading_order'),
            '_shared/pagination-authority-rules.md': (
                '正文归属与视觉上下文分开', '后页预览', '不增加正文覆盖', '不改原旁白顺序'),
            'stage-aline-course-visual-routing/SKILL.md': (
                '必呈不等于全时同屏', '观察顺序', 'cross_page_reason', 'context_refs'),
            'stage-bline-production-handoff/SKILL.md': (
                '无匹配案例', 'reading_order', '准确可见文字子集', '全页其他状态去向', 'no_external_asset'),
            'stage-cline-gpt-image-execution-feedback/references/gpt_image_execution_adapter_rules.md': (
                '当前实际状态', '完整映射到全部状态', '状态说明不扩大',
                '当前状态/分配不明退B澄清', '教学/分页问题回A',
                '单张通过不释放未验证状态', 'no_external_asset'),
        }
        for relative, required in markers.items():
            text = (ROOT / relative).read_text(encoding='utf-8')
            with self.subTest(file=relative):
                for marker in required:
                    self.assertIn(marker, text)

    def test_export_check_rejects_stale_preview_and_never_writes(self):
        source = ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio'
        previews = list(ROOT.glob(source.stem + '-*.drawio.svg'))
        self.assertEqual(2, len(previews))
        # Plain mkdir retains workspace ACLs; tempfile's mode=0700 can make a
        # Windows sandbox directory inaccessible even to its creating process.
        temp = ROOT / ('.workflow-test-' + str(uuid4()))
        self.assertEqual(ROOT.resolve(), temp.resolve().parent)
        temp.mkdir()
        self.addCleanup(temp.rmdir)
        for path in [source, *previews]:
            target = temp / path.name
            self.addCleanup(lambda target=target: target.unlink(missing_ok=True))
            target.write_bytes(path.read_bytes())
        for optimize in ([], ['-O']):
            command = [sys.executable, '-B', *optimize, str(ROOT / 'scripts/export_workflow_diagrams.py'),
                       '--source', str(temp / source.name), '--check']
            utf8_env = dict(os.environ, PYTHONUTF8='1', PYTHONIOENCODING='utf-8')
            result = subprocess.run(command, env=utf8_env, capture_output=True, text=True, encoding='utf-8')
            self.assertEqual(0, result.returncode, result.stdout + result.stderr)
            for changed in (temp / previews[0].name, temp / source.name):
                with self.subTest(changed=changed.name, optimize=bool(optimize)):
                    original = changed.read_bytes()
                    changed.write_bytes(original + b'\n')
                    before = {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in temp.iterdir()}
                    result = subprocess.run(command, env=utf8_env, capture_output=True, text=True, encoding='utf-8')
                    self.assertNotEqual(0, result.returncode)
                    self.assertIn('preview differs', result.stderr)
                    after = {p.name: (p.read_bytes(), p.stat().st_mtime_ns) for p in temp.iterdir()}
                    self.assertEqual(before, after)
                    changed.write_bytes(original)

    def test_pagination_authority_is_available_at_each_entry(self):
        for stage in ('stage-sline-srt-media-routing', 'stage-aline-course-visual-routing',
                      'stage-bline-production-handoff'):
            with self.subTest(stage=stage):
                t = (ROOT / stage / 'SKILL.md').read_text(encoding='utf-8')
                self.assertIn('pagination-authority-rules.md', t)
                self.assertTrue('源' in t and 'A' in t and '分页' in t)
        authority = (ROOT / '_shared/pagination-authority-rules.md').read_text(encoding='utf-8')
        self.assertTrue('分页批准不是A分析前置条件' in authority)
        self.assertTrue('原文和准入未变不重跑S' in authority)
        self.assertTrue('逐字起止（均含）' in authority)

    def test_authority_preserves_approvals_and_limits(self):
        t = (ROOT / '_shared/pagination-authority-rules.md').read_text(encoding='utf-8')
        for phrase in ('源文片段', '教学单元', '执行页面', 'A分页方案已内部复核',
                       '执行分页已批准', '原文和准入未变不重跑S', '无关页的有效决定保留',
                       '不原地重编号', '正文归属与视觉上下文分开',
                       '用户明确批准S候选方案时，该批准仍有效', 'Non-A不等于删除',
                       '独立审者的自动触发条件本轮不定义', '不证明教学分页合理'):
            self.assertTrue(phrase in t, phrase)

    def test_a_entry_owns_final_pages_without_prebuilt_s_pages(self):
        t = (ROOT / 'stage-aline-course-visual-routing/SKILL.md').read_text(encoding='utf-8')
        self.assertTrue('A 负责明确分页' in t)
        for phrase in ('全文分析', '拆合', '全套内部复核'):
            self.assertTrue(phrase in t, phrase)
        self.assertTrue('只有用户明确要求独立复核时' in t)
        self.assertNotIn('与已由用户确认的 S07 共享页面简报', t)
        template = (ROOT / 'stage-sline-srt-media-routing/templates/s_line_segment_card.md').read_text(encoding='utf-8')
        self.assertTrue('不创建 page_id' in template)
        self.assertTrue('不预交一套教学候选分页' in template)
        self.assertTrue('逐字起止（均含）' in template)

if __name__ == '__main__':
    unittest.main()
