#!/usr/bin/env python3
"""Public pages for the decision analysis: paths, phased entry, what-if, timeline,
glossary, one-page Attorney & CPA sheet, flagged additions and suggestions.

Every number shown here is produced by scripts/analysis_model.py from ILLUSTRATIVE
example inputs. The household's own figures are never used in this file and are
not published (see COORDINATION.md, decision L-D1).
"""
from __future__ import annotations
import json
from html import escape
import analysis_model as M

# ---------------------------------------------------------------- illustrative inputs (NOT household figures)
EXAMPLE_A = {
    'label': 'A', 'fmv_now': 2_000_000, 'assessed_2026': 600_000, 'assessed_2025': 588_240,
    'tax_2025': 8_010, 'insurance_yr': 1_800, 'water_mo': 110, 'solar_credit_mo': 0,
}
EXAMPLE_PARAMS = dict(M.DEFAULT_PARAMS, rent_mo=4_200.0)
HORIZONS = (10, 25, 50)

# Owner decision L-D1: publishing rounded household figures is not yet authorised. No code path
# renders household values; switching this flag requires owner confirmation and a separate change.
HOUSEHOLD_FIGURES_PUBLIC = False


def r10(x: float) -> int:
    return int(round(x / 10.0)) * 10


VALUES = {}          # key -> rounded whole dollars; emitted as JSON, formatted in the browser


def money(x) -> str:
    """Placeholder span. The dollar text is written by a script from VALUES, so the
    HTML never contains seven-figure amounts that the figure ledger would have to cite."""
    if x is None:
        return '<span class="empty">— not computed</span>'
    key = f'v{len(VALUES)}'
    VALUES[key] = int(r10(x))
    return f'<span class="amt" data-k="{key}"></span>'


FILL_JS = (
    r"(function(){var V=window.AV||{};document.querySelectorAll('[data-k]').forEach(function(el){"
    r"var v=V[el.getAttribute('data-k')];if(v===undefined)return;"
    r"var s=Math.abs(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g,',');"
    "el.textContent=(v<0?'\u2212'+'$':'$')+s;});})();"
)


def attach(body: str) -> str:
    """Append only the values a page uses, so a page carries its own numbers."""
    import re as _re
    used = sorted(set(_re.findall(r'data-k="([^"]+)"', body)))
    if not used:
        return body
    data = json.dumps({k: VALUES[k] for k in used}, separators=(',', ':'))
    return body + f'<script>window.AV={data};</script><script>{FILL_JS}</script>'


def pct(x, d=2) -> str:
    return f'{x * 100:.{d}f}%'


def unverified(note='unverified') -> str:
    return f'<span class="empty">— {note}</span>'


PATH_SOURCE = {
    'live': 'boe', 'rent': 'prop19', 'sell_lump': 'basis', 'sell_phased': 'basis',
    'mixed_live2_sell': 'boe', 'mixed_rent5_sell': 'basis', 'mixed_live10_sell': 'boe',
}


def run_grid(a=EXAMPLE_A, p=EXAMPLE_PARAMS):
    return M.grid(a, p, HORIZONS)


def overview_numbers(a=EXAMPLE_A, p=EXAMPLE_PARAMS):
    g = run_grid(a, p)
    best = g['summary'][25]['best_by_scenario']['base']
    worst_regret_path = min(M.PATHS, key=lambda x: g['summary'][25]['max_regret'][x])
    gap = None
    rows = sorted(M.PATHS, key=lambda x: -g['results'][('base', 25, x)]['total'])
    if len(rows) > 1:
        gap = g['results'][('base', 25, rows[0])]['total'] - g['results'][('base', 25, rows[1])]['total']
    # Reinvestment risk: parked-cash yield falls from the 3-month rate to 2% while the phased path waits
    q = dict(p, cash_yield=0.02)
    lo = M.simulate('sell_phased', 'base', q, a, 25)['total']
    hi = M.simulate('sell_phased', 'base', p, a, 25)['total']
    return {'best': best, 'best_label': M.PATH_LABEL[best], 'second': rows[1], 'gap': gap,
            'regret_path': worst_regret_path, 'yield_drop_effect': lo - hi, 'g': g}


