"""Synthetic source-coverage tests. No lesson manuscript or image generation."""
from copy import deepcopy
from pathlib import Path
import json
import sys
import unittest
from uuid import uuid4

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from validate_pagination_plan import validate_pagination_plan
from validate_page_brief import validate_contract


def span(line, start=1, end=4):
    text = {1: '甲乙丙丁', 2: '戊己庚辛', 3: '壬癸子丑', 4: '批注勿归'}[line]
    return dict(source_id='source-1', line=line, start_char=start, end_char=end,
                start_text=text[start - 1], end_text=text[end - 1])


def review(plan):
    plan['internal_review'] = dict(
        plan_id=plan['plan_id'], plan_version=plan['plan_version'], status='completed',
        reviewed_page_spans=[dict(page_id=p['page_id'], owned_spans=deepcopy(p['owned_spans']))
                             for p in plan['pages']],
        checks=[dict(item=item, result='pass', evidence_refs=['source:source-1', 'comparison:compare-1'])
                for item in ('source_coverage', 'source_order', 'boundaries', 'capacity',
                             'split_merge', 'non_a_retention')], unresolved_issues=[])
    return plan


def make_plan(source_path, page_spans=None):
    groups = page_spans or [[span(1)], [span(2)]]
    pages = [dict(page_id=f'KP-{i:02}', order=i, owned_spans=owned, context_refs=[],
                  capacity_basis=dict(teaching_task='比较状态', required_text_and_labels=['状态标签'],
                      approved_assets=[], asset_applicability_reason='合成原文覆盖测试不涉及真实生产资产，故不适用。',
                      same_screen_reason='同页比较两个状态', cross_page_reason='不同学习任务跨页',
                      visual_carrier_feasibility='成对关系可表达，尚未制作',
                      unverified_limits='未生图；不能证明真实模板承载或教学效果'))
             for i, owned in enumerate(groups, 1)]
    return review(dict(schema='course_visual_a_pagination/v1', plan_id='plan-synthetic', plan_version=1,
        source_evidence=dict(sources=[dict(source_id='source-1', path=str(source_path),
                             version='synthetic-v1', version_date='2026-09-07', order=1)],
            approved_body_spans=[span(1), span(2), span(3)], annotation_spans=[span(4)],
            approval=dict(status='confirmed', record='synthetic approval; not a real lesson')),
        pages=pages,
        non_a_dispositions=[dict(disposition_id='non-a-1', owned_spans=[span(3)],
                                reason='保留原文，不需要新图', target='existing_material')],
        split_merge_comparisons=[dict(comparison_id='compare-1',
            source_spans=[s for p in pages for s in p['owned_spans']],
            alternatives=[dict(candidate_id='alternative', proposed_page_spans=(
                               [[span(1)], [span(2)]] if len(pages) == 1 else [[span(1), span(2)]]),
                               reason='synthetic joint display; not a quality conclusion')],
            selected_page_ids=[p['page_id'] for p in pages], decision_reason='测试记录，不声称教学合理')]))


def attach_plan(contract, plan):
    contract['workflow']['stages'] = ['A', 'B', 'C_adapter', 'C_generate', 'assembly']
    contract['a_pagination_plan'] = plan
    for wrapper, pp in zip(contract['page_briefs'], plan['pages']):
        page = wrapper['page_brief']
        page.pop('s_section', None)
        page['a_section'].pop('a_review_status', None)
        ref = dict(plan_id=plan['plan_id'], plan_version=plan['plan_version'],
                   page_id=pp['page_id'], owned_spans=deepcopy(pp['owned_spans']))
        page['a_section']['pagination_ref'] = deepcopy(ref)
        page['b_section']['pagination_ref'] = deepcopy(ref)
        page['b_section']['pagination_feedback'] = []
        preflight = page['c_section']['adapter_preflight']
        preflight.pop('s_section_complete', None)
        preflight['a_pagination_plan_complete'] = 'yes'
        preflight['source_evidence_complete'] = 'yes'
        preflight['A_internal_review_complete'] = 'yes'
    return contract


