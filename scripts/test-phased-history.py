#!/usr/bin/env python3
"""Independent verification of scripts/phased_history.py (the recorded-history entry test).

The model steps a portfolio month by month. This check recomputes every headline number in
closed form from the two official data extracts — tranche by tranche, product by product — with
a different code path, and asserts the structural invariants the published page relies on. It
also pins the official values this session read on 16 Nov 2026, so an edit to the extracts
cannot silently move a published figure.
"""
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parent))
import phased_history as H  # noqa: E402

TOL = 1e-6
checks = 0


def ok(cond, msg):
    global checks
    checks += 1
    if not cond:
        raise SystemExit('FAIL: ' + msg)


def factor(entry, m, series, override=None):
    return (1.0 + H.yield_for(entry, m, series, override)) ** (1 / 12)


def accrual(entry, lo, hi, series, override=None):
    """Product of the monthly yield factors over months lo (exclusive) to hi (inclusive)."""
    out = 1.0
    for m in range(lo + 1, hi + 1):
        out *= factor(entry, m - 1, series, override)
    return out


def closed_form(entry, strategy, dividends=H.DIVIDENDS, override=None):
    spec = H.STRATEGIES[strategy]
    series = spec.get('series', 'dgs3mo_annual_avg')
    park, tranches = spec['park'], spec['tranches']
    L = lambda m: H.path_level(entry, m)  # noqa: E731
    if strategy == 'now':
        return H.PRINCIPAL / L(0) * L(H.HORIZON) * (1 + dividends) ** (H.HORIZON / 12)
    if spec.get('never_invest'):
        return H.PRINCIPAL * accrual(entry, 0, H.HORIZON, series, override)
    cash_park = H.PRINCIPAL * accrual(entry, 0, park, series, override)
    c = cash_park / tranches
    # residual cash: the parked balance compounded for the whole post-parking period, less each
    # tranche compounded only from the month it was paid out.
    residual = cash_park * accrual(entry, park, H.HORIZON, series, override)
    for k in range(1, tranches + 1):
        residual -= c * accrual(entry, park + k, H.HORIZON, series, override)
    stock = 0.0
    for k in range(1, tranches + 1):
        m = park + k
        stock += c * (L(H.HORIZON) / L(m)) * (1 + dividends) ** ((H.HORIZON - m) / 12)
    return residual + stock


# ---------------------------------------------------------------- data lineage anchors
# Read from the official FRED endpoints on 16 Nov 2026; see scripts/data/*_README_2026-11-16.md.
ok(abs(H.PRICE[2007] - 91.882580) < 1e-9, 'share-price index, December 2007 (FRED monthly)')
ok(abs(H.PRICE[2008] - 51.736620) < 1e-9, 'share-price index, December 2008 (FRED monthly)')
ok(abs(H.PRICE[2009] - 67.164700) < 1e-9, 'share-price index, December 2009 (FRED monthly)')
ok(abs(H.YIELDS['dgs3mo_annual_avg'][2007] - 0.0448) < 1e-9, '3-month annual average 2007')
ok(abs(H.YIELDS['dgs3mo_annual_avg'][2008] - 0.0140) < 1e-9, '3-month annual average 2008')
ok(abs(H.YIELDS['dgs3mo_annual_avg'][2009] - 0.0015) < 1e-9, '3-month annual average 2009')
ok(abs(H.YIELDS['dgs3mo_annual_avg'][2011] - 0.0005) < 1e-9, '3-month annual average 2011')
ok(abs(H.YIELDS['dgs3mo_annual_avg'][1982] - 0.1109) < 1e-9, '3-month annual average 1982 (first year)')
ok(abs(H.YIELDS['dgs2_annual_avg'][2020] - 0.0039) < 1e-9, '2-year annual average 2020')
ok(abs(H.YIELDS['dgs2_annual_avg'][1981] - 0.1457) < 1e-9, '2-year annual average 1981 (series peak year here)')
ok(abs(H.CPI[2025] - 321.943) < 1e-9, 'CPI-U annual average 2025')
ok(min(H.PRICE) > 0 and all(v >= 0 for v in H.YIELDS['dgs3mo_annual_avg'].values()),
   'no negative yield and no non-positive index level')

# ---------------------------------------------------------------- window definition
entries = H.entry_years()
ok(entries == list(range(1982, 2017)), f'entry window is 1982..2016, got {entries[0]}..{entries[-1]}')
ok(H.HORIZON == 120, 'ten-year horizon')
ok(H.PRICE[min(entries) - 1] > 0 and H.PRICE[max(entries) + 9] > 0, 'every path is bracketed by price data')

