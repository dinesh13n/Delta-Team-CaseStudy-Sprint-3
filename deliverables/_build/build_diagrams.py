"""Render every diagram in diagram_specs.py to .drawio (editable), .svg, .png, and diagrams.json (for the deck).
Usage (from the repository root): python deliverables/_build/build_diagrams.py"""

import html
import json
import math
import pathlib
import sys
import textwrap

HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE.parent / "diagrams"
sys.path.insert(0, str(HERE))
from diagram_specs import DIAGRAMS, H, STYLES, W  # noqa: E402

TITLE_H = 64  # standalone renders carry the title above the canvas
LH = 1.28     # line height factor


def wrap(node):
    """Wrap each paragraph to the box width. The same wrapped lines go to every output."""
    if node["kind"] == "lane":
        return [node["text"]]
    avail = node["w"] - 18
    per = max(6, int(avail / (node["fs"] * 0.54)))
    lines = []
    for para in node["text"].split("\n"):
        if not para:
            lines.append("")
            continue
        indent = "  " if para.startswith("• ") else ""
        lines += textwrap.wrap(para, per, subsequent_indent=indent, break_on_hyphens=False) or [""]
    return lines


def edge_point(n, tx, ty):
    """Point where the ray from n's centre towards (tx, ty) leaves n's rectangle."""
    cx, cy = n["x"] + n["w"] / 2, n["y"] + n["h"] / 2
    dx, dy = tx - cx, ty - cy
    if dx == 0 and dy == 0:
        return cx, cy
    sx = (n["w"] / 2) / abs(dx) if dx else math.inf
    sy = (n["h"] / 2) / abs(dy) if dy else math.inf
    s = min(sx, sy)
    return cx + dx * s, cy + dy * s


def endpoints(d):
    idx = {n["id"]: n for n in d["nodes"]}
    out = []
    for e in d["edges"]:
        a, b = idx[e["from"]], idx[e["to"]]
        ax, ay = edge_point(a, b["x"] + b["w"] / 2, b["y"] + b["h"] / 2)
        bx, by = edge_point(b, a["x"] + a["w"] / 2, a["y"] + a["h"] / 2)
        out.append({**e, "x1": round(ax, 1), "y1": round(ay, 1), "x2": round(bx, 1), "y2": round(by, 1)})
    return out


def svg(d):
    oy = TITLE_H
    p = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H + oy}" viewBox="0 0 {W} {H + oy}" '
         f'font-family="Arial, Helvetica, sans-serif">',
         '<defs><marker id="ah" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">'
         '<path d="M0,0 L10,5 L0,10 z" fill="#41545A"/></marker></defs>',
         f'<rect width="{W}" height="{H + oy}" fill="#FFFFFF"/>',
         f'<text x="12" y="40" font-size="26" font-weight="bold" fill="#0B3C49">{html.escape(d["title"])}</text>']
    for n in d["nodes"]:
        fill, stroke, col, dashed, boldfirst = STYLES[n["kind"]]
        x, y = n["x"], n["y"] + oy
        dash = ' stroke-dasharray="6 4"' if dashed else ""
        sw = 0 if n["kind"] == "note" else (1.2 if n["kind"] == "lane" else 1.6)
        rx = 6 if n["kind"] != "lane" else 4
        p.append(f'<rect x="{x}" y="{y}" width="{n["w"]}" height="{n["h"]}" rx="{rx}" fill="#{fill}" '
                 f'stroke="#{stroke}" stroke-width="{sw}"{dash}/>')
        lines = n["_lines"]
        fs = n["fs"]
        if n["kind"] == "lane":
            p.append(f'<text x="{x + 10}" y="{y + 24}" font-size="{fs}" font-weight="bold" fill="#{col}">{html.escape(lines[0])}</text>')
            continue
        total = len(lines) * fs * LH
        ty = y + (n["h"] - total) / 2 + fs * 0.98
        for i, ln in enumerate(lines):
            bold = ' font-weight="bold"' if (boldfirst and i == 0) else ""
            if n["align"] == "center":
                p.append(f'<text x="{x + n["w"] / 2}" y="{ty + i * fs * LH:.1f}" font-size="{fs}" text-anchor="middle" fill="#{col}"{bold}>{html.escape(ln)}</text>')
            else:
                p.append(f'<text x="{x + 9}" y="{ty + i * fs * LH:.1f}" font-size="{fs}" fill="#{col}"{bold} xml:space="preserve">{html.escape(ln)}</text>')
    for e in d["_edges"]:
        dash = ' stroke-dasharray="6 4"' if e["dashed"] else ""
        p.append(f'<line x1="{e["x1"]}" y1="{e["y1"] + oy}" x2="{e["x2"]}" y2="{e["y2"] + oy}" stroke="#41545A" '
                 f'stroke-width="1.8" marker-end="url(#ah)"{dash}/>')
    p.append("</svg>")
    return "\n".join(p)


