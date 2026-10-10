#!/usr/bin/env python3
"""Fail-closed validator for the shared A/B/C page-brief contract.

The checker intentionally validates only stable execution invariants.  It does
not score visual quality, choose a batch count, or infer a design when the
contract is incomplete.  Only the Python standard library is required.
"""
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from validate_pagination_plan import typed_equal, validate_pagination_plan


EXPECTED_STAGES = ["A", "B", "C_adapter", "C_generate", "assembly"]
FORBIDDEN_BATCH_COUNT_KEYS = {"batch_count", "fixed_batch_count", "planned_batch_count"}
FORBIDDEN_IMAGE_SHARE_KEYS = {
    "fixed_image_ratio",
    "image_area_percentage",
    "image_area_ratio",
    "image_coverage",
    "image_percentage",
    "image_ratio_range",
    "image_share",
    "recommended_image_ratio",
    "visual_area_ratio",
    "visual_percentage",
    "图片占比",
    "图像占比",
    "主视觉占比",
    "图像面积比例",
}
INDEPENDENT_T_STAGE = re.compile(
    r"^(?:t|t[-_ ]?line|t线|stage-tline-prompt-translation)$", re.IGNORECASE
)
MECHANICAL_IMAGE_SHARE = re.compile(
    r"(?:图片|图像|主视觉|image|visual).{0,24}(?:占比|面积比例|share|coverage|percentage)"
    r".{0,16}\d+(?:\.\d+)?\s*%",
    re.IGNORECASE,
)


@dataclass(frozen=True)
class ContractError:
    code: str
    path: str
    message: str


def is_present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple)):
        return bool(value)
    return True


def walk(value: Any, path: str = "$"):
    """Yield ``(path, key, value)`` for every mapping member recursively."""
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}"
            yield child_path, str(key), child
            yield from walk(child, child_path)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from walk(child, f"{path}[{index}]")


def resolve_asset(contract_path: Path, raw_path: str) -> Path:
    path = Path(raw_path)
    if not path.is_absolute():
        path = contract_path.parent / path
    return path


