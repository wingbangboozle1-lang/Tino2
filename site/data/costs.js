/*
  Operating-cost evidence layer (session aa1f073e, checked 2026-11-11).

  Every figure here was read on the official page named in SOURCES on 2026-11-11.
  Nothing in this file is a household bill, a quote, or an appraisal:
    - "tariff"     = a published, adopted or regulator-approved rate schedule;
    - "benchmark"  = an official survey average that is not property specific;
    - "scenario"   = arithmetic applied to tariff rates at a stated usage;
    - "unverified" = no official source confirms it, so the value stays blank.
  Dollar amounts of $1,000 or more are rounded to the nearest $10 before display.
*/
(function () {
  Object.assign(window.SOURCES, {
    ocSjw: {
      agency: "San Jose Water Company (CPUC-regulated)",
      title: "Advice Letter 628 — Schedule No. 1, General Metered Service, effective July 1, 2026",
      url: "https://www.sjwater.com/media/oycbyo3o/adv-628-web.pdf",
      note: "Checked 2026-11-11: service charge $78.64/month for 5/8x3/4-inch and 3/4-inch meters; quantity rate $4.9692 (0–6 Ccf), $7.4167 (6+–12 Ccf), $14.1659 (over 12 Ccf) per Ccf; territory includes portions of Cupertino."
    },
    ocSjwApproved: {
      agency: "San Jose Water Company (CPUC-regulated)",
      title: "Advice Letter 628-A — approved tariff sheets (CPUC Sheet 2402-W/2403-W)",
      url: "https://www.sjwater.com/media/dm3lribs/san-jose-water-company-al-628-a-approved.pdf",
      note: "Checked 2026-11-11: approved sheets carry the same July 1, 2026 rates under D.24-12-077 and Resolution 2026-22."
    },
    ocSjwBillExample: {
      agency: "San Jose Water Company (CPUC-regulated)",
      title: "Advice Letter 628 — customer notice, average residential bill",
      url: "https://www.sjwater.com/media/oycbyo3o/adv-628-web.pdf",
      note: "Checked 2026-11-11: \"the average base residential bill (volume and service charges) with a 3/4-inch meter and using 10 CCF per month would increase by approximately $4.95 or 3.62% per month, from $136.78 at present rates, to $141.73 from July 1, 2026\"."
    },
    ocSjwWholesale: {
      agency: "San Jose Water Company (CPUC-regulated)",
      title: "Advice Letter 628 — wholesale cost increase",
      url: "https://www.sjwater.com/media/oycbyo3o/adv-628-web.pdf",
      note: "Checked 2026-11-11: Valley Water adopted a groundwater (pump tax) rate of 2,673 dollars per acre-foot and a purchased-water rate of 2,788 dollars per acre-foot effective July 1, 2026, each 223 dollars per acre-foot above the July 1, 2025 rates; the filing passes through a 3.71% revenue increase."
    },
    ocCupertinoWater: {
      agency: "City of Cupertino",
      title: "Water — service providers and municipal system lease",
      url: "https://www.cupertino.gov/Residents/Utilities/Water",
      note: "Checked 2026-11-11: three systems serve the city — California Water Service (northeast), San Jose Water Company's own system (southeast), and the City-owned system (west) operated by San Jose Water Company under a lease extended to 2036. The City states that since January 2017 municipal-system customers have had a lower cost of water than customers of SJWC's own system in Cupertino."
    },
    ocSfpucSchedule: {
      agency: "San Francisco Public Utilities Commission",
      title: "Rate Schedules & Fees for Water and Sewer Service, FY 2026-27 and FY 2027-28",
      url: "https://www.sfpuc.gov/sites/default/files/accounts-and-services/Rates_Schedule_Water_Sewer_2026-7.pdf",
      note: "Checked 2026-11-11: adopted by Resolutions 26-0064 (water) and 26-0066 (sewer) on April 28, 2026, effective July 1, 2026. Schedule W-1B multi-family water $12.03 per unit for the first 3 units per dwelling unit and $12.91 thereafter; monthly water service charge $19.65 (5/8 in), $24.93 (3/4 in), $35.53 (1 in); Schedule A residential wastewater $6.62 service charge plus $20.74 per discharge unit; multi-family flow factor 95%."
    },
    ocSfpuc218: {
      agency: "San Francisco Public Utilities Commission",
      title: "Proposition 218 notice — proposed water and sewer rates, FY 2027 and FY 2028",
      url: "https://www.sfpuc.gov/accounts-services/water-power-sewer-rates/proposed-water-sewer-rates-2026/proposition-218-notice",
      note: "Checked 2026-11-11: for the average single-family household the schedule represents a combined monthly bill increase of about $21 and $23 (about 12.6% and 12.5% a year) in FY 2027 and FY 2028; stormwater component for residential parcels $12.63 / $19.66 / $29.55 a month by parcel-size tier in FY 2027; drought surcharges up to 32%."
    },
    ocPgeMinBill: {
      agency: "Pacific Gas and Electric Company (CPUC-regulated)",
      title: "How rates work — minimum bill charges",
      url: "https://www.pge.com/en/account/rate-plans/how-rates-work.html",
      note: "Checked 2026-11-11: \"The Minimum Delivery Charge ... is $10.12 for Non-CARE customers, $5.06 for CARE customers\"; all customers are responsible for it, net-metered customers pay it monthly, and it is credited against the amount owed at the annual True-Up."
    },
    ocPgeSolarPlan: {
      agency: "Pacific Gas and Electric Company (CPUC-regulated)",
      title: "Solar Billing Plan",
      url: "https://www.pge.com/en/clean-energy/solar/getting-started-with-solar/solar-billing-plan.html",
      note: "Checked 2026-11-11: \"The 20-year NEM legacy program rules are tied to the system, not the owner\" — a buyer inherits the remaining years; customers whose legacy period ends move to the Solar Billing Plan at their True-Up; residential Solar Billing Plan customers are enrolled in the Electric Home rate plan, which includes a Base Services Charge."
    },
    ocPgeNbt: {
      agency: "Pacific Gas and Electric Company (CPUC-regulated)",
      title: "Advice Letter 6848-E — creating the Net Billing Tariff per CPUC Decision 22-12-056",
      url: "https://www.pge.com/tariffs/assets/pdf/adviceletter/ELEC_6848-E.pdf",
      note: "Checked 2026-11-11: the Net Billing Tariff eliminates netting of imports and exports; export compensation follows the Avoided Cost Calculator and varies by hour, month and day type; NBT customers remain subject to the minimum bill or fixed charge of their otherwise applicable rate and to four non-bypassable charges; the legacy period under NBT is 9 years."
    },
    ocPgeLegacy: {
      agency: "Pacific Gas and Electric Company (CPUC-regulated)",
      title: "Advice Letter 6395-E — NEM 20-year transition period",
      url: "https://www.pge.com/tariffs/assets/pdf/adviceletter/ELEC_6395-E-B.pdf",
      note: "Checked 2026-11-11: under D.14-03-041 and D.16-01-044 service continues for 20 years from the original year of interconnection (permission to operate) and customers \"may not restart the 20-year period by switching to the successor tariff\"."
    },
    ocCdiCompare: {
      agency: "California Department of Insurance",
      title: "Compare Insurance Premiums — survey basis",
      url: "https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/index.cfm",
      note: "Checked 2026-11-11: surveys are run under Insurance Code sections 12959, 10234.6 and 10192.20; \"The results of these surveys are not premium quotes\"; the Department is a regulator and cannot provide quotes."
    },
    ocCdiTool: {
      agency: "California Department of Insurance",
      title: "2026 Homeowners Insurance Comparison Tool",
      url: "https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:20",
      note: "Checked 2026-11-11: premiums are for hypothetical risks in selected ZIP codes; wildfire-related surcharges \"can range from 15% to over 300%\" and are not reflected; an exact premium requires an agent, broker or insurer."
    },
    ocCdiProfiles: {
      agency: "California Department of Insurance",
      title: "Homeowners Profiles used in the premium survey",
      url: "https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/homeowners-profile.cfm",
      note: "Checked 2026-11-11: survey profiles are defined by coverage amount ($500,000 to $1,000,000 for the larger frame-construction profiles), deductible and age of home."
    },
    ocNaic: {
      agency: "National Association of Insurance Commissioners",
      title: "Dwelling Fire, Homeowners Owner-Occupied, and Homeowners Tenant and Condominium/Cooperative Unit Owner's Insurance Report: Data for 2023 (July 2026)",
      url: "https://content.naic.org/sites/default/files/publication-hmr-zu-homeowners-report.pdf",
      note: "Checked 2026-11-11: California data in this report are provided by the California Department of Insurance; premiums for earthquake coverage are excluded; HO-3 is 79.45% of owner-occupied exposures countrywide; dwelling-fire policies are a separate, more limited product. State average-premium tables were not reachable in the fetched extract, so no state figure is published here."
    },
    ocBlsMaint: {
      agency: "U.S. Bureau of Labor Statistics, Consumer Expenditure Survey (retrieved from FRED, Federal Reserve Bank of St. Louis)",
      title: "Expenditures: Maintenance, Repairs, Insurance, Other Expenses for Owned Dwelling, Home Owner (CXUOWNEXPENLB1702M)",
      url: "https://fred.stlouisfed.org/series/CXUOWNEXPENLB1702M",
      note: "Checked 2026-11-11: annual average per home-owning consumer unit — 2020, 3,267 dollars; 2021, 3,587; 2022, 3,911; 2023, 3,974; 2024, 4,481. National survey average, not a Bay Area or property-specific amount."
    }
  });

  const round10 = v => (v === null || v === undefined || !Number.isFinite(v)) ? null : Math.round(v / 10) * 10;
  const money = (v, dp) => v === null ? "—" : "$" + Number(v).toLocaleString("en-US", { minimumFractionDigits: dp || 0, maximumFractionDigits: dp || 0 });

  // ---- Property A: San Jose Water Company, Schedule No. 1, effective 2026-07-01 ----
  const SJW = { service: 78.64, t1: 4.9692, t2: 7.4167, t3: 14.1659 };
  function sjwMonthly(ccf) {
    const t1 = Math.min(ccf, 6), t2 = Math.min(Math.max(ccf - 6, 0), 6), t3 = Math.max(ccf - 12, 0);
    return SJW.service + t1 * SJW.t1 + t2 * SJW.t2 + t3 * SJW.t3;
  }

  // ---- Property B: SFPUC adopted FY2026-27 schedules ----
  // Water Schedule W-1B (multi-family), wastewater Schedule A, simplified residential stormwater.
  const SFPUC = { serviceWater: 24.93, t1: 12.03, t2: 12.91, serviceSewer: 6.62, discharge: 20.74, flowFactor: 0.95, stormTier2: 19.66 };
  function sfpucMonthly(ccf, units) {
    const tier1Allowance = 3 * (units || 3);
    const t1 = Math.min(ccf, tier1Allowance), t2 = Math.max(ccf - tier1Allowance, 0);
    const water = SFPUC.serviceWater + t1 * SFPUC.t1 + t2 * SFPUC.t2;
    const sewer = SFPUC.serviceSewer + ccf * SFPUC.flowFactor * SFPUC.discharge;
    return { water, sewer, storm: SFPUC.stormTier2, total: water + sewer + SFPUC.stormTier2 };
  }

  // ---- Escalation evidence (official, published) ----
  const ESCALATION = [
    { label: "SFPUC combined single-family bill, FY 2027", value: "about +12.6%", basis: "Adopted two-year schedule", src: "ocSfpuc218" },
    { label: "SFPUC combined single-family bill, FY 2028", value: "about +12.5%", basis: "Adopted two-year schedule", src: "ocSfpuc218" },
    { label: "San Jose Water volumetric rates, July 1 2026", value: "+3.69%", basis: "Wholesale-cost offset filing", src: "ocSjw" },
    { label: "San Jose Water service charges, July 1 2026", value: "+3.70%", basis: "Wholesale-cost offset filing", src: "ocSjw" },
    { label: "Valley Water groundwater charge to the retailer", value: "2,450 → 2,673 dollars per acre-foot", basis: "Pass-through driver of the 2026 retail increase", src: "ocSjwWholesale" },
    { label: "Valley Water purchased-water charge to the retailer", value: "2,565 → 2,788 dollars per acre-foot", basis: "Pass-through driver of the 2026 retail increase", src: "ocSjwWholesale" },
    { label: "Temporary drought surcharge, SFPUC", value: "up to 32% on volumetric rates", basis: "Applies only when the Commission declares a shortage stage", src: "ocSfpuc218" },
    { label: "Maintenance/repairs/insurance per owner household, 2020 → 2024", value: "$3,270 → $4,480 (+37%)", basis: "National survey average, rounded to $10", src: "ocBlsMaint" }
  ];

  // ---- Solar legacy: 20 years from permission to operate ----
  const SOLAR_LEGACY = [2014, 2016, 2018, 2020, 2022, 2024].map(y => ({ pto: y, ends: y + 20 }));

  window.COSTS = {
    round10, money, SJW, SFPUC, sjwMonthly, sfpucMonthly, ESCALATION, SOLAR_LEGACY,
    pgeMinimumDelivery: 10.12,
    pgeMinimumDeliveryCare: 5.06,
    blsMaintenance: { 2020: 3267, 2021: 3587, 2022: 3911, 2023: 3974, 2024: 4481 },
    // Projection helper: constant real growth applied to a rounded annual base.
    project(base, rate, years) { return base * Math.pow(1 + rate, years); }
  };
})();

