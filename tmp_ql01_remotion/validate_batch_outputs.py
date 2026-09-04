from __future__ import annotations

import hashlib
import json
from pathlib import Path

import numpy as np
from PIL import Image


PROJECT = Path(r"E:\remotion")
OUT = PROJECT / "out"
SOURCE_ROOT = Path(r"E:\shengtu\智能物流\生图输出\2成品")
MANIFEST = PROJECT / "scripts" / "batch-manifest.json"

BOTTOM_START = {"QL-04": 972, "QL-20": 1005}
TITLE_END = {"QL-02": 180, "QL-04": 195}
CUSTOM_COMBINED = {
    "QL-02": [
        (130, 220, 790, 725, 18),
        (130, 180, 420, 80, 18),
        (940, 275, 850, 390, 18),
        (940, 690, 830, 120, 18),
    ],
    "QL-03": [
        (145, 275, 1645, 535, 18),
        (285, 850, 1350, 105, 2),
    ],
    "QL-04": [
        (165, 195, 1590, 775, 10),
    ],
    "QL-05": [(180, 210, 1595, 745, 10)],
    "QL-08": [(170, 215, 1580, 720, 10)],
    "QL-09": [(155, 220, 1600, 735, 2)],
    "QL-10": [(160, 210, 1605, 740, 10)],
    "QL-13": [(190, 245, 1560, 700, 10)],
    "QL-14": [(155, 210, 1605, 730, 10)],
    "QL-15": [(155, 200, 1595, 755, 2)],
    "QL-17": [(180, 220, 1535, 690, 18)],
    "QL-18": [(180, 220, 1540, 715, 10)],
    "QL-19": [(155, 210, 1605, 720, 10)],
    "QL-20": [(145, 210, 1630, 775, 10)],
    "QL-21": [(180, 225, 1660, 710, 18)],
    "QL-22": [(165, 210, 1600, 740, 10)],
    "QL-23": [(145, 250, 1630, 680, 10)],
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    transparent_by_page: dict[str, list[str]] = {}
    for item in manifest["transparent"]:
        transparent_by_page.setdefault(item["page"], []).append(item["filename"])
    checker_by_page = {item["page"]: item["filename"] for item in manifest["checkerboards"]}

    checked_files = 0
    total_intermediate = 0
    for page, names in transparent_by_page.items():
        directory = OUT / page.lower()
        expected = set(names + [checker_by_page[page]])
        actual = {path.name for path in directory.glob("*.png")}
        assert actual == expected, (page, expected - actual, actual - expected)

        images: list[Image.Image] = []
        alphas: list[np.ndarray] = []
        for name in names:
            image = Image.open(directory / name)
            assert image.mode == "RGBA", (page, name, image.mode)
            assert image.size == (1920, 1080), (page, name, image.size)
            alpha = np.asarray(image.getchannel("A"))
            assert int(alpha.min()) == 0 and int(alpha.max()) == 255, (page, name)
            assert bool(((alpha > 0) & (alpha < 255)).any()), (page, name)
            title_end = TITLE_END.get(page, 200)
            assert int(alpha[:title_end, :].max()) == 0, (page, name, "title")
            bottom_start = BOTTOM_START.get(page, 955)
            assert int(alpha[bottom_start:, :].max()) == 0, (page, name, "bottom")
            images.append(image)
            alphas.append(alpha)

        combined_alpha = alphas[-1]
        if page in CUSTOM_COMBINED:
            for x, y, width, height, feather in CUSTOM_COMBINED[page]:
                interior = combined_alpha[
                    y + feather : y + height - feather,
                    x + feather : x + width - feather,
                ]
                assert int(interior.min()) == 255, (page, "combined interior gap")
        else:
            union_alpha = np.maximum.reduce(alphas[:-1])
            assert np.array_equal(union_alpha, combined_alpha), (page, "union mismatch")
        total_intermediate += int(((combined_alpha > 0) & (combined_alpha < 255)).sum())

        checker = Image.open(directory / checker_by_page[page])
        assert checker.mode == "RGBA" and checker.size == (1920, 1080), (page, "checker")
        assert checker.getchannel("A").getextrema() == (255, 255), (page, "checker alpha")

        source_copy = PROJECT / "public" / "ql-batch" / f"{page}.png"
        source_final = next((SOURCE_ROOT / page).glob("*最终合成版.png"))
        assert sha256(source_copy) == sha256(source_final), (page, "source hash")

        source_rgb = np.asarray(Image.open(source_copy).convert("RGB"))
        combined_rgb = np.asarray(images[-1].convert("RGB"))
        opaque = combined_alpha == 255
        assert np.array_equal(source_rgb[opaque], combined_rgb[opaque]), (page, "pixel drift")

        checked_files += len(expected)
        print(
            f"{page} PASS files={len(expected)} layers={len(names)-1} "
            f"alpha_values={len(np.unique(combined_alpha))} "
            f"bbox={images[-1].getchannel('A').getbbox()}"
        )

    expected_files = len(manifest["transparent"]) + len(manifest["checkerboards"])
    assert checked_files == expected_files, (checked_files, expected_files)
    print(f"BATCH_VALIDATION=PASS pages=22 files={checked_files} intermediate={total_intermediate}")


if __name__ == "__main__":
    main()
