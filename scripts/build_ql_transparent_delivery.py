from __future__ import annotations

import json
import re
import shutil
from pathlib import Path
from PIL import Image, ImageDraw


ROOT = Path(r"E:\shengtu\智能物流\生图输出\2成品")
SIZE = (1920, 1080)


# Coordinates are defined on the normalized 1920x1080 delivery canvas.
# Each entry is a teaching/visual module; multiple rectangles mean one logical layer.
LAYERS = {
    1: [("供应物流", [(86, 278, 491, 554)]), ("生产物流", [(515, 278, 935, 554)]),
        ("销售物流", [(956, 278, 1385, 554)]), ("回收物流", [(86, 566, 590, 822)]),
        ("总结", [(610, 590, 1390, 822)])],
    2: [("收货场景", [(92, 278, 965, 874)]), ("定义文字", [(965, 292, 1814, 694)]),
        ("核心边界", [(986, 704, 1797, 844)])],
    3: [("物资需求", [(96, 337, 340, 777)]), ("采购订单", [(347, 337, 590, 777)]),
        ("供应商发货运输", [(598, 337, 910, 777)]), ("质检点数验收", [(917, 337, 1225, 777)]),
        ("合格物资入库", [(1234, 337, 1535, 777)]), ("连接箭头", [(294, 405, 1285, 608)]),
        ("结果带", [(690, 782, 1538, 914)])],
    4: [("盲目采购", [(96, 286, 873, 550)]), ("物资积压", [(884, 286, 1650, 550)]),
        ("物料短缺", [(96, 560, 873, 850)]), ("验收低效", [(884, 560, 1650, 850)])],
    5: [("采购管理系统", [(75, 278, 612, 546)]), ("WMS", [(1186, 278, 1750, 546)]),
        ("供应商协同平台", [(75, 564, 612, 811)]), ("中央协同网络", [(590, 330, 1238, 829)]),
        ("结果带", [(187, 826, 1687, 935)])],
    6: [("完整口诀图文", [(244, 305, 1672, 827)])],
    7: [("企业内部说明", [(625, 248, 1300, 328)]), ("厂房背景", [(93, 327, 1807, 683)]),
        ("六节点", [(105, 339, 1791, 690)]), ("路线层", [(145, 548, 1760, 733)]),
        ("底部定义", [(95, 704, 1074, 899)]), ("价值结论", [(1090, 704, 1805, 899)])],
    8: [("库存原料", [(91, 287, 623, 545)]), ("车间暂存", [(635, 287, 1164, 545)]),
        ("在制品工序", [(1178, 287, 1711, 545)]), ("半成品暂存", [(91, 558, 623, 838)]),
        ("成品包装", [(635, 558, 1164, 838)]), ("成品入库", [(1178, 558, 1711, 838)])],
    9: [("动线混乱", [(81, 316, 500, 826)]), ("物料堆积", [(510, 316, 925, 826)]),
        ("人工搬运低效", [(935, 316, 1352, 826)]), ("工序衔接断层", [(1362, 316, 1778, 826)]),
        ("结果", [(374, 835, 1508, 934)])],
    10: [("AGV搬运机器人", [(91, 286, 628, 808)]), ("智能动态规划", [(641, 286, 1177, 808)]),
         ("数字化生产调度", [(1190, 286, 1725, 808)]), ("结果", [(360, 820, 1522, 924)])],
    11: [("完整口诀图文", [(297, 299, 1585, 829)])],
    12: [("左侧业务场景", [(87, 282, 1112, 894)]), ("定义文字", [(1130, 294, 1789, 659)]),
         ("核心价值", [(1130, 674, 1789, 890)])],
    13: [("接收客户订单", [(87, 300, 620, 548)]), ("成品拣货打包", [(633, 300, 1166, 548)]),
         ("销售分拨出库", [(1179, 300, 1711, 548)]), ("干线运输与配送", [(87, 561, 620, 812)]),
         ("终端交付验收", [(633, 561, 1166, 812)]), ("订单闭环", [(1179, 561, 1711, 812)]),
         ("客户体验结论", [(278, 822, 1518, 923)])],
    14: [("人工分拣低效", [(86, 306, 495, 795)]), ("配送时效不稳", [(506, 306, 915, 795)]),
         ("订单轨迹不透明", [(926, 306, 1335, 795)]), ("错发漏发", [(1346, 306, 1755, 795)]),
         ("结果", [(391, 809, 1452, 917)])],
    15: [("TMS", [(86, 290, 908, 532)]), ("智能分拣设备", [(920, 290, 1743, 532)]),
         ("AI路径规划", [(86, 548, 908, 790)]), ("可视化追踪", [(920, 548, 1743, 790)]),
         ("结果", [(382, 805, 1450, 925)])],
    16: [("上部口诀", [(320, 272, 1621, 500)]), ("下部MG场景", [(84, 518, 1095, 902)]),
         ("解释文字", [(1114, 518, 1788, 902)])],
    17: [("左侧回收场景", [(80, 312, 777, 897)]), ("定义文字", [(789, 302, 1780, 480)]),
         ("五类对象组", [(789, 486, 1780, 707)]), ("职责结论", [(789, 713, 1780, 900)])],
    18: [("三步主线", [(107, 291, 1763, 471)]), ("主线连接符", [(517, 318, 1370, 447)]),
         ("完好商品", [(107, 493, 900, 674)]), ("瑕疵商品", [(913, 493, 1763, 674)]),
         ("破损商品", [(107, 687, 900, 852)]), ("生产废料", [(913, 687, 1763, 852)]),
         ("关键动作", [(272, 861, 1605, 941)])],
    19: [("流程混乱", [(92, 310, 643, 726)]), ("处理缓慢", [(656, 310, 1207, 726)]),
         ("资源浪费", [(1220, 310, 1771, 726)]), ("经营后果", [(258, 742, 1605, 832)]),
         ("共同根因", [(258, 839, 1605, 925)])],
    20: [("平台底座", [(165, 287, 1694, 497)]), ("全程溯源", [(92, 513, 642, 821)]),
         ("智能质检", [(656, 513, 1206, 821)]), ("自动归仓", [(1220, 513, 1770, 821)]),
         ("结果", [(228, 832, 1640, 929)])],
    21: [("主口诀文字", [(99, 320, 884, 566)]), ("三行处置文字", [(99, 582, 884, 873)]),
         ("右侧MG场景", [(894, 282, 1778, 897)])],
    22: [("供应物流", [(90, 314, 485, 845)]), ("生产物流", [(498, 314, 893, 845)]),
         ("销售物流", [(906, 314, 1301, 845)]), ("回收物流", [(1314, 314, 1710, 845)]),
         ("判断方法", [(182, 853, 1623, 936)])],
    23: [("四段分工文字", [(84, 281, 1783, 427)]), ("数字场域背景", [(132, 426, 1755, 738)]),
         ("企业主体", [(225, 457, 1659, 815)]), ("前景车辆光轨", [(123, 643, 1763, 830)]),
         ("升级结论", [(190, 838, 1691, 932)])],
}


