#!/usr/bin/env python3
"""Phased-entry model for proceeds from a sale, with stylised crash templates.

Everything here is an illustration per $100,000 of net proceeds. No household
figure is an input. Crash templates are calibrated only to the official
peak-to-trough declines cited on the public guide; the path between the peak
and the trough is a smooth geometric interpolation, not the index history.

Two shapes of recovery are offered, because the shape decides the answer:
  'trend' — after the trough the index grows at the stated recovery rate. The
            index stays permanently below the no-crash line, which is the
            pessimistic reading of a crash.
  'peak'  — the index is returned to its pre-crash level at the month the
            record says that happened, then grows at the recovery rate. The
            annual rate implied from the trough is therefore steep, and the
            point of the shape is the *time* under water, not the rate.
The parking leg models the proceeds held in U.S. Treasury securities: either
rolled three-month bills, or a ladder whose two-year leg is locked to maturity
(see LADDER and PARK_PATHS), so that reinvestment risk is a named input rather
than a caveat.
"""
from __future__ import annotations

PRINCIPAL = 100_000  # invented, per-$100,000 illustration
HORIZON = 120  # months after the sale: ten years
TEST_WINDOW = 36  # months used for the entry-risk (drawdown) read

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

# Recovery *shape*. 'trend' grows from the trough at the recovery rate and never
# returns to the pre-crash level. 'peak' returns the index to its pre-crash level
# at the month below and then grows at the recovery rate.
#   1929: 303 months. Federal Reserve History, "Stock Market Crash of 1929", states
#         the Dow closed at 381.17 on 3 Sep 1929, fell to 41.22 on 8 Jul 1932 (89 percent
#         below the peak) and "did not return to its pre-crash heights until November 1954";
#         its chart dates the regain 23 Nov 1954. 3 Sep 1929 to 23 Nov 1954 = 303 months.
#         Re-read 16 Nov 2026: https://www.federalreservehistory.org/essays/stock-market-crash-of-1929
#   2008: 66 months. ASSUMPTION, not an observation. No official page re-read in this review
#         states when the S&P 500 regained its October 2007 level; 66 months is the figure the
#         decision engine already carries as a labelled assumption, so the two stay consistent.
PEAK_REGAIN = {'1929': 303, '2008': 66, 'none': 0}
PEAK_REGAIN_STATUS = {
    '1929': 'Official record: Federal Reserve History states the pre-crash high was not reached again until November 1954.',
    '2008': 'Assumption: 66 months, the same figure the decision engine uses; no official regain date was found in this review.',
    'none': 'Not applicable: the control has no decline to recover from.',
}
SHAPES = ('trend', 'peak')

# Parking the proceeds in Treasuries. A three-month bill reprices every quarter, so the yield
# over a 24-to-36-month wait is a path, not a number; a two-year note is locked to maturity.
ROLL_MONTHS = 3          # Treasury bills mature in 4 to 52 weeks (TreasuryDirect)
NOTE_MONTHS = 24         # the shortest Treasury note maturity band that covers a 24-month wait
BILL_START = YIELDS['base']   # 3-month par yield observed 13 Nov 2026
NOTE_LOCK = YIELDS['high']    # 2-year par yield observed 13 Nov 2026

# Quarterly bill-reinvestment paths. Only the first quarter is an observation; the rest are
# labelled planning assumptions chosen to match what the decision engine assumes for the same
# crash scenarios, so the two tests do not disagree about rates by accident.
PARK_PATHS = {
    'flat': {'label': 'Rates stay where they are: every roll at the observed 4.32%',
             'quarters': [0.0432]},
    'crash-1929': {'label': 'Crash-recession path used by the engine for a 1929-style year two: 4.32% for the first year, then 1.00%',
                    'quarters': [0.0432, 0.0432, 0.0432, 0.0432, 0.01]},
    'crash-2008': {'label': 'Crash-recession path used by the engine for a 2008-style year one: 4.32% for six months, then 0.50%',
                   'quarters': [0.0432, 0.0432, 0.005]},
    'rising': {'label': 'Rate-rise path (inflation risk to the buyer of the short bill): 4.32%, then 5.00%, 5.50%, 6.00%',
               'quarters': [0.0432, 0.05, 0.055, 0.06]},
}


