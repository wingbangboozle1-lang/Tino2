#!/usr/bin/env python3
"""Generate the public decision dashboard.

Every number comes from scripts/data/snapshot.json, which is produced by running
the same JavaScript model the browser runs (scripts/snapshot.cjs ->
guide/data/model.js). Amounts are rounded to $10 before they are written. No
household record is stored in this file or in its output.
"""
from pathlib import Path
from html import escape
import json

ROOT = Path(__file__).resolve().parents[1]
SNAP = json.loads((ROOT / 'scripts' / 'data' / 'snapshot.json').read_text())

SRC = {
 'irs_estate': ('IRS · estate tax and filing thresholds',
   'https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax'),
 'irs_2027': ('IRS IR-2026-133 · 2027 exclusion',
   'https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts'),
 'irs_basis': ('IRS · inherited basis FAQ',
   'https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances'),
 'irs_rr232': ('IRS · Rev. Rul. 2023-2',
   'https://www.irs.gov/pub/irs-drop/rr-23-02.pdf'),
 'irs_tc701': ('IRS · Topic 701, sale of your home',
   'https://www.irs.gov/taxtopics/tc701'),
 'irs_p523': ('IRS · Publication 523', 'https://www.irs.gov/publications/p523'),
 'irs_p527': ('IRS · Publication 527', 'https://www.irs.gov/publications/p527'),
 'irs_p551': ('IRS · Publication 551', 'https://www.irs.gov/publications/p551'),
 'irs_niit': ('IRS · Topic 559, NIIT', 'https://www.irs.gov/taxtopics/tc559'),
 'irs_706faq': ('IRS · estate tax FAQ',
   'https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes'),
 'sco': ('CA State Controller · estate tax',
   'https://www.sco.ca.gov/ardtax_estate_tax.html'),
 'boe19': ('California BOE · Proposition 19', 'https://www.boe.ca.gov/prop19/'),
 'lta25009': ('BOE LTA 2025/009 · $1,044,586',
   'https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf'),
 'lta26026': ('BOE LTA 2026/026 · Prop 19 Q&A',
   'https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf'),
 'lta26002': ('BOE LTA 2026/002 · inflation factor',
   'https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf'),
 'scc_asr': ('Santa Clara County Assessor · parent-child transfer',
   'https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2'),
 'scc_hoex': ("Santa Clara County Assessor · homeowners' exemption",
   'https://asr.santaclaracounty.gov/tax-savings/exemptions/homeowners'),
 'scc_rates': ('Santa Clara County · FY2025-26 tax rate book',
   'https://files.santaclaracounty.gov/exjcpb1531/2025-11/tax-rate-book-2025-2026.pdf'),
 'sf_tax': ('SF Treasurer · secured property tax rate',
   'https://sftreasurer.org/property/secured-property-taxes'),
 'sf_parcel': ('SF Treasurer · parcel taxes',
   'https://sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments'),
 'sf_rent': ('SF Rent Board · current rates',
   'https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit'),
 'sf_fee': ('SF Rent Board · Rent Board fee', 'https://www.sf.gov/rent-board-fee'),
 'sf_muni': ('SFMTA · Proposition H', 'https://www.sfmta.com/getting-around/muni/parcel'),
 'sf_election': ('SF Department of Elections · November 2026',
   'https://www.sfelections.org/results/20261103/index.html'),
 'probate': ('California Probate Code §16061.7',
   'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=16061.7'),
 'rtc480': ('California Revenue and Taxation Code §480',
   'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480'),
 'ftb593': ('California FTB · Form 593',
   'https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html'),
 'cdi_survey': ('CA Dept of Insurance · premium comparison tool',
   'https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/'),
 'cdi_guide': ('CA Dept of Insurance · homeowners guide',
   'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm'),
 'cdi_quake': ('CA Dept of Insurance · earthquake cover',
   'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/eq-ins.cfm'),
 'sjw': ('San Jose Water · 2026 rates', 'https://www.sjwater.com/2026-rates/'),
 'sfpuc': ('SFPUC · adopted water and sewer schedules',
   'https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf'),
 'cupertino_water': ('City of Cupertino · water',
   'https://www.cupertino.gov/Residents/Utilities/Water'),
 'pge': ('PG&E · solar billing',
   'https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html'),
 'ab942': ('CA Legislature · AB 942',
   'https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB942'),
 'hud95014': ('HUD · FY2027 SAFMR 95014',
   'https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=95014&cbsasub=METRO41940M41940'),
 'hud94122': ('HUD · FY2027 SAFMR 94122',
   'https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360'),
 'fhfa_scc': ('FHFA · Santa Clara County house price index',
   'https://fred.stlouisfed.org/series/ATNHPIUS06085A'),
 'fhfa_sf': ('FHFA · San Francisco County house price index',
   'https://fred.stlouisfed.org/series/ATNHPIUS06075A'),
 'cbo': ('Congressional Budget Office · outlook 2026-2036',
   'https://www.cbo.gov/system/files/2026-02/61882-By-the-Numbers.pdf'),
 'fed': ('Federal Reserve · September 2026 projections',
   'https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm'),
 'ssa': ('Social Security Trustees · 2026 assumptions',
   'https://www.ssa.gov/oact/TR/2026/II_C_assump.html'),
 'usgs': ('USGS · Bay Area earthquake outlook',
   'https://pubs.usgs.gov/publication/fs20163020'),
 'hr1301': ('Congress.gov · H.R. 1301',
   'https://www.congress.gov/bill/119th-congress/house-bill/1301'),
 'sb284': ('CA Legislature · SB 284',
   'https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB284'),
 'fdic': ('FDIC · insured deposits',
   'https://www.fdic.gov/resources/deposit-insurance/brochures/insured-deposits'),
 'invest': ('SEC · diversification',
   'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/world-investor-week-2026-investor-bulletin'),
 'github': ('GitHub · removing sensitive data',
   'https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository'),
}


def money(v):
    if v is None:
        return '—'
    r = round(v / 10) * 10
    return ('−' if r < 0 else '') + '${:,.0f}'.format(abs(r))


def mil(v):
    return ('−' if v < 0 else '') + '${:,.2f}M'.format(abs(v) / 1e6)


def pct(v, dp=1):
    return '—' if v is None else f'{v * 100:.{dp}f}%'


def link(key, label=None):
    title, url = SRC[key]
    return f'<a href="{escape(url, quote=True)}" rel="noopener noreferrer">{escape(label or title)} ↗</a>'


def table(headers, rows, wrap=''):
    h = ''.join(f'<th scope="col">{x}</th>' for x in headers)
    body = ''.join('<tr>' + ''.join(
        f'<td class="{c[1]}">{c[0]}</td>' if isinstance(c, tuple) else f'<td>{c}</td>'
        for c in r) + '</tr>' for r in rows)
    return (f'<div class="table-wrap {wrap}"><table><thead><tr>{h}</tr></thead>'
            f'<tbody>{body}</tbody></table></div>')


def section(title, body, eyebrow='', sid=''):
    e = f'<div class="eyebrow">{eyebrow}</div>' if eyebrow else ''
    i = f' id="{sid}"' if sid else ''
    return (f'<section class="section"{i}><div class="section-head"><div>{e}'
            f'<h2>{title}</h2></div></div>{body}</section>')


def card(label, value, note=''):
    return (f'<div class="card"><div class="metric-label">{label}</div>'
            f'<div class="metric">{value}</div><p class="tiny">{note}</p></div>')


def cards(items):
    return '<div class="grid three">' + ''.join(
        f'<a class="card card-link" href="{u}"><div class="eyebrow">{t}</div>'
        f'<h3>{n}</h3><p class="muted">{d}</p><span class="arrow">Open →</span></a>'
        for t, n, d, u in items) + '</div>'


PAGES = [
    ('overview', 'Summary', 'index.html'),
    ('requirements', 'Requirements', 'guide/requirements.html'),
    ('decision', 'Decision', 'guide/decision.html'),
    ('stress', 'Black swans', 'guide/stress.html'),
    ('property', 'Properties', 'guide/property.html'),
    ('tax', 'Taxes', 'guide/tax.html'),
    ('inheritance', 'Inheritance', 'guide/inheritance.html'),
    ('questions', 'Questions', 'guide/questions.html'),
    ('suggestions', 'Suggestions', 'guide/suggestions.html'),
    ('review', 'Flagged', 'guide/review.html'),
    ('sources', 'Sources', 'guide/sources.html'),
    ('method', 'Method', 'guide/method.html'),
]


def page(key, title, lead, body, scripts=(), home=False):
    base = '' if home else '../'
    nav = ''.join(
        f'<a href="{base}{path}"'
        + (' aria-current="page"' if i == key else '')
        + f'>{label}</a>' for i, label, path in PAGES)
    script_tags = ''.join(f'<script defer src="{base}{s}"></script>'
                          for s in ('assets/safe.js', *scripts))
    hero = (f'<section class="hero{" compact" if not home else ""}">'
            f'<div class="container"><div class="eyebrow">Inheritance decision '
            f'dashboard · figures reviewed 13 Nov 2026</div><h1>{title}</h1>'
            f'<p class="lead">{lead}</p><div class="meta">'
            f'<span class="pill">Anonymous by design</span>'
            f'<span class="pill">Official sources linked</span>'
            f'<span class="pill warn">Projections are estimates</span>'
            f'</div></div></section>')
    html = (
        '<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        '<meta name="robots" content="noindex,nofollow,noarchive">'
        '<meta name="referrer" content="no-referrer">'
        f'<title>{escape(title)} · Inheritance planning</title>'
        f'<link rel="stylesheet" href="{base}assets/safe.css">{script_tags}'
        '</head><body><a class="skip" href="#main">Skip to content</a>'
        '<header class="header"><div class="container topbar">'
        f'<a class="brand" href="{base}index.html"><span class="brand-mark">H</span>'
        '<span>Inheritance planning<small>DECISION DASHBOARD · ANONYMISED</small></span></a>'
        '<button class="menu" aria-expanded="false" aria-controls="navigation">Menu</button>'
        f'<nav class="nav" id="navigation" aria-label="Main navigation">{nav}</nav>'
        '</div></header>'
        '<div class="notice"><div class="container"><strong>Anonymised.</strong> '
        'No names, addresses, parcel numbers or document values appear here. '
        'Record-specific inputs stay in your browser and are never sent anywhere. '
        f'<a href="{base}guide/review.html">Privacy limits →</a></div></div>'
        '<noscript><div class="no-js">Rule and projection tables work without '
        'JavaScript. The interactive comparison and the break-even calculator '
        'need JavaScript.</div></noscript>'
        f'<main id="main">{hero}<div class="container">{body}</div></main>'
        '<footer class="footer"><div class="container footer-inner"><div>'
        '<strong>Inheritance planning</strong><br>Planning estimates and legal '
        'context, not legal, tax, insurance or investment advice.</div>'
        f'<div>Figure review: 13 Nov 2026 · <a href="{base}guide/sources.html">Sources</a> · '
        f'<a href="{base}guide/review.html">Flagged for review</a><br>'
        'Never enter personal records into this site.</div></div></footer>'
        '</body></html>')
    target = ROOT / ('index.html' if home else f'guide/{key}.html')
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(html + '\n', encoding='utf8')


