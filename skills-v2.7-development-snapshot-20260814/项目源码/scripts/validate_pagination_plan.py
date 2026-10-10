#!/usr/bin/env python3
"""Read-only A pagination checks: source locations, coverage and recorded mapping.

No image calls, writes, content fingerprints, fixed page count or pedagogical
quality verdict. Source version/date and approval remain attributable records,
not independently authenticated facts. Boundary anchors do not detect every
interior edit: changed input/decisions require a new version and internal review.
"""
from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from datetime import date
import json
from pathlib import Path
from typing import Any

SCHEMA = 'course_visual_a_pagination/v1'
REVIEW_ITEMS = {'source_coverage', 'source_order', 'boundaries', 'capacity',
                'split_merge', 'non_a_retention'}


@dataclass(frozen=True)
class ContractError:
    code: str
    path: str
    message: str


def text_value(value):
    return isinstance(value, str) and bool(value.strip())


def positive_int(value):
    return type(value) is int and value > 0


def typed_equal(left, right):
    """JSON mapping equality must not accept True as the integer 1."""
    if type(left) is not type(right):
        return False
    if isinstance(left, dict):
        return left.keys() == right.keys() and all(typed_equal(left[k], right[k]) for k in left)
    if isinstance(left, list):
        return len(left) == len(right) and all(typed_equal(a, b) for a, b in zip(left, right))
    return left == right


def normalize(spans):
    """Merge adjacent intervals for comparison, without allocating per character."""
    groups = defaultdict(list)
    for source, line, start, end in spans:
        groups[(source, line)].append((start, end))
    result = {}
    for key, intervals in groups.items():
        merged = []
        for start, end in sorted(intervals):
            if merged and start <= merged[-1][1] + 1:
                merged[-1] = (merged[-1][0], max(end, merged[-1][1]))
            else:
                merged.append((start, end))
        result[key] = merged
    return result


def contained(spans, approved):
    return all(any(a <= start and end <= b for a, b in approved.get((source, line), []))
               for source, line, start, end in spans)


def overlaps(left, right):
    return any(any(start <= b and a <= end for a, b in right.get((source, line), []))
               for source, line, start, end in left)


def duplicate_coverage(spans):
    seen = defaultdict(list)
    for source, line, start, end in spans:
        if any(start <= b and a <= end for a, b in seen[(source, line)]):
            return True
        seen[(source, line)].append((start, end))
    return False


