#!/usr/bin/env python3
"""Generate the public, generic guide; never put household records in this file."""
from pathlib import Path
from html import escape
import re

ROOT=Path(__file__).resolve().parents[1]
S={
 'dgs3m':('FRED · 3-month Treasury bill (DGS3MO)','https://fred.stlouisfed.org/series/DGS3MO'),
 'dgs2':('FRED · 2-year Treasury note (DGS2)','https://fred.stlouisfed.org/series/DGS2'),
 'cg409':('IRS · Topic 409 capital gains','https://www.irs.gov/taxtopics/tc409'),
 'niit559':('IRS · Topic 559 net investment income tax','https://www.irs.gov/taxtopics/tc559'),
 'form706':('IRS · About Form 706','https://www.irs.gov/forms-pubs/about-form-706'),
 'i706':('IRS · Instructions for Form 706 (07/2026)','https://www.irs.gov/instructions/i706'),
 'usc6075':('U.S. Code · 26 U.S.C. §6075 (Cornell LII copy)','https://www.law.cornell.edu/uscode/text/26/6075'),
 'sccTax':('Santa Clara County · Property Tax (DTAC)','https://www.santaclaracountyca.org/Property_Tax.html'),
 'ftbSchedule':('FTB · 2025 Form 540 rate schedules (PDF)','https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf'),
 'boe':('California BOE · Prop 19','https://www.boe.ca.gov/prop19/'),
 'prop19':('California BOE · fact sheet','https://www.boe.ca.gov/pdf/pub801.pdf'),
 'allowance':('BOE · 2025/009','https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf'),
 'prop13':('BOE · Prop 13 explanation','https://boe.ca.gov/proptaxes/pdf/lta25023.pdf'),
 'county':('Santa Clara County Assessor','https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2'),
 'estate':('IRS · estate tax','https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax'),
 'estate27':('IRS · 2027 adjustments','https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts'),
 'basis':('IRS · inherited basis','https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances'),
 'trustbasis':('IRS · Rev. Rul. 2023-2','https://www.irs.gov/pub/irs-drop/rr-23-02.pdf'),
 'residence':('IRS · sale of home','https://www.irs.gov/taxtopics/tc701'),
 'rental':('IRS · residential rental property','https://www.irs.gov/publications/p527'),
 'ira':('IRS · retirement beneficiaries','https://www.irs.gov/retirement-plans/plan-participant-employee/retirement-topics-beneficiary'),
 'ftb':('CA Controller · estate tax','https://www.sco.ca.gov/ardtax_estate_tax.html'),
 'notice':('California Probate Code §16061.7','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=16061.7.&lawCode=PROB'),
 'ownership':('California RTC §480','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480.'),
 'sfRent':('SF Rent Board · current rates','https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit'),
 'sfTax':('SF Treasurer · secured property tax','https://sftreasurer.org/property/secured-property-taxes'),
 'sfMuni':('SFMTA · Proposition H','https://www.sfmta.com/getting-around/muni/parcel'),
 'sfElection':('SF Department of Elections · preliminary results','https://www.sfelections.org/results/20261103/index.html'),
 'sfWater':('SFPUC · water and sewer rates','https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf'),
 'water':('City of Cupertino · water','https://www.cupertino.gov/Residents/Utilities/Water'),
 'solar':('PG&E · solar billing','https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html'),
 'cdi':('CA Department of Insurance','https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/'),
 'quake':('CA Department of Insurance · earthquake coverage','https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/eq-ins.cfm'),
  'hud':('HUD · small-area rent data','https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html'),
 'fdic':('FDIC · insured deposits','https://www.fdic.gov/resources/deposit-insurance/brochures/insured-deposits'),
 'invest':('SEC · diversification','https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/world-investor-week-2026-investor-bulletin'),
 'treasuryBills':('TreasuryDirect · Treasury bills','https://www.treasurydirect.gov/marketable-securities/treasury-bills/'),
 'treasuryNotes':('TreasuryDirect · Treasury notes','https://www.treasurydirect.gov/marketable-securities/treasury-notes/'),
 'treasuryPricing':('TreasuryDirect · pricing','https://www.treasurydirect.gov/marketable-securities/understanding-pricing/'),
 'cbo':('Congressional Budget Office','https://www.cbo.gov/publication/61882'),
 'bls':('BLS · December 2022 CPI','https://www.bls.gov/news.release/archives/cpi_01122023.htm'),
 'hpi':('FHFA · house price index via FRED','https://fred.stlouisfed.org/series/ATNHPIUS41940Q'),
 'usgs':('USGS · Bay Area outlook','https://pubs.usgs.gov/publication/fs20163020'),
 'hr1301':('Congress.gov · H.R. 1301','https://www.congress.gov/bill/119th-congress/house-bill/1301'),
 'sb284':('CA Legislature · SB 284 status','https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB284'),
 'github':('GitHub · sensitive data removal','https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository'),
 'prop13factor':('BOE · 2026-27 inflation factor (LTA 2026/002)','https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf'),
 'prop13cap':('BOE · how property is assessed','https://boe.ca.gov/proptaxes/pdf/lta25023.pdf'),
 'cpiHistory':('BLS CPI-U via FRED · CPIAUCNS','https://fred.stlouisfed.org/series/CPIAUCNS'),
 'pmms':('Freddie Mac · mortgage rates','https://www.freddiemac.com/pmms'),
 'census':('Census Bureau · new housing characteristics','https://www.census.gov/construction/chars/'),
 'cdieq':('CA Department of Insurance · earthquake','https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/eq-ins.cfm'),
 'fairplan':('CA FAIR Plan','https://www.cfpnet.com/'),
 'pge':('PG&E · solar billing','https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html'),
 'sjwc':('San Jose Water · tariffs','https://www.sjwater.com/'),
 'sfpuc':('SFPUC · water and sewer rates','https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf'),
 'fed1929':('Federal Reserve History · Stock Market Crash of 1929','https://www.federalreservehistory.org/essays/stock-market-crash-of-1929'),
 'fed2008':('Federal Reserve History · The Great Recession','https://www.federalreservehistory.org/essays/great-recession-of-200709'),
 'treasury':('U.S. Treasury · daily par yield curve, November 2026','https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611'),
 'rtc480':('CA Revenue &amp; Taxation Code §480','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480.'),
 'rtc2617':('CA Revenue &amp; Taxation Code §2617','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=2617.'),
 'rtc2618':('CA Revenue &amp; Taxation Code §2618','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=2618.'),
 'irs706about':('IRS · About Form 706','https://www.irs.gov/forms-pubs/about-form-706'),
 'irs706i':('IRS · Instructions for Form 706','https://www.irs.gov/instructions/i706'),
 'irs1041about':('IRS · About Form 1041','https://www.irs.gov/forms-pubs/about-form-1041'),
 'dca':('SEC Investor.gov · dollar-cost averaging','https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging'),
 'irs701':('IRS · Topic 701, sale of your home','https://www.irs.gov/taxtopics/tc701'),
}
def source(key,label=None):
    title,url=S[key]
    return f'<a href="{escape(url,quote=True)}" rel="noopener noreferrer">{escape(label or title)} ↗</a>'
def table(headers,rows):
    h=''.join('<th scope="col">'+x+'</th>' for x in headers)
    r=''.join('<tr>'+''.join('<td'+(' class="source"' if i==len(row)-1 else ' class="wrap"')+'>'+str(x)+'</td>' for i,x in enumerate(row))+'</tr>' for row in rows)
    return '<div class="table-wrap"><table><thead><tr>'+h+'</tr></thead><tbody>'+r+'</tbody></table></div>'
def section(title,body,eyebrow=''):
    return f'<section class="section"><div class="section-head"><div>{f"<div class=eyebrow>{eyebrow}</div>" if eyebrow else ""}<h2>{title}</h2></div></div>{body}</section>'