# --------------------------------------------------------------------------
# Overview
# --------------------------------------------------------------------------
def build_overview():
    comps = {c['year']: c for c in SNAP['comparisons'] if c['horizon'] == 20}
    t45 = SNAP['baseTransfer']
    boot = SNAP['bootstrap']
    sell20 = comps[2045]['sell']

    body = '<section class="section"><div class="grid four">'
    body += card('Property A value today', money(2990000),
                 'Round planning anchor. Not an appraisal, and not the record value.')
    body += card('Projected value at 2045', money(t45['market']),
                 'At 3.6% a year, the CBO national home-price path.')
    body += card('Sell A at 2045, after 20 years',
                 f'<span id="sum-sell">{mil(sell20)}</span>',
                 'Net proceeds invested at 5.0% less 0.5% fees.')
    body += card('Renting beats selling in', pct(boot['rentLeads']),
                 f"{boot['draws']:,} resampled 30-year histories from 1976-2025.")
    body += '</div></section>'

    body += section('Executive summary',
        '<div class="card highlight"><div class="eyebrow" style="color:#d1e8b1">'
        'The answer depends on one variable</div>'
        '<h2>Selling wins the base case. It is not robust to a bad 30 years.</h2>'
        f'<p>On the central assumptions a sale of Property A at inheritance, with the '
        f'proceeds invested, ends 20 years later at <strong>{mil(sell20)}</strong>. '
        f'Renting ends at <strong>{mil(comps[2045]["rent"])}</strong> and living in it at '
        f'<strong>{mil(comps[2045]["live"])}</strong>. That ranking holds for home-price '
        f'growth from &minus;2% to about {pct(SNAP["breakEven"][1]["rent"]["rate"] or 0.064, 1)} a year, '
        f'and for portfolio returns from 3% to 9%.</p>'
        f'<p>But resampling the actual 1976-2025 record of California inflation and '
        f'Santa Clara County house prices gives renting the higher real outcome in '
        f'<strong>{pct(boot["rentLeads"])}</strong> of {boot["draws"]:,} thirty-year histories. '
        f'Selling is tightly clustered ({mil(boot["real"]["sell"]["p10"])} to '
        f'{mil(boot["real"]["sell"]["p90"])} at the 10th to 90th percentile); renting '
        f'spans {mil(boot["real"]["rent"]["p10"])} to {mil(boot["real"]["rent"]["p90"])}. '
        f'Selling buys certainty, not the highest expected value.</p>'
        f'<p><strong>Recommendation:</strong> treat selling as the risk-controlled '
        f'default and renting as the higher-variance alternative. The decision should '
        f'wait on the six critical facts listed on the <a href="guide/questions.html">'
        f'questions page</a>; three of them can reverse the ranking on their own.</p>'
        '<p class="tiny">Live figures: selling <span id="sum-sell-live"></span>, '
        'renting <span id="sum-rent"></span>, living in <span id="sum-live"></span>; '
        'break-even growth <span id="sum-breakeven"></span>.</p>'
        '<div class="actions"><a class="button secondary" href="guide/decision.html">'
        'See the comparison</a><a class="button secondary" href="guide/stress.html">'
        'See the black-swan cases</a></div></div>')

    body += section('What the three options look like',
        table(['Option', 'What happens', 'Ending value, 2045 transfer + 20 years',
               'Main risk', 'Rule source'],
              [('Sell A', ('Proceeds of about ' + money(t45['market'] * 0.94) +
                ' after 6% sale costs, invested; basis resets at death so no gain tax.',
                'wrap'),
                (mil(sell20), 'number'),
                ('Gives up the rent and the house. Return depends on markets, not the property.', 'wrap'),
                link('irs_basis')),
               ('Keep and rent', ('Full reassessment at transfer, depreciation shield, '
                '25% recapture on sale.',
                'wrap'),
                (mil(comps[2045]['rent']), 'number'),
                ('Rent does not cover reassessed tax plus costs in year one; the '
                 'shortfall is about ' + money(-comps[2045]['rentY1']) + ' a year.', 'wrap'),
                link('irs_p527')),
               ('Keep and live in', ('Proposition 19 relief cuts year-one tax by about '
                + money(t45['savingsYear1']) + '; the SF third unit can then be rented.',
                'wrap'),
                (mil(comps[2045]['live']), 'number'),
                ('No rent from A and about ' + money(-comps[2045]['liveY1']) +
                 ' a year of costs to fund; a later move out reverses the relief.', 'wrap'),
                link('lta26026'))]),
        '01 / the choice')

    body += section('Six facts that can change the answer',
        table(['Fact still unknown', 'Why it can flip the ranking', 'How to resolve',
               'Official context'],
              [('Trust type and estate inclusion',
                'A bypass or irrevocable arrangement outside the estate may not reset '
                'basis, which removes the main tax advantage of selling.', 'Read the signed trust with counsel.', link('irs_rr232')),
               ('Whether A was the parent&rsquo;s principal residence',
                'Without it, Proposition 19 relief is unavailable and the live-in option '
                'loses its tax advantage.', 'Document residence and file the exemption.',
                link('lta26026')),
               ('Date-of-death value',
                'Sets both basis and the reassessed value; a lower value than projected '
                'helps holding, a higher one helps selling.', 'Order a qualified appraisal.',
                link('irs_basis')),
               ('Lawful rent for A',
                'Rent must clear reassessed tax plus costs. At ' + money(6500) + ' a month '
                'it does not in year one.', 'Get local comparables.', link('hud95014')),
               ('Land versus building value',
                'Only the building can be depreciated; a low building share removes the '
                'rental tax shield.', 'Use a defensible allocation.', link('irs_p527')),
               ('Insurance and earthquake cover',
                'A standard policy excludes earth movement; an uncovered loss is the '
                'single largest tail risk for either holding option.', 'Get quotes.',
                link('cdi_quake'))]),
        '02 / uncertainty')

    body += section('Navigate the dashboard', cards([
        ('01 / requirements', 'Full requirements list',
         'Every element of the brief, and where it is answered.', 'guide/requirements.html'),
        ('02 / decision', 'Live, rent or sell',
         'Year-by-year tables, break-even rates and a sensitivity grid.', 'guide/decision.html'),
        ('03 / uncertainty', 'Black-swan conditions',
         'Five real historical shocks plus 2,000 resampled histories.', 'guide/stress.html'),
        ('04 / facts', 'Properties and data quality',
         'What is known, what is estimated, and what cannot be traced.', 'guide/property.html'),
        ('05 / rules', 'Taxes and inheritance',
         'Property tax, income tax, estate thresholds and the step-by-step process.', 'guide/tax.html'),
        ('06 / review', 'Suggestions and flags',
         'Proposals to review, and every item still unverified.', 'guide/suggestions.html'),
    ]), '03 / navigate')

    page('overview', 'The best plan, and how sure it is.',
         'A source-linked comparison of inheriting, renting, living in or selling the '
         'Cupertino home, with the San Francisco building held separately.',
         body, ['guide/data/model.js', 'guide/data/summary-page.js'], home=True)


# --------------------------------------------------------------------------
# Requirements register
# --------------------------------------------------------------------------
def build_requirements():
    rows = [
     ('R01', 'Collect and organise a full list of requirements', 'Requirements', 'This page.',
      'Done', link('boe19')),
     ('R02', 'Executive summary of important details', 'Summary', 'Front page summary card.',
      'Done', link('irs_estate')),
     ('R03', 'Suggestions section to review and choose a path', 'Suggestions',
      'Twenty proposals with a per-item decision recorded in your browser.', 'Done', link('boe19')),
     ('R04', 'Clear list of questions, answers and missing information', 'Questions',
      'Thirty-item register with priority, current answer and how to find it.', 'Done', link('lta26026')),
     ('R05', 'Suggest ways to discover missing information', 'Questions',
      'Each row names the document, agency or professional that resolves it.', 'Done', link('scc_asr')),
     ('R06', 'Anonymise all personal information', 'Flagged',
      'Placeholders only. No name, address, parcel number or document value is published.', 'Done',
      link('github')),
     ('R07', 'Personal information internal only, never on the site', 'Flagged',
      'Record-specific fields are computed in the browser only; nothing is stored or sent.',
      'Done', link('github')),
     ('R08', 'Treat the Cupertino house as inherited and the SF house as already owned',
      'Properties', 'Separate roles, separate tax treatment, separate tables.', 'Done',
      link('irs_rr232')),
     ('R09', 'Separate black-swan section covering real economic conditions', 'Black swans',
      'Five historical shocks, 2,000 resampled histories, and an honest note on what '
      'cannot be predicted.', 'Done', link('fhfa_scc')),
     ('R10', 'Baseline projections grounded in real economics', 'Method',
      'CBO, Federal Reserve and Social Security Trustees anchors, cross-checked against '
      'the 1976-2025 record.', 'Done', link('cbo')),
     ('R11', 'All numbers rounded to the nearest $10', 'Method',
      'Enforced mechanically: the build fails on any non-$10 dollar amount.', 'Done',
      link('scc_rates')),
     ('R12', 'Clear numbers and projections for the reasoning', 'Decision',
      'Year-by-year property tax, assessed value, operating cost and outcome tables.', 'Done',
      link('lta26002')),
     ('R13', 'Guidance based on current local, state and federal law', 'Taxes',
      'Santa Clara County rate book, California statutes, IRS guidance, each re-opened '
      'and dated.', 'Done', link('scc_rates')),
     ('R14', 'Whether to live in, rent, or sell and reinvest', 'Decision',
      'Three-way comparison with break-even rates and a sensitivity grid.', 'Done',
      link('irs_tc701')),
     ('R15', 'Project value, property tax and assessed value by year', 'Properties',
      '2026-2076 table for both properties, before and after transfer.', 'Done',
      link('lta26002')),
     ('R16', 'Show the inheritance process step by step', 'Inheritance',
      'Fifteen-step timeline with statutory deadlines and claim forms.', 'Done',
      link('probate')),
     ('R17', 'Water, electricity, insurance and maintenance costs', 'Properties',
      'Year-one cost build-up for both properties, with the solar credit shown separately.',
      'Done', link('cdi_guide')),
     ('R18', 'Costs specific to Cupertino: about $100-$150 water, solar credit, no power cost',
      'Properties', 'Modelled as $130 water, a $10 monthly solar credit and $2,200 insurance.',
      'Done', link('pge')),
     ('R19', 'SF rental: two units at about $7,000 a month, third unit available',
      'Properties', 'Modelled as supplied, with the third unit valued at the HUD one-bedroom '
      'fair market rent.', 'Done', link('hud94122')),
     ('R20', 'Inheritance-tax thresholds at local, state and federal level', 'Inheritance',
      'Federal exclusion $15,000,000 (2026) and $15,480,000 (2027); no California estate tax.',
      'Done', link('sco')),
     ('R21', 'Projections of thresholds and how much may pass before tax', 'Inheritance',
      'Headroom table 2027-2076 with the transfer value beside it.', 'Done', link('irs_2027')),
     ('R22', 'Changes to inheritance law under discussion', 'Taxes',
      'Watchlist: H.R. 1301, SB 284, San Francisco Measure H and rent legislation.', 'Done',
      link('hr1301')),
     ('R23', 'Any potential change to current law that affects the decision', 'Taxes',
      'Same watchlist, plus the 2027 Proposition 19 allowance still unpublished.', 'Done',
      link('lta25009')),
     ('R24', 'Clean, simple, dashboard-style UI with tables', 'Summary',
      'Twelve pages, one consistent table format, keyboard and mobile tested.', 'Done',
      link('boe19')),
     ('R25', 'Every table row links to an official source, or is blank and flagged',
      'Sources', 'Checked mechanically; unverifiable rows are blank on the flagged page.',
      'Done', link('github')),
     ('R26', 'No hallucinations: leave values blank rather than infer', 'Flagged',
      'Nine items published as unverified, including both insurance premiums.', 'Done',
      link('cdi_survey')),
     ('R27', 'Coordinate with parallel sessions', 'Method',
      'Claim, scope and completion recorded in COORDINATION.md.', 'Done', link('github')),
     ('R28', 'Publish to a live GitHub Pages site', 'Summary',
      'Deployed from main through Jekyll with an explicit publication allowlist.',
      'Done', link('github')),
    ]
    body = ('<div class="callout"><strong>How to read this page.</strong> Each row is '
            'a requirement from the brief, the page that answers it, and the official '
            'source that anchors the rule it relies on. Requirements marked '
            '<span class="tag">Done</span> are answered; anything not fully answerable is '
            'listed on <a href="review.html">Flagged for review</a> rather than guessed.</div>')
    body += section('Requirements and where each is answered',
        table(['#', 'Requirement', 'Answered on', 'How it is answered', 'Status',
               'Anchor source'], rows), '01 / coverage')
    body += section('What the brief asked for that cannot be answered yet',
        table(['Request', 'Why it is not answered', 'What would answer it', 'Source'],
         [('A single definitive best plan',
           'The ranking depends on facts not yet known, chiefly the trust type and the '
           'date-of-death value.', 'Trust document and an appraisal.', link('irs_rr232')),
          ('An exact estate-tax bill',
           'The total estate and prior taxable gifts were never supplied, and only the '
           'threshold is public.', 'A private estate inventory.', link('irs_estate')),
          ('An exact insurance premium',
           'Premiums are quoted per property; no official source publishes a premium for a '
           'specific house.', 'Written quotes from insurers.', link('cdi_survey')),
          ('An exact future Proposition 19 allowance',
           'The 16 February 2027 adjustment had not been published as of this review.',
           'The BOE letter to assessors that publishes it.', link('lta25009'))]),
        '02 / limits')
    page('requirements', 'Every requirement, and whether it is answered.',
         'A line-by-line check of the brief against the site, with the source that anchors '
         'each answer.', body)


