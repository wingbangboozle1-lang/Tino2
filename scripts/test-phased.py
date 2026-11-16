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

# ---------------------------------------------------------------- 16 Nov 2026 additions
# Recovery shapes. 'trend' and 'peak' must agree until the trough: the shape changes only the
# recovery, so a difference in the decline leg would mean the calibration drifted.
for t in ('1929', '2008'):
    n = M.TEMPLATES[t]['months']
    for rec in M.RECOVERY.values():
        a = M.index_path(t, rec, M.HORIZON, 'trend')
        b = M.index_path(t, rec, M.HORIZON, 'peak')
        ok(all(abs(a[m] - b[m]) < 1e-12 for m in range(n + 1)), f'{t}: decline leg is shape-independent')
# The 'peak' shape reaches the pre-crash level exactly at the recorded/assumed regain month.
ok(abs(M.index_path('2008', 0.04, M.HORIZON, 'peak')[M.PEAK_REGAIN['2008']] - 1.0) < 1e-9,
   '2008 peak shape regains the prior level at month 66')
_long = M.index_path('1929', 0.04, M.PEAK_REGAIN['1929'], 'peak')
ok(abs(_long[M.PEAK_REGAIN['1929']] - 1.0) < 1e-9, '1929 peak shape regains the prior level at month 303')
ok(_long[M.HORIZON] < 0.25 and _long[M.HORIZON] > 0.2,
   '1929 peak shape is still well below the prior level ten years after the entry')
ok(len(M.PARK_PATHS) == 4 and all(v['quarters'] for v in M.PARK_PATHS.values()), 'four named parking paths')
ok(all(abs(y - M.BILL_START) < 1e-12 for y in M.bill_path('flat', 60)), 'flat path is the observed bill rate throughout')
ok(M.bill_path('crash-1929', 48)[11] == M.BILL_START and M.bill_path('crash-1929', 48)[12] == 0.01,
   '1929 parking path holds the observed rate for four quarters then uses the engine rate')
# A ladder fully in the two-year note cannot reprice inside a wait no longer than its term:
# that is the whole point of the note leg, and the published table shows it as one repeated number.
for kind in M.PARK_PATHS:
    for park in (24,):
        path = M.ladder_path(park, 1.0, kind, 36)
        ok(all(abs(y - M.NOTE_LOCK) < 1e-12 for y in path[:park]),
           f'note-only parking is insensitive to the bill path within the note term ({kind})')
# A constant path and the flat yield argument must give the same simulation, or the two published
# tables would disagree for a reason nobody stated.
for t in M.TEMPLATES:
    for k in M.STRATEGIES:
        flat = M.simulate(t, k, M.YIELDS['base'], 0.04)['value_end']
        listed = M.simulate(t, k, 0.0, 0.04, cash_path=[M.YIELDS['base']] * M.HORIZON)['value_end']
        ok(abs(flat - listed) < 1e-6, f'{t}/{k}: constant path equals the flat yield')
# Independent arithmetic for the parking table the guide publishes: compound each month of the
# ladder by hand and compare with the model's realised-yield read.
for weight in (0.0, 0.5, 1.0):
    for kind in M.PARK_PATHS:
        for park in (24, 36):
            path = M.ladder_path(park, weight, kind, park)
            factor = 1.0
            for rate in path:
                factor *= (1.0 + rate) ** (1.0 / 12.0)
            res = M.simulate('none', 'park_24' if park == 24 else 'park_36', M.YIELDS['base'], 0.04,
                             cash_path=path)
            ok(abs(res['park_value_at_deploy'] - M.PRINCIPAL * factor) < 1e-6,
               f'parked value at deployment, {weight}/{kind}/{park}')
            ok(abs(res['realized_park_yield'] - (factor ** (12.0 / park) - 1.0)) < 1e-12,
               f'realised parking yield, {weight}/{kind}/{park}')
# Under-water reading: a peak entry into the 1929 record stays below the amount put in for the
# whole ten-year window; a 36-month park into the same record never goes below it at all.
for rec in M.RECOVERY.values():
    peak_now = M.simulate('1929', 'sell_now_all', M.YIELDS['base'], rec, shape='peak')
    ok(peak_now['under_water_months'] == M.HORIZON, '1929 peak entry is under water for all 120 months')
    ok(peak_now['break_even_month'] is None, '1929 peak entry does not break even inside the window')
    wait = M.simulate('1929', 'park_36', M.YIELDS['base'], rec, shape='peak',
                      cash_path=M.ladder_path(36, 0.5, 'crash-1929', M.HORIZON))
    ok(wait['under_water_months'] == 0, 'park-36 with a ladder is never marked below the amount put in')
    ok(wait['value_end'] > peak_now['value_end'], 'parking and phasing ends above the peak entry in a 1929 shape')
ok(M.simulate('1929', 'cash_only', M.YIELDS['base'], 0.04, shape='peak')['value_end']
   < M.simulate('1929', 'park_36', M.YIELDS['base'], 0.04, shape='peak',
                cash_path=M.ladder_path(36, 0.5, 'crash-1929', M.HORIZON))['value_end'],
   'waiting in Treasuries then phasing beats waiting in Treasuries alone in a 1929 shape')
# A rejected shape name must fail loudly rather than be read as 'trend'.
try:
    M.index_path('1929', 0.04, 12, 'sine')
    ok(False, 'unknown recovery shape must raise')
except ValueError:
    ok(True, 'unknown recovery shape raises')

print(f'PASS: phased model reproduced by an independent tranche reconstruction; {checks} checks.')
