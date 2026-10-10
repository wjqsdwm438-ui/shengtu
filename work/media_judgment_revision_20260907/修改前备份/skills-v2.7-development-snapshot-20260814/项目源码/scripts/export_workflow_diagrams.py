#!/usr/bin/env python3
"""Synchronize the two workflow SVG previews from uncompressed draw.io XML.

This is a deliberately small, standard-library SVG renderer, NOT a native
diagrams.net export. It supports the styles used by this project's workflow
diagrams: text, rectangles, swimlanes, ellipses, diamonds, ports and waypoints.
Every visible cell carries its source ID/label, every edge its source/target,
and the SVG content attribute embeds the exact current draw.io source. No
network, installation, source mutation, or fingerprint generation is involved.

Usage: python export_workflow_diagrams.py [--check] [--source PATH]
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path
import unicodedata
import xml.etree.ElementTree as ET

NS = 'http://www.w3.org/2000/svg'
ET.register_namespace('', NS)
DEFAULT_SOURCE = Path(__file__).resolve().parents[1] / '课程视觉生产工具V2.7_项目节点与流程.drawio'
SUFFIXES = {'project-overview': '项目节点总览2', 'business-flow': '完整业务流程'}
RENDERER = 'project-standard-library-svg-v1 (not a native diagrams.net export)'


def tag(name):
    return f'{{{NS}}}{name}'


def element(parent, name, **attrs):
    return ET.SubElement(parent, tag(name), {k.replace('_', '-'): str(v) for k, v in attrs.items()})


def styles(cell):
    return dict(part.split('=', 1) if '=' in part else (part, '1')
                for part in cell.get('style', '').split(';') if part)


def text_width(text, size):
    return sum(size * (1 if unicodedata.east_asian_width(c) in 'WF' else .56) for c in text)


def wrap(text, width, size):
    result = []
    for line in text.splitlines() or ['']:
        current = ''
        for char in line:
            if current and text_width(current + char, size) > width:
                result.append(current); current = ''
            current += char
        result.append(current)
    return result


def render(diagram, source):
    model = diagram.find('mxGraphModel')
    width, height = float(model.get('pageWidth')), float(model.get('pageHeight'))
    cells = {c.get('id'): c for c in model.findall('root/mxCell')}
    svg = ET.Element(tag('svg'), {
        'width': str(int(width)), 'height': str(int(height)),
        'viewBox': f'0 0 {width:g} {height:g}', 'content': source,
        'data-renderer': RENDERER, 'data-diagram-id': diagram.get('id'),
        'role': 'img', 'aria-label': diagram.get('name'),
    })
    element(svg, 'title').text = diagram.get('name')
    element(svg, 'desc').text = '标准库同步预览；可编辑源为同目录 drawio。所有节点、边和内嵌源均来自当前 XML；不是原生导出。'
    element(svg, 'metadata').text = RENDERER
    defs = element(svg, 'defs')
    element(svg, 'rect', width=width, height=height, fill='#FFFFFF')
    layers = {name: element(svg, 'g', id=name) for name in ('containers', 'edges', 'vertices', 'edge-labels')}
    boxes = {}

    def box(cid):
        if cid in boxes: return boxes[cid]
        c = cells[cid]; g = c.find('mxGeometry')
        vals = [float(g.get(k, 0)) for k in ('x','y','width','height')]
        p = cells.get(c.get('parent'))
        if p is not None and p.get('vertex') == '1':
            pb = box(p.get('id')); vals[0] += pb[0]; vals[1] += pb[1]
        boxes[cid] = tuple(vals)
        return boxes[cid]

    def port(cid, st, prefix, other):
        x,y,w,h = box(cid)
        if prefix + 'X' in st:
            px,py = float(st[prefix+'X']), float(st.get(prefix+'Y', '.5'))
            dx,dy = (px-.5)*w, (py-.5)*h
        else:
            dx,dy = other[0]-(x+w/2), other[1]-(y+h/2)
        sh=styles(cells[cid])
        if not dx and not dy: return (x+w/2,y+h/2)
        if 'rhombus' in sh:
            scale=1/(abs(dx)/(w/2)+abs(dy)/(h/2))
        elif 'ellipse' in sh:
            scale=1/math.sqrt((dx/(w/2))**2+(dy/(h/2))**2)
        else:
            scale=min((w/2)/abs(dx) if dx else math.inf,(h/2)/abs(dy) if dy else math.inf)
        return x+w/2+dx*scale,y+h/2+dy*scale

    for cid,c in cells.items():
        if c.get('vertex') != '1': continue
        x,y,w,h = box(cid); st=styles(c); label=c.get('value','')
        is_group='swimlane' in st
        group=element(layers['containers' if is_group else 'vertices'], 'g',
                      data_cell_id=cid, data_label=label, data_parent=c.get('parent', ''))
        element(group,'title').text=label
        attrs={'fill':st.get('fillColor','#FFFFFF'), 'stroke':st.get('strokeColor','#475569'),
               'stroke_width':st.get('strokeWidth',1)}
        if st.get('dashed')=='1': attrs['stroke_dasharray']='7 5'
        if 'text' not in st:
            if 'rhombus' in st:
                element(group,'polygon',points=f'{x+w/2},{y} {x+w},{y+h/2} {x+w/2},{y+h} {x},{y+h/2}',**attrs)
            elif 'ellipse' in st:
                element(group,'ellipse',cx=x+w/2,cy=y+h/2,rx=w/2,ry=h/2,**attrs)
            else:
                element(group,'rect',x=x,y=y,width=w,height=h,rx=10 if st.get('rounded')=='1' or is_group else 0,**attrs)
            if is_group:
                sy=y+float(st.get('startSize',40))
                element(group,'path',d=f'M {x} {sy} H {x+w}',fill='none',stroke=attrs['stroke'],stroke_width=1)
        size=float(st.get('fontSize',14)); max_width=w-24; max_height=h-20
        if 'text' in st: max_height=h-4
        if 'rhombus' in st:
            max_width=w*.69; max_height=h*.61
        if is_group: max_height=float(st.get('startSize',40))-8
        lines=wrap(label,max_width,size)
        while size>10 and (len(lines)*size*1.4>max_height or max((text_width(l,size) for l in lines),default=0)>max_width):
            size-=.5; lines=wrap(label,max_width,size)
        text_y=(y+float(st.get('startSize',40))/2) if is_group else y+h/2
        text=element(group,'text',x=x+w/2,y=text_y,font_size=size,
                     font_family='Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif',
                     font_weight='600' if st.get('fontStyle')=='1' or is_group else '400',
                     fill=st.get('fontColor','#1F2937'),text_anchor='middle')
        for i,line in enumerate(lines):
            element(text,'tspan',x=x+w/2,y=text_y+(i-(len(lines)-1)/2)*size*1.4+size*.35).text=line

    for cid,c in cells.items():
        if c.get('edge')!='1': continue
        st=styles(c); source_id=c.get('source'); target_id=c.get('target')
        sb,tb=box(source_id),box(target_id)
        raw=[(float(p.get('x')),float(p.get('y'))) for p in c.findall('mxGeometry/Array/mxPoint')]
        start=port(source_id,st,'exit',raw[0] if raw else (tb[0]+tb[2]/2,tb[1]+tb[3]/2))
        end=port(target_id,st,'entry',raw[-1] if raw else (sb[0]+sb[2]/2,sb[1]+sb[3]/2))
        points=[start]+raw+[end]
        # Draw orthogonal elbows when the endpoints of an otherwise direct edge
        # are not exactly aligned. Explicit waypoints remain source-authoritative.
        if not raw and start[0]!=end[0] and start[1]!=end[1]:
            if st.get('exitX') in ('0','1'):
                mid=(start[0]+end[0])/2; points=[start,(mid,start[1]),(mid,end[1]),end]
            else:
                mid=(start[1]+end[1])/2; points=[start,(start[0],mid),(end[0],mid),end]
        color=st.get('strokeColor','#475569')
        marker=element(defs,'marker',id=f'arrow-{cid}',viewBox='0 0 10 10',refX=9,refY=5,
                       markerWidth=7,markerHeight=7,orient='auto-start-reverse',markerUnits='strokeWidth')
        element(marker,'path',d='M 0 0 L 10 5 L 0 10 z',fill=color)
        group=element(layers['edges'],'g',data_cell_id=cid,data_source=source_id,data_target=target_id,data_label=c.get('value',''))
        attrs={'fill':'none','stroke':color,'stroke_width':st.get('strokeWidth',2),'marker_end':f'url(#arrow-{cid})'}
        if st.get('dashed')=='1': attrs['stroke_dasharray']='7 5'
        element(group,'polyline',points=' '.join(f'{x:g},{y:g}' for x,y in points),**attrs)
        label=c.get('value','')
        if label:
            segments=[(a,b,math.dist(a,b)) for a,b in zip(points,points[1:])]
            total=sum(s[2] for s in segments); geo=c.find('mxGeometry')
            fraction=(float(geo.get('x',0))+1)/2; remaining=total*fraction
            px,py=points[0]; vertical=False
            for a,b,length in segments:
                if remaining<=length and length:
                    t=remaining/length; px=a[0]+(b[0]-a[0])*t; py=a[1]+(b[1]-a[1])*t
                    vertical=abs(b[1]-a[1])>abs(b[0]-a[0]); break
                remaining-=length
            offset=float(geo.get('y',-10)); py+=offset if not vertical else 0
            if vertical: px+=offset
            size=float(st.get('fontSize',13)); tw=text_width(label,size)+12
            # Source-relative placement is used above; keep labels fully inside
            # the declared preview canvas rather than clipping outer feedbacks.
            px=min(max(px,tw/2+8),width-tw/2-8)
            py=min(max(py,14),height-35)
            group=element(layers['edge-labels'],'g',data_edge_label_for=cid)
            element(group,'rect',x=px-tw/2,y=py-11,width=tw,height=22,rx=4,fill='#FFFFFF',fill_opacity='.96')
            element(group,'text',x=px,y=py+4,font_size=size,font_family='Microsoft YaHei, Noto Sans CJK SC, Arial, sans-serif',text_anchor='middle',fill=color).text=label
    element(svg,'text',x=40,y=height-15,font_size=11,font_family='Microsoft YaHei, Arial, sans-serif',fill='#64748B').text='标准库同步 SVG 预览（非原生导出）｜可编辑源与内嵌 XML 同步｜S/A/B 授权重构 2026-09-07'
    ET.indent(svg,space='  ')
    return ET.tostring(svg,encoding='unicode',xml_declaration=True)


def validate(path, source, diagram):
    assert path.read_text(encoding='utf-8')==render(diagram,source), f'{path.name}: preview differs from current source rendering'
    svg=ET.parse(path).getroot()
    assert svg.get('content')==source, f'{path.name}: embedded source differs'
    assert svg.get('data-diagram-id')==diagram.get('id')
    assert svg.get('data-renderer')==RENDERER
    expected={c.get('id'):c for c in diagram.findall('mxGraphModel/root/mxCell') if c.get('vertex')=='1' or c.get('edge')=='1'}
    actual={g.get('data-cell-id'):g for g in svg.iter(tag('g')) if g.get('data-cell-id')}
    assert set(expected)==set(actual), f'{path.name}: cell inventory differs'
    for cid,c in expected.items():
        g=actual[cid]
        assert g.get('data-label')==c.get('value',''), f'{cid}: label differs'
        if c.get('edge')=='1':
            assert g.get('data-source')==c.get('source') and g.get('data-target')==c.get('target'), f'{cid}: topology differs'
        else:
            visible=''.join(t.text or '' for t in g.iter(tag('tspan')))
            assert visible==''.join(c.get('value','').splitlines()), f'{cid}: visible label differs'
    return {'diagram':diagram.get('id'),'vertices':sum(c.get('vertex')=='1' for c in expected.values()),
            'edges':sum(c.get('edge')=='1' for c in expected.values()),'embedded_source_equal':True,'visible_labels_equal':True}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source',type=Path,default=DEFAULT_SOURCE)
    parser.add_argument('--check',action='store_true',help='Validate checked-in previews without writing files.')
    args=parser.parse_args()
    source=args.source.read_text(encoding='utf-8'); root=ET.fromstring(source)
    for did,suffix in SUFFIXES.items():
        diagram=root.find(f"diagram[@id='{did}']")
        if diagram is None: raise ValueError(f'Missing required diagram: {did}')
        out=args.source.with_name(args.source.stem+'-'+suffix+'.drawio.svg')
        if not args.check: out.write_text(render(diagram,source),encoding='utf-8')
        result=validate(out,source,diagram)
        print(f"PASS {did}: {result['vertices']} vertices, {result['edges']} edges; visible labels, topology, exact embedded source synchronized")


if __name__=='__main__': main()