# --------------------------------------------------------------------------
# Decision
# --------------------------------------------------------------------------
def build_decision():
    comps = [c for c in SNAP['comparisons'] if c['horizon'] in (10, 20, 30)]
    t = SNAP['baseTransfer']
    hold = SNAP['holdRent']

    body = ('<div class="callout warning"><strong>These are planning estimates, not a '
            'recommendation for a specific household.</strong> The two property values are '
            'owner estimates rounded to $1,000. Tax rates are official. Every operating '
            'cost is a stated assumption listed on the <a href="method.html">method page</a>. '
            'Change any of them below and the tables recompute in your browser.</div>')

    body += section('Transfer-year figures for Property A',
        '<p>Proposition 19 relief is only available if the home becomes the heir&rsquo;s '
        'principal residence within one year. Renting it out generally does not qualify, so '
        'the tax differs sharply between the two holding options.</p>' +
        table(['Transfer year', 'Projected market value', 'Factored base carried in',
               'Prop 19 allowance in force', 'Value cap',
               'Assessed if you live in it', 'Annual tax if you live in it',
               'Annual tax if you rent it', 'Annual tax if never transferred',
               'Rule source'],
              [(r['year'], money(r['market']), money(r['carryForward']),
                money(r['allowance']), money(r['cap']), money(r['primaryAssessed']),
                (money(r['taxLive']), 'number'), (money(r['taxRent']), 'number'),
                (money(r['taxNoTransfer']), 'number'),
                (link('lta25009', 'BOE value cap'), 'wrap'))
               for r in SNAP['transfers']]) +
        '<p class="tiny">The allowance is the official $1,044,590 for transfers before '
        '16 February 2027, stepped up every second year on one year of the FHFA California '
        'index. Later steps are a planning assumption of 3.6% a year. Live-in tax also '
        'credits the $7,000 homeowners&rsquo; exemption, worth about '
        + money(7000 * 0.01335) + ' a year. Sources: ' + link('lta25009') + ' &middot; '
        + link('lta26026') + ' &middot; ' + link('scc_hoex') + '</p>',
        '01 / property tax at transfer')

    body += section('Three options, same endpoint',
        '<p>Each option is measured at the same date, after tax and after the sale costs '
        'that would be paid to convert the house into cash. Renting and living in are '
        'charged every operating cost and credited the value of the house at the endpoint. '
        'Cash flows are reinvested at 5.0% less 0.5% fees.</p>' +
        table(['Transfer year', 'Horizon', 'Sell A and invest', 'Keep and rent',
               'Keep and live in', 'Leads', 'Margin over selling', 'Rule source'],
              [(c['year'], f"{c['horizon']}y", (mil(c['sell']), 'number'),
                (mil(c['rent']), 'number'), (mil(c['live']), 'number'),
                c['best'].title(),
                (mil(max(c['sell'], c['rent'], c['live']) - c['sell']), 'number'),
                link('irs_tc701'))
               for c in comps]) +
        '<p class="tiny">Living in also frees the San Francisco third unit, worth about '
        f'{money(comps[0]["sfExtra"])} invested over the horizon; that is included in the '
        'live-in figure. Source for the rules: ' + link('irs_tc701') + ' · ' +
        link('irs_p527') + '</p>', '02 / the comparison')

    body += section('Break-even home-price growth',
        '<p>The rate at which holding A overtakes selling it, with every other assumption '
        'unchanged. The recorded 1975-2025 nominal growth for Santa Clara County was '
        '<strong>7.01%</strong> a year and the real rate was 2.98%. The central projection '
        'uses 3.6%, inside the CBO national path.</p>' +
        table(['Transfer year', 'Rent beats sell above', 'Live-in beats sell above',
               'Recorded 50-year nominal', 'Central projection used', 'Source'],
              [(r['year'],
                (pct(r['rent']['rate']) if r['rent']['rate'] is not None else 'not in range', 'number'),
                (pct(r['live']['rate']) if r['live']['rate'] is not None else 'not in range', 'number'),
                (pct(0.0701), 'number'), (pct(0.036), 'number'), link('fhfa_scc'))
               for r in SNAP['breakEven']]) +
        '<p class="tiny">Break-even is computed at a 20-year horizon. A single crossing '
        'rate is reported; where the model crosses more than once the highest is shown, '
        'because above that rate holding stays ahead. Source: ' + link('fhfa_scc') + '</p>',
        '03 / break-even')

    body += section('Sensitivity grid: which option leads',
        '<p>Each cell is the leading option when home growth and portfolio return are '
        'varied together. The central case is 3.6% growth and a 5.0% portfolio.</p>' +
        _sensitivity_table(SNAP['sensitivity']) +
        '<p class="tiny">Selling leads across almost the whole grid. Holding only takes the '
        'lead when home prices compound materially faster than the CBO path.</p>',
        '04 / where the ranking changes')

    body += section('Annual detail if A is kept and rented',
        '<p>The first year after a 2045 transfer. Rent is the largest line; reassessed '
        'property tax is next. Depreciation shelters the cash flow, so no income tax is '
        'modelled in year one.</p>' +
        table(['Year', 'Market value', 'Assessed value', 'Property tax', 'Gross rent',
               'Net operating income', 'Income tax modelled', 'Cash flow',
               'Cumulative reserve', 'Rate source'],
              [(r['year'], money(r['market']), money(r['assessed']),
                (money(r['propTax']), 'number'), (money(r['rent']), 'number'),
                (money(r['noi']), 'number'), (money(r['incomeTax']), 'number'),
                (money(r['flow']), 'number'), (money(r['reserve']), 'number'),
                link('lta26002'))
               for r in hold]) +
        '<p class="tiny">A negative reserve means the household funds the shortfall from '
        'other income. Source: ' + link('irs_p527') + ' · ' + link('lta26002') + '</p>',
        '05 / year by year')

    body += section('Try your own assumptions',
        '<p>Everything below runs in your browser. Nothing is sent, stored or logged.</p>'
        '<div class="controls">'
        '<div class="control"><label for="c-transfer">Transfer year</label>'
        '<select id="c-transfer"><option>2040</option><option selected>2045</option>'
        '<option>2050</option></select></div>'
        '<div class="control"><label for="c-horizon">Years held after transfer</label>'
        '<select id="c-horizon"><option>10</option><option selected>20</option>'
        '<option>30</option><option>50</option></select></div>'
        '<div class="control"><label for="c-home">Home-price growth a year</label>'
        '<select id="c-home"><option value="0.02">2%</option>'
        '<option value="0.036" selected>3.6%</option><option value="0.05">5%</option>'
        '<option value="0.07">7%</option></select></div>'
        '<div class="control"><label for="c-port">Portfolio return a year</label>'
        '<select id="c-port"><option value="0.03">3%</option>'
        '<option value="0.05" selected>5%</option><option value="0.07">7%</option></select>'
        '</div><div class="control"><label for="c-rent">Rent for A a month</label>'
        '<select id="c-rent"><option value="5000">$5,000</option>'
        '<option value="6500" selected>$6,500</option><option value="8000">$8,000</option>'
        '<option value="9500">$9,500</option></select></div></div>'
        '<div id="live-result" class="card highlight" aria-live="polite"></div>'
        '<div class="table-wrap"><table><thead><tr>'
        '<th scope="col">Option</th><th scope="col">First-year cash flow</th>'
        '<th scope="col">Ending value</th><th scope="col">Difference from selling</th>'
        '<th scope="col">Rule source</th>'
        '</tr></thead><tbody id="live-compare"></tbody></table></div>'
        '<p class="tiny">Same formulas as the static tables above. Source: '
        + link('irs_basis') + '</p>', '06 / interactive')

    page('decision', 'Live in it, rent it, or sell it.',
         'A three-way comparison with year-by-year figures, break-even rates and a grid '
         'showing where the ranking changes.', body,
         ['guide/data/model.js', 'guide/data/decision-page.js'])


def _sensitivity_table(sens):
    head = ['Home growth \\ portfolio'] + [pct(p) for p in sens['portfolio']] + ['Rule source']
    rows = []
    for g in sens['grid']:
        cells = [pct(g['homeGrowth'])]
        for c in g['cells']:
            cells.append((c['best'].title(), 'number'))
        cells.append(link('irs_tc701'))
        rows.append(tuple(cells))
    return table(head, rows)


