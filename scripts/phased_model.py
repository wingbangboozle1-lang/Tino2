#!/usr/bin/env python3
"""Phased-entry model for proceeds from a sale, with stylised crash templates.

Everything here is an illustration per $100,000 of net proceeds. No household
figure is an input. Crash templates are calibrated only to the official
peak-to-trough declines cited on the public guide; the path between the peak
and the trough is a smooth geometric interpolation, not the index history.
"""
from __future__ import annotations

PRINCIPAL = 100_000  # invented, per-$100,000 illustration

# Official peak-to-trough declines and the months they took.
#   1929: Dow Jones Industrial Average, peak 3 Sep 1929 (381.17) to trough 8 Jul 1932 (41.22),
#         89 percent below its peak; about 34 months.  Source: Federal Reserve History.
#   2008: S&P 500, peak 9 Oct 2007 to trough 9 Mar 2009, 57 percent decline; about 17 months.
#         Source: Federal Reserve History, "The Great Recession".
TEMPLATES = {
    '1929': {'decline': 0.89, 'months': 34, 'label': '1929-style entry (Dow, −89%, 34 months)'},
    '2008': {'decline': 0.57, 'months': 17, 'label': '2008-style entry (S&P 500, −57%, 17 months)'},
    # Control: no decline. Shows what waiting costs when markets rise.
    'none': {'decline': 0.0, 'months': 0, 'label': 'No-crash control (index rises at the recovery rate)'},
}

# Parking yields: observed U.S. Treasury par yields on 13 Nov 2026 (3-month 4.32%, 2-year 4.88%),
# plus a stated downside stress for falling rates on reinvestment.
YIELDS = {'low': 0.025, 'base': 0.0432, 'high': 0.0488}

# Post-trough recovery is an assumption, shown as a range. It is not a forecast.
RECOVERY = {'slow': 0.04, 'fast': 0.08}

HORIZON = 120  # months after the sale: ten years
TEST_WINDOW = 36  # months used for the entry-risk (drawdown) read

STRATEGIES = {
    'sell_now_all': {'label': 'Invest all now', 'now': 1.0, 'park': 0, 'deploy': 0},
    'mixed_third': {'label': 'One-third now, rest parked 24 months then phased over 12', 'now': 1/3, 'park': 24, 'deploy': 12},
    'park_24': {'label': 'Park all 24 months, then phase in over 12', 'now': 0.0, 'park': 24, 'deploy': 12},
    'park_36': {'label': 'Park all 36 months, then phase in over 12', 'now': 0.0, 'park': 36, 'deploy': 12},
    'cash_only': {'label': 'Cash only (no stock exposure, reference)', 'now': 0.0, 'park': 0, 'deploy': 0},
}


def index_path(template: str, recovery: float, horizon: int = HORIZON) -> list[float]:
    """Stock index normalised to 1.0 at the peak; geometric decline, then steady recovery."""
    spec = TEMPLATES[template]
    trough = 1.0 - spec['decline']
    n = spec['months']
    growth = (1.0 + recovery) ** (1 / 12) - 1
    out = []
    for m in range(horizon + 1):
        if n == 0:
            out.append((1 + growth) ** m)
        else:
            out.append(trough ** (m / n) if m <= n else trough * (1 + growth) ** (m - n))
    return out


def simulate(template: str, strategy: str, yield_rate: float, recovery: float, horizon: int = HORIZON) -> dict:
    s = STRATEGIES[strategy]
    idx = index_path(template, recovery, horizon)
    r = (1.0 + yield_rate) ** (1 / 12)
    invested_now = PRINCIPAL * s['now']
    cash = PRINCIPAL - invested_now
    shares = invested_now / idx[0] if invested_now else 0.0
    cost_basis_index = []  # index level at each purchase, weighted by dollars
    dollars_bought = []
    if invested_now:
        dollars_bought.append((invested_now, idx[0]))
    park_cash = None
    values = [PRINCIPAL]
    for m in range(1, horizon + 1):
        cash *= r
        if m == s['park']:
            park_cash = cash
        if s['deploy'] and s['park'] < m <= s['park'] + s['deploy'] and park_cash is not None:
            amount = min(park_cash / s['deploy'], cash)
            if amount > 0:
                shares += amount / idx[m]
                cash -= amount
                dollars_bought.append((amount, idx[m]))
        values.append(cash + shares * idx[m])
    total_bought = sum(d for d, _ in dollars_bought)
    avg_entry = (sum(d for d, _ in dollars_bought) / sum(d / p for d, p in dollars_bought)) if dollars_bought else None
    return {
        'values': values,
        'value_36': values[TEST_WINDOW],
        'worst_36': min(values[: TEST_WINDOW + 1]),
        'worst_36_month': min(range(TEST_WINDOW + 1), key=lambda m: values[m]),
        'value_end': values[horizon],
        'avg_entry_index': avg_entry,
        'total_bought': total_bought,
    }


def round10(x: float) -> int:
    return int(round(x / 10.0)) * 10


if __name__ == '__main__':
    for t in TEMPLATES:
        for rec_k, rec in RECOVERY.items():
            if t == '1929' and rec_k == 'fast':
                pass
            print(f'\n== {t} template, recovery {rec_k} {rec:.0%}')
            for sk in STRATEGIES:
                res = simulate(t, sk, YIELDS['base'], rec)
                ae = res['avg_entry_index']
                print(f"{sk:14s} v36={round10(res['value_36']):>8,} worst36={round10(res['worst_36']):>8,} "
                      f"(m{res['worst_36_month']:>2}) end120={round10(res['value_end']):>8,} avgEntry={ae if ae is None else round(ae,3)}")
    print('\nYield sensitivity (park_24, 2008, recovery slow): ')
    for yk, y in YIELDS.items():
        print(yk, y, round10(simulate('2008', 'park_24', y, RECOVERY['slow'])['value_end']), round10(simulate('2008', 'sell_now_all', y, RECOVERY['slow'])['value_end']))
