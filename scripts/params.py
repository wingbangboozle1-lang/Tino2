"""Published planning parameters for the public guide.

Every value here is either (a) an amount published by an official agency, quoted
in `qa/ledger.json` or in `verification/23c5a9c4/REPORT.md`, or (b) a planning
assumption whose basis is stated. Nothing here is a household record: the two
originally supplied property figures are rounded to $1,000 and every derived
figure is rounded to $10 before publication.

`basis` values
  official   amount published by a government/regulator source (link in SOURCES)
  supplied   owner-supplied estimate, rounded; not independently verifiable
  planning   analyst assumption used to make the comparison runnable
"""

# ---------------------------------------------------------------------------
# Properties
# ---------------------------------------------------------------------------
A = {
    'label': 'Property A · Cupertino home (future trust inheritance)',
    'market_2026': 3_100_000,          # supplied estimate, $1,000 rounding
    'assessed_2026': 550_000,          # supplied tax record, $1,000 rounding
    'assessed_rounding': 1_000,        # record-derived field: coarser on purpose
    'tax_rate': 0.01335,               # observed effective rate; see RATE_A note
    'water_month': 130,                # supplied band $100-$150, midpoint
    'electric_month': -10,             # supplied: solar credit, small net benefit
    'insurance_year': 2_200,           # planning, inside the CDI survey range
    'maintenance_pct': 0.0075,         # planning, of market value
    'rent_month': 6_500,               # planning, anchored on FY2027 HUD SAFMR
    'vacancy': 0.05,
    'management': 0.08,
    'land_share': 0.20,                # planning: depreciable building share
}

B = {
    'label': 'Property B · San Francisco three-unit building (already owned)',
    'market_2026': 1_800_000,          # supplied estimate, $1,000 rounding
    'assessed_2026': 116_500,          # supplied tax record + 2% factor, $100 rounding
    'tax_rate': 0.0118162182,          # official FY2026-27 secured rate
    'rent_month_two_units': 7_150,     # supplied
    'rent_month_third_unit': 2_770,    # planning, FY2027 HUD SAFMR 1-bedroom
    'water_month': 360,                # supplied band $330-$400, midpoint
    'electric_month': 50,              # supplied band $30-$70, midpoint
    'insurance_year': 3_600,           # planning; no official multi-unit quote
    'maintenance_pct': 0.0100,         # planning, of market value
    'vacancy': 0.04,
    'management': 0.05,
    'land_share': 0.35,                # planning: depreciable building share
}

# ---------------------------------------------------------------------------
# Official anchors quoted on the pages
# ---------------------------------------------------------------------------
RATE_A = {
    # FY2025-26 Santa Clara County rate book, per $100 of assessed value.
    'components': [
        ('1% maximum levy', 1.00000, 'statutory'),
        ('County retirement levy', 0.03880, 'official'),
        ('County library retirement levy', 0.00240, 'official'),
        ('VMC 2008 bond', 0.00520, 'official'),
        ('County housing bond 2016', 0.00560, 'official'),
        ('Cupertino Elementary 2001', 0.01650, 'official'),
        ('Cupertino Elementary 2012', 0.01690, 'official'),
        ('Cupertino Elementary 2024', 0.00010, 'official'),
        ('Fremont Union High 2008', 0.00880, 'official'),
        ('Fremont Union High 2014', 0.01070, 'official'),
        ('Fremont Union High 2018', 0.01180, 'official'),
        ('Fremont Union High 2022', 0.01040, 'official'),
        ('Foothill-De Anza 1999', 0.00750, 'official'),
        ('Foothill-De Anza 2006', 0.01010, 'official'),
        ('Foothill-De Anza 2020', 0.01350, 'official'),
        ('Midpeninsula Open Space 2014', 0.00140, 'official'),
    ],
    'water_project': 0.00390,   # SCVWD State Water Project, land and improvements
    # Check: the components sum to 1.1597% (1.1636% with the water-project rate).
    # The supplied bills imply about 1.335% of assessed value. The roughly 13-15%
    # residual is consistent with fixed direct charges on the bill that are not
    # part of the ad valorem rate. The model uses the observed effective rate and
    # the gap is published as a flagged irregularity.
}