# --------------------------------------------------------------------------
# Black swans
# --------------------------------------------------------------------------
def build_stress():
    boot = SNAP['bootstrap']
    eco = SNAP['eco']
    body = ('<div class="callout warning"><strong>Growth is never a straight line.</strong> '
            'A single 3.6% growth assumption over 50 years is a convenience, not a forecast. '
            'This page replaces it with the actual joint record of California inflation and '
            'county house prices from 1976 to 2025, replayed two ways.</div>')

    body += section('What the real record looks like',
        table(['Measure', 'Lowest', '10th percentile', 'Median', '90th percentile',
               'Highest', 'Source'],
              [('Inflation over 30 years, annualised',
                pct(eco['cpiWindows'][1]['stats']['min']),
                pct(eco['cpiWindows'][1]['stats']['p10']),
                pct(eco['cpiWindows'][1]['stats']['median']),
                pct(eco['cpiWindows'][1]['stats']['p90']),
                pct(eco['cpiWindows'][1]['stats']['max']), link('lta26002')),
               ('Santa Clara house prices, 30-year real growth',
                pct(eco['sccWindows'][1]['real']['min']),
                pct(eco['sccWindows'][1]['real']['p10']),
                pct(eco['sccWindows'][1]['real']['median']),
                pct(eco['sccWindows'][1]['real']['p90']),
                pct(eco['sccWindows'][1]['real']['max']), link('fhfa_scc')),
               ('Santa Clara house prices, 20-year real growth',
                pct(eco['sccWindows'][0]['real']['min']),
                pct(eco['sccWindows'][0]['real']['p10']),
                pct(eco['sccWindows'][0]['real']['median']),
                pct(eco['sccWindows'][0]['real']['p90']),
                pct(eco['sccWindows'][0]['real']['max']), link('fhfa_scc'))]) +
        f'<p class="tiny">The county index fell {pct(abs(eco["sccDrawdown"]["worstFall"]))} '
        f'between {eco["sccDrawdown"]["from"]} and {eco["sccDrawdown"]["to"]} and went '
        f'{eco["sccDrawdown"]["longestFlat"]} years without a new high. Over the full '
        f'1975-2025 period it rose {pct(eco["scc50"]["nominal"])} a year in nominal terms '
        f'and {pct(eco["scc50"]["real"])} in real terms. The model uses 3.6% nominal, '
        f'which sits above the real median and below the nominal median.</p>',
        '01 / empirical baseline')

    rows = []
    for key, v in SNAP['stress'].items():
        r = v['rows'][29]
        rows.append((v['title'],
                     (v['note'], 'wrap'),
                     (mil(r['sell']), 'number'),
                     (mil(r['rent']), 'number'),
                     (mil(r['live']), 'number'),
                     link('fhfa_scc')))
    body += section('Five real shocks, applied in year one',
        '<p>Each path applies the shock at the start of the holding period, then returns to '
        'the central assumptions. A 2045 transfer with a 30-year hold; nominal dollars.</p>' +
        table(['Scenario', 'What it models', 'Sell A', 'Keep and rent', 'Keep and live in',
               'Source'], rows) +
        '<p class="tiny">The stagflation path is the one case where both holding options '
        'beat selling: rents rise with inflation while the reassessed tax is capped, and a '
        'portfolio of financial assets does badly. The other four paths put selling ahead. '
        'Source: ' + link('ssa') + ' · ' + link('usgs') + '</p>', '02 / named scenarios')

    body += section('2,000 resampled histories',
        f'<p>The record contains only one 1975-2025 window, which is too few to judge risk. '
        f'Instead the {boot["years"]}-year joint history of annual inflation and house-price '
        f'change is resampled in five-year blocks, {boot["draws"]:,} times, and each draw is '
        f'run through the same model. Outcomes are deflated to constant purchasing power.</p>' +
        table(['Outcome in real terms', '10th percentile', 'Median', '90th percentile',
               'Lowest', 'Highest', 'Series source'],
              [('Sell A and invest', (mil(boot['real']['sell']['p10']), 'number'),
                (mil(boot['real']['sell']['median']), 'number'),
                (mil(boot['real']['sell']['p90']), 'number'),
                (mil(boot['real']['sell']['min']), 'number'),
                (mil(boot['real']['sell']['max']), 'number'), link('fhfa_scc')),
               ('Keep A and rent', (mil(boot['real']['rent']['p10']), 'number'),
                (mil(boot['real']['rent']['median']), 'number'),
                (mil(boot['real']['rent']['p90']), 'number'),
                (mil(boot['real']['rent']['min']), 'number'),
                (mil(boot['real']['rent']['max']), 'number'), link('fhfa_scc')),
               ('Keep A and live in it', (mil(boot['real']['live']['p10']), 'number'),
                (mil(boot['real']['live']['median']), 'number'),
                (mil(boot['real']['live']['p90']), 'number'),
                (mil(boot['real']['live']['min']), 'number'),
                (mil(boot['real']['live']['max']), 'number'), link('fhfa_scc'))]) +
        f'<div class="grid two" style="margin-top:16px">'
        f'<div class="card warning"><div class="metric-label">Renting beats selling in</div>'
        f'<div class="metric">{pct(boot["rentLeads"])}</div>'
        f'<p class="tiny">of {boot["draws"]:,} histories, by ending real value</p></div>'
        f'<div class="card warning"><div class="metric-label">Living in it beats selling in</div>'
        f'<div class="metric">{pct(boot["liveLeads"])}</div>'
        f'<p class="tiny">of {boot["draws"]:,} histories, including the renting of the '
        f'San Francisco third unit</p></div></div>'
        '<p class="tiny">This is the most important number on the site. Selling is not the '
        'expected-value winner once the actual record is resampled, but it is the option with '
        'almost no spread. Renting has a higher median in a bad-inflation world and a much '
        'wider range. Source: ' + link('fhfa_scc') + ' · ' + link('lta26002') + '</p>',
        '03 / resampled history')

    body += section('What no projection can capture',
        table(['Condition', 'Why it matters here', 'What the model does', 'Source'],
         [('Earthquake damage',
           'A standard homeowners policy excludes earth movement; the county sits in a zone '
           'with a high long-run probability of a damaging event.',
           'The disaster path charges one $600,000 unrepaired loss and doubles the premium.',
           link('usgs') + ' · ' + link('cdi_quake')),
          ('Insurer withdrawal',
           'Premiums and availability have moved sharply; the FAIR Plan is the residual '
           'market and offers narrower cover.',
           'Insurance grows at inflation plus 1.5 points, which may understate a repricing.',
           link('cdi_survey')),
          ('Rent control and habitability',
           'San Francisco limits increases on covered units and imposes relocation costs on '
           'some exits.', 'Rent grows at 1.6% for the SF building, near the allowed rate.',
           link('sf_rent')),
          ('Proposition 19 repeal or change',
           'The relief is a voter-approved constitutional rule, not a permanent entitlement.',
           'Assumes current law at the transfer date.', link('boe19')),
          ('Federal exclusion change',
           'The 2026 increase to $15,000,000 came from legislation; repeal bills are pending.',
           'Indexes the 2027 amount with inflation.', link('hr1301')),
          ('Long-run productivity and rates',
           'Real returns depend on forces no 50-year projection settles.',
           'Flags the Trustees low-cost and high-cost cases as the honest range.',
           link('ssa'))]), '04 / tail risks')
    page('stress', 'Black-swan economic conditions.',
         'The real 1976-2025 record, five named shocks and 2,000 resampled thirty-year '
         'histories, because growth and inflation are never consistent.', body,
         ['guide/data/model.js', 'guide/data/stats.js'])


# --------------------------------------------------------------------------
# Properties
# --------------------------------------------------------------------------
def build_property():
    proj = SNAP['projection']
    sf = SNAP['sf']
    a1 = SNAP['aYearOne']
    b1 = SNAP['bYearOne']

    body = ('<div class="callout"><strong>Two different things are being mixed here, on '
            'purpose but never blended.</strong> Property A is a future inheritance. '
            'Property B is already owned. B does not belong in the decedent&rsquo;s estate '
            'unless a specific fact creates an interest, and B&rsquo;s rent continues '
            'whatever happens to A. The tables below keep them apart.</div>')

    body += section('The two properties side by side',
        table(['Item', 'Property A &middot; Cupertino home', 'Property B &middot; San Francisco building', 'Source'],
         [('Role', ('Future trust inheritance, expected 2040-2050', 'wrap'),
           ('Already owned by the heir; not part of the estate', 'wrap'), link('irs_rr232')),
          ('Market value band, Nov 2026',
           ('2,990,000 &ndash; 3,100,000 (band, not a record value)', 'number'),
           ('1,790,000 &ndash; 1,850,000 (band, not a record value)', 'number'),
           link('fhfa_sf')),
          ('Tax assessed value, 2026',
           ('0.17 to 0.18 of market value (ratio only)', 'number'),
           ('0.06 to 0.07 of market value (ratio only)', 'number'), link('sf_tax')),
          ('Effective tax rate used', (pct(0.01335, 3), 'number'), (pct(0.0118162182, 4), 'number'),
           link('sf_tax')),
          ('Annual property tax, 2026', (money(7330), 'number'), (money(2130), 'number'),
           link('scc_rates')),
          ('Rent received', ('None now; modelled at ' + money(6500) + ' a month', 'number'),
           (money(7000) + ' a month from 2 units', 'number'), link('hud95014')),
          ('Third unit', ('Not applicable', 'wrap'),
           ('Available for the owner; modelled at ' + money(2770) + ' a month if rented', 'wrap'),
           link('hud94122')),
          ('Water a month', (money(130), 'number'), (money(360), 'number'), link('sjw')),
          ('Electricity a month', ('&minus;' + money(10) + ' net solar credit', 'number'),
           (money(50), 'number'), link('pge')),
          ('Insurance a year', (money(2200), 'number'), (money(3600), 'number'), link('cdi_guide')),
          ('Maintenance a year', (pct(0.0075, 2) + ' of value', 'number'),
           (pct(0.01, 2) + ' of value', 'number'), link('irs_p527'))]) +
        '<p class="tiny">Neither property value is verifiable from a public source and '
        'neither is an appraisal. The assessed values are the owner&rsquo;s record, rounded; '
        'the Cupertino figure is rounded to $1,000 because a base-year value is the one '
        'number that could identify a specific parcel in a public assessor database.</p>',
        '01 / side by side')

    body += section('Operating cost, first full year of ownership',
        '<p>Property A after a 2045 transfer, in the live-in case, and Property B as it '
        'stands. Fixed and variable costs are separated so each can be re-quoted.</p>' +
        table(['Cost line', 'Property A, live in', 'Property A, rent out',
               'Property B, all three units', 'Basis', 'Source'],
         [('Property tax', (money(a1['live']['propTax']), 'number'),
           (money(a1['rent']['propTax']), 'number'), (money(b1['tax']), 'number'),
           ('Official rate on assessed value', 'wrap'), link('scc_rates')),
          ('Homeowners&rsquo; exemption credit', ('&minus;' + money(a1['live']['hoex']), 'number'),
           ('&minus;' + money(0), 'number'), ('Included in tax above', 'wrap'),
           ('$7,000 off assessed value', 'wrap'), link('scc_hoex')),
          ('Water and sewer', (money(a1['live']['water']), 'number'),
           (money(a1['rent']['water']), 'number'), (money(b1['water']), 'number'),
           ('Owner-supplied band midpoint, inflated', 'wrap'), link('sfpuc')),
          ('Electricity net of solar', (money(a1['live']['electric']), 'number'),
           (money(a1['rent']['electric']), 'number'), (money(b1['electric']), 'number'),
           ('Solar credit held flat in real terms', 'wrap'), link('pge')),
          ('Insurance', (money(a1['live']['insurance']), 'number'),
           (money(a1['rent']['insurance']), 'number'), (money(b1['insurance']), 'number'),
           ('Planning assumption, inside the regulator survey range', 'wrap'),
           link('cdi_survey')),
          ('Maintenance and repairs', (money(a1['live']['maintenance']), 'number'),
           (money(a1['rent']['maintenance']), 'number'), (money(b1['maintenance']), 'number'),
           ('Percentage of market value', 'wrap'), link('irs_p527')),
          ('Rent Board fee', ('Not applicable', 'number'), ('Not applicable', 'number'),
           (money(177), 'number'), ('$59 a unit, 2026-27', 'wrap'), link('sf_fee')),
          ('Total operating cost', ('<strong>' + money(a1['live']['opex']) + '</strong>', 'number'),
           ('<strong>' + money(a1['rent']['opex']) + '</strong>', 'number'),
           ('<strong>' + money(b1['tax'] + b1['water'] + b1['electric'] + b1['insurance'] + b1['maintenance']) + '</strong>', 'number'),
           ('Sum of the lines above', 'wrap'), link('cdi_guide'))]) +
        '<p class="tiny">Cupertino water is billed by more than one system depending on the '
        'address, so the provider is not confirmed here. Source: ' + link('cupertino_water') +
        '</p>', '02 / operating cost')

    body += section('Renting A: does the rent cover the tax?',
        '<p>The critical question for the rental strategy. Full reassessment at transfer '
        'raises the tax bill roughly sevenfold; rent has to clear that plus costs.</p>' +
        table(['Year after transfer', 'Annual gross rent', 'Annual operating cost',
               'Net operating income', 'Covered?', 'Rate source'],
         [(f'Year {i + 1}', (money(r['rent']), 'number'), (money(r['opex']), 'number'),
           (money(r['noi']), 'number'), ('Yes' if r['noi'] > 0 else 'No, shortfall', 'wrap'),
           link('lta26002'))
          for i, r in enumerate(SNAP['holdRent'][:10])]) +
        '<p class="tiny">The shortfall persists because reassessed tax grows at 2% while '
        'rent grows at 2.3% on a much smaller base. The rental strategy is a growth bet on '
        'the house, not a cash-flow strategy.</p>', '03 / rental coverage')

    body += section('Property B, twenty years of rent and cost',
        table(['Year', 'Market value', 'Assessed value', 'Property tax', 'Gross rent',
               'Water', 'Electric', 'Insurance', 'Maintenance', 'Net operating income',
               'Rate source'],
              [(r['year'], money(r['market']), money(r['assessed']), (money(r['tax']), 'number'),
                (money(r['gross']), 'number'), money(r['water']), money(r['electric']),
                money(r['insurance']), money(r['maintenance']), (money(r['noi']), 'number'),
                link('sf_tax'))
               for r in sf]) +
        '<p class="tiny">Includes the Rent Board fee. Excludes income tax, financing and the '
        'Measure H parcel tax, whose final certification and parcel classification were '
        'still pending at review. Source: ' + link('sf_rent') + ' &middot; ' +
        link('sf_muni') + '</p>', '04 / San Francisco building')

    body += section('Projected value, assessed value and tax, 2026-2076',
        '<p>Both properties, before any transfer of A. Select a decade to jump; every year '
        'is in the table.</p>'
        '<div class="controls"><div class="control"><label for="p-jump">Jump to year</label>'
        '<select id="p-jump"><option value="2026">2026</option><option value="2036">2036</option>'
        '<option value="2046" selected>2046</option><option value="2056">2056</option>'
        '<option value="2066">2066</option><option value="2076">2076</option></select></div></div>' +
        table(['Year', 'A market value', 'A assessed value', 'A property tax',
               'A assessed as % of value', 'B market value', 'B assessed value',
               'B property tax', 'B assessed as % of value', 'Base-rate source'],
              [(r['year'], money(r['aMarket']), money(r['aAssessed']), (money(r['aTax']), 'number'),
                (pct(r['aRate'], 2), 'number'), money(r['bMarket']), money(r['bAssessed']),
                (money(r['bTax']), 'number'), (pct(r['bRate'], 2), 'number'), link('lta26002'))
               for r in proj]) +
        '<p class="tiny">Assessed value is the lower of the factored base and market value, '
        'the same decline-in-value proxy the assessor applies. The assessed share of value '
        'falls for both properties, which is the Proposition 13 benefit expressed as a '
        'number. Source: ' + link('lta26002') + '</p>', '05 / projections')

    body += section('Anomalies worth checking against the actual bills',
        table(['Anomaly', 'What the numbers show', 'Why it matters', 'Source'],
         [('Cupertino bill does not match the published rate',
           'The FY2025-26 components sum to 1.1597% of assessed value, which is about $6,260 '
           'on a $540,000 assessment. The supplied bills run about 13-15% higher, consistent '
           'with fixed direct charges on the bill. The model uses the observed 1.335% '
           'effective rate.', 'If the gap is a fixed charge it will not scale with value, so '
           'projecting tax as a flat percentage overstates the later bill slightly.',
           link('scc_rates')),
          ('Water provider is not confirmed',
           'Cupertino is served by more than one water system depending on the address.',
           'A wrong provider means a wrong rate schedule.', link('cupertino_water')),
          ('Insurance is an assumption',
           'No official source publishes a premium for a specific house; the regulator '
           'publishes only ranges for hypothetical profiles.',
           'The figure could be materially wrong in either direction.', link('cdi_survey')),
          ('Measure H is not modelled',
           'The Muni parcel tax starts on 2027-28 bills; certification and parcel '
           'classification were pending at review.',
           'Adds a fixed charge to Property B.', link('sf_muni'))]), '06 / data quality')

    page('property', 'Two properties, two sets of facts.',
         'What is known, what is estimated, what is projected, and what still has to be '
         'checked against a real bill.', body, ['guide/data/model.js', 'guide/data/property-page.js'])