/* Session 60ca3e1f — California Department of Insurance 2026 premium survey, read on 12 Nov 2026 (append-only block).
   The survey prices HYPOTHETICAL homes. It is not a quote, and no figure here is a premium for either property.
   Each row was transcribed from the Department's result page (link in SOURCES under `src`); the transcription
   and the statistics are in research/60ca3e1f/build_insurance_survey.py. "median" is the middle of the list of
   insurers that show a premium, calculated here; "lowest" and "highest" are amounts as published. */
(function () {
  const P = (place, age, dwelling, listed, priced, lowest, median, highest, atOrBelow1500, src) =>
    ({ place, age, dwelling, listed, priced, lowest, median, highest, atOrBelow1500, src });
  const INSURANCE_SURVEY = {
    readOn: "12 Nov 2026", effective: "1 May 2026", deductible: 2500,
    profiles: [
      P("Cupertino", 40, 500000, 37, 35, 790, 1383, 3371, 20, "cdiSurveyCup40_500"),
      P("Cupertino", 40, 750000, 37, 35, 1167, 2017, 4901, 4, "cdiSurveyCup40_750"),
      P("Cupertino", 40, 1000000, 37, 35, 1543, 2690, 6430, 0, "cdiSurveyCup40_1000"),
      P("Cupertino", 70, 1000000, 36, 34, 1598, 2741, 4968, 0, "cdiSurveyCup70_1000"),
      P("San Francisco · Sunset", 40, 1000000, 37, 35, 1328, 3353, 10384, 1, "cdiSurveySun40_1000"),
      P("San Francisco · Sunset", 70, 1000000, 36, 34, 1413, 3191, 10384, 1, "cdiSurveySun70_1000")
    ],
    // Earthquake, single-family profile: a rate per $1,000 of coverage, not a premium.
    earthquake: [
      { place: "Cupertino", listed: 40, withRate: 19, lowest: 1.15, median: 3.10, highest: 15, throughCea: 13, footnotes: 8, src: "cdiSurveyEqCup" },
      { place: "San Francisco · Sunset", listed: 40, withRate: 19, lowest: 1.13, median: 3.29, highest: 15, throughCea: 13, footnotes: 8, src: "cdiSurveyEqSun" }
    ],
    // California FAIR Plan, residential policies in force at 30 September of each year, as published.
    fairPlan: {
      years: [2022, 2023, 2024, 2025, 2026], src: "fairPlanZip",
      rows: [
        { label: "ZIP 95014 · Property A", counts: [74, 51, 119, 213, 227] },
        { label: "ZIP 94122 · Property B", counts: [15, 21, 81, 129, 154] },
        { label: "California", counts: [265909, 320572, 449832, 621234, 665673] }
      ]
    },
    // Statewide earned premium and earned exposures, all residential policy forms, as published (SB 824 workbook).
    statewide: { from: 2018, to: 2023, premiumFrom: 8334249009, exposuresFrom: 11375891, premiumTo: 14217212455, exposuresTo: 12580970, src: "cdiSb824Workbook" }
  };
  INSURANCE_SURVEY.statewide.growth = Math.pow(
    (INSURANCE_SURVEY.statewide.premiumTo / INSURANCE_SURVEY.statewide.exposuresTo) /
    (INSURANCE_SURVEY.statewide.premiumFrom / INSURANCE_SURVEY.statewide.exposuresFrom),
    1 / (INSURANCE_SURVEY.statewide.to - INSURANCE_SURVEY.statewide.from)) - 1;

  /* Re-runs the published model (site/data/model.js, unchanged) for Property A with another 2026 premium and,
     when `growth` is given, with insurance alone growing at that yearly rate instead of the model's rate.
     The model reads the premium once for each of the ten rented years and once for each of the ten lived-in years;
     the Proxy hands it the amount that makes the model's own formula land on the intended premium for that year.
     If the model reads the premium a different number of times, the result is refused (null) rather than shown. */
  function insuranceCase(M, inheritYear, premium2026, growth) {
    const base = { ...M.BASE, inheritYear };
    let d;
    if (growth == null) {
      d = M.decision({ ...base, aInsuranceAnnual: premium2026 }, 10, "4BR");
    } else {
      const years = [];
      for (let pass = 0; pass < 2; pass += 1) for (let t = 1; t <= 10; t += 1) years.push(inheritYear + t);
      let reads = 0;
      const cfg = new Proxy(base, { get(target, key) {
        if (key !== "aInsuranceAnnual") return target[key];
        const n = years[Math.min(reads, years.length - 1)] - target.startYear;
        reads += 1;
        return premium2026 * Math.pow(1 + growth, n) / Math.pow(1 + target.expenseInflation, n);
      } });
      d = M.decision(cfg, 10, "4BR");
      if (reads !== years.length) return null;
    }
    const premiums = d.live.yearly.map(r => r.insurance);
    return {
      firstYear: premiums[0], tenYears: premiums.reduce((a, b) => a + b, 0),
      sellAheadOfRent: d.sell.terminal - d.rent.terminal, sellAheadOfLive: d.sell.terminal - d.live.terminal,
      winner: d.winner
    };
  }

  window.COSTS.INSURANCE_SURVEY = INSURANCE_SURVEY;
  window.COSTS.insuranceCase = insuranceCase;
})();

/* Session 60ca3e1f — two older notes brought up to date on 2026-11-12. The original wording is kept; a sentence is added. */
window.SOURCES.ocCdiTool.note += " Read again 12 Nov 2026: the result pages open by direct address and were read for both survey locations; see the survey rows above.";
window.SOURCES.ocCdiProfiles.note += " Read again 12 Nov 2026: the homeowners profiles run from $250,000 to $1,000,000 of dwelling cover; there is no profile for a rented building of two to four units.";
