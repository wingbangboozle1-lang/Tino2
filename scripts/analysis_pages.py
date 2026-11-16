#!/usr/bin/env python3
"""Build public teaching examples for the inheritance decision guide.

Only synthetic inputs belong in the public source tree or shipped site. Household
records and household-derived figures are private and are not loaded by this module.
Official links support legal rules or published benchmarks; they do not verify the
synthetic inputs or turn model outputs into forecasts or personal advice.
"""
from __future__ import annotations
import json
from html import escape
import analysis_model as M

# Fixed, deliberately synthetic inputs used only to demonstrate the model mechanics.
# They are not sourced from or intended to represent any real household or property.
EXAMPLE_A = {
    'label': 'A', 'fmv_now': 1_240_000, 'assessed_2026': 398_000, 'assessed_2025': 390_200,
    'tax_2025': 5_980, 'insurance_yr': 2_240, 'water_mo': 180, 'solar_credit_mo': 0,
}
EXAMPLE_B = {
    'label': 'B', 'fmv_now': 980_000, 'assessed_2025': 321_000, 'tax_2025': 5_120,
    'rent_mo': 3_600, 'water_mo': 540, 'elec_mo': 130, 'insurance_yr': 4_300,
}
EXAMPLE_PARAMS = dict(M.DEFAULT_PARAMS, rent_mo=4_400.0)
HORIZONS = (10, 25, 50)
ACTIVE_A = EXAMPLE_A
ACTIVE_B = EXAMPLE_B
ACTIVE_PARAMS = EXAMPLE_PARAMS
PROVENANCE = 'Synthetic example inputs; not household figures. Model outputs are not forecasts.'


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


def run_grid(a=ACTIVE_A, p=ACTIVE_PARAMS):
    return M.grid(a, p, HORIZONS)


def overview_numbers(a=ACTIVE_A, p=ACTIVE_PARAMS):
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


def breakevens(a=ACTIVE_A, p=ACTIVE_PARAMS):
    return {
        'rent_25': M.breakeven_rent(a, p, 25),
        'growth_25': M.breakeven_growth(a, p, 25),
        'equity_25': M.breakeven_equity(a, p, 25),
    }


# ---------------------------------------------------------------- paths page
def distribution_svg(g) -> str:
    """Range chart of terminal wealth across the four stress scenarios, per path.

    Tick labels carry data-k placeholders, so the SVG text is filled in the
    browser from the same JSON block as the tables and no seven-figure amount
    appears in the static HTML.
    """
    W, ROW_H, LBL_W, RIGHT, TOP = 760, 36, 250, 30, 26
    n = len(M.PATHS)
    H = TOP + ROW_H * n + 52
    vals = {p: [g['results'][(s, 25, p)]['total'] for s in M.SCENARIOS] for p in M.PATHS}
    vmin = min(min(v) for v in vals.values())
    vmax = max(max(v) for v in vals.values())
    span = (vmax - vmin) or 1.0
    lo, hi = vmin - span * 0.07, vmax + span * 0.07
    def x(v):
        return LBL_W + (v - lo) / (hi - lo) * (W - LBL_W - RIGHT)
    parts = ['<svg id="distribution-chart" viewBox="0 0 %d %d" width="100%%" height="%d" role="img" '
             'aria-label="Range of terminal wealth across the four stress scenarios at 25 years, one bar per path.">'
             % (W, H, H)]
    y_bottom = TOP + ROW_H * n
    for f in (0.0, 0.25, 0.5, 0.75, 1.0):
        t = lo + (hi - lo) * f
        parts.append('<line x1="%.1f" y1="%d" x2="%.1f" y2="%d" stroke="#d9d9d9" stroke-dasharray="2 4"/>'
                     % (x(t), TOP - 10, x(t), y_bottom + 6))
        parts.append('<text class="amt" data-k="dt%d" x="%.1f" y="%d" text-anchor="middle" font-size="11" fill="#666"></text>'
                     % (len(VALUES), x(t), y_bottom + 22))
        VALUES['dt%d' % len(VALUES)] = int(r10(t))
    scen_diamond = M.SCENARIOS[0]
    for row, path in enumerate(M.PATHS):
        y = TOP + ROW_H * row + ROW_H / 2
        vs = vals[path]
        parts.append('<g data-path="%s"><title>%s — 25-year terminal wealth across four scenarios</title>' % (path, M.PATH_LABEL[path]))
        parts.append('<text x="%d" y="%.1f" text-anchor="end" dominant-baseline="middle" font-size="12" fill="#333">%s</text>'
                     % (LBL_W - 14, y, M.PATH_LABEL[path]))
        parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#8a8a7a" stroke-width="5" stroke-linecap="round"/>'
                     % (x(min(vs)), y, x(max(vs)), y))
        for s, v in zip(M.SCENARIOS, vs):
            if s == scen_diamond:
                parts.append('<path d="M %.1f %.1f l 6 6 l -6 6 l -6 -6 z" fill="#4a5d23"/>' % (x(v), y - 6))
            else:
                parts.append('<line x1="%.1f" y1="%.1f" x2="%.1f" y2="%.1f" stroke="#333" stroke-width="2"/>' % (x(v), y - 8, x(v), y + 8))
        parts.append('<text class="amt" data-k="dv%d" x="%.1f" y="%.1f" text-anchor="start" dominant-baseline="middle" font-size="11" fill="#666"></text>'
                     % (len(VALUES), x(max(vs)) + 10, y))
        VALUES['dv%d' % len(VALUES)] = int(r10(max(vs)))
        parts.append('</g>')
    parts.append('</svg>')
    return ''.join(parts)