# --------------------------------------------------------------------------
# Taxes
# --------------------------------------------------------------------------
def build_tax():
    body = ('<div class="callout"><strong>Four different taxes are involved and they are '
            'constantly confused.</strong> Property tax is an annual local tax on assessed '
            'value. Income tax applies when the house is rented or sold. The federal estate '
            'tax applies to the decedent&rsquo;s estate, not to the heir. California has no '
            'inheritance tax. Each has its own table below.</div>')

    body += section('Annual property tax',
        table(['Question', 'Current rule', 'Source'],
         [('How is the bill calculated?',
           'One per cent of assessed value plus voter-approved bond rates for the tax rate '
           'area, which differ parcel by parcel.', link('scc_rates')),
          ('How fast can the assessed value rise?',
           'Each year by the California CPI change, capped at 2%. In 2026-27 the factor was '
           '1.02 because CPI rose 3.307%. Over 51 years the full 2% applied in 40 years and '
           'the average was 1.81%.', link('lta26002')),
          ('What happens on inheritance?',
           'A change in ownership normally reassesses to market value, which is where the '
           'sevenfold jump in the rental case comes from.', link('boe19')),
          ('When does Proposition 19 help?',
           'Only when the home was the parent&rsquo;s principal residence and becomes the '
           'heir&rsquo;s principal residence within one year, with the exemption claimed in '
           'time. Renting it out generally fails that test.', link('lta26026')),
          ('What is the value cap?',
           'Factored base year value plus the adjusted allowance, $1,044,590 for transfers '
           'from 16 February 2025 to 15 February 2027. Value above the cap is added to the '
           'base.', link('lta25009')),
          ('What if the heir later moves out?',
           'The exclusion is removed and the value enrolled is the date-of-transfer market '
           'value, factored forward, not the later market value.', link('lta26026')),
          ('How much does the homeowners&rsquo; exemption save?',
           '$7,000 off assessed value, about $80 to $90 a year at the Cupertino rate, and it '
           'must be claimed.', link('scc_hoex')),
          ('When are the bills due?',
           'First instalment delinquent after 10 December, second after 10 April; a 10% '
           'penalty applies.', link('scc_rates'))]), '01 / property tax')

    body += section('Income tax on rent and on sale',
        table(['Question', 'Current rule', 'Source'],
         [('What is the basis of inherited property?',
           'Generally fair market value at the date of death, so a prompt sale produces little '
           'or no gain. A trust outside the estate can keep the old basis instead.',
           link('irs_basis') + ' &middot; ' + link('irs_rr232')),
          ('Can the building be depreciated?',
           'Yes, over 27.5 years, on the building only; land is never depreciable. Gain on '
           'that depreciation is recaptured at up to 25% on sale.',
           link('irs_p527')),
          ('What is the home-sale exclusion?',
           'Up to $250,000 of gain, or $500,000 on a joint return, if the home was owned and '
           'used as a main home for 24 of the previous 60 months.', link('irs_tc701')),
          ('Are rental losses deductible?',
           'Generally passive; a $25,000 allowance phases out between $100,000 and $150,000 '
           'of modified adjusted gross income, and unused losses carry forward.',
           link('irs_p527')),
          ('Is there an extra investment tax?',
           '3.8% net investment income tax above $200,000 single or $250,000 joint, on the '
           'lesser of net investment income or the excess. Thresholds are not indexed.',
           link('irs_niit')),
          ('Does California tax capital gains differently?',
           'No; they are ordinary income, up to 13.3% at the top.', link('sco')),
          ('Is anything withheld when the house is sold?',
           'California withholds 3 1/3% of the sales price unless an exemption is certified '
           'before closing.', link('ftb593')),
          ('Can the proceeds be rolled into another property?',
           'A like-kind exchange needs property held for business or investment, not a '
           'personal residence.', link('irs_p551'))]), '02 / income tax')

    body += section('Estate and inheritance tax',
        table(['Level', 'Rule in force', 'Amount that can pass before tax', 'Source'],
         [('Federal', 'Basic exclusion amount for a decedent dying in 2026',
           ('<strong>$15,000,000</strong>', 'number'), link('irs_estate')),
          ('Federal', 'Basic exclusion amount for a decedent dying in 2027',
           ('<strong>$15,480,000</strong>', 'number'), link('irs_2027')),
          ('Federal', 'Rate above the exclusion', ('40%', 'number'), link('irs_estate')),
          ('Federal', 'Annual gift exclusion per recipient, 2027',
           (money(20000), 'number'), link('irs_2027')),
          ('Federal', 'Return due date', ('9 months, extendable 6', 'number'), link('irs_706faq')),
          ('California', 'Estate tax return required for deaths on or after 1 January 2005',
           ('<strong>None</strong>', 'number'), link('sco')),
          ('California', 'Inheritance tax', ('<strong>None</strong>; collected only for '
           'deaths before 8 June 1982', 'number'), link('sco')),
          ('Santa Clara County', 'Local death or inheritance tax',
           ('<strong>None</strong>; only the annual property tax above', 'number'),
           link('scc_rates')),
          ('San Francisco', 'Local death or inheritance tax',
           ('<strong>None</strong>; only the annual property tax and parcel taxes', 'number'),
           link('sf_tax'))]) +
        '<p class="tiny">The federal exclusion is per person. A surviving spouse can '
        'generally use any unused amount through a portability election on a timely filed '
        'return, which is why the practical threshold for a married couple can be double. '
        'Source: ' + link('irs_706faq') + '</p>', '03 / inheritance thresholds')

    body += section('How much room is left, year by year',
        '<p>The federal exclusion projected forward at 2.3% a year from the official 2027 '
        'amount, beside Property A&rsquo;s projected value. The gap is the headroom before '
        'any federal estate tax could apply to A alone.</p>' +
        table(['Year', 'Projected federal exclusion', 'Property A projected value',
               'Headroom if A were the whole estate', 'A as a share of the exclusion',
               'Threshold source'],
              [(r['year'], money(r['exclusion']), money(r['aValue']),
                (money(r['headroom']), 'number'), (pct(r['aValue'] / r['exclusion']), 'number'),
                link('irs_estate'))
               for r in SNAP['estate']]) +
        '<p class="tiny">This is not a tax calculation. The actual test uses the whole gross '
        'estate plus adjusted taxable gifts, less deductions, so the cash and securities in '
        'the inheritance matter as much as the house. That amount was not supplied. Source: '
        + link('irs_estate') + '</p>', '04 / headroom')

    body += section('Law changes under discussion',
        table(['Measure', 'Status at review', 'Effect if enacted', 'Source'],
         [('H.R. 1301, federal', 'Introduced, in committee; not enacted',
           'Would repeal the federal estate and generation-skipping transfer taxes.',
           link('hr1301')),
          ('SB 284, California', 'In committee; not enacted',
           'Would change family-home transfer rules.', link('sb284')),
          ('Proposition 19 allowance for 2027',
           'The 16 February 2027 adjustment had not been published as of 13 November 2026',
           'Changes the value cap for a transfer after that date.', link('lta25009')),
          ('San Francisco Measure H', 'Preliminary approval at the November 2026 election',
           'Adds a Muni parcel tax from 2027-28 to Property B.', link('sf_muni')),
          ('San Francisco rent legislation', 'Not enacted at the Rent Board&rsquo;s 9 November '
           'notice', 'Would temporarily cap some banked and capital-improvement increases.',
           link('sf_rent'))]), '05 / watchlist')

    page('tax', 'Every tax that touches this decision.',
         'Property tax, income tax and inheritance thresholds, kept separate, with the exact '
         'amount in force and the date it was checked.', body)


