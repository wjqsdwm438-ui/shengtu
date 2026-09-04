from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(r"E:\shengtu\skills-v2.7-development-snapshot-20260814\staging_ql01_precise")
OUT.mkdir(parents=True, exist_ok=True)
W, H = 1920, 1080
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
REG = r"C:\Windows\Fonts\msyh.ttc"
BLUE = (17, 117, 234, 255)
DARK = (5, 24, 77, 255)

ASSETS = {
    "供应物流": Path(r"C:\Users\Administrator\.codex\generated_images\01a04721-3537-73d3-9917-b7b3639f44aa\exec-40d5adc5-84cd-4599-bab9-0c9ac45cca52.png"),
    "生产物流": Path(r"C:\Users\Administrator\.codex\generated_images\01a04721-3537-73d3-9917-b7b3639f44aa\exec-e2dd089e-b64a-4327-bac9-c12ce80d967d.png"),
    "销售物流": Path(r"C:\Users\Administrator\.codex\generated_images\01a04721-3537-73d3-9917-b7b3639f44aa\exec-34f773cc-90c1-46f8-94cd-50b8581882e0.png"),
    "回收物流": Path(r"C:\Users\Administrator\.codex\generated_images\01a04721-3537-73d3-9917-b7b3639f44aa\exec-1ea4052d-810b-4c13-b1da-8f2499bb4e03.png"),
}


def canvas():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def paste_asset(dst, path, box):
    im = Image.open(path).convert("RGBA")
    alpha = im.getchannel("A")
    bbox = alpha.getbbox()
    if bbox:
        im = im.crop(bbox)
    x, y, maxw, maxh = box
    scale = min(maxw / im.width, maxh / im.height)
    size = (round(im.width * scale), round(im.height * scale))
    im = im.resize(size, Image.Resampling.LANCZOS)
    dst.alpha_composite(im, (x + (maxw - size[0]) // 2, y + (maxh - size[1]) // 2))


def module(title, subtitle, title_xy, subtitle_xy, asset_box, asset_path):
    im = canvas()
    d = ImageDraw.Draw(im)
    d.text(title_xy, title, font=ImageFont.truetype(BOLD, 63), fill=BLUE, stroke_width=0)
    d.text(subtitle_xy, subtitle, font=ImageFont.truetype(REG, 41), fill=DARK, stroke_width=0)
    paste_asset(im, asset_path, asset_box)
    return im


layers = [
    ("供应物流", module("供应物流：", "源头进货，保障生产", (202, 267), (207, 360), (160, 420, 500, 235), ASSETS["供应物流"])),
    ("生产物流", module("生产物流：", "内部流转，提质降本", (758, 267), (762, 360), (680, 420, 530, 238), ASSETS["生产物流"])),
    ("销售物流", module("销售物流：", "终端出货，链接市场", (1304, 267), (1308, 360), (1240, 418, 520, 242), ASSETS["销售物流"])),
    ("回收物流", module("回收物流：", "逆向闭环，盘活资源", (203, 672), (207, 762), (515, 666, 440, 250), ASSETS["回收物流"])),
]

summary = canvas()
d = ImageDraw.Draw(summary)
font = ImageFont.truetype(REG, 42)
bold = ImageFont.truetype(BOLD, 48)
x, y = 976, 721
d.text((x, y), "四者环环相扣，", font=bold, fill=BLUE)
prefix_w = d.textbbox((x, y), "四者环环相扣，", font=bold)[2] - x
d.text((x + prefix_w + 8, y + 5), "共同影响生产成本、", font=font, fill=DARK)
d.text((x, 808), "交付效率与资源利用率", font=font, fill=DARK)
layers.append(("总结", summary))

combined = canvas()
for idx, (name, im) in enumerate(layers, 1):
    im.save(OUT / f"企业全流程_QL-01_L{idx:02d}_{name}_通道.png", optimize=True)
    combined = Image.alpha_composite(combined, im)
combined.save(OUT / "企业全流程_QL-01_插图文字_通道合并版.png", optimize=True)

for name, path in ASSETS.items():
    Image.open(path).convert("RGBA").save(OUT / f"QL-01_重生成素材_{name}.png", optimize=True)

print(OUT)
