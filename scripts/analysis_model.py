#!/usr/bin/env python3
"""Deterministic decision engine for the inheritance guide (pure functions, no I/O).

The same engine produces (a) the public illustrative examples and (b) the
private household analysis. The private output is written to the git-ignored
private/ folder and is never committed or published.

Official benchmarks are listed in OFFICIAL with their source. Every other number
is an input supplied by the caller and labelled as such. Results are stylised
projections, not forecasts, and not tax or legal advice.
"""
from __future__ import annotations
import math

# --- Official benchmarks (each read on 14 Nov 2026; see verification/12f68358/REPORT.md)
OFFICIAL = {
    'fed_exclusion_2026': 15_000_000,        # IRS, basic exclusion amount for 2026
    'fed_exclusion_2027': 15_480_000,        # IRS, 2027 (IR-2026-133)
    'prop19_allowance_exact': 1_044_586,     # BOE LTA 2025/009 (16 Feb 2025 - 15 Feb 2027)
    # BOE LTA 2025/009 quoting article XIII A section 2.1(c)(4): the $1 million amount is adjusted
    # every other 16 February, beginning 2023, by the percentage change in the House Price Index
    # for California for the prior calendar year as determined by the Federal Housing Finance Agency.
    # FHFA's 2024 California change, quoted in that letter, was 2.15 percent.
    'prop19_hpi_2024': 0.0215,
    'prop19_first_index_year': 2025,
    'prop13_cap': 0.02,                      # BOE: assessed value grows at most 2% a year
    'sf_rent_increase_26_27': 0.016,         # sf.gov Rent Board, 1 Mar 2026 - 28 Feb 2027
    'prop_h_floor': 249,                     # SFMTA Prop H FY 2027-28, multifamily up to 5,000 sq ft
    'prop_h_cap': 50_000,                    # SFMTA Prop H FY 2027-28, cap
    # SFMTA Proposition H: first tax on FY 2027-28 bills, amounts rise with inflation starting
    # FY 2028-29, and the tax runs 1 July 2027 through 30 June 2042.
    'prop_h_first_year': 2028,               # calendar year of the first bill (FY 2027-28)
    'prop_h_index_from_year': 2029,          # first inflation adjustment (FY 2028-29)
    'prop_h_last_year': 2042,                # last calendar year of the tax (ends 30 June 2042)
    'prop_h_renter_cap': 65,                 # SFMTA: renter pass-through capped at $65 a unit a year
    'irs121_single': 250_000,                # IRS Topic 701: $250,000 / $500,000 home-sale exclusion
    'irs121_joint': 500_000,
    'ca_cgt_top': 0.123,                     # FTB 2025 rate schedules, top marginal rate
    'ca_bhs_rate': 0.01,                     # FTB 2025 Form 540 instructions, line 62: 1% over $1,000,000
    'dtt_rate': 0.0011,                      # Santa Clara County: 55c per $500 = $110 per $100,000
    'treasury_3m': 0.0432,                   # FRED DGS3MO, 12 Nov 2026
    'treasury_2y': 0.0486,                   # FRED DGS2, 12 Nov 2026
    'cpi_mean_35y': 0.0262,                  # FRED CPIAUCNS, 35-year mean (ledger, 330ce4c5)
    'cpi_max_35y': 0.0800,                   # FRED CPIAUCNS, 35-year maximum
    'dow_peak': 381.17, 'dow_trough': 41.22, # Federal Reserve History: 1929-1932
    'dow_months_peak_to_trough': 34,         # 3 Sep 1929 to 8 Jul 1932
    'dow_recovery_months': 303,              # 3 Sep 1929 to 23 Nov 1954 (first close above old high)
    'sp500_drop_2007_09': 0.57,              # Federal Reserve History: Oct 2007 to Mar 2009
    'sp500_months_2007_09': 17,              # Oct 2007 to Mar 2009
    'hpi_sj_1975q3': 18.60, 'hpi_sj_1981q1': 48.69,   # FHFA ATNHPIUS41940Q via FRED
    'hpi_sj_2006q3': 320.14, 'hpi_sj_2009q3': 235.72,
    'hpi_sj_2026q2': 558.75,
    'niit': 0.038,                           # IRS topic 559
    'ltcg_top': 0.20,                        # IRS topic 409 (2025 thresholds)
}