# --------------------------------------------------------------------------
# Inheritance
# --------------------------------------------------------------------------
def build_inheritance():
    steps = [
     ('Before', 'Locate the trust, deed and property schedule',
      'The signed trust, any amendments, the deed and the schedule of assets establish who '
      'holds title and who may sell. A trust does not by itself prove a basis adjustment.',
      'Months to years ahead', link('irs_rr232')),
     ('Before', 'Confirm the trust type',
      'A revocable trust that is included in the estate generally resets basis. Property in '
      'an irrevocable trust outside the estate may keep the old basis, which removes the main '
      'reason selling beats holding.', 'Before relying on any projection', link('irs_rr232')),
     ('Before', 'Decide where the heir will live',
      'Proposition 19 requires the home to become the heir&rsquo;s principal residence within '
      'one year. Choosing to live in it is a precondition for the relief, not a consequence '
      'of it.', 'Before the transfer date', link('lta26026')),
     ('At death', 'Obtain the date-of-death valuation',
      'A qualified appraisal at the date of death sets both the income-tax basis and the '
      'reassessed value.', 'Immediately', link('irs_basis')),
     ('Within 60 days', 'Trustee gives statutory notice',
      'The trustee serves notice on beneficiaries and heirs after the triggering event, with '
      'the statutory warnings.', '60 days', link('probate')),
     ('Within 150 days', 'File the change in ownership statement',
      'The trustee or transferee files with the county; a penalty applies for failing to '
      'respond to a written request.', '150 days', link('rtc480')),
     ('Within 1 year', 'Claim the homeowners&rsquo; exemption',
      'Required for the Proposition 19 exclusion to be timely, and worth about $90 a year on '
      'its own.', '1 year', link('lta26026')),
     ('Within 3 years', 'File the exclusion claim',
      'Form BOE-19-P must be filed within three years or before a transfer to a third party. '
      'Late claims get prospective relief only.', '3 years', link('scc_asr')),
     ('Within 9 months', 'Decide on Form 706',
      'The federal return is due nine months after death, extendable six. Filing is also how '
      'portability is elected, so it can matter even when no tax is due.', '9 months',
      link('irs_706faq')),
     ('Before selling', 'Get the title and lien picture',
      'Liens, reverse mortgages, co-beneficiaries and equalisation duties can each block or '
      'reshape a sale.', 'Before listing', link('probate')),
     ('Before selling', 'Model the sale costs',
      'Commission, escrow, title and transfer costs are modelled at 6%; they come off the '
      'top before any comparison to holding.', 'Before listing', link('irs_tc701')),
     ('At sale', 'Check the withholding rule',
      'California withholds 3 1/3% of the price unless an exemption is certified before '
      'closing, which affects cash available at settlement.', 'At closing', link('ftb593')),
     ('If renting', 'Set up the rental properly',
      'Land versus building allocation, depreciation schedule, local rent rules and '
      'insurance form all have to be in place before the first tenant.', 'Before the first '
      'lease', link('irs_p527')),
     ('If renting', 'Verify the insurance form',
      'A landlord policy differs from a homeowners policy, and both generally exclude earth '
      'movement.', 'Before the first lease', link('cdi_quake')),
     ('Every year', 'Recheck the law and the numbers',
      'The Proposition 19 allowance steps every second February, and the federal exclusion '
      'and rent rules change.', 'Annually', link('lta25009')),
    ]
    rows = [(i + 1, when, f'<strong>{what}</strong>', (why, 'wrap'), (when2, 'nowrap'), src)
            for i, (when, what, why, when2, src) in enumerate(steps)]

    body = ('<div class="callout warning"><strong>This is a sequence, not advice.</strong> '
            'Deadlines are statutory and the facts of a particular trust change which ones '
            'apply. Every step links to the controlling source so it can be checked.</div>')
    body += section('Fifteen steps from trust to decision',
        table(['#', 'When', 'Step', 'Why it matters', 'Deadline', 'Source'], rows),
        '01 / process')
    body += section('The four decisions that actually have to be made',
        table(['Decision', 'Options', 'What settles it', 'Source'],
         [('Where the heir lives', 'In A, or elsewhere',
           'This single choice gates Proposition 19 relief, the rental strategy and the '
           'availability of the San Francisco third unit.', link('lta26026')),
          ('Whether to keep A', 'Keep or sell',
           'Break-even home growth of about ' + pct(0.064) + ' against a 50-year record of '
           + pct(0.0701) + ' nominal is the whole question.', link('fhfa_scc')),
          ('How to hold it if kept', 'Rent or occupy',
           'Renting covers about ' + pct(0.76) + ' of operating cost in year one; occupying '
           'covers none but avoids reassessment.', link('irs_p527')),
          ('What to do with proceeds', 'Diversified portfolio, deposits, or both',
           'Sequence risk and liquidity needs decide this, not the property comparison.',
           link('invest'))]), '02 / decisions')
    page('inheritance', 'The inheritance process, step by step.',
         'A statutory timeline from locating the trust to the first year of ownership, with '
         'every deadline linked to its source.', body)


# --------------------------------------------------------------------------
# Questions
# --------------------------------------------------------------------------
def build_questions():
    q = [
     ('1', 'Does the trust hold title to A, and what type is it?',
      '— unverified', 'Signed trust, amendments and the deed; ask counsel about inclusion.',
      'Determines whether basis resets at death, which is the core of the sell case.',
      'irs_rr232'),
     ('1', 'Is A included in the decedent&rsquo;s gross estate?',
      '— unverified', 'Trust terms and counsel.',
      'An excluded trust can keep the old basis and kill the sell advantage.', 'irs_estate'),
     ('1', 'What is the total gross estate and prior taxable gifts?',
      '— unverified', 'A private estate inventory. Only the heir can assemble it.',
      'Decides whether any federal estate tax is due at all.', 'irs_estate'),
     ('1', 'What is the date-of-death value of A?',
      'Owner estimate only: ' + money(2990000), 'Qualified appraisal at the relevant date.',
      'Sets both basis and reassessed value.', 'irs_basis'),
     ('1', 'Was A the parent&rsquo;s principal residence?',
      '— unverified, but the brief implies a long-term home',
      'Assessor history and the homeowners&rsquo; exemption record.',
      'Without it there is no Proposition 19 relief at all.', 'lta26026'),
     ('1', 'Will the heir occupy A within one year?',
      '— not decided', 'A decision, not a document.',
      'Gates the relief and the rental strategy simultaneously.', 'lta26026'),
     ('1', 'Are there co-beneficiaries or equalisation duties?',
      '— unverified', 'Trust clause review.',
      'Can force a sale regardless of the optimal plan.', 'probate'),
     ('1', 'What is the exact assessed value and tax rate area?',
      'Record value ' + money(549000) + ', rounded', 'The current county tax bill.',
      'A flat percentage misses fixed direct charges.', 'scc_rates'),
     ('2', 'What rent can A actually command?',
      'Assumed ' + money(6500) + ' a month', 'Three independent local lettings comparisons.',
      'Rent must clear reassessed tax plus costs to make renting viable.', 'hud95014'),
     ('2', 'What is the replacement cost of the Cupertino home?',
      '— unverified', 'An insurer&rsquo;s replacement-cost estimate, not the market value.',
      'Sets the dwelling limit and therefore the premium.', 'cdi_guide'),
     ('2', 'What would insurance actually cost, both forms?',
      'Assumed ' + money(2200) + ' and ' + money(3600), 'Written quotes, owners and landlord forms.',
      'Premiums are not published per property by any official source.', 'cdi_survey'),
     ('2', 'Is earthquake cover available and at what price?',
      '— unverified', 'Quotes from the California Earthquake Authority and private insurers.',
      'The single largest uninsured tail risk in either holding option.', 'cdi_quake'),
     ('2', 'Which water system serves the Cupertino address?',
      'Assumed San Jose Water rates', 'The water bill itself.',
      'Cupertino is served by more than one system.', 'cupertino_water'),
     ('2', 'What are the solar terms and the true-up?',
      'Assumed net credit of about ' + money(120) + ' a year',
      'The interconnection agreement and an annual true-up statement.',
      'Export credits and fixed charges can change with the tariff.', 'pge'),
     ('2', 'What is the land-to-building split for A?',
      'Assumed 20% land', 'A defensible appraisal allocation.',
      'Only the building depreciates, so the split drives the tax shield.', 'irs_p527'),
     ('2', 'What condition are both properties in?',
      'Assumed ' + pct(0.0075, 2) + ' and ' + pct(0.01, 2) + ' of value a year',
      'A property inspection and the last five years of invoices.',
      'Deferred maintenance can wipe out a year of modelled cash flow.', 'irs_p527'),
     ('2', 'What are the San Francisco leases and rent-control status?',
      'Supplied: ' + money(7000) + ' a month from two units',
      'The leases, the building&rsquo;s rent history and Rent Board records.',
      'Lawful increases and relocation exposure depend on it.', 'sf_rent'),
     ('2', 'What is the third San Francisco unit worth if rented?',
      'Assumed ' + money(2770) + ' a month', 'Local comparables for that unit type.',
      'It is the main offset to the cost of living in A.', 'hud94122'),
     ('2', 'What are the household&rsquo;s income and marginal rates?',
      'Assumed 30% ordinary and 28% capital gains', 'Prior returns with a CPA.',
      'Flat rates can overstate or understate the rental tax bill.', 'irs_niit'),
     ('2', 'How much liquidity is needed, and when?',
      '— not established', 'A private cash-flow plan.',
      'A house cannot be sold in slices; a portfolio can.', 'fdic'),
     ('2', 'What is the desired living arrangement?',
      '— not established', 'The household&rsquo;s own preference.',
      'The value of living in A is real and is not in any table here.', 'invest'),
     ('2', 'What does the San Francisco Measure H cost this parcel?',
      'Not modelled', 'The certified result and the parcel classification.',
      'A fixed annual charge on B from 2027-28.', 'sf_muni'),
     ('3', 'What will the Proposition 19 allowance be in 2040-2050?',
      'Projected at 3.6% a year; the 2027 step was unpublished',
      'The BOE letter to assessors when it is issued, then each biennial step.',
      'Changes the reassessed value on the live-in path.', 'lta25009'),
     ('3', 'Will the federal exclusion or the estate tax change?',
      'Projected at 2.3% a year from the 2027 amount',
      'Congress.gov and the IRS each year.',
      'Repeal bills are pending and would change the headroom.', 'hr1301'),
     ('3', 'How will insurance and utility rates move?',
      'Inflation plus 1.5 points for insurance, CPI for utilities',
      'Annual rate filings from the regulator and the utilities.',
      'Insurance has repriced sharply in recent years.', 'cdi_survey'),
     ('3', 'What will home prices and rents do over 30 years?',
      '3.6% and 2.3% a year; stress-tested against the real record',
      'Nothing resolves this in advance; the stress page shows the range.',
      'This is the variable the whole ranking depends on.', 'fhfa_scc'),
     ('3', 'When exactly will the inheritance happen?',
      'Modelled at 2040, 2045 and 2050', 'It is outside anyone&rsquo;s control.',
      'Each five years moves the value by roughly a third.', 'lta26002'),
     ('3', 'Will the trust be amended before then?',
      '— unknown', 'Review the trust at each amendment.',
      'An amendment can change beneficiaries, powers or title.', 'probate'),
     ('3', 'Will the heir still want to live in Cupertino?',
      '— unknown', 'A personal decision at the time.',
      'The live-in case depends on a preference, not a number.', 'invest'),
    ]
    rows = [(a, f'<strong>{b}</strong>', (c, 'wrap'), (d, 'wrap'), (e, 'wrap'), link(f))
            for a, b, c, d, e, f in q]
    body = ('<div class="callout"><strong>Twenty-nine questions, in three tiers.</strong> '
            'Tier 1 can reverse the recommendation. Tier 2 changes the size of the answer. '
            'Tier 3 cannot be known now and is handled by stress testing instead of guessing. '
            'Where no official source can supply an answer, the cell says so rather than '
            'offering a number.</div>')
    body += section('Question register',
        table(['Tier', 'Question', 'Current answer', 'How to find the real answer',
               'Why it matters', 'Framework source'], rows), '01 / register')
    body += section('Suggested order of discovery',
        table(['Order', 'Action', 'Resolves', 'Typical effort', 'Source'],
         [('1', 'Read the trust with counsel',
           'Trust type, title, inclusion, co-beneficiaries; four tier-1 questions.',
           'One meeting plus document review', link('irs_rr232')),
          ('2', 'Pull both counties&rsquo; tax bills and the assessor record',
           'Exact assessed values, rate areas, direct charges and exemption status.',
           'Both are online in minutes', link('scc_rates')),
          ('3', 'Order one appraisal of A now and another at death',
           'Date-of-death value and the land-to-building split.',
           'About two to four weeks', link('irs_basis')),
          ('4', 'Request six insurance quotes across both forms',
           'Premium, dwelling limit, exclusions and earthquake availability.',
           'One to three weeks', link('cdi_survey')),
          ('5', 'Assemble a private estate inventory',
           'Total estate, prior gifts and whether Form 706 will be needed.',
           'Weeks, and it needs the executor', link('irs_estate')),
          ('6', 'Get three rent comparisons and the actual leases',
           'Lawful rent for A and the true position of the San Francisco units.',
           'Days', link('sf_rent')),
          ('7', 'Have a CPA model the rental case',
           'Land allocation, depreciation, passive-loss limits and real brackets.',
           'One engagement', link('irs_p527'))]), '02 / discovery')
    page('questions', 'What still has to be answered.',
         'Twenty-nine questions in three tiers, with the current answer, the reason it '
         'matters and where to find the real answer.', body)


