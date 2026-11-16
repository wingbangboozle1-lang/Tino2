#!/usr/bin/env python3
"""Whole-repository privacy gate — every tracked file, not only the published artifact.

Why this exists: the published guide is guarded by ``scripts/test-guide.cjs`` and
``scripts/privacy-audit.cjs``, which look at ``_public`` only. The repository also keeps a
legacy analysis tree (``docs/``, ``site/``, ``pages/``, ``qa/``, ``verification/`` …) that
GitHub code search indexes on a public repository, so a quasi-identifier or an un-rounded
household figure sitting there is findable even though no page serves it. This gate fails
the build on those files too.

What it enforces
  1. BLOCKED-IDENTIFIER   a quasi-identifier whose SHA-256 appears in scripts/privacy-blocklist.json
                          (ZIP codes and the district-level locator this repository was scrubbed of).
                          The list stores hashes only, so the gate cannot itself leak what it hides.
  2. ROUNDING             a dollar amount of $1,000 or more that is not a multiple of $10 and is not a
                          government-published amount, inside the household-derived analysis artifacts.
                          The published guide enforces the same rule on its own terms in test-guide.cjs.
  3. PATTERN              an e-mail address, phone number, SSN-shaped token, Santa Clara County parcel
                          number, San Francisco block/lot reference, or a street address.
  4. RAW-FIGURE           a pre-rounding household figure, recognised by the SHA-256 list the published
                          artifact audit uses (``RAW_BANNED`` in scripts/privacy-audit.cjs). That audit
                          scans ``_public`` only, so before this rule the same token was invisible in a
                          verification report, a research note or this board — where a rounded figure can
                          be quoted raw by accident. This rule covers every tracked text file. Only hashes
                          are compared, so neither this file nor the blocklist discloses what is blocked.

Usage:  python3 scripts/privacy-gate.py [--self-test] [--json]
Exit code 1 on any violation. Violations name the file, the line number and the rule — never the
matched text, so a failing CI log cannot become a leak either.
"""
import argparse
import hashlib
import importlib.util
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCKLIST = ROOT / 'scripts' / 'privacy-blocklist.json'
TEXT_EXT = {'.md', '.html', '.htm', '.txt', '.css', '.js', '.json', '.jsonl',
            '.csv', '.py', '.cjs', '.yml', '.yaml'}

ZIP = re.compile(r'(?<!\d)\d{5}(?:-\d{4})?(?!\d)')
CAPTION = re.compile(r'\b[A-Z][a-z]+(?:[ %20.-][A-Z][a-z]+){0,2}\b')
EMAIL = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b')
SSN = re.compile(r'(?<![\d-])\d{3}-\d{2}-\d{4}(?![\d-])')
PHONE = re.compile(r'(?<![\d-])(?:1[-. ])?\(?\d{3}\)?[-. ]\d{3}[-. ]\d{4}(?![\d-])')
APN_SCC = re.compile(r'(?<![\d-])\d{3}-\d{2}-\d{3}(?![\d-])')
BLOCKLOT_SF = re.compile(r'\b(?:block|lot|parcel|apn)\b[^\n<]{0,25}\b\d{4}[- ]?\d{3}[A-Z]?\b', re.I)
STREET = re.compile(r'\b\d{1,5}\s+(?:[NSEW]\.?\s+)?[A-Z][a-z]+(?:\s+[A-Z][a-z]+)?\s+'
                    r'(?:Street|St|Avenue|Ave|Boulevard|Blvd|Drive|Dr|Road|Rd|Lane|Ln|Way|'
                    r'Court|Ct|Place|Pl|Terrace|Circle|Way)\b')

SAFE_EMAIL_DOMAINS = ('example.com', 'example.org', 'example.net', 'example.test', 'localhost')

AUDIT = ROOT / 'scripts' / 'privacy-audit.cjs'
NUMERIC = re.compile(r'\d[\d,]*')
MONEY_CTX = re.compile(r'\$\s*([\d,]+)')
YEAR_LIKE = re.compile(r'^\d{4}$')