def cagr(a: float, b: float, years: float) -> float:
    return (b / a) ** (1.0 / years) - 1.0


G_20Y = cagr(OFFICIAL['hpi_sj_2006q3'], OFFICIAL['hpi_sj_2026q2'], 19.75)     # about 2.9%
G_51Y = cagr(OFFICIAL['hpi_sj_1975q3'], OFFICIAL['hpi_sj_2026q2'], 50.75)     # about 6.9%
G_1970S = cagr(OFFICIAL['hpi_sj_1975q3'], OFFICIAL['hpi_sj_1981q1'], 5.5)     # about 19%
HPI_DD_2008 = OFFICIAL['hpi_sj_2009q3'] / OFFICIAL['hpi_sj_2006q3'] - 1.0     # about -26.4%
DOW_RATIO = OFFICIAL['dow_trough'] / OFFICIAL['dow_peak']                     # about 0.108
SP_RATIO_2008 = 1.0 - OFFICIAL['sp500_drop_2007_09']                          # 0.43

DEFAULT_PARAMS = {
    'valuation_year': 2026,
    'inherit_year': 2045,
    'g_pre': (G_20Y + G_51Y) / 2,     # growth 2026 to inheritance: midpoint of the two FHFA CAGRs
    'g_post': (G_20Y + G_51Y) / 2,    # growth after inheritance (same midpoint; what-if)
    'g_low_post': G_20Y,              # growth after a crash drawdown (low FHFA CAGR)
    'mu_equity': 0.06,                # ASSUMPTION: nominal equity return (no official forecast used)
    'cash_yield': OFFICIAL['treasury_3m'],
    'cpi': OFFICIAL['cpi_mean_35y'],
    'vacancy': 0.05,                  # ASSUMPTION
    'sale_cost': 0.06,                # ASSUMPTION: selling costs, negotiated
    'fed_cgt': OFFICIAL['ltcg_top'] + OFFICIAL['niit'],
    'ca_cgt': 0.133,                  # UNVERIFIED in an official source (see flagged items)
    'phase_months': 24,               # park proceeds 24 months (range 24 to 36 tested)
    'deploy_months': 12,              # then equal monthly tranches into equities
    'maint_a': 0.0075,                # ASSUMPTION: share of value per year
    'maint_b': 0.0125,                # ASSUMPTION: share of value per year
    'rent_mo': 0.0,                   # Property A monthly rent in inheritance-year dollars
    # Imputed rent for the living paths: the housing cost avoided by living in the house, or the
    # rent given up by not letting it. Set to the same benchmark the letting path uses, so that
    # living and letting are compared on equal terms. It is a benchmark, not a quote (see S19).
    'imputed_rent_mo': 6_390.0,
    # IRC section 121 exclusion for a living-then-sell path, applied only where the owner-occupies
    # the home. IRS Topic 701: up to $250,000 ($500,000 joint) after 24 months of ownership and use
    # in the 5 years ending on the sale. Applied to the living-then-sell paths (S20).
    'home_gain_exclusion': OFFICIAL['irs121_single'],
    # Costs of selling that are priced separately from the negotiated sale cost (S26). The county
    # documentary transfer tax is 55 cents per $500 of consideration. A transfer by reason of death
    # is exempt from that tax (R&TC section 11930), so it is charged on a later sale only.
    'transfer_tax_rate': OFFICIAL['dtt_rate'],
    'recording_fee': 0.0,             # ASSUMPTION: no official Santa Clara fee schedule was read
    'prop19_hpi': OFFICIAL['prop19_hpi_2024'],   # indexation basis for the allowance, carried forward
    'prop_h_index': 0.02,             # ASSUMPTION: SFMTA states inflation indexing without naming an index
    'ca_cgt': OFFICIAL['ca_cgt_top'] + OFFICIAL['ca_bhs_rate'],   # 12.3% top rate + 1% over $1m
}