B_PARCEL_TAXES = [
    ('School Parcel Tax of 2020', 334.38, 'per parcel, inflation-adjusted'),
    ('SFUSD Teacher Support', 319.34, 'per parcel, inflation-adjusted'),
    ('SFUSD Facilities District', 21.50, 'per dwelling unit, multi-family'),
    ('City College parcel tax', 99.00, 'per parcel'),
    ('SF Bay Restoration Authority', 12.00, 'per parcel'),
]
B_PARCEL_UNITS = 3          # dwelling units for the per-unit parcel tax
B_MEASURE_H = 249.00        # multifamily residential base, from FY2027-28
B_RENT_BOARD_FEE = 59.00    # per dwelling unit, 2026-27, billed directly

# ---------------------------------------------------------------------------
# Economy: baseline and stress
# ---------------------------------------------------------------------------
BASE = {
    'inflation': 0.023,        # CBO 2031-2036 CPI, 2.3% a year
    'home_growth': 0.036,      # CBO FHFA purchase-only path 2026-2036, 3.6% a year
    'portfolio': 0.050,        # planning: total return before tax and fees
    'portfolio_drag': 0.005,   # planning: annual drag from tax on income and fees
    'rent_growth': 0.023,      # planning: rents track inflation
    'insurance_growth': 0.038, # planning: inflation + 1.5 points
    'ordinary_tax': 0.30,      # planning: blended federal + California
    'capital_gains_tax': 0.28, # planning: federal 20% + NIIT 3.8% + CA
    'recapture_tax': 0.25,     # official maximum on unrecaptured 1250 gain
    'sale_cost': 0.06,         # planning: commission, escrow, title, transfer
    'primary_gain_exclusion': 250_000,  # official IRS single-filer amount
    'depreciation_years': 27.5,         # official IRS residential GDS
    'prop19_allowance': 1_044_586,      # official BOE, 16 Feb 2025 - 15 Feb 2027
    'estate_exclusion_2026': 15_000_000,   # official IRS
    'estate_exclusion_2027': 15_480_000,   # official IRS IR-2026-133
    'estate_index': 0.023,     # planning: future exclusion indexed with CPI
    'hpi_ca_growth': 0.036,    # planning for the biennial Prop 19 step
    'transfer_years': (2040, 2045, 2050),
    'start_year': 2026,
    'end_year': 2076,
}

# Real-history replays. Each is a list of annual rates applied in order,
# anchored on the published FHFA/CPI record for those years.
STRESS = {
    'stagflation': {
        'title': '1970s-style stagflation',
        'inflation': [0.09, 0.06, 0.07, 0.11, 0.09, 0.06, 0.07, 0.06, 0.07, 0.05],
        'home': [0.05, 0.07, 0.12, 0.14, 0.10, 0.08, 0.06, 0.10, 0.13, 0.10],
        'portfolio': [-0.03, 0.08, 0.02, -0.15, -0.27, 0.20, 0.13, 0.02, 0.05, 0.13],
        'note': 'Inflation near or above 9% for part of the decade while a balanced portfolio lost money in real terms.',
    },
    'ca_crash': {
        'title': '1990-1996 California housing bust',
        'inflation': [0.06, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03],
        'home': [-0.01, -0.06, -0.05, -0.02, -0.01, 0.01, 0.02],
        'portfolio': [0.05, 0.13, 0.07, 0.05, 0.01, 0.16, 0.15],
        'note': 'Regional prices fell for several consecutive years; the published county index did not regain its 1990 level until the late 1990s.',
    },
    'gfc': {
        'title': '2007-2012 financial crisis',
        'inflation': [0.04, 0.01, 0.03, 0.02, 0.03, 0.02],
        'home': [-0.05, -0.12, -0.09, -0.02, -0.01, 0.03],
        'portfolio': [0.05, -0.37, 0.26, 0.15, 0.02, 0.16],
        'note': 'A one-year portfolio loss of about 37% with home prices falling about a quarter over the period.',
    },
    'rate_shock': {
        'title': '2022-2023 rate shock',
        'inflation': [0.08, 0.04, 0.03],
        'home': [0.02, -0.04, -0.02],
        'portfolio': [-0.13, 0.20, 0.12],
        'note': 'Inflation near 8% with a simultaneous fall in both bonds and equities; mortgage rates roughly doubled.',
    },
    'disaster': {
        'title': 'Uninsured earthquake, year 10 after transfer',
        'inflation': [0.023] * 50,
        'home': [0.0] * 50,
        'portfolio': [0.05] * 50,
        'note': 'A single $600,000 unrepaired-loss event plus doubled insurance for the remaining horizon; standard policies exclude earth movement.',
        'extra': {'repair': 600_000, 'insurance_jump_year': 10, 'insurance_jump': 1.0},
    },
}