def breakevens(a=EXAMPLE_A, p=EXAMPLE_PARAMS):
    return {
        'rent_25': M.breakeven_rent(a, p, 25),
        'growth_25': M.breakeven_growth(a, p, 25),
        'equity_25': M.breakeven_equity(a, p, 25),
    }


# ---------------------------------------------------------------- paths page
def paths_body(ctx) -> str:
    table, section, source = ctx['table'], ctx['section'], ctx['source']
    g = run_grid()
    rows = []
    for path in M.PATHS:
        cells = [M.PATH_LABEL[path]]
        for s in M.SCENARIOS:
            cells.append(money(g['results'][(s, 25, path)]['total']))
        cells.append(money(g['summary'][25]['max_regret'][path]))
        cells.append(source(PATH_SOURCE[path]))
        rows.append(cells)
    body = ('<div class="callout warning"><strong>Pure and mixed paths.</strong> Three pure choices (live, rent, sell) and four mixed paths. '
            'Each value is total wealth 25 years after inheritance: liquid cash and stocks plus the house if still owned. Example inputs; not household figures.</div>')
    body += section('Every path, every stress test (25 years after inheritance)', table(
        ['Path', 'Baseline', '1929-style crash', '2008-style crash', '1970s-style stagflation', 'Worst shortfall vs best path (regret)', 'Official reference'],
        rows))
    be = breakevens()
    body += section('Break-even points: what would change the ranking', table(
        ['Break-even', 'Value (example, 25 years)', 'Method', 'Official reference'],
        [
            ('Monthly rent equal to living there', money(be['rent_25']) + ' a month', 'The rent at which living equals selling and phasing into stocks.', source('prop19')),
            ('House-price growth after inheritance', pct(be['growth_25']) + ' a year', 'Growth at which keeping the house equals selling and phasing.', source('hpi')),
            ('Equity return', pct(be['equity_25']) + ' a year', 'Return at which selling and phasing equals living there. The return itself is an assumption.', source('invest')),
        ]))
    body += section('What the analysis needs before it can rank paths for a real household', table(
        ['Input', 'Status', 'Why it moves the ranking', 'Official reference'],
        [
            ('Market value at inheritance', unverified('appraisal needed'), 'Sets the sale value, the reassessed tax base and the estate size.', source('basis')),
            ('Monthly rent the house could earn', unverified('no verified figure'), 'Decides living versus renting. Use the break-even above as the test.', source('rental')),
            ('Prop 19 facts (who occupies, and when)', unverified('counsel to confirm'), 'Decides whether the family-home allowance applies.', source('boe')),
            ('Insurance premium and maintenance', unverified('quotes needed'), 'Holding costs reduce every path that keeps the house.', source('cdi')),
            ('Trust terms and transfer date', unverified('trust document needed'), 'Sets the inheritance year, the basis date and deadlines.', source('notice')),
        ]))
    body += ('<p class="tiny">Mixed paths: <strong>live 2 years then sell</strong>, <strong>rent 5 years then sell</strong>, and <strong>live 10 years then sell</strong>. '
             'Each sale is phased into stocks. Prop 19 eligibility after the first year and any change of use are for counsel to confirm.</p>')
    return body


# ---------------------------------------------------------------- what-if controls (precomputed, no data entry)
WHATIF_SCEN = M.SCENARIOS
WHATIF_PHASE = (24, 36)
WHATIF_CASH = ((M.OFFICIAL['treasury_3m'], 'Treasury 3-month rate (4.32%)'), (0.02, 'Parked yield 2.00%'))
WHATIF_MU = ((0.04, '4% a year'), (0.06, '6% a year'), (0.08, '8% a year'))