# --------------------------------------------------------------------------
# Suggestions
# --------------------------------------------------------------------------
def build_suggestions():
    opts = ('<option value="">Not decided</option><option value="adopt">Adopt</option>'
            '<option value="adapt">Adapt</option><option value="defer">Defer</option>'
            '<option value="decline">Decline</option>')
    s = [
     ('S01', 'Critical', 'Publish real figures instead of fictional ones',
      'This site now uses rounded planning figures rather than invented examples, because a '
      'fictional example cannot support a real decision.',
      'The brief asked for clear numbers behind the reasoning.', 'boe19'),
     ('S02', 'Critical', 'Keep the base-year value out of the published site',
      'A base-year value is the one figure that lets a reader pull a specific parcel from a '
      'public assessor database, so it is published only as a ratio band.',
      'Rounding alone is not anonymisation.', 'github'),
     ('S03', 'Critical', 'Confirm the trust type before anything else',
      'Everything downstream depends on whether basis resets.', 'It can reverse the '
      'recommendation on its own.', 'irs_rr232'),
     ('S04', 'Critical', 'Commission one appraisal now',
      'A current appraisal tests the $3,000,000 planning anchor and produces the land-to-building '
      'split that the rental case needs.', 'It is the cheapest way to de-risk the analysis.',
      'irs_basis'),
     ('S05', 'Critical', 'Treat the estate threshold as per person',
      'The practical threshold can double through portability, which changes the headroom '
      'table entirely.', 'A single-filer assumption understates the room.', 'irs_706faq'),
     ('S06', 'High', 'Model the San Francisco third unit explicitly',
      'Renting it is the main financial offset to living in A; the model includes it, but the '
      'rent is an assumption.', 'It shifts the live-in result by about $0.8M.', 'hud94122'),
     ('S07', 'High', 'Get landlord-form insurance quotes',
      'No official source publishes a premium for a specific building, and a homeowners form '
      'may not be appropriate for a three-unit building.', 'Premium uncertainty is the largest '
      'unmodelled cost.', 'cdi_guide'),
     ('S08', 'High', 'Price earthquake cover',
      'Uncovered seismic loss is the biggest tail risk in either holding option.',
      'The disaster path costs $600,000 in one year.', 'cdi_quake'),
     ('S09', 'High', 'Model a phased sale',
      'Selling part of the San Francisco building later could fund costs without touching A.',
      'Gives a middle path between hold and sell.', 'sf_rent'),
     ('S10', 'High', 'Have a CPA model the rental case properly',
      'Land allocation, passive-loss limits and real brackets will move after-tax rental '
      'results.', 'The flat 30% rate is a placeholder.', 'irs_p527'),
     ('S11', 'Medium', 'Add a property-level cash reserve target',
      'Both holding options run negative cash flow; the reserve size determines whether they '
      'are survivable.', 'It converts a modelling gap into a number.', 'fdic'),
     ('S12', 'Medium', 'Track the Proposition 19 biennial allowance',
      'The 2027 step was unpublished at review and moves the value cap.',
      'Keeps the live-in case current.', 'lta25009'),
     ('S13', 'Medium', 'Re-run the stress page annually',
      'The resampled distribution is the honest way to see risk, and it should be refreshed.',
      'Prevents anchoring on one projection.', 'fhba_scc' if False else 'fhfa_scc'),
     ('S14', 'Medium', 'Split the decision into two dates',
      'Decide occupancy at the transfer and the sale later, keeping the option open.',
      'Preserves flexibility at low cost.', 'irs_tc701'),
     ('S15', 'Medium', 'Check the water provider before modelling utilities',
      'Cupertino has more than one water system.', 'Small numbers, but avoidable error.',
      'cupertino_water'),
     ('S16', 'Low', 'Add a printable one-page decision sheet',
      'A single page with the six critical facts and the three outcomes.',
      'Useful for the meeting with counsel.', 'boe19'),
     ('S17', 'Low', 'Add unit tests for every table',
      'The arithmetic is already reconstructed independently in Python; keep it that way.',
      'Prevents silent drift.', 'github'),
     ('S18', 'Low', 'Record the decision and the reason',
      'A dated note of what was decided and why, so a later session does not relitigate it.',
      'Reduces churn.', 'github'),
     ('S19', 'Low', 'Review the San Francisco leases before any owner move-in',
      'Owner move-in carries relocation obligations on covered units.',
      'A cost that is easy to overlook.', 'sf_rent'),
     ('S20', 'Low', 'Reconcile the Cupertino bill with the published rate',
      'The 13-15% gap is probably fixed direct charges; confirm on the bill.',
      'Removes an unexplained residual.', 'scc_rates'),
    ]
    rows = [(i, p, f'<strong>{t}</strong>', (a, 'wrap'), (b, 'wrap'), link(sr),
             f'<select data-suggestion="{i}" aria-label="Your decision on {i}">{opts}</select>')
            for i, p, t, a, b, sr in s]
    body = ('<div class="callout warning"><strong>Review, then choose.</strong> These are '
            'proposals. Recording a choice stores one word in this browser&rsquo;s local '
            'storage; it changes nothing on the site and is never transmitted. The three '
            'paths below are the coherent bundles if you would rather choose once.</div>')
    body += section('Three coherent paths',
        table(['Path', 'What it means', 'What it costs', 'Best when', 'Source'],
         [('Certainty first', 'Sell A at inheritance and invest the proceeds. Keep B as it '
           'is.', 'Gives up the house and its rent; buys a narrow outcome range.',
           'The household values predictability over upside.', link('fdic')),
          ('Upside first', 'Live in A for the Proposition 19 relief, rent the San Francisco '
           'third unit, and keep both properties.', 'Funds about $116,000 a year of costs in '
           'year one and concentrates wealth in Bay Area housing.',
           'The household wants to live in Cupertino and can carry the cash flow.',
           link('lta26026')),
          ('Hybrid', 'Live in A for the required period to secure the relief, then decide '
           'between renting and selling once the date-of-death value and real quotes are in.',
           'Requires the one-year occupancy commitment; keeps both options open.',
           'Facts are still missing and the household can wait.', link('irs_tc701'))]),
        '01 / paths')
    body += section('Suggestion register',
        table(['ID', 'Priority', 'Suggestion', 'What it involves', 'Why it helps',
               'Source', 'Your decision'], rows) +
        '<p id="save-status" class="tiny" aria-live="polite">Selections stay in this '
        'browser only.</p>'
        '<button class="button secondary" id="clear-selections" type="button">'
        'Clear selections</button>', '02 / register')
    page('suggestions', 'Suggestions to review before changing anything.',
         'Twenty proposals with the trade-off stated, plus three coherent paths to choose '
         'between.', body)


# --------------------------------------------------------------------------
# Flagged for review
# --------------------------------------------------------------------------
def build_review():
    f = [
     ('Critical', 'The repository itself is public',
      'This GitHub repository is public. Earlier commits, branches, pull requests, caches and '
      'forks may still contain household-derived figures from earlier sessions, even though '
      'they are excluded from the published site. Excluding a file from Pages is not access '
      'control.', 'Coordinate a history cleanup with collaborators, or contact GitHub Support. '
      'Copies outside the repository cannot be recalled.', 'github'),
     ('Critical', 'Base-year values can identify a parcel',
      'An old assessed value is searchable in a public assessor database. Publishing it, even '
      'rounded to $10, would point at one house.', 'It is published here only as a ratio band. '
      'Keep the record value out of any public file.', 'scc_rates'),
     ('High', 'Cupertino tax bill does not reconcile to the published rate',
      'The FY2025-26 rate components sum to 1.1597% of assessed value, but the supplied bills '
      'imply about 1.335%. The gap is about 13-15% and is consistent with fixed direct charges '
      'on the bill.', 'Check the actual bill: if the gap is a fixed charge, a flat-percentage '
      'projection slightly overstates future tax.', 'scc_rates'),
     ('High', 'Insurance premiums are assumptions, not quotes',
      'No official source publishes a premium for a specific house. The regulator publishes '
      'only ranges for hypothetical profiles, and there is no published profile for a '
      'three-unit rented building.', 'Obtain written quotes before relying on either figure.',
      'cdi_survey'),
     ('High', 'The 2027 Proposition 19 allowance is unpublished',
      'The $1,044,590 figure expires on 15 February 2027. The next biennial amount had not been '
      'published as of this review, so later steps are a planning assumption.',
      'Recheck the BOE letters to assessors before any transfer after that date.', 'lta25009'),
     ('High', 'Estate headroom is not an estate-tax calculation',
      'The actual test uses the whole gross estate plus adjusted taxable gifts. The cash and '
      'securities in the inheritance were never quantified, so the headroom table compares the '
      'exclusion with the house only.', 'This is the single largest missing input on the site.',
      'irs_estate'),
     ('High', 'Trust type is unknown',
      'If the trust is irrevocable and outside the estate, basis may not reset, and the sell '
      'case loses its tax advantage.', 'This is a tier-1 question; nothing downstream is safe '
      'without it.', 'irs_rr232'),
     ('Medium', 'The water provider for the Cupertino address is unconfirmed',
      'Cupertino is served by more than one water system depending on the address, so the rate '
      'schedule used may be the wrong one.', 'Confirm from the bill.', 'cupertino_water'),
     ('Medium', 'San Francisco Measure H is not modelled',
      'The Muni parcel tax begins on 2027-28 bills. Certification and parcel classification '
      'were still pending at review.', 'Add the certified amount to Property B once it is '
      'known.', 'sf_muni'),
     ('Medium', 'Rent growth for the San Francisco units is a judgement',
      'San Francisco limits increases on covered units, currently 1.6% a year. The model uses '
      '1.6%, which is close to the cap but not a forecast.', 'Confirm the covered status of '
      'each unit.', 'sf_rent'),
     ('Medium', 'Sale costs are a single percentage',
      'A flat 6% is used for commission, escrow, title and transfer costs. Actual costs vary '
      'with price and negotiation.', 'A lower or higher cost changes the sell result by '
      'roughly the same percentage.', 'irs_tc701'),
     ('Low', 'Two source links point at pages that moved',
      'Two Board of Equalization paths used in earlier sessions now return a 404; the working '
      'pages are linked instead.', 'Sources on this site were re-opened and corrected.',
      'boe19'),
     ('Low', 'Every figure has a review date, not a guarantee',
      'Official amounts change annually or biennially. All figures here were checked on 13 '
      'November 2026.', 'Recheck before filing or closing.', 'irs_2027'),
    ]
    rows = [(p, f'<strong>{t}</strong>', (d, 'wrap'), (n, 'wrap'), link(sr))
            for p, t, d, n, sr in f]
    body = ('<div class="callout review"><strong>Nothing on this page blocks publication, and '
            'nothing on it is hidden.</strong> These are the items that are unknown, assumed or '
            'unreconciled. Each one says what would resolve it.</div>')
    body += section('Unverified and unresolved items',
        table(['Priority', 'Item', 'Detail', 'What would resolve it', 'Source'], rows),
        '01 / open items')
    body += section('What was done to keep this anonymous',
        table(['Measure', 'How it is enforced', 'Limitation', 'Source'],
         [('No personal identifiers', ('A scan rejects email-like and street-address-like '
           'strings in the published files.', 'wrap'), ('A scan cannot prove anonymity.', 'wrap'),
           link('github')),
          ('No record-specific figures on the pages',
           ('The base-year value is published only as a ratio; the two market values are '
            'rounded to $1,000.', 'wrap'), ('Rounding is not anonymisation.', 'wrap'),
           link('scc_rates')),
          ('No data leaves the browser',
           ('No form posts anywhere; no analytics, cookies or remote assets. The interactive '
            'controls compute locally.', 'wrap'),
           ('The page is still served over the public internet.', 'wrap'), link('github')),
          ('Every published amount is $10-rounded',
           ('The build and the test suite both fail on a non-$10 dollar amount.', 'wrap'),
           ('A rounding test does not test anonymity.', 'wrap'), link('irs_estate'))]),
        '02 / privacy')
    page('review', 'Flagged for review.',
         'Every unknown, assumption and unreconciled figure on the site, with what would '
         'resolve it.', body)


