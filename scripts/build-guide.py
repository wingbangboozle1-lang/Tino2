#!/usr/bin/env python3
"""Generate the public, generic guide; never put household records in this file."""
from pathlib import Path
from html import escape
import re

ROOT=Path(__file__).resolve().parents[1]
S={
 'dgs3m':('FRED · 3-month Treasury bill (DGS3MO)','https://fred.stlouisfed.org/series/DGS3MO'),
 'dgs2':('FRED · 2-year Treasury note (DGS2)','https://fred.stlouisfed.org/series/DGS2'),
 'spIndex':('FRED · OECD U.S. share price index (SPASTT01USM661N)','https://fred.stlouisfed.org/series/SPASTT01USM661N'),
 'rp2532':('IRS · Rev. Proc. 2025-32, 2026 inflation adjustments','https://www.irs.gov/pub/irs-drop/rp-25-32.pdf'),
 'cg409':('IRS · Topic 409 capital gains','https://www.irs.gov/taxtopics/tc409'),
 'niit559':('IRS · Topic 559 net investment income tax','https://www.irs.gov/taxtopics/tc559'),
 'form706':('IRS · About Form 706','https://www.irs.gov/forms-pubs/about-form-706'),
 'i706':('IRS · Instructions for Form 706 (07/2026)','https://www.irs.gov/instructions/i706'),
 'usc6075':('U.S. Code · 26 U.S.C. §6075 (Cornell LII copy)','https://www.law.cornell.edu/uscode/text/26/6075'),
 'sccTax':('Santa Clara County · Property Tax (DTAC)','https://www.santaclaracountyca.org/Property_Tax.html'),
 'sccRateBook':('Santa Clara County Controller-Treasurer · Compilation of Tax Rates FY 2025–26','https://controller.santaclaracounty.gov/property-tax-distribution/property-tax-rate-book'),
 'ftbSchedule':('FTB · 2025 Form 540 rate schedules (PDF)','https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf'),
 'rtc17043':('CA Revenue & Taxation Code §17043','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=17043.'),
 'boe':('California BOE · Prop 19','https://www.boe.ca.gov/prop19/'),
 'prop19':('California BOE · fact sheet','https://www.boe.ca.gov/pdf/pub801.pdf'),
 'allowance':('BOE · 2025/009','https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf'),
 'prop13':('BOE · Prop 13 explanation','https://boe.ca.gov/proptaxes/pdf/lta25023.pdf'),
 'county':('Santa Clara County Assessor','https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2'),
 'estate':('IRS · estate tax','https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax'),
 'estate27':('IRS · 2027 adjustments','https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts'),
 'rp2532':('IRS · Rev. Proc. 2025-32','https://www.irs.gov/pub/irs-drop/rp-25-32.pdf'),
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
 'ghVisibility':('GitHub Docs · setting repository visibility','https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility'),
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
 'rtc480':('CA Revenue & Taxation Code §480','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480.'),
 'rtc2617':('CA Revenue & Taxation Code §2617','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=2617.'),
 'rtc2618':('CA Revenue & Taxation Code §2618','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=2618.'),
 'irs706about':('IRS · About Form 706','https://www.irs.gov/forms-pubs/about-form-706'),
 'irs706i':('IRS · Instructions for Form 706','https://www.irs.gov/instructions/i706'),
 'i4768':('IRS · Instructions for Form 4768 (02/2020)','https://www.irs.gov/instructions/i4768'),
 'irs1041about':('IRS · About Form 1041','https://www.irs.gov/forms-pubs/about-form-1041'),
 'dca':('SEC Investor.gov · dollar-cost averaging','https://www.investor.gov/introduction-investing/investing-basics/glossary/dollar-cost-averaging'),
 'secCallable':('SEC Investor.gov · callable or redeemable bonds','https://www.investor.gov/introduction-investing/investing-basics/glossary/callable-or-redeemable-bonds'),
 'irs701':('IRS · Topic 701, sale of your home','https://www.irs.gov/taxtopics/tc701'),
 'scc-recording':('Santa Clara County Clerk-Recorder · Recording real estate','https://clerkrecorder.santaclaracounty.gov/recording-documents/recording-real-estate'),
 'usc6072':('U.S. Code · 26 U.S.C. §6072 time for filing income tax returns (Cornell LII copy)','https://www.law.cornell.edu/uscode/text/26/6072'),
 'rtc11911':('CA Revenue & Taxation Code §11911','https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=11911.'),
 'usc1031':('U.S. Code · 26 U.S.C. §1031 (Cornell LII copy)','https://www.law.cornell.edu/uscode/text/26/1031'),
 'asrGlossary':('Santa Clara County Assessor · glossary','https://asr.santaclaracounty.gov/faq/glossary'),
 'ftb540':('FTB · 2025 Instructions for Form 540','https://www.ftb.ca.gov/forms/2025/2025-540-instructions.html'),
 # Added 16 Nov 2026 by session 070d6a2e; each page below was opened and read that day.
 'boe2026':('BOE · 2026 Letters to Assessors index','https://www.boe.ca.gov/proptaxes/2026.htm'),
 'lta26026':('BOE · LTA 2026/026, Proposition 19 exclusion Q&amp;A','https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf'),
 'cdiSurvey':('CA Department of Insurance · homeowners premium comparison','https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/'),
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
 ('Decide',[('overview','Overview','index.html'),('summary','Executive summary','guide/summary.html'),('decision','Compare','guide/decision.html'),('paths','Paths, mixed and pure','guide/paths.html'),('whatif','What-if controls','guide/whatif.html'),('brief','What decides it','guide/brief.html'),('stress','Black swans','guide/stress.html')]),
 ('Property &amp; rules',[('property','Properties','guide/property.html'),('tax','Taxes','guide/tax.html'),('process','Trust steps','guide/process.html'),('timeline','Timeline','guide/timeline.html')]),
 ('Evidence &amp; terms',[('conditions','Real conditions','guide/conditions.html'),('questions','Questions','guide/questions.html'),('glossary','Glossary','guide/glossary.html'),('sources','Sources','guide/sources.html')]),
 ('Act',[('precommit','Pre-commitment','guide/precommit.html'),('attorney-cpa','Attorney &amp; CPA sheet','guide/attorney-cpa.html'),('suggestions','Suggestions','guide/suggestions.html'),('review','Flagged','guide/review.html')]),
]
PAGES=[item for _,group in PAGE_GROUPS for item in group]
def page(key,title,lead,body,scripts=(),home=False):
    body=AP.attach(body)
    base='' if home else '../'
    nav=''.join(f'<div class="navgroup" role="group" aria-label="{gname}"><span class="navlabel" aria-hidden="true">{gname}</span>'+''.join(f'<a href="{base}{path}"'+(' aria-current="page"' if id==key else '')+f'>{label}</a>' for id,label,path in items)+'</div>' for gname,items in PAGE_GROUPS)
    links=''.join(f'<script defer src="{base}{s}"></script>' for s in ['assets/safe.js',*scripts])
    hero=f'''<section class="hero{' compact' if not home else ''}"><div class="container"><div class="eyebrow">Inheritance decision guide · official sources re-opened 13–17 Nov 2026</div><h1>{title}</h1><p class="lead">{lead}</p><div class="meta"><span class="pill">Private facts withheld</span><span class="pill">Official sources linked</span><span class="pill">Synthetic examples only</span></div></div></section>'''
    html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow,noarchive"><meta name="referrer" content="no-referrer"><title>{escape(re.sub(r'<[^>]*>', ' ', title))} · Inheritance planning</title><link rel="stylesheet" href="{base}assets/safe.css">{links}</head><body><a class="skip" href="#main">Skip to content</a><header class="header"><div class="container topbar"><a class="brand" href="{base}index.html"><span class="brand-mark">H</span><span>Inheritance planning<small>PUBLIC GUIDE · FICTIONAL EXAMPLES</small></span></a><button class="menu" aria-expanded="false" aria-controls="navigation">Menu</button><nav class="nav" id="navigation" aria-label="Main navigation">{nav}</nav></div></header><div class="notice"><div class="container"><strong>Public guide.</strong> Only synthetic example inputs are used. Household records and household-derived figures are not published. Model outputs are not forecasts or personal advice. <a href="{base}guide/review.html">Important privacy limits →</a></div></div><noscript><div class="no-js">Tables of rules are available without JavaScript. Projection tables and suggestion choices require JavaScript.</div></noscript><main id="main">{hero}<div class="container">{body}</div></main><footer class="footer"><div class="container footer-inner"><div><strong>Inheritance planning</strong><br>Educational scenarios, not legal, tax, insurance or investment advice.</div><div>Source review: 13–17 Nov 2026 · <a href="{base}guide/sources.html">Sources</a> · <a href="{base}guide/review.html">Flagged for review</a><br>Never upload personal records to this public repository.</div></div></footer></body></html>'''
    target=ROOT/('index.html' if home else f'guide/{key}.html');target.write_text(html+'\n',encoding='utf8')

def cards(items):
    return '<div class="grid three">'+''.join(f'<a class="card card-link" href="{url}"><div class="eyebrow">{tag}</div><h3>{title}</h3><p class="muted">{desc}</p><span class="arrow">Explore →</span></a>' for tag,title,desc,url in items)+'</div>'

# ---- b33f5f9e additions: phased entry, reinvestment risk, first-screen answer, new pages ----
import sys as _sys
_sys.path.insert(0, str(ROOT / 'scripts'))
import analysis_pages as AP  # synthetic public examples only; private records are not loaded
CTX={'S':S,'table':table,'section':section,'source':source}
import phased_model as PM

# ---- Imputed rent, computed from the model itself so the disclosure can never drift -------------
# The living paths are credited the rent the owner does not pay (analysis_model.simulate,
# 'imputed_rent_mo'). This block measures that credit on the synthetic example inputs and states
# it on the pages that publish the comparison. It is recomputed at build time; no number is typed.
def _imputed_block():
    A, P = AP.ACTIVE_A, AP.ACTIVE_PARAMS
    with_credit = AP.M.simulate('live', 'base', P, A, 25)
    no_credit_p = dict(P, imputed_rent_mo=0.0)
    no_credit = AP.M.simulate('live', 'base', no_credit_p, A, 25)
    sell = AP.M.simulate('sell_lump', 'base', P, A, 25)
    gap = with_credit['total'] - no_credit['total']
    share = gap / with_credit['total']
    flips = (no_credit['total'] > sell['total']) != (with_credit['total'] > sell['total'])
    # Does the credit decide which path leads at any published horizon?
    flip_horizons = []
    for h in (10, 25, 50):
        w = AP.M.simulate('live', 'base', P, A, h)['total']
        n = AP.M.simulate('live', 'base', dict(P, imputed_rent_mo=0.0), A, h)['total']
        best_other = max(AP.M.simulate(q, 'base', P, A, h)['total'] for q in ('sell_lump', 'rent'))
        if (w > best_other) != (n > best_other):
            flip_horizons.append(h)
    note = (
        'The living paths <em>are</em> credited the rent an owner does not pay while occupying the home \u2014 '
        'an explicit, adjustable assumption, not a market rent. On the default synthetic inputs that credit is worth '
        f'about ${PM.round10(gap):,} at 25 years, roughly {round(share * 100)}% of the live path\u2019s total. '
        'The <a href="whatif.html">What-if controls</a> run the same model with the credit set to zero.'
    )
    if flip_horizons:
        horizons = ', '.join(f'{h} years' for h in flip_horizons)
        note += (' On these inputs the credit decides which path leads at ' + horizons + ': remove it and a '
                 'selling path leads instead. That makes it a first-order assumption, not a rounding detail, '
                 'and it is why the owner\u2019s own figure for occupying the home has to be agreed in writing '
                 'before the comparison is used.')
    return {'note': note, 'gap': gap, 'share': share, 'with_credit': with_credit['total'],
            'no_credit': no_credit['total'], 'flips': flips, 'flip_horizons': flip_horizons,
            'rent_avoided': with_credit['avoided_rent']}

IMPUTED = _imputed_block()
IMPUTED_NOTE = IMPUTED['note']

def money(v):
    value = PM.round10(v)
    return (f"−${abs(value):,}" if value < 0 else f"${value:,}")

def money_range(vals):
    lo, hi = min(vals), max(vals)
    return money(lo) if PM.round10(lo) == PM.round10(hi) else f"{money(lo)} – {money(hi)}"

def _plan_reserve_a():
    """Model maintenance reserve for Property A, years 1-5 after transfer (model output)."""
    M = AP.M
    p = AP.ACTIVE_PARAMS
    base = M.fmv_at_inheritance(AP.ACTIVE_A, p)
    return sum(p['maint_a'] * base * (1 + p['g_post']) ** t for t in range(1, 6))

def _plan_reserve_b():
    """Model maintenance reserve for Property B, the next five years (model output)."""
    p = AP.ACTIVE_PARAMS
    b = AP.EXAMPLE_B
    return sum(p['maint_b'] * b['fmv_now'] * (1 + p['g_pre']) ** t for t in range(1, 6))

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

# ---- 16 Nov 2026 (session ec971900): return-to-peak recovery shape, and an explicit 3-month/2-year ladder ----
PARK_FOR_TEMPLATE = {'1929': 'crash-1929', '2008': 'crash-2008', 'none': 'flat'}
MIXES = [(0.0, 'Rolled three-month bills only'),
         (1.0, 'A two-year note held to maturity only'),
         (0.5, 'Ladder: half a two-year note, half rolled three-month bills')]


def _park_value(park_months: int, weight_2y: float, kind: str):
    """Terminal value and realised annual yield of $100,000 parked for `park_months`."""
    path = PM.ladder_path(park_months, weight_2y, kind, park_months)
    factor = 1.0
    for rate in path:
        factor *= (1.0 + rate) ** (1 / 12)
    return PM.round10(PM.PRINCIPAL * factor), factor ** (12.0 / park_months) - 1.0


def park_mix_table():
    rows = []
    for weight, label in MIXES:
        for park in (24, 36):
            cells = [label, f'{park} months']
            for kind in PM.PARK_PATHS:
                value, annual = _park_value(park, weight, kind)
                cells.append(f'{money(value)} <span class="tiny">({annual * 100:.2f}% a year)</span>')
            cells.append(source('treasury', 'Treasury · observed 3-month and 2-year par yields')
                         + ' · ' + source('treasuryBills', 'TreasuryDirect · bills')
                         + ' · ' + source('treasuryNotes', 'TreasuryDirect · notes')
                         + ' · every rate after the first quarter is an assumption, not an observation')
            rows.append(tuple(cells))
    return table(['How the parked proceeds are held', 'Wait before buying stocks',
                  'Rates stay at the observed level', 'Rates fall, 1929-scenario path',
                  'Rates fall, 2008-scenario path', 'Rates rise', 'Source'], rows)


def _path_for(template: str, strategy: str):
    """The monthly parking-yield path one strategy faces in one crash template.

    A plan that never parks money, or that parks it and never buys equities, is held in rolled
    bills: only a plan that waits and then deploys can afford a two-year leg without selling a
    note before maturity.
    """
    kind = PARK_FOR_TEMPLATE[template]
    spec = PM.STRATEGIES[strategy]
    if spec['park'] == 0:
        return PM.bill_path(kind, PM.HORIZON)
    return PM.ladder_path(spec['park'], 0.5, kind, PM.HORIZON)


def _peak_runs(template: str, strategy: str):
    path = _path_for(template, strategy)
    return [PM.simulate(template, strategy, PM.YIELDS['base'], rec, shape='peak', cash_path=path)
            for rec in (REC_LO, REC_HI)]


def _under_water(runs):
    months = sorted({r['under_water_months'] for r in runs})
    return f'{months[0]} months' if len(months) == 1 else f'{months[0]}–{months[1]} months'


PEAK_ROWS = []
for _k in ['sell_now_all', 'mixed_third', 'park_24', 'park_36', 'cash_only']:
    _r29, _r08, _rn = _peak_runs('1929', _k), _peak_runs('2008', _k), _peak_runs('none', _k)
    PEAK_ROWS.append((STRAT_LABEL[_k],
                      money_range([x['worst_36'] for x in _r29]), _under_water(_r29),
                      money_range([x['value_end'] for x in _r29]),
                      money_range([x['worst_36'] for x in _r08]), _under_water(_r08),
                      money_range([x['value_end'] for x in _r08]),
                      money_range([x['value_end'] for x in _rn]),
                      source('fed1929', 'Fed 1929 · pre-crash high regained Nov 1954') + ' · '
                      + source('fed2008', 'Fed 2008') + ' · the 2008 regain month is an assumption'))

SHAPE_ROWS = []
for _t in ('1929', '2008'):
    for _k in ('sell_now_all', 'mixed_third', 'park_24'):
        _path = _path_for(_t, _k)
        _trend = [PM.simulate(_t, _k, PM.YIELDS['base'], rec, shape='trend', cash_path=_path)
                  for rec in (REC_LO, REC_HI)]
        _peak_ = _peak_runs(_t, _k)
        _tt = [x['value_end'] for x in _trend]
        _pp = [x['value_end'] for x in _peak_]
        SHAPE_ROWS.append((f'{_t} shape · {STRAT_LABEL[_k]}', money_range(_tt), money_range(_pp),
                           money_range([b - a for a, b in zip(_tt, _pp)]),
                           source('fed1929' if _t == '1929' else 'fed2008', 'Fed ' + _t)
                           + ' · the shapes differ only in the assumed recovery, not in the decline'))

PEAK_SECTION_HTML = section(
    'Entry risk, second version: a recovery that returns to the prior peak, with the proceeds in a 3-month/2-year ladder',
    '<div class="callout"><strong>Why a second version of the test.</strong> The table above lets the index grow '
    'from its trough at the same 4% to 8% it grows at in the no-crash control. That is the reason its 2008 parked '
    'rows equal the control, and it flatters a peak entry: it never has to live with the fact that the 1929 high '
    'stood for a quarter of a century. The Federal Reserve states that the Dow peaked at 381.17 on 3 September 1929, '
    'closed at 41.22 on 8 July 1932 — 89 percent below the peak — and "did not return to its pre-crash heights until '
    'November 1954" (<a href="https://www.federalreservehistory.org/essays/stock-market-crash-of-1929" rel="noopener noreferrer">Fed 1929 ↗</a>), '
    'which is 303 months after the peak. This version rebuilds the index so it reaches its prior peak at exactly that '
    'month for 1929, then grows at the same 4% to 8%. For 2008 it uses 66 months, labelled an assumption: no official '
    'page re-opened in this review states when the S&amp;P 500 regained its October 2007 level, and 66 months is the '
    'figure the decision engine already carries.</div>'
    '<p>The parked money is now a Treasury ladder rather than one flat rate. A three-month bill reprices every quarter, so what '
    'proceeds earn over a 24- or 36-month wait is a path, not a number. TreasuryDirect sells bills "for terms ranging '
    'from four weeks to 52 weeks" and notes for "a term of 2, 3, 5, 7, or 10 years" '
    '(<a href="https://www.treasurydirect.gov/marketable-securities/treasury-bills/" rel="noopener noreferrer">bills ↗</a>, '
    '<a href="https://www.treasurydirect.gov/marketable-securities/treasury-notes/" rel="noopener noreferrer">notes ↗</a>). '
    'The yields used are the observed par yields on 13 Nov 2026: 4.32% for three months and 4.88% for two years '
    '(<a href="https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve&field_tdr_date_value_month=202611" rel="noopener noreferrer">Treasury ↗</a>). '
    'Only a plan that waits before it buys can hold the note to maturity, so the note leg is priced only for the '
    'parking plans; a plan that needs money earlier would have to sell the note at market, which is not modeled here.</p>'
    + '<h3>What the parked money earns, per $100,000</h3>'
    + '<p>Value at the day the phasing begins, on the same $100,000. The four columns are four assumed paths for the '
    'bill rate after the first quarter: unchanged, the two fall-to-low-rates paths the decision engine uses inside its '
    'crash scenarios, and a rise. Read the two middle columns as the reinvestment risk of the short bill, and the last '
    'as the price of locking the note instead.</p>'
    + park_mix_table()
    + '<p class="tiny">Realised annual yield is the geometric rate the pot actually earned over the wait, not a quoted '
    'coupon. The note-only row at 24 months is identical in all four columns by construction: a two-year note bought at '
    'the observed 4.88% and held to maturity does not reprice inside the wait, which is exactly what a bill roll does. '
    'At 36 months the note row moves again, because months 25 to 36 are spent in rolled bills after the note matures. '
    'Federal income tax is due on Treasury interest and there is no state or local income tax on it '
    '('
    '<a href="https://www.treasurydirect.gov/marketable-securities/treasury-notes/" rel="noopener noreferrer">TreasuryDirect · taxes ↗</a>'
    '); no tax, fee or inflation adjustment is applied to these amounts. Rates other than the first quarter are assumptions.</p>'
    + '<h3>The five entry plans on the return-to-peak shape</h3>'
    + '<p>Each plan parks its undeployed money in the ladder above, on the rate path that matches its crash. '
    '"Months under water" counts the months in the ten-year window in which the portfolio is below the $100,000 put in '
    '— the measure a 303-month regain makes visible and a terminal value hides. The 1929 column carries one number '
    'rather than a range because the window ends 183 months before the recorded regain, so the post-regain growth rate '
    'never applies inside it.</p>'
    + table(['Plan', '1929 · worst point in the first 36 months', '1929 · months under water', '1929 · value after 10 years',
             '2008 · worst point in the first 36 months', '2008 · months under water', '2008 · value after 10 years',
             'No-crash control · value after 10 years', 'Source'], PEAK_ROWS)
    + '<h3>How much the assumed recovery is worth</h3>'
    + '<p>The same plan, the same decline, the same parking — and two ideas about what happens after the low. The gap is '
    'a modelling assumption, not new information about the market, and on this horizon it is larger than most of the '
    'differences the site reports between paths.</p>'
    + table(['Plan and template', 'Year 10, trend shape', 'Year 10, return-to-peak shape', 'Difference', 'Source'], SHAPE_ROWS)
    + '<div class="callout warning"><strong>What this version says that the first one could not.</strong> Under a '
    'recovery that only reaches its starting level again after 25 years, the plan that invested everything at the peak '
    'spent every one of the 120 months in the window below the amount put in, and finished the decade at about a fifth '
    'of it. The parked plans never bought that top: parking 36 months was marked below the amount put in in no month at '
    'all, and parking 24 months and phasing into a market still falling spent 21 months under water before it turned. '
    'Both parked plans finished the decade above the peak entry in both crash shapes. In the 2008 shape the 24-month '
    'wait beat the 36-month one, because that low arrives at month 17 and a longer wait buys the climb instead of the '
    'bottom — the honest form of the finding, since the wait is priced against a shape nobody can know in advance. In '
    'the no-crash control the ranking turns on where equity growth sits against the parked yield: at 4% growth a '
    'two-year wait still ends slightly ahead, at 8% it ends about eighteen thousand behind per $100,000. That is the '
    'whole trade on one row of a table: phasing is insurance against the entry date, paid for with the growth of a good '
    'decade. No source reviewed here assigns a probability to either state.</div>'
    + '<p class="tiny">Not modeled: individual bill maturities and auction discounts, the market value of a note sold '
    'before maturity, income tax on the interest or on the gain, transaction costs, the timing of the trust transfer, '
    'and any path between the peak and the low except a smooth geometric one. Reinvestment risk is the risk the SEC '
    'describes for money that has to be put to work again later — "faced with reinvesting the money at a lower, less '
    'attractive rate" '
    '('
    '<a href="https://www.investor.gov/introduction-investing/investing-basics/glossary/callable-or-redeemable-bonds" rel="noopener noreferrer">SEC Investor.gov ↗</a>'
    ') — and the two middle columns of the parking table are that risk, priced.</p>',
    '03c / ladder and shape')