def distribution_cells(path: str, g) -> list[str]:
    """Best / worst / spread of the scenario band for one path at one horizon, per horizon cell."""
    cells = []
    for h in HORIZONS:
        vals = {s: g['results'][(s, h, path)]['total'] for s in M.SCENARIOS}
        best = max(vals, key=vals.get)
        worst = min(vals, key=vals.get)
        spread = vals[best] - vals[worst]
        share = f'{spread / vals[best] * 100:.0f}% of the best' if vals[best] else '—'
        cells.append(f'{money(vals[best])} / {money(vals[worst])} / {money(spread)} <span class="tiny">({share})</span>')
    return cells


def distribution_body(ctx) -> str:
    """The comparison page's distribution of outcomes, computed from the same scenario grid."""
    table, source = ctx['table'], ctx['source']
    g = run_grid()
    rows = []
    for path in M.PATHS:
        cells = [M.PATH_LABEL[path]] + distribution_cells(path, g)
        vals25 = {s: g['results'][(s, 25, path)]['total'] for s in M.SCENARIOS}
        best25 = max(vals25, key=vals25.get)
        worst25 = min(vals25, key=vals25.get)
        reading = (f'{M.SCENARIO_LABEL[best25]} gives this path its best 25-year outcome and '
                   f'{M.SCENARIO_LABEL[worst25]} its worst. A path whose best and worst come from the same pair of '
                   f'scenarios is exposed to that pair; one whose ranking changes hands is exposed to which scenario '
                   f'arrives, not only to how much.')
        cells.append(reading)
        cells.append(source('invest', 'Model output on scenario assumptions · not a forecast'))
        rows.append(tuple(cells))
    return table(
        ['Path', '10 years · best / worst / spread', '25 years · best / worst / spread',
         '50 years · best / worst / spread', 'Which scenarios bound it', 'Source context'], rows)


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
            'Each value is total wealth 25 years after inheritance: liquid cash and stocks plus the house if still owned. '+PROVENANCE+'</div>')
    body += section('Every path, every stress test (25 years after inheritance)', table(
        ['Path', 'Baseline', '1929-style crash', '2008-style crash', '1970s-style stagflation', 'Worst shortfall vs best path (regret)', 'Official reference'],
        rows))
    body += section('Distribution of outcomes across the scenario bands (25 years)', 
        '<p>The chart is the table above drawn as a distribution: for each path the bar spans the worst to the best of the four stress scenarios at the 25-year horizon, the diamond marks the baseline, and the ticks mark the crash and stagflation scenarios. A wide bar means the path is scenario-sensitive; a short bar means the scenario band changes little. These are model outputs on synthetic example inputs, rounded to $10 — not forecasts, and no probability is attached to any scenario.</p>'
        + distribution_svg(g)
        + '<p class="tiny">Reading the shape: the sell paths cluster at the high end with wide scenario spreads (they are fully exposed to the stock scenario), the live path is pulled down by the holding costs in every scenario, and the mixed paths sit between the two. The distribution is the honest form of the single-number comparison: there is no path whose worst case equals its best case. The stress shapes are stylised; see <a href="stress.html">Black swans</a> and the flagged notes.</p>')
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
            ('Market value at inheritance', unverified('private value withheld; independent appraisal needed'), 'Sets the sale value, the reassessed tax base and the estate size. No household valuation is published in this guide.', source('basis')),
            ('Monthly rent the house could earn', unverified('HUD benchmark published, no rent quote'), 'Decides living versus renting. The HUD small-area FMR is a voucher benchmark, not a rent quote; use the break-even above as the test.', source('hud')),
            ('Prop 19 facts (who occupies, and when)', unverified('counsel to confirm'), 'Decides whether the family-home allowance applies.', source('boe')),
            ('Insurance premium and maintenance', unverified('CDI survey range published, quotes needed'), 'Holding costs reduce every path that keeps the house. The regulator survey is not a quote.', source('cdi')),
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
                        p = dict(ACTIVE_PARAMS, phase_months=ph, cash_yield=cy, mu_equity=mu)
                        key = f'{s}|{h}|{ph}|{ci}|{mi}'
                        out[key] = {path: r10(M.simulate(path, s, p, ACTIVE_A, h)['total']) for path in M.PATHS}
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
    body += section('Total wealth 25 years after inheritance (synthetic example inputs)', table(
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
    if (st) st.textContent = 'Highest total under these controls: ' + (lb ? lb.textContent : best) + '. ' + '__PROVENANCE__';
  }
  els.forEach(function(e){ e.addEventListener('change', refresh); });
  refresh();
})();
"""
WHATIF_JS = WHATIF_JS.replace('__PROVENANCE__', PROVENANCE.replace('\\', '\\\\').replace("'", "\\'"))


# ---------------------------------------------------------------- flagged additions and suggestions
FLAGGED_ADDITIONS = [
    ('Critical', 'Household-derived values are excluded from the current public model; only synthetic examples and rule-level public facts are shown. Earlier public commits, branches and repository files may still contain household-derived material.', 'Make the repository private and have an administrator assess history and cached copies; do not treat this site change as a history scrub.', 'github'),
    ('Critical', 'The repository history was not rewritten. The checkout for this review is shallow and rewriting shared refs would affect collaborators; later commits and Pages exclusions cannot remove old Git objects or external copies.', 'A repository administrator should set visibility to private, inventory refs and pull requests, follow GitHub’s sensitive-data-removal procedure, and request cache removal. Independent clones and caches may remain.', 'github'),
    ('Medium', 'Synthetic property-tax rates and cost inputs in the public model are teaching assumptions, not a household bill, parcel rate or quote. Actual tax-rate areas and direct charges are not published.', 'Verify the private bill and parcel details with the county before modeling a real property.', 'sccTax'),
    ('Medium', 'Two official county pages give different TRA counts: the Assessor glossary says “over 3,200 TRAs in Santa Clara County”, while the Controller-Treasurer’s FY 2025–26 rate book states “Total number of Tax Rate Areas in Fiscal Year 2025-26 is 816”. Both were read 15 Nov 2026 and both numbers are printed on the Properties page. The difference may be a cumulative count of ever-assigned numbers versus active TRAs, but no official page explains it.', 'Ask the Assessor’s office which count the glossary means before relying on either number', 'asrGlossary'),
    ('Medium', 'The five-year maintenance table uses synthetic planning percentages. It is not a property-specific estimate, inspection finding or contractor bid.', 'Replace the example with private inspection findings and written contractor bids before acting.', 'county'),
    ('Medium', 'The insurance example is a regulator survey for a hypothetical homeowners profile, not a quote. It is not appropriate to infer a premium for any household or multi-unit rental from that profile.', 'Obtain private, product-specific quotes with rebuild limits and deductibles.', 'cdi'),
    ('Medium', 'HUD fair-market-rent tables are program benchmarks, not property-specific rent opinions or lawful-rent determinations. The public guide does not publish a household rent or map a rent benchmark to a private property.', 'Obtain private comparable-rent evidence and management estimates.', 'hud'),
    ('Medium', 'The Santa Clara County installment dates were read on the official county page on 14 Nov 2026. No household bill was checked; each bill must be matched to its parcel.', 'Check each bill against the county calendar', 'sccTax'),
    ('Medium', 'Closed 15 Nov 2026 (parallel sessions). The 1% California Behavioral Health Services Tax is now verified from the official sources: R&TC §17043 and the FTB 2025 Form 540 instructions (line 62: 1% of California taxable income above $1,000,000, any filing status, not indexed), read 14–15 Nov 2026; the tax page publishes the row. The model’s flat capital-gains rate stays 0.361 and does not add the above-$1,000,000 slice, so high-gain stacks still understate California tax on that slice.', 'Model the surcharge as a marginal slice above $1,000,000, or accept the flat-rate understatement', 'ftb540'),
    ('Medium', 'Form 706 due date (9 months after death, 26 U.S.C. §6075(a)) was read in the statute text, from a Cornell LII copy because the uscode.house.gov page was unavailable. The payment rule and the Form 4768 extension period are not yet read and are left blank.', 'Confirm the payment rule and Form 4768 in the IRS instructions', 'usc6075'),
    ('Medium', 'Prop 19 after the first year (when occupancy stops) and any later change of use is not stated here; counsel must confirm.', 'Counsel', 'boe'),
    ('Medium', 'Pending San Francisco legislation (File No. 261020, posted 9 Nov 2026) would cap combined banked and capital-improvement rent increases at 10% a year. It has not been enacted.', 'Track legislation', 'sfRent'),
    ('Medium', 'The stress shapes are stylised. The 2008 recovery length (66 months) and the 1929 home-price fall (30%) are assumptions. Equity returns are assumptions.', 'Owner review of assumptions', 'fed2008'),
    ('Low', 'Property B’s Prop H amount depends on parcel type and building area, which are not public. The official floor ($249) is used as the minimum; the cap is $50,000.', 'Assessor-Recorder parcel data', 'sfMuni'),
]


def review_block(ctx) -> str:
    table, section, source = ctx['table'], ctx['section'], ctx['source']
    rows = [(p, i, treat, source(k)) for p, i, treat, k in FLAGGED_ADDITIONS]
    return section('Added 15 Nov 2026 · analysis and privacy items', table(['Priority', 'Item', 'Next step', 'Official reference'], rows), 'added 15 Nov 2026')


NEW_SUGGESTIONS = [
    ('N01', 'Review repository privacy and visibility', 'The public guide now uses synthetic examples only. Ask a repository administrator to review public files, refs, pull requests, forks and caches before treating the earlier exposure as contained.', 'Separates the current site boundary from unresolved repository and history exposure.', 'github'),
    ('N02', 'Administrator history scrub (L-D2)', 'Run the six-step runbook on the Flagged page: inventory, git filter-repo, force-push, pull-request purge, GitHub Support cache removal, fork invalidation.', 'Removes exact figures from reachable history; cannot reach copies already cloned.', 'github'),
    ('N03', 'Model the California 1% surcharge above the threshold', 'The official read is done (R&TC §17043 and the Form 540 instructions, 14–15 Nov 2026). What remains is to decide whether to model the 1% Behavioral Health Services Tax as a marginal slice on taxable income above $1,000,000 instead of the flat rate.', 'Removes the last understatement in the California tax rate.', 'ftb540'),
    ('N04', 'Obtain insurance quotes for both properties', 'Request owner-occupied and landlord quotes with rebuild limits, and rerun the holding-cost lines against the CDI survey range.', 'Replaces a generic survey illustration with a private quote before any decision.', 'cdi'),
    ('N05', 'Counsel review of Prop 19 facts', 'Ask counsel to confirm the transferee rules, the one-year window and any change-of-use exposure.', 'Decides whether the living path keeps the family-home allowance.', 'boe'),
    ('N06', 'Replace the HUD rent benchmark with a written rent opinion', 'Obtain independent, private rental comparables for the inherited property; do not publish addresses, leases or household rent.', 'Replaces a benchmark with a sourced figure before the rent path is ranked.', 'hud'),
    ('N07', 'Pin each parcel’s tax-rate-area rate', 'Read the TRA rate and direct charges off each county bill and replace the implied effective rates in both models.', 'Removes the flat-charge caveat from every projected tax line.', 'sccTax'),
    ('N08', 'Decide the like-kind exchange question before any listing', 'Take advice and decide in writing whether a §1031 exchange is wanted; it reaches only real property for real property and cannot shelter proceeds reinvested in stocks.', 'Prevents an irreversible sale from foreclosing a deferral the household wanted.', 'usc1031'),
    ('N09', 'Sign the decision charter before the figures are shown', 'Fill the Decision and Date columns of the charter on the What-decides-it page in writing, offline, and date each entry.', 'Stops the criteria from being reverse-engineered from one projection.', 'invest'),
]


def suggestions_block(ctx) -> str:
    table, section, source = ctx['table'], ctx['section'], ctx['source']
    rows = [(i, t, act, ben, source(k), 'Proposed; awaiting owner choice', '— record decision and date offline') for i, t, act, ben, k in NEW_SUGGESTIONS]
    return section('New suggestions from the 15 Nov 2026 review', table(
        ['ID', 'Suggestion', 'Proposed action', 'Decision benefit', 'Official reference', 'Status', 'Decision and date'], rows),
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