PAGE_GROUPS=[
 ('Decide',[('overview','Overview','index.html'),('decision','Compare','guide/decision.html'),('paths','Paths, mixed and pure','guide/paths.html'),('whatif','What-if controls','guide/whatif.html'),('brief','What decides it','guide/brief.html'),('stress','Black swans','guide/stress.html')]),
 ('Property &amp; rules',[('property','Properties','guide/property.html'),('tax','Taxes','guide/tax.html'),('process','Trust steps','guide/process.html'),('timeline','Timeline','guide/timeline.html')]),
 ('Evidence &amp; terms',[('conditions','Real conditions','guide/conditions.html'),('questions','Questions','guide/questions.html'),('glossary','Glossary','guide/glossary.html'),('sources','Sources','guide/sources.html')]),
 ('Act',[('attorney-cpa','Attorney &amp; CPA sheet','guide/attorney-cpa.html'),('suggestions','Suggestions','guide/suggestions.html'),('review','Flagged','guide/review.html')]),
]
PAGES=[item for _,group in PAGE_GROUPS for item in group]
def page(key,title,lead,body,scripts=(),home=False):
    body=AP.attach(body)
    base='' if home else '../'
    nav=''.join(f'<div class="navgroup" role="group" aria-label="{gname}"><span class="navlabel" aria-hidden="true">{gname}</span>'+''.join(f'<a href="{base}{path}"'+(' aria-current="page"' if id==key else '')+f'>{label}</a>' for id,label,path in items)+'</div>' for gname,items in PAGE_GROUPS)
    links=''.join(f'<script defer src="{base}{s}"></script>' for s in ['assets/safe.js',*scripts])
    hero=f'''<section class="hero{' compact' if not home else ''}"><div class="container"><div class="eyebrow">Inheritance decision guide · reviewed 13 Nov 2026</div><h1>{title}</h1><p class="lead">{lead}</p><div class="meta"><span class="pill">Private facts withheld</span><span class="pill">Official sources linked</span><span class="pill warn">Examples are synthetic</span></div></div></section>'''
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="referrer" content="no-referrer"><title>{escape(re.sub(r'<[^>]*>', ' ', title))} · Inheritance planning</title><link rel="stylesheet" href="{base}assets/safe.css">{links}</head><body><a class="skip" href="#main">Skip to content</a><header class="header"><div class="container topbar"><a class="brand" href="{base}index.html"><span class="brand-mark">H</span><span>Inheritance planning<small>PUBLIC GUIDE · FICTIONAL EXAMPLES</small></span></a><button class="menu" aria-expanded="false" aria-controls="navigation">Menu</button><nav class="nav" id="navigation" aria-label="Main navigation">{nav}</nav></div></header><div class="notice"><div class="container"><strong>Public guide.</strong> Household financial records are not published here; figures in the calculators are fictional examples, not personal estimates. <a href="{base}guide/review.html">Important privacy limits →</a></div></div><noscript><div class="no-js">Tables of rules are available without JavaScript. Projection tables and suggestion choices require JavaScript.</div></noscript><main id="main">{hero}<div class="container">{body}</div></main><footer class="footer"><div class="container footer-inner"><div><strong>Inheritance planning</strong><br>Educational scenarios, not legal, tax, insurance or investment advice.</div><div>Source review: 13 Nov 2026 · <a href="{base}guide/sources.html">Sources</a> · <a href="{base}guide/review.html">Flagged for review</a><br>Never upload personal records to this public repository.</div></div></footer></body></html>'''
    target=ROOT/('index.html' if home else f'guide/{key}.html');target.write_text(html+'\n',encoding='utf8')

def cards(items):
    return '<div class="grid three">'+''.join(f'<a class="card card-link" href="{url}"><div class="eyebrow">{tag}</div><h3>{title}</h3><p class="muted">{desc}</p><span class="arrow">Explore →</span></a>' for tag,title,desc,url in items)+'</div>'

# ---- b33f5f9e additions: phased entry, reinvestment risk, first-screen answer, new pages ----
import sys as _sys
_sys.path.insert(0, str(ROOT / 'scripts'))
import analysis_pages as AP  # illustrative-example pages; household figures never used
CTX={'S':S,'table':table,'section':section,'source':source}
import phased_model as PM

def money(v):
    return f"${PM.round10(v):,}"

def money_range(vals):
    lo, hi = min(vals), max(vals)
    return money(lo) if PM.round10(lo) == PM.round10(hi) else f"{money(lo)} – {money(hi)}"

REC_LO, REC_HI = PM.RECOVERY['slow'], PM.RECOVERY['fast']

def _year10(template, strategy, y=None):
    y = PM.YIELDS['base'] if y is None else y
    return [PM.simulate(template, strategy, y, r)['value_end'] for r in (REC_LO, REC_HI)]

def _at36(template, strategy):
    return [PM.simulate(template, strategy, PM.YIELDS['base'], r)['value_36'] for r in (REC_LO, REC_HI)]

def _worst(template, strategy):
    return [PM.simulate(template, strategy, PM.YIELDS['base'], r)['worst_36'] for r in (REC_LO, REC_HI)]

STRAT_LABEL = {
    'sell_now_all': 'Invest all now (baseline at the peak)',
    'mixed_third': 'Mixed: one-third now; two-thirds parked 24 months, then phased in over 12',
    'park_24': 'Park 24 months, then phase in over 12',
    'park_36': 'Park 36 months, then phase in over 12',
    'cash_only': 'Cash only, no stock exposure (reference)',
}

def reinvest_table():
    rows = []
    for label, y, src in [
        ('Stress: parking yield falls to 2.50%', PM.YIELDS['low'], source('treasury', 'Treasury · stress rate, not an observation')),
        ('Observed 3-month rate, 13 Nov 2026: 4.32%', PM.YIELDS['base'], source('treasury')),
        ('Observed 2-year rate, 13 Nov 2026: 4.88%', PM.YIELDS['high'], source('treasury')),
    ]:
        rows.append((label,
                     money_range(_year10('1929', 'park_24', y)),
                     money_range(_year10('2008', 'park_24', y)),
                     money_range(_year10('none', 'park_24', y)),
                     src))
    return table(['Parking yield for the proceeds', '1929-style entry, park 24 months', '2008-style entry, park 24 months', 'No-crash control, park 24 months', 'Source'], rows)

REINVEST_OVERVIEW_HTML = (
    '<p>Proceeds that wait before they are invested earn the parking yield, and their value at the end depends on that yield. '
    'The observed U.S. Treasury par yields on 13 Nov 2026 were 4.32% for 3 months and 4.88% for 2 years. The 2.50% row is a stress '
    'assumption for falling short rates, not an observation. Only the parking yield changes between rows. Values are per $100,000 of proceeds, '
    'after 10 years, with post-trough growth between 4% and 8% a year.</p>'
    + reinvest_table()
    + '<p class="tiny">The sell, rent and live comparison on the Compare page uses its own net return assumptions. This table isolates the parking yield on sale proceeds only. See <a href="guide/brief.html">What decides it</a> for the break-even return.</p>'
)

_phase_rows = []
for k in ['sell_now_all', 'mixed_third', 'park_24', 'park_36', 'cash_only']:
    _phase_rows.append((
        STRAT_LABEL[k],
        money_range(_worst('1929', k)), money_range(_at36('1929', k)), money_range(_year10('1929', k)),
        money_range(_worst('2008', k)), money_range(_at36('2008', k)), money_range(_year10('2008', k)),
        source('fed1929', 'Fed 1929') + ' · ' + source('fed2008', 'Fed 2008') + ' · ' + source('treasury', 'Treasury'),
    ))

_ctrl_rows = []
for k in ['sell_now_all', 'mixed_third', 'park_24', 'park_36']:
    base_lo, base_hi = _year10('none', 'sell_now_all')
    v = _year10('none', k)
    cost = [a - b for a, b in zip(v, [base_lo, base_hi])]
    _ctrl_rows.append((STRAT_LABEL[k], money_range(v), money_range(cost), source('treasury', 'Treasury · parking yield') + ' · growth range is an assumption, not an official figure'))

PHASED_SECTION_HTML = (
    section('Entry risk after a sale: invest now or phase in?',
    '<div class="callout warning"><strong>An entry-risk test, not a forecast.</strong> Phasing changes the price paid for the proceeds. It does not predict when a crash starts. The table compares starting at a market peak with waiting, using two crash shapes from the official record and a no-crash control.</div>'
    '<p><strong>A second view, on observed rates.</strong> The section above uses synthetic Treasury rates. This one uses the observed 3-month and 2-year Treasury yields on 13 Nov 2026 and the official 1929 and 2008 declines. The two are different tests and are not directly comparable.</p>'
    '<p>Two official declines anchor the crash shapes. The Federal Reserve reports an 89 percent decline in stock prices from the 1929 peak to the trough (<a href="https://www.federalreservehistory.org/essays/stock-market-crash-of-1929" rel="noopener noreferrer">Fed 1929 ↗</a>). It also reports that the S&amp;P 500 fell 57 percent from its October 2007 peak to its March 2009 trough (<a href="https://www.federalreservehistory.org/essays/great-recession-of-200709" rel="noopener noreferrer">Fed 2008 ↗</a>). The 1929 template takes 34 months to reach its low and the 2008 template takes 17. Between peak and trough the path is a smooth geometric decline, not the actual index history. After the low, both shapes and the no-crash control grow at 4% or 8% a year. Those growth rates are assumptions, shown as a range.</p>'
    '<p>The proceeds are <strong>per $100,000 and invented</strong>. Parked money earns the observed 3-month Treasury rate of 4.32%. Stocks are bought in 12 equal monthly tranches when the phasing begins. The <strong>mixed path</strong> puts one-third in at once and holds the rest for 24 months, then phases it in. The pure choices bracket it.</p>'
    '<h3>Crash entries: worst point, month 36, and year 10</h3>'
    + table(['Strategy', '1929 · worst point, first 36 months', '1929 · month 36', '1929 · year 10', '2008 · worst point, first 36 months', '2008 · month 36', '2008 · year 10', 'Source'], _phase_rows)
    + '<p class="tiny">Ranges show post-trough growth of 4% (lower value) to 8% (higher value). The worst point is the lowest portfolio value in months 0 to 36, marked to market.</p>'
    + '<h3>The cost of waiting when markets rise</h3>'
    + '<p>The control has no crash: the index grows at the same 4% to 8% range. Against it, the cost of each waiting strategy is the difference from investing all now.</p>'
    + table(['Strategy, no-crash control', 'Year 10 value', 'Difference from investing all now', 'Source'], _ctrl_rows)
    + '<h3>Reinvestment risk on the parked money</h3>'
    + '<p>The parking yield is the reinvestment variable. Read the rows as: a lower yield on proceeds parked for 24 months lowers their value at year 10, in every template.</p>'
    + reinvest_table()
    + '<div class="callout warning"><strong>Read the 2008 park-24 row carefully.</strong> The template recovers from its trough at a constant rate, so every tranche bought after the trough grows exactly like the no-crash path. For that reason the 2008 park-24 values equal the no-crash park-24 values. The test shows the crash only through tranches bought before the trough. It does not model a recovery that stays below its earlier trend, which would change the result and is not included.</div>'
        + '<p class="tiny">What the test does not show: a fast, V-shaped recovery such as 2008 favours investing all now. A slow decline and recovery favours waiting. Phasing is therefore a choice about which risk the household prefers to carry, not a forecast. Reviewers should confirm the templates against official index history before relying on exact figures.</p>',
    '03 / entry risk')
)

WWCA=section('What would change the answer',table(['If this turns out to be true','Then the answer moves toward','Why it moves the answer','Official reference'],[
 ('The trust terms, not the planning premise, control what happens to the residence','A different path (sell, rent or live) from the one assumed','The trust terms are not in any official source here; counsel must read them.',source('notice')),
 ('Basis differs from the date-of-death value (for example, an alternate valuation election)','A different taxable gain on a later sale','The IRS FAQ states the general rule (fair market value on the date of death) and the alternate-valuation exception.',source('basis')),
 ('Family-home relief (Proposition 19) applies to the transfer','Whether the household lives in the home becomes the question for counsel and the CPA','The BOE describes the relief for a principal residence; the conditions are confirmed privately.',source('boe')),
 ('The estate is above the 2026 federal filing threshold of $15,000,000','A federal return and a possible estate tax','Filing and tax depend on the whole gross estate, not just this home.',source('irs706i')),
 ('A crash comes right after a sale','Phasing in over 24 to 36 months, if the entry price matters more than early growth','Phasing changes the price paid for the proceeds; the test is on the Black swans page.',source('fed2008')),
 ('Parking yields fall after the sale','A smaller lead for selling; check the break-even return on What decides it','Proceeds held in short Treasuries earn what the market pays on the day they are reinvested.',source('treasury')),
 ]),'00 / first screen')
body=WWCA+'''<section class="section"><div class="card highlight"><div class="eyebrow" style="color:#d1e8b1">Executive summary</div><h2>Make the decision after the critical facts are known.</h2><p>Property A is the anticipated Cupertino trust inheritance. Property B is an already-owned San Francisco three-unit property, not automatically part of the decedent’s estate. The planning premise is that two units are rented and a third is available for the owner; occupying that unit does not displace the other two rents. This premise is supplied, not independently verified. B’s value and continuing rent must be modeled separately.</p><p><strong>Working direction:</strong> compare selling A and investing the net proceeds with renting it, while keeping B; consider living in A if the household values that residence and meets all conditions for reassessment relief. Do not treat any example as the best plan for a real household.</p><div class="actions"><a class="button secondary" href="guide/questions.html">See the decision questions</a><a class="button secondary" href="guide/decision.html">Explore the example</a></div></div></section>'''
body+=section('What matters most',table(['Issue','What is known or needs verification','Official reference'],[
 ('Different ownership','A is the anticipated Cupertino inheritance; B is the already-owned San Francisco property. The stated two rentals and owner-available third unit are a planning premise, not independently verified. Count B in the decedent’s estate only if facts create a relevant ownership or other includible interest.',source('estate','Estate-rule context only')),
 ('Property tax','An eligible family-home transfer may qualify for limited Proposition 19 relief. Renting out A rather than occupying it generally does not satisfy that family-home condition.',source('boe')),
 ('Income-tax basis','Inherited basis is generally date-of-death fair market value, but trust and other exceptions matter. Do not confuse assessed value with income-tax basis.',source('basis')),
 ('Estate tax','Federal exposure depends on the whole decedent’s estate, prior taxable gifts, deductions, credits and elections. Actual headroom is unknown.',source('estate')),
 ('Risk and liquidity','A concentrated home and a portfolio face different risks. Diversification reduces some risks but does not guarantee a profit or prevent loss.',source('invest')),
 ]),'01 / decision context')
body+=section('The finding, in one paragraph','''<p>On every set of invented assumptions this site tests, <strong>selling the inherited residence and reinvesting the net proceeds leads</strong> once the portfolio earns a modest net return, and it leads by a wide margin in the middle case. The reason is structural rather than a matter of market timing: a property that is rented rather than occupied carries a property tax bill computed on a reassessed market value, plus upkeep that rises with price, and on this model those two lines exceed the rent. The live strategy avoids part of the tax but gives up the rent, so it trails both. What actually changes the answer is not the return assumption — it is whether a basis step-up applies, whether family-home relief is available, and whether the trust permits a sale at all.</p><p><a href="guide/brief.html">See the decision boundary, and what would have to be true for a holding strategy to win →</a></p>''','03 / the finding')

body+=section('Reinvestment risk, beside the headline',REINVEST_OVERVIEW_HTML,'03b / reinvestment')
body+=section('Readiness scorecard',table(['Fact that decides the decision','Status','Who holds the answer','Discovery step','Official framework'],[
 ('Does the trust permit a sale of the residence?','<span class="tag warn">Unverified</span>','Trustee or drafting attorney','<a href="guide/questions.html">Register D01 and D02</a>',source('notice')),
 ('Is the residence titled in the trust?','<span class="tag warn">Unverified</span>','County recorder, trustee','<a href="guide/questions.html">Register D02</a>',source('ownership')),
 ('Will basis step up to date-of-death value?','<span class="tag warn">Unverified</span>','Tax counsel','<a href="guide/questions.html">Register D03</a>',source('trustbasis')),
 ('Is family-home relief available?','<span class="tag warn">Unverified</span>','County assessor, recipient','<a href="guide/questions.html">Register D04</a>',source('prop19')),
 ('Is the estate above the federal filing threshold?','<span class="tag warn">Unverified</span>','Counsel, personal representative','<a href="guide/questions.html">Register D05</a>',source('estate')),
 ('What is the date-of-death value?','<span class="tag warn">Unverified</span>','Qualified appraiser','<a href="guide/questions.html">Register D06</a>',source('basis')),
 ('Do the San Francisco leases and unit status hold?','<span class="tag warn">Unverified</span>','Owner files, Rent Board','<a href="guide/questions.html">Register D07</a>',source('sfRent')),
 ('What is the achievable rent floor?','<span class="tag warn">Unverified</span>','Property manager, comparables','<a href="guide/questions.html">Register D10</a>',source('hud')),
 ])+'<p class="tiny">Zero of eight resolved. Each row links to the register entry that names the exact document, who holds it, and a typical lead time. The register has sixteen entries in total; these eight are the ones that can change the answer.</p>','04 / readiness')

body+=section('Explore the guide',cards([
 ('01 / compare','Live, rent or sell','See assumptions, same-endpoint results and yearly costs for a fictional case.','guide/decision.html'),
 ('01b / boundary','What decides it','Which inputs flip the ranking, and what would have to be true for a holding strategy to win.','guide/brief.html'),
 ('02 / uncertainty','Black-swan paths','Stress 50 years with inflation, crashes and a disaster; inspect every year.','guide/stress.html'),
 ('02b / evidence','Real conditions','The observed inflation and assessment record, the official projection horizon, and the scenario bands.','guide/conditions.html'),
 ('03 / rules','Tax &amp; inheritance','Separate federal estate tax, income-tax basis, reassessment and trustee steps.','guide/tax.html'),
 ('04 / readiness','Questions to resolve','A prioritized list of missing records, answers and discovery routes.','guide/questions.html'),
 ('05 / improvements','Suggestions to review','Choose or defer ideas without applying them to the site or the analysis.','guide/suggestions.html'),
 ('06 / review','Flagged for review','See the public-repository exposure and other unresolved issues.','guide/review.html'),
 ]),'02 / navigate')
body+='''<section class="section"><div class="callout review"><strong>Privacy is not solved by rounding.</strong> This public guide omits personalized financial histories and uses invented values. Earlier repository revisions, old branches, pull requests and caches can still expose information. The repository itself is public; a Pages exclusion is not access control. <a href="guide/review.html">Read the incident and limitations →</a></div></section>'''
page('overview','A clearer way to plan<br>for an inheritance.','A source-linked guide to comparing a possible Cupertino inheritance with an already-owned San Francisco property, without publishing private records.',body,home=True)

body=section('How to read the two properties',table(['Property','Role in the analysis','What is still missing','Reference'],[
 ('A · Cupertino home','Anticipated future transfer through a trust. A living, rental or sale strategy changes its tax and cash flows.','Trust terms, inclusion, basis, value, parcel rate and eligibility are unverified.',source('prop19')),
 ('B · San Francisco property','Already owned: planning premise of two rented units plus a third available for the owner without displacing those rents. B is modeled separately, not automatically included in the decedent’s estate.','The supplied unit/occupancy description, title, leases, expenses and coverage need private confirmation.',source('estate','Estate-rule context only')),
 ]))
body+=section('Actual property figures', '<p>These cells are intentionally blank: the public guide cannot independently verify a household’s bills, valuation or policy and should not disclose them. A source below describes the rule or where to investigate, not the private amount.</p>'+table(['Item','Confirmed value','How to verify privately','Official context'],[
 ('Market value of A or B','<span class="empty">— unverified</span>','Independent appraisals and comparable sales; revalue at relevant dates.',source('basis')),
 ('Factored assessment and actual property-tax bill','<span class="empty">— unverified</span>','County assessor records, actual bill and tax-rate area; verify parcel-specific direct charges.',source('prop13')),
 ('Reassessed value and tax after transfer','<span class="empty">— unverified</span>','Confirm the assessor’s value, eligible relationship, residence status and local rate.',source('county')),
 ('Rent, vacancy, lawful increases','<span class="empty">— unverified</span>','Review leases and collections privately; verify local rules and use independent rent comparables.',source('sfRent')),
 ('Owner-occupied home insurance','<span class="empty">— unverified</span>','Get quotes with rebuild limit, deductible, occupancy and exclusions.',source('cdi')),
 ('Owner-occupied building with rental units','<span class="empty">— unverified</span>','Ask insurers which owner-occupied or landlord form fits the building and occupancy; do not assume the product.',source('cdi')),
 ('Water / sewer bills','<span class="empty">— unverified</span>','Confirm provider, meter, usage and applicable schedule from bills. Cupertino has more than one water system.',source('water')),
 ('Electricity and solar credits','<span class="empty">— unverified</span>','Review annual true-up, tariff, interconnection date and fixed charges; a credit is not a guaranteed profit.',source('solar')),
 ('Maintenance / capital repairs','<span class="empty">— unverified</span>','Review multi-year invoices, inspection findings and contractor quotes; distinguish regular maintenance from capital improvements.',source('rental')),
 ]),'Private inputs')
body+=section('Local context',table(['Topic','Current general information','Reference'],[
 ('Property A water','The city identifies three water systems. ZIP code alone does not establish the provider or bill.',source('water')),
 ('Property B water','SFPUC publishes water and sewer schedules; the actual bill depends on service configuration and use.',source('sfWater')),
 ('Rental increases','For covered SF rent-controlled units, the general annual allowable increase is 1.6% from 1 March 2026 through 28 February 2027; actual applicability and notices must be checked.',source('sfRent')),
 ('Proposition H parcel tax','SFMTA states that voters approved Proposition H on 3 November 2026 and publishes the FY 2027–28 schedule and the exemption rules. The elections office still labels its own results preliminary as of this review. The amount for B depends on parcel facts that are not public; it is set out below and is not included in B’s example.',source('sfMuni')+' · '+source('sfElection')) ,
 ('Solar','An interconnection’s tariff and annual true-up matter; neither a monthly credit nor a future tariff is confirmed here.',source('solar')),
 ('Insurance','The regulator’s premium survey compares hypothetical profiles and is not a quote. Standard homeowners coverage generally excludes earthquake damage, with exceptions; review the actual policy.',source('cdi')+' · '+source('quake')),
 ]))
body+=section('Proposition H parcel tax — official schedule for B','<p>San Francisco voters approved Proposition H on 3 November 2026. SFMTA publishes the FY 2027–28 annual amounts by parcel type and taxable building area, bills the first tax on fiscal year 2027–28 bills mailed in autumn 2027, and indexes the amounts with inflation from FY 2028–29. The measure runs from 1 July 2027 to 30 June 2042. The rows below are the published amounts; they are official rates, not estimates.</p>'+table(['Parcel type','Taxable building area','Official annual amount, FY 2027–28','Amount for Property B','Reference'],[
 ('Multifamily residential','Up to 5,000 sq ft','$249','<span class="empty">— unverified</span>',source('sfMuni')),
 ('Multifamily residential','Over 5,000 sq ft','$249 plus $0.195 per sq ft over 5,000, capped at $50,000','<span class="empty">— unverified</span>',source('sfMuni')),
 ('Single-family residential','Up to 3,000 sq ft','$129','<span class="empty">— unverified</span>',source('sfMuni')),
 ('Single-family residential','3,001–5,000 sq ft','$129 plus $0.42 per sq ft over 3,000','<span class="empty">— unverified</span>',source('sfMuni')),
 ('Amount for Property B','Parcel type and taxable building area are not public facts','Official schedule verified; the amount cannot be computed from public information','<span class="empty">— unverified</span>',source('sfMuni')),
 ])+'<p class="tiny">Why B’s amount is blank: the tax depends on the parcel type the Assessor-Recorder uses and on taxable building area. Neither can be read from a public page, so no figure is computed here. Exemptions and reductions exist for qualifying senior owners, SRO parcels and parcels on which no property tax is levied; the exemption application deadline is 1 June for the coming fiscal year. The measure is not included in the synthetic operating table on the comparison page, so that table understates B’s costs from FY 2027–28 onward.</p>','')
page('property','Two homes, different roles.','The inherited property and the existing property must not be blended into one estate. Actual household figures are deliberately withheld.',body)

body=section('Property-tax rules',table(['Question','Current rule / limitation','Reference'],[
 ('What changes at transfer?','Change in ownership can cause reassessment. The Proposition 13 factored base year value generally grows by the inflation factor, capped at 2%, absent reassessment or new construction; declining-market relief can apply.',source('prop13')),
 ('When can Proposition 19 help?','Generally an eligible parent-child family-home transfer requires the transferor’s principal residence and the transferee to make it their principal residence within one year and continue occupancy. Special rules apply to other eligible transfers.',source('prop19')),
 ('How much value is protected?','For 16 Feb 2025–15 Feb 2027 the additional allowance is approximately <strong>$1,044,590</strong>, rounded from the official amount. If fair market value exceeds factored base value plus the allowance, the excess is added to the factored value. The Board states the allowance is adjusted every other February 16; a county summary page describes a different cadence, so the Board’s Letters to Assessors govern. Later amounts are unknown.',source('allowance')+' · '+source('county')),
 ('Does renting qualify?','Renting the inherited home instead of making it the eligible transferee’s principal residence generally fails the family-home condition. Confirm facts with the assessor.',source('boe')),
 ]))
body+=section('Estate, gift and income tax',table(['Item','Official current information','Case-specific amount','Reference'],[
 ('Federal basic exclusion','<strong>$15,000,000</strong> for deaths in 2026; <strong>$15,480,000</strong> in 2027. Prior taxable gifts and an available transferred spousal exclusion may change the available amount.','— unverified',source('estate27')),
 ('Filing threshold versus taxable estate','The filing threshold generally tests the gross estate plus adjusted taxable gifts and certain exemption amounts. Deductions are relevant to taxable estate and tax, not a simple subtraction from the gross filing test.','— unverified',source('estate')),
 ('California','The Controller says no California estate-tax return is required for deaths on or after 1 January 2005. Other taxes, and taxes of other jurisdictions if relevant, are separate.','— unverified',source('ftb')),
 ('Income-tax basis','Inherited property generally receives date-of-death FMV basis, subject to exceptions and elections. One particular irrevocable grantor-trust fact pattern outside the estate did not receive an adjustment.','— unverified',source('trustbasis')),
 ('Retirement accounts','Taxable inherited IRA distributions may be income to the beneficiary; treatment and timing depend on account and beneficiary rules.','— unverified',source('ira')),
 ('Federal home-sale exclusion','Up to $250,000, or $500,000 for qualifying joint filers, subject to ownership, use and other conditions; it is not automatic.','— unverified',source('residence')),
 ]))
body+=section('Future federal exclusion: illustration only','<p>Starting at the official 2027 amount, the numbers below apply an invented 2% yearly growth rate. They are <strong>not IRS forecasts</strong>; actual future law and adjustments are unknown. Estate liability and actual headroom remain blank.</p><div class="table-wrap"><table><thead><tr><th scope="col">Year</th><th scope="col">Illustrative exclusion</th><th scope="col">Actual available exclusion / headroom</th><th scope="col">Context</th></tr></thead><tbody id="estate-projections"></tbody></table></div>')
body+=section('Law-change watchlist',table(['Measure','Status checked 13 Nov 2026','Potential relevance','Reference'],[
 ('H.R. 1301 · federal','Introduced; referred to the House Ways and Means Committee. Not enacted.','Would repeal federal estate and generation-skipping transfer taxes if enacted as proposed; recheck before reliance.',source('hr1301')),
 ('SB 284 · California','Official status page lists it in committee; not enacted as of review.','Proposes changes to family-home transfer rules. Existing Proposition 19 remains the model’s framework.',source('sb284')),
 ('SF Proposition H','SFMTA states that voters approved the measure on 3 November 2026 and publishes the FY 2027–28 schedule; the election office still labels its own results preliminary at review.','A parcel tax reaches FY 2027–28 bills and is indexed with inflation from FY 2028–29. The official schedule is published on the Properties page; the amount for B is not computable from public information and is not modeled.',source('sfMuni')+' · '+source('sfElection')),
 ('Proposition 19 adjustment cadence','Two official pages differ: the Board says the one-million-dollar allowance is adjusted every other February 16, while the county assessor page says it is adjusted annually beginning in 2023. The guide follows the Board.','The amount and its date must come from the Board’s Letters to Assessors. The assessor’s page is a local summary, not the governing rule.',source('allowance')+' · '+source('county')),
 ('SF File 261020','Rent Board notice says the proposal has not been enacted as of its 9 Nov 2026 notice.','Would temporarily limit combined certain banked and capital-improvement increases for covered units, if enacted.',source('sfRent')),
 ]))
page('tax','Taxes and the rules that matter.','Current law, future assumptions, and unknowns are kept separate. Recheck the official links before making a filing or decision.',body,['guide/data/model.js','guide/data/tax-page.js'])

body=section('A practical sequence',table(['When','Step','Why / caution','Official reference'],[
 ('Before a transfer','Locate the signed trust, amendments, deed, property schedule, beneficiary designations and trustee powers. Privately confirm ownership and estate inclusion.','A trust does not by itself prove a particular basis adjustment or authority to sell.',source('trustbasis')),
 ('At the triggering event','Successor trustee accepts the role, safeguards the home, arranges insurance and retains certified records through private channels.','Review occupancy, coverage, liens, beneficiaries and required notices with counsel.',source('notice')),
 ('Generally within 60 days when required','Provide statutory trustee notification to required recipients after an applicable triggering event; statutory timing and exceptions depend on the facts.','Do not assume every trust triggers the same notice or deadline.',source('notice')),
 ('Within 150 days for qualifying nonprobate death transfers','Trustee or transferee files the change-in-ownership statement with the county where required. For probate, the statute has a different inventory-and-appraisal deadline.','Check the precise form, dates and county instructions.',source('ownership')),
 ('Within one year, if seeking family-home relief','An eligible transferee must move into the home within one year; timely file the homeowners’ or disabled veterans’ exemption to obtain exclusion from the transfer date.','Delayed exemption claims can have prospective effect; confirm current rules and special cases.',source('prop19')),
 ('Claim the exclusion','File BOE-19-P or applicable claim generally within three years and before transfer to a third party. A claim can also be timely within six months of the applicable supplemental or escape assessment notice.','A missed or late filing can affect when relief begins.',source('prop19')),
 ('Value and account','Arrange qualified date-of-death valuations; list includible assets, debts, prior gifts, distributions and liquidity.','Basis and estate filing tests differ; already-owned heir assets are not automatically the decedent’s.',source('estate')),
 ('By applicable federal deadline','Determine if Form 706 is required or desirable for portability; check Form 1041 and final income returns.','An extension to file is not automatically an extension to pay; get advice.',source('estate')),
 ('Only after the review','Compare sale, rental and occupancy on equal time horizons and after documented costs and taxes; follow trust authority and local rental rules.','Avoid irreversible action solely on illustrative projections.',source('rental')),
 ]))
page('process','From trust to decision, step by step.','A checklist for a future transfer, not a substitute for the trust instrument, county instructions or professional advice.',body)

questions=[
 ('1','Who owns A, and does the signed trust actually hold title?','Rule known: where an interest transfers by reason of death, including through a trust, the trustee or transferee files the change-in-ownership statement with the county recorder or assessor within 150 days of death; where the property is probated, the statement is filed with the inventory and appraisal. That fixes who must file, not who holds title.','— unverified','Read deed, trust schedule and amendments with the trustee.', 'Changes authority to transfer or sell.','ownership'),
 ('1','What type of trust, what powers and which beneficiaries?','Rule known: a trustee must serve written notification on the beneficiaries and heirs of a deceased settlor within 60 days of specified events, including a revocable trust becoming irrevocable because of a settlor’s death. The trust instrument, not the statute, sets the powers and the distribution timetable.','— unverified','Obtain signed trust and amendments privately; ask counsel about distribution powers.', 'Affects allocation, timing, tax and contest risk.','notice'),
 ('1','Does A qualify for an income-tax basis adjustment?','Rule known: inherited property generally takes its basis in the fair market value at the decedent’s death. Where property is not includible in the decedent’s gross estate, no basis adjustment applies — the IRS so held for the irrevocable-trust fact pattern in Rev. Rul. 2023-2.','— unverified','Ask a tax lawyer to assess title, estate inclusion and trust facts.', 'An unadjusted basis can change the sale analysis materially.','trustbasis'),
 ('1','Was A the transferor’s principal residence and can an eligible recipient occupy it on time?','Rule known: for a parent–child family-home transfer the transferee must make the home their principal residence within one year and claim the homeowners’ or disabled veterans’ exemption within that year, or the exclusion starts in the year the claim is filed. Renting the home out does not satisfy the family-home condition.','— unverified','Document residence and relationship; ask the county assessor about special circumstances.', 'Determines eligibility for family-home reassessment relief.','prop19'),
 ('1','What is the complete gross estate, prior taxable gifts, debts and available spousal exclusion?','Rule known: a return is required only if the gross estate plus adjusted taxable gifts and specific gift tax exemption exceeds the filing threshold, which is $15,000,000 for a 2026 death. Deductions bear on the taxable estate, not on that filing test. California requires no estate-tax return for deaths on or after 1 January 2005.','— unverified','Prepare a confidential estate inventory with advisers; include all relevant interests.', 'Determines filing and estate tax; no actual headroom can be calculated yet.','estate'),
 ('1','What is the property’s date-of-death fair market value?','Rule known: the basis is generally the fair market value at the date of death, or at the alternate valuation date if the executor elects it on Form 706. A qualified appraisal is how that value is established and documented.','— unverified','Obtain a qualified appraisal at the relevant date; retain private documentation.', 'Sets the usual basis and affects reassessment and sale proceeds.','basis'),
 ('1','Are there co-beneficiaries, equalization duties, debts or liens?','Rule known: the trust instrument, the lien records and the probate rules decide who may take property free of claims and when. No statute published on this site answers that for a particular trust.','— unverified','Review trust, loans, liens and distribution terms privately.', 'Could constrain the ability or timing to keep or sell.','notice'),
 ('1','What are the actual assessed values and parcel-specific tax rates?','Rule known: Proposition 13 caps annual assessed-value growth at 2% and limits the property tax rate to 1% plus voter-approved debt; a change in ownership generally sets base year value to market value, subject to exclusions. Where market value falls below the factored base year value, decline-in-value relief applies.','— unverified','Read county bill and tax-rate-area details for each property.', 'A simple percentage misses direct charges and reassessment timing.','prop13'),
 ('1','What are the dwelling replacement costs and actual insurance quotes?','Rule known: the Department of Insurance publishes premium-comparison surveys and states on the page that they are not quotes; it is a regulator and cannot issue one. Standard homeowners policies exclude earthquake damage, with a separate California Earthquake Authority policy available.','— unverified','Get owner-occupied and rental/owner-occupied-multiunit quotes as applicable.', 'Premium, deductible, exclusions and vacancy terms alter cash flow and risk.','cdi'),
 ('1','How much are lawful market rent, vacancy and management costs for A?','Rule known: HUD small-area fair market rents are ZIP-code benchmarks calculated for Housing Choice Voucher payment standards. They are not a rent quote and do not determine a lawful rent.','— unverified','Get independent current comparables and professional management estimates.', 'Rental economics and legal limitations can change the ranking.','hud'),
 ('1','What are the current leases and rent-control status for B?','Rule known: for covered San Francisco units the general annual allowable increase is 1.6% from 1 March 2026 through 28 February 2027. Board of Supervisors File 261020 would limit combined banked and capital-improvement increases, but the Rent Board’s 9 November 2026 notice states it has not been enacted.','— unverified','Review leases, building history and Rent Board rules privately.', 'Income and lawful increases cannot be inferred from a benchmark.','sfRent'),
 ('2','Who pays utilities and what are actual bills?','Rule known: Cupertino supplies water through three separate systems — California Water Services, San Jose Water Company and the city-operated system — so a ZIP code does not identify the provider or the rate schedule.','— unverified','Review a year of bills, meter counts, provider and lease terms.', 'Water, sewer and electricity are not fixed by the ZIP code.','water'),
 ('2','What solar tariff and interconnection date apply?','Rule known: PG&E’s Solar Billing Plan produces a monthly statement and an annual True-Up statement. The tariff a system keeps and the value of any export credit depend on when the system was authorised to operate, so a monthly credit is not assured.','— unverified','Review interconnection agreement and annual true-up privately.', 'Future export credits and fixed charges may differ.','solar'),
 ('2','What repairs and capital improvements are likely?','Rule known: rental expenses are deductible only if the property is rented or held for production of income; capital work is generally depreciated rather than deducted, and whether an item is a repair or an improvement is a question of fact that the records decide.','— unverified','Obtain inspections, multi-year invoices and contractor estimates.', 'Maintenance, capital basis and one-off risks affect both costs and tax.','rental'),
 ('2','What is land versus building value if A is rented?','Rule known: land is not depreciable; the building portion is. The allocation between them is an appraisal and tax-preparer question, not a published figure.','— unverified','Use a defensible appraisal and tax preparer’s depreciation schedule.', 'Depreciation and later recapture can materially change the comparison.','rental'),
 ('2','What are the income, brackets and potential passive-loss limits?','Rule known: the comparison page uses a flat scenario rate. The actual tax follows the taxpayer’s own brackets, other income and the passive-loss rules in Publication 527.','— unverified','Prepare confidential taxpayer-specific scenarios with a CPA.', 'Flat scenario rates are not the actual combined tax.','rental'),
 ('2','What is the type and beneficiary treatment of inherited cash or retirement accounts?','Rule known: beneficiaries of an IRA and most plans may take a lump-sum distribution at any time and must include taxable distributions in gross income; a designated beneficiary who is not an eligible designated beneficiary follows the 10-year rule. Cash and securities carry no equivalent beneficiary rule.','— unverified','Inventory account types and designations privately with an adviser.', 'IRA distributions and cash or securities have different tax treatment.','ira'),
 ('2','What is the desired living arrangement and the value of housing services?','Rule known: none — no official source governs this question. It is a household preference, and the financial ranking on the comparison page deliberately omits the value of housing services.','— preference not established','Compare nonfinancial needs, work, accessibility and alternate housing privately.', 'A financial ranking omits the benefit of living in a home.','invest'),
 ('2','How would sale proceeds be invested, and how much liquidity is needed?','Rule known: FDIC insurance covers depositor accounts dollar-for-dollar up to the limit; for a trust owner with five or more beneficiaries that limit is $1,250,000 per owner for all trust accounts held at the same bank. Diversification and asset allocation can reduce risk but do not guarantee returns.','— preference not established','Set an investment policy, risk tolerance and deposit-insurance plan.', 'Returns, tax drag and sequence risk are assumptions, not guarantees.','fdic'),
 ('3','What laws, valuation and insurance conditions will apply at the event?','Rule known: the official baseline is CBO’s February 2026 outlook for 2026–2036, in which PCE inflation returns to about 2% by 2030. It is a ten-year budget outlook, not a 50-year housing or portfolio forecast, and future law is unknown.','— not knowable yet','Recheck official sources regularly and immediately before a decision.', 'Future law and prices can make today’s model obsolete.','cbo'),
]
priority_counts={p:sum(1 for row in questions if row[0]==p) for p in ('1','2','3')}
open_household=sum(1 for row in questions if row[3].startswith('—'))
rule_settled=sum(1 for row in questions if row[2].startswith('Rule known'))
body='<div class="callout"><strong>How to use this register:</strong> Priority 1 items can overturn the comparison or affect a deadline. The <em>answer already known</em> column states the rule exactly as the official source gives it today. The household’s own answer stays blank on this public site by design and must be gathered privately. Do not enter personal answers into the public site.</div>'
body+=section('Can a decision reasonably be made yet?','''<div class="grid three">
 <div class="card"><div class="eyebrow">Priority 1 · gates the decision</div><h3>'''+str(priority_counts['1'])+''' open</h3><p class="muted">Each can change the ranking between sell, rent and live, or miss a filing deadline.</p></div>
 <div class="card"><div class="eyebrow">Priority 2 · changes the numbers</div><h3>'''+str(priority_counts['2'])+''' open</h3><p class="muted">Cost, depreciation and preference inputs that move the result without usually moving the ranking.</p></div>
 <div class="card"><div class="eyebrow">Priority 3 · recheck at the time</div><h3>'''+str(priority_counts['3'])+''' open</h3><p class="muted">Law, prices and conditions that cannot be known now and must be rechecked near the event.</p></div>
