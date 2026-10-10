# Example: SRT Index Companion Success

Input: short `.srt` sample.
Run: `build_srt_index.py input.srt --out-dir test_logs\srt_sample`
Result: timeline JSONL, timeline Markdown, and semi-manual SRT index are created.
Success reason: output preserves timecodes and source line IDs, and leaves S-route/A-line decisions for S-line review.