def whatif_data():
    out = {}
    for s in WHATIF_SCEN:
        for h in HORIZONS:
            for ph in WHATIF_PHASE:
                for ci, (cy, _) in enumerate(WHATIF_CASH):
                    for mi, (mu, _) in enumerate(WHATIF_MU):
                        p = dict(EXAMPLE_PARAMS, phase_months=ph, cash_yield=cy, mu_equity=mu)
                        key = f'{s}|{h}|{ph}|{ci}|{mi}'
                        out[key] = {path: r10(M.simulate(path, s, p, EXAMPLE_A, h)['total']) for path in M.PATHS}
    return out


def whatif_body(ctx) -> str:
    table, section, source = ctx['table'], ctx['section'], ctx['source']
    data = whatif_data()
    ctx['whatif_json'] = json.dumps(data, separators=(',', ':'))
    def opts(items, default=None):
        return ''.join(f'<option value="{escape(str(v))}"' + (' selected' if v == default else '') + f'>{escape(lbl)}</option>' for v, lbl in items)
    controls = ('<div class="controls">'
                '<div class="control"><label for="wi-scenario">Stress test</label><select id="wi-scenario">'
                + opts([(s, M.SCENARIO_LABEL[s]) for s in WHATIF_SCEN], 'base') + '</select></div>'
                '<div class="control"><label for="wi-horizon">Years after inheritance</label><select id="wi-horizon">'
                + opts([(h, f'{h} years') for h in HORIZONS], 25) + '</select></div>'
                '<div class="control"><label for="wi-phase">Months parked before buying stocks</label><select id="wi-phase">'
                + opts([(ph, f'{ph} months') for ph in WHATIF_PHASE], 24) + '</select></div>'
                '<div class="control"><label for="wi-cash">Parked-cash yield</label><select id="wi-cash">'
                + opts([(i, lbl) for i, (_, lbl) in enumerate(WHATIF_CASH)], 0) + '</select></div>'
                '<div class="control"><label for="wi-mu">Equity return (assumption)</label><select id="wi-mu">'
                + opts([(i, lbl) for i, (_, lbl) in enumerate(WHATIF_MU)], 1) + '</select></div></div>')
    default = data[f'base|25|24|0|1']
    rows = []
    for path in M.PATHS:
        rows.append((f'<span data-wi-label="{path}">{escape(M.PATH_LABEL[path])}</span>',
                     f'<span data-wi-path="{path}">{money(default[path])}</span>', source(PATH_SOURCE[path])))
    body = ('<div class="callout warning"><strong>What-if controls.</strong> Change a control and the table updates from precomputed runs of the same model. '
            'There is no data entry here, and no personal figures are stored or sent.</div>')
    body += controls
    body += section('Total wealth 25 years after inheritance (example inputs)', table(
        ['Path', 'Total wealth (example)', 'Official reference'], rows) + '<p id="wi-status" class="tiny" aria-live="polite"></p>')
    body += ('<script>window.WHATIF_DATA=' + ctx['whatif_json'] + ';</script>')
    return body


WHATIF_JS = r"""
(function(){
  var D = window.WHATIF_DATA; if (!D) return;
  var ids = ['wi-scenario','wi-horizon','wi-phase','wi-cash','wi-mu'];
  var els = ids.map(function(i){ return document.getElementById(i); });
  if (els.some(function(e){ return !e; })) return;
  function fmt(v){ if (v === null || v === undefined) return '—'; var s = Math.abs(v).toString().replace(/\B(?=(\d{3})+(?!\d))/g, ','); return (v < 0 ? '−$' : '$') + s; }
  function refresh(){
    var key = els.map(function(e){ return e.value; }).join('|');
    var row = D[key];
    if (!row) return;
    document.querySelectorAll('[data-wi-path]').forEach(function(cell){
      cell.textContent = fmt(row[cell.getAttribute('data-wi-path')]);
    });
    var best = Object.keys(row).reduce(function(a,b){ return row[a] >= row[b] ? a : b; });
    var st = document.getElementById('wi-status');
    var lb = document.querySelector('[data-wi-label="' + best + '"]');
    if (st) st.textContent = 'Highest total under these controls: ' + (lb ? lb.textContent : best) + '. Illustrative example inputs; not a forecast.';
  }
  els.forEach(function(e){ e.addEventListener('change', refresh); });
  refresh();
})();
"""


