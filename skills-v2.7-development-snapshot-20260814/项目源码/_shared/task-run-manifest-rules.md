# Task Run Manifest Rules

## Purpose
Record each V2.7 task so decisions, samples, reference images, and user confirmations do not drift across turns.

## Standard Manifest
```yaml
task_run_id:
created_at:
input_type:
source_material:
segment_time_metadata:
sline_result:
aline_result:
a_review_result:
bline_result:
tline_result:
cline_result:
reference_images:
inheritance_rules:
text_budget:
risk_score:
visual_sample_state: not_generated
user_gate_status:
revision_history:
final_user_decision:
```

## State Rules
The manifest must distinguish sample generation from user confirmation. Never set `visual_sample_state` to final automatically. Record every local revision with the `revision_contract` used.