def source_map() -> dict[int, Path]:
    found: dict[int, Path] = {}
    for p in ROOT.glob("*.png"):
        m = re.search(r"QL-(\d{2})", p.name)
        if m:
            found[int(m.group(1))] = p
    return found


def normalize(im: Image.Image) -> Image.Image:
    im = im.convert("RGBA")
    if im.size == SIZE:
        return im
    # Cover, then center-crop. This avoids deformation and satisfies the delivery canvas.
    scale = max(SIZE[0] / im.width, SIZE[1] / im.height)
    nw, nh = round(im.width * scale), round(im.height * scale)
    im = im.resize((nw, nh), Image.Resampling.LANCZOS)
    left, top = (nw - SIZE[0]) // 2, (nh - SIZE[1]) // 2
    return im.crop((left, top, left + SIZE[0], top + SIZE[1]))


def make_layer(final: Image.Image, rects: list[tuple[int, int, int, int]]) -> Image.Image:
    mask = Image.new("L", SIZE, 0)
    draw = ImageDraw.Draw(mask)
    for box in rects:
        w, h = box[2] - box[0], box[3] - box[1]
        radius = max(8, min(22, w // 25, h // 10))
        draw.rounded_rectangle(box, radius=radius, fill=255)
    layer = final.copy()
    layer.putalpha(mask)
    return layer


def validate_page(page_dir: Path, expected_layers: int) -> dict:
    files = sorted(page_dir.glob("*.png"))
    fixed = [p for p in files if "最终合成版" in p.name or "通道合并版" in p.name]
    split = [p for p in files if re.search(r"_L\d{2}_", p.name)]
    errors = []
    if len(fixed) != 2:
        errors.append("missing fixed delivery")
    if len(split) != expected_layers:
        errors.append(f"split layer count {len(split)} != {expected_layers}")
    alpha_stats = {}
    for p in files:
        try:
            with Image.open(p) as im:
                im.load()
                if im.size != SIZE:
                    errors.append(f"wrong size: {p.name}")
                if im.mode != "RGBA":
                    errors.append(f"wrong mode: {p.name}")
                if "最终合成版" not in p.name:
                    a = im.getchannel("A")
                    lo, hi = a.getextrema()
                    alpha_stats[p.name] = [lo, hi]
                    if lo != 0 or hi == 0:
                        errors.append(f"invalid alpha: {p.name} ({lo},{hi})")
        except Exception as exc:
            errors.append(f"unreadable: {p.name}: {type(exc).__name__}")
    return {"ok": not errors, "errors": errors, "files": len(files), "alpha": alpha_stats}


def main() -> None:
    root_resolved = ROOT.resolve()
    if root_resolved != Path(r"E:\shengtu\智能物流\生图输出\2成品").resolve():
        raise RuntimeError(f"Unsafe target: {root_resolved}")
    srcs = source_map()
    missing = [i for i in range(1, 24) if i not in srcs]
    if missing:
        raise RuntimeError(f"Missing source pages: {missing}")

    report = {"root": str(root_resolved), "size": list(SIZE), "pages": {}}
    for page in range(1, 24):
        ql = f"QL-{page:02d}"
        out = ROOT / ql
        if out.exists() and any(out.iterdir()):
            existing = validate_page(out, len(LAYERS[page]))
            if not existing["ok"]:
                partials = list(out.iterdir())
                safe_prefix = f"企业全流程_{ql}_"
                if not partials or any((not p.is_file()) or p.suffix.lower() != ".png" or not p.name.startswith(safe_prefix) for p in partials):
                    raise RuntimeError(f"Refusing to clean unknown files in incomplete folder: {out}")
                # These are incomplete artifacts created by this script; remove only this page's exact prefixed PNGs.
                for p in partials:
                    p.unlink()
            else:
                report["pages"][ql] = existing
                continue
        out.mkdir(parents=True, exist_ok=True)
        final = normalize(Image.open(srcs[page]))
        final_name = out / f"企业全流程_{ql}_最终合成版.png"
        final.save(final_name, optimize=True)

        layers = []
        for idx, (label, rects) in enumerate(LAYERS[page], 1):
            layer = make_layer(final, rects)
            layer_path = out / f"企业全流程_{ql}_L{idx:02d}_{label}_通道.png"
            layer.save(layer_path, optimize=True)
            layers.append(layer)

        combined = Image.new("RGBA", SIZE, (0, 0, 0, 0))
        for layer in layers:
            combined = Image.alpha_composite(combined, layer)
        combined_path = out / f"企业全流程_{ql}_插图文字_通道合并版.png"
        combined.save(combined_path, optimize=True)
        report["pages"][ql] = validate_page(out, len(LAYERS[page]))

    all_ok = all(v["ok"] for v in report["pages"].values())
    report["all_ok"] = all_ok
    report_path = ROOT / "透明拆层交付验证报告.json"
    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    if not all_ok:
        raise RuntimeError(f"Validation failed; see {report_path}")

    # Delete only the exact 23 flat source files after every new page has validated.
    for p in srcs.values():
        if p.parent.resolve() != root_resolved or not re.search(r"QL-\d{2}", p.name):
            raise RuntimeError(f"Refusing unsafe delete: {p}")
    for p in srcs.values():
        p.unlink()
    print(json.dumps({"all_ok": True, "pages": 23, "report": str(report_path)}, ensure_ascii=False))


if __name__ == "__main__":
    main()