def validate_contract(data: Any, contract_path: Path) -> tuple[list[ContractError], dict[str, Any]]:
    errors: list[ContractError] = []

    def add(code: str, path: str, message: str) -> None:
        errors.append(ContractError(code, path, message))

    if not isinstance(data, dict):
        add("schema.root", "$", "contract root must be an object")
        return errors, {"page_count": 0, "batch_count": 0}
    if data.get("schema") != "course_visual_page_brief/v2.7":
        add(
            "schema.version",
            "$.schema",
            "schema must be 'course_visual_page_brief/v2.7'",
        )

    workflow = data.get("workflow")
    if not isinstance(workflow, dict):
        add("workflow.required", "$.workflow", "workflow must be an object")
        workflow = {}

    stages = workflow.get("stages")
    if stages != EXPECTED_STAGES:
        add(
            "workflow.stages",
            "$.workflow.stages",
            f"stages must be exactly {EXPECTED_STAGES!r}; independent T is forbidden",
        )
    if isinstance(stages, list):
        for index, stage in enumerate(stages):
            if isinstance(stage, str) and INDEPENDENT_T_STAGE.fullmatch(stage.strip()):
                add(
                    "workflow.independent_t",
                    f"$.workflow.stages[{index}]",
                    "independent T stage/call is forbidden; use C_adapter",
                )
    if workflow.get("batch_count_policy") != "derived_from_pages":
        add(
            "batch.dynamic",
            "$.workflow.batch_count_policy",
            "batch_count_policy must be 'derived_from_pages'",
        )
    if workflow.get("production_order_policy") != "by_batch":
        add(
            "batch.production_order",
            "$.workflow.production_order_policy",
            "production_order_policy must be 'by_batch'",
        )
    if workflow.get("assembly_order_policy") != "original_page_order":
        add(
            "page.assembly_policy",
            "$.workflow.assembly_order_policy",
            "assembly_order_policy must be 'original_page_order'",
        )

    pagination = data.get("a_pagination_plan")
    if not isinstance(pagination, dict):
        add("pagination.legacy_not_ready", "$.a_pagination_plan",
            "旧合同不就绪：旧 s_section/a_review_status 或9单元通过记录不能替代本轮 A 分页与内部复核。")
        pagination = {}
    pagination_errors, pagination_derived = validate_pagination_plan(pagination, contract_path)
    errors.extend(ContractError(e.code, "$.a_pagination_plan" + e.path[1:], e.message)
                  for e in pagination_errors)
    planned_pages_raw = pagination.get("pages")
    planned_pages = {p["page_id"]: p for p in planned_pages_raw
                     if isinstance(p, dict) and isinstance(p.get("page_id"), str)} if isinstance(planned_pages_raw, list) else {}

    for item_path, key, value in walk(data):
        normalized_key = key.strip().lower()
        if normalized_key in FORBIDDEN_BATCH_COUNT_KEYS:
            add("batch.fixed_count", item_path, "batch count must be derived, not declared")
        if normalized_key in FORBIDDEN_IMAGE_SHARE_KEYS:
            add("image.fixed_share", item_path, "fixed image-area share fields are forbidden")
        if INDEPENDENT_T_STAGE.fullmatch(normalized_key) or (
            isinstance(value, str) and INDEPENDENT_T_STAGE.fullmatch(value.strip())
        ):
            add("workflow.independent_t", item_path, "independent T stage/call is forbidden")
        if isinstance(value, str) and MECHANICAL_IMAGE_SHARE.search(value):
            add("image.fixed_share", item_path, "mechanical image-area percentage rule is forbidden")

    batches_raw = data.get("batches")
    pages_raw = data.get("page_briefs")
    if not isinstance(batches_raw, list) or not batches_raw:
        add("batch.required", "$.batches", "batches must be a non-empty array")
        batches_raw = []
    if not isinstance(pages_raw, list) or not pages_raw:
        add("page.required", "$.page_briefs", "page_briefs must be a non-empty array")
        pages_raw = []

    batches: dict[str, dict[str, Any]] = {}
    for index, batch in enumerate(batches_raw):
        path = f"$.batches[{index}]"
        if not isinstance(batch, dict):
            add("batch.object", path, "batch must be an object")
            continue
        batch_id = batch.get("batch_id")
        if not is_present(batch_id):
            add("batch.id", f"{path}.batch_id", "batch_id is required")
            continue
        batch_id = str(batch_id)
        if batch_id in batches:
            add("batch.duplicate", f"{path}.batch_id", f"duplicate batch_id {batch_id!r}")
        else:
            batches[batch_id] = batch
        for field in (
            "outer_template",
            "teaching_relation",
            "semantic_visual_carrier",
            "shared_reference_and_generation_basis",
            "representative_page_id",
            "representative_reason",
            "representative_status",
        ):
            if not is_present(batch.get(field)):
                add("batch.field", f"{path}.{field}", f"{field} is required")

    pages: dict[str, dict[str, Any]] = {}
    order_values: dict[int, str] = {}
    for index, wrapper in enumerate(pages_raw):
        wrapper_path = f"$.page_briefs[{index}]"
        if not isinstance(wrapper, dict) or not isinstance(wrapper.get("page_brief"), dict):
            add("page.object", wrapper_path, "entry must contain a page_brief object")
            continue
        page = wrapper["page_brief"]
        path = f"{wrapper_path}.page_brief"
        page_id = page.get("page_id")
        if not is_present(page_id):
            add("page.id", f"{path}.page_id", "page_id is required")
            continue
        page_id = str(page_id)
        if page_id in pages:
            add("page.duplicate", f"{path}.page_id", f"duplicate page_id {page_id!r}")
        else:
            pages[page_id] = page

        order = page.get("original_course_order")
        if not isinstance(order, int) or isinstance(order, bool) or order < 1:
            add(
                "page.original_order",
                f"{path}.original_course_order",
                "original_course_order must be a positive integer",
            )
        elif order in order_values:
            add(
                "page.original_order_duplicate",
                f"{path}.original_course_order",
                f"order {order} is already used by {order_values[order]!r}",
            )
        else:
            order_values[order] = page_id

        batch_id = page.get("batch_id")
        if batch_id not in batches:
            add("page.batch", f"{path}.batch_id", f"unknown batch_id {batch_id!r}")

        a_section = page.get("a_section")
        if not isinstance(a_section, dict):
            add("a.required", f"{path}.a_section", "a_section must be an object")
            a_section = {}
        for field in (
            "teaching_goal",
            "teaching_relation",
            "must_show_items",
            "image_pedagogical_task",
            "forbidden_semantic_drift",
        ):
            if not is_present(a_section.get(field)):
                add("a.field", f"{path}.a_section.{field}", f"{field} is required")
        teaching_relation = a_section.get("teaching_relation")
        relation_kind = teaching_relation.get("relation_kind") if isinstance(teaching_relation, dict) else None
        if not is_present(relation_kind):
            add("a.relation_kind", f"{path}.a_section.teaching_relation.relation_kind", "relation_kind is required")

        b_section = page.get("b_section")
        if not isinstance(b_section, dict):
            add("b.required", f"{path}.b_section", "B section must be an object")
            b_section = {}
        planned_page = planned_pages.get(page_id)
        if planned_page is None:
            add("pagination.page_mapping", path, "page is not present in the current A pagination plan")
        else:
            expected_ref = {"plan_id": pagination.get("plan_id"), "plan_version": pagination.get("plan_version"),
                            "page_id": page_id, "owned_spans": planned_page.get("owned_spans")}
            for section_name, section in (("a_section", a_section), ("b_section", b_section)):
                if not typed_equal(section.get("pagination_ref"), expected_ref):
                    add("pagination.page_mapping", f"{path}.{section_name}.pagination_ref",
                        "A/B must reference this exact current plan version and page source boundaries; B cannot repaginate")
            if page.get("original_course_order") != planned_page.get("order"):
                add("pagination.page_mapping", path + ".original_course_order", "page order must match A pagination")
        feedback = b_section.get("pagination_feedback")
        if not isinstance(feedback, list):
            add("pagination.feedback", path + ".b_section.pagination_feedback", "must be an array; use [] for no local feedback")
            feedback = []
        feedback_ids = set()
        for fi, item in enumerate(feedback):
            fp = f"{path}.b_section.pagination_feedback[{fi}]"
            if not isinstance(item, dict):
                add("pagination.feedback", fp, "feedback must be a recorded object")
                continue
            feedback_id = item.get("feedback_id")
            if not isinstance(feedback_id, str) or not feedback_id.strip() or feedback_id in feedback_ids:
                add("pagination.feedback", fp, "feedback_id must be a unique non-empty string")
            else:
                feedback_ids.add(feedback_id)
            issue = item.get("issue")
            if not isinstance(issue, str) or not issue.strip():
                add("pagination.feedback", fp, "concrete local issue evidence is required")
            affected = item.get("page_ids")
            if not isinstance(affected, list) or not affected or not all(isinstance(pid, str) and pid in planned_pages for pid in affected):
                add("pagination.feedback", fp, "feedback must name affected current pages")
            if item.get("requested_owner") != "A":
                add("pagination.feedback_owner", fp, "pagination/capacity feedback returns locally to A, never creates B-owned page boundaries")
            if item.get("status") != "resolved_by_A":
                add("pagination.feedback_pending", fp, "unresolved pagination feedback blocks B/C readiness")
            elif type(item.get("resolution_plan_version")) is not int or item.get("resolution_plan_version") != pagination.get("plan_version"):
                add("pagination.feedback_version", fp, "resolution must refer to the current A plan version")
        evidence = b_section.get("implementation_evidence")
        if not isinstance(evidence, dict):
            add("b.evidence", f"{path}.b_section.implementation_evidence", "implementation_evidence must be an object")
            evidence = {}
        else:
            for field in ("what_it_proves", "what_it_does_not_prove", "highest_risk"):
                if not is_present(evidence.get(field)):
                    add("b.evidence_field", f"{path}.b_section.implementation_evidence.{field}", f"{field} is required")
            evidence_assets = evidence.get("asset_used")
            if not isinstance(evidence_assets, list) or not evidence_assets:
                add(
                    "b.evidence_asset",
                    f"{path}.b_section.implementation_evidence.asset_used",
                    "asset_used must be a non-empty array of implementation-evidence objects",
                )
                evidence_assets = []
            for asset_index, asset in enumerate(evidence_assets):
                asset_path = f"{path}.b_section.implementation_evidence.asset_used[{asset_index}]"
                if not isinstance(asset, dict):
                    add("b.evidence_asset", asset_path, "implementation evidence must be an object")
                    continue
                for field in (
                    "reference_id",
                    "real_path",
                    "file_name",
                    "dimensions",
                    "template_version",
                    "reference_role",
                    "user_confirmation",
                ):
                    if not is_present(asset.get(field)):
                        add("b.evidence_asset_field", f"{asset_path}.{field}", f"{field} is required")
                raw_asset = asset.get("real_path")
                if isinstance(raw_asset, str) and raw_asset.strip():
                    resolved = resolve_asset(contract_path, raw_asset)
                    if not resolved.is_file():
                        add("b.evidence_asset_missing", f"{asset_path}.real_path", f"asset does not exist: {resolved}")
            if evidence.get("representative_calibration_required") not in {"yes", "no"}:
                add(
                    "b.evidence_field",
                    f"{path}.b_section.implementation_evidence.representative_calibration_required",
                    "representative_calibration_required must be 'yes' or 'no'",
                )

        plan = b_section.get("main_execution_plan")
        if not isinstance(plan, dict):
            add("b.main_plan", f"{path}.b_section.main_execution_plan", "main_execution_plan must be an object")
            plan = {}
        for field in ("plan_id", "semantic_visual_carrier", "main_visual_description", "reading_order", "reference_mapping", "must_show_text_verbatim"):
            if not is_present(plan.get(field)):
                add("b.main_plan_field", f"{path}.b_section.main_execution_plan.{field}", f"{field} is required")
        outer_template = plan.get("outer_template")
        if not isinstance(outer_template, dict):
            add("b.outer_template", f"{path}.b_section.main_execution_plan.outer_template", "outer_template must be an object")
            outer_template = {}
        for field in ("identity", "description", "evidence_reference_id"):
            if not is_present(outer_template.get(field)):
                add("b.outer_template_field", f"{path}.b_section.main_execution_plan.outer_template.{field}", f"{field} is required")

        assignment = b_section.get("batch_assignment")
        if not isinstance(assignment, dict):
            add("b.batch_assignment", f"{path}.b_section.batch_assignment", "batch_assignment must be an object")
            assignment = {}
        for field in (
            "batch_id",
            "member_original_course_orders",
            "shared_outer_template_basis",
            "shared_teaching_relation_basis",
            "shared_semantic_visual_carrier_basis",
            "shared_reference_and_generation_basis",
            "representative_page",
            "representative_selection_reason",
        ):
            if not is_present(assignment.get(field)):
                add("b.batch_field", f"{path}.b_section.batch_assignment.{field}", f"{field} is required")
        for field, expected in (
            ("independent_C_context_required", "yes"),
            ("include_other_batches_context", "no"),
            ("include_previous_page_output_by_default", "no"),
            ("final_assembly_order", "use_original_course_order"),
        ):
            if assignment.get(field) != expected:
                add("b.batch_isolation", f"{path}.b_section.batch_assignment.{field}", f"{field} must be {expected!r}")

        calibration = b_section.get("batch_calibration")
        if not isinstance(calibration, dict):
            add("b.batch_calibration", f"{path}.b_section.batch_calibration", "batch_calibration must be an object")
            calibration = {}
        handoff = b_section.get("C_adapter_handoff")
        if not isinstance(handoff, dict):
            add("b.c_handoff", f"{path}.b_section.C_adapter_handoff", "C_adapter_handoff must be an object")
            handoff = {}

        c_section = page.get("c_section")
        if not isinstance(c_section, dict):
            add("c.required", f"{path}.c_section", "C section must be an object")
            c_section = {}
        preflight = c_section.get("adapter_preflight")
        if not isinstance(preflight, dict):
            add("c.preflight", f"{path}.c_section.adapter_preflight", "adapter_preflight must be an object")
            preflight = {}
        required_yes = (
            "source_evidence_complete",
            "A_internal_review_complete",
            "a_pagination_plan_complete",
            "a_section_complete",
            "b_section_complete",
            "main_execution_plan_present",
            "concrete_canvas_size_present",
            "main_execution_plan_main_visual_description_present",
            "declared_assets_exist_and_readable",
            "unresolved_design_open_items_absent",
            "placeholders_or_truncated_sentences_absent",
            "contradictions_absent",
            "representative_gate_passed_or_calibration_exception_valid",
        )
        for field in required_yes:
            if preflight.get(field) != "yes":
                add("c.preflight_failed", f"{path}.c_section.adapter_preflight.{field}", f"{field} must be 'yes'")
        if preflight.get("result") != "pass":
            add("c.preflight_result", f"{path}.c_section.adapter_preflight.result", "preflight result must be 'pass'")
        preflight_template = preflight.get("main_execution_plan_outer_template")
        if not isinstance(preflight_template, dict):
            add(
                "c.preflight_template",
                f"{path}.c_section.adapter_preflight.main_execution_plan_outer_template",
                "main_execution_plan_outer_template must be an object",
            )
        else:
            for field in ("identity_present", "description_present", "evidence_reference_id_present"):
                if preflight_template.get(field) != "yes":
                    add("c.preflight_failed", f"{path}.c_section.adapter_preflight.main_execution_plan_outer_template.{field}", f"{field} must be 'yes'")

        preflight_evidence = preflight.get("implementation_evidence")
        if not isinstance(preflight_evidence, dict):
            add(
                "c.preflight_evidence",
                f"{path}.c_section.adapter_preflight.implementation_evidence",
                "implementation_evidence preflight must be an object",
            )
        else:
            for field in (
                "asset_used_complete",
                "excluded_assets_and_reason_checked",
                "what_it_proves_present",
                "what_it_does_not_prove_present",
                "highest_risk_present",
                "representative_calibration_required_present",
                "calibration_reason_checked",
                "calibration_covered_by_representative_page_checked",
            ):
                if preflight_evidence.get(field) not in {"yes", "not_applicable"}:
                    add("c.preflight_failed", f"{path}.c_section.adapter_preflight.implementation_evidence.{field}", f"{field} must be checked")

        preflight_calibration = preflight.get("source_batch_calibration")
        if not isinstance(preflight_calibration, dict):
            add(
                "c.preflight_calibration",
                f"{path}.c_section.adapter_preflight.source_batch_calibration",
                "source_batch_calibration preflight must be an object",
            )
        else:
            for field in ("state", "human_confirmation"):
                if preflight_calibration.get(field) != calibration.get(field):
                    add(
                        "c.preflight_source_mismatch",
                        f"{path}.c_section.adapter_preflight.source_batch_calibration.{field}",
                        f"{field} must match B batch_calibration",
                    )

        preflight_handoff = preflight.get("source_C_adapter_handoff")
        if not isinstance(preflight_handoff, dict):
            add(
                "c.preflight_handoff",
                f"{path}.c_section.adapter_preflight.source_C_adapter_handoff",
                "source_C_adapter_handoff preflight must be an object",
            )
        else:
            if preflight_handoff.get("readiness") != handoff.get("readiness"):
                add(
                    "c.preflight_source_mismatch",
                    f"{path}.c_section.adapter_preflight.source_C_adapter_handoff.readiness",
                    "readiness must match B C_adapter_handoff",
                )
            for field in (
                "selected_reference_paths_match",
                "preserve_items_present",
                "change_items_present",
                "unresolved_blockers_empty",
            ):
                if preflight_handoff.get(field) not in {"yes", "not_applicable"}:
                    add("c.preflight_failed", f"{path}.c_section.adapter_preflight.source_C_adapter_handoff.{field}", f"{field} must be checked")
        if preflight.get("reference_mapping_matches_attachments") not in {"yes", "not_applicable"}:
            add(
                "c.preflight_failed",
                f"{path}.c_section.adapter_preflight.reference_mapping_matches_attachments",
                "reference_mapping_matches_attachments must be checked",
            )

        compiled = c_section.get("compiled_execution_contract")
        if not isinstance(compiled, dict):
            add("c.compiled_contract", f"{path}.c_section.compiled_execution_contract", "compiled_execution_contract must be an object")
            compiled = {}
        template_identity = compiled.get("template_identity")
        if not isinstance(template_identity, dict):
            add("c.template_identity", f"{path}.c_section.compiled_execution_contract.template_identity", "template_identity must be an object")
            template_identity = {}
        for field in ("template_id", "template_version", "evidence_reference_id", "master_asset_path"):
            if not is_present(template_identity.get(field)):
                add(
                    "c.template_identity_field",
                    f"{path}.c_section.compiled_execution_contract.template_identity.{field}",
                    f"{field} is required",
                )
        page_task = compiled.get("page_task")
        if not isinstance(page_task, dict):
            add("c.page_task", f"{path}.c_section.compiled_execution_contract.page_task", "page_task must be an object")
            page_task = {}
        change_or_generate = compiled.get("change_or_generate")
        if not isinstance(change_or_generate, dict):
            add("c.change_or_generate", f"{path}.c_section.compiled_execution_contract.change_or_generate", "change_or_generate must be an object")
            change_or_generate = {}
        technical = compiled.get("technical_parameters")
        if not isinstance(technical, dict):
            add("c.technical_parameters", f"{path}.c_section.compiled_execution_contract.technical_parameters", "technical_parameters must be an object")
            technical = {}

        required_compiled_values = (
            ("template_identity.master_asset_path", template_identity.get("master_asset_path")),
            ("page_task.teaching_goal", page_task.get("teaching_goal")),
            ("page_task.teaching_relation", page_task.get("teaching_relation")),
            ("page_task.semantic_visual_carrier", page_task.get("semantic_visual_carrier")),
            ("change_or_generate.subject_and_content_boundary", change_or_generate.get("subject_and_content_boundary")),
            ("technical_parameters.size", technical.get("size")),
            ("preserve", compiled.get("preserve")),
            ("chinese_execution_prompt", compiled.get("chinese_execution_prompt")),
            ("chinese_negative_constraints", compiled.get("chinese_negative_constraints")),
            ("local_revision_boundary", compiled.get("local_revision_boundary")),
        )
        for field, value in required_compiled_values:
            if not is_present(value):
                add("c.required_field", f"{path}.c_section.compiled_execution_contract.{field}", f"{field} is required")

        compiled_mirrors = (
            (
                "page_task.teaching_goal",
                page_task.get("teaching_goal"),
                a_section.get("teaching_goal", {}).get("learner_outcome")
                if isinstance(a_section.get("teaching_goal"), dict)
                else a_section.get("teaching_goal"),
            ),
            ("page_task.teaching_relation", page_task.get("teaching_relation"), relation_kind),
            (
                "page_task.semantic_visual_carrier",
                page_task.get("semantic_visual_carrier"),
                plan.get("semantic_visual_carrier"),
            ),
            (
                "template_identity.evidence_reference_id",
                template_identity.get("evidence_reference_id"),
                outer_template.get("evidence_reference_id"),
            ),
            (
                "technical_parameters.size",
                technical.get("size"),
                plan.get("technical_output_spec", {}).get("dimensions")
                if isinstance(plan.get("technical_output_spec"), dict)
                else None,
            ),
        )
        for field, compiled_value, upstream_value in compiled_mirrors:
            if is_present(compiled_value) and is_present(upstream_value) and compiled_value != upstream_value:
                add(
                    "c.compile_mismatch",
                    f"{path}.c_section.compiled_execution_contract.{field}",
                    f"compiled value must match the upstream page brief: {upstream_value!r}",
                )

        asset_fields: list[tuple[str, Any]] = [
            (
                f"{path}.c_section.compiled_execution_contract.template_identity.master_asset_path",
                template_identity.get("master_asset_path"),
            )
        ]
        references = compiled.get("references", [])
        if not isinstance(references, list):
            add("c.references", f"{path}.c_section.compiled_execution_contract.references", "references must be an array")
            references = []
        for asset_index, reference in enumerate(references):
            reference_path = f"{path}.c_section.compiled_execution_contract.references[{asset_index}]"
            if not isinstance(reference, dict):
                add("c.reference", reference_path, "reference must be an object")
                continue
            for field in ("path", "role", "must_inherit", "must_not_inherit"):
                if not is_present(reference.get(field)):
                    add("c.reference_field", f"{reference_path}.{field}", f"{field} is required")
            if reference.get("exists_and_readable") != "yes" or reference.get("actually_attached") != "yes":
                add("c.reference_gate", reference_path, "reference must exist, be readable, and be actually attached")
            asset_fields.append((f"{reference_path}.path", reference.get("path")))
        for asset_path, raw_asset in asset_fields:
            if not isinstance(raw_asset, str) or not raw_asset.strip():
                continue  # Empty mandatory fields were reported above.
            resolved = resolve_asset(contract_path, raw_asset)
            if not resolved.is_file():
                add("c.asset_missing", asset_path, f"asset does not exist: {resolved}")

        b_inheritance = b_section.get("skeleton_inheritance")
        c_inheritance = c_section.get("skeleton_inheritance")
        if not isinstance(c_inheritance, dict):
            add("c.inheritance", f"{path}.c_section.skeleton_inheritance", "C skeleton_inheritance must be an object")
        elif isinstance(b_inheritance, dict):
            expected_decision = b_inheritance.get("decision")
            if c_inheritance.get("decision") != expected_decision:
                add("c.inheritance_mismatch", f"{path}.c_section.skeleton_inheritance.decision", "C must preserve B inheritance decision")
            if expected_decision == "inherit_local_skeleton":
                mirror = (
                    ("source_page_id", b_inheritance.get("source_page")),
                    ("same_teaching_relation_reason", b_inheritance.get("same_teaching_relation_reason")),
                    ("inherited_parts", b_inheritance.get("inherited_parts")),
                    ("required_changes", b_inheritance.get("required_changes")),
                )
                for field, expected in mirror:
                    if c_inheritance.get(field) != expected:
                        add("c.inheritance_mismatch", f"{path}.c_section.skeleton_inheritance.{field}", f"{field} must match B")
                if c_inheritance.get("evidence_complete") != "yes":
                    add("c.inheritance_incomplete", f"{path}.c_section.skeleton_inheritance.evidence_complete", "inheritance evidence must be complete")

        if not isinstance(c_section.get("release_ready"), bool):
            add("c.release_ready", f"{path}.c_section.release_ready", "release_ready must be boolean")

        batch = batches.get(str(batch_id))
        if batch is not None:
            comparable = (
                ("teaching_relation", relation_kind, batch.get("teaching_relation")),
                ("outer_template", outer_template.get("identity"), batch.get("outer_template")),
                (
                    "semantic_visual_carrier",
                    plan.get("semantic_visual_carrier"),
                    batch.get("semantic_visual_carrier"),
                ),
                (
                    "shared_reference_and_generation_basis",
                    assignment.get("shared_reference_and_generation_basis"),
                    batch.get("shared_reference_and_generation_basis"),
                ),
            )
            for field, page_value, batch_value in comparable:
                if is_present(page_value) and is_present(batch_value) and page_value != batch_value:
                    add(
                        "batch.incompatible_page",
                        path,
                        f"page {field} does not match its batch contract",
                    )
            if assignment.get("batch_id") != batch_id:
                add("b.batch_id", f"{path}.b_section.batch_assignment.batch_id", "batch assignment does not match page batch_id")
            if assignment.get("representative_page") != batch.get("representative_page_id"):
                add("b.representative_page", f"{path}.b_section.batch_assignment.representative_page", "representative page does not match batch")
            member_orders = assignment.get("member_original_course_orders")
            if isinstance(order, int) and (not isinstance(member_orders, list) or order not in member_orders):
                add("b.member_order", f"{path}.b_section.batch_assignment.member_original_course_orders", "page original order is missing from batch members")
            if c_section.get("release_ready") is True:
                is_representative = page_id == batch.get("representative_page_id")
                calibration_exception = is_representative and batch.get("representative_status") == "pending"
                if calibration_exception:
                    gate_ok = (
                        calibration.get("state") == "calibrating"
                        and calibration.get("human_confirmation") == "pending"
                        and handoff.get("readiness") == "ready_for_representative_calibration"
                        and preflight.get("entry_mode") == "representative_calibration"
                    )
                else:
                    gate_ok = (
                        batch.get("representative_status") == "confirmed"
                        and calibration.get("state") == "frozen_for_execution"
                        and calibration.get("human_confirmation") == "confirmed"
                        and handoff.get("readiness") == "ready_for_C"
                        and preflight.get("entry_mode") in {"batch_expansion", "single_page"}
                    )
                if not gate_ok:
                    add(
                        "batch.representative_unconfirmed",
                        f"{path}.b_section.batch_calibration",
                        "release requires the representative calibration exception or a frozen, human-confirmed batch",
                    )
                if handoff.get("unresolved_blockers") not in ([], "none", "not_applicable"):
                    add("b.unresolved_blockers", f"{path}.b_section.C_adapter_handoff.unresolved_blockers", "unresolved_blockers must be empty")

    for batch_id, batch in batches.items():
        representative_id = batch.get("representative_page_id")
        representative = pages.get(str(representative_id))
        path = f"$.batches[{batch_id!r}]"
        if representative is None:
            add("batch.representative", f"{path}.representative_page_id", "representative page does not exist")
            continue
        if representative.get("batch_id") != batch_id:
            add("batch.representative_batch", f"{path}.representative_page_id", "representative page belongs to another batch")
        if batch.get("representative_status") != "confirmed":
            for page_id, page in pages.items():
                if (
                    page.get("batch_id") == batch_id
                    and page_id != representative_id
                    and isinstance(page.get("c_section"), dict)
                    and page["c_section"].get("release_ready") is True
                ):
                    add(
                        "batch.representative_unconfirmed",
                        f"$.page_briefs[{page_id!r}].page_brief.c_section.release_ready",
                        "non-representative page cannot be released before representative confirmation",
                    )

    for page_id, page in pages.items():
        b_section = page.get("b_section") if isinstance(page.get("b_section"), dict) else {}
        inheritance = b_section.get("skeleton_inheritance", {"decision": "no_inheritance"})
        path = f"$.page_briefs[{page_id!r}].page_brief.b_section.skeleton_inheritance"
        if not isinstance(inheritance, dict):
            add("inheritance.object", path, "skeleton_inheritance must be an object")
            continue
        mode = inheritance.get("decision")
        if mode not in {"no_inheritance", "inherit_local_skeleton"}:
            add(
                "inheritance.mode",
                f"{path}.decision",
                "decision must be 'no_inheritance' or 'inherit_local_skeleton'",
            )
            continue
        if mode == "no_inheritance":
            continue
        for field in (
            "source_page",
            "same_teaching_relation_reason",
            "inherited_parts",
            "required_changes",
        ):
            if not is_present(inheritance.get(field)):
                add("inheritance.field", f"{path}.{field}", f"{field} is required when inheritance is enabled")
        source_id = inheritance.get("source_page")
        source = pages.get(str(source_id))
        if source is None:
            add("inheritance.source", f"{path}.source_page", "source page does not exist")
            continue
        if source.get("batch_id") != page.get("batch_id"):
            add("inheritance.cross_batch", f"{path}.source_page", "skeleton inheritance must stay within one batch")
        source_a = source.get("a_section") if isinstance(source.get("a_section"), dict) else {}
        target_a = page.get("a_section") if isinstance(page.get("a_section"), dict) else {}
        source_relation = source_a.get("teaching_relation") if isinstance(source_a.get("teaching_relation"), dict) else {}
        target_relation = target_a.get("teaching_relation") if isinstance(target_a.get("teaching_relation"), dict) else {}
        if source_relation.get("relation_kind") != target_relation.get("relation_kind"):
            add(
                "inheritance.teaching_relation",
                path,
                "source and target teaching_relation must be identical; visual similarity is insufficient",
            )
        source_b = source.get("b_section") if isinstance(source.get("b_section"), dict) else {}
        source_plan = source_b.get("main_execution_plan") if isinstance(source_b.get("main_execution_plan"), dict) else {}
        target_plan = b_section.get("main_execution_plan") if isinstance(b_section.get("main_execution_plan"), dict) else {}
        if source_plan.get("semantic_visual_carrier") != target_plan.get("semantic_visual_carrier"):
            add(
                "inheritance.semantic_carrier",
                path,
                "source and target semantic_visual_carrier must be identical",
            )

    expected_assembly = [page_id for _, page_id in sorted(order_values.items())]
    if set(pages) != set(planned_pages):
        add("pagination.page_set", "$.page_briefs", "A final pages and B/C page briefs must correspond exactly")
    assembly_order = data.get("assembly_order")
    if assembly_order != expected_assembly or len(expected_assembly) != len(pages_raw):
        add(
            "page.assembly_order",
            "$.assembly_order",
            f"assembly_order must exactly follow original_course_order: {expected_assembly!r}",
        )

    derived = {
        "page_count": len(pages),
        "batch_count": len(batches),
        "assembly_order": expected_assembly,
        "mechanical_validation_only": True,
        "pedagogical_quality_verified": False,
        "pagination": pagination_derived,
    }
    return errors, derived


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a shared A/B/C page-brief and A pagination contract.")
    parser.add_argument("input_json", type=Path)
    args = parser.parse_args()

    try:
        data = json.loads(args.input_json.read_text(encoding="utf-8-sig"))
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        result = {
            "check": "page_brief_contract",
            "pass": False,
            "error_count": 1,
            "errors": [{"code": "input.invalid", "path": "$", "message": str(exc)}],
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 2

    # Keep relative input paths relative.  Besides producing shorter evidence,
    # this avoids leaking host-specific absolute paths into checked-in logs.
    errors, derived = validate_contract(data, args.input_json)
    result = {
        "check": "page_brief_contract",
        "pass": not errors,
        "error_count": len(errors),
        "errors": [error.__dict__ for error in errors],
        "derived": derived,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 2


if __name__ == "__main__":
    raise SystemExit(main())
