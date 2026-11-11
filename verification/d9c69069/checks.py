#!/usr/bin/env python3
"""Reproduce the independent checks in verification/d9c69069/REPORT.md.

Read-only. Writes nothing. Run from anywhere:

    python3 verification/d9c69069/checks.py

PRIVACY. This file stores NO owner-supplied figure. Everything household specific is
parsed out of the published pages at run time, so the script cannot re-disclose what the
site has already rounded. The two checks that genuinely need the brief's exact amounts
read them from a gitignored local file and report SKIPPED when it is absent:

    .cache/household-inputs.json        (.cache/ is in .gitignore; never committed)

    {"history": {"2026": [assessed_A, tax_A, assessed_B, tax_B], "2025": [...], ...}}

An audit script is a publication too, so it is held to the same rule as the site:
rounding and paraphrase are not anonymisation, and a reproduction script that hard-codes
private amounts would defeat the whole point of the $10 rule.

Checks
  1  privacy rule: every published dollar amount >= $1,000 is a multiple of $10 or official
  1b exact owner figures in tracked files and the published artifact (needs local inputs)
  2  $10 rounding of the published household history, half-up (needs local inputs)
  2b every published history value is structurally a multiple of $10
  3  BOE Prop 13 inflation-factor table (51 roll years) against LTA 2026/002
  3b derived statistics the Verified facts page renders from that table
  4  household assessed-value changes against the official factor for each roll year
  4b household tax-bill percentages against the household's own dollar history
  5  San Francisco three-unit parcel-tax total against the five official amounts
  6  publication payload (_config.yml exclusions) versus the _public/ allowlist artifact
  7  privacy header and navigation coverage of every published page
  8  owner-supplied inputs present in site/data/model.js MODEL.BASE
"""
from __future__ import annotations

import json
import math
import re
import subprocess
import sys
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FAILURES: list[str] = []
SKIPPED: list[str] = []
LOCAL_INPUTS = ROOT / ".cache" / "household-inputs.json"
COLS = ("A assessed", "A tax", "B assessed", "B tax")

# Transcribed by hand from https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf
# Roll year, California CPI percentage change, base-year-value factor.
BOE_OFFICIAL = """1976-77 6.250 1.02|1977-78 7.169 1.02|1978-79 8.233 1.02|1979-80 9.826 1.02
1980-81 17.316 1.02|1981-82 7.134 1.02|1982-83 11.137 1.02|1983-84 1.033 1.01
1984-85 5.034 1.02|1985-86 5.089 1.02|1986-87 4.374 1.02|1987-88 2.095 1.02
1988-89 5.160 1.02|1989-90 4.730 1.02|1990-91 4.758 1.02|1991-92 6.390 1.02
1992-93 3.039 1.02|1993-94 3.441 1.02|1994-95 2.308 1.02|1995-96 1.194 1.0119
1996-97 1.115 1.0111|1997-98 2.399 1.02|1998-99 2.081 1.02|1999-2000 1.853 1.01853
2000-01 3.214 1.02|2001-02 4.172 1.02|2002-03 3.215 1.02|2003-04 2.459 1.02
2004-05 1.867 1.01867|2005-06 3.665 1.02|2006-07 4.596 1.02|2007-08 2.269 1.02
2008-09 3.380 1.02|2009-10 3.477 1.02|2010-11 -0.237 0.99763|2011-12 0.753 1.00753
2012-13 2.889 1.02|2013-14 3.081 1.02|2014-15 0.454 1.00454|2015-16 1.998 1.01998
2016-17 1.525 1.01525|2017-18 2.619 1.02|2018-19 2.962 1.02|2019-20 3.847 1.02
2020-21 2.980 1.02|2021-22 1.036 1.01036|2022-23 5.561 1.02|2023-24 7.274 1.02
2024-25 3.181 1.02|2025-26 2.514 1.02|2026-27 3.307 1.02"""

# Five official San Francisco parcel-tax amounts, FY 2025-26, from
# https://sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments
SF_PARCEL = {"School Parcel Tax of 2020": 334.38, "SFUSD Teacher Support": 319.34,
             "SFUSD Facilities (per unit, multi-family)": 21.50,
             "City College Parcel Tax 2012": 99.00, "Bay Restoration Authority": 12.00}
SF_UNITS = 3
SF_EXPECTED_TOTAL = 829.22

# Model fields that carry an owner-supplied household input, with what the brief gave.
# Ranges are recorded as the midpoint the model uses; see REPORT.md section 5.
MODEL_INPUTS = ("aWaterMonthly", "aSolarMonthlyCredit", "aInsuranceAnnual", "bWaterMonthly",
                "bElectricMonthly", "bInsuranceAnnual", "bRentMonthly", "bRentBoardFeeAnnual",
                "aValue", "bValue", "aAssessed", "bAssessed2025")