def validate_pagination_plan(data: Any, contract_path: Path):
    errors = []
    derived = dict(page_count=0, mechanical_validation_only=True, pedagogical_quality_verified=False,
                   source_versions_independently_verified=False, all_source_edits_detected=False)

    def add(code, path, message):
        errors.append(ContractError('pagination.' + code, path, message))

    def array(value, path, nonempty=False):
        if not isinstance(value, list) or (nonempty and not value):
            add('array', path, 'must be an array' + (' with at least one entry' if nonempty else ''))
            return []
        return value

    def fields(obj, names, path):
        for name in names:
            if not text_value(obj.get(name)):
                add('field', path + '.' + name, 'must be a non-empty recorded string, not proof of quality')

    if not isinstance(data, dict):
        add('required', '$.a_pagination_plan', 'A pagination plan object is required')
        return errors, derived
    if data.get('schema') != SCHEMA:
        add('schema', '$.schema', f'must be {SCHEMA!r}')
    fields(data, ('plan_id',), '$')
    if not positive_int(data.get('plan_version')):
        add('version', '$.plan_version', 'must be a positive integer')

    evidence = data.get('source_evidence')
    if not isinstance(evidence, dict):
        add('source_evidence', '$.source_evidence', 'independent source evidence object is required')
        evidence = {}
    approval = evidence.get('approval')
    if not isinstance(approval, dict) or approval.get('status') != 'confirmed' or not text_value(approval.get('record')):
        add('scope_approval', '$.source_evidence.approval', 'existing approved text scope/classification record required; not page or generation approval')
    sources = {}
    source_orders = []
    source_paths = set()
    for i, source in enumerate(array(evidence.get('sources'), '$.source_evidence.sources', True)):
        path = f'$.source_evidence.sources[{i}]'
        if not isinstance(source, dict):
            add('source', path, 'source must be an object')
            continue
        fields(source, ('source_id', 'path', 'version', 'version_date'), path)
        sid = source.get('source_id')
        if not text_value(sid):
            continue
        if sid in sources:
            add('source_duplicate', path, 'source_id must be unique')
            continue
        order = source.get('order')
        if not positive_int(order):
            add('source_order', path + '.order', 'source order must be a positive integer')
        else:
            source_orders.append(order)
        try:
            date.fromisoformat(source.get('version_date', ''))
        except (TypeError, ValueError):
            add('source_date', path + '.version_date', 'recorded version date must use YYYY-MM-DD')
        lines = []
        if text_value(source.get('path')):
            resolved = Path(source['path'])
            if not resolved.is_absolute():
                resolved = contract_path.parent / resolved
            try:
                resolved = resolved.resolve()
                if resolved in source_paths:
                    add('source_path_duplicate', path + '.path', 'same physical source cannot use two IDs')
                source_paths.add(resolved)
                with resolved.open('r', encoding='utf-8-sig', newline=None) as stream:
                    lines = stream.read().splitlines()
            except (OSError, UnicodeError, ValueError) as exc:
                add('source_unreadable', path + '.path', str(exc))
        sources[sid] = (order if positive_int(order) else i + 1, lines)
    if source_orders != list(range(1, len(sources) + 1)):
        add('source_order', '$.source_evidence.sources', 'sources must be listed in unique contiguous original order')

    def spans(value, path, nonempty=False):
        result = []
        for i, s in enumerate(array(value, path, nonempty)):
            here = f'{path}[{i}]'
            if not isinstance(s, dict):
                add('span', here, 'span must be an object')
                continue
            sid = s.get('source_id')
            coords = [s.get(k) for k in ('line', 'start_char', 'end_char')]
            if not text_value(sid) or sid not in sources:
                add('span_source', here, 'span must reference a known source_id')
                continue
            if not all(positive_int(c) for c in coords):
                add('span_type', here, 'line/start_char/end_char must be 1-based positive integers, not booleans')
                continue
            line, start, end = coords
            lines = sources[sid][1]
            if line > len(lines) or end < start or end > len(lines[line - 1]):
                add('span_bounds', here, 'span is outside actual source line bounds')
                continue
            selected = lines[line - 1][start - 1:end]
            if not text_value(s.get('start_text')) or not text_value(s.get('end_text')):
                add('span_anchor', here, 'literal non-empty start_text and end_text anchors required')
            elif not selected.startswith(s['start_text']) or not selected.endswith(s['end_text']):
                add('anchor_mismatch', here, 'literal boundary anchors do not match actual source')
            result.append((sid, line, start, end))
        return result

    approved = spans(evidence.get('approved_body_spans'), '$.source_evidence.approved_body_spans', True)
    annotations = spans(evidence.get('annotation_spans'), '$.source_evidence.annotation_spans')
    approved_map, annotation_map = normalize(approved), normalize(annotations)
    if duplicate_coverage(approved) or duplicate_coverage(annotations):
        add('scope_overlap', '$.source_evidence', 'approved scope/classification entries must not duplicate each other')
    if overlaps(approved, annotation_map):
        add('scope_annotation_overlap', '$.source_evidence', 'annotations cannot be approved body ownership')

    all_owned, page_owned, page_records, references = [], {}, [], {'source:' + sid for sid in sources}
    original_positions = []
    page_contexts = []
    page_ids = []
    for i, page in enumerate(array(data.get('pages'), '$.pages', True)):
        path = f'$.pages[{i}]'
        if not isinstance(page, dict):
            add('page', path, 'page must be an object')
            continue
        pid = page.get('page_id')
        if not text_value(pid) or pid in page_owned:
            add('page_id', path, 'page_id must be a unique non-empty string assigned by A')
            continue
        page_ids.append(pid)
        references.add('page:' + pid)
        if type(page.get('order')) is not int or page.get('order') != i + 1:
            add('page_order', path + '.order', 'pages must follow contiguous final original-source order')
        owned = spans(page.get('owned_spans'), path + '.owned_spans', True)
        contexts = spans(page.get('context_refs'), path + '.context_refs')
        page_contexts.append((path + '.context_refs', contexts))
        all_owned.extend(owned)
        page_owned[pid] = owned
        page_records.append(dict(page_id=pid, owned_spans=page.get('owned_spans')))
        original_positions.extend((sources[sid][0], line, start, end) for sid, line, start, end in owned)
        capacity = page.get('capacity_basis')
        if not isinstance(capacity, dict):
            add('capacity', path + '.capacity_basis', 'actual carrying-basis record required')
            capacity = {}
        fields(capacity, ('teaching_task', 'asset_applicability_reason', 'same_screen_reason',
                         'cross_page_reason', 'visual_carrier_feasibility', 'unverified_limits'), path + '.capacity_basis')
        labels = array(capacity.get('required_text_and_labels'), path + '.capacity_basis.required_text_and_labels')
        if not all(text_value(label) for label in labels):
            add('capacity_text', path, 'required_text_and_labels entries must be literal strings')
        assets = array(capacity.get('approved_assets'), path + '.capacity_basis.approved_assets')
        for n, asset in enumerate(assets):
            ap = f'{path}.capacity_basis.approved_assets[{n}]'
            if not isinstance(asset, dict):
                add('capacity_asset', ap, 'asset must be an object')
                continue
            fields(asset, ('path', 'approval_record', 'usable_space_and_limits'), ap)
            if text_value(asset.get('path')):
                resolved = Path(asset['path'])
                if not resolved.is_absolute():
                    resolved = contract_path.parent / resolved
                try:
                    with resolved.open('rb') as stream:
                        stream.read(1)
                except (OSError, ValueError) as exc:
                    add('capacity_asset_missing', ap + '.path', str(exc))
    if original_positions != sorted(original_positions):
        add('source_order', '$.pages', 'page-owned body must retain original source ordering, including splits and merges')

    # Context can preview later A-owned body as well as recall earlier body.
    # Collect all A ownership first, but before adding Non-A dispositions.
    # This does not authenticate the stated teaching purpose or visual order.
    a_owned_map = normalize(all_owned)
    for path, contexts in page_contexts:
        if (not contained(contexts, a_owned_map) or not contained(contexts, approved_map)
                or overlaps(contexts, annotation_map)):
            add('context_not_a_owned', path,
                'context refs must refer to approved body owned by A pages, not Non-A or annotations; forward preview/backreference adds no coverage')

    for i, disposition in enumerate(array(data.get('non_a_dispositions'), '$.non_a_dispositions')):
        path = f'$.non_a_dispositions[{i}]'
        if not isinstance(disposition, dict):
            add('non_a', path, 'Non-A disposition must be an object; it does not delete source body')
            continue
        fields(disposition, ('disposition_id', 'reason', 'target'), path)
        did = disposition.get('disposition_id')
        if text_value(did):
            if 'non_a:' + did in references:
                add('non_a_duplicate', path, 'disposition_id must be unique')
            references.add('non_a:' + did)
        all_owned.extend(spans(disposition.get('owned_spans'), path + '.owned_spans', True))
    if duplicate_coverage(all_owned):
        add('coverage_overlap', '$', 'body spans must be owned exactly once across A pages and Non-A dispositions')
    if overlaps(all_owned, annotation_map):
        add('annotation_owned', '$', 'annotation text cannot be owned as body')
    if not contained(all_owned, approved_map):
        add('coverage_outside_scope', '$', 'ownership is outside approved body scope')
    if not contained(approved, normalize(all_owned)):
        add('coverage_missing', '$', 'approved body is omitted; context refs never replace ownership')

    for i, comparison in enumerate(array(data.get('split_merge_comparisons'), '$.split_merge_comparisons', True)):
        path = f'$.split_merge_comparisons[{i}]'
        if not isinstance(comparison, dict):
            add('comparison', path, 'comparison must be an object')
            continue
        fields(comparison, ('comparison_id', 'decision_reason'), path)
        cid = comparison.get('comparison_id')
        if text_value(cid):
            if 'comparison:' + cid in references:
                add('comparison_duplicate', path, 'comparison_id must be unique')
            references.add('comparison:' + cid)
        selected = array(comparison.get('selected_page_ids'), path + '.selected_page_ids', True)
        if not all(text_value(pid) and pid in page_owned for pid in selected) or len(set(p for p in selected if isinstance(p, str))) != len(selected):
            add('comparison_pages', path, 'selected_page_ids must reference unique final pages')
            selected = [pid for pid in selected if text_value(pid) and pid in page_owned]
        if selected != [pid for pid in page_ids if pid in selected]:
            add('comparison_order', path, 'selected_page_ids must follow final original-source page order')
        selected_owned = [span for pid in selected for span in page_owned[pid]]
        compared = spans(comparison.get('source_spans'), path + '.source_spans', True)
        if normalize(compared) != normalize(selected_owned) or duplicate_coverage(compared):
            add('comparison_mapping', path, 'comparison source spans must exactly map its selected pages')
        candidates = set()
        alternatives = array(comparison.get('alternatives'), path + '.alternatives')
        different_alternative = False
        if not alternatives and not text_value(comparison.get('no_reasonable_alternative_reason')):
            add('comparison_no_alternative', path, 'record why no reasonable alternative was found; do not invent a candidate count')
        for n, alt in enumerate(alternatives):
            if not isinstance(alt, dict):
                add('comparison_alternative', path, 'alternative must be an object')
                continue
            fields(alt, ('candidate_id', 'reason'), f'{path}.alternatives[{n}]')
            if text_value(alt.get('candidate_id')):
                if alt['candidate_id'] in candidates:
                    add('comparison_alternative', path, 'candidate IDs must be unique within comparison')
                candidates.add(alt['candidate_id'])
            groups = array(alt.get('proposed_page_spans'), f'{path}.alternatives[{n}].proposed_page_spans', True)
            alternative_owned = []
            normalized_groups = []
            for gi, group in enumerate(groups):
                group_spans = spans(group, f'{path}.alternatives[{n}].proposed_page_spans[{gi}]', True)
                alternative_owned.extend(group_spans)
                normalized_groups.append(normalize(group_spans))
            if normalized_groups != [normalize(page_owned[pid]) for pid in selected]:
                different_alternative = True
            if normalize(alternative_owned) != normalize(compared) or duplicate_coverage(alternative_owned):
                add('comparison_alternative_mapping', path, 'specific alternative grouping must exactly cover this comparison scope without duplicate ownership')
            positions = [(sources[sid][0], line, start, end) for sid, line, start, end in alternative_owned]
            if positions != sorted(positions):
                add('comparison_alternative_order', path, 'alternative page grouping must preserve original source order')
        if alternatives and not different_alternative and not text_value(comparison.get('no_reasonable_alternative_reason')):
            add('comparison_unchanged_alternatives', path, 'copies of current boundaries are not alternatives; record an actual difference or why no reasonable alternative exists')

    review = data.get('internal_review')
    if not isinstance(review, dict):
        add('internal_review', '$.internal_review', 'current A internal review required; old S/A_review or nine-unit pass is not readiness')
        review = {}
    if review.get('plan_id') != data.get('plan_id') or not positive_int(review.get('plan_version')) or review.get('plan_version') != data.get('plan_version'):
        add('review_version', '$.internal_review', 'review must name this plan and exact version')
    if not typed_equal(review.get('reviewed_page_spans'), page_records):
        add('review_boundaries', '$.internal_review.reviewed_page_spans', 'review must record the entire current final page-to-source mapping')
    if review.get('status') != 'completed' or review.get('unresolved_issues') != []:
        add('review_incomplete', '$.internal_review', 'completed internal review with no unresolved issues required')
    items = []
    for i, check in enumerate(array(review.get('checks'), '$.internal_review.checks', True)):
        path = f'$.internal_review.checks[{i}]'
        if not isinstance(check, dict):
            add('review_check', path, 'check must be an object')
            continue
        item = check.get('item')
        if not text_value(item) or item not in REVIEW_ITEMS or check.get('result') != 'pass':
            add('review_check', path, 'known review item with recorded pass required')
        else:
            items.append(item)
        refs = array(check.get('evidence_refs'), path + '.evidence_refs', True)
        if not all(text_value(ref) and ref in references for ref in refs):
            add('review_reference', path, 'review references must resolve to source:/page:/comparison:/non_a: IDs in this plan, not prior pass logs')
    if set(items) != REVIEW_ITEMS or len(items) != len(REVIEW_ITEMS):
        add('review_checks', '$.internal_review.checks', 'exactly one record for each of the six review items required')
    derived.update(page_count=len(page_ids), page_ids=page_ids, non_a_count=len([r for r in references if r.startswith('non_a:')]))
    return errors, derived


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input_json', type=Path)
    args = parser.parse_args()
    try:
        data = json.loads(args.input_json.read_text(encoding='utf-8-sig'))
        if isinstance(data, dict) and 'a_pagination_plan' in data:
            data = data['a_pagination_plan']
        errors, derived = validate_pagination_plan(data, args.input_json)
    except (OSError, UnicodeError, ValueError) as exc:
        errors, derived = [ContractError('input.invalid', '$', str(exc))], {}
    print(json.dumps(dict(check='a_pagination_plan', **{'pass': not errors}, error_count=len(errors),
                          errors=[e.__dict__ for e in errors], derived=derived), ensure_ascii=False, indent=2))
    return 2 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
