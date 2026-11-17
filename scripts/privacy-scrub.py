#!/usr/bin/env python3
"""De-identify the repository tree, per the owner's rule: mask quasi-identifiers,
and round every dollar amount that no government body publishes to the nearest $10.

This script contains NO identifier and NO household value. The tokens it masks are
read from a file that lives outside git (``private/privacy-identifiers.txt``, listed in
``.gitignore``), one entry per line in the form ``literal<TAB>placeholder``. The hashes
of those same literals are what ``scripts/privacy-gate.py`` blocks, so a reader of the
repository cannot learn from the gate which strings were removed.

Usage:
    python3 scripts/privacy-scrub.py                  # report only
    python3 scripts/privacy-scrub.py --apply          # rewrite the tree
    python3 scripts/privacy-scrub.py --dirs docs research --apply
"""
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IDENTITY_FILE = ROOT / "private" / "privacy-identifiers.txt"

TEXT_EXT = {".md", ".html", ".htm", ".txt", ".css", ".js", ".json", ".jsonl",
            ".csv", ".py", ".cjs", ".yml", ".yaml"}
# Rounding is applied to the household-derived analysis artifacts that stay in the
# repository but are never published. It is deliberately NOT applied to the generated
# guide (whose figures are already governed by the $10 gate in scripts/test-guide.cjs),
# to code, or to session records: the coordination board forbids editing another
# session's block, and verification reports are the evidence trail for what was read.
# Identifiers, by contrast, are masked in every tracked file without exception.
ROUND_SCOPE = ("docs", "research", "pages", "dashboard", "site", "qa", "src", "integration",
               "cupertino.html", "decision.html", "flagged.html", "inheritance.html",
               "san-francisco.html", "research-portal.html", "sources.html", "taxes.html")

MONEY = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.\d{1,2})?")


def tracked_files():
    listing = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True,
                             text=True, check=True)
    for name in listing.stdout.splitlines():
        if Path(name).suffix in TEXT_EXT:
            yield name


def repo_text(name):
    """Read a tracked text file from the working tree, or from HEAD when there is none.

    The history audit is documented to run against ``git clone --mirror``, and a mirror
    clone is bare: it has no working tree. Reading the allowlist only from the filesystem
    therefore returned an empty set there, which made the audit report officially published
    amounts as rounding violations and listed clean HEAD blobs as still flagged — a false
    picture for the administrator deciding whether to rewrite history. Reading the same
    path out of the object database makes the instrument measure the same thing in a bare
    mirror as in a checkout.
    """
    path = ROOT / name
    if path.exists():
        return path.read_text(encoding="utf8")
    try:
        proc = subprocess.run(["git", "show", f"HEAD:{name}"], cwd=ROOT,
                              capture_output=True, text=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None
    return proc.stdout or None


def official_amounts():
    """Dollar amounts a government body publishes may stay exact; they are not household data."""
    allowed = set()
    for name in ("integration/ledger/official_amounts.txt", "integration/ledger/facts.jsonl"):
        text = repo_text(name)
        if text:
            for m in re.finditer(r"(?<![\d.])(\d{1,3}(?:,\d{3})+|\d{4,})(?![\d,]*\d)", text):
                allowed.add(int(m.group(1).replace(",", "")))
    ledger_text = repo_text("guide/figures/official-figures.json")
    if ledger_text:
        for fig in json.loads(ledger_text).get("figures", []):
            for field in ("official_exact", "display_rounded", "claim", "note"):
                for m in re.finditer(r"\$\s?([\d,]+)", str(fig.get(field, ""))):
                    allowed.add(int(m.group(1).replace(",", "")))
    gate_text = repo_text("scripts/test-guide.cjs")
    if gate_text:                          # the published allowlist of official amounts
        block = re.search(r"const OFFICIAL_AMOUNTS=new Map\(\[(.*?)\n\]\);",
                          gate_text, re.S)
        if block:
            for m in re.finditer(r"\[(\d+),", block.group(1)):
                allowed.add(int(m.group(1)))
    allowed.add(100)                        # statutory de-minimis thresholds are quoted exactly
    return allowed


def round10(value):
    return int(round(value / 10.0)) * 10


def load_masks():
    if not IDENTITY_FILE.exists():
        return []
    masks = []
    for line in IDENTITY_FILE.read_text(encoding="utf8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        literal, _, placeholder = line.partition("\t")
        if literal and placeholder:
            masks.append((literal.strip(), placeholder.strip()))
    return masks


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--dirs", nargs="*", default=None)
    args = parser.parse_args()

    masks = load_masks()
    if not masks:
        print(f"note: no identifier file at {IDENTITY_FILE.relative_to(ROOT)} (git-ignored); "
              "running the $10 rounding pass only")
    allowed = official_amounts()
    scope = set(args.dirs) if args.dirs else None
    counts = {"mask": 0, "money": 0, "files": 0}

    for name in tracked_files():
        if scope and not any(name == d or name.startswith(d.rstrip("/") + "/") for d in scope):
            continue
        path = ROOT / name
        text = original = path.read_text(encoding="utf8")
        for literal, placeholder in masks:
            if literal in text:
                counts["mask"] += text.count(literal)
                text = text.replace(literal, placeholder)
        if name.startswith(ROUND_SCOPE):
            def fix(match):
                amount = int(match.group(1).replace(",", ""))
                if amount % 10 == 0 or amount in allowed or amount < 1000:
                    return match.group(0)
                counts["money"] += 1
                return "$" + format(round10(amount), ",")
            text = MONEY.sub(fix, text)
        if text != original:
            counts["files"] += 1
            if args.apply:
                path.write_text(text, encoding="utf8")

    verb = "scrubbed" if args.apply else "would scrub"
    print(f"{verb} {counts['files']} file(s); {counts['mask']} identifier occurrence(s); "
          f"{counts['money']} dollar amount(s) re-rounded to $10")
    if not args.apply and (counts["mask"] or counts["money"]):
        print("run with --apply to rewrite the tree")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
