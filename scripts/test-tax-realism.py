#!/usr/bin/env python3
"""Independent reconstruction of the depreciation / recapture / exclusion engine.

No household data are read. The public engine in guide/data/tax-realism.js is run in
node across every control combination; this file recomputes the same arithmetic from
the published IRS rules with separate Python formulas and compares unrounded values.
It also re-runs the two worked examples the IRS publishes in Pub. 523 and checks the
result against the number the IRS prints, and checks that the synthetic property
inputs this page uses are the same ones the comparison page uses.
"""
import json
import pathlib
import math
import subprocess

script = r'''
global.window=global;
require('./guide/data/model.js'); require('./guide/data/tax-realism.js');
const T=window.TAXREALISM, out={scenarios:[],imputed:[],worked:[]};
for (const p of T.PATTERNS) for (const y of T.YEARS) for (const s of T.SHARES)
for (const f of T.FILINGS) for (const r of T.CG_RATES)
  out.scenarios.push({p:p.key,y:y,s:s,f:f.key,r:r,res:T.evaluate({pattern:p.key,years:y,share:s,filing:f.key,cgRate:r})});
for (const y of T.YEARS) for (const m of T.IMPUTED_RENTS)
  out.imputed.push({y,m,res:T.imputedRent({years:y},m)});
// The two worked examples printed by the IRS in Pub. 523 (2025), read 17 Nov 2026.
out.worked.push({name:'Finley', res:T.worksheet3({basis:400000, depreciation:20000, salePrice:700000, ownedYears:5, nonuseYears:2, exclusionLimit:250000})});
out.worked.push({name:'Taylor', res:T.worksheet3({basis:400000, depreciation:27000, salePrice:600000, ownedYears:5, nonuseYears:0, exclusionLimit:250000})});
console.log(JSON.stringify({base:MODEL.BASE, out}));
'''
obj = json.loads(subprocess.check_output(['node', '-e', script], text=True))
b = obj['base']
out = obj['out']
checks = 0


def near(actual, expected, label):
    global checks
    checks += 1
    if not math.isclose(actual, expected, rel_tol=2e-12, abs_tol=1e-5):
        raise AssertionError(f'{label}: independent reconstruction differs ({actual!r} vs {expected!r})')


# --- the comparison page's synthetic example, reconstructed independently -------------
def series_a(year, c):
    n = year - c['startYear']
    market = c['aValue'] * (1 + c['appreciation']) ** n
    factored = c['aAssessed'] * (1 + c['assessmentGrowth']) ** n
    return market, min(market, factored)


