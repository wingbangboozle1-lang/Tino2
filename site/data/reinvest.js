/*
  After-tax return of each place the sale proceeds could go, and what each does to the plan.
  Session 9caf8551, 2026-11-12.

  Rules for this file, checked by scripts/validate.js:
  - Every rate, yield and historical return carries the official page it came from (source key in sources.js).
  - Every dollar result is produced by the published engine MODEL.decision() — no second model — and is
    rounded to the nearest $10 by MODEL.round10 before it leaves this file.
  - Nothing is inferred. A figure no official source publishes (a fund's future return, a municipal-bond
    yield for this household) is left null and rendered as a blank with a review flag.
*/
(function () {
  const R = window.MODEL;
  const round10 = R.round10;

  // ---------------------------------------------------------------------------
  // 1. What each destination pays, after tax, at official current benchmarks.
  //    Nominal per-year rates. "afterTax" is what the household keeps after the
  //    taxes that actually fall on that kind of income.
  // ---------------------------------------------------------------------------
  const DESTINATIONS = [
    {
      id: "cash",
      name: "Bank savings account",
      what: "Deposits at an FDIC-insured bank or credit union",
      grossNow: 0.0038, grossSource: "fdicRates", grossNote: "national average savings rate, October 2026",
      afterTax: 0.0038 * (1 - 0.331), afterTaxBasis: "0.38% × (1 − 33.1%)",
      taxRule: "Interest is ordinary income: federal rates up to 37% and California treats it as ordinary income, so the model's 33.1% combined scenario rate is applied. A 3.8% federal net investment income tax is added on investment income above the federal thresholds; it is inside the 33.1% scenario, not added again.",
      taxSource: "irsInterest", taxSource2: "irsNIIT",
      protection: "$250,000 per depositor, per bank, per ownership category",
      protectionSource: "fdic",
      risk: "No market loss within the insured limit; the risk is that the rate does not keep up with prices.",
      flag: null,
      scaleNote: "A balance above $250,000 at one bank is uninsured above that amount unless it sits in another ownership category or another bank."
    },
    {
      id: "bills",
      name: "Treasury bills, held to maturity",
      what: "Bills bought at auction or in the secondary market and held to maturity",
      grossNow: 0.0456, grossSource: "ustCurve", grossNote: "1-year Treasury par yield, 10 November 2026",
      afterTax: 0.0456 * (1 - 0.331), afterTaxBasis: "4.56% × (1 − 33.1%)",
      taxRule: "Interest is taxable federally and exempt from state and local income tax, which is the one place this household gains against a bank account: California cannot tax it. The 33.1% scenario rate is applied unchanged, so the comparison is conservative.",
      taxSource: "irsInterest", taxSource2: "treasuryDirectBills",
      protection: "Full faith and credit of the United States; also exempt from California income tax",
      protectionSource: "treasuryDirectBills",
      risk: "Reinvestment risk: the yield at each maturity is unknown; the 4.56% is today's one-year rate, not a forecast.",
      flag: null,
      scaleNote: "No practical limit for this household; minimum purchase $100, increments of $100."
    },
    {
      id: "notes",
      name: "Treasury notes, 10-year",
      what: "10-year Treasury notes, held to maturity",
      grossNow: 0.0498, grossSource: "ustCurve", grossNote: "10-year Treasury par yield, 10 November 2026",
      afterTax: 0.0498 * (1 - 0.331), afterTaxBasis: "4.98% × (1 − 33.1%)",
      taxRule: "Same rule as bills: federal tax on the interest, no California tax. A note sold before maturity can lose value when rates rise, so the return shown assumes it is held to maturity.",
      taxSource: "irsInterest", taxSource2: "treasuryDirectNotes",
      protection: "Full faith and credit of the United States; exempt from California income tax",
      protectionSource: "treasuryDirectNotes",
      risk: "Price risk if sold early; the coupon is fixed for ten years while prices may rise faster.",
      flag: null,
      scaleNote: null
    },
    {
      id: "municipal",
      name: "California municipal bonds",
      what: "Bonds of California state and local governments",
      grossNow: null, grossSource: "caMuniExempt", grossNote: "no official yield for this household",
      afterTax: null, afterTaxBasis: "blank — no official yield for a California bond of this household's term and credit",
      taxRule: "Interest on bonds issued by California or its local governments is excluded from California income; interest on most municipal bonds is also excluded from federal income. The exemption covers interest, not a gain on selling the bond.",
      taxSource: "caMuniExempt", taxSource2: "irsInterest",
      protection: "Credit of the issuing city, county or state — not the United States",
      protectionSource: "irsInterest",
      risk: "Credit risk and interest-rate risk; the tax exemption is only worth as much as the yield it gives up.",
      flag: "No official source publishes a yield for a bond this household would buy. The rate is left blank rather than estimated. Compare the taxable-equivalent yield of a real bond against the 4.98% Treasury note before choosing.",
      scaleNote: null
    },
    {
      id: "fund",
      name: "Broad share fund held for the long run",
      what: "A diversified, low-cost fund of United States shares, held across decades",
      grossNow: null, grossSource: "investorRisk", grossNote: "no official forward return exists",
      afterTax: null, afterTaxBasis: "blank — no official forward return; the page shows 5% (the published assumption) and the sensitivity around it",
      taxRule: "Dividends and realised gains are taxed federally at capital-gain rates plus the 3.8% net investment income tax where thresholds are exceeded, and California taxes them as ordinary income with no preferential rate. The model's 5% for shares is stated as after tax.",
      taxSource: "irsCapGains", taxSource2: "ftbCapGains",
      protection: "None against market loss. SIPC protects custody only: $500,000, of which $250,000 may be cash.",
      protectionSource: "sipc",
      risk: "Value can fall and stay down for a decade; the recorded history below shows how far.",
      flag: "No official body publishes a forward return for shares. The 5% used on this site is an assumption, shown as such and tested across 3% to 7%.",
      scaleNote: null
    }
  ];

  // ---------------------------------------------------------------------------
  // 2. Recorded history, official series only. Rates are nominal per year.
  //    CAGR = (last / first)^(1/years) - 1, computed from the published series.
  // ---------------------------------------------------------------------------
  const SERIES = [
    {
      id: "share",
      name: "United States share prices (OECD share-price index)",
      unit: "index",
      source: "fredSharePrice",
      first: { year: 1970, value: 4.852874 },
      last: { year: 2025, value: 191.0952 },
      cagr: 0.0689,
      worst: { years: "2007–2009", change: -0.369 },
      best: { years: "1994–2000", change: 1.532 },
      real: null,
      note: "Nominal share-price index (2015 = 100), not a total-return index: dividends are not included, so a fund's recorded return is higher than this line. The 37% fall is measured on annual averages, so it understates the peak-to-trough fall within the year."
    },
    {
      id: "cpi",
      name: "Consumer prices (all urban consumers, annual average)",
      unit: "index",
      source: "fredCpi",
      first: { year: 1970, value: 38.825 },
      last: { year: 2025, value: 321.943 },
      cagr: 0.0393,
      worst: null,
      best: null,
      real: null,
      note: "The same series the site's black-swan pages replay. Prices rose about eight times over these 55 years (321.943 ÷ 38.825)."
    },
    {
      id: "oneYear",
      name: "One-year Treasury yield (annual average)",
      unit: "% a year",
      source: "fredOneYear",
      first: { year: 1970, value: 6.43 },
      last: { year: 2025, value: 3.95 },
      cagr: null,
      worst: { years: "August 1981", change: null, level: 16.72 },
      best: null,
      real: null,
      note: "The average level, not a compound return: a deposit rolled at this rate earns roughly this each year. The highest monthly reading in the series is 16.72% (August 1981); the lowest is 0.10% (2010, 2020 and 2021)."
    },
    {
      id: "tenYear",
      name: "Ten-year Treasury yield (annual average)",
      unit: "% a year",
      source: "fredTenYear",
      first: { year: 1970, value: 7.35 },
      last: { year: 2025, value: 4.23 },
      cagr: null,
      worst: null,
      best: null,
      real: null,
      note: "Annual average of the ten-year constant-maturity yield, the series already used for the model's reinvestment rate in the black-swan pages."
    }
  ];

  // ---------------------------------------------------------------------------
  // 3. Current official thresholds that decide how much tax each destination
  //    carries and how much of a balance protection covers.
  // ---------------------------------------------------------------------------
  const THRESHOLDS = [
    {
      item: "Federal long-term capital-gain rate, top",
      why: "Caps the federal tax on a gain on shares, or on the house after its date-of-death basis, at 20% for the incomes involved.",
      value: "20% above $533,400 of taxable income (single, 2025); 15% above $48,350",
      source: "irsCapGains"
    },
    {
      item: "Federal net investment income tax",
      why: "A further 3.8% on investment income above the threshold; it is already inside the model's 33.1% scenario rate and is not added again.",
      value: "3.8% on the lesser of net investment income or MAGI above $200,000 (single) / $250,000 (joint)",
      source: "irsNIIT"
    },
    {
      item: "California top marginal rate on capital gains and interest",
      why: "California adds its own tax on top of the federal rate; the 1% surtax applies above $1,000,000 of taxable income.",
      value: "13.3% (12.3% bracket plus the 1% mental-health surtax above $1,000,000)",
      source: "caSurtax",
      source2: "ftbRates2025"
    },
    {
      item: "California treatment of capital gains",
      why: "No preferential rate: the state rate applies in full to gains, which is why the combined rate is far above the 15% federal headline.",
      value: "No lower rate: gains are taxed as ordinary income",
      source: "ftbCapGains"
    },
    {
      item: "California tax on Treasury interest",
      why: "The one tax advantage a Treasury has over a bank account for a California resident.",
      value: "Exempt from state and local income tax",
      source: "irsInterest",
      source2: "treasuryDirectBills"
    },
    {
      item: "California tax on in-state municipal interest",
      why: "The exemption is why a lower-yielding California bond can beat a taxable one, and why out-of-state bonds lose the advantage.",
      value: "Excluded from California gross income",
      source: "caMuniExempt"
    },
    {
      item: "FDIC deposit insurance",
      why: "A single account above $250,000 leaves the excess uninsured unless it is split across banks or ownership categories.",
      value: "$250,000 per depositor, per bank, per ownership category",
      source: "fdic"
    },
    {
      item: "SIPC protection",
      why: "Protects custody of shares, not their value; a fall in the market is not covered.",
      value: "$500,000 per customer, of which up to $250,000 may be cash; custody only, not market loss",
      source: "sipc"
    },
    {
      item: "Treasury bills",
      why: "Minimum purchase $100 in $100 increments; interest is federally taxable and exempt from state and local tax.",
      value: "Minimum $100, in $100 increments; federal tax on interest, no state or local tax",
      source: "treasuryDirectBills"
    }
  ];

  // ---------------------------------------------------------------------------
  // 4. The model at each after-tax return. Every figure comes from the published
  //    engine, so the rows agree with the Best plan and Decision pages at 5%.
  // ---------------------------------------------------------------------------
  const INHERIT_YEARS = [2040, 2045, 2050];
  const RETURN_ROWS = [
    { key: "cash", label: "Bank savings at today's national average", rate: 0.0038 * (1 - 0.331), howSource: "fdicRates" },
    { key: "bills", label: "Treasury bills at today's one-year yield", rate: 0.0456 * (1 - 0.331), howSource: "ustCurve" },
    { key: "notes", label: "Treasury notes at today's ten-year yield", rate: 0.0498 * (1 - 0.331), howSource: "ustCurve" },
    { key: "base", label: "The published assumption", rate: 0.05, howSource: "investorRisk", assumption: true },
    { key: "high", label: "A good run for shares", rate: 0.07, howSource: "investorRisk", assumption: true }
  ];

  function decisionAt(year, rate) {
    return R.decision({ ...R.BASE, inheritYear: year, portfolioGross: rate + 0.01, portfolioTaxDrag: 0.01 }, 10, "4BR");
  }

  function results() {
    return INHERIT_YEARS.map(year => {
      const rows = RETURN_ROWS.map(row => {
        const d = decisionAt(year, row.rate);
        return {
          key: row.key,
          label: row.label,
          rate: row.rate,
          source: row.howSource,
          assumption: Boolean(row.assumption),
          sell: round10(d.sell.terminal),
          rent: round10(d.rent.terminal),
          live: round10(d.live.terminal),
          sellAheadOfRent: round10(d.sell.terminal - d.rent.terminal),
          sellAheadOfLive: round10(d.sell.terminal - d.live.terminal),
          winner: d.winner
        };
      });
      const base = decisionAt(year, 0.05);
      return {
        year,
        netSaleProceeds: round10(base.sell.initialNet),
        inheritValue: round10(base.transfer.market),
        rows,
        breakEvenRent: breakEven(year, "rent"),
        breakEvenLive: breakEven(year, "live"),
        aboveRange: breakEven(year, "rent") > 0.07
      };
    });
  }

  // The after-tax return at which selling stops finishing first.
  function breakEven(year, against) {
    let lo = 0.0001;
    let hi = 0.25;
    for (let i = 0; i < 200; i += 1) {
      const mid = (lo + hi) / 2;
      const d = decisionAt(year, mid);
      if (d.sell.terminal > d[against].terminal) hi = mid;
      else lo = mid;
    }
    return (lo + hi) / 2;
  }

  // ---------------------------------------------------------------------------
  // 5. First-year income on the net sale proceeds, before any spending.
  // ---------------------------------------------------------------------------
  function incomeRows(year) {
    const d = decisionAt(year, 0.05);
    const principal = d.sell.initialNet;
    return [
      { key: "cash", label: "Bank savings, national average", rate: 0.0038, afterTax: 0.0038 * (1 - 0.331), source: "fdicRates" },
      { key: "bills", label: "Treasury bills, one-year", rate: 0.0456, afterTax: 0.0456 * (1 - 0.331), source: "ustCurve" },
      { key: "notes", label: "Treasury notes, ten-year", rate: 0.0498, afterTax: 0.0498 * (1 - 0.331), source: "ustCurve" },
      { key: "base", label: "Published 5% assumption", rate: null, afterTax: 0.05, source: "investorRisk", assumption: true }
    ].map(row => ({
      ...row,
      principal: round10(principal),
      yearIncome: row.rate == null ? null : round10(principal * row.rate),
      afterTaxIncome: round10(principal * row.afterTax),
      monthly: round10(principal * row.afterTax / 12)
    }));
  }

  window.REINVEST = {
    CHECKED: "12 November 2026",
    DESTINATIONS,
    SERIES,
    THRESHOLDS,
    RETURN_ROWS,
    INHERIT_YEARS,
    results,
    breakEven,
    decisionAt,
    incomeRows
  };
})();
