# Algorithm Companion Rules

The companion is evidence-only. It may run deterministic checks, but the calling V2.7 stage keeps responsibility for final judgment.

## Evidence Levels
- pass: script found no blocking issue.
- return: script found a missing field, over-budget text, or high risk that should return to the calling stage.
- manual-confirm: user Gate or frozen-item risk is likely.

## Logging
Write logs to `<项目根目录>\test_logs`. Logs must not claim final production status.
