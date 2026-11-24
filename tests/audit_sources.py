"""Check the embedded screen inventory against the Phase 1 source package."""

import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from zipfile import ZipFile


ROOT = Path(__file__).resolve().parents[1]
WORD = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def paragraphs(path):
    with ZipFile(path) as document:
        tree = ET.fromstring(document.read("word/document.xml"))
    lines = []
    for paragraph in tree.iter(WORD + "p"):
        text = "".join(t.text or "" for t in paragraph.iter(WORD + "t"))
        if text.strip():
            lines.append(" ".join(text.split()))
    return lines


def main():
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    wire = next(ROOT.rglob("*Wireframe.html")).read_text(encoding="utf-8-sig")
    original = json.loads(re.search(r"const D\s*=\s*(\{[^\n]+\})\s*;", wire)[1])
    embedded = json.loads(re.search(r'id="ux-data"[^>]*>(.*?)</script>', html, re.S)[1])
    assert embedded == original, "The embedded catalog differs from UX-02"
    ids = [s["id"] for s in embedded["screens"]]
    nav = [code for p in embedded["nav"] for g in p["groups"] for code in g["codes"]]
    assert sorted(ids) == sorted(nav) and len(set(ids)) == len(ids)
    sitemap = paragraphs(next(ROOT.rglob("*SRS-07*.docx")))
    assert set(ids) == set(re.findall(r"\bSCR-M\d\d-\d\d\b", "\n".join(sitemap)))

    differences = []
    checked = 0
    for volume in range(1, 7):
        doc = f"SRS-{volume:02}"
        lines = paragraphs(next(ROOT.rglob(f"*{doc}*.docx")))
        records = {p.split()[0]: i for i, p in enumerate(lines[:-1])
                   if p.startswith("SCR-") and lines[i + 1] == "Mục đích"}
        for screen in (s for s in embedded["screens"] if s["doc"] == doc):
            code = screen["id"]
            if code not in records:
                differences.append((code, "missing specification"))
                continue
            i = records[code]
            end = lines.index("Chức năng", i + 4)
            expected = [screen["purpose"], *screen["el"]]
            actual = [lines[i + 2], *lines[i + 4:end]]
            if [" ".join(value.split()) for value in expected] != actual:
                differences.append((code, "purpose/components differ"))
            checked += len(expected)
    for difference in differences:
        print(*difference)
    assert not differences, f"{len(differences)} differences require review"
    print(f"{len(ids)} screens, {len(embedded['nav'])} areas, {checked} purpose/component entries verified.")


if __name__ == "__main__":
    main()