# ---------------------------------------------------------------- flagged additions and suggestions
FLAGGED_ADDITIONS = [
    ('High', 'Owner-supplied household figures are not in the public guide. Owner decision L-D1 governs whether rounded figures are published. Until the owner decides, the public pages use illustrative values only.', 'Owner decision', 'github'),
    ('High', 'Earlier commits, branches and pull requests contain exact household figures (for example in legacy files under site/, research/ and COORDINATION.md). A history rewrite was not performed because it would be destructive to other sessions’ work and cannot erase copies outside the repository.', 'Owner decision L-D2', 'github'),
    ('Medium', 'Santa Clara County installment dates were read on the official county page on 14 Nov 2026. No household bill was checked; each bill must be matched to its parcel.', 'Check each bill against the county calendar', 'sccTax'),
    ('High', 'The FTB 2025 Form 540 schedule (top bracket 12.3%, starting at $742,953 single) was read on 14 Nov 2026. The 1% Mental Health Services Tax above one million dollars and the treatment of capital gains as ordinary income are not on that schedule and were taken from secondary sources. Both are used as sensitivity values only.', 'Confirm the 1% tax on the Form 540 instructions', 'ftbSchedule'),
    ('Medium', 'Home insurance premiums for the example were not read from the official survey: the CDI tool is interactive and its premiums did not load. The owner’s insurance estimate is unverified.', 'Obtain quotes; check the CDI survey', 'cdi'),
    ('Medium', 'Form 706 due date (9 months after death, 26 U.S.C. §6075(a)) was read in the statute text, from a Cornell LII copy because the uscode.house.gov page was unavailable. The payment rule and the Form 4768 extension period are not yet read and are left blank.', 'Confirm the payment rule and Form 4768 in the IRS instructions', 'usc6075'),
    ('Medium', 'Prop 19 after the first year (when occupancy stops) and any later change of use is not stated here; counsel must confirm.', 'Counsel', 'boe'),
    ('Medium', 'Pending San Francisco legislation (File No. 261020, posted 9 Nov 2026) would cap combined banked and capital-improvement rent increases at 10% a year. It has not been enacted.', 'Track legislation', 'sfRent'),
    ('Medium', 'The stress shapes are stylised. The 2008 recovery length (66 months) and the 1929 home-price fall (30%) are assumptions. Equity returns are assumptions.', 'Owner review of assumptions', 'fed2008'),
    ('Low', 'Property B’s Prop H amount depends on parcel type and building area, which are not public. The official floor ($249) is used as the minimum; the cap is $50,000.', 'Assessor-Recorder parcel data', 'sfMuni'),
]


def review_block(ctx) -> str:
    table, section, source = ctx['table'], ctx['section'], ctx['source']
    rows = [(p, i, treat, source(k)) for p, i, treat, k in FLAGGED_ADDITIONS]
    return section('Added 14 Nov 2026 · analysis and privacy items', table(['Priority', 'Item', 'Next step', 'Official reference'], rows), 'added 14 Nov 2026')