</div><p class="tiny">Register totals: '''+str(len(questions))+''' questions — '''+str(priority_counts['1'])+''' / '''+str(priority_counts['2'])+''' / '''+str(priority_counts['3'])+''' by priority — with the household answer still blank on all '''+str(open_household)+''', and a rule-level answer settled from an official source on all '''+str(rule_settled)+'''. Every question below states the rule that is settled today; what is missing is the household’s own facts.</p><div class="callout warning"><strong>Answer: not yet.</strong> A live, rent or sell decision cannot reasonably be made today, because every Priority 1 item is still open and each one is a fact that only the household’s own records and advisers can supply. What is settled is the rule set, which is what makes a private comparison possible at all. Close the Priority 1 items first — the <a href="suggestions.html">suggestions register</a> lists the route for each one.</div>''')
body+=section('Questions, answers and discovery',table(['Priority','Question','Answer already known from official sources','Household answer','How to discover privately','Decision impact','Official framework'],[(a,b,c,d,e,f,source(g)) for a,b,c,d,e,f,g in questions]))

# ---------------------------------------------------------------- discovery register
# Each row: (id, priority, question, why_it_blocks, document_or_source, holder, lead_time, official_link_key, gate)
# The gate marks whether the answer can change the ranking on the comparison page.
DISCOVERY=[
 ('D01','1','What kind of trust is it, who is trustee, and does the instrument give the trustee power to sell the residence?',
  'Selling may not be a decision available to the beneficiary at all. If the trustee must sell, or must keep the property for another beneficiary, the comparison is moot.',
  'The signed trust instrument, every amendment, and the schedule of assets. Ask counsel to confirm the trustee’s powers and any requirement to hold or divide the property in kind.',
  'Settlor, trustee, or the estate-planning attorney who drafted it','Weeks; potentially months if the attorney is unavailable','notice','Ranking-changing'),
 ('D02','1','Is the residence actually titled in the trust, or is it still in individual names with a pour-over will?',
  'Title controls who can convey, and it drives both the basis question and the reassessment question. A trust that names the house but does not hold title can force probate.',
  'A current grant deed and a preliminary title report. A title company will produce the report for a modest fee, and it shows every recorded interest.',
  'County recorder; the trustee; a title company','Days for the recorded deed; one to two weeks for a title report','ownership','Ranking-changing'),
 ('D03','1','Did the decedent retain a power that causes the residence to be included in the gross estate, and therefore to receive a basis step-up?',
  'If basis does not step up, an immediate sale produces a taxable gain that can consume a large share of the proceeds. This single answer can flip sell from first to last.',
  'Trust instrument plus the decedent’s Forms 709 and 706 if any were filed, reviewed by a tax attorney. Rev. Rul. 2023-2 is the IRS example of a grantor-trust pattern that did not receive an adjustment.',
  'Tax counsel; the decedent’s accountant; the trustee’s records','One to three weeks for a written opinion','trustbasis','Ranking-changing'),
 ('D04','1','Was the residence the decedent’s principal residence, and can an eligible child occupy it within one year?',
  'Prop 19 family-home relief requires occupancy by an eligible transferee. Without it the base resets to market value and the annual tax can multiply.',
  'The decedent’s last filed homeowners’ exemption record at the county assessor, plus a documented occupancy plan from the recipient.',
  'Santa Clara County Assessor; the recipient’s own decision','Days for the exemption record; the occupancy plan is a family decision','prop19','Ranking-changing'),
 ('D05','1','What is the complete gross estate, including prior taxable gifts and any spousal exclusion available?',
  'Federal estate tax is assessed on the whole estate, not on this house. Without the total, no headroom exists and no tax can be estimated. Portability must be elected on a timely return.',
  'A confidential estate inventory prepared with counsel: every account, policy, real property, business interest, debt, prior gift and the decedent’s marital history.',
  'Personal representative or trustee; counsel; financial institutions','Two to six weeks, longer if accounts are hard to trace','estate','Ranking-changing'),
 ('D06','1','What is the date-of-death fair market value of the residence?',
  'Basis, reassessment and the estate filing all reference this value. An appraisal prepared for the estate is the defensible record; a later one is not the same number.',
  'A qualified retrospective appraisal as of the date of death, with the comparable sales attached.',
  'Licensed appraiser, engaged by the trustee or counsel','Two to four weeks after engagement','basis','Ranking-changing'),
 ('D07','1','What are the current leases, occupancy and rent-control status of each unit in the San Francisco property?',
  'Existing tenancy and coverage determine lawful rent, notice requirements and whether the owner can occupy a unit at all. The premise of two rents plus a free unit is unverified.',
  'Signed leases, rent history, security deposit records, and the Rent Board’s unit history. Relocation rules apply to some owner move-ins.',
  'The owner’s own files; SF Rent Board records','Days for the owner’s own files; one to two weeks for Rent Board history','sfRent','Ranking-changing'),
 ('D08','2','What are the actual assessed values, tax-rate areas and direct charges on both parcels?',
  'A single blended percentage hides parcel-specific direct charges, bond levies and any special assessments. It also hides the actual assessed value the county uses.',
  'The current secured tax bill for each parcel, showing the rate area and every direct charge as a separate line.',
  'Santa Clara County Tax Collector; SF Treasurer & Tax Collector','Days; both publish online bill lookup','prop13','Ranking-changing'),
 ('D09','2','What would it cost to insure each property, for each occupancy, including or excluding earthquake?',
  'Premium is a real recurring cost and, more importantly, coverage determines whether an earthquake or water loss is a balance-sheet event or an inconvenience.',
  'Binding quotes for a homeowners form on the residence and a landlord form on the multi-unit property, each with and without earthquake coverage, plus a FAIR Plan comparison if the standard market declines.',
  'Licensed brokers; the California FAIR Plan','One to three weeks; longer in a tight market','cdieq','Ranking-changing'),
 ('D10','2','What is the achievable market rent for the residence, and what would professional management cost?',
  'The rent break-even table shows the rental only works above a rent floor. Whether that floor is achievable is the single most important rental input.',
  'Three or more comparable active and recently signed leases within a short radius, plus two management quotes expressed as a percentage of collected rent.',
  'Licensed property managers; public listing data; HUD small-area fair market rents as a floor check only','One week','hud','Ranking-changing'),
 ('D11','2','Will the solar interconnection still produce a credit, and under which tariff?',
  'A credit today is a function of the interconnection date and the applicable tariff. A future true-up, fixed charge or export rate change can turn a small credit into a cost.',
  'The interconnection agreement, the annual true-up statement, and the current tariff sheet.',
  'PG&E; the system owner’s records','Days to weeks','solar','Cost-changing'),
 ('D12','2','What repairs, replacements and capital items are likely in the next ten years?',
  'Roof, foundation, sewer line, electrical panel and seismic retrofit are lumpy costs that a percentage-of-value maintenance assumption cannot capture.',
  'A professional inspection, plus a disclosed list of past permits and any retrofit records. Ask for a reserve study if available.',
  'Licensed inspector; permit records at the city','Two to four weeks','rental','Cost-changing'),
 ('D13','2','What are the recipients’ own income, filing status and other income sources?',
  'Capital-gain rates, passive-loss limits, net investment income tax and bracket effects are personal. A flat rate is a teaching assumption, not a tax computation.',
  'Prior-year returns and a scenario prepared by a CPA, not a public calculator.',
  'The recipients’ own CPA','One to two weeks','rental','Cost-changing'),
 ('D14','3','What is the family’s actual preference about living in the residence?',
  'Living there has real value that this model deliberately omits: imputed rent, proximity, continuity. A financial ranking can be correct and still be the wrong decision.',
  'A documented family discussion of needs, timeline and alternatives, written down before the numbers are shown.',
  'The family','Immediate, but must precede the decision','invest','Preference'),
 ('D15','3','What investment policy will govern the proceeds if the property is sold?',
  'A portfolio return assumption is doing enormous work in every result on this site. Without a written policy, the return is a guess dressed as a plan.',
  'A short written investment policy statement stating target allocation, risk tolerance, liquidity needs and rebalancing rule.',
  'The recipients, with an adviser if desired','One to two weeks','fdic','Preference'),
 ('D16','3','Which specific bills are moving, and what would each do?',
  'Proposed law is not law. A bill that changes family-home transfer rules or repeals the federal estate tax changes the answer, but only once enacted.',
  'The official status page for each bill, checked before the decision, not months earlier.',
  'Congress.gov and the California Legislature, via the links in the register','Ongoing; a few minutes each','hr1301','Watchlist'),
]
DISCOVERY_PRIORITY={
 '1':'<span class="tag">P1</span> Blocks the decision. A different answer can reverse the ranking.',
 '2':'<span class="tag">P2</span> Changes a cost materially but is unlikely to reverse the ranking alone.',
 '3':'<span class="tag">P3</span> Preference, policy or watchlist. Necessary for a real decision, not for the arithmetic.'
}
body+='<div class="callout"><strong>This section exists to close the gap between a model and a decision.</strong> The comparison page is arithmetic on invented inputs. A real decision needs the facts below. For each one, this register states the question, why the answer can change the outcome, the specific document or source that answers it, who physically holds that document, and how long it usually takes. <strong>Do not enter any answer on this site.</strong> Keep the completed register offline.</div>'
body+=section('How to read the priority column',table(['Priority','Meaning','How to treat it','Official framework'],[
 ('P1','Blocks the decision. A different answer can reverse the ranking.','Resolve before comparing strategies seriously. Eight items.',source('notice')),
 ('P2','Changes a cost materially but is unlikely to reverse the ranking alone.','Resolve before committing capital or signing anything. Six items.',source('prop13')),
 ('P3','Preference, policy or watchlist. Necessary for a real decision, not for the arithmetic.','Resolve as part of the decision, not before the analysis. Three items.',source('invest')),
 ]))
rows=[]
for (i,p,q,why,doc,who,lead,link,gate) in DISCOVERY:
    rows.append((DISCOVERY_PRIORITY[p],'<strong id="'+i+'">'+q+'</strong>',why,doc,who,lead,source(link),gate))
body+=section('Discovery register',table(['Priority','Question','Why it blocks the decision','Document or source that answers it','Who holds it','Typical lead time','Official framework','Gate'],rows))
body+=section('The four facts that decide the ranking','''<p>Most of the register above improves accuracy. Four items can change which strategy wins, and they should be resolved in this order.</p>''')
body+=section('Order of resolution','<div class="grid two">'+''.join(
 '<div class="card"><div class="eyebrow">Step %d</div><h3>%s</h3><p class="muted">%s</p></div>'%(n,t,d)
 for n,t,d in [
  (1,'Does the trust permit a sale?','D01 and D02. If the trustee cannot or must not sell, the rest of the comparison is academic.'),
  (2,'Is there a basis step-up?','D03. An unadjusted basis turns an immediate sale from a low-tax event into a large one, which can lose the sale its first place.'),
  (3,'Is family-home relief available?','D04. Without occupancy, the assessed base resets to market value; on the invented example that raises the first-year property tax by about half.'),
  (4,'Is the estate over the filing threshold?','D05. If it is, estate tax and liquidity become constraints that no strategy comparison on this site models.')]
)+'</div>')
body+=section('What to do with the answers',table(['If the answer is','Then','Because','Official context'],[
 ('The trustee must sell','Stop comparing. The decision is about timing, price and net proceeds.','The comparison assumes a choice that does not exist.',source('notice')),
 ('No basis step-up','Re-run every sell scenario with a large taxable gain before ranking anything.','The sale strategy loses much of its advantage when the gain is taxed.',source('trustbasis')),
 ('No family-home relief','Model the residence at full market reassessment, which is what the comparison page’s rent column already does.','The live column understates tax if relief is unavailable.',source('prop19')),
 ('The estate exceeds the filing threshold','Add a liquidity review before choosing to keep the property.','Estate tax can force a sale regardless of preference.',source('estate')),
 ('The rent floor is not achievable','Treat renting as a cost-carrying choice, not an income strategy.','The break-even table on the real-conditions page shows the floor.',source('prop13')),
 ]))
page('questions','What must be answered first?','Two registers in one place: the answers official sources already give, and the facts that are still missing, with the exact document that resolves each one, who holds it, and how long it takes.',body)


suggestions=[
 ('S01','Critical','Contain the prior public-data exposure','Coordinate a history and pull-request cleanup; keep private case data out of public commits.','Protects household privacy; Pages exclusions alone do not remove public Git copies.','github'),
 ('S02','Critical','Confirm title, trust and basis','Review the deed, trust, beneficiaries and estate inclusion with counsel.','Can change who may sell and the taxable gain.','trustbasis'),
 ('S03','Critical','Build a private estate inventory','Include all interests, taxable gifts, debts and available portability.','Replaces an unsupported estate-tax headroom estimate.','estate'),
 ('S04','High','Obtain independent property and rental estimates','Use qualified appraisals and rent comparables, not public inputs or HUD alone.','Changes values and expected rental income.','hud'),
 ('S05','High','Get insurance and earthquake quotes','Compare coverage limits, occupancy, exclusions and deductibles for each use.','Replaces an unverified premium and makes tail exposure visible.','cdi'),
 ('S06','High','Validate Proposition 19 eligibility','Confirm transferor residence, recipient relationship, move-in timing and claim deadlines.','Determines if a partial assessment exclusion applies.','prop19'),
 ('S07','High','Model depreciation and recapture','Use private land/building allocation and adviser-prepared tax assumptions.','Rental after-tax results may change materially.','rental'),
 ('S08','High','Verify B’s leases and local rules','Review covered status, notices, actual collection and expenses.','Preserves existing rental context without assuming permitted increases.','sfRent'),
 ('S09','Medium','Use actual utility and solar terms','Match water provider, annual true-up and interconnection tariff.','Improves operating-cost estimates and reveals tariff changes.','solar'),
 ('S10','Medium','Create a documented investing policy','Compare insured deposits, Treasuries and diversified investments for risk and liquidity.','Makes portfolio return and downside assumptions explicit.','invest'),
 ('S11','Medium','Run tax-aware sensitivities','Test different gain rates, holding periods, rent, home growth and exit costs.','Shows where the financial ranking flips.','basis'),
 ('S12','Medium','Review extreme scenarios annually','Repeat inflation, rate, housing crash, market crash and disaster paths.','Avoids treating constant growth as a prediction.','usgs'),
 ('S13','Medium','Track proposed legislation','Recheck federal, state and local watchlists before decisions.','Prevents treating proposed law as current law.','hr1301'),
 ('S14','Low','Improve dashboard explanations','Add a clear status and methodology to every future table and retain source links.','Helps separate estimates, legal rules and unknown facts.','boe'),
 ('S15','Low','Independent model review','Have a qualified adviser review assumptions and compare outcomes with a separate calculation.','Reduces arithmetic, basis and tax-allocation risk.','estate'),
('S16','Critical','Owner decision: scrub pre-rounding history','Plan a history rewrite across all refs (for example git-filter-repo, then a force-push by a repository administrator), ask GitHub Support to purge cached views, and ask forks and clones to be deleted. Not run in this review: it overwrites shared branches and cannot reach copies outside GitHub.','Only a rewrite removes exact figures from Git objects; a Pages exclusion or a later commit does not.','github'),
('S17','Critical','Owner decision: remove legacy household files from the tree','Remove, in a reviewed pull request, the older root pages, the dashboard and docs folders, and the research and site data files that still hold household figures. Removal from the tree does not remove history (see S16).','Stops current readers from seeing household figures on main.','github'),
('S18','High','Keep household figures out of the public analysis (confirm)','Keep the current rule: the owner’s figures are analysed only in a git-ignored private folder, and the public site shows labelled examples. Publishing rounded figures needs an explicit owner decision.','Protects the privacy priority the owner set.','github'),
('S19','High','Add an imputed-rent input for living paths','Living paths currently credit no rent avoided. Add an input for the rent the owner would otherwise pay, from comparable leases or an official benchmark, and show the break-even beside it.','Living beats selling only when avoided rent passes a break-even; without the input the comparison is one-sided.','hud'),
('S20','High','Switch on the primary-residence exclusion for living-then-sell paths','The engine now has an optional exclusion, default zero so published figures are unchanged. After owner review, set the default, regenerate the examples and re-run the reference test.','Living-then-sell paths are otherwise taxed on the full gain, which overstates tax.','irs701'),
('S21','High','Model Prop H with its official terms','If Property B costs are shown over time, apply the FY 2027–28 schedule, the inflation adjustment from FY 2028–29 and the end after 30 June 2042, unless the measure is renewed.','A flat amount understates later years and ignores the sunset.','sfMuni'),
('S22','Medium','Replace maintenance-as-a-percentage with cost inputs','Maintenance is now a share of market value, which rises with the house and can overstate upkeep on a high-value home. Use contractor quotes and an age-based schedule.','Maintenance is a large line over long horizons; its driver should be a cost, not a price.','rental'),
('S23','Medium','Carry the Proposition 19 allowance forward','Use each BOE letter after 15 February 2027 rather than holding the current amount flat.','The allowance is re-set every other February; a flat figure is a modeling limit.','allowance'),
('S24','Medium','Check the San Francisco tax composition on the bill','Read the secured tax bill and separate the base 1% levy from bonds and direct assessments before modeling Property B.','A tax-to-assessed ratio above the base levy needs an explanation before it is used.','sfTax'),
]
options='<option value="">Not decided</option><option value="consider">Consider</option><option value="defer">Defer</option><option value="decline">Decline</option>'
rows=[(i,priority,title,action,reason,source(src),f'<select data-suggestion="{i}" aria-label="Choice for {i}">{options}</select>') for i,priority,title,action,reason,src in suggestions]
body='<div class="callout warning"><strong>Review before implementation.</strong> These are proposals. Marking a choice stores only the status in this browser; it does not approve work, transmit information, modify the model or implement a change. No personal answers should be entered here.</div>'
body+=section('Suggested paths',table(['Path','What it prioritizes','Trade-off','Reference'],[
 ('Privacy first','Contain old exposure, then keep case-specific work private.','Protects privacy but cannot erase copies already outside control.',source('github')),
 ('Decision first','Verify trust, basis, estate, assessment, rents and insurance with professionals.','Requires private documents and independent quotes; timeline varies.',source('estate')),
 ('Risk first','Run variable inflation, market and disaster paths with explicit exclusions.','Illustrations show sensitivity, not probabilities or forecasts.',source('invest')),
 ('Presentation first','Improve navigation, notes, source checks and accessible comparison tables.','Clarity alone cannot verify unknown inputs.',source('boe')),
 ]))
body+='<div class="control" style="max-width:420px"><label for="chosen-path">Optional path to review (browser only)</label><select id="chosen-path" data-suggestion="PATH"><option value="">Not decided</option><option value="privacy">Privacy first</option><option value="decision">Decision first</option><option value="risk">Risk first</option><option value="presentation">Presentation first</option></select></div>'
body+=section('Suggestions register',table(['ID','Priority','Suggestion','Proposed action','Decision benefit','Reference','Your choice'],rows)+'<p id="save-status" class="tiny" aria-live="polite">Selections, if made, stay in this browser only.</p><button class="button secondary" id="clear-selections" type="button">Clear selections</button>')
body+=AP.suggestions_block(CTX)
page('suggestions','Suggestions to review, not automatic changes.','Consider the options, record a local choice if useful, and choose a path before implementing discretionary improvements.',body)

body=section('Unresolved items',table(['Priority','Issue','Current treatment','Next step','Reference'],[
 ('Critical','Public repository and history exposure','The current public guide omits household-specific financial records, but earlier revisions, public branches, pull requests and external caches can still contain them. Excluding files from Pages does not make the public repository private.','Coordinate a repository-history and PR-ref cleanup with all collaborators; contact GitHub Support where appropriate. No guarantee exists for independent copies.',source('github')),
 ('Critical','Exact household figures remain in legacy files at the branch tip','Legacy files outside the Pages artifact (root pages, docs, pages, dashboard, site, research and integration folders) still contain household-specific figures and ZIP codes in the public repository. Pages does not serve them, but GitHub does show them. Removing them from the current tree does not change Git history.','Owner decision: remove those figures from the current tree in a separate change, then decide on the history cleanup in N02. Until then, treat the repository as public.',source('github')),
 ('High','Household figures and actual property bills','Not officially verified and not published in this guide. The supplied B occupancy description is a planning premise; all numerical property examples are fictional.','Verify bills and appraisals privately; do not add them to the public repository.',source('county')),
 ('High','Actual estate, assets and prior gifts','Unknown; real estate-tax filing and liability headroom are blank.','Prepare a confidential complete inventory with tax counsel.',source('estate')),
 ('High','Insurance and solar','No actual binding premiums, deductible, coverage, tariff or annual true-up are established.','Obtain coverage quotes and utility records privately.',source('cdi')),
 ('High','SF Proposition H and other direct charges','SFMTA publishes the FY 2027–28 schedule and states the measure was approved on 3 November 2026; the election office still labels its own results preliminary. The amount for B is not computable from public information, and the measure is not included in the synthetic B operating table.','Confirm the parcel type and taxable building area privately, check certification after the election deadline, and model the tax before relying on any long-run B figure.',source('sfMuni')+' · '+source('sfElection')),
 ('High','Basis and Proposition 19 eligibility','No trust document, title or eligibility finding was verified.','Obtain written advice from counsel and the assessor.',source('trustbasis')),
 ('High','Scenario output is not a personalized recommendation','Invented model data, flat tax assumptions and omitted depreciation/recapture, financing, estate tax and personal housing value can alter results.','Run a taxpayer-specific comparison privately before acting.',source('rental')),
 ('Medium','Older research contained imprecise estate filing language','The filing test uses gross estate and adjusted taxable gifts, while deductions concern taxable estate and tax.','Use the IRS filing test and a professional, not a simplified headroom subtraction.',source('estate')),
 ('Medium','Future laws, exemption amounts and returns','Future values are assumptions; proposals are not law.','Recheck official law and prices near the decision date.',source('estate27')),
 ('Medium','Local provider and quote availability','The exact water provider and insurance product cannot be determined from a generic area. An owner-occupied multiunit property may have more than one policy option.','Verify address privately and ask insurers for product eligibility.',source('water')),
 ('Medium','Two official pages describe the Proposition 19 adjustment cadence differently','The Santa Clara County Assessor page says the one-million-dollar allowance is adjusted “annually beginning in 2023”. The Board of Equalization says the amount is adjusted “every other February 16”, and Letter to Assessors 2025/009 applied one step for the February 2025–February 2027 period. The guide follows the Board.','Use the Board’s Letter to Assessors for the amount and its date; the assessor’s page is a local summary and should not be read as the governing rule.',source('boe')+' · '+source('county')),
 ('Medium','Form 1041 due date not confirmed from IRS text','The IRS About Form 1041 page was opened, but the due-date text was not on it. Secondary sites give April 15 for calendar-year estates and trusts; the guide does not use that date.','Re-read the Form 1041 instructions and the statute on the IRS site, then enter the date if confirmed.',source('irs1041about')),
 ('Medium','Proposition 19 claim periods: re-read 15 Nov 2026','The BOE fact sheet (Publication 801) states that the transferee must live in the home as a primary residence within one year, that the homeowners’ exemption claim (BOE-266 or BOE-261-G) within one year starts the exclusion on the transfer date, and that Form BOE-19-P is due within three years of transfer and before any transfer to a third party. A late exemption claim starts the exclusion in the year it is filed.','Confirm the dates with counsel before any filing. The Timeline now lists them.',source('prop19')),
 ('Medium','Santa Clara County installment dates not read from the county site','The timeline uses the state dates in RTC §2617 and §2618. The county page was not re-read, and secondary sites were not used as the source.','Confirm the county’s stated due dates on its official page.',source('county')),
 ('Medium','Federal exclusion ledger label conflict','The figures ledger lists $15,000,000 under two labels: a 2026 basic exclusion and a 2026 filing threshold. The IRS page supports $15,000,000 as the filing threshold, not as the basic exclusion amount.','Re-read the Form 706 instructions basic-exclusion table and correct the ledger label before any reuse.',source('irs706i')),
 ('Medium','Form 706 basic exclusion table and California estate-tax status','Neither was verified in this review. The guide states the federal filing threshold only.','Read the Form 706 instructions table and an official California source before stating either.',source('estate')),
 ('Medium','Reinvestment risk: no verified definition','The term appears as a label on the Black swans page, but no official definition has been captured.','Find an official definition before adding it to the glossary.',source('dca')),
 ('Medium','Crash shapes are illustrative, not index history','The 1929 and 2008 paths on the Black swans page are smooth templates built from the Federal Reserve’s peak-to-trough declines. The post-trough growth rates are assumptions.','Compare the templates with official index history before relying on exact figures.',source('fed1929')),
 ('Medium','Early-crash path and cycle row are assumptions','The first-three-years path on the Black swans page and the 10-year cycle shape are assumptions. The CPI series shows annual rates, not a cycle.','Keep the path labelled as illustrative; do not cite CPI as evidence of a cycle.',source('cpiHistory')),
 ('Critical','Legacy household files and older Git history','Older root pages, the dashboard and docs folders, and research and site data files on main still contain household figures, and older commits contain exact figures. Pages does not serve these files, but the repository is public, so copies may already exist.','Owner decision: file removal (S17) and history rewrite with GitHub Support (S16). No history rewrite was run in this review, because it overwrites shared branches.',source('github')),
 ('High','Owner-supplied tables: arithmetic check','Every printed year-over-year percentage was recomputed. Most match within rounding. Two printed assessment changes differ from the arithmetic by a few hundredths of a point; one projected value is a derived figure, not an assessor roll value; one tax-to-assessed ratio is higher than the base levy and is not explained by the tables; two early rows have no prior year to test. Figures stay private.','Compare against the assessor roll and actual tax bills before using any owner table in a filing decision (S24).',source('county')+' · '+source('sfTax')),
 ('High','Primary-residence exclusion is not in the public calculator','The public calculator taxes living-then-sell paths on the full gain. The engine now has an optional exclusion, default zero, so published figures are unchanged.','Owner decision on the default (S20).',source('irs701')),
 ('High','Living paths credit no avoided rent','The public engine has no rent input for the living path, so living carries no imputed rent, which biases the comparison toward selling. The break-even rent is the decision figure. No official rent for the Cupertino ZIP code was captured in this review.','Obtain comparable rents, then add the input (S19).',source('hud')),
 ('High','Prop H is held flat in the public engine','The guide reports the official FY 2027–28 schedule, but the engine does not index it and does not model the 30 June 2042 end.','Apply the official terms before publishing any Property B cost series (S21).',source('sfMuni')),
 ('Medium','Proposition 19 allowance is held flat in the engine','The current allowance covers transfers through 15 February 2027. Later transfers use a figure not yet published.','Use the BOE letter in force on the transfer date (S23).',source('allowance')),
 ('Medium','Yield values carry different dates','The model uses 12 November 2026 values (3-month 4.32%, 2-year 4.86%, FRED). The guide text quotes the 13 November Treasury values (4.32% and 4.88%). Both match their official source for their own date.','Label each yield with its date in one place (no value change).',source('treasury')+' · '+source('dgs2')),
 ('Medium','Estate exclusion after 2027 is a projection','The engine indexes the 2027 basic exclusion with inflation for later deaths. That is an assumption, not law.','Recheck the IRS figure for the year of death.',source('estate27')),
 ('Medium','Maintenance, insurance, water and electricity are unverified inputs','Maintenance is a percentage of value in the engine. Insurance premiums for both properties are owner estimates; no official premium data for either ZIP code was found. Water and electricity are owner ranges, not matched to tariffs.','Obtain insurance quotes and utility bills (S22, and the insurance and utility rows above).',source('cdi')+' · '+source('water')),
 ('Low','Model conventions','The sale year includes one year of holding costs; break-evens are in inheritance-year dollars; house growth uses the midpoint of two official FHFA series; the equity return is an assumption with no official forecast.','Read the assumptions before reusing any figure.',source('hpi')),
 ]))
body+='<div class="callout review"><strong>Important:</strong> A passing privacy scan cannot prove anonymity or clean previously published history. GitHub warns that commits may remain reachable through pull requests, caches, forks and clones. Do not put personal information, private links or financial documents in this repository.</div>'
body+=AP.review_block(CTX)
page('review','Flagged for review.','Unknown facts, modeling limitations and the remaining public-history privacy incident are visible here; none should be mistaken for a verified value.',body)

sources=[
 ('Property tax','BOE Proposition 19','Qualifying transfers, value cap and timing.','boe'),('Property tax','BOE fact sheet','Move-in, exemption and claim filing details.','prop19'),('Property tax','BOE LTA 2025/009','Exact 2025–2027 allowance and adjustment cadence.','allowance'),('Property tax','BOE LTA 2025/023','Prop 13 assessment and rate mechanics.','prop13'),('Property tax','Santa Clara County Assessor','Local parent-child claim guidance.','county'),
 ('Federal tax','IRS estate tax','Gross estate, filing threshold and portability.','estate'),('Federal tax','IRS 2027 adjustments','2026 and 2027 exclusion amounts.','estate27'),('Federal tax','IRS inherited property','General inherited basis rule.','basis'),('Federal tax','IRS Rev. Rul. 2023-2','Specific trust and estate-inclusion basis example.','trustbasis'),('Federal tax','IRS home sales','Ownership/use requirements and possible exclusion.','residence'),('Federal tax','IRS rental property','Rental income, depreciation and sale rules.','rental'),('Federal tax','IRS retirement beneficiaries','Inherited account distributions and rules.','ira'),('California tax','State Controller','State estate tax-return requirements.','ftb'),
 ('Administration','Probate Code §16061.7','When trustee notification is required.','notice'),('Administration','Revenue and Taxation Code §480','Death-related ownership reporting.','ownership'),('Local context','SF Rent Board','Current allowable increases and proposal notice.','sfRent'),('Local context','SF Treasurer','2026–27 secured property tax rate; direct charges may be additional.','sfTax'),('Local context','SFMTA','Proposition H parcel-tax details.','sfMuni'),('Local context','SF Department of Elections','Preliminary election results.','sfElection'),('Local context','SFPUC','Water and sewer schedules.','sfWater'),('Local context','City of Cupertino','Water service systems.','water'),('Local context','PG&E','Solar billing plan and true-up.','solar'),('Local context','California Department of Insurance','Premium comparison surveys, not quotes.','cdi'),('Local context','CA Department of Insurance','Earthquake coverage and exclusions.','quake'),('Local context','HUD','Small-area fair market rents, not a property quote.','hud'),
 ('Observed series','BLS CPI-U via FRED (CPIAUCNS)','Annual-average inflation record used on the real-conditions page.','cpiHistory'),('Observed series','Freddie Mac PMMS','Observed 30-year fixed mortgage benchmark.','pmms'),('Observed series','BOE LTA 2026/002','2026-27 Prop 13 inflation factor and the 51-year factor history.','prop13factor'),
 ('Risk','CBO','2026–2036 economic baseline; not a 50-year property forecast.','cbo'),('Risk','BLS','Recorded 2022 CPI and electricity inflation.','bls'),('Risk','FHFA','House-price index data and methods.','hpi'),('Risk','USGS','Bay Area earthquake outlook 2014–2043.','usgs'),('Risk','SEC Investor.gov','Diversification and investing risks.','invest'),('Risk','FDIC','Deposit insurance categories and limits.','fdic'),('Investment','TreasuryDirect bills','Bill maturities, redemption and federal/state/local tax treatment.','treasuryBills'),('Investment','TreasuryDirect notes','2-year notes and marketable security terms.','treasuryNotes'),('Investment','TreasuryDirect pricing','Market-price variation with yield and interest rate.','treasuryPricing'),('Law watch','Congress.gov','Federal H.R. 1301 bill status.','hr1301'),('Law watch','California Legislature','SB 284 status and history.','sb284'),('Privacy','GitHub documentation','Removal, PR references and copies.','github'),
]
body='<div class="callout">Sources explain law, official benchmarks or decision context. They do not verify a household’s private records or this site’s fictional assumptions. Every link in the register below was re-opened and the wording the guide attributes to it was checked on 13 November 2026, except the rows added on 14 November 2026, which were opened on that date; recheck the underlying documents and date-specific details before relying on them.</div>'
sources+=AP.SOURCES_ADD
body+=section('Source register',table(['Category','Agency or source','What it supports','Official link'],[(a,b,c,source(d)) for a,b,c,d in sources]))
body+=section('How each official figure was checked',table(['Check','What it does','What it does not do','Official context'],[
 ('Machine-readable ledger','Every official rule figure the guide publishes is recorded in a public ledger with its source URL, the exact published value, the form shown on the site, and the date it was re-opened.','It does not prove the value is still current on the day you read it, and it does not verify any household figure.',source('estate27')),
 ('Build gate','The build fails if a seven-figure amount appears on a published page without a ledger record, or if a ledger record is marked verified without an official https source.','It cannot detect a value that was verified once and has since changed at the agency.',source('prop19')),
 ('Rounding disclosure','Where a published amount is rounded to the nearest $10, the page says so and the ledger keeps the exact official value so a reader can match it.','Rounding does not anonymize: a multi-year series can be matched even after rounding.',source('prop13')),
 ('Deliberately unverified','An item that could not be confirmed at an official source is left blank on the page and recorded as unverified in the ledger.','It stays open until someone opens the official document and records it.',source('github')),
 ]))+'<p class="tiny">Last full re-read of official sources: 13 November 2026. The guide states a review date rather than promising currency. Laws, exemption amounts and local rates change.</p>'
body+=section('What is deliberately left blank',table(['Blank item','Why it is blank','Where to find the real value privately','Official context'],[
 ('Market value of either property','No appraisal has been published to this site, and publishing one would breach the privacy rule.','Independent appraisal and comparable sales, kept offline.',source('basis')),
 ('Actual property-tax bill and assessed value','Parcel-specific and household-specific.','The county secured tax bill for each parcel.',source('prop13')),
 ('Insurance premium and coverage','A quote is not a public document.','Binding quotes from licensed brokers, including or excluding earthquake.',source('cdieq')),
 ('Rent roll and lease terms','Private contracts.','Signed leases and the local rent board history.',source('sfRent')),
 ('Estate inventory and any estate-tax headroom','The whole estate is unknown.','A confidential inventory prepared with counsel.',source('estate')),
 ('Date-of-death value','An event that has not occurred.','A retrospective appraisal as of the actual date.',source('basis')),
 ])+'<p class="tiny">Each blank is recorded as unverified rather than filled with an estimate. The build fails if a seven-figure official amount appears without a ledger record, and the ledger itself records one item as explicitly unverified rather than guessing.</p>','05 / blanks')
AP.write_js(ROOT)
page('paths','Paths, including mixed ones.','Three pure choices and three mixed paths, compared across four stress tests with break-even points. Example inputs only.',AP.paths_body(CTX))
page('whatif','What-if controls.','Change the stress test, horizon, parking period, parked-cash yield or equity return and see the effect on each path.',AP.whatif_body(CTX),['guide/data/whatif-page.js'])
page('sources','Sources and verification.','Direct links to official agencies and primary materials, organized by subject for manual review.',body)

body='''<div class="callout warning"><strong>Fictional values, not your household’s figures.</strong> This example was invented for a public site. Its numerical results cannot establish the best personal plan. Official links support the rules or risk context, not the synthetic inputs or projections.</div>'''
body+=section('Set the example horizon','''<div class="controls"><div class="control"><label for="transfer-year">Illustrative transfer year</label><select id="transfer-year"><option>2040</option><option selected>2045</option><option>2050</option></select></div><div class="control"><label for="hold-years">Years after transfer</label><select id="hold-years"><option>10</option><option>20</option><option>30</option><option>50</option></select></div><div class="control"><label for="home-growth">Illustrative annual home-price growth</label><select id="home-growth"><option value="0.02">2%</option><option selected value="0.035">3.5%</option><option value="0.05">5%</option></select></div><div class="control"><label for="portfolio-return">Illustrative annual portfolio return, net proxy</label><select id="portfolio-return"><option value="0.03">3%</option><option selected value="0.05">5%</option><option value="0.07">7%</option></select></div></div><p class="tiny">Only public, invented assumptions are changed. Nothing is uploaded or saved.</p>''')
body+=section('Example inputs and conventions','''<p>Property values, rents and operating costs here are fabricated. Each is a scenario assumption rather than a verified value.</p><div class="table-wrap"><table><thead><tr><th scope="col">Example assumption</th><th scope="col">Illustrative value</th><th scope="col">Why it matters</th><th scope="col">Official context only</th></tr></thead><tbody id="assumptions"></tbody></table></div>''')
body+=section('Compare equal endpoints','''<div id="winner" class="card highlight" aria-live="polite"></div><div class="table-wrap"><table><thead><tr><th scope="col">Strategy</th><th scope="col">Initial investable proceeds</th><th scope="col">First-year cash / portfolio change</th><th scope="col">Value at endpoint</th><th scope="col">Calculation / rule context</th></tr></thead><tbody id="comparison"></tbody></table></div><p class="tiny">The hold strategies include a hypothetical sale at the endpoint and assumed gain tax. Sale proceeds earn a constant after-tax return proxy; there is no additional portfolio liquidation tax. Retained-property cash flows are accumulated using the same proxy. Sell’s first-year figure is a portfolio-value change proxy, not spendable distributions. Living costs are treated as funded externally and compounded. No estate-tax allocation or value of housing services is included. These omissions can change the ordering.</p>''')
body+=section('Inherited property: annual illustration','''<p>For each year through 2076, the table shows fictional market value, the model’s pre-transfer assessment if not yet transferred, and the two modeled post-transfer assessments. “Live” assumes the family-home exclusion applies; “rent” assumes full reassessment. Full-year operating cost includes property tax, water, insurance and maintenance, before rental income; it is not a bill and ignores proration or supplemental taxes.</p><div class="table-wrap"><table><thead><tr><th scope="col">Year</th><th scope="col">A market</th><th scope="col">A assessment · applicable</th><th scope="col">A tax · live / rent</th><th scope="col">A annual costs · live / rent</th><th scope="col">Context, not verification</th></tr></thead><tbody id="years-a"></tbody></table></div>''')
body+=section('Already-owned property: annual illustration','''<p>Property B is already owned and is not transferred in this comparison. On the supplied planning premise, the two rents continue whether or not the owner occupies the available third unit, so B is not added to the A-only comparison. This fictional operating table is separate. NOI subtracts vacancy, management, property tax, water, electricity, insurance, upkeep and a scenario fee, but excludes income tax, financing and direct tax charges.</p><div class="table-wrap"><table><thead><tr><th scope="col">Year</th><th scope="col">B market / assessment</th><th scope="col">B ad valorem tax</th><th scope="col">Gross rent</th><th scope="col">Water / electric / insurance / upkeep</th><th scope="col">NOI after reserves</th><th scope="col">Context, not verification</th></tr></thead><tbody id="years-b"></tbody></table></div>''')
body+=section('Limitations that can change the answer',table(['Omission or assumption','Effect','Official context'],[
 ('Estate tax','No estate-tax payment, allocation, liquidity need or timing is modeled because the estate is unknown.',source('estate')),
 ('Rental tax','No building/land allocation, depreciation, recapture, passive-loss rules or taxpayer-specific brackets; compare with a CPA.',source('rental')),
 ('Income-tax basis','Uses date-of-death value as basis. Trust or other exceptions can make that wrong.',source('trustbasis')),
 ('Property tax','Rate and future allowance are scenarios. Decline in value is only a simplified market-value cap; no direct charges, supplemental bills, appeals or new construction are modeled.',source('prop19')),
 ('Insurance and utilities','Flat annual inflation is not an insurance quote or rate forecast. Solar credit is set to zero solely in this invented case.',source('cdi')),
 ('Housing choice','No value for occupying A or any income from changing B’s occupancy; the heir’s preferences are missing.',source('invest')),
 ]))
page('decision','Compare the options, not just a number.','A transparent live-versus-rent-versus-sell example, with year-by-year property and operating-cost tables.',body,['guide/data/model.js','guide/data/decision-page.js'])

body='''<div class="callout warning"><strong>Not forecasts or probabilities.</strong> These fictional paths apply to a fictional 2045 transfer and end in 2095. They illustrate sensitivity and sequence risk; they do not predict returns, insurance losses or home values.</div>'''
body+=section('Observed context',table(['Evidence','Why it matters','Official source'],[
 ('Inflation in 2022','BLS reported 6.5% CPI-U inflation and 14.3% electricity inflation over the 12 months ending December 2022. A single 3% cost assumption can miss such divergence.',source('bls')),
 ('Official macro baseline','CBO’s February 2026 outlook projects PCE inflation moving toward roughly 2% in 2030. It covers 2026–2036 and is not a 50-year housing or portfolio forecast.',source('cbo')),
 ('Home-price cycles','FHFA publishes house-price indexes; historical regional changes and future individual-house values are not the same.',source('hpi')),
 ('Earthquake','USGS estimated a 72% chance of at least one magnitude 6.7 or larger Bay Area earthquake over 2014–2043. That is not a probability of a particular property loss.',source('usgs')),
 ('Investment risk','Diversification can reduce certain risks but neither guarantees returns nor prevents loss.',source('invest')),
 ]))
body+=section('Five paths',table(['Path','Synthetic shocks','Context only'],[
 ('Changing cycle (illustrative)','An assumed 10-year pattern in home, portfolio and inflation rates, including a down year. The annual CPI rates below are official; the cycle shape is not.',source('cpiHistory')),
 ('Early deep crash','First three years: home −25%, −10%, +4%; portfolio −35%, −10%, +12%; rent falls 5% annually and vacancy is 20%. This is a stylized stress analogue, not a literal reconstruction of 1929 or 2008.',source('invest')),
 ('Late crash','The same three-year shock occurs in the last three years. Underlying returns are aligned with the early case so the two contain the same set of annual rates, though cash-flow timing differs.',source('invest')),
 ('Stagflation and insurance','First five years: home 0%, portfolio 1%, inflation 8%, rent growth 2%; insurance doubles at the start.',source('bls')),
 ('Disaster','Year ten: home −15%, vacancy 100%, a fictional $250,000 unreimbursed repair and a permanently doubled premium. No insurance reimbursement or immediate one-time price rebound is assumed.',source('usgs')),
 ]))
body+=section('Black-swan sale-proceeds path: phase into stocks','''<p><strong>Question:</strong> if a fictional heir sells at transfer, does holding net proceeds in a short U.S. Treasury ladder for 24 or 36 months, then moving into stocks over 12 months, reduce the damage from an early crash compared with investing immediately? Choose a waiting period and a flat annual Treasury-return proxy. The model runs the choice through all five paths; the early and late crash comparisons are highlighted.</p><div class="controls"><label for="phase-months">Treasury parking period<select id="phase-months"><option value="24">24 months</option><option value="36">36 months</option></select></label><label for="treasury-proxy">Illustrative annual Treasury return<select id="treasury-proxy"><option value="0.01">1% proxy</option><option value="0.03" selected>3% proxy</option><option value="0.05">5% proxy</option></select></label></div><div class="callout warning"><strong>Reinvestment and duration risk belong beside the headline.</strong> Treasury bills mature in 4–52 weeks (<a href="https://www.treasurydirect.gov/marketable-securities/treasury-bills/" rel="noopener noreferrer">TreasuryDirect bills ↗</a>); Treasury notes include 2-year securities (<a href="https://www.treasurydirect.gov/marketable-securities/treasury-notes/" rel="noopener noreferrer">TreasuryDirect notes ↗</a>). A ladder therefore returns principal at different dates, and maturing proceeds must be reinvested at then-available yields. The 1%, 3% and 5% rates here are invented flat sensitivities, not current yields or forecasts; the model does not simulate individual maturities, taxes, fees, changing rates, market-price losses on early sale, or inflation surprises. A fixed-income position can lose purchasing power, and its market value can fluctuate if sold before maturity (<a href="https://www.treasurydirect.gov/marketable-securities/understanding-pricing/" rel="noopener noreferrer">TreasuryDirect pricing ↗</a>). Treasury interest is federally taxable and generally exempt from state and local income taxes (<a href="https://www.treasurydirect.gov/marketable-securities/treasury-bills/" rel="noopener noreferrer">TreasuryDirect tax treatment ↗</a>); obtain tax advice for actual holdings.</div><p>The phase-in is an explicit simplifying assumption: after the selected wait, half of the portfolio earns that year’s scenario stock return and half earns the Treasury proxy for one year; it is fully in the stock proxy the following year. This is annual arithmetic, not a quarterly trading schedule. No probabilities are assigned. The stress path is not a historical replay of 1929 or 2008.</p><div class="table-wrap"><table><thead><tr><th scope="col">Path / selected plan</th><th scope="col">Immediate stock investment at endpoint · nominal / real</th><th scope="col">Treasury parking + phase-in · nominal / real</th><th scope="col">Phased minus immediate · nominal / real</th><th scope="col">Source context</th></tr></thead><tbody id="phase-summary"></tbody></table></div><h3>Crash windows: early-entry years 1–6 and late-entry years 45–50</h3><div class="table-wrap"><table><thead><tr><th scope="col">Path / year</th><th scope="col">Scenario stock return</th><th scope="col">Treasury proxy</th><th scope="col">Stock exposure in phase path</th><th scope="col">Immediate · nominal</th><th scope="col">Phased · nominal</th><th scope="col">Difference</th><th scope="col">Source context</th></tr></thead><tbody id="phase-years"></tbody></table></div>''')
body+=section('Same-endpoint property strategies','''<p>The starting 2045 property value, rent, costs, sale fee and tax rates come from the <a href="decision.html">default fictional example</a>, not the comparison page’s current control selections. After 2045, rent grows 2.5% and vacancy is 5% except during listed shocks. Water and insurance follow each path’s inflation, plus the listed premium shocks; maintenance follows modeled home value. B is treated the same across choices and is not included. No estate-tax payment or financing is modeled.</p><p>Nominal amounts are rounded to $10. Real figures are divided by cumulative inflation and expressed in 2045 dollars. Living results omit the value of housing services; negative reserves assume externally funded costs.</p><div class="table-wrap"><table><thead><tr><th scope="col">Scenario</th><th scope="col">Sell · nominal / real</th><th scope="col">Rent · nominal / real</th><th scope="col">Live · nominal / real</th><th scope="col">Context only</th></tr></thead><tbody id="stress-results"></tbody></table></div>''')
body+=PHASED_SECTION_HTML

body+=section('Audit every year','''<p>Expand a path to inspect all 50 annual rates and outputs. The model caps annual factor growth at 2% and uses the lesser of market value and factored base as a simplified decline-in-value proxy; actual lien dates, assessment appeals, new construction and supplemental bills are not modeled. The disaster repair is charged to both property-holding strategies. Each portfolio rate is a hypothetical net proxy with no separate liquidation tax. Income tax on positive rental cash is a flat scenario; depreciation and recapture are omitted.</p><div id="stress-years"></div>''')
page('stress','A straight line is not a forecast.','Five variable 50-year scenarios put inflation, investment returns, housing cycles and an uninsured disaster into the same comparison.',body,['guide/data/model.js','guide/data/stress.js','guide/data/stress-page.js'])

# ---------------------------------------------------------------- real conditions
body='<div class="callout warning"><strong>Observed history, stated as history.</strong> Every figure on this page is a published official statistic, or a statistic this site computed from a published series with the arithmetic shown. None of it is a forecast. The scenario bands further down are invented planning assumptions, clearly labelled, and they are not predictions.</div>'
body+=section('Why a straight line is the wrong planning tool',table(['What the record shows','Evidence','Why it changes a decision','Source'],[
 ('Inflation is not a constant','Over the 35 complete years from 1991 to 2025, annual CPI-U change averaged 2.62%, ranged from −0.36% to 8.00%, and exceeded 3% in 10 of those years.','A single 3% cost assumption is reasonable in the middle and badly wrong at both ends. Costs that compound quietly for 24 years magnify that error.',source('cpiHistory')),
 ('Two recent years broke the pattern','CPI-U rose 4.70% in 2021, 8.00% in 2022 and 4.12% in 2023 as annual averages, after a decade mostly under 2%.','A planner who calibrates on 2010–2020 understates cost growth; one who calibrates on 2021–2023 overstates it. Both are extrapolation errors.',source('cpiHistory')),
 ('The tax base is capped, prices are not','Proposition 13 limits the annual adjustment to a property’s factored base year value to 2%. Across the 51 published assessment years from 1976-77 to 2026-27 the factor hit the full 2% cap in 40 years, was lower 11 times, and compounded at about 1.81% a year.','The assessed base and the market price diverge over time by design. Modeling them with the same growth rate is a structural error, not a rounding error.',source('prop13factor')),
 ('Official projections stop long before the horizon','CBO’s February 2026 baseline runs 2026 to 2036 and projects PCE inflation returning to roughly 2% around 2030.','A 2045 or 2050 transfer sits far outside any official projection. Anything shown for those years is a scenario, whoever produces it.',source('cbo')),
 ('Regional hazard is priced separately','USGS estimated a 72% chance of at least one magnitude 6.7 or greater earthquake somewhere in the Bay region between 2014 and 2043.','Standard homeowners policies generally exclude earthquake damage, so an uninsured loss is a genuine balance-sheet event rather than a premium line.',source('usgs')),
 ('Borrowing is not cheap','Freddie Mac’s survey averaged 7.11% for a 30-year fixed rate as of 12 November 2026.','Any plan that assumes borrowing against a property to fund a repair or a purchase has to clear that hurdle. No borrowing is modeled here.',source('pmms')),
 ]))
rows=[]
for y,ch in [(1991,'4.24%'),(1995,'2.81%'),(2000,'3.38%'),(2005,'3.39%'),(2008,'3.84%'),(2009,'−0.36%'),(2010,'1.64%'),(2015,'0.12%'),(2020,'1.23%'),(2021,'4.70%'),(2022,'8.00%'),(2023,'4.12%'),(2024,'2.95%'),(2025,'2.63%')]:
    rows.append((str(y),ch,'Annual average, not seasonally adjusted, computed from the published series.',source('cpiHistory','Published CPI series')))
body+=section('The inflation record, selected years',table(['Year','Annual CPI-U change','Note','Source'],rows)+'<p class="tiny">Annual averages, not seasonally adjusted. Computed from the published series; 2026 is excluded because the year is incomplete. The years shown are chosen for range, not to support a trend claim. The full 35-year series is in the data file.</p>')
body+=section('Two rates that move differently',table(['Quantity','Long-run observed behavior','Official basis','Source'],[
 ('Market price of a home','Not published as a national constant. Regional indexes exist; a single parcel is not an index.','FHFA publishes house-price indexes; they are not a forecast for one house.',source('hpi')),
 ('Assessed value used for tax','Capped at 2% a year absent a reassessment event, and the assessor enrolls the lower of the factored base or market value.','BOE LTA 2026/002 and the Pub 800-10 information sheet.',source('prop13')),
 ('Effect on the decision','If market growth outruns the 2% assessed cap, an owner who keeps the protected base pays tax on a shrinking fraction of value. A sale resets that base for the buyer, not for this household.','This is the mechanical reason the live-versus-rent gap widens over time.',source('prop13cap')),
 ('Effect of a reassessment event','A transfer that does not qualify for relief resets the base to market value, which can multiply the tax bill in one year.','Prop 19 relief has occupancy, timing and filing conditions.',source('prop19')),
 ]))
body+=section('Scenario bands used on this site','<p>These five rates are planning assumptions. Three of them are invented bands; the 2% rate is the official statutory cap, used here as a scenario rather than as a price forecast. The table is generated from the data file so the rates cannot drift from the numbers used elsewhere.</p><div class="table-wrap"><table><thead><tr><th scope="col">Band</th><th scope="col">Assumed annual inflation</th><th scope="col">Price level after 24 years</th><th scope="col">Price level after 50 years</th><th scope="col">Status</th><th scope="col">Context only</th></tr></thead><tbody id="band-table"></tbody></table></div>')
body+=section('What compounding actually does to a cost','<p>The same four rates, applied to one unit of cost. The right-hand column is the part most planning documents omit: a nominal balance is not purchasing power. These are multipliers on an index, not dollar estimates.</p><div class="table-wrap"><table><thead><tr><th scope="col">Annual inflation</th><th scope="col">Cost multiplier after 24 years</th><th scope="col">Cost multiplier after 50 years</th><th scope="col">Purchasing power of 1,000,000 units after 24 years</th><th scope="col">Context only</th></tr></thead><tbody id="compound-table"></tbody></table></div>')
body+=section('The observation that most affects the ranking','<p>In the invented example on the comparison page, the rental strategy is <strong>cash-negative before income tax</strong> at the assumed growth rate. The property tax line alone, computed on a reassessed market value, is larger than the modeled operating margin. That is not a quirk of the arithmetic; it is what full reassessment does to a long-held California property at today’s price-to-rent ratio.</p><p>The table below finds the gross monthly rent the rental would need just to cover operating costs, before financing and income tax, expressed in today’s money so it can be compared with an actual rent roll. If the achievable rent is below that line, renting loses to selling for reasons that have nothing to do with investment returns.</p><div class="table-wrap"><table><thead><tr><th scope="col">Quantity, first full year after transfer</th><th scope="col">Invented example</th><th scope="col">What it means</th><th scope="col">Source</th></tr></thead><tbody id="breakeven-table"></tbody></table></div><p class="tiny">All values are from the invented teaching example and are rounded to $10. They are not a rent estimate for any property. The comparison is the point: the rent the model assumes against the rent the model’s own cost structure requires.</p>')
body+=section('Where the operating cost goes','<p>Shares below are computed from the invented example for its first full year after transfer and rounded to a whole percent, so they will not sum exactly to 100. The shape is what matters: property tax and upkeep dominate, and utilities are a minor line for this property type.</p><div class="table-wrap"><table><thead><tr><th scope="col">Component</th><th scope="col">Live strategy</th><th scope="col">Rent strategy</th><th scope="col">Rule or source</th></tr></thead><tbody id="cost-table"></tbody></table></div>')
body+=section('What this page cannot tell you',table(['Limit','Why','What would resolve it','Source'],[
 ('Whether prices or rents will rise','No official 25-year projection exists, and none is claimed here.','Local comparables and a documented investment policy, reviewed periodically.',source('cbo')),
 ('What this household would actually pay','The inputs are invented. A real bill depends on the parcel, the rate area and the reassessment outcome.','The county tax bill and an appraisal, kept private.',source('prop13')),
 ('Whether insurance is obtainable','Availability and price in an earthquake and wildfire state are not determined by a rate filing alone.','Binding quotes, and an explicit decision about earthquake coverage.',source('cdieq')),
 ('What the trust actually requires','A trust is a private document.','Counsel’s reading of the signed instrument.',source('trustbasis')),
 ('What future law will be','Bills in this space move every session.','Recheck the watchlist before acting.',source('hr1301')),
 ]))
page('conditions','The record, not a trend line.','The observed inflation and assessment record, the official projection horizon, and the scenario bands this site uses, kept separate from each other.',body,['guide/data/conditions.js','guide/data/model.js','guide/data/breakeven.js','guide/data/conditions-page.js'])

# ---------------------------------------------------------------- decision brief
body='<div class="callout warning"><strong>A decision brief, not a recommendation.</strong> Everything below is arithmetic on invented values, produced by the same model as the comparison page. Its purpose is to show <em>which unknown facts would change the answer</em>, so the reader knows where to spend effort. It is not advice about any real household, and it does not rank real properties.</div>'
body+=section('The answer is decided by four inputs, not forty',table(['Input','Range tested on this site','Where the answer sits','What it means for effort','Official framework'],[
 ('Whether the trust permits a sale','Not a number. A legal fact.','If the trustee cannot or must not sell, every other input is irrelevant.','Resolve first. See the discovery register, D01 and D02.',source('notice')),
 ('Whether basis steps up','Not a number. A legal and factual test.','An immediate sale is low-tax with a step-up and heavily taxed without one.','Resolve second. See D03.',source('trustbasis')),
 ('Whether family-home relief applies','Occupancy, timing and filing conditions.','Without relief the assessed base resets to market value; on the invented 2045 example that raises the first-year property tax by about half.','Resolve third. See D04.',source('prop19')),
 ('Portfolio return versus home growth','Return: 0% to 10%. Growth: 0% to 7%.','Selling leads once the net portfolio return clears roughly 3%, at every growth rate tested.','This is the input most reports argue about, and on this model it matters least.',source('pmms')),
 ])+'<p class="tiny">The last row is the finding worth reading twice: the portfolio rate that makes selling lead is low and stable across home-price growth, because the holding strategies are carrying a large reassessed tax bill plus upkeep. Arguing about 3% versus 5% home appreciation changes far less than establishing whether a step-up or relief applies.</p>')

body+=section('Decision boundary: which strategy leads', '<p>The grid below runs every combination of home-price growth and net portfolio return the comparison page exposes, for a 24-year hold after a 2045 transfer. Each cell shows the leading strategy for that pair of assumptions. The point is the shape, not any single cell.</p><div class="grid four" style="margin-bottom:1rem"><div class="control"><label for="be-year">Illustrative transfer year</label><select id="be-year"><option>2040</option><option selected>2045</option><option>2050</option></select></div><div class="control"><label for="be-horizon">Years after transfer</label><select id="be-horizon"><option>10</option><option selected>24</option><option>50</option></select></div></div><div class="table-wrap"><table><thead id="boundary-head"></thead><tbody id="boundary-body"></tbody></table></div><p class="tiny">S = sell and reinvest, R = rent then sell, L = live then sell. Every cell is a separate run of the model. No estate tax, financing, depreciation, recapture or value of occupying the home is modeled, so the boundary is a teaching illustration rather than a boundary for a real household.</p>')

body+=section('Break-even return by home-price growth','<p>Read this as: at a given assumption about home prices, how strong does the portfolio have to be before selling leads? A low threshold means selling is robust to a weak market in the assumptions.</p><div class="table-wrap"><table><thead><tr><th scope="col">Assumed annual home-price growth</th><th scope="col">Net portfolio return at which selling starts to lead</th><th scope="col">Interpretation</th><th scope="col">Context only</th></tr></thead><tbody id="threshold-body"></tbody></table>')

body+=section('Which assumption actually flips the answer','<p>Each row moves one assumption away from the middle of its range and holds the other constant. A row that changes the leading strategy is an input the decision is genuinely sensitive to; a row that does not is an input a report can stop arguing about.</p><div class="table-wrap"><table><thead><tr><th scope="col">Assumption moved</th><th scope="col">Value tested</th><th scope="col">Leading strategy</th><th scope="col">Does the answer change</th><th scope="col">Context only</th></tr></thead><tbody id="sensitivity-body"></tbody></table>')

body+=section('The comparison is not close in the middle case',table(['Measure, invented example','Sell','Rent','Live','What the gap is','Official context'],[
 ('Value at the endpoint, 24 years after a 2045 transfer','Highest','Second','Third','Holding strategies pay reassessed property tax plus upkeep from the first year; the sale proceeds compound without either.',source('prop13')),
 ('Cash in the first full year','Portfolio change, not a distribution','Negative before income tax','Most negative','A rental whose rent is below its cost structure is a cost, not an income.',source('rental')),
 ('What the model leaves out','Basis risk if no step-up applies','Value of a future step-up is not credited; depreciation and recapture omitted','Imputed rent and any relief are not valued','The omissions are asymmetric: they could favor either holding strategy.',source('trustbasis')),
 ]))

body+=section('What would have to be true for a holding strategy to lead',table(['For renting to lead','For living there to lead','Official context'],[
 ('The net portfolio return must be below about 3% at the assumed growth rate. In the observed inflation record, a 3% nominal return on a diversified portfolio would be a weak outcome over 24 years, but it is not impossible.','Living must be valued at more than its modeled cash cost, and family-home relief must actually apply, otherwise the tax gap widens each year.',source('invest')),
 ('Rent must clear the break-even floor shown on the real-conditions page. On the invented inputs it does not by about 6%.','The household must intend to occupy for years, not months, because the relief and the exclusion both depend on duration.',source('prop19')),
 ('The property would need to keep appreciating faster than the portfolio net of a reassessed tax bill, which on these inputs requires unusually high price growth and unusually weak returns together.','A sale later still faces the same gain and transaction costs, so living there defers rather than avoids the comparison.',source('residence')),
 ]))
page('brief','What actually decides it.','A decision-boundary view: which inputs flip the ranking, which ones a report can stop arguing about, and what would have to be true for a holding strategy to win.',body,['guide/data/conditions.js','guide/data/model.js','guide/data/breakeven.js','guide/data/brief-page.js'])

# ---- Glossary: every definition is tied to an official page that was opened on 14 Nov 2026 ----
GLOSSARY=[
 ('Basis (income-tax)','The starting figure for gain or loss on a later sale. For inherited property the IRS FAQ gives the general rule as fair market value on the date of death, with an alternate-valuation exception.','Decides the tax on any later sale of the inherited home. Assessed value is a different number.',source('basis')),
 ('Change in ownership (property tax)','A transfer that can reset assessed value to current market value unless an exclusion applies.','Determines whether the property-tax bill resets after the transfer.',source('boe')),
 ('Change-in-ownership statement','The signed form filed with the county recorder or assessor for a transfer of real property. For a transfer by reason of death through a trust, it is filed within 150 days after the date of death.','Sets a hard filing date that the trustee or transferee must meet.',source('rtc480')),
 ('Date of death','The date the owner died.','Starts the deadlines on the Timeline page.',source('estate')),
 ('Dollar-cost averaging','Investing equal amounts at regular intervals regardless of market ups and downs; the investor buys more shares when prices are low and fewer when they are high.','The phased path in the entry-risk test is a form of dollar-cost averaging.',source('dca')),
 ('Family-home transfer (Proposition 19)','A transfer of a principal residence from parent to child, where the child makes it a principal residence. The BOE page sets a value limit built from the factored base-year value plus an allowance. The allowance is adjusted over time; the current amount is not stated here (see Flagged for Review).','The main route to limited reassessment for an inherited home. The guide does not conclude that it applies.',source('boe')),
 ('Federal filing threshold','The gross-estate amount above which a federal estate tax return is required. The IRS page lists $15,000,000 for a 2026 death.','Determines whether a federal return is needed at all.',source('estate')+' · '+source('irs706i')),
 ('Form 706','The federal estate and generation-skipping transfer tax return. The executor uses it to figure the estate tax.','The return the CPA and attorney must decide whether to file.',source('irs706about')),
 ('Form 1041','The income-tax return for a decedent\u2019s estate or trust. It reports income, deductions, gains and distributions to beneficiaries.','Governs trust and estate income once the property is held outside the decedent.',source('irs1041about')),
 ('Form 4768','The application for an automatic 6-month extension of time to file Form 706.','Used to request the automatic 6-month extension of time to file. It is the form the IRS names for that request.',source('irs706i')),
 ('Peak-to-trough decline','The fall from a market\u2019s highest level to its lowest level before the next recovery. Example: the 1929 decline the Federal Reserve reports as 89 percent.','The measure used to build the 1929 and 2008 crash shapes.',source('fed1929')),
 ('Probate Code §16061.7 notice','A trustee notice to beneficiaries and heirs, due not later than 60 days following the triggering event, subject to the section\u2019s exceptions.','Sets the notice clock that runs in parallel with the estate and tax filings.',source('notice')),
 ('Reassessment','Setting a new taxable value for property. The BOE guidance states that a family home that stops being the owner\u2019s principal residence receives a new taxable value.','The step that can move the property-tax line sharply after the transfer.',source('boe')),
 ('Residential rental property','IRS Publication 527 is titled Residential Rental Property; the guide does not restate its rules.','Relevant to Property B, which the planning premise treats as rented.',source('rental')),
 ('Treasury par yield (Constant Maturity)','The yield the U.S. Treasury publishes for a given maturity, derived from the daily par yield curve. Used here for the 3-month and 2-year rates.','The observed parking yields on 13 November 2026 come from this series.',source('treasury')),
]

body=section('Terms used in this guide',table(['Term','Plain meaning','Why it matters here','Official source'],[(a,b,c,d) for a,b,c,d in GLOSSARY])+'<p class="tiny">Each term links to an official page. Definitions are plain-language summaries of the page named in the source column, not legal advice. Reinvestment risk is used on the Black swans page as a label; no official definition has been captured yet, so it is not defined here. See Flagged for Review.</p>')
page('glossary','Plain words for the decision.','Terms that recur across the guide, each with the official page it comes from. Use them to read the Compare, Black swans and Trust steps pages.',body)

# ---- Timeline: dated deadlines in order, each opened on an official page on 14 Nov 2026 ----
body=section('When each deadline falls',table(['When (from the event)','Deadline or event','Who acts','Why it matters here','Official source'],[
 ('Day 0 · date of death','Valuation date for the federal estate accounting and the date-of-death value used for basis.','Executor or trustee; qualified appraiser','Every later figure in the Trust steps depends on documenting this value.',source('estate')+' · '+source('basis')),
 ('Within 60 days following the triggering event','Trustee notification to beneficiaries and heirs (Probate Code §16061.7(f)), subject to the section’s exceptions.','Trustee','Runs on its own clock. Not every trust triggers it; the guide does not assume that it does.',source('notice')),
 ('Within 150 days after death','Change-in-ownership statement for real property transferred by reason of death, including through a trust (RTC §480(b)).','Trustee, or transferee, with the county recorder or assessor where the property lies','The county filing for the Cupertino transfer if it is held in trust. Confirm the county and the form with counsel.',source('rtc480')),
 ('Within 9 months after death','Form 706 due, if a return is required; the IRS states the due date as 9 months after the date of death.','Executor, with the CPA','Required only above the federal filing threshold ($15,000,000 for a 2026 death). Form 4768 gives an automatic 6-month extension of time to file.',source('irs706i')),
 ('Each year: 1 November, first installment','Property-tax first installment for the secured tax year. Delinquent after 5 p.m. on 10 December, with a 10 percent penalty.','Owner or trustee','Applies to the bill on either property. The bill amount is not in this guide because it is a private figure.',source('rtc2617')),
 ('Within 1 year of transfer','Transferee lives in the home as a primary residence, and files the homeowners’ exemption claim (BOE-266 or BOE-261-G) so the exclusion starts on the transfer date. A later claim starts the exclusion in the year it is filed.','Transferee and counsel','Late occupancy or late filing delays family-home relief; the Proposition 19 value limit applies from the start.',source('prop19')),
 ('Within 3 years of transfer, and before any transfer to a third party','Form BOE-19-P, the claim for reassessment exclusion for a parent-to-child transfer, filed with the county assessor.','Transferee and counsel','Filing late is not fatal, but the exclusion then begins in the year the claim is filed.',source('prop19')),
 ('Each year: 1 February, second installment','Property-tax second installment. Delinquent after 5 p.m. on 10 April, with a 10 percent penalty.','Owner or trustee','Same bill as above; missing either date adds a penalty.',source('rtc2618')),
]),'Dated steps')
body+='<div class="callout warning"><strong>Not on this timeline yet.</strong> The Form 1041 due date for the estate or trust, and the San Francisco parcel-tax deadlines, have not been re-read from official text in this review. They are listed on the Flagged page for verification before any filing decision.</div>'
page('timeline','Deadlines in order.','The dated steps that can move the decision, from the date of death to the Proposition 19 claim deadlines. Each row links to the official rule.',body,['guide/data/model.js'] if False else [])

# ---- Attorney & CPA one-page sheet: synthetic structure, placeholders only, prints on one page ----
PRINT_CSS='''<style>@media print{@page{size:letter;margin:.4in}.header,.notice,.footer,.hero,.no-print,.skip,noscript{display:none!important}body{background:#fff;font-size:8.6pt;line-height:1.25}main{padding:0}.container{width:100%}.brief-sheet{padding:0}.brief-sheet h2{font-size:10.5pt;margin:5px 0 2px}.brief-sheet p,.brief-sheet li{margin:1px 0}.brief-sheet ul{margin:2px 0 3px;padding-left:14px}.brief-sheet .section{padding:2px 0}.brief-sheet table{font-size:7.8pt}.brief-sheet th,.brief-sheet td{padding:2px 4px}.brief-sheet .tiny{font-size:7.2pt}.brief-sheet a{color:#000;text-decoration:none}.brief-sheet .print-head{display:block!important}}
@media screen{.print-head{display:none}}</style>'''
def _li(items):
    return '<ul>'+''.join('<li>'+x+'</li>' for x in items)+'</ul>'
sheet=(
 PRINT_CSS+'<div class="brief-sheet">'
 '<div class="print-head"><strong>Attorney &amp; CPA briefing sheet · Inheritance decision guide · reviewed 14 Nov 2026</strong></div>'
 '<p class="tiny">For [ATTORNEY] and [CPA]. A structure built on invented figures. The household’s own facts go to counsel privately under placeholders such as [DECEDENT], [TRUSTEE], [PROPERTY A] and [PROPERTY B]. Educational, not legal or tax advice.</p>'
 + section('Facts to confirm privately',_li([
   'Date of death, and the date-of-death value of [PROPERTY A] from a qualified appraiser (see '+source('basis')+').',
   'Whether [PROPERTY A] is titled in [TRUSTEE]’s trust, and what the trust allows for a sale of the residence (see '+source('notice')+').',
   'Title, leases and unit status of [PROPERTY B], which the planning premise treats as two rented units and one available to the owner (see '+source('estate','Estate-rule context')+').',
   'Gross estate, adjusted taxable gifts and any elections, compared with the federal filing threshold (see '+source('irs706i')+').',
 ]))
 + section('Questions for the attorney',_li([
   'Does the trust allow sale of [PROPERTY A], or does it require another distribution? Which trust clauses control?',
   'Who files the change-in-ownership statement for [PROPERTY A], and by when? The statutory window for a transfer through a trust is 150 days from death ('+source('rtc480')+').',
   'Does a trustee notification apply, and what is the 60-day service date? ('+source('notice')+')',
   'Does any interest in [PROPERTY B] fall within the decedent’s estate, given how it is titled? ('+source('estate','Estate-rule context')+')',
 ]))
 + section('Questions for the CPA',_li([
   'Confirm the income-tax basis of [PROPERTY A]: the IRS FAQ gives the general rule (fair market value on the date of death) and the alternate-valuation exception. ('+source('basis')+')',
   'Should a Form 706 be filed? If the return is not ready, the Form 4768 extension is 6 months from the 9-month due date ('+source('irs706i')+').',
   'Which returns does the trust or estate file, and on what dates? The Form 1041 due date is still to be confirmed from IRS text ('+source('irs1041about')+').',
   'What rental income and depreciation rules apply to [PROPERTY B]? ('+source('rental')+')',
   'Which Proposition 19 claims apply to the transfer, and their filing periods? The periods are not yet confirmed from BOE text. ('+source('boe')+')',
 ]))
 + section('Figures used, rounded to $10 unless an official amount',table(['Figure','Value','Source'],[
   ('Federal filing threshold, 2026 death','$15,000,000 (official)',source('estate')),
   ('Treasury par yields, 13 Nov 2026','3-month 4.32%; 2-year 4.88%',source('treasury')),
   ('Crash shapes used in the test','1929: −89% over 34 months · 2008: −57% over 17 months',source('fed1929')+' · '+source('fed2008')),
   ('Entry test, per $100,000, year 10','Invest all now '+money_range(_year10('2008','sell_now_all'))+' · park 24 then phase '+money_range(_year10('2008','park_24'))+' (2008-style)',source('fed2008')),
 ]))
 + section('What would change this advice',_li([
   'A different trust clause, title, or basis answer from counsel or the CPA (see the questions above).',
   'A different filing position for the estate, or a federal threshold change after the date of death.',
   'A different parking yield, or a different post-trough growth view; the test shows the sensitivity, not a forecast.',
 ]))
 + '</div>'
)
page('attorney-cpa','Attorney &amp; CPA briefing sheet.','One printable page for counsel and the tax adviser. Placeholders replace every private fact; figures are rounded to $10 unless an official amount.',sheet)
