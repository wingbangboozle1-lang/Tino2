#!/usr/bin/env python3
"""Append verified facts to qa/ledger.json (session f16e6e34 verification ledger).

Every entry records the claim, the value, the official source URL, the date it was
re-opened, and the wording found there. Nothing household-specific is stored here.
Usage: python3 qa/tools/ledger_add.py <<'JSON'  [ {...}, {...} ]  JSON
"""
import json, sys, pathlib
P = pathlib.Path(__file__).resolve().parents[1] / "ledger.json"
REQ = ("id", "topic", "claim", "url", "source", "evidence", "status")
def main():
    new = json.load(sys.stdin)
    data = json.loads(P.read_text()) if P.exists() else []
    ids = {d["id"]: i for i, d in enumerate(data)}
    for n in new:
        for k in REQ:
            if k not in n:
                raise SystemExit(f"missing {k} in {n.get('id')}")
        if n["status"] not in ("verified", "unverified", "flag"):
            raise SystemExit("bad status " + n["id"])
        if n["status"] == "verified" and not n["url"].startswith("https://"):
            raise SystemExit("verified entry needs https url " + n["id"])
        n.setdefault("checked", "2026-11-11")
        if n["id"] in ids:
            data[ids[n["id"]]] = n
        else:
            data.append(n)
    P.write_text(json.dumps(data, indent=1, ensure_ascii=False) + "\n")
    print(f"ledger entries: {len(data)} (+{len(new)} submitted)")
main()
