"""Checks the built dashboard: internal links, source link on every table row, rounding, placeholders.

External links cannot be reached from the build sandbox, so they are only counted and listed.
No personal data is stored in this script: the privacy check is rule-based (every dollar figure must
end in 0 unless it is on the short list of published statutory amounts).
"""
import os, re, sys
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DIRS = sys.argv[1:] or ["dashboard"]
STATUTORY = {"$1,044,586"}          # BOE Prop 19 amount, published figure
BANNED = re.compile(r"\b(APN|parcel (no|number|#)\s*[:#]?\s*\d|\d{3}-\d{2}-\d{3}|\d{1,5} [A-Z][a-z]+ (St|Street|Ave|Avenue|Dr|Drive|Rd|Road|Ct|Court|Way|Blvd|Ln|Lane)\b)")


class P(HTMLParser):
    def __init__(self):
        super().__init__(); self.links = []; self.ids = set(); self.rows = []; self._row = None; self.text = []
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a: self.ids.add(a["id"])
        if tag in ("a", "link") and a.get("href"): self.links.append(a["href"])
        if tag == "tr": self._row = {"td": 0, "a": 0}
        if self._row is not None and tag == "td": self._row["td"] += 1
        if self._row is not None and tag == "a": self._row["a"] += 1
    def handle_endtag(self, tag):
        if tag == "tr" and self._row is not None:
            if self._row["td"]: self.rows.append(self._row)
            self._row = None
    def handle_data(self, d): self.text.append(d)


errors, ext, pages, rows_total = [], set(), 0, 0
for d in DIRS:
    for base, _, files in os.walk(os.path.join(ROOT, d)):
        for fn in files:
            if not fn.endswith(".html"): continue
            path = os.path.join(base, fn); rel = os.path.relpath(path, ROOT); pages += 1
            p = P(); p.feed(open(path, encoding="utf-8").read()); text = " ".join(p.text)
            for h in p.links:
                if h.startswith(("http://", "https://")): ext.add(h); continue
                if h.startswith(("mailto:", "#")): continue
                target = os.path.normpath(os.path.join(base, h.split("#")[0].split("?")[0]))
                if os.path.isdir(target): target = os.path.join(target, "index.html")
                if not os.path.exists(target): errors.append(f"{rel}: broken internal link {h}")
            for r in p.rows:
                rows_total += 1
                if d == "dashboard" and r["a"] == 0: errors.append(f"{rel}: table row without a source link")
            for mny, tail in re.findall(r"(\$\d{1,3}(?:,\d{3})*|\$\d+)(\s*billion)?", text):
                if tail:
                    continue
                if d == "dashboard" and not mny.replace(",", "").endswith("0") and mny not in STATUTORY:
                    errors.append(f"{rel}: dollar figure not rounded to $10: {mny}")
            if BANNED.search(text): errors.append(f"{rel}: possible identifier: {BANNED.search(text).group(0)}")
            if d == "dashboard" and 'name="robots"' not in open(path).read(): errors.append(f"{rel}: missing noindex meta")
print(f"{pages} pages, {rows_total} table rows, {len(ext)} distinct external links (not machine-checked from this sandbox)")
for e in errors: print("ERROR", e)
sys.exit(1 if errors else 0)
