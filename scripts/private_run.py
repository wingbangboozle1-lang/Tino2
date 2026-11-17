#!/usr/bin/env python3
"""Run the decision engine on PRIVATE household inputs and write the results to private/.

Nothing this script reads or writes is committed: the inputs file and every output live in
the git-ignored private/ folder. The script contains no household figures.

Input file: private/inputs.json (see the schema in the docstring of load_inputs()).
  * Every dollar input is rounded to the nearest $10 before use (the brief's rule).
  * A value given as [low, high] is run as three cases (low, mid, high) so that the
    result is shown as a range, not a point.
  * A value that is missing, or marked "unverified", is NOT filled in: the dependent
    path is reported as a floor / not computed, and the report says why.

Outputs (private/): run-summary.md, property-a-annual.csv, property-b-annual.csv.
Run:  python3 scripts/private_run.py
"""
from __future__ import annotations

import csv
import json
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import analysis_model as M  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
PRIVATE = ROOT / 'private'
INPUTS = PRIVATE / 'inputs.json'
HORIZONS = (10, 25, 50)
CASE_NAMES = ('low', 'mid', 'high')


def r10(x: float) -> int:
    """Round a dollar amount to the nearest $10 (half away from zero)."""
    q = math.floor(abs(x) / 10.0 + 0.5) * 10
    return int(q) if x >= 0 else -int(q)


def money(x) -> str:
    if x is None:
        return 'not computed'
    return ('−' if x < 0 else '') + '$' + f'{r10(abs(x)):,}'


def cases(value):
    """Return (low, mid, high) for a scalar or a [low, high] range; None if missing."""
    if value is None:
        return None
    if isinstance(value, (list, tuple)):
        lo, hi = float(value[0]), float(value[1])
        return (lo, (lo + hi) / 2.0, hi)
    v = float(value)
    return (v, v, v)


def load_inputs() -> dict:
    """Schema (all keys optional unless noted; amounts in whole dollars):

    {
      "property_a": {                       # the inherited home (live / rent / sell paths)
        "fmv_now": 0, "assessed_2025": 0, "assessed_2026": 0, "tax_2025": 0,
        "insurance_yr": 0, "water_mo": [lo, hi], "solar_credit_mo": [lo, hi],
        "market_rent_mo": null,              # null = not supplied -> rent paths are a floor
        "status": {"fmv": "owner estimate, unverified", ...}
      },
      "property_b": {                       # the house the heir already owns (constant across paths)
        "fmv_now": 0, "assessed_2025": 0, "tax_2025": 0, "rent_mo": 0,
        "water_mo": [lo, hi], "elec_mo": [lo, hi], "insurance_yr": 0
      },
      "params": {}                          # optional overrides of analysis_model.DEFAULT_PARAMS
    }
    """
    if not INPUTS.exists():
        sys.exit(f'Missing {INPUTS.relative_to(ROOT)}: create it from the schema in this script. '
                 'The file is git-ignored and is never published.')
    return json.loads(INPUTS.read_text())


def build(raw: dict, idx: int):
    """Build (a, b, p) for case index idx (0 low, 1 mid, 2 high)."""
    pa, pb = raw.get('property_a', {}), raw.get('property_b', {})
    p = dict(M.DEFAULT_PARAMS)
    p.update(raw.get('params', {}))

    def pick(v, default=0.0):
        c = cases(v)
        return default if c is None else c[idx]

    a = {'label': 'A',
         'fmv_now': r10(pick(pa.get('fmv_now'))),
         'assessed_2025': r10(pick(pa.get('assessed_2025'))),
         'assessed_2026': r10(pick(pa.get('assessed_2026'))),
         'tax_2025': r10(pick(pa.get('tax_2025'))),
         'insurance_yr': r10(pick(pa.get('insurance_yr'))),
         'water_mo': r10(pick(pa.get('water_mo'))),
         'solar_credit_mo': r10(pick(pa.get('solar_credit_mo'))) }
    mr = pa.get('market_rent_mo')
    p['rent_mo'] = float(r10(mr)) if mr is not None else 0.0
    b = {'label': 'B',
         'fmv_now': r10(pick(pb.get('fmv_now'))),
         'assessed_2025': r10(pick(pb.get('assessed_2025'))),
         'tax_2025': r10(pick(pb.get('tax_2025'))),
         'rent_mo': r10(pick(pb.get('rent_mo'))),
         'water_mo': r10(pick(pb.get('water_mo'))),
         'elec_mo': r10(pick(pb.get('elec_mo'))),
         'insurance_yr': r10(pick(pb.get('insurance_yr'))) }
    return a, b, p


def write_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    with path.open('w', newline='') as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
        w.writeheader()
        for r in rows:
            w.writerow({k: (r10(v) if isinstance(v, float) and k not in ('year', 'year_offset') else v)
                        for k, v in r.items()})


def self_test() -> int:
    """Checks that need no household inputs: rounding, ranges and the missing-input refusal."""
    assert r10(12345) == 12350 and r10(15) == 20 and r10(14.9) == 10
    assert r10(-1234.5) == -1230 and money(None) == 'not computed' and money(-4444) == '−$4,440'
    assert cases(None) is None and cases(5) == (5.0, 5.0, 5.0) and cases([100, 150]) == (100.0, 125.0, 150.0)
    a, b, p = build({'property_a': {'fmv_now': 1000, 'water_mo': [100, 150]}}, 0)
    assert a['water_mo'] == 100 and p['rent_mo'] == 0.0            # missing rent = floor, not an estimate
    a2, _, _ = build({'property_a': {'water_mo': [100, 150]}}, 2)
    assert a2['water_mo'] == 150
    print('PASS: private_run self-test (rounding, ranges, missing-input handling).')
    return 0