# ---------------------------------------------------------------- closed-form agreement
for t in entries:
    for strategy in H.STRATEGIES:
        got = H.simulate(t, strategy)['terminal']
        want = closed_form(t, strategy)
        ok(abs(got - want) <= TOL * max(1.0, abs(want)), f'{t}/{strategy}: {got!r} != {want!r}')
    for div in (0.0, H.DIVIDENDS, 0.04):
        got = H.simulate(t, 'park24', div)['terminal']
        want = closed_form(t, 'park24', div)
        ok(abs(got - want) <= TOL * max(1.0, abs(want)), f'{t}/park24/div{div}: {got!r} != {want!r}')
    # a flat override must reproduce the same cash arithmetic the template-style test uses
    ok(abs(H.simulate(t, 'park24', H.DIVIDENDS, 0.0432)['terminal']
           - closed_form(t, 'park24', H.DIVIDENDS, 0.0432)) <= TOL * 1e6, f'{t}/park24 flat 4.32%')

# ---------------------------------------------------------------- structural invariants
for t in entries:
    p36 = H.simulate(t, 'park36')
    ok(abs(p36['worst_36'] - H.PRINCIPAL) < 1e-9, f'{t}: a 36-month park holds the balance through month 36')
    ok(p36['full_tranches'] and H.simulate(t, 'park24')['full_tranches'], f'{t}: every tranche paid in full')
    now = H.simulate(t, 'now')
    ok(now['worst_36'] <= H.PRINCIPAL + 1e-9, f'{t}: invest-now is marked at or below the start within the first three years')
    ok(0.2 * H.PRINCIPAL < now['terminal'] < 8 * H.PRINCIPAL, f'{t}: invest-now terminal within a sane band')
    ok(abs(p36['terminal'] - closed_form(t, 'park36')) < 1e-6, f'{t}: park-36 reconstructs')
    ok(H.simulate(t, 'park24')['parked_years'] == [t, t + 1], f'{t}: 24 months of parking spans two tax years')
    ok(H.simulate(t, 'park24y')['parked_years'] == [t, t + 1], f'{t}: the 2-year variant parks the same window')
    # the recorded path and a flat path can only differ through the yield, never through the prices
    ok(H.simulate(t, 'park24')['bought_at'][0][1] == H.path_level(t, 25), f'{t}: first tranche buys at month 25')

# the cash-only reference must equal the compounded recorded bill yields, and never beat itself
for t in entries:
    want = H.PRINCIPAL * accrual(t, 0, H.HORIZON, 'dgs3mo_annual_avg')
    ok(abs(H.simulate(t, 'cash')['terminal'] - want) <= TOL * want, f'{t}: cash reference')

# a higher parking yield can only raise a parked result, in every entry year and every plan
for t in entries:
    for strategy in ('park24', 'park36', 'park24y', 'cash'):
        low = H.simulate(t, strategy, H.DIVIDENDS, 0.01)['terminal']
        high = H.simulate(t, strategy, H.DIVIDENDS, 0.05)['terminal']
        ok(high > low, f'{t}/{strategy}: a higher flat yield must pay more')
    inv = H.simulate(t, 'now', H.DIVIDENDS, 0.05)['terminal']
    ok(abs(inv - H.simulate(t, 'now')['terminal']) < 1e-9, f'{t}: an invested portfolio ignores the parking yield')

# the yield actually earned while parked must be the geometric mean of the recorded years
for t in entries:
    res = H.simulate(t, 'park24')
    y0 = H.YIELDS['dgs3mo_annual_avg'][t]
    y1 = H.YIELDS['dgs3mo_annual_avg'][t + 1]
    want = ((1 + y0) * (1 + y1)) ** 0.5 - 1
    ok(abs(res['parked_yield'] - want) < 1e-12, f'{t}: parked yield {res["parked_yield"]} != {want}')