def allowance(year, c):
    if year < 2023:
        return 1000000
    if year < 2025:
        return 1022600
    if year <= 2026:
        return c['prop19Amount']
    steps = max(0, (year - 2025) // 2)
    return c['prop19Amount'] * (1 + c['prop19Index']) ** steps


def transfer(year, c):
    market, assessed = series_a(year, c)
    return min(market, max(assessed, market - allowance(year, c)))


def operating(year, option, c):
    """Reconstruction of MODEL.annualA's net operating income before depreciation."""
    t = c['inheritYear']
    market, _ = series_a(year, c)
    start = transfer(t, c) if option == 'live' else series_a(t, c)[0]
    assessed = min(market, start * (1 + c['assessmentGrowth']) ** (year - t))
    n = year - c['startYear']
    costs = (assessed * c['aRate']
             + c['aWaterMonthly'] * 12 * (1 + c['expenseInflation']) ** n
             + c['aInsuranceAnnual'] * (1 + c['expenseInflation']) ** n
             + market * c['maintenanceA'] - c['aSolarMonthlyCredit'] * 12)
    if option == 'live':
        return -costs
    gross = c['aRentMonthly'] * 12 * (1 + c['rentGrowth']) ** n
    return gross * (1 - c['vacancy']) * (1 - c['management']) - costs


# --- the rules, reconstructed independently ------------------------------------------
RECOVERY_YEARS = 27.5          # Pub. 527, GDS recovery period, residential rental property
MID_MONTH = 11.5 / 12          # Pub. 527, mid-month convention
UNRECAPTURED_RATE = 0.25       # IRS Topic 409, maximum rate on unrecaptured section 1250 gain
EXCLUSION = {'single': 250000, 'joint': 500000}   # Pub. 523


def occupancy(pattern, years):
    modes = []
    for y in range(1, years + 1):
        if pattern == 'rent_all':
            modes.append('rent')
        elif pattern == 'live_all':
            modes.append('live')
        elif pattern == 'live_then_rent':
            modes.append('live' if y <= 2 else 'rent')
        else:
            modes.append('rent' if y <= years - 2 else 'live')
    return modes


def depreciation_schedule(building_basis, rental_years):
    annual = building_basis / RECOVERY_YEARS
    rows = []
    total = 0.0
    if rental_years >= 2:
        for i in range(1, rental_years + 1):
            amount = annual * (MID_MONTH if i in (1, rental_years) else 1.0)
            total += amount
            rows.append({'year': i, 'amount': amount, 'cumulative': total})
    return rows, total, annual


def worksheet3(basis, depreciation, sale_price, owned_years, nonuse_years, limit):
    adjusted = basis - depreciation
    gain = sale_price - adjusted
    unrecaptured = max(0.0, min(depreciation, gain))
    net_gain = max(0.0, gain - unrecaptured)
    factor = nonuse_years / owned_years if owned_years else 0.0
    nonqualified = net_gain * factor
    eligible = max(0.0, net_gain - nonqualified)
    exclusion = min(eligible, limit)
    return {'gain': gain, 'unrecaptured': unrecaptured, 'netGain': net_gain,
            'factor': factor, 'nonqualified': nonqualified, 'eligible': eligible,
            'exclusion': exclusion, 'taxable': max(0.0, eligible - exclusion)}


def evaluate(pattern, years, share, filing, cg_rate):
    c = dict(b, inheritYear=2045)
    modes = occupancy(pattern, years)
    rental_years = modes.count('rent')
    residence_in_window = sum(1 for i, m in enumerate(modes) if m == 'live' and (i + 1) > years - 5)
    eligible = residence_in_window >= 2 and years >= 2
    nonuse_years = rental_years if pattern == 'rent_then_live' else 0
    basis = c['aValue'] * (1 + c['appreciation']) ** (2045 - c['startYear'])
    sale_value = c['aValue'] * (1 + c['appreciation']) ** (2045 + years - c['startYear'])
    net_proceeds = sale_value * (1 - c['saleCost'])
    dep_rows, accumulated, annual = depreciation_schedule(basis * share, rental_years)
    ws = worksheet3(basis, accumulated, net_proceeds, years, nonuse_years,
                    EXCLUSION[filing] if eligible else 0.0)
    tax_unrecaptured = ws['unrecaptured'] * UNRECAPTURED_RATE
    tax_capital = ws['taxable'] * cg_rate
    cash = 0.0
    shield = 0.0
    suspended = 0.0
    rows = []
    dep_index = 0
    for i, mode in enumerate(modes):
        year = 2045 + i + 1
        flow = operating(year, mode, c)
        noi = flow if mode == 'rent' else 0.0
        housing_cost = -flow if mode == 'live' else 0.0
        dep = 0.0
        if mode == 'rent' and dep_index < len(dep_rows):
            dep = dep_rows[dep_index]['amount']
            dep_index += 1
        taxable = max(0.0, noi - dep)
        tax = taxable * c['ordinaryTax']
        suspended += max(0.0, dep - max(0.0, noi))
        shield += min(dep, max(0.0, noi)) * c['ordinaryTax']
        cash += noi - housing_cost - tax
        rows.append({'noi': noi, 'housingCost': housing_cost, 'depreciation': dep,
                     'taxable': taxable, 'tax': tax, 'afterTaxCash': noi - housing_cost - tax})
    return {'residenceYears': years - rental_years, 'rentalYears': rental_years,
            'residenceInWindow': residence_in_window, 'eligible121': eligible,
            'nonuseFactor': ws['factor'], 'basis': basis, 'saleValue': sale_value,
            'netProceeds': net_proceeds, 'annualDepreciation': annual,
            'accumulatedDepreciation': accumulated, 'totalGain': ws['gain'],
            'unrecaptured': ws['unrecaptured'], 'remainder': ws['netGain'],
            'nonqualifiedGain': ws['nonqualified'], 'exclusionUsed': ws['exclusion'],
            'taxableCapital': ws['taxable'], 'federalTax': tax_unrecaptured + tax_capital,
            'afterTaxProceeds': net_proceeds - tax_unrecaptured - tax_capital,
            'cumulativeCash': cash, 'cumulativeShield': shield,
            'suspendedDepreciation': suspended,
            'total': cash + net_proceeds - tax_unrecaptured - tax_capital,
            'rows': rows, 'depRows': dep_rows}


for item in out['scenarios']:
    got = item['res']
    exp = evaluate(item['p'], item['y'], item['s'], item['f'], item['r'])
    where = f"{item['p']} {item['y']}y share {item['s']} {item['f']} {item['r']:.0%}"
    near(got['residenceYears'], exp['residenceYears'], where + ' residence years')
    near(got['rentalYears'], exp['rentalYears'], where + ' rental years')
    near(got['residenceInWindow'], exp['residenceInWindow'], where + ' residence in 5-year window')
    near(got['nonuseFactor'], exp['nonuseFactor'], where + ' nonqualified-use factor')
    near(got['basis'], exp['basis'], where + ' basis')
    near(got['saleValue'], exp['saleValue'], where + ' sale value')
    near(got['netProceeds'], exp['netProceeds'], where + ' net proceeds')
    near(got['annualDepreciation'], exp['annualDepreciation'], where + ' annual depreciation')
    near(got['accumulatedDepreciation'], exp['accumulatedDepreciation'], where + ' accumulated depreciation')
    near(got['totalGain'], exp['totalGain'], where + ' total gain')
    near(got['unrecaptured'], exp['unrecaptured'], where + ' unrecaptured 1250 gain')
    near(got['remainder'], exp['remainder'], where + ' gain net of depreciation')
    near(got['nonqualifiedGain'], exp['nonqualifiedGain'], where + ' nonqualified-use gain')
    near(got['exclusionUsed'], exp['exclusionUsed'], where + ' exclusion used')
    near(got['taxableCapital'], exp['taxableCapital'], where + ' taxable capital gain')
    near(got['federalTax'], exp['federalTax'], where + ' federal tax')
    near(got['afterTaxProceeds'], exp['afterTaxProceeds'], where + ' after-tax proceeds')
    near(got['cumulativeCash'], exp['cumulativeCash'], where + ' cumulative cash')
    near(got['cumulativeShield'], exp['cumulativeShield'], where + ' cumulative shield')
    near(got['suspendedDepreciation'], exp['suspendedDepreciation'], where + ' suspended depreciation')
    near(got['total'], exp['total'], where + ' total')
    checks += 1
    assert got['eligible121'] is exp['eligible121'], where + ' exclusion eligibility'
    assert len(got['annual']) == len(exp['rows']) == item['y'], where + ' annual row count'
    assert len(got['depreciationRows']) == len(exp['depRows']), where + ' depreciation row count'
    for i, (a, e) in enumerate(zip(got['annual'], exp['rows'])):
        near(a['noi'], e['noi'], f'{where} year {i + 1} net operating income')
        near(a['depreciation'], e['depreciation'], f'{where} year {i + 1} depreciation')
        near(a['taxable'], e['taxable'], f'{where} year {i + 1} taxable rental income')
        near(a['tax'], e['tax'], f'{where} year {i + 1} rental tax')
        near(a['afterTaxCash'], e['afterTaxCash'], f'{where} year {i + 1} after-tax cash')
    for i, (a, e) in enumerate(zip(got['depreciationRows'], exp['depRows'])):
        near(a['amount'], e['amount'], f'{where} depreciation year {i + 1} amount')
        near(a['cumulative'], e['cumulative'], f'{where} depreciation year {i + 1} cumulative')

# --- the IRS's own worked examples, checked against the numbers the IRS prints -------
worked = {w['name']: w['res'] for w in out['worked']}
finley = worked['Finley']
near(finley['gain'], 320000, 'Finley total gain (Pub. 523 prints $320,000)')
near(finley['netGain'], 300000, 'Finley gain net of depreciation (Pub. 523 prints $300,000)')
near(finley['nonqualified'], 120000, 'Finley nonqualified-use gain (Pub. 523 prints $120,000)')
near(finley['exclusion'], 180000, 'Finley excluded gain (Pub. 523 prints $180,000)')
near(finley['unrecaptured'], 20000, 'Finley depreciation recapture (Pub. 523 prints $20,000)')
near(finley['taxable'], 0, 'Finley taxable gain (Pub. 523 leaves none taxable)')
taylor = worked['Taylor']
near(taylor['gain'], 227000, 'Taylor total gain (Pub. 523 prints $227,000)')
near(taylor['netGain'], 200000, 'Taylor gain net of depreciation (Pub. 523 prints $200,000)')
near(taylor['exclusion'], 200000, 'Taylor excluded gain (Pub. 523 prints $200,000)')
near(taylor['unrecaptured'], 27000, 'Taylor depreciation recapture (Pub. 523 prints $27,000)')
near(taylor['taxable'], 0, 'Taylor taxable gain (Pub. 523 leaves none taxable)')

# --- imputed rent, reconstructed independently --------------------------------------
for item in out['imputed']:
    got = item['res']
    years = item['y']
    live = evaluate('live_all', years, 0.8, 'single', 0.20)
    rent = evaluate('rent_all', years, 0.8, 'single', 0.20)
    residence_years = max(1, live['residenceYears'])
    factor = sum((1 + b['rentGrowth']) ** i for i in range(residence_years))
    needed = rent['total'] - live['total']
    near(got['liveTotal'], live['total'], f'imputed {years}y live total')
    near(got['rentTotal'], rent['total'], f'imputed {years}y rent total')
    near(got['factor'], factor, f'imputed {years}y rent-growth factor')
    near(got['needed'], needed, f'imputed {years}y rent needed to match')
    near(got['breakevenMonthly'], needed / (12 * factor), f'imputed {years}y break-even monthly rent')
    near(got['cumulativeImputed'], item['m'] * 12 * factor, f'imputed {years}y cumulative at {item["m"]}')
    near(got['gap'], needed - item['m'] * 12 * factor, f'imputed {years}y gap')

# --- the two pages must describe the same fictional property ------------------------
# The engine takes its property inputs from MODEL.BASE rather than restating them, so
# the two pages cannot drift apart. Check that it really does, and that no synthetic
# input literal has been copied into it.
engine = pathlib.Path('guide/data/tax-realism.js').read_text(encoding='utf8')
checks += 1
assert 'M.BASE' in engine or 'MODEL.BASE' in engine, 'engine must take its inputs from the comparison model'
checks += 1
assert 'window.MODEL' in engine, 'engine must read the published synthetic model'
for literal in ('1240000', '398000', '4400', '2240', '1044586'):
    checks += 1
    assert literal not in engine, f'synthetic input {literal} must not be restated in the engine'

print(f'PASS: independently reconstructed {len(out["scenarios"])} depreciation/recapture scenarios, '
      f'{sum(len(s["res"]["annual"]) for s in out["scenarios"])} annual rows, '
      f'{len(out["imputed"])} imputed-rent cases and both IRS worked examples; {checks} comparisons.')
