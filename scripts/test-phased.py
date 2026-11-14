#!/usr/bin/env python3
"""Independent check of scripts/phased_model.py.

The model steps month by month. This check reconstructs each end value tranche by
tranche with closed-form yield terms, and asserts invariants. It fails loudly on drift.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import phased_model as M  # noqa: E402

TOL = 1e-6
checks = 0


def ok(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise SystemExit('FAIL: ' + msg)


def independent_end(template, strategy, y, rec):
    s = M.STRATEGIES[strategy]
    idx = M.index_path(template, rec)
    H = M.HORIZON
    P = M.PRINCIPAL
    now = P * s['now']
    R = P - now
    park, D = s['park'], s['deploy']
    value = now * idx[H] / idx[0]
    value += R * (1 + y) ** (H / 12)           # all parked dollars earn yield
    if D:
        tranche = R * (1 + y) ** (park / 12) / D  # amount fixed at the parking date
        for k in range(1, D + 1):
            t = park + k
            value += tranche * idx[H] / idx[t]     # shares bought at t, held to H
            value -= tranche * (1 + y) ** ((H - t) / 12)  # yield forgone on that tranche
    return value


for template in M.TEMPLATES:
    for rec in M.RECOVERY.values():
        for sk in M.STRATEGIES:
            for y in M.YIELDS.values():
                got = M.simulate(template, sk, y, rec)['value_end']
                want = independent_end(template, sk, y, rec)
                ok(abs(got - want) <= TOL * max(1.0, abs(want)), f'{template}/{sk}/{y}/{rec}: {got} != {want}')

# Template anchors: the calibrations the guide cites.
ok(abs(M.index_path('1929', 0.04)[34] - 0.11) < 1e-12, '1929 trough is 11% of peak (89% decline)')
ok(abs(M.index_path('2008', 0.04)[17] - 0.43) < 1e-12, '2008 trough is 43% of peak (57% decline)')
ok(all(abs(M.index_path('none', r)[0] - 1.0) < 1e-12 for r in M.RECOVERY.values()), 'no-crash path starts at peak')

# Invariants.
for rec in M.RECOVERY.values():
    cash = M.simulate('2008', 'cash_only', M.YIELDS['base'], rec)['value_end']
    ok(abs(cash - M.PRINCIPAL * (1 + M.YIELDS['base']) ** (M.HORIZON / 12)) < 1e-6, 'cash-only equals compounding at the stated yield')
    ok(M.simulate('2008', 'park_36', M.YIELDS['base'], rec)['value_36'] == M.simulate('2008', 'cash_only', M.YIELDS['base'], rec)['value_36'],
       'park-36 holds only cash through month 36')
    for t in ('1929', '2008'):
        a = M.simulate(t, 'sell_now_all', M.YIELDS['base'], rec)
        ok(a['worst_36'] <= a['value_36'] + 1e-9, 'worst point cannot exceed month-36 value by construction')
        ok(a['worst_36'] < M.PRINCIPAL, 'invest-now loses money at the trough in a crash template')
for t in ('1929', '2008'):
    ok(M.simulate(t, 'park_24', M.YIELDS['base'], 0.04)['worst_36'] >= M.simulate(t, 'sell_now_all', M.YIELDS['base'], 0.04)['worst_36'],
       'phasing softens the worst point in a crash entry')
# Reinvestment sensitivity: higher parking yield can only raise the parked-cash result.
for t in M.TEMPLATES:
    v = [M.simulate(t, 'park_24', y, 0.04)['value_end'] for y in (M.YIELDS['low'], M.YIELDS['base'], M.YIELDS['high'])]
    ok(v[0] <= v[1] <= v[2], 'end value rises with the parking yield')

# Known structural result, disclosed on the page: the template recovers from its trough at a constant rate,
# so tranches bought after the trough (2008: month 17) grow exactly like the no-crash path. The 2008 park-24
# result therefore equals the no-crash park-24 result. The check fails if the model changes this silently.
for rec in (0.04, 0.08):
    ok(abs(M.simulate('2008', 'park_24', M.YIELDS['base'], rec)['value_end'] - M.simulate('none', 'park_24', M.YIELDS['base'], rec)['value_end']) < 1e-6,
       'post-trough tranches share the no-crash growth path (2008, park 24)')
# A 1929 park-24 result must differ, because its tranches are bought before the trough at month 34.
ok(abs(M.simulate('1929', 'park_24', M.YIELDS['base'], 0.04)['value_end'] - M.simulate('none', 'park_24', M.YIELDS['base'], 0.04)['value_end']) > 1000,
   '1929 park-24 differs from the no-crash control (purchases before the trough)')

print(f'PASS: phased model reproduced by an independent tranche reconstruction; {checks} checks.')
