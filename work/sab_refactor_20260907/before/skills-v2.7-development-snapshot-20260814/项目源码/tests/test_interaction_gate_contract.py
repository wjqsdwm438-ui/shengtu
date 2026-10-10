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
        self.assertIn('已批准文字范围直接交A分析', t)
        self.assertIn('用户未明确确认分页方案时，不得输出冻结分页', t)
        self.assertNotIn('不得输出冻结分页或正式 S 区', t)

    def test_progressive_protocol_matches_content_first(self):
        t = (ROOT / '_shared/progressive-reading-protocol.md').read_text(encoding='utf-8')
        self.assertNotIn('一次只确认一个类别', t)
        self.assertNotIn('再读取脚本并作路线', t)
        self.assertIn('S/A不由版式反推教学关系', t)

    def test_drawio_gate_is_substantive(self):
        tree = ET.parse(ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio')
        cells = {c.get('id'): c.get('value', '') for c in tree.iter('mxCell')}
        self.assertIn('文字范围获批即可交A分析', cells['fl-s08'])
        self.assertIn('未批准分页不得冻结', cells['fl-s08'])
        self.assertIn('不重复询问是否进入A线', cells['fl-s07'])
        self.assertIn('端到端授权内持续推进', cells['ov-state'])
        self.assertIn('关键语义冲突才问用户', cells['fl-a-confirm'])
        self.assertIn('不静默降级PSD', cells['fl-layout-confirm'])
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
                self.assertIn('分页批准不是A分析前置条件', t)
                self.assertIn('原文和准入未变不重跑S', t)
                self.assertIn('pagination-authority-rules.md', t)
                self.assertIn('逐字起止（均含）', t)

    def test_authority_preserves_approvals_and_limits(self):
        t = (ROOT / '_shared/pagination-authority-rules.md').read_text(encoding='utf-8')
        for phrase in ('源文片段', '教学单元', '执行页面', 'A教学分组已复核',
                       '执行分页已批准', '源文未变不回S', '不要求A/S重做已有效结论',
                       '不原地重编号', '自动多对多映射', '用户明确批准S候选方案时，该批准仍有效'):
            self.assertIn(phrase, t)

    def test_a_entry_and_templates_do_not_require_final_pages(self):
        t = (ROOT / 'stage-aline-course-visual-routing/SKILL.md').read_text(encoding='utf-8')
        self.assertIn('仅候选切分存在时可以先做教学分组复核', t)
        self.assertNotIn('与已由用户确认的 S07 共享页面简报', t)
        template = (ROOT / 'stage-sline-srt-media-routing/templates/s_line_segment_card.md').read_text(encoding='utf-8')
        self.assertIn('不隐含最终分页批准', template)
        self.assertIn('逐字起止（均含）', template)

if __name__ == '__main__':
    unittest.main()
