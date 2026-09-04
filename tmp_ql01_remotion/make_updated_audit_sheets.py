from pathlib import Path
from PIL import Image, ImageDraw

source = Path(r"E:\remotion\out")
target = Path(r"E:\shengtu\skills-v2.7-development-snapshot-20260814\tmp_ql01_remotion\updated-audit")
target.mkdir(parents=True, exist_ok=True)

pages = list(range(2, 24))
for sheet_index in range(0, len(pages), 6):
    selected = pages[sheet_index:sheet_index + 6]
    canvas = Image.new("RGB", (1440, 960), "white")
    draw = ImageDraw.Draw(canvas)
    for slot, page in enumerate(selected):
        path = source / f"ql-{page:02d}" / f"企业全流程_QL-{page:02d}_羽化棋盘审核图.png"
        image = Image.open(path).convert("RGB")
        image.thumbnail((700, 405), Image.Resampling.LANCZOS)
        x = 10 + (slot % 2) * 720
        y = 40 + (slot // 2) * 305
        canvas.paste(image, (x, y))
        draw.text((x, y - 26), f"QL-{page:02d}", fill="black")
    canvas.save(target / f"audit-{sheet_index // 6 + 1:02d}.jpg", quality=92)