# ---------------------------------------------------------------- published findings
# These are the numbers the Black swans page states. They are regression guards: if the extracts
# change, or the model changes, the page and this check must be re-verified against official data.
s_all = H.summary()
s_down = H.summary(H.down_entries())
s_deep = H.summary(H.crash_entries())
ok(s_all['n'] == 35, 'thirty-five entry years are tested')
ok(s_all['park24']['win_years'] == [1999, 2000, 2001, 2006, 2007, 2008], 'park-24 wins in six entries, all listed')
ok(s_all['park24']['wins'] == 6, 'six wins out of 35')
ok(s_all['park36']['wins'] == 7, 'seven wins for the 36-month park')
ok(s_all['cash']['wins'] == 2, 'two wins for staying in bills')
ok(s_all['park24']['median_diff'] < 0, 'the median entry year loses from parking: waiting is not free')
ok(H.round10(s_all['park24']['median_diff']) == -42860, f'median difference published as −$42,860, got {s_all["park24"]["median_diff"]}')
ok(H.round10(s_all['park24']['best_diff']) == 66060, 'best entry-year gain (2007)')
ok(H.round10(s_all['park24']['worst_diff']) == -132870, 'worst entry-year cost')
ok(s_all['park24']['dd_wins'] == 11, 'the worst point improves in eleven entries')
ok(s_down['n'] == 9 and s_deep['n'] == 2, 'down-year and deep-crash subsets')
ok(s_deep['park24']['win_years'] == [2008], 'in a double-digit decline year, parking won in 2008 only')
e08 = {k: H.simulate(2008, k) for k in H.STRATEGIES}
ok(e08['now']['worst_36'] < 0.6 * H.PRINCIPAL, '2008 invest-now drawdown is severe')
ok(abs(e08['park24']['worst_36'] - H.PRINCIPAL) < 1e-9, '2008 park-24 never prints a loss in the first three years')
ok(H.round10(e08['park24']['terminal'] - e08['now']['terminal']) == 41030, '2008 gain from parking, published as $41,030')
ok(round(e08['park24']['parked_yield'] * 100, 2) == 0.77, f"2008 parked yield displayed as 0.77%, got {e08['park24']['parked_yield']:.4%}")
ok(abs(e08['park24']['parked_yield'] - (((1 + H.YIELDS['dgs3mo_annual_avg'][2008]) * (1 + H.YIELDS['dgs3mo_annual_avg'][2009])) ** 0.5 - 1)) < 1e-12, '2008 parked yield is the geometric mean of 1.40% and 0.15%')
flat = H.flat_park_compare(2008, 'park24', 0.0432)
ok(flat['difference'] > 10_000, 'a flat 4.32% assumption flatters the 2008 park by five figures')
ok(H.round10(flat['difference']) == 17610, f'the suggestion page quotes the flattery as about $17,610, got {flat["difference"]:,.0f}')
ok(H.money(flat['flat']) == '$216,580' and H.money(flat['recorded']) == '$198,970', 'flat-versus-recorded pair')
# the maturity choice inside the 3M–2Y band is second-order next to the entry-date choice
gain = [H.simulate(t, 'park24y')['terminal'] - H.simulate(t, 'park24')['terminal'] for t in entries]
ok(max(gain) < 15_000, f'2-year over 3-month is worth at most about $10,000 per $100,000, got {max(gain):,.0f}')
ok(H.round10(max(gain)) == 11620, f'the suggestion page quotes the maximum as $11,620, got {max(gain):,.0f}')
ok(H.round10(H.median(gain)) == 2700, f'the suggestion page quotes the median as roughly $2,700, got {H.median(gain):,.0f}')
# dividends: the assumed stock return drives the price of waiting, so the page must say so
mean = {d: H.summary(dividends=d)['park24']['mean_diff'] for d in (0.0, 0.02, 0.04)}
ok(mean[0.0] > mean[0.02] > mean[0.04], 'a higher dividend assumption makes waiting look more expensive')
# the flagged-issues page quotes both the median and the mean at each setting; neither may drift
med = {d: H.summary(dividends=d)['park24']['median_diff'] for d in (0.0, 0.02, 0.04)}
ok(H.round10(med[0.0]) == -22740 and H.round10(med[0.02]) == -42860 and H.round10(med[0.04]) == -64730,
   f'the flagged-issues page quotes medians −$22,740 / −$42,860 / −$64,730, got '
   + ' / '.join(f'{med[d]:,.0f}' for d in (0.0, 0.02, 0.04)))
ok(H.round10(mean[0.0]) == -23130 and H.round10(mean[0.02]) == -40190 and H.round10(mean[0.04]) == -62280,
   f'the flagged-issues page quotes means −$23,130 / −$40,190 / −$62,280, got '
   + ' / '.join(f'{mean[d]:,.0f}' for d in (0.0, 0.02, 0.04)))
ok(med[0.0] > med[0.02] > med[0.04], 'the median moves the same way the mean does')
ok(H.summary(dividends=0.0)['park24']['wins'] == H.summary()['park24']['wins'] == 6
   and H.summary(dividends=0.04)['park24']['wins'] == 5, 'wins are 6 / 6 / 5 across the settings')
# interpolation must reproduce the year-end levels exactly at the December months
for t in entries:
    for k in range(11):
        ok(abs(H.path_level(t, 12 * k) - H.PRICE[t - 1 + k]) < 1e-12, f'{t}: December month {12 * k} is the observation itself')
    mid = H.path_level(t, 6)
    lo, hi = H.PRICE[t - 1], H.PRICE[t]
    ok(min(lo, hi) < mid < max(lo, hi) or lo == hi, f'{t}: mid-year interpolation stays inside the bracket')

print(f'PASS: recorded-history entry test reproduced in closed form across {len(entries)} entry years '
      f'and {len(H.STRATEGIES)} plans; {checks} checks.')
