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
        self.assertIn('随具体分页方案提交同一次审阅', t)
        self.assertIn('用户未明确确认分页方案时，不得输出冻结分页或正式 S 区', t)

    def test_progressive_protocol_matches_content_first(self):
        t = (ROOT / '_shared/progressive-reading-protocol.md').read_text(encoding='utf-8')
        self.assertNotIn('一次只确认一个类别', t)
        self.assertNotIn('再读取脚本并作路线', t)
        self.assertIn('S/A不由版式反推教学关系', t)

    def test_drawio_gate_is_substantive(self):
        tree = ET.parse(ROOT / '课程视觉生产工具V2.7_项目节点与流程.drawio')
        cells = {c.get('id'): c.get('value', '') for c in tree.iter('mxCell')}
        self.assertIn('无新歧义：路由清单随分页审阅', cells['fl-s08'])
        self.assertIn('未批准分页不得冻结', cells['fl-s08'])
        self.assertIn('不重复询问是否进入A线', cells['fl-s07'])
        self.assertIn('端到端授权内持续推进', cells['ov-state'])

    def test_scenario_contract_keeps_real_gates(self):
        t = (ROOT / '_shared/interaction-gate-rules.md').read_text(encoding='utf-8')
        for text in ('制作方式保持未定', '不推定8页方案获批', '不偷写文件',
                     '新增第9页', '代表页生成/扩批/最终定稿', '不能证明真实会话行为已稳定'):
            self.assertIn(text, t)

if __name__ == '__main__':
    unittest.main()
