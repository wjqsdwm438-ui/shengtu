from __future__ import annotations

from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

W, H = 1920, 1080
OUT = Path(r"E:\shengtu\skills-v2.7-development-snapshot-20260814\staging_ql02_23_regenerated")
GEN = Path(r"C:\Users\Administrator\.codex\generated_images\01a04721-3537-73d3-9917-b7b3639f44aa")
BOLD = r"C:\Windows\Fonts\msyhbd.ttc"
REG = r"C:\Windows\Fonts\msyh.ttc"
BLUE = (17, 117, 234, 255)
DARK = (5, 24, 77, 255)
MID = (48, 79, 125, 255)
CARD = (245, 249, 255, 246)
EDGE = (199, 221, 245, 255)

ASSET_FILES = {
    2:"exec-f336975d-4e17-49cf-92e7-446e66b9c57b.png",3:"exec-9c72b09f-572b-405a-912a-fd38a90da821.png",
    4:"exec-20e05f2a-1315-4018-b668-a1d0b88eea2c.png",5:"exec-2d162795-f37a-4915-8575-0e2ceb3fd7b3.png",
    6:"exec-44e0df56-79b4-48bb-8d7f-8260bc264653.png",7:"exec-939969b4-dd7a-47b4-b7c8-79a4f7821b1c.png",
    8:"exec-939969b4-dd7a-47b4-b7c8-79a4f7821b1c.png",9:"exec-fd4fe57a-2273-4dd8-927a-72c76c0b0831.png",
    10:"exec-9b9371ea-8aab-4cea-b7a6-c4053381f477.png",11:"exec-43c0fd2c-3ccb-4f39-9070-1d747604dfce.png",
    12:"exec-4abb3812-4bd9-4838-a1aa-a34e9656a895.png",13:"exec-630a0a03-0258-4152-9573-d251fbb56494.png",
    14:"exec-526d90d5-1768-48d1-a715-434016ebf46e.png",15:"exec-719e1a74-0b57-41ec-ad1f-1084192efce7.png",
    16:"exec-5edd9d40-ab5a-4956-9fb1-a45a2cb7f3d6.png",17:"exec-a9316e6f-6d4b-4a94-b245-6689e7503e5b.png",
    18:"exec-1722ba0c-f97e-4ba0-bf14-c75e67e5f96e.png",19:"exec-a72ad44f-7d5e-45dc-b453-5dd59d5a1fac.png",
    20:"exec-2895e74a-242c-4045-b6b3-af225eec8313.png",21:"exec-78c4b67f-6258-4025-b279-93dafc71fa4d.png",
    22:"exec-00eac2e6-f282-4609-b26c-7adcfe9c9fe1.png",23:"exec-14923925-842c-4345-985f-fd884fb68c82.png",
}
QL23_FORE = "exec-1aa92598-a16e-4671-9c82-d1f4bb6b8dcd.png"


def cv(): return Image.new("RGBA", (W, H), (0,0,0,0))
def font(size, bold=False): return ImageFont.truetype(BOLD if bold else REG, size)


def trim(im: Image.Image, pad=8) -> Image.Image:
    im = im.convert("RGBA")
    b = im.getchannel("A").getbbox()
    if not b: return im
    b = (max(0,b[0]-pad),max(0,b[1]-pad),min(im.width,b[2]+pad),min(im.height,b[3]+pad))
    return im.crop(b)


def asset(page): return trim(Image.open(GEN / ASSET_FILES[page]))


def split_grid(im, cols, rows):
    im = im.convert("RGBA"); out=[]
    for r in range(rows):
        for c in range(cols):
            x0=round(c*im.width/cols); x1=round((c+1)*im.width/cols)
            y0=round(r*im.height/rows); y1=round((r+1)*im.height/rows)
            out.append(trim(im.crop((x0,y0,x1,y1))))
    return out