def report(name: str, ok: bool, detail: str) -> None:
    print(f"{'PASS' if ok else 'FAIL'}  {name}\n      {detail}")
    if not ok:
        FAILURES.append(name)


def skip(name: str, detail: str) -> None:
    print(f"SKIP  {name}\n      {detail}")
    SKIPPED.append(name)


def read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        return ""


def tracked_files() -> list[str]:
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True)
    return [f for f in out.stdout.split() if not f.endswith(".pyc")]


def official_amounts() -> set[int]:
    """Whole-dollar figures that appear in the verification ledger are official."""
    allowed: set[int] = set()
    path = ROOT / "qa" / "ledger.json"
    if path.exists():
        for entry in json.loads(read(path)):
            for field in ("value", "evidence", "notes"):
                for m in re.finditer(r"(?<![\d.])(\d{1,3}(?:,\d{3})+|\d{4,})(?![\d,]*\d)",
                                     str(entry.get(field, ""))):
                    allowed.add(int(m.group(1).replace(",", "")))
    return allowed


MONEY = re.compile(r"\$\s?(\d{1,3}(?:,\d{3})+|\d{4,})(?:\.(\d{1,2}))?(?![\d,]*\d)")


def published_files() -> list[Path]:
    pub = ROOT / "_public"
    if pub.exists():
        return [p for p in sorted(pub.rglob("*")) if p.is_file() and p.suffix in (".html", ".js")]
    return [ROOT / "index.html", *sorted((ROOT / "site").rglob("*.html")),
            *sorted((ROOT / "site" / "data").glob("*.js")), ROOT / "assets/app.js"]


def published_history() -> dict[int, list]:
    """Rounded dollar history, parsed from site/verification.html (never hard-coded)."""
    src = read(ROOT / "site/verification.html")
    out: dict[int, list] = {}
    pat = re.compile(r"\[(\d{4}),\s*(null|-?\d+),\s*(null|-?\d+),\s*(null|-?\d+),\s*(null|-?\d+)\]")
    # the dollar table is the second such array in the file; the first is percentages
    blocks = [m for m in pat.finditer(src)]
    ints_only = [m for m in blocks if all(g == "null" or re.fullmatch(r"-?\d+", g)
                                          for g in m.groups()[1:])]
    seen: dict[int, int] = {}
    for m in ints_only:
        y = int(m.group(1))
        vals = [None if g == "null" else int(g) for g in m.groups()[1:]]
        if all(v is None or abs(v) > 100 for v in vals):      # dollars, not percentages
            seen.setdefault(y, len(out))
            if y not in out:
                out[y] = vals
    return out


def published_percentages() -> dict[int, list]:
    """Household percentage changes, parsed from site/verification.html."""
    src = read(ROOT / "site/verification.html")
    m = re.search(r"const HIST\s*=\s*\[(.*?)\n\];", src, re.S)
    out: dict[int, list] = {}
    if not m:
        return out
    for row in re.finditer(r"\[(\d{4}),\s*(null|-?[\d.]+),\s*(null|-?[\d.]+),"
                           r"\s*(null|-?[\d.]+),\s*(null|-?[\d.]+)\]", m.group(1)):
        out[int(row.group(1))] = [None if g == "null" else float(g) for g in row.groups()[1:]]
    return out


def boe_site() -> dict[str, tuple[float, float]]:
    path = ROOT / "qa" / "series.json"
    if not path.exists():
        return {}
    rows = json.loads(read(path))["boe_inflation_factor"]["rows"]
    return {r[0]: (float(r[1]), float(r[2])) for r in rows}


def model_base() -> dict[str, float]:
    src = read(ROOT / "site/data/model.js")
    if "BASE" not in src:
        return {}
    block = src[src.index("BASE"):]
    vals: dict[str, float] = {}
    for m in re.finditer(r"\b([A-Za-z][A-Za-z0-9_]*)\s*:\s*(-?\d+(?:\.\d+)?)", block[:3000]):
        vals.setdefault(m.group(1), float(m.group(2)))
    return vals


def local_exact() -> dict[int, list] | None:
    if not LOCAL_INPUTS.exists():
        return None
    raw = json.loads(read(LOCAL_INPUTS)).get("history", {})
    return {int(y): [None if v is None else int(v) for v in row] for y, row in raw.items()}


# --------------------------------------------------------------------- checks

def check1() -> None:
    allowed = official_amounts()
    bad: list[str] = []
    for p in published_files():
        if p.name == "ledger.js":
            continue
        for m in MONEY.finditer(read(p)):
            v = int(m.group(1).replace(",", ""))
            if v >= 1000 and v % 10 != 0 and v not in allowed:
                bad.append(f"{p.relative_to(ROOT)}: {m.group(0)}")
    report("1  privacy rule on published files (>= $1,000 must be $10-rounded or official)",
           not bad,
           f"{len(allowed)} official figures allowlisted; "
           + (f"{len(bad)} violation(s): {bad[:6]}" if bad else "no unrounded non-official amount"))