def drawio_cells(d, page):
    cells = [f'<mxCell id="{page}-0"/>', f'<mxCell id="{page}-1" parent="{page}-0"/>']
    cells.append(f'<mxCell id="{page}-title" value="{html.escape(d["title"])}" style="text;html=1;fontSize=26;fontStyle=1;'
                 f'fontColor=#0B3C49;align=left;verticalAlign=middle;" vertex="1" parent="{page}-1">'
                 f'<mxGeometry x="12" y="10" width="{W - 24}" height="44" as="geometry"/></mxCell>')
    oy = TITLE_H
    for n in d["nodes"]:
        fill, stroke, col, dashed, boldfirst = STYLES[n["kind"]]
        lines = [html.escape(x) for x in n["_lines"]]
        if n["kind"] != "lane" and boldfirst and lines:
            lines[0] = f"<b>{lines[0]}</b>"
        if n["kind"] == "lane":
            value = f"<b>{lines[0]}</b>"
            st = (f"rounded=1;arcSize=2;whiteSpace=wrap;html=1;fillColor=#{fill};strokeColor=#{stroke};fontColor=#{col};"
                  f"fontSize={n['fs']};align=left;verticalAlign=top;spacingLeft=10;spacingTop=4;")
        else:
            value = "<br>".join(lines)
            st = (f"rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#{fill};strokeColor=#{'none' if n['kind'] == 'note' else stroke};"
                  f"fontColor=#{col};fontSize={n['fs']};align={n['align']};verticalAlign=middle;spacingLeft=8;spacingRight=8;"
                  f"{'dashed=1;' if dashed else ''}")
        cells.append(f'<mxCell id="{page}-{n["id"]}" value="{html.escape(value)}" style="{st}" vertex="1" parent="{page}-1">'
                     f'<mxGeometry x="{n["x"]}" y="{n["y"] + oy}" width="{n["w"]}" height="{n["h"]}" as="geometry"/></mxCell>')
    for i, e in enumerate(d["edges"]):
        st = "endArrow=block;endFill=1;html=1;rounded=0;strokeColor=#41545A;strokeWidth=2;" + ("dashed=1;" if e["dashed"] else "")
        cells.append(f'<mxCell id="{page}-e{i}" style="{st}" edge="1" parent="{page}-1" source="{page}-{e["from"]}" '
                     f'target="{page}-{e["to"]}"><mxGeometry relative="1" as="geometry"/></mxCell>')
    return "".join(cells)


def drawio(diagrams):
    pages = []
    for k, d in enumerate(diagrams):
        pages.append(f'<diagram id="p{k}" name="{html.escape(d["name"])}"><mxGraphModel dx="1280" dy="800" grid="1" gridSize="10" '
                     f'guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="{W}" '
                     f'pageHeight="{H + TITLE_H}" math="0" shadow="0"><root>{drawio_cells(d, f"p{k}")}</root></mxGraphModel></diagram>')
    return f'<mxfile host="app.diagrams.net" type="device">{"".join(pages)}</mxfile>\n'


def main():
    OUT.mkdir(exist_ok=True)
    for d in DIAGRAMS:
        for n in d["nodes"]:
            n["_lines"] = wrap(n)
            if n["kind"] != "lane":
                need = len(n["_lines"]) * n["fs"] * LH + 10
                if need > n["h"]:
                    print(f"WARN overflow {d['name']}:{n['id']} needs {need:.0f} has {n['h']}")
        d["_edges"] = endpoints(d)
        (OUT / f"{d['name']}.svg").write_text(svg(d), encoding="utf-8")
        (OUT / f"{d['name']}.drawio").write_text(drawio([d]), encoding="utf-8")
    (OUT / "all-diagrams.drawio").write_text(drawio(DIAGRAMS), encoding="utf-8")
    deck = [{"name": d["name"], "title": d["title"], "W": W, "H": H, "styles": STYLES,
             "nodes": [{k: v for k, v in n.items() if k != "text"} | {"lines": n["_lines"]} for n in d["nodes"]],
             "edges": d["_edges"]} for d in DIAGRAMS]
    (HERE / "diagrams.json").write_text(json.dumps(deck, indent=1), encoding="utf-8")
    print("wrote", len(DIAGRAMS), "diagrams")


if __name__ == "__main__":
    main()