class PaginationContractTests(unittest.TestCase):
    def setUp(self):
        directory = ROOT / ('.pagination-test-' + str(uuid4()))
        directory.mkdir()
        self.addCleanup(directory.rmdir)
        self.path = directory / 'source.txt'
        self.addCleanup(lambda: self.path.unlink(missing_ok=True))
        self.path.write_text('甲乙丙丁\n戊己庚辛\n壬癸子丑\n批注勿归\n', encoding='utf-8')
        self.plan = make_plan(self.path)

    def errors(self, plan=None):
        errors, _ = validate_pagination_plan(plan or self.plan, self.path.parent / 'plan.json')
        return {e.code for e in errors}

    def test_valid_two_pages_non_a_retained(self):
        self.assertEqual(set(), self.errors())

    def test_different_legal_page_counts_and_many_to_many(self):
        for groups in ([[span(1), span(2)]],
                       [[span(1, 1, 2)], [span(1, 3, 4), span(2, 1, 2)], [span(2, 3, 4)]]):
            with self.subTest(groups=groups):
                self.assertEqual(set(), self.errors(make_plan(self.path, groups)))

    def test_missing_source_body_is_rejected(self):
        self.plan['pages'][0]['owned_spans'] = [span(1, 1, 3)]
        self.assertIn('pagination.coverage_missing', self.errors())

    def test_duplicate_ownership_is_rejected(self):
        self.plan['pages'][1]['owned_spans'].insert(0, span(1))
        self.assertIn('pagination.coverage_overlap', self.errors())

    def test_non_a_is_not_deleted(self):
        self.plan['non_a_dispositions'] = []
        self.assertIn('pagination.coverage_missing', self.errors())

    def test_annotation_cannot_be_owned(self):
        self.plan['pages'][1]['owned_spans'].append(span(4))
        self.assertIn('pagination.annotation_owned', self.errors())

    def test_approved_body_cannot_silently_include_annotation(self):
        self.plan['source_evidence']['approved_body_spans'].append(span(4))
        self.assertIn('pagination.scope_annotation_overlap', self.errors())

    def test_context_backreference_does_not_duplicate_body(self):
        self.plan['pages'][1]['context_refs'] = [span(1)]
        self.assertEqual(set(), self.errors())

    def test_context_cannot_cover_missing_body_or_future_page(self):
        self.plan['pages'][0]['context_refs'] = [span(2)]
        self.assertIn('pagination.context_not_prior', self.errors())
        self.plan['pages'][0]['owned_spans'] = []
        self.plan['pages'][1]['context_refs'] = [span(1)]
        self.assertIn('pagination.coverage_missing', self.errors())

    def test_out_of_range_and_bad_types_fail_closed(self):
        for field, value in [('line', 999), ('start_char', 0), ('end_char', 999),
                             ('line', True), ('line', []), ('source_id', {})]:
            with self.subTest(field=field, value=value):
                plan = deepcopy(self.plan)
                plan['pages'][0]['owned_spans'][0][field] = value
                self.assertTrue(self.errors(plan))
        for field in ('pages', 'source_evidence', 'internal_review', 'split_merge_comparisons'):
            for value in (None, True, 'bad', []):
                with self.subTest(field=field, value=value):
                    plan = deepcopy(self.plan)
                    plan[field] = value
                    self.assertTrue(self.errors(plan))

    def test_anchor_mismatch_and_missing_source(self):
        self.plan['pages'][0]['owned_spans'][0]['start_text'] = '错误'
        self.assertIn('pagination.anchor_mismatch', self.errors())
        self.path.unlink()
        self.assertIn('pagination.source_unreadable', self.errors())

    def test_source_order_preserved(self):
        self.plan['pages'][0]['owned_spans'], self.plan['pages'][1]['owned_spans'] = (
            self.plan['pages'][1]['owned_spans'], self.plan['pages'][0]['owned_spans'])
        self.assertIn('pagination.source_order', self.errors())

    def test_legacy_nine_passes_cannot_replace_internal_review(self):
        self.plan.pop('internal_review')
        self.plan['a_review_status'] = 'passed'
        self.plan['legacy_nine_units'] = dict(status='passed', page_count=9)
        self.assertIn('pagination.internal_review', self.errors())

    def test_review_version_and_boundaries_are_current(self):
        self.plan['plan_version'] = 2
        self.assertIn('pagination.review_version', self.errors())
        self.plan['plan_version'] = 1
        self.plan['internal_review']['reviewed_page_spans'][0]['owned_spans'] = [span(2)]
        self.assertIn('pagination.review_boundaries', self.errors())

    def test_boolean_cannot_impersonate_integer_in_review_or_a_b_reference(self):
        self.plan['internal_review']['reviewed_page_spans'][0]['owned_spans'][0]['line'] = True
        self.assertIn('pagination.review_boundaries', self.errors())
        review(self.plan)
        data, path = self.contract()
        data['page_briefs'][0]['page_brief']['b_section']['pagination_ref']['plan_version'] = True
        errors, _ = validate_contract(data, path)
        self.assertIn('pagination.page_mapping', {e.code for e in errors})

    def test_multiple_sources_keep_independent_order_and_versions(self):
        second = self.path.parent / 'second.txt'
        second.write_text('甲乙丙丁\n戊己庚辛\n壬癸子丑\n批注勿归\n', encoding='utf-8')
        self.addCleanup(lambda: second.unlink(missing_ok=True))
        evidence = self.plan['source_evidence']
        evidence['sources'].append(dict(source_id='source-2', path=str(second), version='v2',
                                        version_date='2026-09-07', order=2))
        extra = dict(span(1), source_id='source-2')
        evidence['approved_body_spans'].append(extra)
        self.plan['pages'][1]['owned_spans'].append(deepcopy(extra))
        comparison = self.plan['split_merge_comparisons'][0]
        comparison['source_spans'].append(deepcopy(extra))
        comparison['alternatives'][0]['proposed_page_spans'][0].append(deepcopy(extra))
        review(self.plan)
        self.assertEqual(set(), self.errors())
        evidence['sources'][1]['order'] = 1
        self.assertIn('pagination.source_order', self.errors())

    def test_unknown_review_reference_is_rejected(self):
        self.plan['internal_review']['checks'][0]['evidence_refs'] = ['legacy:9-passed']
        self.assertIn('pagination.review_reference', self.errors())

    def test_same_count_different_boundaries_is_legal(self):
        alternative = self.plan['split_merge_comparisons'][0]['alternatives'][0]
        alternative['proposed_page_spans'] = [[span(1), span(2, 1, 2)], [span(2, 3, 4)]]
        self.assertEqual(set(), self.errors())

    def test_no_reasonable_alternative_is_recorded_not_fabricated(self):
        comparison = self.plan['split_merge_comparisons'][0]
        comparison['alternatives'] = []
        comparison['no_reasonable_alternative_reason'] = '当前两项任务及可见标签已核对；未发现有依据的替代，尚未生图。'
        self.assertEqual(set(), self.errors())
        comparison.pop('no_reasonable_alternative_reason')
        self.assertIn('pagination.comparison_no_alternative', self.errors())

    def test_comparisons_may_focus_only_on_risky_boundaries(self):
        comparison = self.plan['split_merge_comparisons'][0]
        comparison['source_spans'] = [span(1)]
        comparison['selected_page_ids'] = ['KP-01']
        comparison['alternatives'] = []
        comparison['no_reasonable_alternative_reason'] = '局部同屏必要，另一页在全套内部复核中检查。'
        self.assertEqual(set(), self.errors())

    def test_alternative_must_map_real_source_not_a_page_count_label(self):
        comparison = self.plan['split_merge_comparisons'][0]
        comparison['alternatives'][0]['proposed_page_spans'] = [[span(1)]]
        self.assertIn('pagination.comparison_alternative_mapping', self.errors())

    def test_same_boundaries_are_not_disguised_as_alternatives(self):
        comparison = self.plan['split_merge_comparisons'][0]
        comparison['alternatives'][0]['proposed_page_spans'] = [[span(1)], [span(2)]]
        self.assertIn('pagination.comparison_unchanged_alternatives', self.errors())
        comparison['no_reasonable_alternative_reason'] = '确认是现方案，无合理不同边界；未声明教学效果已证实。'
        self.assertEqual(set(), self.errors())

    def test_b_c_gates_remain_enforced_on_new_workflow(self):
        cases = [
            ('b.evidence_asset_missing', lambda d: d['page_briefs'][0]['page_brief']['b_section']['implementation_evidence']['asset_used'][0].update(real_path='missing-evidence.png')),
            ('batch.representative_unconfirmed', lambda d: d['batches'][0].update(representative_status='pending')),
            ('image.fixed_share', lambda d: d.update(image_area_percentage=70)),
            ('batch.fixed_count', lambda d: d['workflow'].update(fixed_batch_count=1)),
            ('b.batch_isolation', lambda d: d['page_briefs'][0]['page_brief']['b_section']['batch_assignment'].update(include_other_batches_context='yes')),
            ('c.required_field', lambda d: d['page_briefs'][0]['page_brief']['c_section']['compiled_execution_contract']['technical_parameters'].update(size='')),
            ('c.asset_missing', lambda d: d['page_briefs'][0]['page_brief']['c_section']['compiled_execution_contract']['template_identity'].update(master_asset_path='missing-master.png')),
            ('inheritance.teaching_relation', lambda d: d['page_briefs'][1]['page_brief']['a_section']['teaching_relation'].update(relation_kind='unrelated')),
        ]
        for expected, mutate in cases:
            with self.subTest(expected=expected):
                data, path = self.contract()
                mutate(data)
                errors, _ = validate_contract(data, path)
                self.assertIn(expected, {e.code for e in errors})

    def test_capacity_asset_must_exist(self):
        self.plan['pages'][0]['capacity_basis']['approved_assets'] = [dict(
            path='missing-template.png', approval_record='synthetic', usable_space_and_limits='safe region')]
        self.assertIn('pagination.capacity_asset_missing', self.errors())

    def contract(self):
        fixture = ROOT / 'tests/page_brief_contract_valid.json'
        return attach_plan(json.loads(fixture.read_text(encoding='utf-8-sig')), self.plan), fixture

    def test_new_workflow_without_s_or_independent_review_passes(self):
        data, path = self.contract()
        errors, derived = validate_contract(data, path)
        self.assertEqual([], errors)
        self.assertFalse(derived['pedagogical_quality_verified'])

    def test_old_workflow_and_legacy_only_contract_rejected(self):
        data, path = self.contract()
        data['workflow']['stages'] = ['S', 'A', 'A_review', 'B', 'C_adapter', 'C_generate', 'assembly']
        data.pop('a_pagination_plan')
        errors, _ = validate_contract(data, path)
        self.assertIn('workflow.stages', {e.code for e in errors})
        self.assertIn('pagination.legacy_not_ready', {e.code for e in errors})

    def test_a_b_boundaries_match_and_feedback_returns_to_a(self):
        data, path = self.contract()
        b = data['page_briefs'][0]['page_brief']['b_section']
        b['pagination_ref']['owned_spans'] = [span(2)]
        errors, _ = validate_contract(data, path)
        self.assertIn('pagination.page_mapping', {e.code for e in errors})
        data, path = self.contract()
        b = data['page_briefs'][0]['page_brief']['b_section']
        b['pagination_feedback'] = [dict(feedback_id='f1', page_ids=['KP-01'], issue='density',
            requested_owner='B', status='pending')]
        errors, _ = validate_contract(data, path)
        self.assertIn('pagination.feedback_owner', {e.code for e in errors})
        self.assertIn('pagination.feedback_pending', {e.code for e in errors})


if __name__ == '__main__':
    unittest.main()