def raw_figure_hashes():
    """The pre-rounding tokens the published-artifact audit blocks, reused here.

    Read from ``scripts/privacy-audit.cjs`` rather than duplicated, so one list governs both the
    ``_public`` artifact and the whole tracked tree. Only 64-hex digests are ever taken from it.
    """
    text = AUDIT.read_text(encoding='utf8')
    block = re.search(r"const RAW_BANNED=new Set\(\[(.*?)\]\);", text, re.S)
    if not block:
        raise SystemExit('privacy-gate: RAW_BANNED set not found in scripts/privacy-audit.cjs')
    hashes = set(re.findall(r"'([0-9a-f]{64})'", block.group(1)))
    if not hashes:
        raise SystemExit('privacy-gate: RAW_BANNED set is empty; refusing to scan without it')
    return hashes


def numeric_tokens(line):
    """Digit strings in a line, split from adjacent letters so '$2,179,680NextWord' is one token.

    A bare four-digit calendar year in a table column is not treated as a figure, exactly as the
    artifact audit decides, because every money amount in this repository is '$'-prefixed or
    comma-grouped. A '$'-prefixed amount is always tested, in either scanner.
    """
    spaced = re.sub(r'([0-9])([A-Za-z])', r'\1 \2', line)
    spaced = re.sub(r'([A-Za-z])([0-9])', r'\1 \2', spaced)
    for match in NUMERIC.finditer(spaced):
        token = match.group(0).replace(',', '')
        if YEAR_LIKE.match(token) and 2010 <= int(token) <= 2120:
            continue
        yield token
    for match in MONEY_CTX.finditer(line):
        yield match.group(1).replace(',', '')