SOURCES = {
    'irs_estate': ('IRS · estate tax, filing thresholds 2011-2026',
                   'https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax'),
    'irs_2027': ('IRS IR-2026-133 · 2027 exclusion $15,480,000',
                 'https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts'),
    'irs_basis': ('IRS · gifts and inheritances FAQ',
                  'https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances'),
    'irs_trust_basis': ('IRS · Rev. Rul. 2023-2',
                        'https://www.irs.gov/pub/irs-drop/rr-23-02.pdf'),
    'irs_tc701': ('IRS · Topic 701, sale of your home',
                  'https://www.irs.gov/taxtopics/tc701'),
    'irs_p523': ('IRS · Publication 523, selling your home',
                 'https://www.irs.gov/publications/p523'),
    'irs_p527': ('IRS · Publication 527, residential rental property',
                 'https://www.irs.gov/publications/p527'),
    'irs_p551': ('IRS · Publication 551, basis of assets',
                 'https://www.irs.gov/publications/p551'),
    'irs_1031': ('IRS · like-kind exchanges, real property',
                 'https://www.irs.gov/publications/p551'),
    'irs_niit': ('IRS · Topic 559, net investment income tax',
                 'https://www.irs.gov/taxtopics/tc559'),
    'irs_706faq': ('IRS · estate tax frequently asked questions',
                   'https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes'),
    'irs_709': ('IRS · instructions for Form 709',
                'https://www.irs.gov/instructions/i709'),
    'sco': ('California State Controller · estate tax',
            'https://www.sco.ca.gov/ardtax_estate_tax.html'),
    'boe19': ('California BOE · Proposition 19',
              'https://www.boe.ca.gov/prop19/'),
    'lta25009': ('BOE LTA 2025/009 · $1,044,586 allowance',
                 'https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf'),
    'lta26026': ('BOE LTA 2026/026 · Prop 19 Q&A',
                 'https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf'),
    'lta26002': ('BOE LTA 2026/002 · 2026-27 inflation factor',
                 'https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf'),
    'scc_asr': ('Santa Clara County Assessor · parent-child transfer',
                'https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2'),
    'scc_hoex': ('Santa Clara County Assessor · homeowners\' exemption',
                 'https://asr.santaclaracounty.gov/tax-savings/exemptions/homeowners'),
    'scc_rates': ('Santa Clara County · FY2025-26 tax rate compilation',
                  'https://files.santaclaracounty.gov/exjcpb1531/2025-11/tax-rate-book-2025-2026.pdf'),
    'sf_tax': ('SF Treasurer · secured property taxes, 1.18162182%',
               'https://sftreasurer.org/property/secured-property-taxes'),
    'sf_parcel': ('SF Treasurer · parcel taxes and special assessments',
                  'https://sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments'),
    'sf_rent': ('SF Rent Board · current rates and notices',
                'https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit'),
    'sf_fee': ('SF Rent Board · Rent Board fee',
               'https://www.sf.gov/rent-board-fee'),
    'sf_muni': ('SFMTA · Proposition H parcel tax',
                'https://www.sfmta.com/getting-around/muni/parcel'),
    'sf_election': ('SF Department of Elections · November 2026 results',
                    'https://www.sfelections.org/results/20261103/index.html'),
    'probate_notice': ('California Probate Code §16061.7',
                       'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=16061.7'),
    'rtc480': ('California Revenue and Taxation Code §480',
               'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480'),
    'ftb_593': ('California FTB · Form 593 withholding',
                'https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html'),
    'cdi_survey': ('CA Department of Insurance · homeowners premium comparison',
                   'https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/'),
    'cdi_guide': ('CA Department of Insurance · homeowners guide',
                  'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm'),
    'cdi_quake': ('CA Department of Insurance · earthquake coverage',
                  'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/eq-ins.cfm'),
    'cdi_fair': ('California FAIR Plan',
                 'https://www.cfpnet.com/'),
    'sjw': ('San Jose Water · 2026 rates',
            'https://www.sjwater.com/2026-rates/'),
    'sjw_grc': ('San Jose Water · 2025-27 general rate case',
                'https://www.sjwater.com/grc-2025-27/'),
    'sfpuc': ('SFPUC · adopted water and sewer schedules FY2026-28',
              'https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf'),
    'cupertino_water': ('City of Cupertino · water service',
                        'https://www.cupertino.gov/Residents/Utilities/Water'),
    'pge_solar': ('PG&E · solar billing plan',
                  'https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html'),
    'ab942': ('California Legislative Information · AB 942 status',
              'https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB942'),
    'hud': ('HUD · FY2027 small-area fair market rents',
            'https://www.huduser.gov/portal/datasets/fmr/smallarea/index.html'),
    'hud_95014': ('HUD · FY2027 SAFMR, ZIP 95014',
                  'https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=95014&cbsasub=METRO41940M41940'),
    'hud_94122': ('HUD · FY2027 SAFMR, ZIP 94122',
                  'https://www.huduser.gov/datasets/fmr/fmr2027/zip-calc?year=2027&zip=94122&cbsasub=METRO41860MM7360'),
    'fhfa_scc': ('FHFA house price index, Santa Clara County, via FRED',
                 'https://fred.stlouisfed.org/series/ATNHPIUS06085A'),
    'fhfa_sf': ('FHFA house price index, San Francisco County, via FRED',
                'https://fred.stlouisfed.org/series/ATNHPIUS06075A'),
    'cbo': ('Congressional Budget Office · outlook 2026-2036',
            'https://www.cbo.gov/system/files/2026-02/61882-By-the-Numbers.pdf'),
    'cbo_home': ('Congressional Budget Office · economic projections, FHFA path',
                 'https://www.cbo.gov/system/files/2026-02/51135-2026-02-Economic-Projections.xlsx'),
    'fed': ('Federal Reserve · September 2026 projections',
            'https://www.federalreserve.gov/monetarypolicy/fomcprojtabl20260916.htm'),
    'ssa': ('Social Security Trustees · 2026 long-range assumptions',
            'https://www.ssa.gov/oact/TR/2026/II_C_assump.html'),
    'bls_cpi': ('BLS · CPI news release archive',
                'https://www.bls.gov/news.release/archives/cpi_01122023.htm'),
    'freddie': ('Freddie Mac · Primary Mortgage Market Survey',
                'https://www.freddiemac.com/pmms'),
    'usgs': ('USGS · Bay Area earthquake outlook',
             'https://pubs.usgs.gov/publication/fs20163020'),
    'hr1301': ('Congress.gov · H.R. 1301, estate tax repeal',
               'https://www.congress.gov/bill/119th-congress/house-bill/1301'),
    'sb284': ('California Legislative Information · SB 284 status',
              'https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260SB284'),
    'irs_etcl': ('IRS · estate tax closing letter FAQ',
                 'https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-the-estate-tax-closing-letter'),
    'fdic': ('FDIC · your insured deposits',
             'https://www.fdic.gov/resources/deposit-insurance/brochures/insured-deposits'),
    'invest': ('SEC · investor bulletin, diversification',
               'https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-bulletins/world-investor-week-2026-investor-bulletin'),
    'github': ('GitHub · removing sensitive data from a repository',
               'https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository'),
}
