/*
 * Source register — session 5a1bd5be.
 * Every entry is a page this session opened on 10 November 2026. `says` is what was read there:
 * words in double quotes are quoted from the page, the rest is a figure or a plain summary.
 * Nothing from blogs, law-firm pages, real-estate sites or search summaries is in this file.
 */
(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory();
  else root.ModelSources = factory();
})(typeof self !== 'undefined' ? self : this, function () {
  'use strict';

  var READ = '10 November 2026';

  var SOURCES = [
    // ---------------- federal estate and gift tax
    { id: 'F1', topic: 'Federal estate tax', publisher: 'Internal Revenue Service', title: 'Estate tax',
      url: 'https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax',
      says: 'Filing threshold by year of death: $5,000,000 (2011) … $5,490,000 (2017), $11,180,000 (2018) … $13,990,000 (2025), $15,000,000 (2026). “Beginning January 1, 2011, estates of decedents survived by a spouse may elect to pass any of the decedent’s unused exemption to the surviving spouse. This election is made on a timely filed estate tax return”.' },
    { id: 'F2', topic: 'Federal estate tax', publisher: 'Internal Revenue Service', title: 'IR-2026-133: tax inflation adjustments for tax year 2027',
      url: 'https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts',
      says: 'For 2027: estate basic exclusion $15,480,000; annual gift exclusion $20,000; standard deduction $33,200 (joint) and $16,600 (single); 24% bracket starts at $109,125 (single) and $218,250 (joint).' },
    { id: 'F2b', topic: 'Federal income tax', publisher: 'Internal Revenue Service', title: 'Revenue Procedure 2026-35',
      url: 'https://www.irs.gov/pub/irs-drop/rp-26-35.pdf',
      says: 'For 2027 long-term capital gains: 0% rate up to $102,100 (joint) / $51,050 (single); 15% rate up to $633,600 (joint) / $563,200 (single); 20% above.' },
    { id: 'F3', topic: 'Federal estate tax', publisher: 'Internal Revenue Service', title: 'What’s new — estate and gift tax',
      url: 'https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax',
      says: 'Public Law 119-21, signed 4 July 2025, “amends § 2010(c)(3) by increasing the basic exclusion amount to $15,000,000 for calendar year 2026”.' },
    { id: 'F4', topic: 'Federal estate tax', publisher: 'Internal Revenue Service', title: 'Instructions for Form 706 (revised July 2026)',
      url: 'https://www.irs.gov/instructions/i706',
      says: 'Form 706 must be filed when the gross estate plus adjusted taxable gifts is more than $15,000,000, or when the executor elects portability of the unused exclusion.' },
    { id: 'F5', topic: 'Federal estate tax', publisher: 'Internal Revenue Service', title: 'Frequently asked questions on estate taxes',
      url: 'https://www.irs.gov/businesses/small-businesses-self-employed/frequently-asked-questions-on-estate-taxes',
      says: 'Form 706 is due nine months after the date of death; Form 4768 gives an automatic six-month extension; the portability election needs a timely Form 706.' },
    { id: 'F6', topic: 'Federal estate tax', publisher: 'U.S. Government Publishing Office', title: '26 U.S.C. § 2001 — Imposition and rate of tax',
      url: 'https://www.govinfo.gov/link/uscode/26/2001',
      says: 'Rate schedule, top line: “Over $1,000,000 … $345,800, plus 40 percent of the excess of such amount over $1,000,000.”' },

    // ---------------- federal income tax
    { id: 'I1', topic: 'Basis and capital gains', publisher: 'Internal Revenue Service', title: 'Gifts and inheritances (FAQ)',
      url: 'https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances',
      says: 'The basis of inherited property is generally its fair market value on the date of death (or on the alternate valuation date if the executor elects it). “If you sell the property for more than your basis, you have a taxable gain.”' },
    { id: 'I2', topic: 'Basis and capital gains', publisher: 'Internal Revenue Service', title: 'Topic no. 409, Capital gains and losses',
      url: 'https://www.irs.gov/taxtopics/tc409',
      says: 'Long-term gains are taxed at 0%, 15% or 20%. Gain from depreciation on real property (unrecaptured section 1250 gain) is taxed at a maximum of 25%. Inherited property is treated as held long term. Losses on personal-use property are not deductible.' },
    { id: 'I3', topic: 'Basis and capital gains', publisher: 'Internal Revenue Service', title: 'Topic no. 701, Sale of your home',
      url: 'https://www.irs.gov/taxtopics/tc701',
      says: 'Up to $250,000 of gain ($500,000 on a joint return) on a main home is excluded if it was owned and lived in for at least two of the five years before the sale.' },
    { id: 'I4', topic: 'Basis and capital gains', publisher: 'Internal Revenue Service', title: 'Topic no. 559, Net investment income tax',
      url: 'https://www.irs.gov/taxtopics/tc559',
      says: '3.8% on the lesser of net investment income or income above $250,000 (joint) / $200,000 (single). Rents and gains from real estate count; gain excluded on a home sale does not.' },
    { id: 'I5', topic: 'Basis and capital gains', publisher: 'Internal Revenue Service', title: 'Topic no. 703, Basis of assets',
      url: 'https://www.irs.gov/taxtopics/tc703',
      says: 'Basis is used to figure depreciation and gain or loss, and is reduced by depreciation allowed.' },
    { id: 'I6', topic: 'Rental income', publisher: 'Internal Revenue Service', title: 'Topic no. 414, Rental income and expenses',
      url: 'https://www.irs.gov/taxtopics/tc414',
      says: 'Rent is taxable income; depreciation, repairs and operating expenses are deductible on Schedule E; passive-loss limits may apply.' },
    { id: 'D1', topic: 'Rental income', publisher: 'Internal Revenue Service', title: 'Publication 527, Residential Rental Property',
      url: 'https://www.irs.gov/publications/p527',
      says: 'Residential rental buildings are depreciated over 27.5 years. Land is not depreciable. “If you aren’t certain of the FMVs of the land and the buildings, you can divide the cost between them based on their assessed values for real estate tax purposes.”' },
    { id: 'TP6', topic: 'After a death', publisher: 'Internal Revenue Service', title: 'Topic no. 356, Decedents',
      url: 'https://www.irs.gov/taxtopics/tc356',
      says: '“The personal representative is responsible for filing any final individual income tax return(s) and the estate tax return of the decedent when due.” Form 56 gives notice of a fiduciary relationship.' },
    { id: 'TP7', topic: 'After a death', publisher: 'Internal Revenue Service', title: 'About Form 1041',
      url: 'https://www.irs.gov/forms-pubs/about-form-1041',
      says: 'The fiduciary of a domestic decedent’s estate or trust files Form 1041 to report its income, deductions, gains and losses.' },

    // ---------------- California: no death tax; income tax
    { id: 'C1', topic: 'California estate and inheritance tax', publisher: 'California Legislative Information', title: 'Revenue and Taxation Code § 13301',
      url: 'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=13301',
      says: '“Neither the state nor any political subdivision of the state shall impose any gift, inheritance, succession, legacy, income, or estate tax, or any other tax, on gifts or on the estate or inheritance of any person or on or by reason of any transfer occurring by reason of a death.”' },
    { id: 'C2', topic: 'California estate and inheritance tax', publisher: 'California State Controller', title: 'California estate tax',
      url: 'https://www.sco.ca.gov/ardtax_estate_tax.html',
      says: '“For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return.”' },
    { id: 'C3', topic: 'California estate and inheritance tax', publisher: 'California Franchise Tax Board', title: 'Gifts and inheritance',
      url: 'https://www.ftb.ca.gov/file/personal/income-types/gifts-and-inheritance.html',
      says: '“If you received a gift or inheritance, do not include it in your income. However, if the gift or inheritance later produces income, you will need to pay tax on that income.”' },
    { id: 'C4', topic: 'California income tax', publisher: 'California Franchise Tax Board', title: 'Capital gains and losses',
      url: 'https://www.ftb.ca.gov/file/personal/income-types/capital-gains-and-losses.html',
      says: '“California does not have a lower rate for capital gains. All capital gains are taxed as ordinary income.”' },
    { id: 'C5', topic: 'California income tax', publisher: 'California Franchise Tax Board', title: '2025 California tax rate schedules',
      url: 'https://www.ftb.ca.gov/forms/2025/2025-540-tax-rate-schedules.pdf',
      says: 'Joint return: 9.3% from $145,448 to $742,958; 10.3% to $891,542; 11.3% to $1,485,906; 12.3% above. Single: 9.3% from $72,724 to $371,479; 12.3% above $742,953.' },
    { id: 'C6', topic: 'California income tax', publisher: 'California Franchise Tax Board', title: 'Real estate withholding',
      url: 'https://www.ftb.ca.gov/pay/withholding/real-estate-withholding.html',
      says: 'Withholding is a “prepayment of income tax due from the selling of California land or anything on it”; Form 593 is completed for every sale; exemptions are certified on that form.' },
    { id: 'TP8', topic: 'After a death', publisher: 'California Franchise Tax Board', title: 'Estates and trusts',
      url: 'https://www.ftb.ca.gov/file/personal/filing-situations/estates-and-trusts/index.html',
      says: 'A trust files Form 541 if the trustee or a non-contingent beneficiary is a California resident (or it has California income) and gross income is over $10,000 or net income is over $100.' },

    // ---------------- Proposition 19 and Proposition 13
    { id: 'P1', topic: 'Proposition 19', publisher: 'California State Board of Equalization', title: 'Proposition 19 — fact sheets, questions and answers, forms checklist',
      url: 'https://www.boe.ca.gov/prop19/',
      says: 'Parent-to-child exclusion applies only to the parent’s principal residence that becomes the child’s principal residence. Worked example: taxable value $300,000, market value $1,500,000 → new taxable value $500,000. A rented home does not qualify. Homeowners’ exemption claim “Within 1 year from date of death or transfer”; exclusion claim “Within 3 years from date of death or transfer, or before transfer to 3rd party, whichever is earlier.” If the child stops living there, the home is taxed on its market value at the date of inheritance, adjusted for inflation.' },
    { id: 'P9', topic: 'Proposition 19', publisher: 'California State Board of Equalization', title: 'Letter to Assessors 2025/009',
      url: 'https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf',
      says: 'The $1 million amount is $1,044,586 for transfers from 16 February 2025 to 15 February 2027 (previously $1,022,600; before that $1,000,000). It is adjusted every other 16 February by the change in the FHFA California house price index for the prior calendar year (2.15% for 2024).' },
    { id: 'P13', topic: 'Proposition 19', publisher: 'California State Board of Equalization', title: 'Letter to Assessors 2026/026 — intergenerational transfer exclusion questions and answers',
      url: 'https://www.boe.ca.gov/proptaxes/pdf/lta26026.pdf',
      says: 'The home must become the child’s principal residence within one year: “There are no exceptions to this rule.” A trust “must be looked through to determine who has present beneficial ownership”. Property moved into a legal entity such as an LLC is not eligible. Of two homes kept by the same child, “only one can qualify as the child’s principal residence”. In a multi-unit property “only the unit occupied as the principal residence qualifies”.' },
    { id: 'B1', topic: 'Proposition 13', publisher: 'California State Board of Equalization', title: 'Letter to Assessors 2026/002 — inflation factor',
      url: 'https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf',
      says: 'Taxable values rise each year by the California inflation factor, capped at 2%. Factor for the 2026-27 roll: 1.02. The table of factors since 1976-77 shows 11 years below 2%.' },
    { id: 'B2', topic: 'Proposition 13', publisher: 'California State Board of Equalization', title: 'Change in ownership — frequently asked questions',
      url: 'https://www.boe.ca.gov/proptaxes/faqs/changeinownership.htm',
      says: 'A change in ownership, including by inheritance or through a trust, causes reassessment to market value on that date unless an exclusion applies. Transfers between spouses are excluded.' },
    { id: 'TP4', topic: 'Proposition 19', publisher: 'Santa Clara County Assessor', title: 'Parent to child transfers (Proposition 19)',
      url: 'https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2',
      says: '“The value limit is equal to the home’s taxable value at time of transfer plus $1 million. Any amount of market value exceeding the limit is added to the taxable value for the transferee.” Example: $200,000 taxable value, $1,800,000 market value → $800,000.' },

    // ---------------- local property tax
    { id: 'L1', topic: 'Local property tax', publisher: 'San Francisco Treasurer & Tax Collector', title: 'Secured property taxes',
      url: 'https://sftreasurer.org/property/secured-property-taxes',
      says: 'Secured property tax rate for fiscal year 2026-27: 1.18162182%. Bill = taxable value × rate + direct charges and special assessments. Instalments are late after 10 December and 10 April.' },
    { id: 'SFP', topic: 'Local property tax', publisher: 'San Francisco Treasurer & Tax Collector', title: 'Parcel tax exemptions and special assessments',
      url: 'https://sftreasurer.org/property/parcel-tax-exemptions-and-special-assessments',
      says: 'Fiscal year 2025-26: School Parcel Tax of 2020 $334.38; Teacher Support $319.34; school facilities $21.50 per dwelling unit on multi-family parcels; City College parcel tax $99 a year adjusted for inflation; Bay Restoration Authority $12.' },
    { id: 'L2', topic: 'Local property tax', publisher: 'County of Santa Clara, Controller-Treasurer', title: 'Compilation of tax rates and information, fiscal year 2025-26',
      url: 'https://controller.santaclaracounty.gov/property-tax-distribution/property-tax-rate-book',
      says: 'Rates per $100 of taxable value: 1% levy 1.00000; county retirement 0.03880; library retirement 0.00240; hospital bond 0.00520; housing bond 0.00560; Cupertino elementary bonds 0.00010 + 0.01650 + 0.01690; Fremont Union High bonds 0.01040 + 0.00880 + 0.01070 + 0.01180; Foothill-De Anza bonds 0.01010 + 0.01350 + 0.00750; open space 0.00140; water district 0.00390. The 2026-27 book was not yet posted.' },

    // ---------------- transfer taxes at sale
    { id: 'T1', topic: 'Transfer tax', publisher: 'California Legislative Information', title: 'Revenue and Taxation Code § 11911',
      url: 'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=11911',
      says: 'County documentary transfer tax “at the rate of fifty-five cents ($0.55) for each five hundred dollars ($500) or fractional part thereof”.' },
    { id: 'T2', topic: 'Transfer tax', publisher: 'California Legislative Information', title: 'Revenue and Taxation Code § 11930',
      url: 'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=11930',
      says: 'The transfer tax does not apply when property passes “by reason of the death of any person”, outright or in trust.' },
    { id: 'T3', topic: 'Transfer tax', publisher: 'Santa Clara County Clerk-Recorder', title: 'Recording real estate documents',
      url: 'https://clerkrecorder.santaclaracounty.gov/recording-documents/recording-real-estate',
      says: 'County tax $0.55 per $500. Only San Jose, Palo Alto and Mountain View are listed as charging an extra city tax; Cupertino is not listed.' },
    { id: 'T4', topic: 'Transfer tax', publisher: 'City and County of San Francisco, Assessor-Recorder', title: 'Transfer tax',
      url: 'https://www.sf.gov/transfer-tax',
      says: 'On the whole price: $3.40 per $500 from over $250,000 to under $1,000,000; $3.75 per $500 from $1,000,000 to under $5,000,000; $11.25 per $500 from $5,000,000 to under $10,000,000.' },
    { id: 'T5', topic: 'Transfer tax', publisher: 'City and County of San Francisco, Assessor-Recorder', title: 'Learn about transfer tax',
      url: 'https://www.sf.gov/information--learn-about-transfer-tax',
      says: 'Inheritances and gifts are generally exempt; the transfer tax affidavit is still filed.' },

    // ---------------- renting in San Francisco
    { id: 'R1', topic: 'San Francisco rent rules', publisher: 'San Francisco Rent Board', title: 'Current rates',
      url: 'https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit',
      says: 'Allowed yearly increase 1.6% from 1 March 2026 to 28 February 2027. Relocation payment for an owner move-in eviction: $8,245 per tenant, at most $24,733 per unit, plus $5,497 for a tenant who is elderly or disabled or a household with minor children.' },
    { id: 'R3', topic: 'San Francisco rent rules', publisher: 'San Francisco Rent Board', title: 'Learn about rent increases in San Francisco',
      url: 'https://www.sf.gov/learn-about-rent-increases-san-francisco',
      says: '“This amount is based on 60% of the increase in the Consumer Price Index for All Urban Consumers in the Bay Area.” “There is no limit on how much rent a landlord may first charge a tenant when renting an empty unit that is covered by rent control.” Board of Supervisors file 261020 (10% yearly limit on banked and capital-improvement increases) “has not been enacted”.' },
    { id: 'EHT', topic: 'San Francisco rent rules', publisher: 'San Francisco Treasurer & Tax Collector', title: 'Empty Homes Tax',
      url: 'https://sftreasurer.org/business/taxes-fees/empty-homes-tax-eht',
      says: 'The Superior Court ruled the tax unconstitutional on 31 October 2024; the Court of Appeal affirmed on 11 September 2026. Owners “will not be required to file or pay unless and until the appeals court’s decision is reversed”.' },

    // ---------------- after a death
    { id: 'TP1', topic: 'After a death', publisher: 'California Legislative Information', title: 'Probate Code § 16061.7',
      url: 'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PROB&sectionNum=16061.7',
      says: 'The trustee serves a notification on every beneficiary and heir “not later than 60 days” after a revocable trust becomes irrevocable on the settlor’s death. A contest must be brought within 120 days of the notification (or 60 days after a copy of the trust is delivered during that period, if later).' },
    { id: 'TP2', topic: 'After a death', publisher: 'California Legislative Information', title: 'Revenue and Taxation Code § 480',
      url: 'https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=RTC&sectionNum=480',
      says: 'For property held in trust, the trustee files the change in ownership statement in each county where the decedent owned real property “within 150 days after the date of death”.' },
    { id: 'TP3', topic: 'After a death', publisher: 'City and County of San Francisco, Assessor-Recorder', title: 'Guide: property-related matters following an owner’s death',
      url: 'https://www.sf.gov/guide-property-related-matters-following-owners-death',
      says: 'Form BOE-502-D within 150 days of the date of death. For property in a trust “the change in ownership (the date of reassessment) is the date of death, not the date of distribution”. Papers asked for: death certificate, deed, the whole trust with amendments.' },

    // ---------------- running costs
    { id: 'N1', topic: 'Solar and electricity', publisher: 'California Public Utilities Commission', title: 'Net energy metering and net billing',
      url: 'https://www.cpuc.ca.gov/industries-and-topics/electrical-energy/demand-side-management/customer-generation/net-energy-metering-and-net-billing',
      says: '“Pursuant to D.14-03-041, customer-generators are allowed to remain on the NEM 2.0 tariff for 20 years from the date they interconnected, or they are permitted to switch to the current tariff.” Systems applied for since 15 April 2023 are on the Net Billing Tariff, whose export credits are “usually lower than import rates”.' },
    { id: 'CDI', topic: 'Insurance', publisher: 'California Department of Insurance', title: 'Homeowners insurance comparison tool (2026)',
      url: 'https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:20',
      says: 'Premiums are shown only for hypothetical homes. “If you want to get the exact premium for your home, you will need to contact an agent, broker or insurer representative”. Wildfire surcharges “can range from 15% to over 300%” and “are not reflected in the premiums shown here”.' },
    { id: 'HUD1', topic: 'Rents', publisher: 'U.S. Department of Housing and Urban Development', title: 'Fiscal year 2026 Fair Market Rents — San Jose-Sunnyvale-Santa Clara area',
      url: 'https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026summary.odn?cbsasub=METRO41940M41940&year=2026&fmrtype=Final&dallas_sa_override=TRUE',
      says: 'Monthly, utilities included: $2,621 (studio), $2,982 (1 bedroom), $3,483 (2), $4,602 (3), $5,010 (4). These are 40th-percentile rents for the whole metro area, not for one city.' },
    { id: 'HUD2', topic: 'Rents', publisher: 'U.S. Department of Housing and Urban Development', title: 'Fiscal year 2026 Fair Market Rents — San Francisco area',
      url: 'https://www.huduser.gov/portal/datasets/fmr/fmrs/FY2026_code/2026summary.odn?cbsasub=METRO41860MM7360&year=2026&fmrtype=Final&dallas_sa_override=TRUE',
      says: 'Monthly, utilities included: $2,485 (studio), $2,977 (1 bedroom), $3,604 (2), $4,604 (3), $4,772 (4).' },

    // ---------------- official data series
    { id: 'H1', topic: 'House prices', publisher: 'Federal Housing Finance Agency, via Federal Reserve Bank of St. Louis', title: 'All-transactions house price index, San Jose-Sunnyvale-Santa Clara (series ATNHPIUS41940Q)',
      url: 'https://fred.stlouisfed.org/series/ATNHPIUS41940Q',
      says: 'Index (1995 Q1 = 100): 104.42 (1996 Q2), 317.27 (2006 Q2), 367.05 (2016 Q2), 558.75 (2026 Q2). From 320.14 (2006 Q3) it fell to 234.33 (2012 Q1), a drop of 26.8%.' },
    { id: 'H2', topic: 'House prices', publisher: 'Federal Housing Finance Agency, via Federal Reserve Bank of St. Louis', title: 'All-transactions house price index, San Francisco-San Mateo-Redwood City (series ATNHPIUS41884Q)',
      url: 'https://fred.stlouisfed.org/series/ATNHPIUS41884Q',
      says: 'Index (1995 Q1 = 100): 100.83 (1996 Q2), 306.74 (2006 Q2), 385.01 (2016 Q2), 506.53 (2026 Q2). From 311.15 (2006 Q3) it fell to 239.43 (2011 Q2), a drop of 23.1%.' },
    { id: 'H3', topic: 'House prices', publisher: 'Federal Housing Finance Agency, via Federal Reserve Bank of St. Louis', title: 'All-transactions house price index, California (series CASTHPI)',
      url: 'https://fred.stlouisfed.org/series/CASTHPI',
      says: 'Index (1980 Q1 = 100): 200.89 (1996 Q2), 643.96 (2006 Q2), 553.43 (2016 Q2), 974.97 (2026 Q2).' },
    { id: 'CPI', topic: 'Inflation', publisher: 'U.S. Bureau of Labor Statistics, via Federal Reserve Bank of St. Louis', title: 'Consumer price index, all items, San Francisco-Oakland-Hayward (series CUURA422SA0)',
      url: 'https://fred.stlouisfed.org/series/CUURA422SA0',
      says: 'Index (1982-84 = 100): 210.700 (August 2006), 267.853 (August 2016), 357.992 (August 2025), 370.130 (August 2026).' },
    { id: 'TSP', topic: 'Investment returns', publisher: 'Federal Retirement Thrift Investment Board', title: 'Thrift Savings Plan — C Fund',
      url: 'https://www.tsp.gov/c-fund/',
      says: 'C Fund (tracks the S&P 500), average annual return to October 2026: 15.41% over 10 years; 11.40% since January 1988.' },
    { id: 'TSPG', topic: 'Investment returns', publisher: 'Federal Retirement Thrift Investment Board', title: 'Thrift Savings Plan — G Fund',
      url: 'https://www.tsp.gov/g-fund/',
      says: 'G Fund (U.S. Treasury securities), average annual return to October 2026: 3.01% over 10 years; 4.65% since April 1987.' },

    // ---------------- law watch
    { id: 'BAL', topic: 'Law watch', publisher: 'California Secretary of State', title: 'Election results, 3 November 2026 — ballot measures',
      url: 'https://electionresults.sos.ca.gov/returns/ballot-measures',
      says: 'Unofficial returns as of 9 November 2026, 7:18 p.m.: Proposition 3 yes 60.6%; Proposition 40 no 52.8%; Proposition 41 no 54.9%; Proposition 42 yes 51.6%; Proposition 43 no 57.3%. Results are not final until certified.' },
    { id: 'V3', topic: 'Law watch', publisher: 'California Secretary of State', title: 'Official voter information guide — Proposition 3',
      url: 'https://voterguide.sos.ca.gov/propositions/3/',
      says: '“Makes permanent existing voter-approved tax rates for individuals earning over $371,000 (adjusted annually for inflation).” Without it the rates would expire in 2031.' },
    { id: 'V42', topic: 'Law watch', publisher: 'California Secretary of State', title: 'Official voter information guide — Proposition 42',
      url: 'https://voterguide.sos.ca.gov/propositions/42/',
      says: '“Prohibits any new state tax (1) imposed on the ownership of personal property (all things people own other than real estate), or (2) that applies retroactively based on taxpayer’s past activities.”' },
    { id: 'LW1', topic: 'Law watch', publisher: 'California Secretary of State', title: 'County Clerk/Registrar of Voters memorandum 26138',
      url: 'https://elections.cdn.sos.ca.gov/ccrov/2026/may/26138jh.pdf',
      says: '18 May 2026: the initiative “Repeals voter-enacted changes to property tax rules for transfers between family members” did not gather enough signatures; “the petition has failed”.' },
    { id: 'LW2', topic: 'Law watch', publisher: 'U.S. Congress', title: 'H.R. 1301, Death Tax Repeal Act (119th Congress)',
      url: 'https://www.congress.gov/bill/119th-congress/house-bill/1301',
      says: 'Introduced 13 February 2025 and referred to the House Committee on Ways and Means the same day. Status: introduced. No later action is listed.' }
  ];

  var byId = {};
  SOURCES.forEach(function (s) { byId[s.id] = s; });

  return { READ: READ, SOURCES: SOURCES, byId: byId };
});