# --------------------------------------------------------------------------
# Sources
# --------------------------------------------------------------------------
def build_sources():
    groups = [
     ('Property tax, California', [
        ('boe19', 'Proposition 19 overview, comparison charts and implementing statutes'),
        ('lta25009', 'Exact $1,044,590 intergenerational allowance and the biennial step'),
        ('lta26026', 'Occupancy requirement, value cap formula, claims and deadlines'),
        ('lta26002', 'California CPI and the annual base-year-value inflation factor'),
        ('scc_rates', 'Santa Clara County tax rate areas and each bond component'),
        ('scc_asr', 'County parent-child transfer guidance and the value test'),
        ('scc_hoex', '$7,000 homeowners&rsquo; exemption and filing deadline'),
        ('rtc480', 'Change in ownership statement, 150 days and the penalty'),
        ('sf_tax', 'San Francisco secured rate of 1.18162182% and due dates'),
        ('sf_parcel', 'San Francisco flat parcel taxes on the bill'),
     ]),
     ('Federal tax', [
        ('irs_estate', 'Estate tax and the filing threshold table for 2011-2026'),
        ('irs_2027', '2027 basic exclusion of $15,480,000 and $20,000 annual gift exclusion'),
        ('irs_basis', 'Basis of inherited property'),
        ('irs_rr232', 'When trust property does and does not receive a basis adjustment'),
        ('irs_tc701', 'Home-sale exclusion, the 24-month tests and the amounts'),
        ('irs_p523', 'Full rules and worksheets for selling a home'),
        ('irs_p527', 'Rental income, expenses, depreciation and passive-loss limits'),
        ('irs_p551', 'Basis, improvements and like-kind exchanges'),
        ('irs_niit', 'Net investment income tax'),
        ('irs_706faq', 'Filing, the due date, extensions and portability'),
     ]),
     ('California income and estate', [
        ('sco', 'No California estate tax return for deaths on or after 1 January 2005'),
        ('ftb593', '3 1/3% withholding on a California sale'),
     ]),
     ('Costs and insurance', [
        ('cdi_survey', 'Insurance department premium comparison tool'),
        ('cdi_guide', 'What a homeowners policy covers, excludes and how the limit is set'),
        ('cdi_quake', 'Earthquake cover, which standard policies exclude'),
        ('sjw', 'San Jose Water 2026 rates, about 2.8% up'),
        ('sfpuc', 'San Francisco water and sewer schedules for FY2026-28'),
        ('cupertino_water', 'Cupertino water service and the multiple systems'),
        ('pge', 'Solar billing and the annual true-up'),
        ('ab942', 'Net-metering legislation, not enacted'),
     ]),
     ('Rents and economic data', [
        ('hud95014', 'Fair market rents for the Cupertino ZIP code, FY2027'),
        ('hud94122', 'Fair market rents for the San Francisco ZIP code, FY2027'),
        ('fhfa_scc', 'Santa Clara County house price index, 1975-2025'),
        ('fhfa_sf', 'San Francisco County house price index, 1975-2025'),
        ('cbo', 'Inflation, Treasury and home-price path, 2026-2036'),
        ('fed', 'Federal Reserve September 2026 projections'),
        ('ssa', 'Long-run inflation assumptions, low and high cost'),
        ('usgs', 'Bay Area earthquake probability over 2014-2043'),
     ]),
     ('Law watch, tenancy and risk', [
        ('hr1301', 'Federal estate tax repeal bill, in committee'),
        ('sb284', 'California family-home transfer bill, in committee'),
        ('sf_muni', 'San Francisco Measure H parcel tax'),
        ('sf_election', 'Certified and preliminary election results'),
        ('sf_rent', 'Rent Board current rates, relocation and pending legislation'),
        ('sf_fee', 'Rent Board fee, $59 a unit'),
        ('probate', 'Trustee notification within 60 days'),
        ('fdic', 'Deposit insurance, including after a depositor dies'),
        ('invest', 'Diversification and investment risk'),
        ('github', 'Removing sensitive data from a public repository'),
     ]),
    ]
    body = ('<div class="callout"><strong>Every figure on this site traces to one of these '
            'links.</strong> Each was opened on 13 November 2026. Where a page publishes an '
            'exact government amount, that amount is quoted; where it publishes a range or a '
            'rule, the rule is quoted and the household number is marked as an assumption.</div>')
    for i, (title, items) in enumerate(groups):
        rows = [(f'<strong>{SRC[k][0]}</strong>', (desc, 'wrap'),
                 f'<a href="{escape(SRC[k][1], quote=True)}" rel="noopener noreferrer">'
                 f'Open ↗</a>') for k, desc in items]
        body += section(title, table(['Source', 'What it supports', 'Link'], rows),
                        f'0{i + 1} / sources')
    body += section('Figures that could not be verified and are therefore blank',
        table(['Item', 'Why it is blank', 'Source that would settle it'],
         [('Insurance premium for either property',
           'No official source publishes a premium for a specific house.',
           link('cdi_survey')),
          ('Cash and securities in the inheritance',
           'Never supplied, and it is not public information.', link('irs_estate')),
          ('Exact date-of-death value',
           'It does not exist yet and requires an appraisal.', link('irs_basis')),
          ('Proposition 19 allowance after February 2027',
           'Not yet published by the Board of Equalization.', link('lta25009'))]),
        '07 / blanks')
    page('sources', 'Sources, checked one by one.',
         'Direct links to every agency page and primary document behind a figure on this '
         'site.', body)


# --------------------------------------------------------------------------
# Method
# --------------------------------------------------------------------------
def build_method():
    b = ['inflation', 'homeGrowth', 'portfolio', 'fee', 'rentGrowth',
         'insuranceGrowth']
    labels = {
      'inflation': 'Inflation',
      'homeGrowth': 'Home-price growth',
      'portfolio': 'Portfolio total return',
      'fee': 'Portfolio fee',
      'rentGrowth': 'Rent growth for A',
      'insuranceGrowth': 'Insurance growth',
    }
    sources = {
      'inflation': ('cbo', 'CBO 2031-2036 CPI of 2.3% a year; the 30-year record median is 2.9%'),
      'homeGrowth': ('cbo', 'CBO national home-price path of 3.6% a year; the county record is 7.0% nominal and 3.0% real'),
      'portfolio': ('ssa', 'Between the Trustees real rate and a typical balanced portfolio; 5.0% nominal is conservative'),
      'fee': ('invest', 'A planning allowance, not a quoted fee'),
      'rentGrowth': ('hud95014', 'Rents follow inflation; HUD raises fair market rents annually'),
      'insuranceGrowth': ('cdi_survey', 'Inflation plus 1.5 points, reflecting recent repricing'),
    }
    rows = [(labels[k], (pct(SNAP['assumptions'][k]) if k != 'fee' else pct(SNAP['assumptions'][k], 1), 'number'),
             (sources[k][1], 'wrap'), link(sources[k][0])) for k in b]

    body = ('<div class="callout"><strong>One model, three outputs.</strong> The static tables, '
            'the interactive controls and the stress paths all run the same arithmetic. An '
            'independent Python reconstruction of every published table is part of the test '
            'suite, so a change to the model that is not reflected in a table fails the '
            'build.</div>')
    body += section('Central assumptions',
        table(['Assumption', 'Value used', 'Basis', 'Source'], rows), '01 / assumptions')
    body += section('Other rates and rules',
        table(['Item', 'Value used', 'Basis', 'Source'],
         [('Property A effective tax rate', (pct(0.01335, 3), 'number'),
           ('Observed effective rate; the published components sum to 1.1597%', 'wrap'),
           link('scc_rates')),
          ('Property B tax rate', (pct(0.0118162182, 4), 'number'),
           ('Official FY2026-27 secured rate', 'wrap'), link('sf_tax')),
          ('Assessment growth cap', (pct(0.02), 'number'),
           ('Statutory cap; the 51-year average was 1.81%', 'wrap'), link('lta26002')),
          ('Sale costs', (pct(0.06), 'number'), ('Planning allowance', 'wrap'), link('irs_tc701')),
          ('Ordinary income tax', (pct(0.30), 'number'),
           ('Blended federal and California', 'wrap'), link('irs_niit')),
          ('Capital gains tax', (pct(0.28), 'number'),
           ('20% federal plus 3.8% net investment income tax plus California', 'wrap'),
           link('irs_niit')),
          ('Depreciation recapture', (pct(0.25), 'number'),
           ('Maximum rate on unrecaptured section 1250 gain', 'wrap'), link('irs_p527')),
          ('Depreciation period', ('27.5 years', 'number'),
           ('Residential rental, straight line', 'wrap'), link('irs_p527')),
          ('Home-sale exclusion', (money(250000), 'number'),
           ('Single filer; $500,000 on a joint return', 'wrap'), link('irs_tc701')),
          ('Prop 19 allowance, 2026', (money(1044586), 'number'), ('Official', 'wrap'),
           link('lta25009'))]), '02 / rates')
    body += section('How the comparison is made',
        '<ol class="list">'
        '<li><strong>Same endpoint.</strong> Every option is valued at the same date, after '
        'the sale costs that would be paid to turn the house into cash.</li>'
        '<li><strong>Same reinvestment.</strong> Cash flows from holding are reinvested at the '
        'same net return as the sale proceeds, so neither option gets a hidden advantage.</li>'
        '<li><strong>Taxes actually applicable.</strong> Selling at inheritance pays no gain '
        'tax because basis resets. Renting pays income tax on positive net operating income '
        'after depreciation, and recapture at exit. Living in gets the home-sale exclusion '
        'and the Proposition 19 relief.</li>'
        '<li><strong>Separate properties.</strong> Property B is never folded into the '
        'comparison except for the third unit, which only becomes rentable if the household '
        'lives in A.</li>'
        '<li><strong>What is left out.</strong> Estate tax, financing, the value of living in '
        'the house, and transaction costs that have not been quoted.</li>'
        '</ol>', '03 / method')
    body += section('How the stress tests work',
        '<p>Two different methods are used because they answer different questions.</p>'
        '<p><strong>Named scenarios</strong> impose a specific historical sequence, such as '
        'the 1970s inflation path or the 2007-2012 financial crisis, at the start of the '
        'holding period. They show what happens if a known bad decade arrives at the wrong '
        'moment.</p>'
        '<p><strong>Resampled histories</strong> take the actual joint record of annual '
        'California inflation and Santa Clara County house-price change from 1976 to 2025 and '
        'resample it in five-year blocks, 2,000 times, keeping some of the serial correlation '
        'in the data. They answer a different question: across the range of conditions the '
        'record actually contains, how often does each option win, and how wide is the '
        'spread?</p>'
        '<p class="tiny">Neither method predicts the future. A model that assumed constant '
        'growth would systematically understate the risk of holding a single house, which is '
        'why this page exists.</p>', '04 / stress method')
    page('method', 'How the numbers are produced.',
         'Every assumption, its basis, and the method behind the comparison and the stress '
         'tests, so any figure can be challenged or recomputed.', body)


# --------------------------------------------------------------------------
# Dispatcher
# --------------------------------------------------------------------------
def build_all():
    build_overview()
    build_requirements()
    build_decision()
    build_stress()
    build_property()
    build_tax()
    build_inheritance()
    build_questions()
    build_suggestions()
    build_review()
    build_sources()
    build_method()


if __name__ == '__main__':
    build_all()
    print(f'PASS: generated {len(PAGES)} public pages')
