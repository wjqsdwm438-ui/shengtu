from __future__ import annotations

import json
import shutil
from pathlib import Path

from PIL import Image


PROJECT = Path(r"E:\remotion")
OUT = PROJECT / "out"
MANIFEST = PROJECT / "scripts" / "batch-manifest.json"


def frames(directory: Path) -> list[Path]:
    result = sorted(directory.glob("element-*.png"))
    if not result:
        raise RuntimeError(f"No rendered frames in {directory}")
    return result


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    transparent_frames = frames(OUT / "_ql-batch-transparent")
    checker_frames = frames(OUT / "_ql-batch-checkerboards")
    if len(transparent_frames) != len(manifest["transparent"]):
        raise RuntimeError("Transparent frame count does not match manifest")
    if len(checker_frames) != len(manifest["checkerboards"]):
        raise RuntimeError("Checkerboard frame count does not match manifest")

    for source, item in zip(transparent_frames, manifest["transparent"]):
        directory = OUT / item["page"].lower()
        directory.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, directory / item["filename"])

    for source, item in zip(checker_frames, manifest["checkerboards"]):
        directory = OUT / item["page"].lower()
        directory.mkdir(parents=True, exist_ok=True)
        target = directory / item["filename"]
        with Image.open(source) as image:
            image.convert("RGBA").save(target)

    print(
        f"archived transparent={len(transparent_frames)} "
        f"checkerboards={len(checker_frames)} pages={len(manifest['checkerboards'])}"
    )


if __name__ == "__main__":
    main()
