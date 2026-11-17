#!/usr/bin/env python3
"""Recorded-history entry test: park sale proceeds in actual Treasury yields, then phase in.

The Black swans page already answers this question on two smooth geometric crash templates with
a flat parking yield. This module answers it again on **recorded official history**: the actual
share-price path and the actual 3-month and 2-year Treasury yields for every calendar year of
the test window. It exists because a flat parking yield hides the one thing a real crash does to
parked money — the bill yield collapses at the same time the index does, so the money that waits
earns least exactly when waiting looks best.

Inputs are two data extracts transcribed from FRED (scripts/data/fred_*_2026-11-16.csv), with
the provenance and cross-checks recorded in the README files beside them. No household figure is
an input here, and no output is a household amount: everything is per $100,000 of illustrative
proceeds.

Conventions, all disclosed on the page:
  * month 0 is the end of the year before the entry year (December of t-1);
  * the index level between year-ends is a geometric interpolation of the two December values,
    because only annual data is used here;
  * parked cash earns the published annual average yield of the calendar year it is in,
    compounded monthly as (1 + y) ** (1/12) (H.15 bill yields are quoted on an investment basis);
  * a 12-month phase-in is twelve equal monthly tranches;
  * every stock leg, and only the stock legs, additionally earns one stated dividend assumption
    (DIVIDENDS below), which is an invented number, not an official figure.
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EQUITY_CSV = ROOT / 'scripts' / 'data' / 'fred_equity_annual_2026-11-16.csv'
YIELD_CSV = ROOT / 'scripts' / 'data' / 'fred_treasury_annual_2026-11-16.csv'

PRINCIPAL = 100_000  # invented illustration, per $100,000 of net proceeds
HORIZON = 120        # months from the start of the entry year
ENTRY_FIRST = 1982   # first year the 3-month Treasury series has a full annual average
ENTRY_LAST = 2016    # last entry year whose 120-month horizon ends inside the price series
DIVIDENDS = 0.02     # stated assumption: 2.0 percentage points a year on the stock legs only

STRATEGIES = {
    'now':     {'label': 'Invest all at the transfer', 'park': 0, 'tranches': 1},
    'park24':  {'label': 'Park 24 months in 3-month bills, then phase in over 12', 'park': 24, 'tranches': 12},
    'park36':  {'label': 'Park 36 months in 3-month bills, then phase in over 12', 'park': 36, 'tranches': 12},
    'park24y': {'label': 'Park 24 months at the 2-year note yield, then phase in over 12',
                'park': 24, 'tranches': 12, 'series': 'dgs2_annual_avg'},
    'cash':    {'label': 'Stay in 3-month bills for the whole horizon (reference)',
                'park': 0, 'tranches': 0, 'series': 'dgs3mo_annual_avg', 'never_invest': True},
}


def load():
    """Read the two official extracts. Returns price, cpi and yield dicts keyed by year."""
    price, cpi = {}, {}
    with EQUITY_CSV.open(encoding='utf8') as fh:
        for row in csv.DictReader(fh):
            y = int(row['year'])
            if row['eq_dec_level_spastt01usm661n']:
                price[y] = float(row['eq_dec_level_spastt01usm661n'])
            if row['cpi_avg_cpiaucns']:
                cpi[y] = float(row['cpi_avg_cpiaucns'])
    yields = {'dgs3mo_annual_avg': {}, 'dgs2_annual_avg': {}}
    with YIELD_CSV.open(encoding='utf8') as fh:
        for row in csv.DictReader(fh):
            y = int(row['year'])
            for col in yields:
                if row[col]:
                    yields[col][y] = float(row[col]) / 100.0
    return price, cpi, yields


PRICE, CPI, YIELDS = load()


def index_level(year: int, month_of_year: int) -> float:
    """Geometric interpolation between the two December observations that bracket the month.

    A month_of_year of 0 is the December observation itself, so it needs no upper bracket;
    that also makes the horizon's final month resolve on the last year in the extract."""
    lo = PRICE[year]
    if month_of_year == 0:
        return lo
    hi = PRICE[year + 1]
    return lo * (hi / lo) ** (month_of_year / 12.0)


def path_level(entry_year: int, m: int) -> float:
    """Index level at month m, where month 0 is the December before the entry year."""
    y = entry_year - 1 + m // 12
    return index_level(y, m % 12)


