"""Static contract checks; not a substitute for live conversation evaluation."""
from pathlib import Path
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
                       '不原地重编号', '正文归属与上下文回指分开',
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
