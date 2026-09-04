from pathlib import Path
from PIL import Image

ROOT = Path(r"E:\shengtu\智能物流\生图输出\2成品")

total = 0
for page_num in range(1, 24):
    page = f"QL-{page_num:02d}"
    directory = ROOT / page
    assert directory.is_dir(), page
    finals = list(directory.glob("*最终合成版.png"))
    assert len(finals) == 1, (page, "final", len(finals))
    layers = [path for path in directory.glob("*.png") if "最终合成版" not in path.name]
    assert layers, (page, "no layers")
    assert not any("羽化棋盘审核图" in path.name for path in layers), (page, "checker leaked")
    assert sum("插图文字_通道合并版" in path.name for path in layers) == 1, (page, "combined")
    for path in layers:
        with Image.open(path) as image:
            assert image.mode == "RGBA", (page, path.name, image.mode)
            assert image.size == (1920, 1080), (page, path.name, image.size)
            extrema = image.getchannel("A").getextrema()
            assert extrema == (0, 255), (page, path.name, extrema)
    total += 1 + len(layers)
    print(f"{page} PASS files={1 + len(layers)}")

print(f"DELIVERY_VALIDATION=PASS pages=23 files={total}")