def yield_for(entry_year: int, m: int, series: str, override: float | None = None) -> float:
    """The published annual-average yield of the calendar year the month falls in."""
    if override is not None:
        return override
    return YIELDS[series][entry_year + m // 12]


def simulate(entry_year: int, strategy: str, dividends: float = DIVIDENDS,
             yield_override: float | None = None) -> dict:
    """One path through the model. `yield_override` replaces the recorded annual-average yield
    with a flat rate, which is what the template test above on the same page assumes; it exists
    so the page can price the difference between the two."""
    spec = STRATEGIES[strategy]
    series = spec.get('series', 'dgs3mo_annual_avg')
    park, tranches = spec['park'], spec['tranches']
    monthly_stock = (1 + dividends) ** (1 / 12)
    cash = 0.0 if strategy == 'now' else PRINCIPAL
    shares = 0.0 if spec.get('never_invest') or park else PRINCIPAL / path_level(entry_year, 0)
    buy_months = range(park + 1, park + tranches + 1) if tranches > 1 else []
    tranche = None  # fixed once, at the moment the parking window closes: balance / tranche count
    values, bought_at = [], []
    for m in range(HORIZON + 1):
        if m:
            cash *= (1 + yield_for(entry_year, m - 1, series, yield_override)) ** (1 / 12)
            shares *= monthly_stock
            if m == park:
                tranche = cash / tranches
            if m in buy_months:
                amount = min(tranche, cash)
                shares += amount / path_level(entry_year, m)
                cash -= amount
                bought_at.append((m, path_level(entry_year, m), amount))
        values.append(cash + shares * path_level(entry_year, m))
    parked = [v for i, v in enumerate(values) if i <= (park or 1)]
    park_end = values[park] if park else values[0]
    park_start = PRINCIPAL
    parked_yield = ((park_end / park_start) ** (12.0 / park) - 1) if park else None
    return {
        'values': values,
        'terminal': values[HORIZON],
        'worst_36': min(values[:37]),
        'worst_36_month': min(range(37), key=lambda i: values[i]),
        'worst_all': min(values),
        'terminal_real': values[HORIZON] * CPI[entry_year - 1] / CPI[entry_year + HORIZON // 12 - 1],
        'entry_change': PRICE[entry_year] / PRICE[entry_year - 1] - 1,
        'parked_yield': parked_yield,
        'parked_years': [entry_year + i for i in range(park // 12)] if park else [],
        'parked_levels': [YIELDS[series][y] for y in ([entry_year + i for i in range(park // 12)] if park else [])],
        'bought_at': bought_at,
        'first_buy_month': (park + 1) if tranches > 1 else (0 if not park else None),
        'cash_only': spec.get('never_invest', False),
        'tranche': tranche,
        'full_tranches': tranche is not None and all(abs(a - tranche) < 1e-9 for _, _, a in bought_at),
    }


def flat_park_compare(entry_year: int, strategy: str, flat: float) -> dict:
    """Recorded yields versus one flat yield, for the same entry and the same plan."""
    real = simulate(entry_year, strategy)
    alt = simulate(entry_year, strategy, yield_override=flat)
    return {'recorded': real['terminal'], 'flat': alt['terminal'], 'difference': alt['terminal'] - real['terminal'],
            'recorded_worst': real['worst_36'], 'flat_worst': alt['worst_36']}


def entry_years():
    return [t for t in range(ENTRY_FIRST, ENTRY_LAST + 1)
            if t + HORIZON // 12 - 1 <= max(PRICE) and all(
                (t + i) in YIELDS['dgs3mo_annual_avg'] for i in range(4))]


def run_all(strategy: str):
    return {t: simulate(t, strategy) for t in entry_years()}


def crash_entries():
    """Entry years whose own calendar year ended at least 10 percent below the previous one."""
    return [t for t in entry_years() if PRICE[t] / PRICE[t - 1] - 1 <= -0.10]


def down_entries():
    """Entry years that ended lower than the year before them, by any amount."""
    return [t for t in entry_years() if PRICE[t] / PRICE[t - 1] - 1 < 0]


def summary(entries=None, dividends: float = DIVIDENDS):
    """Aggregate reading of the test: how often waiting pays, and what it costs."""
    entries = entry_years() if entries is None else entries
    out = {'n': len(entries), 'dividends': dividends}
    now = {t: simulate(t, 'now', dividends)['terminal'] for t in entries}
    worst_now = {t: simulate(t, 'now', dividends)['worst_36'] for t in entries}
    for s in ('park24', 'park36', 'park24y', 'cash'):
        res = {t: simulate(t, s, dividends) for t in entries}
        diff = [res[t]['terminal'] - now[t] for t in entries]
        worst_lift = [res[t]['worst_36'] - worst_now[t] for t in entries]
        out[s] = {
            'wins': sum(1 for d in diff if d > 0),
            'win_years': [t for t in entries if res[t]['terminal'] > now[t]],
            'median_diff': median(diff),
            'mean_diff': sum(diff) / len(diff),
            'best_diff': max(diff),
            'worst_diff': min(diff),
            'mean_worst_lift': sum(worst_lift) / len(worst_lift),
            'median_worst_lift': median(worst_lift),
            'dd_wins': sum(1 for d in worst_lift if d > 0),
            'mean_parked_yield': (sum(res[t]['parked_yield'] for t in entries if res[t]['parked_yield'])
                                  / max(1, sum(1 for t in entries if res[t]['parked_yield']))),
        }
    return out


def median(values):
    """Middle value; the mean of the two central values when the count is even."""
    v = sorted(values)
    n = len(v)
    if not n:
        return None
    return v[n // 2] if n % 2 else (v[n // 2 - 1] + v[n // 2]) / 2.0


def round10(value: float) -> int:
    return int(round(value / 10.0)) * 10


def money(value: float) -> str:
    v = round10(value)
    return f"−${abs(v):,}" if v < 0 else f"${v:,}"


if __name__ == '__main__':
    print('entry years:', entry_years()[0], 'to', entry_years()[-1], f'({len(entry_years())})')
    print('crash entries:', crash_entries())
    for t in (1987, 1989, 1990, 2000, 2001, 2007, 2008, 2015):
        if t not in entry_years():
            continue
        row = {s: simulate(t, s) for s in STRATEGIES}
        print(f'{t}  entry-year index {row["now"]["entry_change"]:+.1%}  '
              f'now {money(row["now"]["terminal"])}  worst {money(row["now"]["worst_36"])} | '
              f'park24 {money(row["park24"]["terminal"])} (diff {money(row["park24"]["terminal"] - row["now"]["terminal"])}, '
              f'yield {row["park24"]["parked_yield"]:.2%}) | '
              f'park36 {money(row["park36"]["terminal"])} (diff {money(row["park36"]["terminal"] - row["now"]["terminal"])}) | '
              f'cash {money(row["cash"]["terminal"])}')
    print()
    print('ALL ENTRIES:', summary())
    print('CRASH ENTRIES:', summary(crash_entries()))
