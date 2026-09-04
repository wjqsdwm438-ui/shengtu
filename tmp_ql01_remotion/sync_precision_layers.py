from __future__ import annotations

import shutil
from pathlib import Path


SOURCE = Path(r"E:\remotion\out")
TARGET = Path(r"E:\shengtu\智能物流\生图输出\2成品")
BACKUP = Path(r"E:\remotion\out\_backup_before_object_aware_sync")


def main() -> None:
    copied = 0
    removed = 0
    backed_up = 0
    for page_num in range(1, 24):
        page = f"QL-{page_num:02d}"
        source_dir = SOURCE / ("ql-01-pilot" if page_num == 1 else page.lower())
        target_dir = TARGET / page
        backup_dir = BACKUP / page
        target_dir.mkdir(parents=True, exist_ok=True)
        backup_dir.mkdir(parents=True, exist_ok=True)

        expected = {
            path.name: path
            for path in source_dir.glob("*.png")
            if "羽化棋盘审核图" not in path.name
        }
        if not expected:
            raise RuntimeError(f"No precision outputs for {page}")

        final_files = list(target_dir.glob("*最终合成版.png"))
        if len(final_files) != 1:
            raise RuntimeError(f"Expected exactly one final composite for {page}")

        for old in target_dir.glob("*.png"):
            if "最终合成版" in old.name:
                continue
            shutil.copy2(old, backup_dir / old.name)
            backed_up += 1
            old.unlink()
            removed += 1

        for name, source_path in expected.items():
            shutil.copy2(source_path, target_dir / name)
            copied += 1

        actual = {path.name for path in target_dir.glob("*.png") if "最终合成版" not in path.name}
        if actual != set(expected):
            raise RuntimeError(f"Post-sync mismatch for {page}: {actual ^ set(expected)}")

    print(f"SYNC_PASS pages=23 copied={copied} removed={removed} backed_up={backed_up}")


if __name__ == "__main__":
    main()
