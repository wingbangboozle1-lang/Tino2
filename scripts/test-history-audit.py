#!/usr/bin/env python3
"""Regression test for the history-audit instrument itself.

The defect this test exists for
--------------------------------
``docs/history-remediation-runbook.md`` §2 told the administrator to audit the remote
history with ``git clone --mirror``. A mirror clone is **bare**: it has no working tree.
``scripts/privacy-scrub.py``'s ``official_amounts()`` read its four allowlist inputs only
from the filesystem, so in a mirror it returned an empty set. The allowlist is the list of
amounts a government body publishes, which are allowed to stay exact; without it the
ROUNDING rule fired on officially published figures and the audit reported nine paths as
"still the blob at HEAD" that were in fact clean at HEAD.

A tool that measures the wrong thing in the exact environment it is documented to run in is
worse than no tool, because the administrator is deciding whether to rewrite a public
history on the strength of the report. This test pins the two properties that matter:

  1. the allowlist resolves identically in a checkout and in a bare mirror of the same
     repository, and is not empty when the ledger exists;
  2. when an allowlist input genuinely cannot be resolved, the audit says so instead of
     reporting a clean result.

Everything here is synthetic: a throwaway repository in a temporary directory, figures
that are not household values, and no identifier of any kind.
"""
import importlib.util
import json
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(args, cwd):
    return subprocess.run(args, cwd=cwd, capture_output=True, text=True)


def make_fixture(tmp):
    """A tiny repository whose allowlist inputs hold one officially published amount."""
    repo = tmp / "fixture"
    (repo / "integration" / "ledger").mkdir(parents=True)
    (repo / "guide" / "figures").mkdir(parents=True)
    (repo / "scripts").mkdir(parents=True)
    (repo / "integration" / "ledger" / "official_amounts.txt").write_text("1,234,560\n", encoding="utf8")
    (repo / "integration" / "ledger" / "facts.jsonl").write_text(
        json.dumps({"id": "X", "official_exact": "$7,770,000"}) + "\n", encoding="utf8")
    (repo / "guide" / "figures" / "official-figures.json").write_text(
        json.dumps({"figures": [{"id": "Y", "claim": "$15,480,000"}]}), encoding="utf8")
    (repo / "scripts" / "test-guide.cjs").write_text(
        "const OFFICIAL_AMOUNTS=new Map([\n  [1000, 'x'],\n]);\n", encoding="utf8")
    shutil.copy(ROOT / "scripts" / "privacy-scrub.py", repo / "scripts" / "privacy-scrub.py")
    run(["git", "init", "-q", "-b", "main"], repo)
    run(["git", "config", "user.email", "test-user@invalid"], repo)
    run(["git", "config", "user.name", "Test"], repo)
    run(["git", "add", "-A"], repo)
    run(["git", "commit", "-q", "-m", "fixture"], repo)
    return repo


def allowlist_size_in(root):
    """Resolve the allowlist with the scrubber's own loader, rooted at a given repository."""
    scrubber = load(ROOT / "scripts" / "privacy-scrub.py", "scrubber_under_test")
    scrubber.ROOT = Path(root)
    return len(scrubber.official_amounts())


def main():
    tmp = Path(tempfile.mkdtemp(prefix="history-audit-test-"))
    failures = []
    try:
        repo = make_fixture(tmp)

        # 1. a checkout resolves the allowlist
        checkout_size = allowlist_size_in(repo)
        if checkout_size < 4:
            failures.append(f"a checkout resolved only {checkout_size} allowlisted amount(s); "
                            "expected the four inputs to be read")

        # 2. a bare mirror of the same repository resolves the same allowlist
        mirror = tmp / "mirror.git"
        proc = run(["git", "clone", "-q", "--mirror", str(repo), str(mirror)], tmp)
        if proc.returncode != 0:
            failures.append("could not make a mirror clone of the fixture")
        else:
            mirror_size = allowlist_size_in(mirror)
            if mirror_size != checkout_size:
                failures.append(
                    f"the allowlist resolves to {checkout_size} amount(s) in a checkout but "
                    f"{mirror_size} in a bare mirror of the same repository — the instrument "
                    "measures different things in the environment the runbook documents")

        # 3. an allowlist input that genuinely cannot be resolved must be reported, not hidden
        empty = tmp / "empty"
        (empty / "scripts").mkdir(parents=True)
        run(["git", "init", "-q", "-b", "main"], empty)
        run(["git", "config", "user.email", "test-user@invalid"], empty)
        run(["git", "config", "user.name", "Test"], empty)
        run(["git", "commit", "-q", "--allow-empty", "-m", "empty"], empty)
        scrubber = load(ROOT / "scripts" / "privacy-scrub.py", "scrubber_probe")
        scrubber.ROOT = empty
        if scrubber.repo_text("guide/figures/official-figures.json") is not None:
            failures.append("repo_text() returned content for a path that does not exist")
        else:
            missing = [n for n in ("scripts/official-amounts.txt",
                                   "integration/ledger/official_amounts.txt",
                                   "integration/ledger/facts.jsonl",
                                   "guide/figures/official-figures.json",
                                   "scripts/test-guide.cjs")
                       if scrubber.repo_text(n) is None]
            if len(missing) != 5:
                failures.append(f"repo_text() resolved {5 - len(missing)} of 5 absent inputs; "
                                "expected every absent input to be reported as absent")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)

    if failures:
        for line in failures:
            print("FAIL:", line)
        return 1
    print("PASS: the official-amount allowlist resolves identically in a checkout and in a bare "
          "mirror, and an unresolvable input is reported as unresolvable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