def paste_fit(dst, im, box, pad=8):
    x,y,w,h=box; im=trim(im)
    s=min((w-2*pad)/im.width,(h-2*pad)/im.height)
    sz=(max(1,round(im.width*s)),max(1,round(im.height*s)))
    im=im.resize(sz,Image.Resampling.LANCZOS)
    dst.alpha_composite(im,(x+(w-sz[0])//2,y+(h-sz[1])//2))


def wrap(draw, text, fnt, maxw):
    lines=[]
    for para in text.split("\n"):
        cur=""
        for ch in para:
            test=cur+ch
            if cur and draw.textbbox((0,0),test,font=fnt)[2]>maxw:
                lines.append(cur); cur=ch
            else: cur=test
        lines.append(cur)
    return lines


def card_layer(box, title, body="", art=None, art_ratio=.58, title_size=34, body_size=24):
    im=cv(); d=ImageDraw.Draw(im); x,y,w,h=box
    d.rounded_rectangle((x,y,x+w,y+h),radius=20,fill=CARD,outline=EDGE,width=2)
    art_h=round(h*art_ratio) if art is not None else 0
    if art is not None: paste_fit(im,art,(x+10,y+10,w-20,art_h-10),4)
    ty=y+art_h+12 if art is not None else y+22
    d.text((x+22,ty),title,font=font(title_size,True),fill=BLUE)
    if body:
        f=font(body_size); yy=ty+title_size+16
        for line in wrap(d,body,f,w-44):
            d.text((x+22,yy),line,font=f,fill=DARK); yy+=body_size+10
    return im


def text_layer(box, text, size=34, bold=False, fill=DARK, panel=False, center=False, line_gap=14):
    im=cv(); d=ImageDraw.Draw(im); x,y,w,h=box
    if panel: d.rounded_rectangle((x,y,x+w,y+h),radius=20,fill=CARD,outline=EDGE,width=2)
    f=font(size,bold); lines=wrap(d,text,f,w-40); yy=y+20
    for line in lines:
        bb=d.textbbox((0,0),line,font=f); xx=x+(w-(bb[2]-bb[0]))//2 if center else x+20
        d.text((xx,yy),line,font=f,fill=fill); yy+=size+line_gap
    return im


def banner(text, y=850, h=76, x=210, w=1500, blue=False):
    im=cv(); d=ImageDraw.Draw(im)
    d.rounded_rectangle((x,y,x+w,y+h),radius=18,fill=((22,119,230,245) if blue else (242,248,255,246)),outline=EDGE,width=2)
    f=font(30,True); bb=d.textbbox((0,0),text,font=f)
    d.text((x+(w-(bb[2]-bb[0]))//2,y+(h-(bb[3]-bb[1]))//2-3),text,font=f,fill=((255,255,255,255) if blue else BLUE))
    return im


def save_page(page, layers):
    p=OUT/f"QL-{page:02d}"; p.mkdir(parents=True,exist_ok=True)
    combined=cv()
    for i,(name,im) in enumerate(layers,1):
        im.save(p/f"企业全流程_QL-{page:02d}_L{i:02d}_{name}_通道.png",optimize=True)
        combined=Image.alpha_composite(combined,im)
    combined.save(p/f"企业全流程_QL-{page:02d}_插图文字_通道合并版.png",optimize=True)
    ad=p/"重生成局部素材"; ad.mkdir(exist_ok=True)
    Image.open(GEN/ASSET_FILES[page]).convert("RGBA").save(ad/f"QL-{page:02d}_重生成素材套件.png",optimize=True)


def standard_cards(page, titles, bodies, cols, rows, result=None):
    arts=split_grid(Image.open(GEN/ASSET_FILES[page]),cols,rows); layers=[]
    gx,gy,gw,gh=90,290,1740,540 if rows==1 else 560
    gap=18; cw=(gw-gap*(cols-1))//cols; ch=(gh-gap*(rows-1))//rows
    for i,title in enumerate(titles):
        r=i//cols;c=i%cols; box=(gx+c*(cw+gap),gy+r*(ch+gap),cw,ch)
        layers.append((title,card_layer(box,title,bodies[i] if i<len(bodies) else "",arts[i],.58 if rows==1 else .61,30 if cols>=4 else 34,21 if cols>=4 else 23)))
    if result: layers.append(("结果",banner(result,870 if rows==1 else 875,64)))
    save_page(page,layers)


# QL-02
im=asset(2); layers=[]
scene=cv(); paste_fit(scene,im,(85,292,860,600)); layers.append(("收货场景",scene))
layers.append(("定义文字",text_layer((980,315,810,360),"服务生产前端，\n负责原材料、零部件、辅助物资和设备耗材的\n采购、运输、验收、入库与仓储保管。",34,True,panel=True,line_gap=20)))
layers.append(("核心边界",banner("核心边界：从物资需求形成，到合格物资进入库存。",720,82,980,810,True)))
save_page(2,layers)

# QL-03
standard_cards(3,["物资需求","采购订单","供应商发货运输","质检点数验收","合格物资入库"],
               ["根据生产计划统计需求","向合格供应商下达订单","打包发货并运输至厂区","核查规格、质量与数量","分类存储形成库存储备"],5,1,"结果：形成库存储备，等待生产领用")

# QL-04
standard_cards(4,["盲目采购","物资积压","物料短缺","验收低效"],
               ["需求判断不准","库存占用资金","影响生产连续性","到货核查耗时"],2,2)

# QL-05
standard_cards(5,["采购管理系统","WMS仓储系统","供应商协同平台","中央协同网络"],
               ["物资需求智能预判","库存自动预警与仓储协同","到货轨迹实时追踪","数据贯通、统一协同"],2,2,"形成“需求可预测、到货可追踪、库存可预警”的供应协同机制")

# QL-06
f6=asset(6); q=cv(); d=ImageDraw.Draw(q); d.rounded_rectangle((315,320,1605,825),24,fill=(242,248,255,245),outline=EDGE,width=2)
d.text((500,435),"供应物流管“进货”，",font=font(52),fill=DARK); d.text((500,525),"守住企业生产的第一道关口。",font=font(52),fill=DARK)
paste_fit(q,f6,(1210,565,340,210)); save_page(6,[("完整口诀图文",q)])

# QL-07 and QL-08 use the valid six-scene kit
arts=split_grid(Image.open(GEN/ASSET_FILES[8]),3,2)
layers=[("企业内部说明",text_layer((600,250,720,60),"生产物流发生在企业内部",28,True,BLUE,False,True))]
names=["库存原料按需出库","车间智能转运","各工序加工流转","半成品临时仓储","成品组装质检","成品入库"]
for i,n in enumerate(names):
    x=85+i*290; layers.append((n,card_layer((x,330,270,350),n,"",arts[i],.72,24,20)))
layers.append(("底部定义",text_layer((90,715,980,170),"原材料和零部件从仓库出库，在工序、工位之间流转、搬运、暂存和组装，直至成品入库。",25,False,DARK,True)))
layers.append(("价值结论",text_layer((1090,715,720,170),"它不创造新产品，却直接影响生产效率与成本。",29,True,BLUE,True,True)))
save_page(7,layers)

standard_cards(8,names,["按生产需求领料","实现精准配送","在制品连续流转","等待后续工序","完成装配与检查","合格成品入库"],3,2)

# QL-09
standard_cards(9,["动线混乱","物料堆积","人工搬运低效","工序衔接断层"],
               ["运输路线相互干扰","工序前后物料失衡","耗时且增加风险","等待时间拉长"],4,1,"结果：生产周期延长，人工与仓储损耗增加")

# QL-10
standard_cards(10,["AGV搬运机器人","智能动线规划","数字化生产调度"],
               ["实现物料精准配送","优化车间运输路径","协调物料与工序节拍"],3,1,"实现精准到位、工序无缝衔接，缩短生产周期并降低损耗")

# QL-11
f11=asset(11); q=cv(); d=ImageDraw.Draw(q); d.rounded_rectangle((310,315,1590,820),24,fill=(242,248,255,245),outline=EDGE,width=2)
d.text((430,435),"生产物流管“内部流转”，",font=font(48),fill=DARK); d.text((430,520),"是企业降本增效的关键。",font=font(48),fill=DARK)
paste_fit(q,f11,(1140,555,390,225)); save_page(11,[("完整口诀图文",q)])

# QL-12
f12=asset(12); sc=cv();paste_fit(sc,f12,(85,300,1040,600));
save_page(12,[("左侧业务场景",sc),("定义文字",text_layer((1150,320,620,340),"销售物流连接企业库存与市场，\n负责成品订单处理、打包分拣、出库运输、终端配送与客户签收。",28,False,DARK,True)),("核心价值",text_layer((1150,690,620,185),"核心价值：\n把库存商品转化为交付、连接客户。",28,True,BLUE,True))])

# QL-13
standard_cards(13,["接收客户订单","成品拣货打包","智能分拣出库","干线运输与配送","终端交付签收","订单闭环"],
               ["确认订单需求","完成拣选与包装","自动识别并分流","干线或同城配送","客户验收确认","状态回传完成履约"],3,2,"客户体验取决于每个节点的速度、准确性与可视性")

# QL-14
standard_cards(14,["人工分拣低效","配送时效不稳","订单轨迹不透明","错发漏发"],
               ["高峰期容易积压","配送时间难以保证","异常难以及时处理","增加补发与售后成本"],4,1,"结果：履约成本上升，企业口碑受损")

# QL-15
standard_cards(15,["TMS运输调度","智能分拣设备","AI路径规划","可视化追踪"],
               ["实现运力智能匹配","提高出库速度与准确率","优化配送路线","实时掌握订单状态"],2,2,"实现快速、准确、可视的全链路履约")

# QL-16
parts=split_grid(Image.open(GEN/ASSET_FILES[16]),2,1); top=text_layer((300,285,1320,190),"销售物流管“出货交付”，\n是企业链接市场、创造收益的桥梁。",40,True,DARK,True,True,18)
icon=cv();paste_fit(icon,parts[0],(185,305,230,150)); top=Image.alpha_composite(icon,top)
sc=cv();paste_fit(sc,parts[1],(85,520,1030,390)); expl=text_layer((1140,540,620,330),"只有把正确的商品，\n按时送到客户手中，\n销售才真正完成。",34,True,DARK,True,False,22)
save_page(16,[("上部口诀",top),("下部MG场景",sc),("解释文字",expl)])

# QL-17
f17=asset(17); sc=cv();paste_fit(sc,f17,(70,305,720,590)); obj="客户退换货　　残次产品\n生产废料　　　包装耗材\n和滞销库存"
save_page(17,[("左侧回收场景",sc),("定义文字",text_layer((810,300,970,175),"回收物流也叫逆向物流，是构建企业物流闭环的最后一环。",28,True,DARK,True)),("五类对象组",text_layer((810,495,970,210),obj,30,False,DARK,True,False,22)),("职责结论",text_layer((810,725,970,175),"它负责回收、运输、质检、分类及复用或报废处置，把单向交付变成企业物流闭环。",27,False,DARK,True))])

# QL-18
standard_cards(18,["退货申请","取件回运","仓库质检分类","完好商品重新入库","瑕疵商品维修复用","破损与废料合规回收"],
               ["客户发起申请","上门取件或回运","按状态检查分类","恢复可售库存","维修后再次利用","规范处置并回收资源"],3,2,"关键动作：先质检分类，再决定去向")

# QL-19
standard_cards(19,["流程混乱","处理缓慢","资源浪费"],["退换货流转难追踪","库存与客户等待增加","可复用物资未被识别"],3,1,"共同根因：逆向信息、质检与处置没有形成统一闭环")

# QL-20
parts=split_grid(Image.open(GEN/ASSET_FILES[20]),2,2)
layers=[("平台底座",card_layer((230,285,1460,225),"逆向物流平台：统一退货任务与状态","",parts[0],.78,30,22))]
for i,(n,b) in enumerate(zip(["全程溯源","智能质检","自动归仓"],["记录退货全流程","快速判断处置方式","可售商品自动回库"])):
    layers.append((n,card_layer((130+i*560,535,520,300),n,b,parts[min(i+1,3)],.60,30,22)))
layers.append(("结果",banner("缩短周期、盘活库存、回收资源，并满足合规要求",860,68)))
save_page(20,layers)

# QL-21
f21=asset(21); sc=cv();paste_fit(sc,f21,(930,310,820,575)); main=text_layer((100,325,760,210),"回收物流管“逆向闭环”，\n盘活企业资源，降低经营损耗。",35,True,DARK,True)
actions=text_layer((100,565,760,300),"让可售商品　重新入库，\n可用物资　再次利用，\n报废物资　合规退出。",31,False,DARK,True,False,24)
save_page(21,[("主口诀文字",main),("三行处置文字",actions),("右侧MG场景",sc)])

# QL-22
standard_cards(22,["供应物流","生产物流","销售物流","回收物流"],["进货，保障生产","内部流转，提质降本","出货交付，链接市场","逆向闭环，盘活资源"],4,1,"判断方法：看物资处于进入、内部、输出还是返回企业的哪一段")

# QL-23
enterprise=trim(Image.open(GEN/ASSET_FILES[23])); foreground=trim(Image.open(GEN/QL23_FORE))
top=text_layer((90,275,1740,150),"供应物流保障生产源头　　生产物流完成内部转化　　销售物流实现市场交付　　回收物流盘活资源闭环",25,True,BLUE,True,True)
bg=cv(); # intentionally transparent atmosphere layer: subtle light field only
d=ImageDraw.Draw(bg); d.ellipse((300,430,1620,865),fill=(65,168,255,22))
body=cv();paste_fit(body,enterprise,(145,405,1630,400)); fore=cv();paste_fit(fore,foreground,(260,690,1400,180))
end=banner("四大模块相互依存，推动传统人工物流向智能化、标准化、闭环化升级。",875,70,210,1500)
save_page(23,[("四段分工文字",top),("数字场域背景",bg),("企业主体",body),("前景车辆光轨",fore),("升级结论",end)])

print(OUT)