def main() -> int:
    raw = load_inputs()
    PRIVATE.mkdir(exist_ok=True)
    lines = ['# Private run summary (not for publication)', '',
             'Generated by `scripts/private_run.py`. Every dollar figure is rounded to the nearest $10.',
             'Low / mid / high are the endpoints and midpoint of each range input. A path with no',
             'supplied market rent is a floor (rent set to $0), not an estimate.', '']
    missing = []
    for key in ('fmv_now', 'assessed_2025', 'assessed_2026', 'tax_2025', 'insurance_yr', 'water_mo',
                'solar_credit_mo', 'market_rent_mo'):
        v = raw.get('property_a', {}).get(key)
        if v is None:
            missing.append(f'Property A {key}')
    if raw.get('property_a', {}).get('status'):
        for k, s in raw['property_a']['status'].items():
            lines.append(f'- Property A `{k}`: {s}')
        lines.append('')

    results = {}
    for idx, case in enumerate(CASE_NAMES):
        a, b, p = build(raw, idx)
        results[case] = M.grid(a, p, HORIZONS)
        if idx == 1:
            mid_a, mid_b, mid_p = a, b, p
            lines += ['## Mid case: total wealth by path, 25 years, baseline scenario', '',
                      '| Path | Total wealth (rounded to $10) |', '|---|---|']
            for path in M.PATHS:
                lines.append(f'| {M.PATH_LABEL[path]} | {money(results[case]["results"][("base", 25, path)]["total"])} |')
            lines.append('')
            lines += ['## Mid case: best and worst scenario per path, by horizon', '',
                      '| Horizon | Path | Best scenario | Worst scenario | Max regret (rounded) |', '|---|---|---|---|---|']
            for h in HORIZONS:
                s = results[case]['summary'][h]
                for path in M.PATHS:
                    vals = {sc: results[case]['results'][(sc, h, path)]['total'] for sc in M.SCENARIOS}
                    best = max(vals, key=vals.get)
                    worst = min(vals, key=vals.get)
                    lines.append(f'| {h} y | {M.PATH_LABEL[path]} | {M.SCENARIO_LABEL[best]} '
                                 f'({money(vals[best])}) | {M.SCENARIO_LABEL[worst]} ({money(vals[worst])}) | '
                                 f'{money(s["max_regret"][path])} |')
            lines.append('')
            write_csv(PRIVATE / 'property-a-annual.csv',
                      M.annual_table(mid_a, mid_p, 50))
            write_csv(PRIVATE / 'property-b-annual.csv',
                      [M.prop_b_year(mid_b, mid_p, t) for t in range(0, 51)])
            lines += ['## Estate-tax headroom (donor estate, mid case)', '']
            eh = M.estate_headroom(mid_a, mid_p)
            lines.append(f'- Federal basic exclusion at inheritance (assumed indexing, see below): {money(eh["exclusion"])}; Property A value at '
                         f'inheritance: {money(eh["house_fmv"])}; headroom for other assets: '
                         f'{money(eh["other_assets_headroom"])}. The 2026 ($15,000,000) and 2027 ($15,480,000) '
                         f'exclusions are official (IRS); the value for the inheritance year is an indexing '
                         f'ASSUMPTION carried from 2027.')
            lines.append('')
            lines += ['## What would change the ranking (mid case, 25 years, baseline)', '']
            be_eq = M.breakeven_equity(mid_a, mid_p, 25, 'base')
            be_g = M.breakeven_growth(mid_a, mid_p, 25, 'base', 'sell_phased')
            eq_txt = 'not found in search range' if be_eq is None else '%.1f%% a year' % (be_eq * 100)
            g_txt = 'not found in search range' if be_g is None else '%.1f%% a year' % (be_g * 100)
            mu_txt = '%.1f%%' % (mid_p['mu_equity'] * 100)
            gp_txt = '%.1f%%' % (mid_p['g_post'] * 100)
            lines.append('- Equity return at which phasing into stocks and living in the house tie: '
                         + eq_txt + ' (mid case assumes ' + mu_txt + ').')
            lines.append('- Home-price growth after inheritance at which living and selling tie: '
                         + g_txt + ' (mid case assumes ' + gp_txt + ').')
            lines.append('- The ranking is conditional on these assumptions; the ones marked ASSUMPTION in analysis_model.py are not official.')
            lines.append('')
            lines += ['## Range check: the same 25-year baseline total at the low and high cases', '',
                      '| Path | Low case | Mid case | High case |', '|---|---|---|---|']
    for path in M.PATHS:
        row = [M.PATH_LABEL[path]]
        for case in CASE_NAMES:
            row.append(money(results[case]['results'][('base', 25, path)]['total']))
        lines.append('| ' + ' | '.join(row) + ' |')
    lines.append('')
    if missing:
        lines += ['## Inputs not supplied (not estimated)', ''] + [f'- {m}' for m in missing] + ['']
    (PRIVATE / 'run-summary.md').write_text('\n'.join(lines) + '\n')
    print(f'Wrote {PRIVATE.relative_to(ROOT)}/run-summary.md and two annual CSV files (git-ignored).')
    return 0


if __name__ == '__main__':
    raise SystemExit(self_test() if '--self-test' in sys.argv else main())
