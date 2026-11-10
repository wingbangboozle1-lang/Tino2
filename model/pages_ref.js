/*
 * Reference pages: Taxes, Running costs, Inheritance steps, Law watch, Why pages differ,
 * Sources, Flagged, Method — session 5a1bd5be.
 * Official figures are quoted exactly here (Fmt.usdExact); model results stay rounded to $10.
 */
'use strict';

exports.build = function (c, x) {
  const { E, I, S, FL, Fmt, L, p0, sim, base, B } = c;
  const usd = Fmt.usd, pct = Fmt.pct, X = Fmt.usdExact;
  const T = p0.inheritYear, H = p0.horizon, END = T + H;
  const SC = I.SCENARIOS;
  const out = {};
  const aFixed = E.fixedCharges(p0.aBill2025, p0.aRate, p0.aAv2025);

  // =========================================================================== TAXES
  const estateRows = [
    { c: ['Amount one person can leave free of federal estate tax, deaths in 2026', X(15000000)], status: 'verified', src: ['F1', 'F3'] },
    { c: ['The same, deaths in 2027', X(15480000)], status: 'verified', src: ['F2'] },
    { c: ['The same, 2028 and later', ''], status: 'unverified', src: ['F2'], flag: 'F-ESTATE' },
    { c: ['Tax rate on the part of the estate above that amount', '40%'], status: 'verified', src: ['F6'] },
    { c: ['What is counted', 'Everything owned at death at fair market value: “cash and securities, real estate, insurance, trusts, annuities, business interests and other assets”'], status: 'verified', src: ['F1'] },
    { c: ['When a return (Form 706) is required', 'Gross estate plus taxable lifetime gifts above the amount for the year of death, or to pass an unused amount to a surviving spouse'], status: 'verified', src: ['F4'] },
    { c: ['Deadline for Form 706', 'Nine months after the date of death; Form 4768 gives six more months'], status: 'verified', src: ['F5'] },
    { c: ['Married couples (“portability”)', 'A surviving spouse can use the unused amount of the first to die, if the first estate files a timely return electing it'], status: 'verified', src: ['F1', 'F5'] },
    { c: ['Gifts: amount per recipient per year that needs no return, 2027', X(20000)], status: 'verified', src: ['F2'] },
    { c: ['California estate tax', 'None. No California estate tax return for deaths on or after 1 January 2005'], status: 'verified', src: ['C2'] },
    { c: ['California inheritance or gift tax', 'Prohibited by statute adopted by the voters in 1982'], status: 'verified', src: ['C1'] },
    { c: ['Is an inheritance income to the heir in California?', 'No. Income it later produces is taxable'], status: 'verified', src: ['C3'] }
  ];
  const roomRows = [];
  for (const TT of [2040, 2045, 2050]) for (const k of Object.keys(SC.house)) {
    const v = E.marketValue(p0.aValue2026, SC.house[k].aGrowth, TT), ex = E.estateExclusion(TT, p0);
    roomRows.push({ c: [`${TT}, ${SC.house[k].label.toLowerCase()} house prices`, usd(v), usd(ex), usd(ex - v), usd(2 * ex - v)], status: 'model', src: ['F1', 'F2', 'H1'], flag: 'F-ESTATE' });
  }
  const incomeRows = [
    { c: ['Tax basis of an inherited house', 'Its fair market value on the date of death', 'Selling at that value leaves no taxable gain'], status: 'verified', src: ['I1'] },
    { c: ['Federal tax on long-term gains', '0%, 15% or 20%. For 2027 the 15% rate runs to ' + X(633600) + ' of taxable income (joint) or ' + X(563200) + ' (single)', 'Applies to growth after the date of death'], status: 'verified', src: ['I2', 'F2b'] },
    { c: ['Net investment income tax', '3.8% once income passes ' + X(250000) + ' (joint) or ' + X(200000) + ' (single)', 'Applies to rents and to gains'], status: 'verified', src: ['I4'] },
    { c: ['California tax on gains', 'Taxed as ordinary income; no lower rate. 9.3% from ' + X(145448) + ' to ' + X(742958) + ' of taxable income (joint, 2025), up to 12.3% above ' + X(1485906), 'Adds to the federal rate'], status: 'verified', src: ['C4', 'C5'] },
    { c: ['Gain not taxed when a main home is sold', X(250000) + ', or ' + X(500000) + ' on a joint return, after owning and living in it two of the last five years', 'Only for the “live in it” choice'], status: 'verified', src: ['I3'] },
    { c: ['Rental house: depreciation', 'Building only, over 27.5 years; land is not depreciable', 'Lowers tax on rent each year'], status: 'verified', src: ['D1'] },
    { c: ['Rental house: depreciation taxed back at sale', 'At a federal rate of up to 25%', 'Raises tax when the rental is sold'], status: 'verified', src: ['I2'] },
    { c: ['Federal 24% bracket, 2027', 'Starts at ' + X(109125) + ' (single) or ' + X(218250) + ' (joint)', 'Rate assumed for rent in the model'], status: 'verified', src: ['F2'] },
    { c: ['California withholding when real estate is sold', 'A prepayment of income tax, handled on Form 593 at closing; exemptions are certified on the form', 'Cash-flow timing only'], status: 'verified', src: ['C6'] },
    { c: ['The heirs’ own tax rates', '', `Model uses ${pct(p0.taxOrdinary, 1)} on rent and ${pct(p0.taxGain, 1)} on gains`], status: 'assumption', flag: 'F-TAXRATES' }
  ];
  const propRows = [
    { c: ['Yearly rise in taxed value while ownership does not change', 'The California inflation factor, at most 2%. Factor for the 2026-27 roll: 1.02'], status: 'verified', src: ['B1'] },
    { c: ['When ownership changes, including by inheritance through a trust', 'The property is revalued to market value as of that date, unless an exclusion applies'], status: 'verified', src: ['B2'] },
    { c: ['Date of the change for a home held in a trust', 'The date of death, not the date the trust distributes the home'], status: 'verified', src: ['P1', 'TP3'] },
    { c: ['Parent-to-child exclusion: which home', 'Only the parent’s principal residence, and only if it becomes the child’s principal residence within one year. “There are no exceptions to this rule.”'], status: 'verified', src: ['P1', 'P13'] },
    { c: ['Amount added to the old taxed value (the “$1 million” amount)', X(1044586) + ' for transfers from 16 February 2025 to 15 February 2027'], status: 'verified', src: ['P9'] },
    { c: ['How that amount changes', 'Every second 16 February, by the change in the California house price index for the single year before'], status: 'verified', src: ['P9'] },
    { c: ['New taxed value', 'If market value is no more than old taxed value plus the amount: the old taxed value. Otherwise: market value minus the amount'], status: 'verified', src: ['P1', 'TP4'] },
    { c: ['Forms and deadlines', 'Homeowners’ exemption claim within one year of the death; exclusion claim (form BOE-19-P) within three years or before a sale to a third party'], status: 'verified', src: ['P1'] },
    { c: ['If the child later moves out or rents the home', 'The exclusion ends; the home is taxed on its market value at the date of inheritance, adjusted for inflation since'], status: 'verified', src: ['P1', 'P13'] },
    { c: ['A rented home, or a second home', 'Does not qualify'], status: 'verified', src: ['P1', 'P13'] },
    { c: ['Home held in a trust', 'Eligible: the trust is “looked through” to the people who benefit'], status: 'verified', src: ['P13'] },
    { c: ['Home moved into an LLC or other entity', 'Not eligible'], status: 'verified', src: ['P13'] },
    { c: ['Two homes kept by the same child', '“only one can qualify as the child’s principal residence”'], status: 'verified', src: ['P13'] },
    { c: ['A building with several units', '“only the unit occupied as the principal residence qualifies”; the rest is revalued'], status: 'verified', src: ['P13'] },
    { c: ['Tax rate, Property A', `${pct(p0.aRate, 4)}: the 1% levy plus voter-approved debt rates for the county, schools, college, open space and water districts, fiscal year 2025-26`], status: 'calculated', src: ['L2'], flag: 'F-RATE-A' },
    { c: ['Tax rate, Property B', '1.18162182% for fiscal year 2026-27'], status: 'verified', src: ['L1'] },
    { c: ['Fixed charges on Property B’s bill', 'School parcel taxes ' + X(334.38, true) + ' and ' + X(319.34, true) + '; school facilities ' + X(21.5, true) + ' per unit; City College ' + X(99) + ' adjusted for inflation; Bay Restoration ' + X(12) + ' (fiscal year 2025-26)'], status: 'verified', src: ['SFP'] },
    { c: ['Fixed charges used in the model', `Property A ${usd(aFixed)}, Property B ${usd(B.fixed)} a year: the 2025 bill minus rate × assessed value`], status: 'calculated', src: ['L1', 'L2'], flag: 'F-FIXED' }
  ];
  const exRows = [
    { c: [`Old taxed value in ${T} (today’s value +2% a year)`, usd(base.fbyvAtDeath)], status: 'model', src: ['B1'], flag: 'F-PROP13' },
    { c: [`Proposition 19 amount projected for ${T}`, usd(base.prop19Amount)], status: 'model', src: ['P9'], flag: 'F-P19AMOUNT' },
    { c: ['Sum: the most that can be excluded', usd(base.prop19.excluded)], status: 'model', src: ['P1'], flag: 'F-P19AMOUNT' },
    { c: [`Market value in ${T}`, usd(base.valueAtDeath)], status: 'model', src: ['H1'], flag: 'F-GROWTH' },
    { c: ['Market value above the sum', usd(base.prop19.excess)], status: 'model', src: ['P1'], flag: 'F-GROWTH' },
    { c: ['New taxed value if an heir moves in', usd(base.prop19.taxable)], status: 'model', src: ['P1', 'TP4'], flag: 'F-GROWTH' },
    { c: ['First tax bill if an heir moves in', usd(x.liveY1.propertyTax)], status: 'model', src: ['P1', 'L2'], flag: 'F-FIXED' },
    { c: ['First tax bill with no exclusion', usd(x.rentY1.propertyTax)], status: 'model', src: ['B2', 'L2'], flag: 'F-FIXED' },
    { c: ['Saved each year by the exclusion', usd(x.p19Saving)], status: 'model', src: ['P1', 'P9'], flag: 'F-P19AMOUNT' }
  ];
  const saleRows = [
    { c: ['County transfer tax when Property A is sold', X(0.55, true) + ' per ' + X(500) + ' of price (' + X(1.1, true) + ' per ' + X(1000) + ')'], status: 'verified', src: ['T1', 'T3'] },
    { c: ['City transfer tax in Cupertino', 'None listed. The county lists only San Jose, Palo Alto and Mountain View as charging one'], status: 'verified', src: ['T3'] },
    { c: ['San Francisco transfer tax if Property B were sold', X(3.75, true) + ' per ' + X(500) + ' of the whole price for sales from ' + X(1000000) + ' to under ' + X(5000000) + '; ' + X(3.4, true) + ' per ' + X(500) + ' below ' + X(1000000)], status: 'verified', src: ['T4'] },
    { c: ['Transfer tax on the inheritance itself', 'None: transfers by reason of death are exempt'], status: 'verified', src: ['T2', 'T5'] },
    { c: ['Agent commission and closing costs', ''], status: 'unverified', flag: 'F-SELLCOST' }
  ];
  out['taxes.html'] = L.page('taxes.html', 'Taxes and thresholds',
    `The rules that drive the decision, as read on official pages on ${S.READ}. Official amounts are quoted exactly; where no official figure exists the cell is blank and the row is flagged.`,
    `
<section aria-labelledby="h-est"><h2 id="h-est">Estate and inheritance tax</h2>
${L.table({ caption: 'Federal estate tax and California', head: ['Rule', 'What the official page says'], rows: estateRows })}
${L.table({ id: 'estate-room', caption: 'Property A against the exclusion: room left for the rest of the estate', head: ['Year of death and house prices', 'Property A', 'Exclusion, one person', 'Room left, one exclusion', 'Room left, two exclusions'], num: [1, 2, 3, 4], rows: roomRows,
    note: `The exclusion after 2027 is projected at ${pct(p0.estateIndexing, 2)} a year. “Room left” is how much else [OWNER]’s estate could hold before any federal estate tax. The brief gives no figure for the other assets.` })}
</section>
<section aria-labelledby="h-inc"><h2 id="h-inc">Income tax when the house is sold or rented</h2>
${L.table({ caption: 'Basis, gains and rental income', head: ['Rule', 'What the official page says', 'Effect here'], rows: incomeRows })}
</section>
<section id="prop19" aria-labelledby="h-prop"><h2 id="h-prop">Property tax: Proposition 13 and Proposition 19</h2>
${L.table({ caption: 'How the taxed value is set', head: ['Rule', 'What the official page says'], rows: propRows })}
${L.table({ caption: `Worked example: Property A inherited in ${T}, middle case`, head: ['Step', 'Amount'], num: [1], rows: exRows,
    note: 'Whenever the house is worth more than the old taxed value plus the amount, the exclusion saves exactly the tax rate times the amount.' })}
</section>
<section aria-labelledby="h-sale"><h2 id="h-sale">Taxes and costs when a property is sold</h2>
${L.table({ caption: 'Transfer taxes', head: ['Item', 'What the official page says'], rows: saleRows })}
</section>
`, { description: 'Federal estate tax, California rules, Proposition 13 and 19, capital gains and transfer taxes, with official sources.' });

  // =========================================================================== RUNNING COSTS
  const br = I.BRIEF;
  const costA = [
    { c: ['Property tax bill, 2025', '', usd(p0.aBill2025)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Home insurance, a year', '', usd(p0.aInsurance) + ' (owner’s guess)'], status: 'brief', src: ['CDI'], flag: 'F-INSURANCE' },
    { c: ['Water, a month', '', `${usd(br.aWaterMonthly[0])} to ${usd(br.aWaterMonthly[1])}`], status: 'brief', flag: 'F-UTIL' },
    { c: ['Electricity, a month', '', `Credit of ${usd(br.aSolarCreditMonthly[0])} to ${usd(br.aSolarCreditMonthly[1])} now; nothing counted after inheritance`], status: 'brief', flag: 'F-SOLAR' },
    { c: ['Solar: how long an older system keeps its original tariff', '20 years from the date it was connected', 'Credit not counted after inheritance'], status: 'verified', src: ['N1'] },
    { c: ['Solar: systems applied for since 15 April 2023', 'Net Billing Tariff; export credits “usually lower than import rates”', 'Not applicable unless the system is replaced'], status: 'verified', src: ['N1'] },
    { c: ['Maintenance and repairs, a year', '', usd(p0.aMaintenance)], status: 'assumption', flag: 'F-MAINT' },
    { c: ['Rent benchmark, 3 bedrooms, a month', X(4602) + ' (whole San Jose area, utilities included, fiscal year 2026)', usd(p0.aRent2026) + ' assumed'], status: 'verified', src: ['HUD1'], flag: 'F-RENT-A' },
    { c: ['Rent benchmark, 4 bedrooms, a month', X(5010), usd(p0.aRent2026) + ' assumed'], status: 'verified', src: ['HUD1'], flag: 'F-RENT-A' }
  ];
  const costB = [
    { c: ['Property tax bill, 2025', '', usd(p0.bBill2025)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Tax rate, fiscal year 2026-27', '1.18162182%', '1.18162182%'], status: 'verified', src: ['L1'] },
    { c: ['Home insurance, a year', '', usd(br.bInsurance) + ' (owner’s guess)'], status: 'brief', src: ['CDI'], flag: 'F-INSURANCE' },
    { c: ['Water, a month, three units', '', `${usd(br.bWaterMonthly[0])} to ${usd(br.bWaterMonthly[1])}`], status: 'brief', flag: 'F-UTIL' },
    { c: ['Electricity, a month', '', `${usd(br.bPowerMonthly[0])} to ${usd(br.bPowerMonthly[1])}`], status: 'brief', flag: 'F-UTIL' },
    { c: ['Maintenance and repairs, a year', '', usd(p0.bMaintenance)], status: 'assumption', flag: 'F-MAINT' },
    { c: ['Rent from two units, a month', '', usd(br.bRentTwoUnits)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Rent benchmark, 1 and 2 bedrooms, a month', X(2977) + ' and ' + X(3604) + ' (whole San Francisco area, fiscal year 2026)', usd(p0.bUnitRent2026) + ' assumed for the third unit'], status: 'verified', src: ['HUD2'], flag: 'F-RENT-B' },
    { c: ['Allowed yearly rent increase, 1 March 2026 to 28 February 2027', '1.6%, set at 60% of Bay Area inflation', `${pct(p0.rentCapShare, 0)} of inflation each year`], status: 'verified', src: ['R1', 'R3'], flag: 'F-RENTCONTROL' },
    { c: ['Rent for a new tenant in an empty unit', '“There is no limit on how much rent a landlord may first charge”', 'Market rent at the start'], status: 'verified', src: ['R3'] },
    { c: ['Relocation payment if a tenancy is ended so the owner can move in', X(8245) + ' per tenant, at most ' + X(24733) + ' per unit, plus ' + X(5497) + ' for some households', 'Not in the model'], status: 'verified', src: ['R1'] },
    { c: ['Empty Homes Tax', 'Ruled unconstitutional; affirmed on appeal 11 September 2026. Nothing to file or pay unless reversed', 'Not in the model'], status: 'verified', src: ['EHT'] }
  ];
  const insRows = [
    { c: ['Official premium for either home', '', 'The State’s tool shows hypothetical homes only: “If you want to get the exact premium for your home, you will need to contact an agent, broker or insurer representative”'], status: 'unverified', src: ['CDI'], flag: 'F-INSURANCE' },
    { c: ['Wildfire surcharges', '“can range from 15% to over 300%”', 'Not included in the State’s comparison premiums'], status: 'verified', src: ['CDI'] }
  ];
  out['costs.html'] = L.page('costs.html', 'Running costs',
    `Insurance, water, electricity and solar, repairs and rents. Most of these have no official figure for one particular home, so the “official figure” cell is often blank and the amount used comes from the brief or is an assumption.`,
    `
<section aria-labelledby="h-ca"><h2 id="h-ca">Property A (Cupertino)</h2>
${L.table({ caption: 'Property A', head: ['Item', 'Official figure', 'Used in the model'], rows: costA })}
</section>
<section aria-labelledby="h-cb"><h2 id="h-cb">Property B (San Francisco)</h2>
${L.table({ caption: 'Property B', head: ['Item', 'Official figure', 'Used in the model'], rows: costB })}
</section>
<section aria-labelledby="h-ins"><h2 id="h-ins">Insurance</h2>
${L.table({ caption: 'What the Department of Insurance publishes', head: ['Item', 'Official figure', 'Note'], rows: insRows })}
<p>Both ${usd(p0.aInsurance)} figures are the owner’s guesses. Before relying on them, get written quotes: an owner-occupier policy and a landlord policy for Property A, and a policy for a three-unit building for Property B. Earthquake cover is separate and is not in the model.</p>
</section>
`, { description: 'Insurance, utilities, solar, maintenance and rent figures with their sources.' });

  // =========================================================================== PROCESS
  const before = [
    { c: ['Now', 'Read the deed to Property B and the trust that holds Property A. Find out who the successor trustee is and whether the trust lets one heir take the house alone.', '[OWNER], [HEIR], attorney'], status: 'question', src: ['P13'], flag: 'F-TRUST' },
    { c: ['Now and every year', 'Keep Property A as [OWNER]’s principal residence, with the homeowners’ exemption on it. Do not rent it out. If [OWNER] moves to a care facility, the home still counts only while it “is not rented or leased to anyone other than an immediate family member”.', '[OWNER]'], status: 'verified', src: ['P13'] },
    { c: ['Now and every year', 'Do not move Property A into an LLC or other entity. Property held by an entity is not eligible for the exclusion.', '[OWNER], attorney'], status: 'verified', src: ['P13'] },
    { c: ['Now', 'Add up the whole estate and compare it with the federal exclusion. If [OWNER] is a surviving spouse, find out whether the first estate filed a return electing portability.', '[OWNER], attorney'], status: 'verified', src: ['F1', 'F5'], flag: 'F-ESTATE' },
    { c: ['Each January', 'Re-read the federal exclusion for the new year.', '[HEIR]'], status: 'verified', src: ['F1', 'F2'] },
    { c: ['Each odd-numbered February', 'Re-read the Proposition 19 amount. The next change is due on 16 February 2027.', '[HEIR]'], status: 'verified', src: ['P9'] },
    { c: ['Now', 'Collect the purchase papers and depreciation records for Property B, so that the tax on any future sale can be worked out.', '[HEIR]'], status: 'question', src: ['I5'], flag: 'F-BASIS-B' }
  ];
  const after = [
    { c: ['Day of death', 'This date fixes three things: the change of ownership for property tax, the new tax basis, and the start of every deadline below. Order an appraisal of Property A as of this date, with land and building stated separately.', '[TRUSTEE]'], status: 'verified', src: ['TP3', 'I1', 'D1'] },
    { c: ['Within 60 days', 'Serve the trust notification on every beneficiary and heir. Anyone wishing to contest the trust then has 120 days.', '[TRUSTEE]'], status: 'verified', src: ['TP1'] },
    { c: ['Within 150 days', 'File the change in ownership statement for a death (form BOE-502-D) with the assessor of each county where [OWNER] owned real property. San Francisco also asks for the death certificate, the deed and the whole trust.', '[TRUSTEE]'], status: 'verified', src: ['TP2', 'TP3'] },
    { c: ['Within 9 months', 'File federal Form 706 if the estate is over the exclusion, or to pass an unused exclusion to a surviving spouse. Form 4768 gives six more months.', '[TRUSTEE], tax preparer'], status: 'verified', src: ['F4', 'F5'] },
    { c: ['When due', 'File [OWNER]’s final income tax return. Form 56 tells the IRS who is acting for the estate.', '[TRUSTEE]'], status: 'verified', src: ['TP6'] },
    { c: ['Each year the trust has income', 'File the trust’s income tax returns: federal Form 1041, and California Form 541 if gross income is over ' + X(10000) + ' or net income is over ' + X(100) + '.', '[TRUSTEE], tax preparer'], status: 'verified', src: ['TP7', 'TP8'], flag: 'F-1041' },
    { c: ['No California death-tax return', 'California has no estate or inheritance tax and no return to file for one.', '—'], status: 'verified', src: ['C1', 'C2'] }
  ];
  const choice = [
    { c: ['Sell', 'Sell at or near the appraised value so that little or no gain arises. At closing, complete California Form 593 and pay the county transfer tax. Decide beforehand how the money will be invested.', '[TRUSTEE] or [HEIR]'], status: 'verified', src: ['I1', 'C6', 'T1'], flag: 'F-RETURN' },
    { c: ['Sell', 'If the exclusion matters for the months before the sale: it applies only if an heir met the one-year residence rule and filed the homeowners’ exemption claim.', '[HEIR]'], status: 'verified', src: ['P13'] },
    { c: ['Live in it — within 1 year', 'Move in and make it the principal residence. File the homeowners’ exemption claim (form BOE-266) with the Santa Clara County Assessor within one year of the death.', '[HEIR]'], status: 'verified', src: ['P1', 'P13', 'TP4'] },
    { c: ['Live in it — within 3 years', 'File the exclusion claim (form BOE-19-P) within three years of the death, or before any sale to a third party if that is sooner.', '[HEIR]'], status: 'verified', src: ['P1'] },
    { c: ['Live in it — afterwards', 'Stay. If the heir moves out or rents the house, the exclusion ends from the next 1 January and the tax is based on the market value at the date of death, adjusted for inflation.', '[HEIR]'], status: 'verified', src: ['P1', 'P13'] },
    { c: ['Live in it — Property B', 'Property B stops being the household’s principal residence, so its homeowners’ exemption ends. The unit left empty can be let at a market rent; later increases are limited if the Rent Ordinance covers the building.', '[HEIR]'], status: 'verified', src: ['P13', 'R3'], flag: 'F-RENTCONTROL' },
    { c: ['Rent it out', 'No exclusion applies. Expect a new assessment at market value as of the date of death and a bill for the difference. Start depreciation when the house is ready and available to rent.', '[HEIR]'], status: 'verified', src: ['P1', 'B2', 'D1'] },
    { c: ['Any choice', 'If the assessor denies the exclusion or sets a value that looks wrong, there is a right of appeal.', '[HEIR]'], status: 'verified', src: ['P13'] }
  ];
  out['process.html'] = L.page('process.html', 'Inheritance steps',
    `What to do, in order, when a house held in a California trust passes to the next generation. Deadlines are counted from the date of death. People appear as [OWNER] (the parent), [TRUSTEE] (whoever takes over the trust) and [HEIR].`,
    `
<section aria-labelledby="h-timeline"><h2 id="h-timeline">Deadlines at a glance</h2>
<ol class="timeline">
  <li><span>Day 0</span>Date of death: appraisal date, new tax basis, change of ownership</li>
  <li><span>60 days</span>Trust notification to beneficiaries and heirs</li>
  <li><span>150 days</span>Change in ownership statement to each county assessor</li>
  <li><span>9 months</span>Federal estate tax return, if required or to elect portability</li>
  <li><span>1 year</span>Heir moved in and homeowners’ exemption claimed — only if living in Property A</li>
  <li><span>3 years</span>Exclusion claim filed — only if living in Property A</li>
</ol>
</section>
<section aria-labelledby="h-before"><h2 id="h-before">1. Before the inheritance</h2>
${L.table({ caption: 'Things to do while [OWNER] is alive', head: ['When', 'What to do', 'Who'], rows: before })}
</section>
<section aria-labelledby="h-after"><h2 id="h-after">2. After the death, whatever is decided</h2>
${L.table({ caption: 'Required steps and deadlines', head: ['When', 'What to do', 'Who'], rows: after })}
</section>
<section aria-labelledby="h-choice"><h2 id="h-choice">3. Then, depending on the choice for Property A</h2>
${L.table({ caption: 'Steps for each choice', head: ['Choice', 'What to do', 'Who'], rows: choice })}
<p class="note">This is a checklist drawn from official pages, not legal advice. Court supervision, creditor claims, a spouse’s share and the terms of the trust itself can add steps; the attorney who administers the trust will know which apply.</p>
</section>
`, { description: 'Step-by-step process and deadlines for inheriting a house through a California trust.' });

  // =========================================================================== LAW WATCH
  const law = [
    { c: ['Federal estate tax exclusion', X(15000000) + ' for 2026 under Public Law 119-21; ' + X(15480000) + ' for 2027', 'Sets whether any estate tax is due. Later years are not published.'], status: 'verified', src: ['F3', 'F2'], flag: 'F-ESTATE' },
    { c: ['Bill to repeal the federal estate tax (H.R. 1301)', 'Introduced 13 February 2025 and referred to committee the same day. No later action listed.', 'Would remove the tax if enacted. Not law.'], status: 'verified', src: ['LW2'] },
    { c: ['California estate or inheritance tax', 'None, and the statute adopted by voters in 1982 forbids one.', 'No state death tax to plan for.'], status: 'verified', src: ['C1', 'C2'] },
    { c: ['Initiative to repeal the Proposition 19 rules for family transfers', 'Failed to qualify for the ballot: signatures fell short, 18 May 2026.', 'The parent-to-child rules on the Taxes page remain in force.'], status: 'verified', src: ['LW1'] },
    { c: ['Proposition 19 guidance', 'The Board of Equalization’s letter of 3 August 2026 applies the rules described on the Taxes page.', 'Confirms the rules as of that date.'], status: 'verified', src: ['P13'] },
    { c: ['Proposition 19 amount', X(1044586) + ' until 15 February 2027; a new figure applies from 16 February 2027.', 'A larger amount lowers the tax if an heir lives in Property A.'], status: 'verified', src: ['P9'] },
    { c: ['Property tax inflation factor', '1.02 for the 2026-27 roll.', 'The yearly rise in taxed value for both homes.'], status: 'verified', src: ['B1'] },
    { c: ['3 November 2026 ballot: Proposition 3', 'Makes permanent the existing higher income-tax rates for high incomes; yes 60.6% in unofficial returns.', 'California’s top rates on a very large gain would not expire in 2031.'], status: 'verified', src: ['BAL', 'V3'], flag: 'F-BALLOT' },
    { c: ['3 November 2026 ballot: Proposition 42', 'Prohibits new state taxes on personal property and retroactive state taxes; yes 51.6% in unofficial returns.', 'Would bar a state tax on holdings such as investments. Close; not final.'], status: 'verified', src: ['BAL', 'V42'], flag: 'F-BALLOT' },
    { c: ['3 November 2026 ballot: Propositions 40, 41 and 43', 'All three behind in unofficial returns (no 52.8%, 54.9% and 57.3%).', 'No change if the results hold.'], status: 'verified', src: ['BAL'], flag: 'F-BALLOT' },
    { c: ['3 November 2026 ballot: property tax rules', 'No measure on this ballot changes Proposition 13 assessments or the Proposition 19 family-transfer rules.', 'No change.'], status: 'verified', src: ['BAL'] },
    { c: ['San Francisco allowed rent increase', '1.6% from 1 March 2026 to 28 February 2027.', 'Limits rent rises for sitting tenants in covered units of Property B.'], status: 'verified', src: ['R1'] },
    { c: ['San Francisco proposal on banked and capital-improvement increases (file 261020)', 'Would cap them at 10% a year for a time. “Has not been enacted.”', 'Could limit catch-up increases on Property B.'], status: 'verified', src: ['R3'] },
    { c: ['San Francisco Empty Homes Tax', 'Struck down; Court of Appeal affirmed 11 September 2026.', 'No tax on a unit left vacant, unless reversed.'], status: 'verified', src: ['EHT'] },
    { c: ['Solar tariffs', 'Older systems keep their original tariff for 20 years from connection; newer ones are on the Net Billing Tariff.', 'The solar credit on Property A will not last into the 2040s.'], status: 'verified', src: ['N1'], flag: 'F-SOLAR' }
  ];
  out['law.html'] = L.page('law.html', 'Law watch',
    `Rules that have changed recently or could change before the inheritance. Each line says where things stood on ${S.READ} according to the official page linked. Nothing here predicts what a legislature or court will do.`,
    `
${L.table({ caption: 'Pending and recent changes', head: ['Item', 'Where it stood', 'Why it matters here'], rows: law })}
<h2>How to keep this current</h2>
<ul>
  <li>Each January: the federal exclusion for the year (IRS estate tax page).</li>
  <li>Each odd-numbered February: the Proposition 19 amount (Board of Equalization letter).</li>
  <li>After each statewide election: the Secretary of State’s certified results.</li>
  <li>Each March: San Francisco’s allowed rent increase.</li>
</ul>
`, { description: 'Pending and recent law changes that affect the inheritance plan.' });

  // =========================================================================== WHY PAGES DIFFER
  const cmp = [
    { c: ['Root pages: <code>cupertino.html</code>, <code>san-francisco.html</code>, <code>decision.html</code>', '3% a year', 'A 1.30% and B 1.22% of taxed value; the page calls the second a third-party estimate', '', '5.5%', 'Sell A unless an heir needs to live there; keep B'] },
    { c: ['<code>pages/</code> and <code>docs/</code>', 'A 3.5%, B 3.0% a year', 'A 1.25%; B 1.18268325%', '6%', '5%', 'Sell A; keep B'] },
    { c: ['<code>dashboard/</code>', 'A 2.87%, 4.29% or 5.75% a year (index history)', 'A 1.1622% plus fixed charges; B 1.18162182%', '4.65%, 8.00% or 11.34%', '6%', 'Sell A; keep B'] },
    { c: ['<code>site/</code> and the landing page', '3.5% a year', 'The 2025 bill divided by taxed value: about 1.34% for A and 2.14% for B', '6% less 1% for tax', '6%', 'Sell A and reinvest'] },
    { c: ['<code>model/</code> (these pages)', `A ${Object.keys(SC.house).map(k => pct(SC.house[k].aGrowth, 2)).join(', ')} a year (index history)`, `A ${pct(p0.aRate, 4)} plus fixed charges; B 1.18162182%`, Object.keys(SC.returns).map(k => pct(SC.returns[k].investReturn, 2)).join(', '), pct(p0.sellCost, 0), 'Sell A unless someone will live there; keep B'] }
  ].map(r => Object.assign(r, { status: 'caution', flag: 'F-COMPARE' }));
  const sum = c.reportSummary, rep = c.report;
  const areas = Object.keys(sum.byArea).sort();
  const privRows = areas.map(a => {
    const v = sum.byArea[a];
    return { c: [`<code>${L.esc(a)}</code>`, String(v.files), String(v.zip || 0), String(v.unrounded || 0), String(v.street || 0), String(v.parcel || 0), String(v.email || 0), String(v.phone || 0)], status: 'caution', flag: 'F-PRIVACY' };
  });
  if (!privRows.length) privRows.push({ c: ['Whole repository', '0', '0', '0', '0', '0', '0', '0'], status: 'caution', flag: 'F-PRIVACY' });
  const brokenAreas = Object.keys(sum.brokenByArea);
  out['compare.html'] = L.page('compare.html', 'Why pages differ',
    `Nine sessions were given the same brief at the same time, and several of them published pages in this repository. The pages agree on what to do and disagree on the dollar amounts, because they assume different growth rates, tax rates and returns. This page sets the assumptions side by side and reports a scan of everything the repository publishes.`,
    `
<section aria-labelledby="h-cmp"><h2 id="h-cmp">Assumptions side by side</h2>
${L.table({ caption: 'Main assumptions of each set of pages, as read in the repository when these pages were built', head: ['Pages', 'House-price growth', 'Property tax rate', 'Investment return', 'Selling cost', 'Recommendation printed'], rows: cmp,
    note: 'A blank cell means the figure was not found on those pages. Only the files were read; nothing in them was changed.' })}
<h3>What the differences do</h3>
<ul>
  <li><strong>Growth rate.</strong> At 3% a year Property A is worth about ${usd(E.marketValue(p0.aValue2026, 0.03, 2045))} in 2045; at 3.5%, ${usd(E.marketValue(p0.aValue2026, 0.035, 2045))}; at ${pct(p0.aGrowth, 2)}, ${usd(E.marketValue(p0.aValue2026, p0.aGrowth, 2045))}. Every later figure scales with this.</li>
  <li><strong>Tax rate.</strong> Dividing a bill by the taxed value counts the fixed parcel charges as if they grew with the house’s value. After a revaluation to ${usd(base.valueAtDeath)} that overstates the bill: at 1.34% the tax would be ${usd(base.valueAtDeath * 0.0134)}, against ${usd(x.rentY1.propertyTax)} with the published rate plus fixed charges.</li>
  <li><strong>Proposition 19 amount.</strong> It changes every second year by one year’s change in the state house-price index. Holding it flat understates it; these pages apply the scenario’s index change at each adjustment.</li>
  <li><strong>Returns.</strong> A single 5% or 6% return and a range from ${pct(SC.returns.low.investReturn, 2)} to ${pct(SC.returns.high.investReturn, 2)} give very different end balances for “sell and invest”, though selling comes out highest at each of them in the middle house-price case.</li>
</ul>
<p>The <a href="decision.html#calculator">calculator</a> accepts any of these assumptions, so each set of pages can be reproduced and compared on the same footing.</p>
</section>

<section aria-labelledby="h-priv"><h2 id="h-priv">Privacy scan of everything published</h2>
<p>GitHub Pages serves the whole repository, so the scan covers every file, not only these pages. It counts patterns; it does not store or print what it matched. ${rep.filesScanned} files were scanned.</p>
${L.table({ caption: 'Number of matches by folder', head: ['Folder', 'Files with a match', 'Five-digit numbers in the Bay Area ZIP range', 'Numbers within $5 of a rounded brief figure', 'Street-address-like', 'Parcel-number-like', 'E-mail', 'Phone-like'], num: [1, 2, 3, 4, 5, 6, 7], rows: privRows,
    note: 'Folders with no match are not listed; <code>model/</code> has none. A “number within $5 of a rounded brief figure” is most likely an original figure that was not rounded to $10. Phone-like strings in other folders may be public agency lines.' })}
<div class="callout">
<h3>What this means</h3>
<ul>
  <li>The repository is public. ZIP codes narrow each property to a small area, and an exact assessed value or tax bill can be matched against public assessor records.</li>
  <li>Earlier commits contain the brief’s figures before rounding. Rounding the current files does not remove them from the history.</li>
  <li>These model pages use only the city names and figures rounded to $10 that were already published, and add no ZIP code, neighbourhood, year-by-year bill history or contact detail.</li>
  <li>Only the owner can close the gap: make the repository private, or rewrite its history and republish.</li>
</ul>
</div>
</section>

<section aria-labelledby="h-links"><h2 id="h-links">Link check of everything published</h2>
<p>${rep.htmlPages} HTML pages were checked for internal links and anchors that do not resolve. Broken: <strong>${rep.brokenLinks.length}</strong>${brokenAreas.length ? ' (' + brokenAreas.map(a => `${L.esc(a)} ${sum.brokenByArea[a]}`).join(', ') + ')' : ''}. The check runs with <code>node model/check.js</code>.</p>
</section>
`, { description: 'Why the sets of pages in this repository show different figures, and a privacy and link scan of the whole repository.' });

  // =========================================================================== SOURCES
  const topics = [];
  for (const s of S.SOURCES) { let t = topics.find(z => z.name === s.topic); if (!t) topics.push(t = { name: s.topic, list: [] }); t.list.push(s); }
  out['sources.html'] = L.page('sources.html', 'Sources',
    `${S.SOURCES.length} official pages, each opened on ${S.READ}. “What was read there” is a quotation (in quotation marks) or a figure from that page. Blogs, law-firm articles, property websites and search summaries were not used.`,
    topics.map(t => `<section><h2>${L.esc(t.name)}</h2>
${L.table({ caption: L.esc(t.name), head: ['Page', 'What was read there'], rows: t.list.map(s => ({ id: 'S-' + s.id, c: [`${L.esc(s.publisher)}<br><span class="small">${L.esc(s.title)}</span>`, L.esc(s.says)], status: 'verified', src: [s.id] })) })}
</section>`).join('\n') + `
<section><h2>Not retrieved</h2>
<p>These were looked for and not found on an official page that could be opened. The related cells are blank and the items are on the <a href="flagged.html">Flagged</a> page: an insurance premium for either home; HUD’s fiscal year 2027 rents; the income threshold for federal Form 1041; San Francisco’s tax rate for fiscal year 2025-26; water and electricity tariff sheets; Santa Clara County’s tax rates for fiscal year 2026-27.</p>
</section>`, { description: 'Register of official sources used by the model.' });

  // =========================================================================== FLAGGED
  const dict = {
    bTaxIfReassessed: usd(B.taxIfReassessed), bBill: usd(p0.bBill2025), excl2026: X(p0.estateExclusion2026), excl2027: X(p0.estateExclusion2027),
    estateIndexing: pct(p0.estateIndexing, 2), aValue: usd(p0.aValue2026), bValue: usd(p0.bValue2026), bTaxMax: usd(B.taxMax),
    aRate: pct(p0.aRate, 4), aFixed: usd(aFixed), bFixed: usd(B.fixed), p19: X(p0.prop19Amount2025), p19per100k: usd(100000 * p0.aRate),
    inflation: pct(p0.inflation, 2), aMaint: usd(p0.aMaintenance), bMaint: usd(p0.bMaintenance), aRent: usd(p0.aRent2026),
    beRent: c.beRent === null ? 'more than any plausible rent' : usd(c.beRent), split: pct(p0.aBuildingShare, 0), vacancy: pct(p0.vacancy, 0),
    sellCost: pct(p0.sellCost, 0), sellPoint: usd(0.01 * base.valueAtDeath), ratePoint: usd(0.0001 * base.valueAtDeath)
  };
  const fill = s => s.replace(/\{(\w+)\}/g, (m, k) => { if (!(k in dict)) throw new Error('No value for {' + k + '}'); return dict[k]; });
  const kindStatus = { question: 'question', unverified: 'unverified', assumption: 'assumption', caution: 'caution' };
  const levels = [['high', 'Can change the answer'], ['medium', 'Changes the amounts noticeably'], ['low', 'Small effect']];
  out['flagged.html'] = L.page('flagged.html', 'Flagged for review',
    `Everything that could not be confirmed on an official page, every assumption in the model, and every question that only the family or their advisers can answer. ${FL.FLAGS.length} items. Nothing on this list was filled in by guesswork: where a value is missing the tables leave it blank or say plainly that it is an assumption.`,
    levels.map(([lv, title]) => {
      const list = FL.FLAGS.filter(f => f.level === lv);
      return `<section><h2>${title} <span class="count">${list.length}</span></h2>
${L.table({ caption: title, head: ['Item', 'Why it is flagged', 'Effect', 'How to settle it'],
        rows: list.map(f => ({ id: f.id, c: [L.esc(fill(f.title)), L.esc(fill(f.why)), L.esc(fill(f.effect)), L.esc(fill(f.fix))], status: kindStatus[f.kind], src: f.src, flag: f.id })) })}
</section>`;
    }).join('\n'), { description: 'Unverified items, assumptions and open questions.' });

  // =========================================================================== METHOD
  const showVal = f => {
    if (f.kind === 'pct') return pct(f.value, f.digits === undefined ? 1 : f.digits);
    if (f.kind === 'choice') { const ch = f.choices.find(z => z[0] === f.value); return L.esc(ch ? ch[1] : String(f.value)); }
    if (f.kind === 'usd' || f.kind === 'usdm') return (f.exact ? X(f.value) : usd(f.value)) + (f.kind === 'usdm' ? ' a month' : '');
    return String(f.value);
  };
  const inputRows = I.FIELDS.map(f => ({ id: 'm-' + f.key, c: [L.esc(f.label) + `<br><span class="small">${L.esc(f.group)}</span>`, showVal(f), L.esc(f.note || '')], status: f.status, src: f.src, flag: f.flag }));
  const scenRows = Object.keys(SC.house).map(k => ({ c: [`House prices, ${SC.house[k].label.toLowerCase()}`, L.esc(SC.house[k].window), `A ${pct(SC.house[k].aGrowth, 2)}; B ${pct(SC.house[k].bGrowth, 2)}; California ${pct(SC.house[k].caHpiChange, 2)}`], status: 'calculated', src: ['H1', 'H2', 'H3'], flag: 'F-GROWTH' }))
    .concat(Object.keys(SC.returns).map(k => ({ c: [`Investment return, ${SC.returns[k].label.toLowerCase()}`, L.esc(SC.returns[k].basis), pct(SC.returns[k].investReturn, 2)], status: 'calculated', src: ['TSP', 'TSPG'], flag: 'F-RETURN' })));
  out['method.html'] = L.page('method.html', 'Method',
    `How the figures are produced, every input with its value and origin, the simplifications, and how to rebuild and re-check the pages.`,
    `
<section aria-labelledby="h-how"><h2 id="h-how">How the model works</h2>
<ol>
  <li><strong>Values.</strong> Each home’s market value grows at a fixed yearly rate from the owner’s estimate for November 2026.</li>
  <li><strong>Property tax.</strong> Bill = tax rate × taxed value + fixed charges. Taxed value rises ${pct(p0.prop13Factor, 0)} a year until ownership changes. Fixed charges are the 2025 bill minus rate × assessed value, and rise with inflation.</li>
  <li><strong>Inheritance.</strong> The death is placed on 1 January of the chosen year. With no exclusion the taxed value becomes the market value. With the parent-to-child exclusion it becomes market value minus the Proposition 19 amount (never less than the old taxed value).</li>
  <li><strong>Proposition 19 amount.</strong> Starts at the official figure and is raised on 16 February of each odd-numbered year by one year of the scenario’s California house-price change.</li>
  <li><strong>Sell and invest.</strong> Sale at the value at death, less selling cost; no gain. The proceeds grow at the investment return. At the end the growth is taxed once at the gains rate.</li>
  <li><strong>Rent it out.</strong> Rent grows with inflation, less vacancy. Costs: property tax on full value, insurance, repairs, manager. Depreciation is the building share of the value at death over 27.5 years; a loss is carried forward and used against later rent or the final gain. Yearly cash goes into the same kind of investment account. At the end the house is sold: depreciation is taxed back at the recapture rate, the rest of the gain at the gains rate.</li>
  <li><strong>Live in it.</strong> Costs: property tax with the exclusion, insurance, repairs, water and power. Income: rent, after tax, from the unit left in Property B, starting at the market level and then rising at ${pct(p0.rentCapShare, 0)} of inflation. The yearly shortfall is drawn from an investment account, so its cost includes the growth given up. At the end the house is sold; the first ${usd(p0.homeSaleExclusion)} of gain is not taxed.</li>
  <li><strong>Comparison.</strong> All three are measured at the same date after selling everything and paying tax. “Yearly price of living in it” is the level yearly amount that, invested at the same return, would close the gap to selling.</li>
  <li><strong>Estate tax.</strong> 40% of the estate above the exclusion. The exclusion is official for 2026 and 2027 and then grows at ${pct(p0.estateIndexing, 2)} a year. It is the same under all three choices and is shown separately.</li>
  <li><strong>Rounding.</strong> Calculations keep full precision; every dollar figure shown in the analysis is rounded to the nearest $10. Official amounts on the reference pages are quoted exactly.</li>
</ol>
</section>
<section id="inputs" aria-labelledby="h-inputs"><h2 id="h-inputs">Every input</h2>
${L.table({ caption: 'Inputs, their values and where they come from', head: ['Input', 'Value', 'Basis'], num: [1], rows: inputRows })}
${L.table({ caption: 'Scenarios', head: ['Scenario', 'Period or basis', 'Rates'], rows: scenRows,
    note: 'Growth rates are compound annual changes between the index values listed on the Sources page.' })}
</section>
<section aria-labelledby="h-simple"><h2 id="h-simple">Simplifications</h2>
<ul>
  <li>One flat tax rate for each kind of income; no brackets, deductions, or alternative minimum tax. Investment growth is taxed once, at the end.</li>
  <li>The loss made by selling the inherited house (the selling cost) is not counted as a tax saving. That makes “sell and invest” look slightly worse than it is.</li>
  <li>No mortgage on either property, no earthquake insurance, no large one-off repairs, no cost of moving.</li>
  <li>Property B’s own rent, costs and value are the same under every choice for Property A and are left out of that comparison. Losing Property B’s ${X(7000)} homeowners’ exemption when the household moves is ignored (under $100 a year).</li>
  <li>A rental loss is used against the final gain at the gain’s rate rather than against other income.</li>
  <li>Rent on the unit left in Property B rises at the allowed rate for the whole period, as if the first tenant stayed.</li>
  <li>The federal estate tax is computed without deductions or lifetime gifts.</li>
</ul>
</section>
<section aria-labelledby="h-build"><h2 id="h-build">Rebuild and check</h2>
<pre><code>node model/build.js                 # writes the pages from model/src
node --test model/test/*.test.js    # ${c.testCount || '21'} tests of the calculations
node model/check.js                 # links, privacy patterns, $10 rounding, a source on every row</code></pre>
<p>No packages are installed and nothing is loaded from other websites. The calculation code is <code>model/src/engine.js</code>; the same file runs in the browser calculator. Built ${c.builtAt}.</p>
</section>
`, { description: 'Method, inputs and simplifications of the model.' });

  return out;
};