def bill_path(kind: str = 'flat', months: int = HORIZON) -> list[float]:
    """Annual yield applied to rolled three-month bills in each month of the wait."""
    quarters = PARK_PATHS[kind]['quarters']
    return [quarters[min(m // ROLL_MONTHS, len(quarters) - 1)] for m in range(months)]


def ladder_path(park_months: int, weight_2y: float, kind: str = 'flat',
                months: int = HORIZON) -> list[float]:
    """Annual yield on a Treasury ladder: a share locked in a 2-year note, the rest rolled.

    The locked share earns the 2-year par yield until month 24, when the note matures; after
    that the whole pot rolls with the bill path. Every strategy in STRATEGIES deploys no earlier
    than month 24, so no note is ever assumed to be sold before maturity — the mark-to-market
    loss on an early sale is therefore out of scope here, and is stated as such on the page.
    """
    bills = bill_path(kind, months)
    out = []
    for m in range(months):
        if m < min(park_months, NOTE_MONTHS):
            out.append(weight_2y * NOTE_LOCK + (1.0 - weight_2y) * bills[m])
        else:
            out.append(bills[m])
    return out



STRATEGIES = {
    'sell_now_all': {'label': 'Invest all now', 'now': 1.0, 'park': 0, 'deploy': 0},
    'mixed_third': {'label': 'One-third now, rest parked 24 months then phased over 12', 'now': 1/3, 'park': 24, 'deploy': 12},
    'park_24': {'label': 'Park all 24 months, then phase in over 12', 'now': 0.0, 'park': 24, 'deploy': 12},
    'park_36': {'label': 'Park all 36 months, then phase in over 12', 'now': 0.0, 'park': 36, 'deploy': 12},
    'cash_only': {'label': 'Cash only (no stock exposure, reference)', 'now': 0.0, 'park': 0, 'deploy': 0},
}


def index_path(template: str, recovery: float, horizon: int = HORIZON,
               shape: str = 'trend') -> list[float]:
    """Stock index normalised to 1.0 at the peak.

    'trend': geometric decline to the trough, then steady growth at `recovery`.
    'peak':  the same decline, then a geometric climb that reaches the pre-crash level
             exactly at PEAK_REGAIN[template], then steady growth at `recovery`.
    """
    if shape not in SHAPES:
        raise ValueError(f'unknown recovery shape: {shape}')
    spec = TEMPLATES[template]
    trough = 1.0 - spec['decline']
    n = spec['months']
    growth = (1.0 + recovery) ** (1 / 12) - 1
    out = []
    for m in range(horizon + 1):
        if n == 0:
            out.append((1 + growth) ** m)
        elif shape == 'trend':
            out.append(trough ** (m / n) if m <= n else trough * (1 + growth) ** (m - n))
        else:
            regain = max(PEAK_REGAIN[template], n + 1)
            climb = (1.0 / trough) ** (1.0 / (regain - n)) - 1.0
            if m <= n:
                out.append(trough ** (m / n))
            elif m <= regain:
                out.append(trough * (1.0 + climb) ** (m - n))
            else:
                out.append((1.0 + growth) ** (m - regain))
    return out


def months_under_water(values: list[float], principal: float = PRINCIPAL) -> int:
    """How many months the portfolio spent below the amount put in. The entry-risk measure
    a 25-year regain makes visible, which a terminal value alone hides."""
    return sum(1 for v in values if v < principal - 1e-9)


def break_even_month(values: list[float], principal: float = PRINCIPAL):
    """First month after the entry at which the portfolio is back to the amount put in, or None.
    Month 0 is the entry itself, so it is not counted as a recovery."""
    for m, v in enumerate(values):
        if m and v >= principal - 1e-9:
            return m
    return None


def simulate(template: str, strategy: str, yield_rate: float, recovery: float, horizon: int = HORIZON,
             *, shape: str = 'trend', cash_path: list[float] | None = None) -> dict:
    """Run one entry plan through one crash shape. `cash_path` replaces the flat parking yield
    with a month-by-month annual yield, which is how the Treasury ladder and the reinvestment
    paths are expressed; `yield_rate` still applies when no path is given."""
    s = STRATEGIES[strategy]
    idx = index_path(template, recovery, horizon, shape)

    def ym(month: int) -> float:
        if cash_path is not None:
            return cash_path[min(month - 1, len(cash_path) - 1)]
        return yield_rate

    invested_now = PRINCIPAL * s['now']
    cash = PRINCIPAL - invested_now
    parked_start = cash
    shares = invested_now / idx[0] if invested_now else 0.0
    cost_basis_index = []  # index level at each purchase, weighted by dollars
    dollars_bought = []
    if invested_now:
        dollars_bought.append((invested_now, idx[0]))
    park_cash = None
    park_value_at_deploy = None
    values = [PRINCIPAL]
    for m in range(1, horizon + 1):
        cash *= (1.0 + ym(m)) ** (1 / 12)
        if m == s['park']:
            park_cash = cash
            park_value_at_deploy = cash
        if s['deploy'] and s['park'] < m <= s['park'] + s['deploy'] and park_cash is not None:
            amount = min(park_cash / s['deploy'], cash)
            if amount > 0:
                shares += amount / idx[m]
                cash -= amount
                dollars_bought.append((amount, idx[m]))
        values.append(cash + shares * idx[m])
    total_bought = sum(d for d, _ in dollars_bought)
    avg_entry = (sum(d for d, _ in dollars_bought) / sum(d / p for d, p in dollars_bought)) if dollars_bought else None
    realized = None
    if park_value_at_deploy is not None and parked_start > 0 and s['park'] > 0:
        realized = (park_value_at_deploy / parked_start) ** (12.0 / s['park']) - 1.0
    return {
        'values': values,
        'value_36': values[TEST_WINDOW],
        'worst_36': min(values[: TEST_WINDOW + 1]),
        'worst_36_month': min(range(TEST_WINDOW + 1), key=lambda m: values[m]),
        'value_end': values[horizon],
        'avg_entry_index': avg_entry,
        'total_bought': total_bought,
        'under_water_months': months_under_water(values),
        'break_even_month': break_even_month(values),
        'park_value_at_deploy': park_value_at_deploy,
        'parked_start': parked_start,
        'realized_park_yield': realized,
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