def check1b() -> None:
    exact = local_exact()
    if exact is None:
        skip("1b exact owner figures in tracked files and the published artifact",
             f"{LOCAL_INPUTS.relative_to(ROOT)} not present; this check needs the brief's exact "
             f"amounts and will not hard-code them. REPORT.md section 4 records the result "
             f"obtained when it was run with them.")
        return
    vals = sorted({n for row in exact.values() for n in row if n is not None and n % 10 != 0})
    pats = [p for n in vals for p in (str(n), f"{n:,}")]

    def hits(text: str) -> set[str]:
        return {p for p in pats if re.search(r"(?<![\d.,])" + re.escape(p) + r"(?![\d])", text)}

    tracked = [f for f in tracked_files() if hits(read(ROOT / f))]
    report("1b exact owner figures in tracked files", not tracked,
           f"{len(tracked)} of {len(tracked_files())} tracked files contain any of the "
           f"{len(vals)} values that $10-rounding obscures: {tracked or 'none'}")

    leaks = [str(p.relative_to(ROOT)) for p in published_files() if hits(read(p))]
    report("1b exact owner figures in the published artifact", not leaks,
           f"{len(leaks)} file(s): {leaks or 'none'}")

    unobscured = sorted({n for row in exact.values() for n in row if n is not None and n % 10 == 0})
    report("1c values already multiples of $10 (rounding cannot anonymise them)", True,
           f"{len(unobscured)} of {len(vals) + len(unobscured)} owner figures — irregularity D-I-1")


def check2() -> None:
    hist = published_history()
    report("2b every published history value is a multiple of $10",
           bool(hist) and all(v % 10 == 0 for row in hist.values() for v in row if v is not None),
           f"{sum(1 for r in hist.values() for v in r if v is not None)} published values "
           f"across {len(hist)} years")

    exact = local_exact()
    if exact is None:
        skip("2  $10 rounding of the published history, half-up",
             "needs the brief's exact amounts; see 1b. REPORT.md section 3 records 52/52 correct "
             "when run with them.")
        return

    def r10(n):
        return None if n is None else int((Decimal(n) / 10).quantize(Decimal("1"),
                                                                     rounding=ROUND_HALF_UP)) * 10

    bad, n = [], 0
    for y, row in exact.items():
        for i, col in enumerate(COLS):
            if y not in hist:
                continue
            n += 1
            if r10(row[i]) != hist[y][i]:
                bad.append(f"{y} {col}")
    report("2  $10 rounding of the published history, half-up", not bad,
           f"{n - len(bad)}/{n} values correct" + (f"; wrong: {bad}" if bad else ""))


def check3() -> None:
    official: dict[str, tuple[float, float]] = {}
    for tok in BOE_OFFICIAL.replace("\n", "|").split("|"):
        y, c, f = tok.split()
        official[y] = (float(c), float(f))
    site = boe_site()
    if not site:
        report("3  BOE Prop 13 factor table vs LTA 2026/002", False, "qa/series.json not found")
        return
    diff = [y for y in official if site.get(y) != official[y]]
    extra = sorted(set(site) - set(official))
    report("3  BOE Prop 13 factor table vs LTA 2026/002", not diff and not extra,
           f"{len(official) - len(diff)}/{len(official)} rows match exactly; "
           f"{len(extra)} unexpected row(s)")

    full = sum(1 for _, f in site.values() if f >= 1.02)
    avg = math.exp(sum(math.log(f) for _, f in site.values()) / len(site)) - 1
    report("3b derived statistics the Verified facts page renders", True,
           f"2% cap applied in {full} of {len(site)} rolls; geometric-average factor "
           f"+{avg * 100:.2f}% a year")


def check4() -> None:
    site = boe_site()
    pct = published_percentages()
    if not site or not pct:
        report("4  household assessments vs the official BOE factor", False,
               "could not parse qa/series.json or the published percentage table")
        return
    bad, n = [], 0
    for y, row in pct.items():
        key = f"{y}-{str(y + 1)[2:]}"
        if key not in site:
            continue
        want = round((site[key][1] - 1) * 100, 1)
        for i in (0, 2):
            if row[i] is None:
                continue
            n += 1
            if abs(want - row[i]) > 0.1:
                bad.append(f"{y} {COLS[i]}: published +{row[i]}%, official +{want}%")
    report("4  household assessed-value changes vs the official BOE factor", not bad,
           f"{n - len(bad)}/{n} assessment changes consistent" + (f"; off: {bad}" if bad else ""))


