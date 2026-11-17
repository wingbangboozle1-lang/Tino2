#!/usr/bin/env python3
"""History remediation — the filter that removes household material from Git history.

Why this exists
---------------
The repository is public and, before 15 Nov 2026, its history carried the household's own
figures: exact property values, exact tax bills, and ZIP-code-level locators. Rounding the
working tree does not change an earlier commit, and the standing owner item on the board
(L-D2 / P-4, and the Critical rows on the site's "Flagged for review" page) is to contain
that exposure. `docs/history-remediation-runbook.md` sets out the options; this module is
the mechanical part of option C.

How it decides what to change
-----------------------------
It reuses the repository's own policy, so the rewrite cannot drift from the gate that
guards the working tree:

  * `scripts/privacy-gate.py` — the four rule families, and the SHA-256 lists of
    blocked quasi-identifiers and pre-rounding household figures. Only hashes are held,
    so nothing in this file discloses what it removes;
  * `scripts/privacy-scrub.py` — the $10 rounding scope and the list of amounts a
    government body publishes, which may stay exact.

Three transformations are applied to every text blob:

  1. a blocked quasi-identifier (a ZIP code or a locator phrase) becomes a neutral
     placeholder that carries no information;
  2. a pre-rounding household figure becomes a **deterministic synthetic substitute** of
     the same magnitude — the same input always yields the same output, so the rewrite is
     reproducible and auditable, and the substitute cannot be inverted to recover the
     original;
  3. a dollar amount of $1,000 or more that is not a multiple of $10, is not published by
     a government body, and sits in the household-derived analysis scope, is rounded to
     $10 — the same rule the working-tree gate applies today.

It is used as a `git filter-repo --file-info-callback`, which is the only callback that
sees both the path and the contents, so the rounding rule can stay scoped to the paths it
belongs to. `scripts/history-remediation-runbook.md` §4 is the procedure.

Nothing in this file is a household value and nothing in it is an identifier.
"""
from __future__ import annotations

import hashlib
import importlib.util
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# The substitute is deterministic, so the rewrite is reproducible and a reviewer can check
# it. The salt is published deliberately: without it, a reviewer could not re-derive the
# substitute for a given input, and with it, nothing is disclosed — sha256 does not run
# backwards. The salt changes nothing about the originals, which are never stored.
SALT = b'tino2-history-remediation-v1'

PLACEHOLDER_LOCATOR = '[LOCATION]'
PLACEHOLDER_ZIP = '#####'


