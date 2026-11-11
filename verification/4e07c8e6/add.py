#!/usr/bin/env python3
"""Append entries to ledger.json. Usage: python3 add.py < entries.json (a JSON list).
Each entry: id, area, rule, wording, url, source, accessed, status, matters.
status is one of: Confirmed | Not confirmed | Differs from site."""
import json, sys, os
p = os.path.join(os.path.dirname(os.path.abspath(__file__)), "ledger.json")
cur = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else []
new = json.load(sys.stdin)
ids = {e["id"] for e in cur}
for e in new:
    for k in ("id", "area", "rule", "wording", "url", "source", "accessed", "status", "matters"):
        assert k in e, (e.get("id"), k)
    assert e["url"].startswith("https://"), e["id"]
    assert e["status"] in ("Confirmed", "Not confirmed", "Differs from site"), e["id"]
    if e["id"] in ids:
        cur = [x for x in cur if x["id"] != e["id"]]
    cur.append(e)
json.dump(cur, open(p, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print(len(cur), "entries")
