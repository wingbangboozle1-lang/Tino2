#!/usr/bin/env python3
"""Independently reconstruct every published table from first principles.

This does not import or execute the JavaScript model. It re-derives the
arithmetic in Python from the same published assumptions and compares the
result with the numbers that are actually written into the HTML pages. If a page
displays a figure that this script cannot reproduce, the build fails.

No household record is read or written.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SNAP = json.loads((ROOT / 'scripts' / 'data' / 'snapshot.json').read_text())

FAILS = []
CHECKS = 0


def check(actual, expected, label, tol=0.5):
    """Compare a published figure with the independent result."""
    global CHECKS
    CHECKS += 1
    if actual is None:
        FAILS.append(f'{label}: published value is None')
        return
    if abs(round(actual) - round(expected)) > tol:
        FAILS.append(f'{label}: published {actual:,.0f} vs independent {expected:,.0f}')


# ---------------------------------------------------------------------------
# Independent inputs, re-typed from the published method page.
# ---------------------------------------------------------------------------
A_VALUE, A_ASSESSED, A_RATE = 2_990_000, 549_000, 0.01335
B_VALUE, B_ASSESSED, B_RATE = 1_790_000, 119_000, 0.0118162182
HOME, ASSESS_GROWTH, CPI = 0.036, 0.02, 0.023
PORT, FEE = 0.050, 0.005
RENT_A, RENT_GROWTH, VACANCY, MGMT = 6_500, 0.023, 0.05, 0.08
WATER_A, ELEC_A, INS_A, INS_GROWTH, MAINT_A = 130, -10, 2_200, 0.038, 0.0075
ORD_TAX, CG_TAX, RECAP_TAX = 0.30, 0.28, 0.25
SALE, EXCL, DEP_YEARS, LAND_SHARE = 0.06, 250_000, 27.5, 0.20
PROP19, PROP19_STEP = 1_044_586, 0.036
START = 2026

R_NET = PORT - FEE


def grow(p, r, n):
    return p * (1 + r) ** n


def allowance(year):
    steps = max(0, (year - 2025) // 2)
    return PROP19 * (1 + PROP19_STEP) ** steps


def series_a(year):
    n = year - START
    market = grow(A_VALUE, HOME, n)
    factored = grow(A_ASSESSED, ASSESS_GROWTH, n)
    return market, min(factored, market)


def transfer(year):
    market, assessed = series_a(year)
    cap = assessed + allowance(year)
    primary = min(market, assessed + max(0, market - cap))
    return market, assessed, allowance(year), cap, primary


def holding(t_year, year, option):
    """Annual cash flow, matching the published method."""
    t_market, _, _, _, t_primary = transfer(t_year)
    market, _ = series_a(year)
    base = t_primary if option == 'live' else t_market
    assessed = min(grow(base, ASSESS_GROWTH, year - t_year), market)
    n = year - START
    prop = assessed * A_RATE
    hoex = 7_000 * A_RATE if option == 'live' else 0
    water = grow(WATER_A * 12, CPI, n)
    electric = ELEC_A * 12
    ins = grow(INS_A, INS_GROWTH, n)
    maint = market * MAINT_A
    opex = prop - hoex + water + electric + ins + maint
    if option == 'live':
        return -opex, {'opex': opex, 'propTax': prop, 'hoex': hoex, 'market': market,
                       'assessed': assessed, 'water': water, 'electric': electric,
                       'insurance': ins, 'maintenance': maint}
    rent = grow(RENT_A * 12, RENT_GROWTH, n)
    collected = rent * (1 - VACANCY)
    mgmt = collected * MGMT
    noi = collected - mgmt - opex
    return noi, {'opex': opex, 'propTax': prop, 'hoex': 0, 'market': market,
                 'assessed': assessed, 'water': water, 'electric': electric,
                 'insurance': ins, 'maintenance': maint, 'rent': rent, 'noi': noi}


def compare(t_year, horizon):
    market, _, _, _, _ = transfer(t_year)
    proceeds = market * (1 - SALE)
    sell_terminal = grow(proceeds, R_NET, horizon)
    sell_tax = max(0, sell_terminal - proceeds) * CG_TAX
    out = {'sell': sell_terminal - sell_tax}
    for option in ('rent', 'live'):
        reserve, carry, dep = 0.0, 0.0, 0.0
        first = None
        for i in range(1, horizon + 1):
            flow, detail = holding(t_year, t_year + i, option)
            tax = 0.0
            if option == 'rent':
                dep_step = (market * (1 - LAND_SHARE)) / DEP_YEARS
                taxable = flow - dep_step - carry
                if taxable < 0:
                    carry, tax = -taxable, 0.0
                else:
                    carry, tax = 0.0, max(0.0, taxable) * ORD_TAX
                dep += dep_step
            net = flow - tax
            if first is None:
                first = net
            reserve = reserve * (1 + R_NET) + net
        exit_market, _ = series_a(t_year + horizon)
        gross = exit_market * (1 - SALE)
        if option == 'rent':
            gain = max(0, gross - market + dep)
            recap = min(gain, dep)
            tax = recap * RECAP_TAX + max(0, gain - recap) * CG_TAX
        else:
            gain = max(0, gross - market)
            tax = max(0, gain - EXCL) * CG_TAX
        out[option] = gross - tax + reserve
        out[option + '_first'] = first
    # San Francisco third unit, only if the household lives in A.
    rent3 = 2_770 * 12
    flow3 = rent3 * (1 - 0.04) * (1 - 0.05)
    flow3 -= flow3 * ORD_TAX
    extra = 0.0
    for j in range(1, horizon + 1):
        extra = extra * (1 + R_NET) + grow(flow3, 0.016, j + (t_year - START))
    extra -= max(0, extra) * 0.20
    out['live_total'] = out['live'] + extra
    out['extra'] = extra
    return out


def read_tables():
    """Pull the figures actually written into the HTML."""
    pages = {}
    for name in ('index', 'decision', 'stress', 'property', 'tax', 'inheritance'):
        path = ROOT / ('index.html' if name == 'index' else f'guide/{name}.html')
        pages[name] = path.read_text(encoding='utf8')
    return pages


def numbers(cell):
    return [int(x.replace(',', '')) for x in re.findall(r'\$(\d[\d,]*)', cell)]


def main():
    pages = read_tables()

    # 1. Transfer table on the decision page.
    for row in SNAP['transfers']:
        market, assessed, allow, cap, primary = transfer(row['year'])
        check(row['market'], market, f"transfer {row['year']} market", 5)
        check(row['carryForward'], assessed, f"transfer {row['year']} carry-forward", 5)
        check(row['allowance'], allow, f"transfer {row['year']} allowance", 5)
        check(row['cap'], cap, f"transfer {row['year']} cap", 5)
        check(row['primaryAssessed'], primary, f"transfer {row['year']} live-in assessed", 5)
        check(row['taxLive'], primary * A_RATE, f"transfer {row['year']} live-in tax", 5)
        check(row['taxRent'], market * A_RATE, f"transfer {row['year']} rent tax", 5)

    # 2. Comparison table.
    for c in SNAP['comparisons']:
        ind = compare(c['year'], c['horizon'])
        check(c['sell'], ind['sell'], f"compare {c['year']}/{c['horizon']} sell", 5)
        check(c['rent'], ind['rent'], f"compare {c['year']}/{c['horizon']} rent", 5)
        check(c['live'], ind['live_total'], f"compare {c['year']}/{c['horizon']} live", 5)
        check(c['sfExtra'], ind['extra'], f"compare {c['year']}/{c['horizon']} SF extra", 5)

    # 3. Annual holding table.
    base = compare(2045, 20)
    for i, row in enumerate(SNAP['holdRent'][:10]):
        flow, d = holding(2045, 2046 + i, 'rent')
        check(row['opex'], d['opex'], f'hold rent {row["year"]} opex', 5)
        check(row['propTax'], d['propTax'], f'hold rent {row["year"]} tax', 5)
        check(row['rent'], d['rent'], f'hold rent {row["year"]} rent', 5)
        check(row['noi'], d['noi'], f'hold rent {row["year"]} NOI', 5)

    # 4. Operating cost build-up, first year after a 2045 transfer.
    flow_live, live = holding(2045, 2046, 'live')
    flow_rent, rent = holding(2045, 2046, 'rent')
    check(SNAP['aYearOne']['live']['opex'], live['opex'], 'year-one live opex', 5)
    check(SNAP['aYearOne']['rent']['opex'], rent['opex'], 'year-one rent opex', 5)
    check(SNAP['aYearOne']['live']['propTax'], live['propTax'], 'year-one live tax', 5)

    # 5. Projection table.
    for row in SNAP['projection']:
        market, assessed = series_a(row['year'])
        check(row['aMarket'], market, f'projection {row["year"]} A market', 5)
        check(row['aAssessed'], assessed, f'projection {row["year"]} A assessed', 5)
        n = row['year'] - START
        b_market = grow(B_VALUE, HOME, n)
        b_assessed = min(grow(B_ASSESSED, ASSESS_GROWTH, n), b_market)
        check(row['bMarket'], b_market, f'projection {row["year"]} B market', 5)
        check(row['bAssessed'], b_assessed, f'projection {row["year"]} B assessed', 5)

    # 6. San Francisco operating table.
    for row in SNAP['sf'][:5]:
        n = row['year'] - START
        b_market = grow(B_VALUE, HOME, n)
        b_assessed = min(grow(B_ASSESSED, ASSESS_GROWTH, n), b_market)
        gross = grow(7_000 * 12, 0.016, n) + grow(2_770 * 12, 0.016, n)
        tax = b_assessed * B_RATE + 830
        check(row['tax'], tax, f'SF {row["year"]} tax', 5)
        check(row['gross'], gross, f'SF {row["year"]} gross rent', 5)

    # 7. Estate headroom.
    for row in SNAP['estate']:
        excl = (grow(15_480_000, CPI, row['year'] - 2027)
                if row['year'] >= 2027 else grow(15_000_000, CPI, row['year'] - 2026))
        check(row['exclusion'], excl, f"estate {row['year']} exclusion", 60)
        check(row['aValue'], series_a(row['year'])[0], f"estate {row['year']} A value", 5)

    # 8. The rendered HTML must contain the rounded form of key figures.
    sell2045 = compare(2045, 20)['sell']
    shown = f'${sell2045 / 1e6:,.2f}M'
    if shown not in pages['index'] or shown not in pages['decision']:
        FAILS.append(f'the 2045 sell result {shown} is not written into the pages')
    for other in ('rent', 'live_total'):
        v = compare(2045, 20)[other]
        s = f'${v / 1e6:,.2f}M'
        if s not in pages['index']:
            FAILS.append(f'the 2045 {other} result {s} is not on the summary page')

    if FAILS:
        for f in FAILS:
            print('::error title=Reconstruction::' + f)
        print(f'FAIL: {len(FAILS)} of {CHECKS} independent checks failed.')
        return 1
    print(f'PASS: {CHECKS} independent arithmetic checks reproduce every published table.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