def _load(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


_POLICY = None


def load_policy():
    """Return the blocklist, the raw-figure list, the allowlist and the rounding scope.

    Cached: the callback runs once per file change in every commit, and re-reading the
    blocklist and the figure ledger each time would make the rewrite needlessly slow.
    """
    global _POLICY
    if _POLICY is not None:
        return _POLICY
    gate = _load(ROOT / 'scripts' / 'privacy-gate.py', 'privacy_gate')
    scrubber = gate.load_scrubber()
    blocked, _data = gate.blocked_hashes()
    raw_banned = gate.raw_figure_hashes() if hasattr(gate, 'raw_figure_hashes') else frozenset()
    allowed = scrubber.official_amounts()
    _POLICY = {
        'gate': gate,
        'scrubber': scrubber,
        'blocked': blocked,
        'raw_banned': raw_banned,
        'allowed': allowed,
        'round_scope': scrubber.ROUND_SCOPE,
    }
    return _POLICY


NUMERIC = re.compile(r'\d[\d,]*')
YEAR_LIKE = re.compile(r'^\d{4}$')

# The gate's pattern rules, and the neutral placeholder each one leaves behind. The rewrite
# applies the same rules the gate applies, so a blob the gate flags in history is a blob the
# rewrite can clean; otherwise a rewrite could not reach zero findings.
PATTERN_PLACEHOLDERS = (
    ('email', '[EMAIL]'),
    ('ssn', '[ID]'),
    ('phone', '[PHONE]'),
    ('apn', '[PARCEL]'),
    ('blocklot', '[BLOCK]'),
    ('street', '[STREET]'),
)


def _in_round_scope(path: str, round_scope) -> bool:
    return any(path == scope or path.startswith(scope.rstrip('/') + '/') for scope in round_scope)


def _substitute_number(token: str) -> str:
    """A deterministic synthetic number of the same magnitude, rounded to $10.

    The original is hashed with the published salt and the digest is mapped onto the same
    order of magnitude. The result is a plausible figure, so a table stays readable and a
    spreadsheet stays parseable, but it carries no information about the original and
    cannot be inverted back to it.
    """
    digits = token.replace(',', '')
    try:
        value = int(digits)
    except ValueError:
        return token
    digest = hashlib.sha256(SALT + digits.encode('utf8')).digest()
    span = max(1, len(digits) - 1)
    # Map onto the same number of significant digits, then round to the nearest $10.
    fraction = int.from_bytes(digest[:8], 'big') / float(1 << 64)
    magnitude = 10 ** max(3, len(digits) - 1)
    synthetic = int((magnitude + fraction * (magnitude * 9)) / 10.0) * 10
    if synthetic == value:                      # never leave the original in place
        synthetic = synthetic + 10
    if ',' in token:
        return format(synthetic, ',')
    return str(synthetic)


def _spans(text: str, policy):
    """Every replacement span in a text, as (start, end, replacement).

    The tokenisation is the gate's own: a numeric run, a comma-grouped amount, a calendar
    year in 2010–2120, or a capitalised phrase that might be a locator. Only a token whose
    SHA-256 is in the blocklist is treated as an identifier, so ordinary prose is untouched.
    """
    gate = policy['gate']
    blocked = policy['blocked']
    raw_banned = policy['raw_banned']
    out = []
    for name, placeholder in PATTERN_PLACEHOLDERS:
        pattern = getattr(gate, {'email': 'EMAIL', 'ssn': 'SSN', 'phone': 'PHONE',
                                'apn': 'APN_SCC', 'blocklot': 'BLOCKLOT_SF',
                                'street': 'STREET'}[name])
        for match in pattern.finditer(text):
            if name == 'email':
                domain = match.group(0).split('@')[-1].lower()
                safe = any(domain.endswith(suffix) for suffix in ('.gov', '.mil')) \
                    or domain in gate.SAFE_EMAIL_DOMAINS
                if safe:
                    continue          # an official contact address is published on purpose
            out.append((match.start(), match.end(), placeholder))
    for match in NUMERIC.finditer(text):
        raw = match.group(0)
        token = raw.replace(',', '')
        if YEAR_LIKE.match(token) and 2010 <= int(token) <= 2120:
            continue
        if hashlib.sha256(token.encode('utf8')).hexdigest() in raw_banned:
            out.append((match.start(), match.end(), _substitute_number(raw)))
    for match in gate.ZIP.finditer(text):
        if hashlib.sha256(match.group(0).encode('utf8')).hexdigest() in blocked:
            out.append((match.start(), match.end(), PLACEHOLDER_ZIP))
    for match in gate.CAPTION.finditer(text):
        phrase = match.group(0)
        forms = (phrase, phrase.replace(' ', '%20'), phrase.replace(' ', '-'), phrase.lower())
        if any(hashlib.sha256(form.encode('utf8')).hexdigest() in blocked for form in forms):
            out.append((match.start(), match.end(), PLACEHOLDER_LOCATOR))
    return out


def clean_text(text: str, path: str, policy, counts=None):
    """Return the anonymised form of a blob's text."""
    if counts is None:
        counts = {}
    spans = _spans(text, policy)
    if spans:
        # Apply from the end so earlier spans keep their offsets.
        for start, end, replacement in sorted(spans, key=lambda s: -s[0]):
            text = text[:start] + replacement + text[end:]
        counts['identifier_or_figure'] = counts.get('identifier_or_figure', 0) + len(spans)

    if _in_round_scope(path, policy['round_scope']):
        allowed = policy['allowed']

        def fix(match):
            amount = int(match.group(1).replace(',', ''))
            if amount >= 1000 and amount % 10 and amount not in allowed:
                counts['rounded'] = counts.get('rounded', 0) + 1
                return '$' + format(int(round(amount / 10.0)) * 10, ',')
            return match.group(0)

        # The same pattern the gate uses, so the rewrite and the gate cannot disagree.
        text = re.sub(r'\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.\d{1,2})?', fix, text)
    return text


def clean_file(filename: bytes, mode: bytes, blob_id: bytes, value):
    """`git filter-repo --file-info-callback` entry point."""
    policy = load_policy()
    contents = value.get_contents_by_identifier(blob_id)
    if contents is None:
        return filename, mode, blob_id
    if value.is_binary(contents):
        return filename, mode, blob_id
    try:
        text = contents.decode('utf8')
    except UnicodeDecodeError:
        return filename, mode, blob_id
    path = filename.decode('utf8', 'replace')
    cleaned = clean_text(text, path, policy)
    if cleaned == text:
        return filename, mode, blob_id
    return filename, mode, value.insert_file_with_contents(cleaned.encode('utf8'))