def load_scrubber():
    """Reuse the scrubber's allowlist and rounding scope, so one policy governs both tools."""
    spec = importlib.util.spec_from_file_location('privacy_scrub', ROOT / 'scripts' / 'privacy-scrub.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def blocked_hashes():
    data = json.loads(BLOCKLIST.read_text(encoding='utf8'))
    return set(data.get('hashes', [])), data


def candidates(line):
    """Tokens whose hash is compared with the blocklist, in every casing/encoding form URLs use."""
    out = set(ZIP.findall(line))
    for match in CAPTION.finditer(line):
        phrase = match.group(0)
        for form in (phrase, phrase.replace(' ', '%20'), phrase.replace(' ', '-'), phrase.lower()):
            out.add(form)
    return out


def pattern_hits(line):
    hits = []
    for rule, pattern in (('PATTERN:email', EMAIL), ('PATTERN:ssn', SSN), ('PATTERN:phone', PHONE),
                          ('PATTERN:apn', APN_SCC), ('PATTERN:blocklot', BLOCKLOT_SF),
                          ('PATTERN:street', STREET)):
        if pattern.search(line):
            hits.append(rule)
    if EMAIL.search(line):
        domain = EMAIL.search(line).group(0).split('@')[-1].lower()
        if any(domain.endswith(suffix) for suffix in ('.gov', '.mil')) or domain in SAFE_EMAIL_DOMAINS:
            hits.remove('PATTERN:email')     # an official contact address is published on purpose
    return hits


def scan_text(text, blocked, round_scope, path, allowed, raw_banned=frozenset()):
    violations = []
    for number, line in enumerate(text.splitlines(), start=1):
        for token in candidates(line):
            if hashlib.sha256(token.encode('utf8')).hexdigest() in blocked:
                violations.append((path, number, 'BLOCKED-IDENTIFIER'))
        for token in numeric_tokens(line):
            if hashlib.sha256(token.encode('utf8')).hexdigest() in raw_banned:
                violations.append((path, number, 'RAW-FIGURE'))
        for rule in pattern_hits(line):
            violations.append((path, number, rule))
        if round_scope and path.startswith(round_scope):
            for match in re.finditer(r'\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.\d{1,2})?', line):
                amount = int(match.group(1).replace(',', ''))
                if amount >= 1000 and amount % 10 and amount not in allowed:
                    violations.append((path, number, 'ROUNDING'))
    return violations


def tracked_text_files():
    listing = subprocess.run(['git', 'ls-files'], cwd=ROOT, capture_output=True, text=True, check=True)
    return [name for name in listing.stdout.splitlines()
            if Path(name).suffix in TEXT_EXT and Path(name).exists()]


def self_test():
    """The gate must detect a registered identifier. The literal below is synthetic and is
    not a real identifier, so registering it leaks nothing but proves the detector fires."""
    data = json.loads(BLOCKLIST.read_text(encoding='utf8'))
    test = data.get('self_test') or {}
    literal, digest = test.get('literal'), test.get('sha256')
    if not literal or not digest:
        print('FAIL: scripts/privacy-blocklist.json carries no self_test literal/sha256 pair')
        return 1
    if hashlib.sha256(literal.encode('utf8')).hexdigest() != digest:
        print('FAIL: the self-test hash does not match its literal; the blocklist file is inconsistent')
        return 1
    blocked = set(data.get('hashes', [])) | {digest}
    # A synthetic figure stands in for a pre-rounding household value, so the self-test proves the
    # detector fires without naming any token it blocks — and without a banned example amount ever
    # appearing in this file as one digit run (an earlier draft quoted one, and the gate flagged its
    # own source). The real list is hashed, so nothing here discloses what the list contains.
    synthetic = int('9876' '543')
    raw = raw_figure_hashes() | {hashlib.sha256(str(synthetic).encode('utf8')).hexdigest()}
    hit = scan_text(f'illustrative locator {literal} in a table row', blocked, None, 'SELF-TEST', set(), raw)
    miss = scan_text('illustrative row with no locator at all', blocked, None, 'SELF-TEST', set(), raw)
    noise = scan_text('a row mentioning 42425 and $1,230', blocked, None, None, set(), raw)
    raw_hit = scan_text(f'the assessment was {synthetic:,} in 2020 and the bill ${synthetic:,}', blocked,
                        None, 'SELF-TEST', set(), raw)
    year_ok = scan_text('| 2020 | 2021 | 2022 |', blocked, None, 'SELF-TEST', set(), raw)
    if (any(v[2] == 'BLOCKED-IDENTIFIER' for v in hit) and not miss and not noise
            and any(v[2] == 'RAW-FIGURE' for v in raw_hit) and not year_ok):
        print('PASS: the gate detects a registered identifier and a registered pre-rounding figure, '
              'stays silent on a clean row, and does not flag a bare calendar year or an unregistered number.')
        return 0
    print(f'FAIL: self-test hit={hit}, miss={miss}, noise={noise}, raw_hit={raw_hit}, year_ok={year_ok}')
    return 1


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--self-test', action='store_true')
    parser.add_argument('--json', action='store_true')
    args = parser.parse_args()
    if args.self_test:
        return self_test()

    scrubber = load_scrubber()
    allowed = scrubber.official_amounts()
    round_scope = scrubber.ROUND_SCOPE
    blocked, _data = blocked_hashes()
    raw_banned = raw_figure_hashes()
    violations = []
    for name in tracked_text_files():
        text = (ROOT / name).read_text(encoding='utf8', errors='replace')
        violations += scan_text(text, blocked, round_scope, name, allowed, raw_banned)

    violations = sorted(set(violations))
    if args.json:
        print(json.dumps([{'file': f, 'line': n, 'rule': r} for f, n, r in violations], indent=1))
    elif violations:
        for path, number, rule in violations[:200]:
            print(f'::error title=Privacy gate::{path}:{number} {rule}', file=sys.stderr)
        print(f'FAIL: {len(violations)} privacy-gate violation(s) across '
              f'{len({v[0] for v in violations})} file(s). The matched text is not printed.', file=sys.stderr)
        return 1
    else:
        print(f'PASS: {len(tracked_text_files())} tracked text files scanned — no blocked identifier or pre-rounding figure, '
              'no un-rounded household-scale amount in the analysis artifacts, no contact or parcel pattern. '
              'This is a guard, not proof of anonymity.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
