#!/usr/bin/env python3
"""Append verified facts to the ledger (integration/ledger/facts.jsonl).

Usage:  python3 integration/tools/add_facts.py <<'JSON'
[ {"id": "...", "category": "...", "item": "...", "value": "...",
   "source_name": "...", "source_url": "https://...", "quote": "...",
   "checked": "YYYY-MM-DD", "status": "verified"}, ... ]
JSON

Rules enforced here so that nothing unverifiable slips into the ledger:
  * status must be one of: verified | unverified | owner-supplied | assumption
  * a "verified" row needs an https source_url on the official-domain allow-list and a non-empty quote
  * an "unverified" row must have an empty value (the value is left blank and the row is flagged)
  * ids are unique; re-adding an id replaces the earlier row (so corrections are explicit)
"""
import json, sys, os, re
from urllib.parse import urlparse

HERE = os.path.dirname(os.path.abspath(__file__))
LEDGER = os.path.join(HERE, "..", "ledger", "facts.jsonl")
ALLOW = os.path.join(HERE, "..", "ledger", "official_domains.txt")
REQUIRED = ["id", "category", "item", "value", "source_name", "source_url", "quote", "checked", "status"]
STATUSES = {"verified", "unverified", "owner-supplied", "assumption"}


def official_domains():
    with open(ALLOW, encoding="utf-8") as fh:
        return [l.split("#")[0].strip().lower() for l in fh if l.split("#")[0].strip()]


def is_official(url, domains):
    host = (urlparse(url).hostname or "").lower()
    return any(host == d or host.endswith("." + d) for d in domains)


def main():
    rows = json.load(sys.stdin)
    domains = official_domains()
    existing = {}
    if os.path.exists(LEDGER):
        with open(LEDGER, encoding="utf-8") as fh:
            for line in fh:
                if line.strip():
                    r = json.loads(line)
                    existing[r["id"]] = r
    for r in rows:
        missing = [k for k in REQUIRED if k not in r]
        if missing:
            sys.exit(f"{r.get('id')}: missing keys {missing}")
        if r["status"] not in STATUSES:
            sys.exit(f"{r['id']}: bad status {r['status']}")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", r["checked"]):
            sys.exit(f"{r['id']}: bad checked date")
        if r["status"] == "verified":
            if not r["source_url"].startswith("https://"):
                sys.exit(f"{r['id']}: verified row needs an https source_url")
            if not is_official(r["source_url"], domains):
                sys.exit(f"{r['id']}: source host is not on the official-domain allow-list: {r['source_url']}")
            if not r["quote"].strip():
                sys.exit(f"{r['id']}: verified row needs the supporting wording (quote)")
        if r["status"] == "unverified" and str(r["value"]).strip():
            sys.exit(f"{r['id']}: an unverified row must leave value blank")
        if r["source_url"] and not is_official(r["source_url"], domains):
            sys.exit(f"{r['id']}: link host is not on the official-domain allow-list: {r['source_url']}")
        if r["id"] in existing:
            print(f"replacing {r['id']}")
        existing[r["id"]] = r
    with open(LEDGER, "w", encoding="utf-8") as fh:
        for r in existing.values():
            fh.write(json.dumps(r, ensure_ascii=False, sort_keys=False) + "\n")
    print(f"ledger now has {len(existing)} rows")


if __name__ == "__main__":
    main()
