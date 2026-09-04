from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(r"E:\remotion\out")
OUT = Path(r"E:\shengtu\skills-v2.7-development-snapshot-20260814\tmp_ql01_remotion\layer-audit-v2")
OUT.mkdir(parents=True, exist_ok=True)


def checker(size: tuple[int, int], cell: int = 12) -> Image.Image:
    image = Image.new("RGB", size, "white")
    draw = ImageDraw.Draw(image)
    colors = ("#edf0f5", "#cfd5df")
    for y in range(0, size[1], cell):
        for x in range(0, size[0], cell):
            draw.rectangle((x, y, x + cell - 1, y + cell - 1), fill=colors[(x // cell + y // cell) % 2])
    return image


for page_num in range(1, 24):
    page = f"QL-{page_num:02d}"
    directory = ROOT / ("ql-01-pilot" if page_num == 1 else page.lower())
    files = sorted(directory.glob("*L??*_通道.png"))
    tile_w, tile_h = 600, 365
    columns = 3
    rows = (len(files) + columns - 1) // columns
    canvas = Image.new("RGB", (columns * tile_w, rows * tile_h), "white")
    draw = ImageDraw.Draw(canvas)
    for index, path in enumerate(files):
        image = Image.open(path).convert("RGBA")
        preview = checker((576, 324))
        scaled = image.resize((576, 324), Image.Resampling.LANCZOS)
        preview.paste(scaled.convert("RGB"), (0, 0), scaled.getchannel("A"))
        x = (index % columns) * tile_w + 12
        y = (index // columns) * tile_h + 28
        canvas.paste(preview, (x, y))
        draw.text((x, 7 + (index // columns) * tile_h), path.stem.split("_通道")[0], fill="black")
    canvas.save(OUT / f"{page}_独立层审核.jpg", quality=92)

print("LAYER_AUDIT_SHEETS=23")