# ---- e3f08d9e: the same entry question, replayed on recorded official history ----
import phased_history as RH

def pct(v, digits=2):
    return '—' if v is None else f"{v*100:.{digits}f}%"


def pct_signed(v, digits=1):
    """A percentage with the site’s minus sign, not a hyphen."""
    text = f"{abs(v) * 100:.{digits}f}%"
    return (f"−{text}" if v < 0 else f"+{text}")

_rh_entries = RH.entry_years()
_rh_all = RH.summary()
_rh_down = RH.summary(RH.down_entries())
_rh_up = RH.summary([t for t in _rh_entries if RH.PRICE[t] / RH.PRICE[t - 1] - 1 >= 0])
_rh_deep = RH.summary(RH.crash_entries())
_rh_real = sorted(RH.simulate(t, 'park24')['terminal_real'] - RH.simulate(t, 'now')['terminal_real'] for t in _rh_entries)
_rh_real_median = _rh_real[len(_rh_entries) // 2]
_rh_data = (source('dgs3m', 'FRED · 3-month yield') + ' · ' + source('dgs2', 'FRED · 2-year yield')
            + ' · ' + source('spIndex', 'FRED · share prices'))

def _rh_group(s_, label, span):
    d = s_['park24']
    wins = ', '.join(str(y) for y in d['win_years']) if d['wins'] else 'none'
    return (label, span, f"{d['wins']} of {s_['n']} · {wins}", RH.money(d['median_diff']),
            f"{RH.money(d['best_diff'])} / {RH.money(d['worst_diff'])}", f"{d['dd_wins']} of {s_['n']}", _rh_data)

_rh_groups = table(['Entry group', 'Entry years tested', 'Park 24 months, then phase over 12: entry years it beat investing at once',
                    'Median difference at year 10', 'Best and worst difference', 'Years the worst point was better', 'Official data'],
                   [_rh_group(_rh_all, 'Every entry year', f"{_rh_entries[0]} to {_rh_entries[-1]} · {_rh_all['n']}"),
                    _rh_group(_rh_up, 'Years it rose or held flat', f"{_rh_up['n']} of {_rh_all['n']}"),
                    _rh_group(_rh_down, 'Years it fell', f"{_rh_down['n']} of {_rh_all['n']}"),
                    _rh_group(_rh_deep, 'Years it fell by 10% or more', f"{_rh_deep['n']} of {_rh_all['n']} · two cases, not a rate")])

_rh_rows = []
for _t in (1987, 1989, 2000, 2002, 2007, 2008, 2015):
    r = {k: RH.simulate(_t, k) for k in RH.STRATEGIES}
    _rh_rows.append((str(_t), pct_signed(r['now']['entry_change']), RH.money(r['now']['terminal']), RH.money(r['now']['worst_36']),
                     RH.money(r['park24']['terminal']), pct(r['park24']['parked_yield']), RH.money(r['park24y']['terminal']),
                     RH.money(r['park36']['terminal']), _rh_data + ' · ' + source('cpiHistory', 'FRED · CPI')))

_rh_flat = []
for _label, _desc, _flat in [('The recorded bill yields, month by month', 'published H.15 annual averages: 1.40% for 2008, then 0.15% for 2009', None),
                             ('Flat 4.32%, the rate observed on 13 Nov 2026', 'the flat assumption the template test above uses', 0.0432),
                             ('Flat 1.00%', 'an invented downside for reinvestment', 0.01),
                             ('Flat 5.00%', 'an invented upside for reinvestment', 0.05)]:
    if _flat is None:
        _rh_flat.append((_label, _desc, RH.money(RH.simulate(2008, 'park24')['terminal']), '— the reference', _rh_data))
    else:
        d = RH.flat_park_compare(2008, 'park24', _flat)
        _src = (source('treasury', 'Treasury · observed rate') if _flat == 0.0432 else
                source('treasuryBills', 'TreasuryDirect · bills') if _flat == 0.01 else source('treasuryNotes', 'TreasuryDirect · notes'))
        _rh_flat.append((_label, _desc, RH.money(d['flat']), RH.money(d['difference']) + ' against the recorded path', _src))

_rh_div = []
for _dv, _lbl in ((0.0, 'None: the price index alone'), (RH.DIVIDENDS, '2.0 points a year, the value this test uses'), (0.04, '4.0 points a year')):
    _sm = RH.summary(dividends=_dv)['park24']
    _rh_div.append((_lbl, RH.money(_sm['median_diff']), f"{_sm['wins']} of {_rh_all['n']}",
                    'The price index excludes distributions, so each row is an invented assumption, not an official figure. '
                    + source('spIndex', 'FRED · the index as published')))
_rh_div_stats = {dv: RH.summary(dividends=dv)['park24'] for dv in (0.0, RH.DIVIDENDS, 0.04)}
_rh_div_note = ('The share-price index used is a price index. The test therefore applies one stated '
  '2.0-point-a-year assumption to every stock leg, and the cost of waiting moves with it. Across the '
  + str(_rh_all['n']) + ' entries the median difference is ' + RH.money(_rh_div_stats[0.0]['median_diff'])
  + ' with no dividend at all, ' + RH.money(_rh_div_stats[RH.DIVIDENDS]['median_diff']) + ' at 2.0 points and '
  + RH.money(_rh_div_stats[0.04]['median_diff']) + ' at 4.0 points; the same three settings mean '
  + RH.money(_rh_div_stats[0.0]['mean_diff']) + ', ' + RH.money(_rh_div_stats[RH.DIVIDENDS]['mean_diff'])
  + ' and ' + RH.money(_rh_div_stats[0.04]['mean_diff']) + '. Every figure in this sentence is invented arithmetic '
  'on a recorded price path, not an official return series.')
_rh_2y_max = max(RH.simulate(t, 'park24y')['terminal'] - RH.simulate(t, 'park24')['terminal'] for t in _rh_entries)
_rh_2y_med = sorted(RH.simulate(t, 'park24y')['terminal'] - RH.simulate(t, 'park24')['terminal'] for t in _rh_entries)[len(_rh_entries) // 2]
_rh_08 = {k: RH.simulate(2008, k) for k in RH.STRATEGIES}
_rh_02 = {k: RH.simulate(2002, k) for k in RH.STRATEGIES}
_rh_flat08 = RH.flat_park_compare(2008, 'park24', 0.0432)

RECORDED_SECTION_HTML = section(
    'The same test on recorded history, with the yields a crash actually pays',
    '<div class="callout"><strong>Why this section exists.</strong> The template tests above answer the entry question on two smooth shapes, with one observed yield applied flatly and a maturity ladder tried at three weights. '
    'This one replays the identical decision — park the net proceeds for 24 or 36 months in short Treasuries, then phase into stocks over 12 months — against '
    '<strong>recorded history</strong>: the actual December share-price index and the <em>actual</em> published 3-month and 2-year Treasury yields of each year. '
    'The reason it matters fits in one sentence: in a real crash the yield on parked money falls at the same time the index does, so waiting is not risk-free in either direction.</div>'
    + '<h3>How this is built</h3><p>Everything is per $100,000 of illustrative proceeds over ten years, the same invented amount the template test uses; no household figure is an input. '
      'Month 0 is the December before the entry year. The index between two year-ends is a geometric interpolation of the two December observations of the OECD U.S. share-price index, '
      'published by the Federal Reserve Bank of St. Louis; the December values for 1986, 1987, 2007, 2008 and 2009 were re-read from that official series on 16 Nov 2026. '
      'Parked cash earns, month by month, the published <em>annual average</em> of the H.15 constant-maturity yield for that calendar year, compounded at one-twelfth of the annual rate, because H.15 bill yields are quoted on an investment basis '
      '(' + source('dgs3m', '3-month DGS3MO') + ', ' + source('dgs2', '2-year DGS2') + '). '
      'A phase-in is twelve equal monthly tranches, sized from the balance the parking account holds when the window closes. The window is 1982 to 2016 for the entry year: the 3-month series begins on 1 September 1981, so nothing earlier can be replayed on recorded yields, and 2016 is the last entry year whose ten years end inside the price series.</p>'
    + '<h3>The record, grouped</h3>' + _rh_groups
    + '<p class="tiny">A difference is the parked plan minus investing at once, at year ten, per $100,000, with a stated 2.0-point-a-year dividend assumption on every stock leg. '
      'Across all ' + str(_rh_all['n']) + ' entries the median nominal difference is ' + RH.money(_rh_all['park24']['median_diff'])
      + ', and the median difference deflated by annual CPI-U averages into the entry year’s dollars is ' + RH.money(_rh_real_median)
      + ' — smaller, because inflation erodes parked cash as well as a portfolio. Deflating a December-to-December path with annual CPI averages is an approximation this site computed, not a published figure '
      + source('cpiHistory', 'FRED · CPI-U') + '.</p>'
    + '<h3>Seven entry years, in full</h3>'
    + table(['Entry year', 'Share index change, that December', 'Invest at once · year 10', 'Invest at once · worst point, first 3 years',
             'Park 24 months then phase · year 10', 'Yield earned while parked', 'Park 24 at the 2-year note yield · year 10',
             'Park 36 months then phase · year 10', 'Official data'], _rh_rows)
    + '<p class="tiny">The 2008 row is the case the brief asks about. An heir who sold and invested at once watched the illustration fall to '
      + RH.money(_rh_08['now']['worst_36']) + ' inside the first three years, while the parked plan printed no loss at all until it began buying during 2010 and finished ten years '
      + RH.money(_rh_08['park24']['terminal'] - _rh_08['now']['terminal']) + ' ahead. The 2002 row is the same protection bought in the wrong year: a shallower worst point, and '
      + RH.money(_rh_02['park24']['terminal'] - _rh_02['now']['terminal']) + ' at year ten. Read the yield column with the price column beside it: the years when parking looked wisest are the years it earned least.</p>'
    + '<h3>What a flat-yield assumption hides</h3>'
    + table(['What the parked money is assumed to earn', 'What that means for a 2008 entry', 'Park 24 months then phase · year 10', 'Difference', 'Official data'], _rh_flat)
    + '<h3>How much of the answer rests on an assumption no official source publishes</h3>'
    + table(['Dividend or total-return assumption on the stock legs', 'Median difference at year 10, all entries', 'Entry years where parking wins', 'Context'], _rh_div)
    + '<div class="callout warning"><strong>Six readings a written policy should carry.</strong> '
      '(1) On the record, parking and phasing <em>beat</em> investing at once in ' + str(_rh_all['park24']['wins']) + ' of ' + str(_rh_all['n'])
      + ' entry years, and every one of them sits at or just before a bear market (' + ', '.join(str(y) for y in _rh_all['park24']['win_years']) + '). '
      '(2) Its median price was ' + RH.money(_rh_all['park24']['median_diff']) + ' per $100,000 over ten years, and the single worst entry year cost '
      + RH.money(_rh_all['park24']['worst_diff']) + '. '
      '(3) It improved the worst point in the first three years in ' + str(_rh_all['park24']['dd_wins']) + ' of ' + str(_rh_all['n'])
      + ' entries, and the improvement was large only where a crash actually arrived: ' + RH.money(_rh_08['park24']['worst_36'] - _rh_08['now']['worst_36'])
      + ' at the 2008 entry. (4) The <em>yield</em> assumption matters more than the <em>maturity</em> choice: holding the 2008 parked cash at a flat 4.32% instead of the recorded 1.40%-then-0.15% path adds '
      + RH.money(_rh_flat08['difference']) + ', about a fifth of the median cost of waiting, while moving the parking from 3-month bills to 2-year notes changed the ten-year outcome by no more than '
      + RH.money(_rh_2y_max) + ' across all entries and about ' + RH.money(_rh_2y_med) + ' at the median. (5) A 36-month park costs roughly a year more of the same trade: '
      + RH.money(_rh_all['park36']['median_diff']) + ' at the median against ' + RH.money(_rh_all['park24']['median_diff'])
      + ' for 24 months. (6) A 1929-style entry cannot be replayed on recorded yields here at all, so the template test above remains the only view of a deeper shape.</div>'
    + '<h3>What this test does not contain</h3>'
    + '<p>No transaction cost, no tax on the Treasury interest (it is federally taxable and generally exempt from California income tax, '
      + source('treasuryBills', 'TreasuryDirect on bill terms') + '), no tax timing on the tranches, no inflation-linked securities, no bonds outside the two maturities named, '
      'and no allowance for changing one’s mind mid-parking. Sampling at December understates within-year swings: the same series shows 1987 ending 5.1% below 1986 although it fell 26.8% between its August 1987 monthly value and its December value. '
      'Nothing here is a forecast and no probability is attached to any entry year. The securities that make a real ladder behave differently from this arithmetic are described by the Bureau of the Fiscal Service: '
      + source('treasuryBills', 'bills, 4 to 52 weeks') + ' and ' + source('treasuryNotes', 'notes, 2 to 10 years') + '. '
      'The written policy these readings belong to is on <a href="brief.html">What decides it</a>; the adjustable version of the template test is on <a href="whatif.html">What-if controls</a>.</p>',
    '04 / recorded history')

WWCA=section('What would change the answer',table(['If this turns out to be true','Then the answer moves toward','Why it moves the answer','Official reference'],[
 ('The trust terms, not the planning premise, control what happens to the residence','A different path (sell, rent or live) from the one assumed','The trust terms are not in any official source here; counsel must read them.',source('notice')),
 ('Basis differs from the date-of-death value (for example, an alternate valuation election)','A different taxable gain on a later sale','The IRS FAQ states the general rule (fair market value on the date of death) and the alternate-valuation exception.',source('basis')),
 ('Family-home relief (Proposition 19) applies to the transfer','Whether the household lives in the home becomes the question for counsel and the CPA','The BOE describes the relief for a principal residence; the conditions are confirmed privately.',source('boe')),
 ('The estate is above the 2026 federal filing threshold of $15,000,000','A federal return and a possible estate tax','Filing and tax depend on the whole gross estate, not just this home.',source('irs706i')),
 ('A crash comes right after a sale','Phasing in over 24 to 36 months, if the entry price matters more than early growth','Phasing changes the price paid for the proceeds; the test is on the Black swans page.',source('fed2008')),
 ('Parking yields fall after the sale','A smaller lead for selling; check the break-even return on What decides it','Proceeds held in short Treasuries earn what the market pays on the day they are reinvested.',source('treasury')),
 ('The recovery after a crash takes years rather than quarters','A longer park-and-phase of the proceeds, and more weight on how many months sit under water than on the ending value','On the Federal Reserve’s record the 1929 high stood for 303 months; the Black swans page prices a peak entry and a parked entry against each other on that shape.',source('fed1929')),
 ]),'00 / first screen')
body=WWCA+'''<section class="section"><div class="card highlight"><div class="eyebrow" style="color:#d1e8b1">Executive summary</div><h2>Do not choose a path until the private facts are verified.</h2><p>This public guide uses synthetic inputs only. Property A is a generic example of a possible trust inheritance; Property B is a generic example of an already-owned rental property. No household value, rent, bill, lease, location identifier or insurance record is loaded into the published model.</p><p><strong>What would change the answer?</strong> Trust authority and title, date-of-death value and tax basis, estate liquidity and prior gifts, eligibility and occupancy under Proposition 19, actual market rent, property-tax bills, insurance quotes, repair needs, transaction costs, tax treatment and the household’s value of living in the home.</p><p><strong>How to use the comparisons.</strong> The tables demonstrate how assumptions change pure and mixed paths. Their rankings are not recommendations. Keep each property’s ownership and tax treatment separate, use the private checklist to obtain verified inputs, and rerun the analysis locally before acting.</p><div class="actions"><a class="button secondary" href="guide/questions.html">See the decision questions</a><a class="button secondary" href="guide/decision.html">Explore the synthetic comparison</a></div></div></section>'''
body+=section('What matters most',table(['Issue','What is known or needs verification','Official reference'],[
 ('Different ownership','Property A is an example of a possible trust inheritance; Property B is an example of an already-owned property. They are separate in the model. Actual title and estate inclusion are private facts.',source('estate','Estate-rule context only')),
 ('Property tax','An eligible family-home transfer may qualify for limited Proposition 19 relief. Renting out A rather than occupying it generally does not satisfy that family-home condition.',source('boe')),
 ('Income-tax basis','Inherited basis is generally date-of-death fair market value, but trust and other exceptions matter. Do not confuse assessed value with income-tax basis.',source('basis')),
 ('Estate tax','Federal exposure depends on the whole decedent’s estate, prior taxable gifts, deductions, credits and elections. Actual headroom is unknown.',source('estate')),
 ('Risk and liquidity','A concentrated home and a portfolio face different risks. Diversification reduces some risks but does not guarantee a profit or prevent loss.',source('invest')),
 ]),'01 / decision context')
body+=section('What the synthetic example demonstrates','''<p>The example model compares the same transfer date and horizon across live, rent, sell, phased-investing and mixed paths. Its output is conditional on invented property values, costs, returns, tax simplifications and stress shapes. It cannot rank a real household’s choices. A real comparison needs private appraisals, tax basis, current bills, insurance and rent evidence, trust terms, occupancy preferences and adviser review.</p><p><a href="guide/brief.html">See the decision boundary, and the questions that could change a real answer →</a></p>''','03 / example finding')

body+=section('Reinvestment risk, beside the headline',REINVEST_OVERVIEW_HTML,'03b / reinvestment')
body+=section('Readiness scorecard',table(['Fact that decides the decision','Status','Who holds the answer','Discovery step','Official framework'],[
 ('Does the trust permit a sale of the residence?','<span class="tag warn">Unverified</span>','Trustee or drafting attorney','<a href="guide/questions.html">Register D01 and D02</a>',source('notice')),
 ('Is the residence titled in the trust?','<span class="tag warn">Unverified</span>','County recorder, trustee','<a href="guide/questions.html">Register D02</a>',source('ownership')),
 ('Will basis step up to date-of-death value?','<span class="tag warn">Unverified</span>','Tax counsel','<a href="guide/questions.html">Register D03</a>',source('trustbasis')),
 ('Is family-home relief available?','<span class="tag warn">Unverified</span>','County assessor, recipient','<a href="guide/questions.html">Register D04</a>',source('prop19')),
 ('Is the estate above the federal filing threshold?','<span class="tag warn">Unverified</span>','Counsel, personal representative','<a href="guide/questions.html">Register D05</a>',source('estate')),
 ('What is the date-of-death value?','<span class="tag warn">Unverified</span>','Qualified appraiser','<a href="guide/questions.html">Register D06</a>',source('basis')),
 ('Do the leases and unit status for Property B hold?','<span class="tag warn">Unverified</span>','Owner files, Rent Board','<a href="guide/questions.html">Register D07</a>',source('sfRent')),
 ('What is the achievable rent floor?','<span class="tag warn">Unverified</span>','Property manager, comparables','<a href="guide/questions.html">Register D10</a>',source('hud')),
 ])+'<p class="tiny">Zero of eight resolved. The rounded figures on the Properties page are owner-stated inputs; none of these document-level facts is verified. Each row links to the register entry that names the exact document, who holds it, and a typical lead time. The register has sixteen entries in total; these eight are the ones that can change the answer.</p>','04 / readiness')

body+='''<div class="callout warning"><strong>Agree the conditions before the figures arrive.</strong> The <a href="guide/precommit.html">pre-commitment register</a> lists, for living, renting, selling and every mixed path, the condition the household writes down and dates <em>first</em>, the falsifier that would void it, and the official rule it rests on. Every threshold on that page is blank on purpose: a public site cannot choose for you, and choosing after seeing one projection is how a decision gets reverse-engineered.</div>'''
body+=section('Explore the guide',cards([
 ('00 / summary','Executive summary','One page: the finding, the four facts that gate it, the figures behind it and the deadlines. Prints on a sheet.','guide/summary.html'),
 ('01 / compare','Live, rent or sell','See assumptions, same-endpoint results and yearly costs on synthetic examples.','guide/decision.html'),
 ('01b / boundary','What decides it','Which inputs flip the ranking, and what would have to be true for a holding strategy to win.','guide/brief.html'),
 ('02 / uncertainty','Black-swan paths','Stress 50 years with inflation, crashes and a disaster; inspect every year.','guide/stress.html'),
 ('02b / evidence','Real conditions','The observed inflation and assessment record, the official projection horizon, and the scenario bands.','guide/conditions.html'),
 ('03 / rules','Tax &amp; inheritance','Separate federal estate tax, income-tax basis, reassessment and trustee steps.','guide/tax.html'),
 ('04 / readiness','Questions to resolve','A prioritized list of missing records, answers and discovery routes.','guide/questions.html'),
 ('04b / pre-commit','Sign before you see the numbers','For each path, the condition to write down first, the falsifier that voids it and the official rule it rests on.','guide/precommit.html'),
 ('05 / improvements','Suggestions to review','Choose or defer ideas without applying them to the site or the analysis.','guide/suggestions.html'),
 ('06 / review','Flagged for review','See the public-repository exposure and other unresolved issues.','guide/review.html'),
 ]),'02 / navigate')
body+='''<section class="section"><div class="callout review"><strong>Privacy boundary.</strong> The published guide uses synthetic examples only; it does not load or publish household records or household-derived values. That does not clean the public repository’s earlier commits, branches, pull requests, caches or copies. A repository administrator must handle visibility and any history remediation. <a href="guide/review.html">Read the incident and limitations →</a></div></section>'''
page('overview','A clearer way to plan for an inheritance.','A source-linked educational guide to comparing inheritance, housing and investment paths. All calculations use synthetic examples; no household records are loaded.',body,home=True)

body=section('Separate the two ownership roles',table(['Placeholder','Role in the example','Private facts that must be verified','Official framework'],[
 ('Property A','Possible trust inheritance; not currently treated as owned by the prospective recipient.','Trust instrument, title, estate inclusion, date-of-death value, tax basis, occupancy and transfer date are not published.',source('trustbasis')),
 ('Property B','Already-owned property; not automatically part of the decedent’s estate.','Title, leases, unit status, rental income, expenses and any estate interest are not published.',source('estate')),
 ]))
body+=section('Property-specific amounts are intentionally blank',table(['Input needed','Property A','Property B','Why it matters','Official verification route'],[
 ('Market value at the relevant date','— private appraisal required','— independent valuation required','Basis, estate reporting, sale proceeds and reassessment depend on the correct date and method.',source('basis')),
 ('Assessed value and property-tax bill','— parcel bill required','— parcel bill required','A reassessment, tax-rate area, bonds and direct assessments affect carrying cost.',source('sccTax')),
 ('Insurance premium and coverage','— binding quote required','— correct landlord/product quote required','A survey is not a policy quote; coverage, exclusions and deductibles matter.',source('cdi')),
 ('Rent and lease terms','— comparable rent opinion required','— leases and rent-roll review required','Vacancy, lawful rent, operating expense and local rules change net income.',source('sfRent')),
 ('Utilities, solar and annual true-up','— bills and tariff required','— bills and tariff required','Usage, tariff, meter allocation and credits must be verified from statements.',source('pge')),
 ('Five-year maintenance and capital costs','— inspection and bids required','— inspection and bids required','Age, condition and large systems drive actual repairs; percentages are only examples.',source('rental')),
 ]))
body+=section('Five-year maintenance and capital plan',table(['Property','Plan item','Planning window','Cost','Decision','Date','Official context'],[
 (prop,item,window,'— quote needed','— not decided','—',source(src))
 for prop,items in [('Property A',[('Roof and drainage','Inspect now; replace by condition','rental'),('Heating/cooling and water heater','Service yearly; replace by condition','rental'),('Plumbing, sewer and electrical','Inspect at transfer','county'),('Foundation, seismic and envelope','Obtain inspection and hazard advice','usgs'),('Solar/inverter and energy system','Confirm tariff and true-up annually','pge')]),('Property B',[('Shared roof and exterior','Inspect now; budget by condition','rental'),('Heating, plumbing and common systems','Inspect and service yearly','rental'),('Life-safety and unit interiors','Inspect and comply with local rules','sfRent'),('Foundation, seismic and envelope','Obtain inspection and hazard advice','usgs'),('Landlord/earthquake coverage','Obtain product-specific quotes','cdieq')])]
 for item,window,src in items
]))
body+='<p class="tiny">No property-specific assessment history, rent, insurance premium, utility amount or repair estimate is published. The annual projection examples on the Compare page are synthetic and must not be substituted for a parcel bill or professional valuation.</p>'
body+=section('City-specific tax schedules need a private parcel match','<p>An official schedule can be shown without estimating any private parcel charge. For a parcel subject to a city tax, first verify its parcel class, taxable area, exemptions and effective date with the relevant agency; the amount remains blank until those facts are established.</p>'+table(['Rule or input','Current published schedule','Parcel-specific amount','Official source'],[
 ('San Francisco Proposition H','Published FY 2027–28 terms; later indexing and sunset rules apply.','— not calculated; parcel type and taxable area must be verified privately.',source('sfMuni')),
 ('Santa Clara County tax-rate area','Base 1% levy plus voter-approved debt and direct charges; exact parcel rate varies.','— read from the actual secured tax bill.',source('sccRateBook')),
 ]))
body+=section('Proposition H: official schedule; Property B amount unverified','<p>The schedule below states the published FY 2027–28 terms. It is not a bill calculation: parcel type, taxable building area, exemptions and effective dates must be checked privately. The actual amount for Property B remains blank.</p>'+table(['Parcel type','Taxable building area','Official annual amount, FY 2027–28','Amount for Property B','Reference'],[
 ('Multifamily residential','Up to 5,000 sq ft','$249','— unverified',source('sfMuni')),
 ('Multifamily residential','Over 5,000 sq ft','$249 plus $0.195 per sq ft over 5,000, capped at $50,000','— unverified',source('sfMuni')),
 ('Single-family residential','Up to 3,000 sq ft','$129','— unverified',source('sfMuni')),
 ('Single-family residential','3,001–5,000 sq ft','$129 plus $0.42 per sq ft over 3,000','— unverified',source('sfMuni')),
 ('Property B','Parcel type and taxable building area not established','Schedule applies only if the parcel qualifies','— unverified',source('sfMuni')),
 ]))
page('property','Property roles and private inputs.','Property A is an anticipated inheritance; Property B is already owned. Private household values and bills are withheld; only synthetic examples are used for projections.',body)
body=section('Property-tax rules',table(['Question','Current rule / limitation','Reference'],[
 ('What changes at transfer?','Change in ownership can cause reassessment. The Proposition 13 factored base year value generally grows by the inflation factor, capped at 2%, absent reassessment or new construction; declining-market relief can apply.',source('prop13')),
 ('When can Proposition 19 help?','Generally an eligible parent-child family-home transfer requires the transferor’s principal residence and the transferee to make it their principal residence within one year and continue occupancy. Special rules apply to other eligible transfers.',source('prop19')),
 ('How much value is protected?','For 16 Feb 2025–15 Feb 2027 the additional allowance is approximately <strong>$1,044,590</strong>, rounded from the official amount. If fair market value exceeds factored base value plus the allowance, the excess is added to the factored value. The Board states the allowance is adjusted every other February 16; a county summary page describes a different cadence, so the Board’s Letters to Assessors govern. Later amounts are unknown; the enacted windows and the carry-forward method are below.',source('allowance')+' · '+source('county')),
 ('Does renting qualify?','Renting the inherited home instead of making it the eligible transferee’s principal residence generally fails the family-home condition. Confirm facts with the assessor.',source('boe')),
 ]))
body+=section('Proposition 19 allowance: enacted windows and how it is carried forward','<p>The value cap is the factored base year value plus the $1,000,000 amount, adjusted. The statute (Cal. Const. art. XIII A §2.1(c)(4), quoted in the Board’s letter) requires the BOE to adjust the $1,000,000 amount for inflation <strong>every other February 16, beginning 16 February 2023, to reflect the percentage change in the House Price Index for California for the prior calendar year, as determined by the FHFA</strong>. The Board publishes each window in a Letter to Assessors. The windows enacted so far, exactly as the Board publishes them:</p>'+table(['Transfer or change-in-ownership date','Applicable $1,000,000 amount, as adjusted','Status','Official source'],[
 ('16 Feb 2021 – 15 Feb 2023','$1,000,000','Enacted window, published in the Board’s letter',source('allowance')),
 ('16 Feb 2023 – 15 Feb 2025','$1,022,600','Enacted window, published in the Board’s letter',source('allowance')),
 ('16 Feb 2025 – 15 Feb 2027','$1,044,586','Enacted window; the letter states the FHFA California HPI change for 2024 was 2.15%, which produced this amount',source('allowance')),
 ('16 Feb 2027 – 15 Feb 2029','— not yet published','The letter states the next adjustment occurs in February 2027. The amount is unknown until the BOE publishes it.',source('allowance')),
])+'<p>Because the transfer is expected decades from now, this site’s projections <strong>carry the allowance forward</strong> from the last enacted amount using the statutory mechanism: one adjustment per two years, indexed to house-price change. The projection basis is the 20-year growth of the FHFA house-price index for the area (about 2.9% a year), which is a labelled assumption, <em>not</em> a published BOE figure. When the BOE publishes each new Letter to Assessors, the enacted amount replaces the projection. The guide’s models use the carried-forward amount in the Proposition 19 formula, and the <a href="questions.html">Questions register</a> records the February 2027 letter as a document to obtain.</p>')
body+=section('Estate, gift and income tax',table(['Item','Official current information','Case-specific amount','Reference'],[
 ('Federal basic exclusion','<strong>$15,000,000</strong> for deaths in 2026; <strong>$15,480,000</strong> in 2027. Prior taxable gifts and an available transferred spousal exclusion may change the available amount.','— unverified',source('estate27')),
 ('Annual gift exclusion, 2026 and 2027','The IRS states the annual exclusion for gifts is <strong>$19,000</strong> per recipient for calendar 2026, rising to <strong>$20,000</strong> for calendar 2027, and that the first that amount given to any one person (other than a future interest) is not included in the total of taxable gifts made during the year — Rev. Proc. 2025-32 §4.42(1) states the 2026 rule, and the 2026 basic exclusion of $15,000,000 comes from the same document. Gifts above the annual exclusion draw on the combined lifetime gift and estate exclusion, and adjusted taxable gifts are added back into the estate filing test.','— prior gifts are a household fact; the annual amounts are official',source('estate27')+' · '+source('rp2532')),
 ('Gifts to a spouse who is not a U.S. citizen','The IRS states a separate, much larger annual exclusion for gifts to a non-citizen spouse: $194,000 for calendar 2026 and $201,000 for calendar 2027. The larger figure is the point: the unlimited marital deduction does not extend to a spouse who is not a U.S. citizen.','— only relevant if it applies; confirm with counsel',source('estate27')),
 ('Filing threshold versus taxable estate','The filing threshold generally tests the gross estate plus adjusted taxable gifts and certain exemption amounts. Deductions are relevant to taxable estate and tax, not a simple subtraction from the gross filing test.','— unverified',source('estate')),
 ('California','The Controller says no California estate-tax return is required for deaths on or after 1 January 2005. Other taxes, and taxes of other jurisdictions if relevant, are separate.','— unverified',source('ftb')),
 ('California income tax on a large gain','California taxes capital gains as ordinary income, with no preferential rate. The 2025 Form 540 rate schedules top out at 12.3% above $742,953 of taxable income (single) or $1,485,906 (joint). A further 1% Behavioral Health Services Tax applies on Form 540 line 62 to taxable income above $1,000,000, for any filing status, and the $1,000,000 threshold is not indexed. The top combined state marginal rate is 13.3% on the part above $1,000,000.','— unverified',source('ftbSchedule')+' · '+source('rtc17043')),
 ('Income-tax basis','Inherited property generally receives date-of-death FMV basis, subject to exceptions and elections. One particular irrevocable grantor-trust fact pattern outside the estate did not receive an adjustment.','— unverified',source('trustbasis')),
 ('Retirement accounts','Taxable inherited IRA distributions may be income to the beneficiary; treatment and timing depend on account and beneficiary rules.','— unverified',source('ira')),
 ('Federal home-sale exclusion','Up to $250,000, or $500,000 for qualifying joint filers, subject to ownership, use and other conditions; it is not automatic.','— unverified',source('residence')),
 ('Like-kind exchange (26 U.S.C. §1031)','The statute covers only exchanges of real property held for productive use or investment for like-kind real property; the replacement must be identified within 45 days and the exchange completed within 180 days (or the return due date). Stocks, bonds and funds are not like-kind real property, so selling and reinvesting in the stock market cannot use this deferral.','— undecided; take advice before selling',source('usc1031')),
 ]))
body+=section('California income tax on a large gain',
    '<p>California taxes capital gains as ordinary income — there is no separate lower long-term-gain rate. Form 540 line 62 adds the Behavioral Health Services Tax: <strong>1% on California taxable income above $1,000,000</strong>, computed on the whole-dollar excess and added on top of the regular rate schedule. The 2025 top bracket is 12.30%, so a large gain that pushes taxable income over $1,000,000 faces up to 13.3% combined on that slice. Exact brackets depend on filing status and year; read the current FTB schedules privately.</p>'
    + table(['Item','Rule as published','Reference'],[
        ('Capital gains treatment','Taxed as ordinary income under the graduated California rate schedule; no preferential long-term rate',source('ftb540')),
        ('Behavioral Health Services Tax','1% of California taxable income above $1,000,000, Form 540 line 62; renamed from Mental Health Services Tax for taxable years beginning on or after 1 January 2025',source('ftb540')),
        ('2025 top bracket threshold','12.30% begins above $742,953 (single), $1,485,906 (married filing jointly), $1,010,417 (head of household)',source('ftbSchedule')),
        ('Sensitivity used in the decision engine','Base 12.30% on a gain (the 12.30% band); sensitivity band 9.30% (the 9.30% band) to 13.30% (the slice above $1,000,000 of taxable income). The engine applies one flat rate, so it does not compute stacked brackets for a specific return.','Set from the FTB 2025 rate schedules and line-62 rule, read 16 Nov 2026. Not a forecast of any household’s tax.'+source('ftbSchedule')+' · '+source('ftb540')),
        ('Combined top marginal rate on a gain over $1,000,000','12.30% + 1.00% = 13.3% on the part above $1,000,000 of taxable income','Computed from the published FTB schedule and line-62 rule; not a separate published rate'+source('ftb540'))
    ])
    + '<p class="tiny">The FTB rate-schedule thresholds are published government amounts and are shown exactly rather than rounded to $10; the $10 rule applies to household and model amounts. The combined rate is a computation from those published figures, not an independently published rate.</p>'
)
body+=section('Future federal exclusion: illustration only','<p>Starting at the official 2027 amount, the numbers below apply an invented 2% yearly growth rate. They are <strong>not IRS forecasts</strong>; actual future law and adjustments are unknown. Estate liability and actual headroom remain blank.</p><div class="table-wrap"><table><thead><tr><th scope="col">Year</th><th scope="col">Illustrative exclusion</th><th scope="col">Actual available exclusion / headroom</th><th scope="col">Context</th></tr></thead><tbody id="estate-projections"></tbody></table></div>')
body+=section('Transfer and sale taxes the county states',table(['Item','What the official page states','Case-specific amount','Reference'],[
 ('Documentary transfer tax','The County Clerk-Recorder states the tax is due on all changes of ownership unless an applicable statutory exemption is cited, computed at 55 cents for each $500 or fractional portion of real property value, excluding liens or encumbrances already of record. On a larger base that is $110 for each $100,000 of consideration, or 0.11%.','— not assumed to apply to a transfer at death until an exemption is cited on the document',source('scc-recording')+' · '+source('rtc11911')),
 ('City add-on','The same county page states that properties located within San Jose, Palo Alto and Mountain View are taxed at triple that rate — $330 for each $100,000 of consideration, or 0.33% — citing R&T Code §11911. Cupertino is not named on that page, and a city add-on is set by ordinance.','— unverified',source('scc-recording')+' · '+source('rtc11911')),
 ('Preliminary Change of Ownership Report','The county states an additional $20 is due if a PCOR is required but is not completed, signed and submitted at recording.','— a filing question for the trustee or transferee',source('scc-recording')+' · '+source('ownership')),
 ('How the tax is computed on the document','The recorded document must indicate whether the tax is computed on the consideration or on the consideration less liens remaining at the time of sale, and the declaration must be signed by the party computing the tax or claiming the exemption.','— procedural',source('scc-recording')),
 ('San Francisco transfer tax','San Francisco administers its own secured property-tax program through the Treasurer. The city transfer-tax rate schedule was not re-read from an official page in this review, so no amount is stated here.','— unverified',source('sfTax')),
]))
body+=section('Law-change watchlist',table(['Measure','Status re-read 16 Nov 2026','Potential relevance','Reference'],[
 ('H.R. 1301 · federal','Re-read 16 Nov 2026 on Congress.gov: sponsored by Rep. Feenstra [R-IA-4], introduced 13 Feb 2025; committee assignment House Ways and Means; the latest action on the page is still the 13 Feb 2025 referral; the tracker reads “This bill has the status Introduced”, and a CBO cost estimate is listed as zero. Proposal, not law.','Would repeal federal estate and generation-skipping transfer taxes if enacted as proposed; recheck before reliance.',source('hr1301')),
 ('SB 284 · California','Re-read 16 Nov 2026 on the Legislature’s site: status “Active Bill - In Committee Process”; House Location: Assembly; last amended 25 Jun 2025; latest history action 14 Jul 2025, “Set, final hearing. Held in committee and under submission.” Its purpose remains amending R&T Code §63.2 and adding §63.2.1. Proposal, not law.','Would amend R&T Code §63.2 and add §63.2.1 on family-home and farm changes of ownership. Existing Proposition 19 remains the model’s framework.',source('sb284')),
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
 ('By applicable federal deadline','Determine if Form 706 is required or desirable for portability; check Form 1041 and final income returns.','An extension to file is not automatically an extension to pay; get advice.',source('estate')+' · '+source('i4768')),
 ('Only after the review','Compare sale, rental and occupancy on equal time horizons and after documented costs and taxes; follow trust authority and local rental rules.','Avoid irreversible action solely on illustrative projections.',source('rental')),
 ]))
page('process','From trust to decision, step by step.','A checklist for a future transfer, not a substitute for the trust instrument, county instructions or professional advice.',body)

questions=[
 ('1','Who owns A, and does the signed trust actually hold title?','Rule known: where an interest transfers by reason of death, including through a trust, the trustee or transferee files the change-in-ownership statement with the county recorder or assessor within 150 days of death; where the property is probated, the statement is filed with the inventory and appraisal. That fixes who must file, not who holds title.','— unverified','Read deed, trust schedule and amendments with the trustee.', 'Changes authority to transfer or sell.','ownership'),
 ('1','What type of trust, what powers and which beneficiaries?','Rule known: a trustee must serve written notification on the beneficiaries and heirs of a deceased settlor within 60 days of specified events, including a revocable trust becoming irrevocable because of a settlor’s death. The trust instrument, not the statute, sets the powers and the distribution timetable.','— unverified','Obtain signed trust and amendments privately; ask counsel about distribution powers.', 'Affects allocation, timing, tax and contest risk.','notice'),
 ('1','Does A qualify for an income-tax basis adjustment?','Rule known: inherited property generally takes its basis in the fair market value at the decedent’s death. Where property is not includible in the decedent’s gross estate, no basis adjustment applies — the IRS so held for the irrevocable-trust fact pattern in Rev. Rul. 2023-2.','— unverified','Ask a tax lawyer to assess title, estate inclusion and trust facts.', 'An unadjusted basis can change the sale analysis materially.','trustbasis'),
 ('1','Was A the transferor’s principal residence and can an eligible recipient occupy it on time?','Rule known: for a parent–child family-home transfer the transferee must make the home their principal residence within one year and claim the homeowners’ or disabled veterans’ exemption within that year, or the exclusion starts in the year the claim is filed. Renting the home out does not satisfy the family-home condition.','— unverified','Document residence and relationship; ask the county assessor about special circumstances.', 'Determines eligibility for family-home reassessment relief.','prop19'),
 ('1','What is the complete gross estate, prior taxable gifts, debts and available spousal exclusion?','Rule known: a return is required only if the gross estate plus adjusted taxable gifts and specific gift tax exemption exceeds the filing threshold, which is $15,000,000 for a 2026 death and $15,480,000 for a 2027 death. Gifts at or below the annual exclusion ($19,000 per recipient for 2026 under Rev. Proc. 2025-32 §4.42(1), $20,000 for 2027) are not counted as taxable gifts at all. Deductions bear on the taxable estate, not on that filing test. California requires no estate-tax return for deaths on or after 1 January 2005.','— unverified','Prepare a confidential estate inventory with advisers; include all relevant interests.', 'Determines filing and estate tax; no actual headroom can be calculated yet.','estate'),
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
 ('2','What is the desired living arrangement and the value of housing services?','Rule known: none — no official source governs this question. It is a household preference. The comparison page does <em>not</em> omit it: the living paths are credited the rent the owner avoids, as a stated and adjustable assumption, and the What-if controls show the same model with that credit removed.','— preference not established','Compare nonfinancial needs, work, accessibility and alternate housing privately.', 'A financial ranking omits the benefit of living in a home.','invest'),
 ('2','How would sale proceeds be invested, and how much liquidity is needed?','Rule known: FDIC insurance covers depositor accounts dollar-for-dollar up to the limit; for a trust owner with five or more beneficiaries that limit is $1,250,000 per owner for all trust accounts held at the same bank. Diversification and asset allocation can reduce risk but do not guarantee returns.','— preference not established','Set an investment policy, risk tolerance and deposit-insurance plan.', 'Returns, tax drag and sequence risk are assumptions, not guarantees.','fdic'),
 ('2','Is a like-kind exchange wanted — and would it even be available?','Rule known: since the 2017 tax act, 26 U.S.C. §1031 applies only to exchanges of real property held for productive use or investment for like-kind real property; the replacement must be identified within 45 days and the exchange completed within 180 days or the return due date. Stocks, bonds and funds are not like-kind real property, so a sale whose proceeds are reinvested in the stock market cannot use this deferral.','— undecided','Take advice before any listing; decide the question in writing first.', 'A like-kind exchange replaces the sell-and-reinvest path with a tax-deferred real-property swap and changes every downstream number.','usc1031'),
 ('3','What laws, valuation and insurance conditions will apply at the event?','Rule known: the official baseline is CBO’s February 2026 outlook for 2026–2036, in which PCE inflation returns to about 2% by 2030. It is a ten-year budget outlook, not a 50-year housing or portfolio forecast, and future law is unknown.','— not knowable yet','Recheck official sources regularly and immediately before a decision.', 'Future law and prices can make today’s model obsolete.','cbo'),
]
priority_counts={p:sum(1 for row in questions if row[0]==p) for p in ('1','2','3')}
open_household=sum(1 for row in questions if row[3].startswith('—'))
rule_settled=sum(1 for row in questions if row[2].startswith('Rule known'))
body='<div class="callout"><strong>How to use this register:</strong> Priority 1 items can overturn the comparison or affect a deadline. The <em>answer already known</em> column states the rule exactly as the official source gives it today. The household’s own answer stays blank here: the rounded cost and assessment figures published on the Properties page are owner-stated inputs, not answers to these trust, tax and preference questions. Do not enter personal answers into the public site.</div>'
body+=section('Can a decision reasonably be made yet?','''<div class="grid three">
 <div class="card"><div class="eyebrow">Priority 1 · gates the decision</div><h3>'''+str(priority_counts['1'])+''' open</h3><p class="muted">Each can change the ranking between sell, rent and live, or miss a filing deadline.</p></div>
 <div class="card"><div class="eyebrow">Priority 2 · changes the numbers</div><h3>'''+str(priority_counts['2'])+''' open</h3><p class="muted">Cost, depreciation and preference inputs that move the result without usually moving the ranking.</p></div>
 <div class="card"><div class="eyebrow">Priority 3 · recheck at the time</div><h3>'''+str(priority_counts['3'])+''' open</h3><p class="muted">Law, prices and conditions that cannot be known now and must be rechecked near the event.</p></div>
</div><p class="tiny">Register totals: '''+str(len(questions))+''' questions — '''+str(priority_counts['1'])+''' / '''+str(priority_counts['2'])+''' / '''+str(priority_counts['3'])+''' by priority — with the household answer still blank on all '''+str(open_household)+''', and a rule-level answer settled from an official source on all '''+str(rule_settled)+'''. Every question below states the rule that is settled today; what is missing is the household’s own facts.</p><div class="callout warning"><strong>Answer: not yet.</strong> A live, rent or sell decision cannot reasonably be made today, because every Priority 1 item is still open and each one is a fact that only the household’s own records and advisers can supply. What is settled is the rule set, which is what makes a private comparison possible at all. Close the Priority 1 items first — the <a href="suggestions.html">suggestions register</a> lists the route for each one. Before the private model is run, also complete the <a href="precommit.html">pre-commitment register</a>: it fixes in writing, and dates, the condition that would make each path the household’s choice, so the outcome cannot be reverse-engineered from one projection.</div>''')
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
 ('D07','1','What are the current leases, occupancy and rent-control status of each unit in Property B?',
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
  'Living there has real value, and this model prices part of it: the living paths are credited the rent the owner avoids (see the What-if controls). Proximity, continuity and everything a rent figure cannot capture are still missing. A financial ranking can be correct and still be the wrong decision.',
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
('S16','Critical','Owner decision: scrub pre-rounding history','Measure first, then decide. Run <code>scripts/privacy-history-audit.py</code> from a <code>git clone --mirror</code> of the repository: it walks every reachable object, applies the working-tree gate’s own rules and prints counts and paths only, never a match. <code>docs/history-remediation-runbook.md</code> then sets out the rewrite across all refs (git-filter-repo 2.47 or newer, a force-push by a repository administrator, a Support request to purge cached views and pull-request references) alongside the option of making the repository private instead. Not run here: it overwrites ~70 shared branches and cannot reach copies outside GitHub.','Only a rewrite removes exact figures from Git objects; a Pages exclusion or a later commit does not. CI now runs the inventory on a full <code>fetch-depth: 0</code> checkout and writes the result into the run summary, which is where a measured answer belongs: on the merged tree it reported pre-rounding blobs that are clean at HEAD and still reachable in history, and zero blobs flagged at HEAD.','github'),
('S17','Critical','Owner decision: remove legacy household files from the tree','Remove, in a reviewed pull request, the older root pages, the dashboard and docs folders, and the research and site data files that still hold household figures. Removal from the tree does not remove history (see S16).','Stops current readers from seeing household figures on main.','github'),
('S18','Critical','Keep all household-derived figures out of the public analysis','Current publication uses synthetic inputs only. Do not restore household values to the public model, even if rounded; use a private, access-controlled analysis instead.','Prevents a financial series from being linked back to a household.','github'),
('S19','Done 17 Nov 2026','Imputed rent for the living paths is now stated and adjustable','Review found that the model had always credited living paths an avoided rent while four pages said it did not. The credit is now a named input (<code>imputed_rent_mo</code>), reported beside the comparison, switchable on the What-if controls, and frozen by <code>scripts/test-imputed-rent.py</code>. Still open: the figure itself is the modelled rent, not an independent rent opinion for a real property.','Living beats selling only when avoided rent passes a break-even; an undeclared credit makes the comparison unauditable, and a missing one makes it one-sided.','hud'),
('S20','High','Switch on the primary-residence exclusion for living-then-sell paths','The engine now has an optional exclusion, default zero so published figures are unchanged. After owner review, set the default, regenerate the examples and re-run the reference test.','Living-then-sell paths are otherwise taxed on the full gain, which overstates tax.','irs701'),
('S21','High','Model Prop H with its official terms','If Property B costs are shown over time, apply the FY 2027–28 schedule, the inflation adjustment from FY 2028–29 and the end on 30 June 2042 that SFMTA publishes. The billing rule (added to the regular property-tax bill, same two installments, from fall 2027) is read.','A flat amount understates later years and ignores the sunset.','sfMuni'),
('S22','Medium','Replace maintenance-as-a-percentage with cost inputs','Maintenance is now a share of market value, which rises with the house and can overstate upkeep on a high-value home. Use contractor quotes and an age-based schedule.','Maintenance is a large line over long horizons; its driver should be a cost, not a price.','rental'),
('S23','Medium','Carry the Proposition 19 allowance forward','Use each BOE letter after 15 February 2027 rather than holding the current amount flat.','The allowance is re-set every other February; a flat figure is a modeling limit.','allowance'),
('S24','Medium','Check the San Francisco tax composition on the bill','Read the secured tax bill and separate the base 1% levy from bonds and direct assessments before modeling Property B.','A tax-to-assessed ratio above the base levy needs an explanation before it is used.','sfTax'),
 ('S25','Critical','Make the repository private, or move the retained analysis out of it','GitHub indexes a public repository at HEAD; excluding a directory from Pages removes it from the site, not from the repository. The 15 Nov 2026 scrub replaced the quasi-identifiers in those files and rounded the household-scale amounts, but the files still narrate the household’s situation in prose, and only removal from the default branch or a private repository ends that.','Closes the last route from a public page to a household record. GitHub states that on GitHub Free a published Pages site is automatically unpublished when a repository becomes private, and that public forks are detached and stay public, so the guide needs republishing from the rewritten repository — one build command, since every page here is generated.','ghVisibility'),
 ('S26','High','Price the transfer tax and recording fees into the sell path','Add the county documentary transfer tax, any city add-on and the change-of-ownership-report question to the cost of selling, and confirm whether a transfer by reason of death is exempt.','Selling carries closing costs the model currently carries as one invented percentage; the county rate is now sourced.','scc-recording'),
 ('S27','High','Diarise the two Proposition 19 claim windows','Put the one-year homeowners’ exemption claim and the three-year BOE-19-P claim in the calendar, with the county form and any supplemental-notice date.','A missed claim window changes the property tax for decades, and it is the deadline the family controls outright.','boe'),
 ('S28','Medium','Run the private model on ranges rather than points','Replace each single assumption with the low and high of the band the Real conditions page now publishes for it, and report both outcomes wherever a single number appears today.','A point estimate invites false precision about an event years away; a band states the uncertainty honestly.','cbo'),
 ('S29','Medium','Move the privacy check to the door, not only to CI','Run scripts/privacy-gate.py in a pre-commit or pre-receive hook so an identifier or an un-rounded amount never reaches a pushed branch.','CI catches the problem after the push, which is when a search index can already see it.','github'),
 ('S30','High','Bucket the per-parcel assessment history, do not only round it','$10 rounding does not defeat an exact-string search when a figure already ends in a zero. Three retained legacy files still print one 2020 assessed value that is a multiple of $10, and a November 2026 verification report printed three raw pre-rounding figures inside the sentence that claimed none were present; the report is now redacted and the gate catches every tracked file. Decide whether a per-parcel series is published at a coarser bucket or not at all.','A year-by-year assessment series identifies a parcel even when each number ends in a zero, and the repository is public and searchable at HEAD.','github'),
 ('S31','High','Write the parking leg into the policy as a ladder, not a rate','Adopt the form the Black swans page now tests: proceeds held in a 3-month/2-year Treasury ladder for 24 to 36 months and phased in over 12, with the note leg sized only for money that will not be needed before month 24.','Bills alone reinvest the whole pot at whatever the crash did to short rates; the tested table shows the gap on the same wait.','treasuryBills'),
 ('S32','Medium','Replace the assumed 2008 regain month with an official series','The entry-risk test carries 66 months as a labelled assumption because no official page re-opened in this review states when the S&P 500 regained its October 2007 level. Find a primary series, record it in the figure ledger and rebuild.','One row of the Black swans page rests on an assumption where the 1929 row rests on the record; the difference should not be invisible.','fed2008'),
 ('S33','High','Write the parking yield as a range in the investing policy, not as today’s rate','The recorded test shows a flat current-rate assumption flatters a 24-month park by about $17,610 per $100,000 at the 2008 entry, because bill yields fell from 1.40% to 0.15% during that parking window. State the policy as a yield band with a reinvestment date, and re-check the published yields at each roll.','A policy written against a spot rate overstates what the parked money will earn exactly when a crash makes parking look attractive.','dgs3m'),
 ('S34','Medium','Choose the parking maturity once, in writing, and stop re-deciding it monthly','On the record, holding parked proceeds at the 2-year note yield rather than rolling 3-month bills changed the ten-year result by at most about $11,620 per $100,000 and by roughly $2,700 at the median, while the entry date moved the result by tens of thousands. Pick one ladder in the policy, note the trade-off, and do not treat it as a market call.','It removes an argument that does not matter from a decision that does, and it keeps the plan from drifting into a rate forecast.','treasuryNotes'),
 ('S35','Medium','Add the entry-year test to the annual re-run','The recommendation-level question is not only what the plan earns but when the money goes in. Each year, re-run the Black swans entry test on the current data extract and record whether the conclusion moved, alongside the property and tax inputs.','Entry timing is the part of the sell path a household controls, and its evidence base changes as history accumulates.','dgs2'),
 ('S36','Low','Decide in writing whether a loss at the worst point is acceptable','The recorded test prices waiting at a median of about −$42,860 per $100,000 over ten years in exchange for a shallower drawdown that only pays off in the minority of entries. Agree the trade-off before the proceeds arrive, so the choice is not made under the influence of whichever month the money lands in.','It is the criterion the phasing decision actually turns on, and it cannot be read off a projection.','invest'),
]
options='<option value="">Not decided</option><option value="consider">Consider</option><option value="defer">Defer</option><option value="decline">Decline</option>'
rows=[(i,priority,title,action,reason,source(src),f'<select data-suggestion="{i}" aria-label="Choice for {i}">{options}</select>','— record decision and date offline') for i,priority,title,action,reason,src in suggestions]
body='<div class="callout warning"><strong>Review before implementation.</strong> These are proposals. Marking a choice stores only the status in this browser; it does not approve work, transmit information, modify the model or implement a change. No personal answers should be entered here.</div>'
body+=section('Suggested paths',table(['Path','What it prioritizes','Trade-off','Reference'],[
 ('Privacy first','Contain old exposure, then keep case-specific work private.','Protects privacy but cannot erase copies already outside control.',source('github')),
 ('Decision first','Verify trust, basis, estate, assessment, rents and insurance with professionals.','Requires private documents and independent quotes; timeline varies.',source('estate')),
 ('Risk first','Run variable inflation, market and disaster paths with explicit exclusions.','Illustrations show sensitivity, not probabilities or forecasts.',source('invest')),
 ('Presentation first','Improve navigation, notes, source checks and accessible comparison tables.','Clarity alone cannot verify unknown inputs.',source('boe')),
 ]))
body+='<div class="control" style="max-width:420px"><label for="chosen-path">Optional path to review (browser only)</label><select id="chosen-path" data-suggestion="PATH"><option value="">Not decided</option><option value="privacy">Privacy first</option><option value="decision">Decision first</option><option value="risk">Risk first</option><option value="presentation">Presentation first</option></select></div>'
body+=section('Suggestions register',table(['ID','Priority','Suggestion','Proposed action','Decision benefit','Reference','Your choice','Decision and date'],rows)+'<p id="save-status" class="tiny" aria-live="polite">Selections, if made, stay in this browser only.</p><button class="button secondary" id="clear-selections" type="button">Clear selections</button>')
body+=AP.suggestions_block(CTX)
page('suggestions','Suggestions to review, not automatic changes.','Consider the options, record a local choice if useful, and choose a path before implementing discretionary improvements.',body)

body=section('Unresolved items',table(['Priority','Issue','Current treatment','Next step','Reference'],[
 ('Critical','Public repository and history exposure','The current public guide was switched to synthetic examples only on 16 Nov 2026. This is not a repository-tree or history scrub: earlier files, commits, other refs, pull requests, caches, forks and clones may still expose household-derived information.','A repository administrator must restrict access and assess history and cached-copy remediation using GitHub’s official guidance. Do not force-rewrite shared refs from this session branch.',source('github')),
 ('Critical','Household figures in the retained legacy tree','Partly closed on 15 Nov 2026. The quasi-identifiers in the root pages, docs, pages, dashboard, site, research and integration folders are now placeholders and every household-scale dollar amount in them is rounded to the nearest $10, but the files remain in the repository as an audit trail and still describe the household’s situation in prose. Pages does not serve them; GitHub still shows them at HEAD.','Owner decision: delete the retained tree from the default branch, or set the repository private. Neither touches Git history, which is the row above.',source('github')),
 ('Critical','Earlier public releases included household-derived financial information','The current public model uses synthetic examples only. Earlier commits, repository files and external copies may still contain sensitive material. Rounding is not anonymization.','Ask a repository administrator to restrict visibility and follow GitHub’s sensitive-data removal guidance; do not restore household data to the site.',source('github')),
 ('High','Actual estate, assets and prior gifts','Unknown; real estate-tax filing and liability headroom are blank.','Prepare a confidential complete inventory with tax counsel.',source('estate')),
 ('High','Insurance and solar','No actual binding premiums, deductible, coverage, tariff or annual true-up are established.','Obtain coverage quotes and utility records privately.',source('cdi')),
 ('High','SF Proposition H and other direct charges','SFMTA publishes the FY 2027–28 schedule and states the measure was approved on 3 November 2026; the election office still labels its own results preliminary. The amount for B is not computable from public information, and the measure is not included in the synthetic B operating table.','Confirm the parcel type and taxable building area privately, check certification after the election deadline, and model the tax before relying on any long-run B figure.',source('sfMuni')+' · '+source('sfElection')),
 ('High','Basis and Proposition 19 eligibility','No trust document, title or eligibility finding was verified.','Obtain written advice from counsel and the assessor.',source('trustbasis')),
 ('High','Scenario output is not a personalized recommendation','Invented model data, flat tax assumptions and omitted depreciation/recapture, financing, estate tax and personal housing value can alter results.','Run a taxpayer-specific comparison privately before acting.',source('rental')),
 ('Medium','Older research contained imprecise estate filing language','The filing test uses gross estate and adjusted taxable gifts, while deductions concern taxable estate and tax.','Use the IRS filing test and a professional, not a simplified headroom subtraction.',source('estate')),
 ('Medium','Future laws, exemption amounts and returns','Future values are assumptions; proposals are not law.','Recheck official law and prices near the decision date.',source('estate27')),
 ('Medium','Local provider and quote availability','The exact water provider and insurance product cannot be determined from a generic area. An owner-occupied multiunit property may have more than one policy option.','Verify address privately and ask insurers for product eligibility.',source('water')),
 ('Medium','Two official pages describe the Proposition 19 adjustment cadence differently','The Santa Clara County Assessor page says the one-million-dollar allowance is adjusted “annually beginning in 2023”. The Board of Equalization says the amount is adjusted “every other February 16”, and Letter to Assessors 2025/009 applied one step for the February 2025–February 2027 period. The guide follows the Board.','Use the Board’s Letter to Assessors for the amount and its date; the assessor’s page is a local summary and should not be read as the governing rule.',source('boe')+' · '+source('county')),
 ('Medium','Form 1041: statute read, instructions not','Closed on the statutory point 15 Nov 2026. 26 U.S.C. §6072(a) sets the due date for a return made under §6012 at the 15th day of the fourth month after the close of the tax year (15 April on a calendar year), and the Timeline now states it. The IRS About Form 1041 page carries no due date, and the instructions were not read, so the fiscal-year end an estate may elect is not published here.','Have the CPA confirm the estate tax year and any extension before the date is diarised.',source('usc6072')),
 ('Medium','Proposition 19 claim periods — closed 15 Nov 2026','The Board’s Proposition 19 comparison chart states “File for homeowners’ exemption within 1 year of transfer” and “File claim for exclusion within 3 years or before transfer to third party”. Publication 801 names the forms — BOE-266 or BOE-261-G for the exemption, BOE-19-P for the exclusion — and adds that a claim filed within six months after a supplemental or escape assessment notice is also timely. Both windows are now dated rows on the Timeline.','Confirm the county’s own filing instructions and the date any supplemental notice is mailed with counsel; the statutory windows are settled, the paperwork is not.',source('boe')+' · '+source('prop19')),
 ('Medium','Santa Clara County installment dates not read from the county site','The timeline uses the state dates in RTC §2617 and §2618. The county page was not re-read, and secondary sites were not used as the source.','Confirm the county’s stated due dates on its official page.',source('county')),
 ('Low','Federal exclusion ledger label conflict — resolved 15 Nov 2026','Both ledger labels are supported: the Form 706 instructions (07/2026) state the basic exclusion amount is $15,000,000 for 2026, and the IRS estate-tax FAQ states the 2026 filing threshold is $15,000,000. Re-read on 15 Nov 2026.','Keep both labels; re-check annually for inflation adjustments.',source('irs706i')),
 ('Medium','Form 706 basic exclusion table and California estate-tax status','Neither was verified in this review. The guide states the federal filing threshold only.','Read the Form 706 instructions table and an official California source before stating either.',source('estate')),
 ('Low','Reinvestment risk: definition captured — closed 16 Nov 2026','The Glossary now defines the term from the SEC page on callable or redeemable bonds, which states the reinvest-at-a-lower-rate risk directly, and the Black swans page prices it on a four-column table of assumed rate paths. The guide does not claim the SEC page defines the term as a heading, and does not quote an official figure for it.','Keep the wording tied to that page. Do not attribute a bond-ladder definition to the SEC that the page does not make.',source('secCallable')),
 ('High','Repository visibility is the real privacy control','The repository is public on GitHub (the API reports private=false as of 15 Nov 2026). The published guide contains no household record, but the retained analysis tree is still indexed by code search at HEAD even though Pages excludes it.','Owner action: make the repository private, or delete the retained legacy tree from the default branch. Both are one click and both are reversible only in part.',source('github')),
 ('Medium','A verified ledger record can still be missing from the page','This review found the figure ledger already carrying a verified three-year Proposition 19 claim deadline while the Timeline still described the period as unconfirmed. The Timeline now publishes it and both carry the 15 Nov 2026 access date.','Process note for reviewers: scripts/check-figures.py guards amounts, not prose, so a page can lag the ledger. Re-read both when an item is closed.',source('prop19')),
 ('Low','County transfer tax published for the first time','The Santa Clara County Clerk-Recorder page states the documentary transfer tax at 55 cents for each $500 of real property value with statutory exemptions to be cited on the document; the Taxes page now shows it, and no amount is asserted for a transfer at death.','Have counsel or the CPA decide whether an exemption applies and cite it on the instrument before recording.',source('scc-recording')),
 ('Medium','The recorded-history entry test cannot reach 1929','The Black swans page now replays the parking decision twice — once on the template shapes with the 1929 return-to-peak month the Federal Reserve states, once on actual prices and actual Treasury yields — but the 3-month constant-maturity series begins on 1 September 1981, so the recorded half covers entry years 1982 to 2016 only. A 1929-style entry has no recorded bill-yield path to be replayed on at all.','Quote only the shape the recorded test can actually reach, and keep the 1929 reading attached to the template and to the Federal Reserve’s own peak and recovery months.',source('dgs3m')),
 ('Medium','Year-end sampling understates within-year swings','The recorded test reads December observations, so 1987 shows a −5.1% year even though the same series fell 26.8% between its August 1987 monthly value and December, and 2008 shows −43.7% against the 57% peak-to-trough fall the Federal Reserve reports.','Read the frequency result from the recorded test and the depth result from the template test; do not combine the two into one number.',source('fed2008')+' · '+source('spIndex')),
 ('Medium','Dividend treatment is an assumption in the recorded test',_rh_div_note,'Settle the total-return convention with the adviser who writes the investing policy, and test the break-even rather than a single rate.',source('spIndex')+' · '+source('invest')),
 ('Medium','Crash shapes are illustrative, not index history — narrowed 16 Nov 2026','The Black swans page now runs the entry-risk test twice: once with growth from the trough at an assumed 4% to 8%, and once with the 1929 index returned to its pre-crash level in November 1954, the month the Federal Reserve states. The path between the anchors is still a smooth geometric interpolation, and the 2008 regain month (66) is an assumption of this site, not a published figure.','If a dated official index series is adopted for the trough-to-peak leg, record it in the figure ledger and rebuild; until then keep both shapes labelled as shapes, not as history.',source('fed1929')+' · '+source('fed2008')),
 ('Medium','Early-crash path and cycle row are assumptions','The first-three-years path on the Black swans page and the 10-year cycle shape are assumptions. The CPI series shows annual rates, not a cycle.','Keep the path labelled as illustrative; do not cite CPI as evidence of a cycle.',source('cpiHistory')),
 ('Critical','Prior property-history material is not included in this guide','The public analysis now uses synthetic examples only. The repository itself may retain earlier property-derived material in files, commits and external copies. No household table is reproduced here.','Restrict repository access and have an administrator assess current files, refs, pull requests, caches and forks.',source('github')),
 ('High','Primary-residence exclusion is not in the public calculator','The public calculator taxes living-then-sell paths on the full gain. The engine now has an optional exclusion, default zero, so published figures are unchanged.','Owner decision on the default (S20).',source('irs701')),
 ('High','Living paths carry an imputed rent — corrected 17 Nov 2026','The 17 Nov 2026 review found that the engine had always credited the living paths the rent an owner avoids, while four pages said the model placed no value on living there. The credit is now a named input, reported beside the comparison and adjustable on the What-if controls; on the default synthetic inputs it is worth ' + f'${PM.round10(IMPUTED["gap"]):,} at 25 years, about {round(IMPUTED["share"] * 100)}% of the live total. What is still missing is the owner’s own figure: the model uses the modelled market rent, not an independent rent opinion or the household’s valuation of proximity and continuity.','Obtain a private rent opinion for the property and agree in writing what occupying the home is worth before the living path is ranked.',source('hud')),
 ('High','Prop H is held flat in the public engine','The guide reports the official FY 2027–28 schedule, but the engine does not index it and does not model the 30 June 2042 end.','Apply the official terms before publishing any Property B cost series (S21).',source('sfMuni')),
 ('Medium','Proposition 19 allowance is held flat in the engine','The current allowance covers transfers through 15 February 2027. Later transfers use a figure not yet published.','Use the BOE letter in force on the transfer date (S23).',source('allowance')),
 ('Medium','Yield observations are date-specific','Treasury yields change daily. The guide cites dated official observations and does not treat them as guaranteed future rates.','Recheck the official series before using an actual investment policy.',source('treasury')+' · '+source('dgs2')),
 ('Medium','Estate exclusion after 2027 is a projection','The engine indexes the 2027 basic exclusion with inflation for later deaths. That is an assumption, not law.','Recheck the IRS figure for the year of death.',source('estate27')),
 ('Medium','Property operating costs are private and unverified','The public model uses synthetic placeholders. Actual maintenance, insurance, water, electricity and rents require private records, inspections and quotes; none is inferred here.','Obtain private bills, insurance quotes and contractor estimates; do not publish them.',source('cdi')+' · '+source('water')),
('Low','The site\u2019s two calculators now answer the same question the same way \u2014 closed 17 Nov 2026','The guide ships two independent models on the same synthetic inputs, and for a while they disagreed: the browser calculator credited the living paths with no housing value, so at a 10-year horizon the workbook made living lead while the browser made selling lead, and the browser\u2019s living path even produced negative wealth at 50 years. Both engines now run the same scenario (4.9% home-price growth, a 6% portfolio return, 5% vacancy, 6% sale cost, 2.62% inflation, and operating cash held at the published 3-month Treasury yield), both credit the living path with the rent an owner avoids, and both value a path that still holds the house at the endpoint as the house at its market value plus the cash it accumulated \u2014 no hypothetical sale, so no gain tax on a sale that is not modelled. They now pick the same leading path at 10, 20, 25, 30 and 50 years, and their dollar figures agree to within about 0.3%.','Keep the gate in CI: `scripts/test-engine-agreement.py` fails if the two ever drift apart again. The differences that remain are structural, not contradictions \u2014 one model compounds monthly and the other annually.',source('hud')+' \u00b7 '+source('invest')),
 ('Medium','Neither calculator charges a property-management cost on the rental path','The published reference engine subtracts vacancy but not management, and the browser calculator now matches it, so the rental path is credited with more cash than a managed letting would deliver. This is an omission of the model, not a finding about any property.','Add a management-cost line to the reference engine and republish, or state the omission wherever the rent path is compared. A real letting carries this cost, so the ranking should not rest on the omission staying invisible.',source('rental')), ('Low','Model conventions','The sale year includes one year of holding costs; break-evens are in inheritance-year dollars; house growth uses the midpoint of two official FHFA series; the equity return is an assumption with no official forecast.','Read the assumptions before reusing any figure.',source('hpi')),
 ]))
body+='<div class="callout review"><strong>History remediation is not complete, and a session branch cannot complete it.</strong> No later commit, no Pages exclusion and no passing scan removes an earlier Git object. This clone is shallow (its <code>.git</code> carries a shallow marker, so only part of the history was fetched), and a partial clone measures only what it holds. The instrument now lives in the repository: <code>python3 scripts/privacy-history-audit.py</code> inventories every reachable object under the same rules as the working-tree gate and prints counts and paths only, never a matched string; run it from a <code>git clone --mirror</code> of the repository for an answer that means something. The written runbook, with the consequence of each option, is <code>docs/history-remediation-runbook.md</code> in this repository, which is not published on this site. GitHub’s own procedure is the authority: '+source('github','sensitive-data removal')+' — rewrite with git-filter-repo 2.47 or newer, read the affected <code>refs/pull/*/head</code> entries, force-push, then ask GitHub Support to remove cached views and pull-request references, because <code>refs/pull/*</code> is read-only and cannot be pushed. Rewriting also discards work other sessions built on the old history, so it is an owner decision made with a freeze, not a cleanup step in a task list. Clones and forks held by other people are outside every one of those steps.</div>'
body+='<div class="callout review"><strong>Read the trade-off before changing visibility.</strong> GitHub states that on GitHub Free for personal accounts and organizations, any published GitHub Pages site is automatically unpublished when a repository becomes private; that a custom domain’s DNS records should be removed or updated <em>before</em> the change, to avoid a domain-takeover risk; and that public forks are detached into a new network and are <em>not</em> made private — '+source('ghVisibility','GitHub Docs on setting repository visibility')+'. This guide is generated from the repository by one build command, so republishing it elsewhere is a rebuild rather than a reconstruction, which is what makes the private-repository option cheaper for a household than it looks. Making the repository private, or removing the retained analysis tree from the default branch, are the two owner decisions on the Suggestions page (S16 and S25); neither is performed by any session.</div>'
body+='<div class="callout review"><strong>Important:</strong> A passing privacy scan cannot prove anonymity or clean previously published history. GitHub warns that commits may remain reachable through pull requests, caches, forks and clones. Do not put personal information, private links or financial documents in this repository.</div>'
body+=AP.review_block(CTX)
page('review','Flagged for review.','Unknown facts, modeling limitations and the remaining public-history privacy incident are visible here; none should be mistaken for a verified value.',body)

sources=[
 ('Property tax','BOE Proposition 19','Qualifying transfers, value cap and timing.','boe'),('Property tax','BOE fact sheet','Move-in, exemption and claim filing details.','prop19'),('Property tax','BOE LTA 2025/009','Exact 2025–2027 allowance and adjustment cadence.','allowance'),('Property tax','BOE LTA 2025/023','Prop 13 assessment and rate mechanics.','prop13'),
 ('Property tax','BOE LTA 2026/026','Proposition 19 exclusion Q&amp;A: claim windows, the six-month supplemental-notice rule, prospective-only relief after the deadlines, and continual-use removal, read 16 November 2026.','lta26026'),
 ('Property tax','BOE 2026 Letters to Assessors index','Confirms 2026/026 is the current published exclusion Q&amp;A and lists the 2026 letters, read 16 November 2026.','boe2026'),('Property tax','Santa Clara County Assessor','Local parent-child claim guidance.','county'),('Property tax','Santa Clara County Assessor · glossary','Tax rate area definition, the 1% maximum basic rate plus voter-approved bonds, and flat direct charges, read 15 November 2026.','asrGlossary'),('Property tax','Santa Clara County Controller-Treasurer · Compilation of Tax Rates FY 2025–26','The rate book itself: 816 tax rate areas for FY 2025–26, the 1% levy plus voter-approved debt example, and every TRA’s exact rate by number, read 15 November 2026.','sccRateBook'),
 ('Federal tax','IRS estate tax','Gross estate, filing threshold and portability. Filing-threshold table re-read 16 November 2026 (2026: $15,000,000).','estate'),('Federal tax','26 U.S.C. §1031 (Cornell LII copy)','Like-kind exchanges: real property only since the 2017 act; 45-day identification and 180-day completion, read 15 November 2026.','usc1031'),('Federal tax','IRS 2027 adjustments','2026 and 2027 exclusion amounts.','estate27'),('Federal tax','IRS Rev. Proc. 2025-32','The 2026 annual gift exclusion of $19,000 per recipient (§4.42(1)), read 16 November 2026.','rp2532'),('Federal tax','IRS inherited property','General inherited basis rule.','basis'),('Federal tax','IRS Rev. Rul. 2023-2','Specific trust and estate-inclusion basis example.','trustbasis'),('Federal tax','IRS home sales','Ownership/use requirements and possible exclusion.','residence'),('Federal tax','IRS rental property','Rental income, depreciation and sale rules.','rental'),('Federal tax','IRS retirement beneficiaries','Inherited account distributions and rules.','ira'),('California tax','State Controller','No California estate-tax return for deaths on or after 1 January 2005; inheritance tax only before 8 June 1982, re-read 16 November 2026.','ftb'),
 ('Federal tax','IRS · Rev. Proc. 2025-32','The published inflation-adjustment procedure carrying the basic exclusion and the GST exemption to $15,000,000 for 2026 and stating the $19,000 annual gift exclusion, re-read 16 November 2026.','rp2532'),
 ('California tax','FTB 2025 Instructions for Form 540','Line 62 Behavioral Health Services Tax worksheet (1% above $1,000,000 taxable income), read 16 November 2026.','ftb540'),
 ('Administration','Probate Code §16061.7','When trustee notification is required.','notice'),
 ('Administration','26 U.S.C. §6072 (Cornell LII copy)','The statutory due date for an estate or trust income-tax return, read 15 November 2026.','usc6072'),
 ('Local recording','Santa Clara County Clerk-Recorder · Recording real estate','Documentary transfer tax rate, exemption citation requirement, and the fee for a missing change-of-ownership report, read 15 November 2026.','scc-recording'),
 ('Local recording','Revenue and Taxation Code §11911','The statute that authorises a county documentary transfer tax and a city add-on at half the county rate, read 15 November 2026.','rtc11911'),('Administration','Revenue and Taxation Code §480','Death-related ownership reporting.','ownership'),('Local context','SF Rent Board','Current allowable increases and proposal notice.','sfRent'),('Local context','SF Treasurer','2026–27 secured property tax rate; direct charges may be additional.','sfTax'),('Local context','SFMTA','Proposition H parcel-tax details.','sfMuni'),('Local context','SF Department of Elections','Preliminary election results.','sfElection'),('Local context','SFPUC','Water and sewer schedules.','sfWater'),('Local context','City of Cupertino','Water service systems.','water'),('Local context','PG&E','Solar billing plan and true-up.','solar'),('Local context','California Department of Insurance','Premium comparison surveys, not quotes.','cdi'),('Local context','CA Department of Insurance','Earthquake coverage and exclusions.','quake'),('Local context','HUD','Small-area fair market rents, not a property quote.','hud'),
 ('Observed series','BLS CPI-U via FRED (CPIAUCNS)','Annual-average inflation record used on the real-conditions page.','cpiHistory'), ('Observed series','FRED · 3-month Treasury constant-maturity yield (DGS3MO)','Recorded annual-average bill yields, 1982 to 2026, used by the Black swans entry test; the series starts 1 September 1981 and was re-read 16 November 2026.','dgs3m'),
 ('Observed series','FRED · 2-year Treasury constant-maturity yield (DGS2)','The other maturity the parking policy names, on the same H.15 basis, re-read 16 November 2026.','dgs2'),
 ('Observed series','FRED · OECD U.S. share price index (SPASTT01USM661N)','Recorded December levels, 1970 to 2025, used by the same test; the December values for 1986, 1987, 2007, 2008 and 2009 were re-read from the official monthly series on 16 November 2026.','spIndex'),('Observed series','Freddie Mac PMMS','Observed 30-year fixed mortgage benchmark.','pmms'),('Observed series','BOE LTA 2026/002','2026-27 Prop 13 inflation factor and the 51-year factor history.','prop13factor'),
 ('Risk','CBO','2026–2036 economic baseline; not a 50-year property forecast.','cbo'),('Risk','BLS','Recorded 2022 CPI and electricity inflation.','bls'),('Risk','FHFA','House-price index data and methods.','hpi'),('Risk','USGS','Bay Area earthquake outlook 2014–2043.','usgs'),('Risk','SEC Investor.gov','Diversification and investing risks.','invest'),('Risk','FDIC','Deposit insurance categories and limits.','fdic'),('Investment','TreasuryDirect bills','Bill maturities, redemption and federal/state/local tax treatment.','treasuryBills'),('Investment','TreasuryDirect notes','2-year notes and marketable security terms.','treasuryNotes'),('Investment','TreasuryDirect pricing','Market-price variation with yield and interest rate.','treasuryPricing'),('Law watch','Congress.gov','Federal H.R. 1301 bill status.','hr1301'),('Law watch','California Legislature','SB 284 status and history.','sb284'),('Privacy','GitHub documentation','Removal, PR references and copies.','github'),
 ('Privacy','GitHub Docs · setting repository visibility','What GitHub states happens to a published Pages site and to public forks when a public repository becomes private, re-read 16 November 2026.','ghVisibility'),
]
body+='<div class="callout">Sources explain law, official benchmarks or decision context. They do not verify a household’s private records or this site’s fictional assumptions. Every link in the register was re-opened and the wording the guide attributes to it was checked on the date recorded for it: 13 or 14 November 2026 for the earlier rows, 15 November 2026 for the rows that review added or closed, and 16 November 2026 for the rows added with the pre-commitment register, the Rev. Proc. 2025-32 row, the recorded-yield and share-price series behind the Black swans entry test, the estate, Form 540 and Proposition 19 pages, and the two GitHub privacy procedure pages, which also carry that date in the public figure ledger. Recheck the underlying documents and date-specific details before relying on them.</div>'
sources+=AP.SOURCES_ADD
body+=section('Source register',table(['Category','Agency or source','What it supports','Official link'],[(a,b,c,source(d)) for a,b,c,d in sources]))
body+=section('How each official figure was checked',table(['Check','What it does','What it does not do','Official context'],[
 ('Machine-readable ledger','Every official rule figure the guide publishes is recorded in a public ledger with its source URL, the exact published value, the form shown on the site, and the date it was re-opened.','It does not prove the value is still current on the day you read it and does not verify any private household fact.',source('estate27')),
 ('Build gate','The build fails if a seven-figure amount appears on a published page without a ledger record, or if a ledger record is marked verified without an official https source.','It cannot detect a value that was verified once and has since changed at the agency.',source('prop19')),
 ('Rounding disclosure','Where a published amount is rounded to the nearest $10, the page says so and the ledger keeps the exact official value so a reader can match it.','Rounding does not anonymize: a multi-year series can be matched even after rounding.',source('prop13')),
 ('Deliberately unverified','An item that could not be confirmed at an official source is left blank on the page and recorded as unverified in the ledger.','It stays open until someone opens the official document and records it.',source('github')),
 ]))+'<p class="tiny">Last full re-read of official sources: 13–16 November 2026, with per-row dates in the figure ledger. The guide states a review date rather than promising currency. Laws, exemption amounts and local rates change.</p>'
body+=section('What is deliberately left blank',table(['Blank item','Why it is blank','Where to find the real value privately','Official context'],[
 ('Market value of either property','No appraisal has been published to this site, and publishing one would breach the privacy rule.','Independent appraisal and comparable sales, kept offline.',source('basis')),
 ('Actual property-tax bill and assessed value','Private and parcel-specific; not published here.','The county secured tax bill for each parcel, reviewed offline.',source('prop13')),
 ('Insurance premium and coverage','A quote is not a public document.','Binding quotes from licensed brokers, including or excluding earthquake.',source('cdieq')),
 ('Rent roll and lease terms','Private contracts.','Signed leases and the local rent board history.',source('sfRent')),
 ('Estate inventory and any estate-tax headroom','The whole estate is unknown.','A confidential inventory prepared with counsel.',source('estate')),
 ('Date-of-death value','An event that has not occurred.','A retrospective appraisal as of the actual date.',source('basis')),
 ])+'<p class="tiny">Each blank is recorded as unverified rather than filled with an estimate. The build fails if a seven-figure official amount appears without a ledger record, and the ledger itself records one item as explicitly unverified rather than guessing.</p>','05 / blanks')
AP.write_js(ROOT)
page('paths','Paths, including mixed ones.','Three pure choices and four mixed paths, compared across four stress tests with break-even points. All figures are synthetic examples.',AP.paths_body(CTX))
page('whatif','What-if controls.','Change the stress test, horizon, parking period, parked-cash yield or equity return and see the effect on each path.',AP.whatif_body(CTX),['guide/data/whatif-page.js'])
page('sources','Sources and verification.','Direct links to official agencies and primary materials, organized by subject for manual review.',body)

body='''<div class="callout warning"><strong>Fictional values, not your household’s figures.</strong> This example was invented for a public site. Its numerical results cannot establish the best personal plan. Official links support the rules or risk context, not the synthetic inputs or projections.</div>'''
body+=section('First: a sale in the year of inheritance','<p>Before any other comparison, the brief asks for the sale that closes in the same tax year as the inheritance. It is modeled first because it fixes the two facts every later figure depends on: the basis and the gain. An inherited home takes a basis of its fair market value at the date of death (the IRS general rule), so a sale in the same year has by construction little or no gain to tax. The line-up below is computed from the same model and controls as the comparison that follows.</p><div class="table-wrap"><table><thead><tr><th scope="col">Line in the same-year sale</th><th scope="col">Amount on the selected assumptions</th><th scope="col">What it is</th><th scope="col">Rule context</th></tr></thead><tbody id="same-year-sale"></tbody></table></div><div class="callout warning"><strong>Three things this line-up does not settle.</strong> (1) Whether a transfer by reason of death is exempt from the county documentary transfer tax is not answered on the county page — confirm before closing (see the Taxes page). (2) A sale whose proceeds are reinvested in the stock market cannot use a like-kind exchange; §1031 reaches only real property exchanged for real property (see the Questions register). (3) If the sale slips into a later tax year, the taxable gain runs from the date-of-death value to the sale price, and the entry-risk question on the Black swans page applies.</div>')
body+=section('Set the example horizon','''<div class="controls"><div class="control"><label for="transfer-year">Illustrative transfer year</label><select id="transfer-year"><option>2040</option><option selected>2045</option><option>2050</option></select></div><div class="control"><label for="hold-years">Years after transfer</label><select id="hold-years"><option>10</option><option>20</option><option>30</option><option>50</option></select></div><div class="control"><label for="home-growth">Illustrative annual home-price growth</label><select id="home-growth"><option value="0.02">2%</option><option value="0.035">3.5%</option><option selected value="0.049">4.9% &mdash; the published FHFA midpoint band</option><option value="0.05">5%</option></select></div><div class="control"><label for="portfolio-return">Illustrative annual portfolio return, net proxy</label><select id="portfolio-return"><option value="0.03">3%</option><option value="0.05">5%</option><option selected value="0.06">6% &mdash; the reference model&rsquo;s nominal equity assumption</option><option value="0.07">7%</option></select></div></div><p class="tiny">Only public, invented assumptions are changed. Nothing is uploaded or saved. <strong>The defaults are the same scenario the published tables on this site run</strong> &mdash; 4.9% home-price growth, a 6% portfolio return, 5% vacancy, 6% sale cost and 2.62% inflation &mdash; so the interactive calculator and the published tables answer the same question on the same assumptions.</p>''')
body+=section('Example inputs and conventions','''<p>Property values, rents and operating costs here are fabricated. Each is a scenario assumption rather than a verified value.</p><div class="table-wrap"><table><thead><tr><th scope="col">Example assumption</th><th scope="col">Illustrative value</th><th scope="col">Why it matters</th><th scope="col">Official context only</th></tr></thead><tbody id="assumptions"></tbody></table></div>''')
body+=section('Compare equal endpoints','''<div id="winner" class="card highlight" aria-live="polite"></div><div class="table-wrap"><table><thead><tr><th scope="col">Strategy</th><th scope="col">Initial investable proceeds</th><th scope="col">First-year cash / portfolio change</th><th scope="col">Value at endpoint</th><th scope="col">Calculation / rule context</th></tr></thead><tbody id="comparison"></tbody></table></div><p class="tiny"><strong>One question, one convention, two calculators.</strong> The published tables on this site come from a monthly model that simulates cash flow month by month; the interactive calculator above is an annual model. They now run the same scenario and the same two conventions: both credit the living path with the rent an owner avoids by occupying the home, and both value a path that still holds the house at the endpoint as <em>the house at its market value plus the cash it accumulated</em> &mdash; no hypothetical sale, and therefore no gain tax charged on a sale that is not modelled. On these inputs the two calculators pick the same leading path at every horizon. The published tables govern; the calculator is for exploring inputs. ''' + IMPUTED_NOTE + '''</p><p class="tiny">Sale proceeds earn a constant after-tax return proxy; there is no additional portfolio liquidation tax. Retained-property cash flows are accumulated using the same proxy. Sell’s first-year figure is a portfolio-value change proxy, not spendable distributions. Living costs are treated as funded externally and compounded. <strong>No estate-tax allocation is included</strong>, and neither calculator charges a property-management cost on the rental path &mdash; a known omission of the reference model, published on the Flagged page rather than hidden in one engine. These omissions can change the ordering.</p>''')
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
body+=section('Distribution of outcomes across stress tests','<p>Each cell opens the single number in the comparison above into the scenario band it came from: the best of the four stress tests, the worst, and the spread between them. A wide spread means the path is exposed to which economic conditions arrive; a narrow spread means the conditions change the answer less. All values are model outputs on the synthetic example inputs, rounded to the nearest $10. None of them is a forecast and no probability is attached to any scenario.</p>'+AP.distribution_body(CTX)+'<p class="tiny">Scenarios: baseline, a 1929-style crash, a 2008-style crash and 1970s-style stagflation, taken from the same grid as the comparison above and the chart on the <a href="paths.html">Paths page</a>. A horizon is years after the modelled transfer. The Black swans page tests every year of the 50-year path under each shock, and its ladder test prices the wait for proceeds that come from a sale.</p>','Distribution')
page('decision','Compare the options, not just a number.','A transparent illustrative live-versus-rent-versus-sell comparison on synthetic inputs, with year-by-year example property and operating-cost tables.',body,['guide/data/model.js','guide/data/decision-page.js'])

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
body+=PEAK_SECTION_HTML
body+=RECORDED_SECTION_HTML

body+=section('Audit every year','''<p>Expand a path to inspect all 50 annual rates and outputs. The model caps annual factor growth at 2% and uses the lesser of market value and factored base as a simplified decline-in-value proxy; actual lien dates, assessment appeals, new construction and supplemental bills are not modeled. The disaster repair is charged to both property-holding strategies. Each portfolio rate is a hypothetical net proxy with no separate liquidation tax. Income tax on positive rental cash is a flat scenario; depreciation and recapture are omitted.</p><div id="stress-years"></div>''')
page('stress','A straight line is not a forecast.','Five variable 50-year scenarios put inflation, investment returns, housing cycles and an uninsured disaster into the same comparison. A second entry-risk test parks the proceeds in a 3-month/2-year Treasury ladder and runs it against a 1929 recovery shaped by the official record.',body,['guide/data/model.js','guide/data/stress.js','guide/data/stress-page.js'])

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
_ASSUMPTION_ROWS=[
 ('Home-price growth for the inherited residence','4.9% a year in the invented example &mdash; the published FHFA midpoint band the monthly engine uses &mdash; applied to both market value and the sale price','0% to 7%, the span the Compare and What-decides-it grids run. No official body publishes a growth rate for one house; FHFA regional indexes are the closest published measure and they are not a parcel forecast.','Market value each year, and the sale proceeds in every path.',source('hpi')),
 ('Growth of the factored base year value','2.0% a year','Exactly the statutory cap, and the only assumption on this page that is a rule rather than a guess. Across the 51 published adjustment years the factor reached the 2% cap 40 times of 51, was lower in the other 11, and fell below 1.0 once, compounding to about 1.81% a year.','Assessed value and therefore the property-tax line while the base stays protected.',source('prop13factor')),
 ('Cost and expense inflation','3.0% a year','Annual CPI-U change 1991 to 2025 averaged 2.62% with a range from −0.36% to 8.00%, above 3% in 10 of 35 years. CBO’s February 2026 baseline has PCE inflation back near 2% by 2030 and stops at 2036, so it says nothing about 2045 or 2050.','Water, insurance, maintenance and repair lines in every annual table.',source('cpiHistory')+' · '+source('cbo')),
 ('Rent growth','3.0% a year on the invented residence','Two published anchors bound it rather than set it: HUD small-area fair market rents are recomputed each fiscal year by formula, and San Francisco’s Rent Board states a 1.6% general adjustment for covered units from 1 March 2026 to 28 February 2027, with a 6% cap and a 10 percent banked-credit rule under its ordinance.','Rent income in the rent and mixed paths.',source('hud')+' · '+source('sfRent')),
 ('Net portfolio return','5.0% a year after tax and fees','0% to 10%, the range tested on the What-decides-it page, because the break-even is the finding rather than the rate. No official source publishes a household’s future net return; the SEC’s guidance is that diversification reduces some risks and guarantees none.','The terminal value of the sale path and of any proceeds parked in Treasuries.',source('invest')),
 ('Yield on parked proceeds','4.32% flat, the observed 3-month Treasury par yield on 13 Nov 2026','1% to 5% on the Black swans page, with the observed 3-month and 2-year yields of 4.32% and 4.88% as the middle of that span. The record is wider and state-dependent: annual averages of the same 3-month series ran from 11.09% in 1982 to 0.03% in 2014, and fell to 1.40% then 0.15% across the 2008 and 2009 calendar years, so a parked portfolio earns least in the years a crash makes parking look attractive. The recorded test on the Black swans page prices that difference at about $17,610 per $100,000 at the 2008 entry.','Every Treasury-parking and phasing result.',source('treasury')+' · '+source('dgs3m')+' · '+source('treasuryBills')),
 ('Return on the stock legs of a phased entry','5.0% a year net in the comparison; a 2.0-point-a-year dividend assumption on top of the price index in the recorded entry test','The index the recorded test uses is a price index and excludes distributions, so any total-return number is an assumption rather than an official figure; the test shows the median cost of waiting moving from −$23,130 with no dividend, to −$40,190 at 2.0 points, to −$62,280 at 4.0 points. CBO’s baseline publishes rates to 2036 and nothing about the 2040s or 2050s.','The ranking of invest-now against park-and-phase, and the sale path at every horizon.',source('spIndex')+' · '+source('cbo')),
 ('Vacancy and management','7% vacancy and 8.5% of gross rent','No official statistic exists for either. They are invented, and the what-if controls are the honest way to change them; a real number comes from a rent roll and a management proposal, not from a public page.','Net rental cash flow before income tax.',source('rental')),
 ('Maintenance and repair','0.75% of value a year on the house, 1.25% on the two-unit building','The official material governs deductibility, not the amount: repairs are deductible while the property is held for the production of income, and capital work is generally depreciated. A reserve study or inspection, not a percentage, sets a real figure.','Operating cost in the rent and live paths, growing with modeled value.',source('rental')),
 ('Insurance premium','$2,800 and $3,000 a year in the invented example','The Department of Insurance publishes premium comparisons for hypothetical profiles and states plainly that they are not quotes and that a consumer must obtain a quote. Standard homeowners forms generally exclude earthquake damage, with a separate CEA market. No premium is verified for any real property here.','Holding cost in every path, doubled in the stagflation and disaster scenarios.',source('cdi')+' · '+source('quake')),
 ('Water, sewer and electricity','$200 a month on the house; $220 water and $100 electric on the building','Cupertino runs three separate water systems, so no city-wide monthly figure is defensible; SFPUC publishes a per-hundred-cubic-foot schedule with sewer charges set by another ordinance, and both change annually. Rates are published; a bill is not.','The utility lines of the annual tables.',source('water')+' · '+source('sfWater')),
 ('Value of a solar credit','Zero in the invented example, deliberately','PG&E states that the Solar Billing Plan produces a monthly statement and an annual True-Up, and that the tariff a system keeps depends on when it was authorised to operate. A recent interconnection can therefore be a cost as easily as a credit; a pre-2023 NEM account is a different case.','The net utility line for a property with an interconnection.',source('solar')),
 ('Proposition 19 allowance','The official amount for the current period, indexated forward on an invented path','Published exactly for 16 February 2025 to 15 February 2027 and adjusted every other 16 February; the amount after February 2027 is not knowable, so the forward path is labelled an assumption.','The assessed base that survives a qualifying family-home transfer.',source('allowance')),
 ('Estate-tax threshold and California tax','$15,000,000 for a 2026 death and $15,480,000 for a 2027 death; no California return for deaths on or after 1 January 2005','Both federal amounts are published; the 2028 path is indexation applied by this site, not the IRS. H.R. 1301 would repeal the federal tax and has not advanced past referral, so the site keeps the current-law number and flags the proposal.','Whether a federal return is filed and whether liquidity is needed at all.',source('estate27')+' · '+source('ftb')+' · '+source('hr1301')),
 ('Income-tax rates on the result','30% ordinary and 25% capital gains, flat','California’s 2025 rate schedules top out at 12.3%, beginning above $742,953 for a single filer and $1,485,906 for a joint filer. Federal long-term gains plus the net investment income tax can reach 23.8% before any state tax. A flat pair of rates is a teaching device: the real number depends on the filer, the year and the other income.','Tax drag on rental cash and on the gain in the sale path.',source('ftbSchedule')+' · '+source('cg409')+' · '+source('niit559')),
]
body+=section('Every invented assumption, against the range the record supports','<p>The comparison pages run on numbers this site invented. The table is the honest version of those inputs: what the model uses, what the official record actually spans, and which of them cannot be answered from any public source at all. Where the third column says no official figure exists, that is a private-document question, and the first register on the Questions page lists the document to obtain.</p>'+table(['Assumption','Value used in the invented example','Range or figure the official record supports','Where it is used','Source'],_ASSUMPTION_ROWS))
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
body+=section('Agree the rules in writing before the figures arrive','<div class="callout"><strong>Why this section comes before the grids.</strong> A criterion chosen after seeing one projection is reverse-engineered from that projection. The household should agree, in writing and in advance, what would make it choose each path — then compare the figures against rules it already accepted. This page is the template; the signed record stays offline. Write the decision and the date beside each item, so a future reader knows what was chosen and why.</div>'+table(['Path','Rule to agree in writing first','Decision','Date','Official reference'],[
 ('Sell and reinvest','Agree the threshold in advance: choose this path if its after-tax value at the agreed horizon leads the best holding path by more than an agreed margin (for example 15%), and no non-financial reason below applies.','— not decided','—',source('invest')),
 ('Rent it out','Agree the rent floor in advance: rent only if written local comparables clear the break-even rent the model publishes, and only if the household accepts the landlord duties and local rules.','— not decided','—',source('hud')),
 ('Live in it','Agree the occupancy commitment and the monthly value of living there <em>before</em> the tables are shown; family-home relief depends on occupying the home as a principal residence, and the model credits the rent an owner avoids by living there — an assumption you can change, not a valuation of the home to you.','— not decided','—',source('boe')),
 ('Mixed paths','Agree the test period in advance (for example: live two years, then re-run the sell-threshold test on facts, not on hope). A mixed path without a pre-agreed review date is just hesitation.','— not decided','—',source('boe')),
 ('Like-kind exchange instead of selling','Decide in writing whether a §1031 exchange is wanted before any listing; it replaces the sell-and-reinvest path with a tax-deferred real-property swap and does not reach stocks.','— not decided','—',source('usc1031')),
 ('Override: the trust decides','If the trust requires or forbids a sale, this charter yields to the instrument. No threshold above overrides a trustee’s actual powers.','— not decided','—',source('notice')),
 ('Override: estate liquidity','If the estate is above the federal filing threshold, agree now that a liquidity plan takes priority over any holding preference; estate tax can force a sale regardless of the arithmetic.','— not decided','—',source('estate')),
 ]))
body+=section('Documented investing policy for the sale proceeds','<p>The sale proceeds should not sit in one account or be moved all at once into stocks. A written policy, agreed before the money arrives, keeps the decision from being reverse-engineered from a single projection:</p>'+table([
    'Policy element','What it says','Why it matters','Official reference'
],[
 ('Parking the proceeds','Hold the net sale proceeds in short U.S. Treasury securities while the trust, basis and Proposition 19 facts are confirmed — as the tested policy, a ladder: part in three-month bills, part in a two-year note held to maturity sized only for money not needed before month 24. Do not leave them in an uninsured or non-interest-bearing account.','Short Treasury maturities return principal at known dates; maturing cash must be reinvested at then-available yields (reinvestment risk), which the parking table on the Black swans page prices for a 24- and a 36-month wait.',source('treasuryBills')+' · '+source('treasuryNotes')+' · '+source('treasuryPricing')),
 ('Phasing into stocks','Move into a diversified portfolio gradually rather than at one price. A phased entry softens a 1929- or 2008-style crash at the entry point; the cost is lower growth in a sustained rally. Read the cost beside the months under water, not only the terminal value: the 1929 record is a 303-month wait to regain a high, which a single ending number hides.','Phasing changes the price paid for the proceeds; it is a choice about which risk to carry, not a forecast. Both readings are on the Black swans page.',source('fed1929')+' · '+source('fed2008')),
 ('Diversification','Do not concentrate the proceeds back into a single home or a single holding. Spread across asset classes and keep the rentals and any inherited home as only part of the total portfolio.','Diversification can reduce certain risks but neither guarantees returns nor prevents loss.',source('invest')),
 ('Liquidity first','Keep enough in insured deposits or short Treasury bills to cover taxes, insurance, maintenance and any estate-liquidity need before committing the rest to markets.','Insured deposits are protected up to the statutory limit per institution per ownership category.',source('fdic')),
 ('Review annually','Re-run the model every year with updated inputs, costs and law changes. A policy set once is not a plan kept.','Changing growth, inflation, tax and rent figures can move the ranking.',source('cbo')),
]))+'<p class="tiny">This is a policy template, not advice. Each element should be confirmed with an adviser and written down with a date before the proceeds arrive.</p>'
body+=section('The answer is decided by four inputs, not forty',table(['Input','Range tested on this site','Where the answer sits','What it means for effort','Official framework'],[
 ('Whether the trust permits a sale','Not a number. A legal fact.','If the trustee cannot or must not sell, every other input is irrelevant.','Resolve first. See the discovery register, D01 and D02.',source('notice')),
 ('Whether basis steps up','Not a number. A legal and factual test.','An immediate sale is low-tax with a step-up and heavily taxed without one.','Resolve second. See D03.',source('trustbasis')),
 ('Whether family-home relief applies','Occupancy, timing and filing conditions.','Without relief the assessed base resets to market value; on the invented 2045 example that raises the first-year property tax by about half.','Resolve third. See D04.',source('prop19')),
 ('Portfolio return versus home growth','Return: 0% to 10%. Growth: 0% to 7%.','Selling leads once the net portfolio return clears roughly 3%, at every growth rate tested.','This is the input most reports argue about, and on this model it matters least.',source('pmms')),
 ])+'<p class="tiny">The last row is the finding worth reading twice: the portfolio rate that makes selling lead is low and stable across home-price growth, because the holding strategies are carrying a large reassessed tax bill plus upkeep. Arguing about 3% versus 5% home appreciation changes far less than establishing whether a step-up or relief applies.</p>')

body+=section('Decision boundary: which strategy leads', '<p>The grid below runs every combination of home-price growth and net portfolio return the comparison page exposes, for a 24-year hold after a 2045 transfer. Each cell shows the leading strategy for that pair of assumptions. The point is the shape, not any single cell.</p><div class="grid four" style="margin-bottom:1rem"><div class="control"><label for="be-year">Illustrative transfer year</label><select id="be-year"><option>2040</option><option selected>2045</option><option>2050</option></select></div><div class="control"><label for="be-horizon">Years after transfer</label><select id="be-horizon"><option>10</option><option selected>24</option><option>50</option></select></div></div><div class="table-wrap"><table><thead id="boundary-head"></thead><tbody id="boundary-body"></tbody></table></div><p class="tiny">S = sell and reinvest, R = rent then sell, L = live then sell. Every cell is a separate run of the model. No estate tax, financing, depreciation or recapture is modeled, and the value of occupying the home is an assumption the grid holds at the modelled rent, so the boundary is a teaching illustration rather than a boundary for a real household.</p>')

body+=section('Break-even return by home-price growth','<p>Read this as: at a given assumption about home prices, how strong does the portfolio have to be before selling leads? A low threshold means selling is robust to a weak market in the assumptions.</p><div class="table-wrap"><table><thead><tr><th scope="col">Assumed annual home-price growth</th><th scope="col">Net portfolio return at which selling starts to lead</th><th scope="col">Interpretation</th><th scope="col">Context only</th></tr></thead><tbody id="threshold-body"></tbody></table>')

body+=section('Which assumption actually flips the answer','<p>Each row moves one assumption away from the middle of its range and holds the other constant. A row that changes the leading strategy is an input the decision is genuinely sensitive to; a row that does not is an input a report can stop arguing about.</p><div class="table-wrap"><table><thead><tr><th scope="col">Assumption moved</th><th scope="col">Value tested</th><th scope="col">Leading strategy</th><th scope="col">Does the answer change</th><th scope="col">Context only</th></tr></thead><tbody id="sensitivity-body"></tbody></table>')


def _middle_case(growth: float = 0.035, ret: float = 0.05, horizon: int = 24) -> dict:
    """The middle of the boundary grid's range, computed by the published monthly engine.

    3.5% home-price growth and a 5% portfolio return, 24 years after a 2045 transfer — the
    same pair the grid marks as its reference case. Nothing here is typed in: the figures
    are produced by the engine that produces the published tables, so the prose and the
    tables cannot drift apart.
    """
    p = dict(AP.ACTIVE_PARAMS)
    p['g_pre'] = growth
    p['g_post'] = growth
    p['mu_equity'] = ret
    out = {}
    for path, label in (('sell_lump', 'Sell'), ('rent', 'Rent'), ('live', 'Live')):
        out[label] = AP.M.simulate(path, 'base', p, AP.ACTIVE_A, horizon)
    return out


def _breakeven_return(growth: float = 0.035, horizon: int = 24) -> float | None:
    """The portfolio return at which selling starts to lead, at the given home-price growth."""
    def gap(r: float) -> float:
        p = dict(AP.ACTIVE_PARAMS)
        p['g_pre'] = growth
        p['g_post'] = growth
        p['mu_equity'] = r
        live = AP.M.simulate('live', 'base', p, AP.ACTIVE_A, horizon)['total']
        sell = AP.M.simulate('sell_lump', 'base', p, AP.ACTIVE_A, horizon)['total']
        return live - sell
    lo, hi = 0.0, 0.15
    if gap(lo) * gap(hi) > 0:
        return None
    for _ in range(60):
        mid = (lo + hi) / 2
        if gap(lo) * gap(mid) <= 0:
            hi = mid
        else:
            lo = mid
    return (lo + hi) / 2


MC = _middle_case()
MC_BE = _breakeven_return()

body+=section('The comparison in the middle case',table(['Measure, invented example','Sell','Rent','Live','What the gap is','Official context'],[
 ('Value at the endpoint, 24 years after a 2045 transfer',AP.money(MC['Sell']['total']),AP.money(MC['Rent']['total']),AP.money(MC['Live']['total']),'Holding strategies pay reassessed property tax plus upkeep from the first year; the sale proceeds compound without either. The living path is credited the rent an owner avoids by occupying the home, at the modelled rent.',source('prop13')),
 ('Cash in the first full year','Portfolio change, not a distribution','Negative before income tax','Negative before income tax, but less negative than renting, because the rent avoided is credited','A rental whose rent is below its cost structure is a cost, not an income.',source('rental')),
 ('What the model leaves out','Basis risk if no step-up applies','Value of a future step-up is not credited; depreciation and recapture omitted','The imputed rent is an assumption you can change, not a valuation of the home to you; family-home relief is not valued','The omissions are asymmetric: they could favor either holding strategy.',source('trustbasis')),
 ]))

body+=section('What would have to be true for a holding strategy to lead',table(['For renting to lead','For living there to lead','Official context'],[
 ('Nothing in the grid does: over a 24-year hold the rental path is the weakest of the three at every combination of home-price growth and portfolio return the grid runs. Rent would have to clear the break-even floor on the real-conditions page before the arithmetic could even be close.','The net portfolio return has to stay below about ' + (pct(MC_BE) if MC_BE is not None else 'the break-even shown on this page') + ' at 3.5% home-price growth and a 24-year hold, or selling takes the lead. In the observed inflation record, a nominal return below that is a weak outcome over 24 years, but it is not impossible. Living must also be valued at more than its modeled cash cost, and family-home relief must actually apply, otherwise the tax gap widens each year.',source('invest')),
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
 ('Like-kind exchange (§1031)','An exchange of real property held for productive use or investment for like-kind real property, on which federal gain is not recognized. The replacement must be identified within 45 days and the exchange completed within 180 days (or the return due date). Stocks and funds are not like-kind real property.','Decides whether a sale can defer gain instead of paying it. Selling to reinvest in stocks cannot use it.',source('usc1031')),
 ('Peak-to-trough decline','The fall from a market\u2019s highest level to its lowest level before the next recovery. Example: the 1929 decline the Federal Reserve reports as 89 percent.','The measure used to build the 1929 and 2008 crash shapes.',source('fed1929')),
 ('Probate Code §16061.7 notice','A trustee notice to beneficiaries and heirs, due not later than 60 days following the triggering event, subject to the section\u2019s exceptions.','Sets the notice clock that runs in parallel with the estate and tax filings.',source('notice')),
 ('Reassessment','Setting a new taxable value for property. The BOE guidance states that a family home that stops being the owner\u2019s principal residence receives a new taxable value.','The step that can move the property-tax line sharply after the transfer.',source('boe')),
 ('Tax rate area (TRA)','A specific geographic area all of whose territory lies within the same combination of local agencies for the fiscal year. Santa Clara County has over 3,200 TRAs, each with a unique number and its own total rate.','The parcel’s TRA decides which voter-approved debt rates are added to the 1% base rate on the bill.',source('asrGlossary')),
 ('Residential rental property','IRS Publication 527 is titled Residential Rental Property; the guide does not restate its rules.','Relevant to Property B, which the planning premise treats as rented.',source('rental')),
 ('Treasury par yield (Constant Maturity)','The yield the U.S. Treasury publishes for a given maturity, derived from the daily par yield curve. Used here for the 3-month and 2-year rates.','The observed parking yields on 13 November 2026 come from this series.',source('treasury')),
 ('Reinvestment risk','The risk that money which becomes available later has to be put to work at a lower rate than it was earning. The SEC states it for an investor whose bond is called early: they are "often faced with reinvesting the money at a lower, less attractive rate".','A ladder of three-month bills is exposed to this in exactly the way a two-year note held to maturity is not. The two middle columns of the parking table on the Black swans page are the risk, priced.',source('secCallable')),
 ('Treasury ladder (bills plus a note)','Holding part of the cash in short bills that reprice every quarter and part in a longer note held to maturity, so some money is always coming back and part of the rate is always locked. TreasuryDirect sells bills for four to 52 weeks and notes for 2, 3, 5, 7 or 10 years.','The investing policy on What decides it and the parking table on the Black swans page both use a 3-month/2-year split.',source('treasuryBills')+' · '+source('treasuryNotes')),
 ('Months under water','The count of months in which a portfolio is worth less than the amount put into it. A terminal value reports where you ended; this reports how long you had to wait to get there.','The entry-risk table on the Black swans page uses it, because the 1929 record is a 303-month wait to regain the high rather than a shallow dip.',source('fed1929')),
 ('Return-to-peak recovery shape','A stress shape in which the index is returned to its pre-crash level at the month the record says that happened, and only then grows at an assumed rate — instead of growing away from the low at that rate all along.','It is the second version of the entry-risk test, and it is what turns 1929 from a decline into a duration.',source('fed1929')+' · '+source('fed2008')),
]

body=section('Terms used in this guide',table(['Term','Plain meaning','Why it matters here','Official source'],[(a,b,c,d) for a,b,c,d in GLOSSARY])+'<p class="tiny">Each term links to an official page. Definitions are plain-language summaries of the page named in the source column, not legal advice. Reinvestment risk, the ladder, the under-water count and the two recovery shapes were added to this glossary on 16 November 2026 with the official pages they rest on.</p>')
page('glossary','Plain words for the decision.','Terms that recur across the guide, each with the official page it comes from. Use them to read the Compare, Black swans and Trust steps pages.',body)

# ---- Timeline: dated deadlines in order, each opened on an official page on 14 Nov 2026 ----
body=section('When each deadline falls',table(['When (from the event)','Deadline or event','Who acts','Why it matters here','Official source'],[
 ('Day 0 · date of death','Valuation date for the federal estate accounting and the date-of-death value used for basis.','Executor or trustee; qualified appraiser','Every later figure in the Trust steps depends on documenting this value.',source('estate')+' · '+source('basis')),
 ('Within 60 days following the triggering event','Trustee notification to beneficiaries and heirs (Probate Code §16061.7(f)), subject to the section’s exceptions.','Trustee','Runs on its own clock. Not every trust triggers it; the guide does not assume that it does.',source('notice')),
 ('Within 150 days after death','Change-in-ownership statement for real property transferred by reason of death, including through a trust (RTC §480(b)).','Trustee, or transferee, with the county recorder or assessor where the property lies','The relevant county filing depends on the property location and title; confirm the county and form with counsel.',source('rtc480')),
 ('Within 9 months after death','Form 706 due, if a return is required. The estate and GST taxes are due within 9 months of the date of death. Form 4768, filed by that original due date, gives an automatic 6-month extension of time to file. A separate Form 4768 request under Part III extends the time to pay; an extension to file does not extend the time to pay.','Executor, with the CPA','Required only above the federal filing threshold ($15,000,000 for a 2026 death). Interest runs on estate tax not paid by the original due date, whether or not an extension is granted.',source('irs706i')+' · '+source('i4768')),
 ('Each year: 1 November, first installment','Property-tax first installment for the secured tax year. Delinquent after 5 p.m. on 10 December, with a 10 percent penalty.','Owner or trustee','Applies to the bill on either property. The bill amount is not in this guide because it is a private figure.',source('rtc2617')),
 ('Within 1 year after the transfer','File for the homeowners’ exemption on the family home received by a parent or child (BOE-266 or BOE-261-G) and occupy it as a principal residence. The Board’s comparison chart states the one-year period; Publication 801 states that a later claim starts the exclusion in the year it is filed.','Transferee, with the county assessor','Missing it does not void the transfer; it delays when the protected base year value begins, and the value limit applies from the start. Re-read 15 Nov 2026.',source('boe')+' · '+source('prop19')),
 ('Within 3 years after the transfer, or before a transfer to a third party','File Form BOE-19-P, the claim for the parent-to-child reassessment exclusion, with the county assessor. The Board states the same three-year period, and Publication 801 adds that a claim filed within six months after a supplemental or escape assessment notice is also timely.','Transferee, with the county assessor','A late claim can still grant relief but only from the year it is filed. Re-read 15 Nov 2026.',source('boe')+' · '+source('prop19')),
 ('15th day of the 4th month after the tax year closes','Form 1041, the income tax return of the estate or trust. 26 U.S.C. §6072(a) sets that date: 15 April for a return made on the basis of the calendar year, and the 15th day of the fourth month after the close of a fiscal year.','Fiduciary, with the CPA','An estate can choose a fiscal year that ends up to twelve months after death, which moves this date. The Form 1041 instructions were not re-read, so confirm the year-end convention with the CPA.',source('usc6072')),
 ('Each year: 1 February, second installment','Property-tax second installment. Delinquent after 5 p.m. on 10 April, with a 10 percent penalty.','Owner or trustee','Same bill as above; missing either date adds a penalty.',source('rtc2618')),
 ('Fall 2027 · FY 2027–28 bill (San Francisco parcels only)','Proposition H parcel tax first appears on the regular property-tax bill and is paid in the same two installments. SFMTA states the tax runs from 1 July 2027 through 30 June 2042, with inflation adjustments from FY 2028–29.','Owner or trustee of a San Francisco parcel','Applies to Property B only if its parcel type and taxable building area fall within the schedule. The amount for Property B is not computed here.',source('sfMuni')),
]),'Dated steps')
body+='<div class="callout warning"><strong>Not on this timeline yet.</strong> The fiscal-year convention a decedent’s estate may elect on Form 1041 has not been read from the governing official text in this review. It stays blank and is listed on the Flagged page rather than filled from a secondary site.</div>'
body+='<div class="callout warning"><strong>Not on this timeline yet.</strong> The San Francisco parcel-tax billing date, the Form 4768 extension mechanics and the fiscal-year convention a decedent’s estate may elect on Form 1041 have not been read from the governing official text in this review. They stay blank and are listed on the Flagged page rather than filled from a secondary site.</div>'
# ---- Pre-commitment register: written, dated conditions set before figures arrive (added 16 Nov 2026) ----
def money0(v):
    return '$' + f'{v:,.0f}'

_pre_rows = [
 ('LIVE','Choose living in [PROPERTY A]','T1 · an occupancy decision','Written and dated by the household before any branch of the private model is run.',
  'A verified written opinion says the qualifying transferee can make the home their principal residence within the statutory year; the household sets, in writing and in advance, the number of years it intends to live there, and every assumption in the private model is fixed and dated on the same day.',
  'In advance: the written occupancy intention and the claim calendar. Falsified if the year passes with no homeowners’ exemption claim filed and a supplemental assessment is enrolled.',
  'Signing it before the figures exist is the only way the choice can be read forward from stated values rather than backward from a favourable projection.',
  'boe', ['prop19','lta26026']),
 ('LIVE','Choose living in [PROPERTY A]','T2 · family-home relief survives','Written and dated before the private model is run.',
  'A written assessor determination (or counsel’s opinion on the claim) confirms the exclusion, and at least one full assessment year passes with the claim intact.',
  'Falsified at the first lien date after the qualifying transferee stops being eligible: the Board states the exclusion is then removed and the new base-year value enrolled. The claim itself must be timely — forms BOE-266 or BOE-261-G within one year — or relief begins only in the year the exemption claim is filed.',
  'If relief falls away the annual cost of the same home changes for decades, which is the largest single number in the live column.',
  'lta26026', ['boe','rtc480']),
 ('LIVE','Choose living in [PROPERTY A]','T3 · rent break-even','No threshold at all: the break-even is a model output the household may set before or after a projection, provided it is written and dated first.',
  'A verified avoided rent, in what the household would otherwise pay for equivalent housing, with three or more comparable leases on file. HUD small-area fair market rents are voucher payment standards, not market or lawful rents, so they are a floor check only.',
  'Reopens at every lease renewal and at any local-law change.',
  'Avoided rent is the value living earns and the model cannot see it; writing the comparison first prevents an unstated preference from being dressed as arithmetic. Where the break-even that crosses the rent line is not computed on the published site, no number is stated here.',
  'hud', ['invest']),
 ('RENT','Choose renting [PROPERTY A] out','T4 · rent floor','Set before the private model is run, from comparable leases only.',
  'At least three usable comparable leases and a written break-even: the gross monthly rent at which the rental covers its own full costs, before financing and income tax, in today’s money. A voucher benchmark is not a comparable lease.',
  'Reopens if two successive comparable quarters fall below the break-even.',
  'A rent achieved in a good quarter is not a policy; the floor is what makes the choice falsifiable, and only a lease can support it.',
  'hud', ['sfRent']),
 ('RENT','Choose renting [PROPERTY A] out','T5 · assessed value and tax','Set before the first projection.',
  'The reconstructed or reassessed assessed value and the tax-rate-area method are agreed in writing before the projection, and the first real secured bill is checked against the projection. The county rate book is published one fiscal year at a time; use the book for the tax year being modelled.',
  'Reopens if the actual bill differs from the projection by a stated margin, or if decline-in-value relief applies.',
  'The property-tax line is large and parcel-specific; an unverified rate silently moves every year of the comparison.',
  'prop13', ['sccRateBook','prop13factor']),
 ('RENT','Choose renting [PROPERTY A] out','T6 · insurance quote','Set before the private model is run.',
  'A binding quote for the correct product — owner-occupied or landlord form, with or without earthquake cover — with the deductible and exclusions in writing. A regulatory survey is not a quote.',
  'Reopens at every renewal and after any loss or local hazard change.',
  'A regulatory survey cannot price this parcel; the deductible, not the premium alone, decides whether a loss is a balance-sheet event.',
  'cdi', ['cdieq','fairplan']),
 ('RENT','Choose renting [PROPERTY A] out','T7 · leases and local rules verified','Set before trusting any rent figure.',
  'The leases, occupancy, rent-control coverage and local rules for [PROPERTY B] are checked against primary documents, and the lawful rent for the household’s own use is settled in writing.',
  'Reopens on enactment of any measure the Rent Board has noticed, and at each annual increase window.',
  'B is already owned; its lawful rents and its rules set the baseline the A decision is measured against, and proposed rules are not law.',
  'sfRent', ['sfMuni']),
 ('SELL','Choose selling [PROPERTY A]','T8 · same-year sale, with basis and gain','Set before the private model is run.',
  'A sale is modelled in the same tax year as the transfer, because inherited basis is generally fair market value at the date of death, so a same-year sale has little or no gain by construction; that line is written down before any multi-year projection.',
  'Reopens if the transaction slips into a later tax year.',
  'Fixing the basis and the gain first is what stops a long projection from being used to justify a sale whose tax was never computed.',
  'basis', ['irs701']),
 ('SELL','Choose selling [PROPERTY A]','T9 · like-kind exchange and transfer tax settled','In writing, before any listing.',
  'The written record says whether a like-kind exchange is wanted and available — the statute reaches real property exchanged for like property, identified within 45 days and completed within 180 days, so proceeds reinvested in stocks cannot use it — and whether any documentary transfer tax exemption applies, which the county requires the instrument itself to cite.',
  'Reopens if the buyer or the timing makes an exchange possible, or if the exemption is refused at recording.',
  'An unstated preference here changes the whole tax treatment and the closing statement of the sale.',
  'usc1031', ['scc-recording','rtc11911']),
 ('SELL','Choose selling [PROPERTY A]','T10 · estate liquidity and portability','Answered privately by counsel and the CPA before any sale decision.',
  'A written answer on whether a return is required (gross estate plus adjusted taxable gifts against the threshold), whether portability is wanted, and how any tax would be paid without a forced sale.',
  'Reopens only if the estate changes materially before the transfer.',
  'Estate tax and portability can force or forbid a sale regardless of the ranking.',
  'estate', ['i706','usc6075']),
 ('SELL','Choose selling [PROPERTY A]','T11 · investment policy in writing','Written and dated before the money arrives.',
  'A short written policy states the allocation, the liquidity reserve, the deposit-insurance plan and the staged-entry rule; the private model’s return assumption is the policy’s expected return, not a hoped-for one.',
  'Reopens annually and after any change in the household’s needs.',
  'The return assumption does most of the work in every sell result; without a policy it is a guess dressed as a plan.',
  'invest', ['fdic','treasuryBills']),
 ('MIXED','Choose a mixed path','T12 · the written hybrid rule','Written and dated before the model is run.',
  'The household writes its hybrid rule first — for example: live in the home for a stated number of years and then sell if a stated condition is met — and the year, and only then compares it with the pure paths on the same dates.',
  'Reopens at the stated review date and at the trigger itself.',
  'A mixed path chosen after the numbers is just the best-fitting line from one projection.',
  'boe', ['irs701','basis']),
 ('ANY','Choose any path','T13 · a falsifier per path, filed with the decision','Written before the first projection and reviewed at the review date.',
  'Each path carries the observable event that would void it — a lost exemption claim, an unreachable rent floor, a tax year that slips, a return that misses policy.',
  'Reviewed at the written review date and whenever a falsifier fires.',
  'A choice that cannot be shown false is not a decision; it is a preference with a spreadsheet attached.',
  'invest', []),
]

def _pre_rows_render():
    out = []
    for path, decision, test, when, rule, falsifier, why, src, extra in _pre_rows:
        official = source(src) + (''.join(' · ' + source(k) for k in extra) if extra else '')
        out.append((path, decision, test, when, rule, falsifier, why, official))
    return out

_rent_test = table(
 ['Rent test, first full year after a living choice', 'Amount', 'What it is', 'Official context'],
 [
  ('Housing the household would otherwise rent', '— private comparable rent required', 'Avoided rent, verified from comparable leases; not published.', source('hud')),
  ('[PROPERTY A] rent the property could earn instead', '— private comparables required', 'The other side of the same choice; not published.', source('hud')),
  ('Break-even rent at which living and renting equal', '— to be computed privately', 'The crossing point, written down before any projection is run.', source('invest')),
 ],
) + '<p class="tiny">No threshold on this page is a recommendation and none carries a dollar figure. Each is a written, dated condition the household sets for itself before the numbers are computed, using the private comparables and adviser letters that the Questions register names. Where a crossing point is not computed on this page, the cell stays blank rather than being inferred.</p>'

body = ('<div class="callout warning"><strong>Why this page exists.</strong> The brief asks that the household agree, in writing and in advance, on what would make it choose each path — so that the outcome cannot be reverse-engineered from one favourable projection. A model cannot do that for you, and this page does not pretend to. It sets out, for every path, the condition to write down first, the falsifier that would void it, and the official rule the condition rests on. Every threshold cell is deliberately blank: filling one in from this public site would be a recommendation.</div>'
 '<div class="callout"><strong>Sign first, then compute.</strong> Write the register on paper or in a private file, date it, and only then run the private model on verified inputs. A condition written after the figures are visible is not a pre-commitment, and a mix chosen after the numbers is just the best-fitting line from one projection.</div>')

body += section('The conditions, by path', table(
 ['Path', 'The decision being pre-committed', 'Test', 'When it must be written', 'The condition to write down first', 'Falsifier that voids it', 'Why it must precede the figures', 'Official framework'],
 _pre_rows_render()) )

body += section('The rent test beside the living choice', _rent_test, 'threshold blank on purpose')

body += section('Official rules this register relies on, re-read 16 Nov 2026', table(
 ['What the rule says', 'Exact wording or effect as the agency publishes it', 'What it does not settle', 'Official source'],
 [
  ('The exclusion is claimed, not automatic',
   '“The exclusions provided for in this section shall not be allowed unless a claim for the exclusion sought … is filed with the assessor.” The BOE asks for the claim within three years of the transfer or before a transfer to a third party, whichever is earlier, and the exemption claim within one year.',
   'Whether this household’s facts qualify, and the day the paperwork is actually filed.',
   source('boe') + ' · ' + source('lta26026')),
  ('Continued use of the home is required to keep the exclusion',
   'The BOE states the home must be continually used as the family home by an eligible transferee, and that if it becomes ineligible for the homeowners’ or disabled veterans’ exemption the exclusion is removed and the new base-year value enrolled as of the lien date following that date.',
   'The exact enrolment date for a particular occupancy change; ask the assessor.',
   source('lta26026')),
  ('A missed family-home condition is not modelled here',
   'Eligibility rests on all of the Board’s conditions being met: the transferor’s home, the transferee moving in within one year, a timely claim and continued use. The guide shows how the claim arithmetic works; it cannot tell you whether a particular family qualifies.',
   'Any fact-specific exception; that is a question for the assessor and counsel.',
   source('boe') + ' · ' + source('prop19')),
  ('The federal filing test uses the gross estate',
   'A return is required if the gross estate, increased by adjusted taxable gifts and the specific gift tax exemption, exceeds the filing threshold for the year of death — $15,000,000 for 2026 on the IRS table; the return is due nine months after death under 26 U.S.C. §6075(a).',
   'This household’s gross estate, gifts and any portability election.',
   source('estate') + ' · ' + source('usc6075')),
  ('California has no estate or inheritance tax for a modern death',
   'The State Controller states no California estate-tax return is required for deaths on or after 1 January 2005, and the inheritance tax is collected only for deaths before 8 June 1982.',
   'Nothing about federal exposure, which is the exposure to test.',
   source('ftb')),
  ('Capital gain is taxed with the ordinary schedule, plus one surcharge',
   'The FTB rate schedules top out at 12.30% above $742,953 (single) or $1,485,906 (joint) of taxable income; Form 540 line 62 adds a 1% Behavioral Health Services Tax on taxable income above $1,000,000. Read from the published schedule and the line-62 worksheet, not from a summary.',
   'The household’s own bracket, deductions and other income.',
   source('ftbSchedule') + ' · ' + source('ftb540')),
  ('The home-sale exclusion has ownership and use tests',
   'The IRS states up to $250,000 of gain ($500,000 on a joint return) may be excluded if the ownership and use tests are met — two of the last five years for each — and that the exclusion is not automatic.',
   'Whether a particular living-then-sell timeline meets both tests.',
   source('irs701')),
  ('A like-kind exchange never reaches stock-market reinvestment',
   '26 U.S.C. §1031 as amended applies to real property exchanged for real property, with 45-day identification and 180-day completion; securities are not like-kind real property.',
   'Whether an exchange of this property for another is available or wanted.',
   source('usc1031')),
  ('A regulatory insurance survey is not a quote',
   'The Department of Insurance states its premium surveys “are not premium quotes”, that it is a regulator and not an agent, and that the amount actually charged may differ.',
   'This parcel’s premium, deductible, exclusions or insurability.',
   source('cdi')),
  ('A rent benchmark is not a lawful rent or a market quote',
   'HUD describes small-area fair market rents as ZIP-code figures used to set voucher payment standards; the site uses them only as a floor check.',
   'The achievable rent or any lease term.',
   source('hud')),
  ('A transfer tax exemption must be cited on the instrument',
   'The Santa Clara County Clerk-Recorder states the documentary transfer tax is “due on all changes of ownership unless an applicable statutory tax exemption is cited”, computed at 55 cents per $500 of real property value, with a higher published rate of 165 cents per $500 for property inside San Jose, Palo Alto and Mountain View, and an additional $20 charge where a Preliminary Change of Ownership Report is missing at recording.',
   'Whether an exemption applies to this transfer — the county page does not answer it for a particular deed.',
   source('scc-recording') + ' · ' + source('rtc11911')),
  ('A proposed measure is not law',
   'The Rent Board’s 9 November 2026 notice states Board of Supervisors File 261020 “has not been enacted and is subject to change”.',
   'Whether it will be enacted before the transfer.',
   source('sfRent')),
 ],
) )

body += section('How to use this register', '<p>Each row above is one line of a private file the household keeps and dates. Fill only the columns that are yours to fill: the condition, the falsifier, and the date. Leave every threshold that requires a number blank until the verified comparables, adviser letters and quotes listed in the Questions register are in hand. When a condition fires or fails, write the date and the reason next to it. When the review date arrives, re-check the official sources linked in each row before relying on any rule that has changed.</p><ul class="list"><li>Write the register before running any private projection, and keep the dated original.</li><li>Record every decision and its date next to the item, so a later reader knows what was chosen and why.</li><li>Never enter a private answer, address, rent, bill or account number on this site; keep the completed register offline.</li><li>Re-read the linked official page before acting; the rules and amounts above are dated 16 November 2026.</li></ul>', 'how to use it')
page('precommit','Sign the decision before you see the numbers.','A written, dated pre-commitment register: for each path, the condition to agree on first, the falsifier that would void it, and the official rule it rests on. Every threshold is blank on purpose.',body)

page('timeline','Deadlines in order.','The dated steps that can move the decision, from the date of death to the Proposition 19 claim deadlines. Each row links to the official rule.',body,['guide/data/model.js'] if False else [])

# ---- Attorney & CPA one-page sheet: synthetic structure, placeholders only, prints on one page ----
PRINT_CSS='''<style>@media print{@page{size:letter;margin:.4in}.header,.notice,.footer,.hero,.no-print,.skip,noscript{display:none!important}body{background:#fff;font-size:8.6pt;line-height:1.25}main{padding:0}.container{width:100%}.brief-sheet{padding:0}.brief-sheet h2{font-size:10.5pt;margin:5px 0 2px}.brief-sheet p,.brief-sheet li{margin:1px 0}.brief-sheet ul{margin:2px 0 3px;padding-left:14px}.brief-sheet .section{padding:2px 0}.brief-sheet table{font-size:7.8pt}.brief-sheet th,.brief-sheet td{padding:2px 4px}.brief-sheet .tiny{font-size:7.2pt}.brief-sheet a{color:#000;text-decoration:none}.brief-sheet .print-head{display:block!important}}
@media screen{.print-head{display:none}}</style>'''
def _li(items):
    return '<ul>'+''.join('<li>'+x+'</li>' for x in items)+'</ul>'
sheet=(
 PRINT_CSS+'<div class="brief-sheet">'
 '<div class="print-head"><strong>Attorney &amp; CPA briefing sheet · Inheritance decision guide · reviewed 16 Nov 2026</strong></div>'
 '<p class="tiny">For [ATTORNEY] and [CPA]. No household figures are included. Identifiers stay placeholders: [DECEDENT], [TRUSTEE], [PROPERTY A] and [PROPERTY B]. Educational, not legal or tax advice.</p>'
 + section('Facts to confirm privately',_li([
   'Date of death, and the date-of-death value of [PROPERTY A] from a qualified appraiser (see '+source('basis')+').',
   'Whether [PROPERTY A] is titled in [TRUSTEE]’s trust, and what the trust allows for a sale of the residence (see '+source('notice')+').',
   'Title, leases and unit status of [PROPERTY B] (see '+source('estate','Estate-rule context')+').',
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
   'Which Proposition 19 claims apply to the transfer? The BOE states the periods: homeowners’ exemption claim within one year of transfer; the exclusion claim within three years of transfer or before transfer to a third party ('+source('boe')+').',
   'Decide in writing whether a like-kind exchange (§1031) is wanted before any listing: it reaches only real property exchanged for real property, with 45-day identification and 180-day completion — it cannot shelter proceeds reinvested in stocks ('+source('usc1031')+').',
 ]))
 + section('Figures used, rounded to $10 unless an official amount',table(['Figure','Value','Source'],[
   ('Property A · example value / assessed base / tax','Synthetic only; private appraisal and bill intentionally blank',source('county')),
   ('Property B · example value / assessed base / tax / rent','Synthetic only; private appraisal, bill and leases intentionally blank',source('sfTax')),
   ('Insurance benchmark','— not mapped to a private property; obtain product-specific quotes',source('cdi')),
   ('Rent benchmark','— no property-specific rent is published; obtain private comparable evidence',source('hud')),
   ('Federal filing threshold, 2026 death','$15,000,000 (official)',source('estate')),
   ('Federal basic exclusion, 2027 death','$15,480,000 (official)',source('estate27')),
   ('Prop 19 allowance, transfers 16 Feb 2025 – 15 Feb 2027','$1,044,590 (rounded from the official amount)',source('allowance')),
   ('Treasury par yields, 13 Nov 2026','3-month 4.32%; 2-year 4.88%',source('treasury')),
   ('Crash shapes used in the test','1929: −89% over 34 months · 2008: −57% over 17 months',source('fed1929')+' · '+source('fed2008')),
   ('Entry test, per $100,000, year 10','Invest all now '+money_range(_year10('2008','sell_now_all'))+' · park 24 then phase '+money_range(_year10('2008','park_24'))+' (2008-style)',source('fed2008')),
 ]))
 + section('Decision status', '<p>No personalized recommendation is made. The inputs that could change a real decision are private and unverified. First settle the trust, tax basis, Proposition 19, estate-liquidity, occupancy, rent, insurance, repair and transaction-cost questions with the relevant professionals.</p>')
 + section('What would change the example ranking',_li([
   'A different trust clause, title, or basis answer from counsel or the CPA (see the questions above).',
   'A different filing position for the estate, or a federal threshold change after the date of death.',
   'A different parking yield, or a different post-trough growth view; the test shows the sensitivity, not a forecast.',
 ]))
 + '</div>'
)
page('attorney-cpa','Attorney & CPA briefing sheet.','One printable page for counsel and the tax adviser. Placeholders replace every private fact; figures are rounded to $10 unless an official amount.',sheet)

# ---- Executive summary: the whole guide on one page, printable (added 15 Nov 2026) ----
_es_find = ('<p><strong>This is a decision framework, not a household recommendation.</strong> The site uses synthetic inputs to demonstrate how live, rent, sell, phased-investing and mixed paths can compare under different economic conditions. No household property value, rent, bill, lease, insurance record or location identifier is included.</p>'
 '<p><strong>What would change the answer?</strong> Trust authority and title, date-of-death valuation and basis, estate liquidity and prior gifts, Proposition 19 eligibility and occupancy, verified rents and leases, property-tax bills, insurance quotes, maintenance plans, sale costs, tax treatment and the household’s own value of living in the home.</p>'
 '<p><strong>Reinvestment risk:</strong> parking proceeds in short Treasuries before phasing into stocks can soften an immediate crash-entry risk, but can lag a rising market and exposes proceeds to reinvestment-rate risk. The Black swans page compares those trade-offs on the same synthetic starting amount and horizon.</p>')
_es_rows = [
 ('Federal estate-tax filing threshold', '<strong>$15,000,000</strong> for a death in 2026 and <strong>$15,480,000</strong> in 2027',
  'Official, published by the IRS', source('estate27')),
 ('California estate and inheritance tax', 'The State Controller states no California estate-tax return is required for a death on or after 1 January 2005, and that the inheritance tax is collected only for deaths before 8 June 1982',
  'Official, text rule', source('ftb')),
 ('Proposition 19 family-home allowance', 'approximately <strong>$1,044,590</strong> for a transfer between 16 February 2025 and 15 February 2027, shown rounded from the official amount; adjusted every other 16 February',
  'Official, rounded for display', source('allowance')),
 ('Proposition 13 assessed growth', 'the factored base year value rises with the inflation factor capped at 2% a year; the cap applied in 40 of the 51 published years from 1976-77 to 2026-27',
  'Official, plus one computation on the published factor list', source('prop13factor')),
 ('Inflation, 1991 to 2025', 'annual CPI-U averaged 2.62% and ranged from −0.36% to 8.00%, exceeding 3% in 10 of those 35 years',
  'Computed from the published BLS series via FRED', source('cpiHistory')),
 ('Yields used for the Treasury parking test', '4.32% at 3 months and 4.88% at 2 years on 13 Nov 2026',
  'Observation, published by the U.S. Treasury', source('treasury')),
 ('Deposit-insurance ceiling for parked cash', '<strong>$1,250,000</strong> per owner for a trust with five or more beneficiaries at the same bank',
  'Official', source('fdic')),
 ('County documentary transfer tax on a sale', '55 cents for each $500 of consideration — $110 for each $100,000, or 0.11% — with a city add-on by ordinance; the exemption question for a transfer at death is not answered on the county page',
  'Official, county', source('scc-recording')),
 ('Household-specific break-even', '— not published; calculate privately from verified inputs',
  'Model output withheld; official reference is context only', source('invest')),
 ('Entry test, per $100,000 at year 10, 2008-style peak', 'invest all now ' + money_range(_year10('2008', 'sell_now_all')) + ' · park 24 months then phase in ' + money_range(_year10('2008', 'park_24')),
  'Model output on the per-$100,000 entry-risk test', source('fed2008') + ' · ' + source('treasury')),
 ('What waiting costs when markets only rise', money_range([a - b for a, b in zip(_year10('none', 'park_24'), _year10('none', 'sell_now_all'))]) + ' per $100,000 at year 10 against the no-crash control',
  'Model output on the per-$100,000 entry-risk test', source('dca')),
 ('Rent increase, covered San Francisco units', '1.6% from 1 March 2026 to 28 February 2027',
  'Official, Rent Board', source('sfRent')),
]
_es_deadlines = [
 ('Within 60 days of the triggering event', 'Trustee notification to beneficiaries and heirs, where the section applies', source('notice')),
 ('Within 150 days of death', 'Change-in-ownership statement for real property transferred by reason of death, including through a trust', source('rtc480')),
 ('Within 9 months of death', 'Form 706 if a federal return is required; Form 4768 extends the time to file by 6 months', source('irs706i')),
 ('15th day of the 4th month after the entity year closes', 'Form 1041, the income tax return of the estate or trust', source('usc6072')),
 ('Within 1 year of the transfer', 'Homeowners’ exemption claim on a Proposition 19 family home', source('boe')),
 ('Within 3 years of the transfer, or before a sale to a third party', 'Claim for the family-home exclusion; also timely within 6 months of a supplemental or escape assessment notice', source('prop19')),
 ('Each 1 November and 1 February', 'Secured property-tax installments; delinquent after 5 p.m. on 10 December and 10 April with a 10 percent penalty', source('rtc2617') + ' · ' + source('rtc2618')),
]
execsum = (PRINT_CSS + '<div class="brief-sheet">'
 '<div class="print-head"><strong>Executive summary · Inheritance decision guide · official sources re-opened 16 Nov 2026</strong></div>'
 + section('Read this first', _es_find)
 + section('The four facts that decide it', table(['Fact to establish', 'Why it is not settled here', 'What it changes', 'Official framework'], [
   ('Does the trust permit a sale of the residence?', 'The trust instrument is not a public record and is not in any official source on this site.', 'If the trustee must or must not sell, no comparison on this site applies.', source('notice')),
   ('Does income-tax basis step up to date-of-death value?', 'The IRS rule is clear; the facts of this trust, and any alternate-valuation election, are not.', 'Without a step-up an immediate sale turns from a low-tax event into a heavily taxed one.', source('trustbasis')),
   ('Does Proposition 19 family-home relief apply?', 'It turns on the transferor’s residence, the transferee’s occupancy within one year, and a filed claim.', 'Without it the assessed base resets to market value, which is the single largest cost of holding the property.', source('boe')),
   ('Is the estate above the federal filing threshold?', 'That needs the whole gross estate, prior taxable gifts, deductions and elections, none of which is published here.', 'Estate tax and liquidity can force a sale whatever the arithmetic says.', source('estate27')),
 ]))
 + section('The numbers that carry the weight', table(['Figure', 'Value used on this site', 'Status of the number', 'Official source, or context for a model row'], _es_rows)
   + '<p class="tiny">Print this page with the browser print command; it is laid out to fit one sheet. Amounts are rounded to the nearest $10 except where a government body publishes the exact figure.</p>')
 + section('Deadlines the family controls', table(['When it falls', 'What is filed', 'Official source'], _es_deadlines))
 + section('What would change this summary', _li([
   'Any of the four facts above coming out the other way — each one is capable of reversing the ranking on its own.',
   'A reassessment, an appeal, new construction or a supplemental bill, none of which the model times to the lien date. See the Properties page.',
   'A parking yield materially below the observed short-Treasury rates, which the reinvestment-risk table on the Black swans page tests.',
   'An enacted change to federal or California transfer rules; the watchlist on the Taxes page records what was re-read, and when.',
   'A family preference about living in the house, which has real value that no table here measures.',
 ]))
 + section('Where to read next', cards([
   ('Decide', 'Compare the three paths', 'The live, rent and sell arithmetic with the annual tables.', 'decision.html'),
   ('Decide', 'Paths, mixed and pure', 'Half-way strategies, including keep-and-rent and sell-with-a-tax-reserve.', 'paths.html'),
   ('Decide', 'Black swans', 'Variable 50-year paths, the Treasury parking test and reinvestment risk.', 'stress.html'),
   ('Decide', 'What-if controls', 'Change the transfer year and the assumptions; no data is entered or stored.', 'whatif.html'),
   ('Evidence', 'What must be answered first', 'Twenty-one questions, the settled rule for each, and the private document that closes it.', 'questions.html'),
   ('Evidence', 'Real conditions', 'The inflation, assessment and market record behind every assumption.', 'conditions.html'),
   ('Rules', 'Taxes and deadlines', 'Property tax, Prop 13 and 19, estate tax, transfer tax, and the watchlist.', 'tax.html'),
   ('Act', 'Attorney &amp; CPA sheet', 'The same summary aimed at the two people who can answer the gating questions.', 'attorney-cpa.html'),
 ]))
 + '</div>')
page('summary', 'Executive summary, on one page.',
     'A privacy-safe decision framework: official rules, unknown private facts, deadlines and the conditions that could change a path.', execsum)