def prop19_allowance(year: int, p: dict) -> float:
    """Proposition 19 allowance carried forward on the Board's published method.

    BOE LTA 2025/009: the amount is adjusted every other 16 February, beginning 2023, by the
    percentage change in the FHFA House Price Index for California for the prior calendar year.
    The 2024 change published in that letter is used here as the forward basis; future FHFA
    changes are not published yet, so every carried-forward year is a projection, not a figure.
    """
    steps = max(0, (year - OFFICIAL['prop19_first_index_year']) // 2)
    return OFFICIAL['prop19_allowance_exact'] * (1 + p.get('prop19_hpi', OFFICIAL['prop19_hpi_2024'])) ** steps


def prop_h_annual(year: int, p: dict) -> float:
    """SFMTA Proposition H parcel tax for one calendar year, on the official terms.

    First tax: FY 2027-28 bill (calendar 2028). Amounts rise with inflation starting FY 2028-29
    (calendar 2029). The tax ends 30 June 2042, so calendar 2042 is the last year charged.
    The amount used is the multifamily floor for a parcel up to 5,000 sq ft; parcel type and
    building area are not public facts, so this is a floor, not the amount for any real parcel.
    """
    if year < OFFICIAL['prop_h_first_year'] or year > OFFICIAL['prop_h_last_year']:
        return 0.0
    n = max(0, year - OFFICIAL['prop_h_index_from_year'] + 1)
    return OFFICIAL['prop_h_floor'] * (1 + p.get('prop_h_index', 0.02)) ** n


def _cpi_level(sc: dict, m: int) -> float:
    """Price level at month m, from monthly compounding of the scenario's annual inflation."""
    lvl = 1.0
    for k in range(m):
        lvl *= (1 + sc['cpi'](k)) ** (1 / 12)
    return lvl


def lvl_m_at_H(sc: dict, H: int) -> float:
    lvl = 1.0
    for k in range(H):
        lvl *= (1 + sc['cpi'](k)) ** (1 / 12)
    return lvl


def scenario(name: str, p: dict) -> dict:
    """Monthly index functions for a named scenario. m = 0 is the inheritance date.

    In the crash cases the crash starts at inheritance, a worst-case entry date.
    Each index equals 1.0 at m = 0 so that inheritance-date values carry over.
    """
    mu, g = p['mu_equity'], p['g_post']
    if name == 'base':
        eq = lambda m: (1 + mu) ** (m / 12)
        home = lambda m: (1 + g) ** (m / 12)
        cash = lambda m: p['cash_yield']
        cpi = lambda m: p['cpi']
    elif name == 'crash_1929':
        mo1 = OFFICIAL['dow_months_peak_to_trough']
        rec = OFFICIAL['dow_recovery_months'] - mo1
        def eq(m):
            if m <= mo1:
                return DOW_RATIO ** (m / mo1)
            if m <= mo1 + rec:
                return DOW_RATIO ** (1 - (m - mo1) / rec)
            return (1 + mu) ** ((m - mo1 - rec) / 12)
        # ASSUMPTION: home values fall 30% over 36 months, then grow at the low rate.
        home = lambda m: (1 - 0.30 * min(m, 36) / 36) * (1 + p['g_low_post']) ** (max(0, m - 36) / 12)
        cash = lambda m: p['cash_yield'] if m < 12 else 0.01              # ASSUMPTION: rates fall
        cpi = lambda m: -0.02 if m < 36 else p['cpi']                     # ASSUMPTION: deflation
    elif name == 'crash_2008':
        mo1 = OFFICIAL['sp500_months_2007_09']
        rec = 66                                                          # ASSUMPTION: months to regain peak
        def eq(m):
            if m <= mo1:
                return SP_RATIO_2008 ** (m / mo1)
            if m <= mo1 + rec:
                return SP_RATIO_2008 ** (1 - (m - mo1) / rec)
            return (1 + mu) ** ((m - mo1 - rec) / 12)
        home = lambda m: (1 + HPI_DD_2008 * min(m, 36) / 36) * (1 + p['g_low_post']) ** (max(0, m - 36) / 12)
        cash = lambda m: p['cash_yield'] if m < 6 else 0.005              # ASSUMPTION
        cpi = lambda m: p['cpi']
    elif name == 'stagflation_1970s':
        eq = lambda m: 1.0 if m < 120 else (1 + mu) ** ((m - 120) / 12)   # ASSUMPTION: flat nominal decade
        home = lambda m: (1 + G_1970S) ** (min(m, 66) / 12) * (1 + g) ** (max(0, m - 66) / 12)
        cash = lambda m: OFFICIAL['cpi_max_35y']                          # ASSUMPTION
        cpi = lambda m: OFFICIAL['cpi_max_35y'] if m < 36 else p['cpi']
    else:
        raise ValueError(name)
    return {'name': name, 'eq': eq, 'home': home, 'cash': cash, 'cpi': cpi}


SCENARIOS = ['base', 'crash_1929', 'crash_2008', 'stagflation_1970s']
SCENARIO_LABEL = {
    'base': 'Baseline (no crash)',
    'crash_1929': '1929-style crash',
    'crash_2008': '2008-style crash',
    'stagflation_1970s': '1970s-style stagflation',
}
PATHS = ['live', 'rent', 'sell_lump', 'sell_phased', 'mixed_live2_sell', 'mixed_rent5_sell', 'mixed_live10_sell']
PATH_LABEL = {
    'live': 'Live in it (never sell)',
    'rent': 'Rent it out (never sell)',
    'sell_lump': 'Sell at inheritance, invest all at once',
    'sell_phased': 'Sell at inheritance, phase into stocks',
    'mixed_live2_sell': 'Mixed: live 2 years, then sell and phase',
    'mixed_rent5_sell': 'Mixed: rent 5 years, then sell and phase',
    'mixed_live10_sell': 'Mixed: live 10 years, then sell and phase',
}


def fmv_at_inheritance(a: dict, p: dict) -> float:
    return a['fmv_now'] * (1 + p['g_pre']) ** (p['inherit_year'] - p['valuation_year'])


def cost_factor(p: dict) -> float:
    """Inflate current (2026) dollar costs to the inheritance year at the base inflation rate."""
    return (1 + p['cpi']) ** (p['inherit_year'] - p['valuation_year'])


def simulate(path: str, scen_name: str, p: dict, a: dict, horizon_years: int, *,
             rent_mo: float | None = None, sell_year: int | None = None) -> dict:
    """Simulate one strategy monthly from the inheritance date and return terminal wealth.

    Terminal wealth = liquid (cash + equities) + house (if still owned, at market).
    Nothing here is a forecast; it is a stylised comparison under stated assumptions.
    """
    sc = scenario(scen_name, p)
    H = horizon_years * 12
    fmv0 = fmv_at_inheritance(a, p)
    rent0 = p['rent_mo'] if rent_mo is None else rent_mo
    # Imputed rent is the housing cost the living paths avoid (or the rent given up by not letting
    # the house). It is credited only while the household occupies the home.
    imputed0 = p.get('imputed_rent_mo', 0.0) if rent_mo is None else rent_mo
    cf = cost_factor(p)
    rate = a['tax_2025'] / a['assessed_2025']                        # owner's own implied effective rate
    maint = p['maint_a'] if a.get('label', 'A') == 'A' else p['maint_b']
    # Sale timing
    if path in ('sell_lump', 'sell_phased'):
        sell_m = 0
    elif path == 'mixed_live2_sell':
        sell_m = 24
    elif path == 'mixed_rent5_sell':
        sell_m = 60
    elif path == 'mixed_live10_sell':
        sell_m = 120
    else:
        sell_m = None
    if sell_year is not None:
        sell_m = sell_year * 12
    living_until = {'live': H + 1, 'mixed_live2_sell': 24, 'mixed_live10_sell': 120}.get(path, 0)
    if path in ('rent', 'mixed_rent5_sell'):
        living_until = 0
    lump = path == 'sell_lump'
    cash, units = 0.0, 0.0
    lvl_m = 1.0                                   # CPI level at month m, compounded incrementally
    sale_value, cgt = None, 0.0
    house_held = True
    assessed = None
    annual = {}
    tax_total = cost_total = rent_total = avoided_total = 0.0
    for m in range(H + 1):
        fmv = fmv0 * sc['home'](m)
        living = m < living_until
        if house_held and (m % 12 == 0):
            if m == 0:
                # Prop 19 if living: excess of market over factored base above the allowance is
                # added to the factored base (BOE rule as published on the guide's tax page);
                # otherwise the transfer is reassessed to market value. Formula mirrors
                # guide/data/model.js inheritanceValues: min(market, max(factored, market - allowance)).
                factored = a['assessed_2026'] * (1 + OFFICIAL['prop13_cap']) ** (p['inherit_year'] - p['valuation_year'])
                allowance = prop19_allowance(p['inherit_year'], p)
                assessed = min(fmv, max(factored, fmv - allowance)) if living else fmv
            else:
                assessed = min(assessed * (1 + OFFICIAL['prop13_cap']), fmv)   # Prop 13 cap and Prop 8 decline-in-value
            cpi_lvl = lvl_m
            tax = rate * assessed
            ins = a['insurance_yr'] * cf * cpi_lvl
            water = a['water_mo'] * 12 * cf * cpi_lvl
            solar = a.get('solar_credit_mo', 0.0) * 12 * cf * cpi_lvl
            mcost = maint * fmv
            rent = 0.0 if living else rent0 * 12 * cf * cpi_lvl * (1 - p['vacancy'])
            avoided = imputed0 * 12 * cf * cpi_lvl if living else 0.0
            annual = {'tax': tax, 'ins': ins, 'water': water, 'solar': solar, 'maint': mcost, 'rent': rent, 'avoided': avoided}
            tax_total += tax
            cost_total += ins + water + mcost
            rent_total += rent
            avoided_total += avoided
        if sell_m is not None and m == sell_m and house_held and path not in ('live', 'rent'):
            # Costs of selling are negotiated costs plus the county documentary transfer tax
            # (S26). A transfer by reason of death is exempt from that tax under R&TC section
            # 11930, so it is charged here, on a later sale, and not on the inheritance itself.
            net = fmv * (1 - p['sale_cost'] - p.get('transfer_tax_rate', 0.0)) - p.get('recording_fee', 0.0) * cf
            gain = max(0.0, net - fmv0)                       # basis is value at death (IRC 1014)
            # Primary-residence gain exclusion (IRC 121: $250,000 single / $500,000 joint, IRS
            # Topic 701), applied to living-then-sell paths where the household occupies the home
            # for at least 24 of the 5 years ending on the sale (S20).
            excl = p.get('home_gain_exclusion', 0.0) if path in ('mixed_live2_sell', 'mixed_live10_sell') else 0.0
            cgt = max(0.0, gain - excl) * (p['fed_cgt'] + p['ca_cgt'])
            sale_value = net - cgt
            house_held = False
            cash += sale_value
            if lump:
                units += cash / sc['eq'](m)
                cash = 0.0
            deploy_start = m + p['phase_months']
            tranche = sale_value / p['deploy_months'] if not lump else 0.0
        if m == H:
            break
        lvl_m *= (1 + sc['cpi'](m)) ** (1 / 12)
        # Monthly cash flow from the house (only while held) and compounding of cash
        if house_held and annual:
            flow = (annual['rent'] + annual['avoided'] + annual['solar'] - annual['tax'] - annual['ins'] - annual['water'] - annual['maint']) / 12
        else:
            flow = 0.0
        cash = cash * (1 + sc['cash'](m)) ** (1 / 12) + flow
        if sale_value is not None and not lump and m >= deploy_start and m < deploy_start + p['deploy_months']:
            amt = min(max(cash, 0.0), tranche)
            units += amt / sc['eq'](m)
            cash -= amt
    liquid = cash + units * sc['eq'](H)
    house_val = fmv0 * sc['home'](H) if house_held else 0.0
    total = liquid + house_val
    lvl = lvl_m_at_H(sc, H)
    return {
        'path': path, 'scenario': scen_name, 'horizon_years': horizon_years,
        'total': total, 'real_total': total / lvl, 'liquid': liquid, 'house': house_val,
        'sale_value': sale_value, 'cgt': cgt, 'fmv0': fmv0,
        'property_tax_paid': tax_total, 'holding_costs': cost_total,
        'rent_income': rent_total, 'avoided_rent': avoided_total,
        'cpi_level': lvl,
    }


def solve(f, lo: float, hi: float, target: float = 0.0, iters: int = 60) -> float | None:
    """Bisection for f(x) = target when f is monotone; None if no sign change in [lo, hi]."""
    flo, fhi = f(lo) - target, f(hi) - target
    if flo == 0:
        return lo
    if flo * fhi > 0:
        return None
    for _ in range(iters):
        mid = (lo + hi) / 2
        fm = f(mid) - target
        if fm == 0:
            return mid
        if (fm < 0) == (flo < 0):
            lo, flo = mid, fm
        else:
            hi = mid
    return (lo + hi) / 2


def breakeven_rent(a: dict, p: dict, horizon_years: int, scen: str = 'base', vs: str = 'sell_phased') -> float | None:
    """Monthly rent (inheritance-year dollars) at which living equals selling and phasing."""
    target = simulate(vs, scen, p, a, horizon_years)['total']
    return solve(lambda r: simulate('live', scen, p, a, horizon_years, rent_mo=r)['total'], 0.0, 20_000.0, target)


def breakeven_growth(a: dict, p: dict, horizon_years: int, scen: str = 'base', vs: str = 'sell_phased') -> float | None:
    """Post-inheritance house growth at which living equals selling and phasing."""
    def diff(g):
        q = dict(p, g_post=g)
        return simulate('live', scen, q, a, horizon_years)['total'] - simulate(vs, scen, q, a, horizon_years)['total']
    return solve(diff, -0.05, 0.15)


def breakeven_equity(a: dict, p: dict, horizon_years: int, scen: str = 'base') -> float | None:
    """Equity return at which selling (phased) and living are equal."""
    def diff(mu):
        q = dict(p, mu_equity=mu)
        return simulate('sell_phased', scen, q, a, horizon_years)['total'] - simulate('live', scen, q, a, horizon_years)['total']
    return solve(diff, -0.05, 0.20)


def grid(a: dict, p: dict, horizons=(10, 25, 50)) -> dict:
    """Terminal wealth for every path, scenario and horizon, plus the regret summary."""
    out = {}
    for s in SCENARIOS:
        for h in horizons:
            for path in PATHS:
                out[(s, h, path)] = simulate(path, s, p, a, h)
    table = {}
    for h in horizons:
        best_by_s = {}
        for s in SCENARIOS:
            best_by_s[s] = max(PATHS, key=lambda x: out[(s, h, x)]['total'])
        # regret = best in this scenario minus this path, maximised over scenarios
        regret = {}
        for path in PATHS:
            regret[path] = max(out[(s, h, best_by_s[s])]['total'] - out[(s, h, path)]['total'] for s in SCENARIOS)
        table[h] = {'best_by_scenario': best_by_s, 'max_regret': regret}
    return {'results': out, 'summary': table}


def estate_headroom(a: dict, p: dict) -> dict:
    """Federal estate-tax check for the donor's estate only (Property B is owned by the heir)."""
    y = p['inherit_year']
    if y <= 2026:
        excl = OFFICIAL['fed_exclusion_2026']
    elif y == 2027:
        excl = OFFICIAL['fed_exclusion_2027']
    else:
        # ASSUMPTION: exclusion indexed for inflation after 2027 (not law; what-if only)
        excl = OFFICIAL['fed_exclusion_2027'] * (1 + p['cpi']) ** (y - 2027)
    fmv = fmv_at_inheritance(a, p)
    return {'exclusion': excl, 'house_fmv': fmv, 'other_assets_headroom': excl - fmv}


def prop_b_year(b: dict, p: dict, years: int) -> dict:
    """Property B: owned by the heir, not part of the donor estate. Constant across Cupertino paths."""
    t = years
    cf = (1 + p['cpi']) ** t
    value = b['fmv_now'] * (1 + p['g_pre']) ** t
    assessed = b['assessed_2025'] * (1 + OFFICIAL['prop13_cap']) ** (t + (2026 - 2025))
    rate = b['tax_2025'] / b['assessed_2025']
    tax = rate * min(assessed, value)
    rent = b['rent_mo'] * 12 * (1 + OFFICIAL['sf_rent_increase_26_27']) ** t * (1 - p['vacancy'])
    water = b['water_mo'] * 12 * cf
    elec = b['elec_mo'] * 12 * cf
    ins = b['insurance_yr'] * cf
    maint = p['maint_b'] * value
    # Proposition H on the official terms: floor of the FY 2027-28 schedule for a multifamily
    # parcel up to 5,000 sq ft, inflation-adjusted from FY 2028-29, ending after 30 June 2042.
    prop_h = prop_h_annual(2026 + t, p)
    net = rent - tax - water - elec - ins - maint - prop_h
    return {'year_offset': t, 'value': value, 'assessed': assessed, 'tax': tax, 'rent': rent,
            'water': water, 'electricity': elec, 'insurance': ins, 'maintenance': maint,
            'prop_h_floor': prop_h, 'net': net}


if __name__ == '__main__':
    print('G_20Y %.4f G_51Y %.4f G_1970S %.4f HPI_DD_2008 %.4f' % (G_20Y, G_51Y, G_1970S, HPI_DD_2008))


def annual_table(a: dict, p: dict, years: int = 50) -> list[dict]:
    """Calendar-year projection for Property A (before and after inheritance, base scenario).

    Before the inheritance year: the decedent's Prop 13 assessment (2% cap, Prop 8 decline-in-value).
    From the inheritance year: the living-path assessment (Prop 19) with Prop 13 growth from there.
    All dollar values are nominal. The rate is the owner's implied effective rate.
    """
    rate = a['tax_2025'] / a['assessed_2025']
    cf_now = lambda y: (1 + p['cpi']) ** (y - p['valuation_year'])
    rows = []
    assessed_pre = a['assessed_2026']
    sc = scenario('base', p)
    for i in range(years):
        y = p['valuation_year'] + i
        fmv = a['fmv_now'] * (1 + p['g_pre']) ** i if y < p['inherit_year'] else None
        if y < p['inherit_year']:
            if i > 0:
                assessed_pre = min(assessed_pre * (1 + OFFICIAL['prop13_cap']), fmv)
            tax = rate * assessed_pre
            rows.append({'year': y, 'fmv': fmv, 'assessed': assessed_pre, 'tax': tax,
                         'insurance': a['insurance_yr'] * cf_now(y),
                         'water': a['water_mo'] * 12 * cf_now(y),
                         'solar_credit': a.get('solar_credit_mo', 0.0) * 12 * cf_now(y),
                         'maintenance': p['maint_a'] * fmv, 'phase': 'held by decedent (not our cost)'})
        else:
            k = y - p['inherit_year']
            fmv_inh = fmv_at_inheritance(a, p)
            fmv = fmv_inh * sc['home'](12 * k)
            factored = a['assessed_2026'] * (1 + OFFICIAL['prop13_cap']) ** (p['inherit_year'] - p['valuation_year'])
            allowance = prop19_allowance(p['inherit_year'], p)
            assessed_live = min(fmv_inh, max(factored, fmv_inh - allowance)) if k == 0 else None
            if k == 0:
                assessed = assessed_live
            else:
                assessed = min(rows[-1]['assessed'] * (1 + OFFICIAL['prop13_cap']), fmv)
            tax = rate * assessed
            rows.append({'year': y, 'fmv': fmv, 'assessed': assessed, 'tax': tax,
                         'insurance': a['insurance_yr'] * cf_now(y),
                         'water': a['water_mo'] * 12 * cf_now(y),
                         'solar_credit': a.get('solar_credit_mo', 0.0) * 12 * cf_now(y),
                         'maintenance': p['maint_a'] * fmv, 'phase': 'after inheritance (living path shown)'})
    return rows
