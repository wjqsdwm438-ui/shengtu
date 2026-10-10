from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1] / 'skills-v2.7-development-snapshot-20260814' / '项目源码'
BACKUP = Path(__file__).resolve().parent / 'interaction-gate-backup-20260906'
replacements = {
 'stage-aline-course-visual-routing/SKILL.md': [
 ('A 区或 A 审结论完成后停止，不自动读取 B/C，不决定模板、骨架、生产批次或生成方式。', '单阶段授权下，A区或A审结论完成后停止；明确端到端授权下，无未决实质Gate则推进下一阶段。A线自身不决定模板、骨架、生产批次或生成方式。'),
 ('写完立即停止，不得顺带生成 B/C 内容。', '单阶段授权写完即停；端到端授权按交互Gate规则继续，不在A区混写B/C内容。')],
 'stage-sline-srt-media-routing/SKILL.md': [
 ('写完立即停止，不得顺带追加 A/B/C 内容。', '单阶段授权写完即停；端到端授权按交互Gate规则继续，各阶段只追加所属分区。')],
 'stage-bline-production-handoff/SKILL.md': [
 ('B区、批次校准状态或退回报告完成后立即停止。一次授权只覆盖当前产物，不自动开始 C线生成；这是本阶段边界。', '单阶段授权下，B区、批次校准状态或退回报告完成后停止。端到端授权下可推进已满足输入条件的C线适配，但生成必须另有当前具体页面的明确授权；不因跨阶段名称重复索批。')],
}
for rel, pairs in replacements.items():
    p = ROOT / rel
    t = p.read_text(encoding='utf-8')
    for old, new in pairs:
        assert old in t, (rel, old)
        t = t.replace(old, new)
    p.write_text(t, encoding='utf-8', newline='\n')

p = ROOT / 'run_all_checks.py'
shutil.copy2(p, BACKUP / p.name)
t = p.read_text(encoding='utf-8-sig')
needle = '    check_script_syntax(report)\n'
assert needle in t
t = t.replace(needle, needle + '''    interaction = subprocess.run(
        [sys.executable, str(ROOT / "tests" / "test_interaction_gate_contract.py")],
        cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace",
    )
    report.check(interaction.returncode == 0, "interaction:gate_contract",
                 interaction.stdout + interaction.stderr)
''')
p.write_text(t, encoding='utf-8', newline='\n')
print('Removed residual stage-stop conflicts and integrated regression test.')
