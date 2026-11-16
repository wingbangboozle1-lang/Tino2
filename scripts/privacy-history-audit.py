#!/usr/bin/env python3
"""Audit every reachable Git object for the findings the working-tree gate blocks.

Why this exists
  ``scripts/privacy-gate.py`` checks the files tracked at HEAD. The standing owner item on the
  board (L-D2, and the "needs review" P-4 row) is that earlier commits, other branches and
  pull-request refs may still carry material that the current tree no longer shows — and that
  the repository is public. An administrator deciding whether to rewrite history, delete the
  retained analysis tree, or privatize the repository needs to know **how much**, without a
  tool that prints what it found.

What it does
  * lists the objects of every commit reachable in this clone (``git rev-list --objects`` over
    all refs and the local reflog);
  * scans each unique text blob **once**, with the same three rule families the working-tree gate
    uses — blocked-identifier hashes, un-rounded household-scale amounts inside the analysis
    scope, and contact / parcel / address patterns — by importing the gate itself, so one policy
    governs both;
  * reports counts and file paths only. Matched text and blob content are never printed, so the
    audit can be pasted into a ticket or a commit message without becoming a second leak;
  * states plainly when the clone is shallow or partial, because "no findings in these objects"
    is not a statement about the remote repository's history.

It is an inventory for a human decision. It is not a gate: it exits 0 by default.
Use ``--strict`` to turn findings into a non-zero exit, and ``--json`` for machine-readable counts.

Run it on a full mirror clone to audit real history:
    git clone --mirror https://github.com/<owner>/<repo>.git
    cd <repo>.git && python3 <checkout>/scripts/privacy-history-audit.py
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load_gate():
    """Reuse the working-tree gate so history and HEAD can never drift apart in policy."""
    spec = importlib.util.spec_from_file_location('privacy_gate', ROOT / 'scripts' / 'privacy-gate.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def git(*args, check=True):
    proc = subprocess.run(['git', *args], cwd=ROOT, capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise SystemExit(f'FAIL: git {" ".join(args)}: {proc.stderr.strip().splitlines()[:1]}')
    return proc.stdout


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument('--json', action='store_true', help='machine-readable counts, no paths')
    parser.add_argument('--strict', action='store_true', help='exit 1 when any flagged blob is reachable')
    parser.add_argument('--max-paths', type=int, default=200, help='how many flagged paths to print')
    parser.add_argument('--self-test', action='store_true',
                        help='prove the detectors fire on a synthetic blob, then exit')
    args = parser.parse_args()

    gate = load_gate()
    scrubber = gate.load_scrubber()
    allowed = scrubber.official_amounts()
    round_scope = scrubber.ROUND_SCOPE
    blocked, _blocklist = gate.blocked_hashes()

    if args.self_test:
        # A synthetic string built from the blocklist’s own synthetic token, plus an un-rounded
        # amount. Nothing here is a household value, and none of it identifies anything.
        meta = json.loads((ROOT / 'scripts' / 'privacy-blocklist.json').read_text(encoding='utf8'))
        literal = meta['self_test']['literal']
        test_blocked = set(meta.get('hashes', [])) | {meta['self_test']['sha256']}
        # The path sits inside the analysis scope on purpose: the rounding rule, like the gate’s,
        # applies only to the household-derived analysis artifacts, not to every file in the tree.
        dirty = gate.scan_text(f'a table row naming {literal} and a cost of $1,234',
                               test_blocked, round_scope, 'docs/SELF-TEST.md', set())
        clean = gate.scan_text('a table row with a cost of $1,230 and no locator at all',
                               test_blocked, round_scope, 'docs/SELF-TEST.md', set())
        rules = {v[2] for v in dirty}
        if 'BLOCKED-IDENTIFIER' in rules and 'ROUNDING' in rules and not clean:
            print('PASS: the history audit applies the same detectors as the working-tree gate — it '
                  'flags a registered identifier hash and an un-rounded amount, and stays silent on a clean row.')
            return 0
        print(f'FAIL: the dirty row produced {sorted(rules)}; the clean row produced {clean}')
        return 1

    shallow = (ROOT / '.git' / 'shallow').exists() or (ROOT / '.git' / 'shallow.lock').exists()
    refs = [r for r in git('for-each-ref', '--format=%(refname)').split() if r]
    try:
        commits = int(git('rev-list', '--all', '--count').strip() or '0')
    except ValueError:
        commits = 0
    objects = git('rev-list', '--objects', '--all', '--reflog').splitlines()

    candidates = []
    for line in objects:
        parts = line.split(' ', 1)
        if len(parts) != 2:
            continue          # a commit or tree with no path: nothing to attribute
        sha, path = parts
        if Path(path).suffix in gate.TEXT_EXT:
            candidates.append((sha, path))

    # Deduplicate by blob: the same content in a hundred commits is one scan. One batched
    # `git cat-file --batch` process feeds the scan, because spawning a reader per object is what
    # makes a history audit slow enough that nobody runs it.
    unique = []
    want = set()
    for sha, path in candidates:
        if sha not in want:
            want.add(sha)
            unique.append(sha)

    seen, flagged, scanned = {}, Counter(), 0
    if unique:
        proc = subprocess.Popen(['git', 'cat-file', '--batch'], cwd=ROOT,
                                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)

        def read_line():
            line = proc.stdout.readline()
            return line.decode('utf8', 'replace').rstrip('\n') if line else None

        def read_exactly(n):
            buf, missing = bytearray(), n
            while missing > 0:
                chunk = proc.stdout.read(missing)
                if not chunk:
                    break
                buf += chunk
                missing -= len(chunk)
            return bytes(buf)

        body = {}
        for sha in unique:
            proc.stdin.write((sha + '\n').encode('ascii'))
            proc.stdin.flush()
            header = read_line()
            if not header:
                break
            fields = header.split(' ')
            if len(fields) < 3 or fields[1] != 'blob':
                continue                       # MISSING, or a tree/commit sharing the prefix
            # Read the blob's own bytes, then discard the newline git appends after each frame.
            body[sha] = read_exactly(int(fields[2])).decode('utf8', 'replace')
            read_exactly(1)
        try:
            proc.stdin.close()
        except BrokenPipeError:
            pass
        proc.wait(timeout=60)

        # Attribute findings to paths, and count each blob once.
        counted = set()
        for sha, path in candidates:
            text = body.get(sha)
            if text is None:
                continue
            if sha not in counted:
                counted.add(sha)
                scanned += 1
                hits = gate.scan_text(text, blocked, round_scope, path, allowed)
                for _path, _line, rule in hits:
                    flagged[rule] += 1
                if hits:
                    seen[sha] = (path, sorted({r for _p, _l, r in hits}))
                del body[sha]                   # keep the footprint flat on long histories

    flagged_blobs = {sha: v for sha, v in seen.items() if isinstance(v, tuple)}
    report = {
        'clone_shallow_or_partial': shallow,
        'refs_reachable': len(refs),
        'commits_reachable': commits,
        'unique_text_blobs_scanned': scanned,
        'flagged_blobs': len(flagged_blobs),
        'findings_by_rule': dict(flagged),
        'blocked_hash_count': len(blocked),
        'note': ('Counts only. Matched text is never printed. A clean report from a shallow or '
                 'partial clone is not a statement about the remote repository’s history.'),
    }
    if args.json:
        print(json.dumps(report, indent=1))
    else:
        print(f"refs reachable: {report['refs_reachable']}   commits reachable: {commits}   "
              f"clone shallow or partial: {str(shallow).lower()}")
        print(f"unique text blobs scanned: {scanned}   flagged blobs: {len(flagged_blobs)}")
        if flagged:
            print('findings by rule: ' + ', '.join(f'{k}×{v}' for k, v in sorted(flagged.items())))
        else:
            print('findings by rule: none in these objects')
        if flagged_blobs:
            print(f'\nflagged paths (up to {args.max_paths}; the path is printed, the content never is):')
            for i, (sha, (path, rules)) in enumerate(sorted(flagged_blobs.items(), key=lambda kv: str(kv[1]))):
                if i >= args.max_paths:
                    print(f'  … {len(flagged_blobs) - i} more')
                    break
                print(f'  {path} · {", ".join(rules)} · blob {sha[:10]}')
        if shallow or commits <= 2:
            print('\nLIMIT. This clone does not hold the repository’s full history '
                  f'({"shallow marker present" if shallow else "only " + str(commits) + " commit(s) reachable"}). '
                  'Nothing here can show whether an earlier commit, an unfetched branch or a '
                  'pull-request ref still carries material the current tree no longer does. '
                  'Re-run against a `git clone --mirror` of the remote to get that answer, and '
                  'remember that GitHub caches, forks and outside clones are outside any local audit.')
        else:
            print('\nThis audit covers every object reachable from the refs in this clone. It does '
                  'not cover GitHub’s caches, forks, or pull-request refs that were never fetched.')
    return 1 if (args.strict and flagged_blobs) else 0


if __name__ == '__main__':
    sys.exit(main())