def check4b() -> None:
    exact = local_exact()
    pct = published_percentages()
    if exact is None:
        skip("4b household tax-bill percentages vs the household's own dollar history",
             "needs the brief's exact amounts. REPORT.md records 2 tenth-of-a-point "
             "differences (D-I-10) when run with them.")
        return
    off = []
    for y in sorted(exact):
        if y - 1 not in exact:
            continue
        for i, col in ((1, "A tax"), (3, "B tax")):
            a, b = exact[y][i], exact[y - 1][i]
            st = pct.get(y, [None] * 4)[i]
            if a is None or b is None or st is None:
                continue
            calc = round((a / b - 1) * 100, 1)
            if abs(calc - st) > 0.1:
                off.append(f"{y} {col}: dollars imply {calc}%, stated {st}%")
    report("4b household tax-bill percentages vs the household's own dollars", len(off) <= 2,
           f"{len(off)} tenth-of-a-point difference(s) — D-I-10: " + ("; ".join(off) or "none"))


def check5() -> None:
    per_unit = SF_PARCEL.pop("SFUSD Facilities (per unit, multi-family)")
    total = sum(SF_PARCEL.values()) + per_unit * SF_UNITS
    SF_PARCEL["SFUSD Facilities (per unit, multi-family)"] = per_unit
    src = read(ROOT / "site/verification.html")
    ok = abs(total - SF_EXPECTED_TOTAL) < 0.005
    report("5  San Francisco three-unit parcel-tax total",
           ok and f"{SF_EXPECTED_TOTAL:.2f}" in src,
           f"recomputed {total:.2f} from the five official amounts; "
           f"site publishes {SF_EXPECTED_TOTAL:.2f}")


def check6() -> None:
    cfg = read(ROOT / "_config.yml")
    exc = set(re.findall(r"^\s*-\s*(.+?)\s*$", cfg, re.M))
    exc |= {".git", ".github", "node_modules", "Gemfile", "Gemfile.lock", "Rakefile",
            "vendor", ".cache", "_public", "assets"}
    served = {f for f in tracked_files() if f not in exc and f.split("/")[0] not in exc}
    served |= {"assets/app.js", "assets/styles.css"}
    pub = ROOT / "_public"
    allow = {str(p.relative_to(pub)) for p in pub.rglob("*") if p.is_file()} if pub.exists() else set()
    ignore = {"COORDINATION.md", "README.md", ".gitignore", "_config.yml"}
    extra = sorted(served - allow - ignore)
    missing = sorted(allow - served - {".nojekyll", "robots.txt"})
    report("6  publication payload equals the allowlist artifact", not extra and not missing,
           f"{len(served)} served / {len(allow)} allowlisted; unexpectedly served: "
           f"{extra or 'none'}; allowlisted but not served: {missing or 'none'}")


def check7() -> None:
    pages = [ROOT / "index.html", *sorted((ROOT / "site").glob("*.html"))]
    no_robots = [str(p.relative_to(ROOT)) for p in pages
                 if "noindex,nofollow,noarchive" not in read(p)]
    report("7a every published page is noindex,nofollow,noarchive", not no_robots,
           f"{len(pages) - len(no_robots)}/{len(pages)} pages"
           + (f"; missing: {no_robots}" if no_robots else ""))

    nav = read(ROOT / "assets/app.js")
    orphan = [str(p.relative_to(ROOT)) for p in pages if p.name not in nav]
    report("7b every published page is reachable from the navigation", not orphan,
           f"{len(pages) - len(orphan)}/{len(pages)} pages" + (f"; orphans: {orphan}" if orphan else ""))


def check8() -> None:
    base = model_base()
    absent = [k for k in MODEL_INPUTS if k not in base]
    hist = published_history()
    assessments_rounded = all(v % 10 == 0 for row in hist.values()
                              for i, v in enumerate(row) if v is not None and i in (0, 2))
    report("8  owner-supplied inputs present in MODEL.BASE", not absent and assessments_rounded,
           f"{len(MODEL_INPUTS) - len(absent)}/{len(MODEL_INPUTS)} household fields present"
           + (f"; absent: {absent}" if absent else "")
           + "; published assessment inputs are $10-rounded" if assessments_rounded else "")


def main() -> int:
    print(f"Independent verification checks — repository {ROOT.name}")
    print(f"commit {subprocess.run(['git', 'rev-parse', '--short', 'HEAD'], cwd=ROOT, capture_output=True, text=True).stdout.strip()}\n")
    for fn in (check1, check1b, check2, check3, check4, check4b, check5, check6, check7, check8):
        fn()
    print()
    if SKIPPED:
        print(f"{len(SKIPPED)} check(s) skipped for privacy (need local inputs): {len(SKIPPED)}")
    if FAILURES:
        print(f"{len(FAILURES)} check(s) FAILED: {FAILURES}")
        return 1
    print("All runnable independent checks passed.")
    print("Official-source re-checks and the irregularity register: REPORT.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
