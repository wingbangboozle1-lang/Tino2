#!/usr/bin/env python3
"""Privacy and number-rule scanner for everything this repository serves.

It contains no owner data. It reports:
  ERROR  e-mail addresses outside .gov, Social Security number patterns, Santa Clara
         County parcel-number patterns, numbered-avenue street addresses, and (when a
         private list is supplied from OUTSIDE the repository) exact owner figures.
  WARN   dollar amounts of $1,000 or more that are not multiples of $10 and do not
         appear in the verification ledger (official figures are allowed as published),
         phone numbers, other street-address patterns, San Francisco block-lot patterns.

Usage:  python3 integration/tools/privacy_scan.py [--private-list /path/outside/repo] [--quiet] [paths...]
Exit code 1 if any ERROR is found.
"""
import argparse, json, os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TEXT_EXT = {".html", ".htm", ".md", ".txt", ".css", ".js", ".json", ".jsonl", ".csv", ".py", ".yml", ".yaml", ".xml", ".svg", ""}
SKIP_DIRS = {".git", "node_modules", "__pycache__"}

MONEY = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.(\d{1,2}))?(?![\d,]*\d)")
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SSN = re.compile(r"(?<![\d-])\d{3}-\d{2}-\d{4}(?![\d-])")
APN_SCC = re.compile(r"(?<![\d-])\d{3}-\d{2}-\d{3}(?![\d-])")
BLOCKLOT_SF = re.compile(r"(?i)\b(?:block|lot|parcel|apn)\b[^<\n]{0,25}\b\d{4}[- ]?\d{3}[A-Z]?\b")
PHONE = re.compile(r"(?<![\d-])(?:1[-. ])?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?![\d-])")
STREET_ORD = re.compile(r"\b\d{3,5}\s+\d{1,2}(?:st|nd|rd|th)\s+(?:Avenue|Ave|Street|St)\b", re.I)
STREET = re.compile(r"\b\d{1,5}\s+(?:[NSEW]\.?\s+)?[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+(?:Street|St|Avenue|Ave|Boulevard|Blvd|Drive|Dr|Road|Rd|Lane|Ln|Way|Court|Ct|Place|Pl|Terrace|Circle)\b")


def official_amounts():
    """Dollar amounts that appear in the verification ledger are official figures."""
    allowed = set()
    path = os.path.join(ROOT, "integration", "ledger", "facts.jsonl")
    if os.path.exists(path):
        text = open(path, encoding="utf-8").read()
        for m in re.finditer(r"(?<![\d.])(\d{1,3}(?:,\d{3})+|\d{4,})(?![\d,]*\d)", text):
            allowed.add(int(m.group(1).replace(",", "")))
    extra = os.path.join(ROOT, "integration", "ledger", "official_amounts.txt")
    if os.path.exists(extra):
        for line in open(extra, encoding="utf-8"):
            line = line.split("#")[0].strip().replace(",", "").replace("$", "")
            if line.isdigit():
                allowed.add(int(line))
    return allowed


def load_private(path):
    vals = {}
    if not path:
        return vals
    ap = os.path.abspath(path)
    if ap.startswith(ROOT + os.sep):
        sys.exit("refusing: the private list must live outside the repository")
    for line in open(ap, encoding="utf-8"):
        line = line.split("#")[0].split()
        if len(line) == 2 and line[1].isdigit():
            vals[int(line[1])] = line[0]
    return vals


def iter_files(paths):
    for p in paths:
        p = os.path.join(ROOT, p) if not os.path.isabs(p) else p
        if os.path.isfile(p):
            yield p
            continue
        for d, dirs, files in os.walk(p):
            dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
            for f in sorted(files):
                if os.path.splitext(f)[1].lower() in TEXT_EXT:
                    yield os.path.join(d, f)


def scan(paths, private=None, include_ledger=False):
    allowed = official_amounts()
    private = private or {}
    priv_re = None
    if private:
        alts = []
        for v in private:
            s = str(v)
            with_commas = f"{v:,}"
            alts.append(re.escape(s))
            if with_commas != s:
                alts.append(re.escape(with_commas))
        priv_re = re.compile(r"(?<![\d,.])(?:" + "|".join(sorted(alts, key=len, reverse=True)) + r")(?![\d,]|\.\d)")
    findings = []
    for path in iter_files(paths):
        rel = os.path.relpath(path, ROOT)
        if rel.startswith(os.path.join("integration", "ledger")) and not include_ledger:
            continue
        if rel == os.path.join("integration", "tools", "privacy_scan.py"):
            continue
        try:
            lines = open(path, encoding="utf-8").read().split("\n")
        except (UnicodeDecodeError, OSError):
            continue
        for n, line in enumerate(lines, 1):
            def add(level, kind, text):
                findings.append((level, kind, rel, n, text))
            if priv_re:
                for m in priv_re.finditer(line):
                    v = int(m.group(0).replace(",", ""))
                    add("ERROR", f"exact owner figure ({private.get(v, '?')})", "[value withheld]")
            for m in EMAIL.finditer(line):
                dom = m.group(0).rsplit("@", 1)[1].lower()
                if dom.endswith(".gov") or dom == "users.noreply.github.com":
                    continue
                add("ERROR", "e-mail address", m.group(0)[:3] + "…@" + dom)
            for m in SSN.finditer(line):
                add("ERROR", "SSN-like pattern", "[withheld]")
            for m in APN_SCC.finditer(line):
                add("ERROR", "parcel-number-like pattern (###-##-###)", "[withheld]")
            for m in STREET_ORD.finditer(line):
                add("ERROR", "street address (numbered avenue/street)", "[withheld]")
            for m in BLOCKLOT_SF.finditer(line):
                add("WARN", "block/lot-like pattern", m.group(0)[:40])
            for m in STREET.finditer(line):
                add("WARN", "street-address-like pattern", m.group(0)[:50])
            for m in PHONE.finditer(line):
                add("WARN", "phone number", m.group(0))
            for m in MONEY.finditer(line):
                v = int(m.group(1).replace(",", ""))
                if v >= 1000 and v % 10 != 0 and m.group(2) is None and v not in allowed:
                    if priv_re and v in private:
                        continue  # already reported as ERROR
                    add("WARN", "dollar amount not rounded to $10 and not in the ledger", m.group(0))
    return findings


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("paths", nargs="*", default=["."])
    ap.add_argument("--private-list")
    ap.add_argument("--quiet", action="store_true", help="summary only")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    findings = scan(a.paths, load_private(a.private_list))
    if a.json:
        print(json.dumps([dict(level=l, kind=k, file=f, line=n, text=t) for l, k, f, n, t in findings], indent=1))
    else:
        summary = {}
        for l, k, f, n, t in findings:
            summary.setdefault((l, k, f), 0)
            summary[(l, k, f)] += 1
            if not a.quiet:
                print(f"{l:5} {f}:{n}  {k}: {t}")
        print("\nSummary (level, kind, file, count):")
        for (l, k, f), c in sorted(summary.items()):
            print(f"  {l:5} {c:4}  {f}  — {k}")
    errors = sum(1 for x in findings if x[0] == "ERROR")
    warns = len(findings) - errors
    print(f"\n{errors} error(s), {warns} warning(s)")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