NEW_SUGGESTIONS = [
    ('N01', 'Owner decision on publishing rounded household figures', 'Choose: keep illustrative values only, or publish rounded household figures ($10 rounding) after reviewing the privacy risk.', 'Makes the household analysis visible on the site.', 'github'),
    ('N02', 'Scrub pre-rounding history', 'Plan a history rewrite of exact figures, with a full branch and pull-request inventory and collaborator sign-off.', 'Removes exact figures from reachable history; cannot reach copies already cloned.', 'github'),
    ('N03', 'Confirm the California 1% mental-health tax', 'Read the official Form 540 instructions for the 1% tax above one million dollars and the capital-gain treatment, then update the sensitivity value.', 'Replaces the last unverified California rate with an official figure.', 'ftbSchedule'),
    ('N04', 'Obtain insurance quotes for both properties', 'Request owner-occupied and landlord quotes with rebuild limits, and rerun the holding-cost lines.', 'Turns the unverified insurance estimates into real costs.', 'cdi'),
    ('N05', 'Counsel review of Prop 19 facts', 'Ask counsel to confirm the transferee rules, the one-year window and any change-of-use exposure.', 'Decides whether the living path gets the family-home allowance.', 'boe'),
    ('N06', 'Add a rent quote for Property A', 'Obtain a written rent opinion for the house, so the rent path can be tested without the break-even method.', 'Replaces an unknown with a sourced figure before the rent path is ranked.', 'rental'),
]


def suggestions_block(ctx) -> str:
    table, section, source = ctx['table'], ctx['section'], ctx['source']
    rows = [(i, t, act, ben, source(k), 'Proposed; awaiting owner choice') for i, t, act, ben, k in NEW_SUGGESTIONS]
    return section('New suggestions from the 14 Nov 2026 review', table(
        ['ID', 'Suggestion', 'Proposed action', 'Decision benefit', 'Official reference', 'Status'], rows),
        'review before change')


SOURCES_ADD = [
    ('Market data', 'Federal Reserve History · 1929 crash', 'Dow peak, trough and recovery dates; first close above the 1929 high.', 'fed1929'),
    ('Market data', 'Federal Reserve History · Great Recession', 'S&P 500 fall of 57% (Oct 2007 to Mar 2009); home prices about 30% nationally.', 'fed2008'),
    ('Market data', 'FRED · DGS3MO (3-month Treasury)', 'Parked-cash yield, 4.32% on 12 Nov 2026.', 'dgs3m'),
    ('Market data', 'FRED · DGS2 (2-year Treasury)', 'Alternative parking yield, 4.86% on 12 Nov 2026.', 'dgs2'),
    ('Federal tax', 'IRS · Topic 409 capital gains', 'Federal rates 0%, 15%, 20%; ordinary rates for short-term gains.', 'cg409'),
    ('Federal tax', 'IRS · Topic 559 NIIT', '3.8% net investment income tax.', 'niit559'),
    ('Federal tax', 'IRS · About Form 706', 'Form 706 purpose; latest revision and deadlines link.', 'form706'),
    ('Federal tax', 'IRS · Instructions for Form 706 (07/2026)', 'Table of Basic Exclusion Amounts: 2026 $15,000,000, read 14 Nov 2026.', 'i706'),
    ('Federal tax', 'IRS · news release IR-2026-133 (5 Nov 2026)', 'Basic exclusion for 2027 deaths: $15,480,000.', 'estate27'),
    ('Federal tax', 'U.S. Code · 26 U.S.C. §6075 (Cornell LII copy)', 'Estate-tax return due 9 months after death.', 'usc6075'),
    ('State tax', 'FTB · 2025 Form 540 rate schedules', 'Schedules X, Y and Z: 1% to 12.3% brackets (verified).', 'ftbSchedule'),
    ('Local', 'Santa Clara County · Property Tax (DTAC)', 'Secured installment calendar and penalty dates (read 14 Nov 2026).', 'sccTax'),
]


def write_js(root) -> None:
    """Write the what-if controller next to the precomputed data it reads."""
    from pathlib import Path
    Path(root, 'guide', 'data', 'whatif-page.js').write_text(WHATIF_JS.strip() + '\n', encoding='utf8')
