/* Observed economic conditions, with sources. This file contains official published
   series and simple derived statistics. It contains no household data and no forecast.
   Every number here can be recomputed from the cited public series. */
(function () {
  'use strict';

  const SRC = Object.freeze({
    cpiHistory: 'https://fred.stlouisfed.org/series/CPIAUCNS',
    cpiRelease: 'https://www.bls.gov/news.release/archives/cpi_01122023.htm',
    cbo: 'https://www.cbo.gov/publication/61882',
    prop13: 'https://www.boe.ca.gov/proptaxes/pdf/lta26002.pdf',
    prop13cap: 'https://boe.ca.gov/proptaxes/pdf/lta25023.pdf',
    pmms: 'https://www.freddiemac.com/pmms',
    usgs: 'https://pubs.usgs.gov/publication/fs20163020',
    hpi: 'https://fred.stlouisfed.org/series/ATNHPIUS41940Q',
    sfRent: 'https://www.sf.gov/reports--current-rates-including-rent-increase-relocation-sec-deposit',
    rental: 'https://www.irs.gov/publications/p527',
    water: 'https://www.cupertino.gov/Residents/Utilities/Water',
    cdi: 'https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/',
    cdieq: 'https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/eq-ins.cfm',
    trustbasis: 'https://www.irs.gov/pub/irs-drop/rr-23-02.pdf',
    hr1301: 'https://www.congress.gov/bill/119th-congress/house-bill/1301',
    prop19: 'https://www.boe.ca.gov/pdf/pub801.pdf'
  });

  /* Annual-average CPI-U, not seasonally adjusted. FRED series CPIAUCNS (BLS data).
     Downloaded 13 November 2026. 2026 is excluded because the year is incomplete. */
  const CPI_ANNUAL = Object.freeze({
    1990: 130.658, 1991: 136.192, 1992: 140.317, 1993: 144.458, 1994: 148.225,
    1995: 152.383, 1996: 156.850, 1997: 160.517, 1998: 163.008, 1999: 166.575,
    2000: 172.200, 2001: 177.067, 2002: 179.875, 2003: 183.958, 2004: 188.883,
    2005: 195.292, 2006: 201.592, 2007: 207.342, 2008: 215.303, 2009: 214.537,
    2010: 218.056, 2011: 224.939, 2012: 229.594, 2013: 232.957, 2014: 236.736,
    2015: 237.017, 2016: 240.007, 2017: 245.120, 2018: 251.107, 2019: 255.657,
    2020: 258.811, 2021: 270.970, 2022: 292.655, 2023: 304.702, 2024: 313.689,
    2025: 321.943
  });

  /* Official Proposition 13 inflation factors, assessment years 1976-77 to 2026-27,
     as published in BOE Letter To Assessors 2026/002. Index 0 = 1976-77. */
  const PROP13_FACTORS = Object.freeze([
    1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.01, 1.02, 1.02, 1.02, 1.02, 1.02,
    1.02, 1.02, 1.02, 1.02, 1.02, 1.02, 1.0119, 1.0111, 1.02, 1.02, 1.01853, 1.02,
    1.02, 1.02, 1.02, 1.01867, 1.02, 1.02, 1.02, 1.02, 1.02, 0.99763, 1.00753, 1.02,
    1.02, 1.00454, 1.01998, 1.01525, 1.02, 1.02, 1.02, 1.02, 1.01036, 1.02, 1.02,
    1.02, 1.02, 1.02
  ]);

  function round10(v) {
    if (!Number.isFinite(v)) return null;
    return Math.sign(v) * Math.round(Math.abs(v) / 10) * 10;
  }
  function pct(v, d) {
    return (100 * v).toFixed(d === undefined ? 2 : d) + '%';
  }
  function mean(a) { return a.reduce((x, y) => x + y, 0) / a.length; }
  function median(a) {
    const s = [...a].sort((x, y) => x - y), m = Math.floor(s.length / 2);
    return s.length % 2 ? s[m] : (s[m - 1] + s[m]) / 2;
  }
  function stdev(a) {
    const m = mean(a);
    return Math.sqrt(a.reduce((s, x) => s + (x - m) * (x - m), 0) / (a.length - 1));
  }
  function cagr(first, last, years) { return Math.pow(last / first, 1 / years) - 1; }

  /* ---- Derived inflation evidence, recomputed from CPI_ANNUAL ---- */
  const cpiYears = Object.keys(CPI_ANNUAL).map(Number).sort((a, b) => a - b);
  const cpiChanges = [];
  for (let i = 1; i < cpiYears.length; i += 1) {
    const y = cpiYears[i];
    cpiChanges.push({ year: y, change: CPI_ANNUAL[y] / CPI_ANNUAL[cpiYears[i - 1]] - 1 });
  }
  const cpiValues = cpiChanges.map(x => x.change);
  const inflation = {
    series: cpiChanges,
    first: cpiYears[0],
    last: cpiYears[cpiYears.length - 1],
    count: cpiValues.length,
    mean: mean(cpiValues),
    median: median(cpiValues),
    sd: stdev(cpiValues),
    min: Math.min(...cpiValues),
    max: Math.max(...cpiValues),
    minYear: cpiChanges.find(x => x.change === Math.min(...cpiValues)).year,
    maxYear: cpiChanges.find(x => x.change === Math.max(...cpiValues)).year,
    above: t => cpiValues.filter(x => x > t).length,
    below: t => cpiValues.filter(x => x < t).length,
    longRunCagr: cagr(CPI_ANNUAL[cpiYears[0]], CPI_ANNUAL[cpiYears[cpiYears.length - 1]],
      cpiYears[cpiYears.length - 1] - cpiYears[0])
  };
  /* Observed cumulative price change across the full window, for scale. */
  inflation.fullWindowMultiple = CPI_ANNUAL[cpiYears[cpiYears.length - 1]] / CPI_ANNUAL[cpiYears[0]];

  /* ---- Derived Proposition 13 evidence, recomputed from PROP13_FACTORS ---- */
  const factorChanges = PROP13_FACTORS.map(f => f - 1);
  const atCap = PROP13_FACTORS.filter(f => Math.abs(f - 1.02) < 1e-9).length;
  let compound = 1;
  for (const f of PROP13_FACTORS) compound *= f;
  const prop13 = {
    firstYear: '1976-77',
    lastYear: '2026-27',
    count: PROP13_FACTORS.length,
    atCap,
    atCapShare: atCap / PROP13_FACTORS.length,
    belowCap: PROP13_FACTORS.length - atCap,
    mean: mean(factorChanges),
    compoundMultiple: compound,
    compoundAnnual: Math.pow(compound, 1 / PROP13_FACTORS.length) - 1,
    negativeYears: PROP13_FACTORS.map((f, i) => ({ year: 1976 + i, f })).filter(x => x.f < 1)
  };

  /* ---- Scenario bands used by the planning tables. These are SCENARIOS, not forecasts. ---- */
  const BANDS = Object.freeze([
    { key: 'low', label: 'Low', inflation: 0.020, note: 'Near the Federal Reserve long-run goal cited by CBO and below the 50-year observed average.' },
    { key: 'observed', label: 'Observed 35-year average', inflation: 0.026, note: 'The 1991-2025 annual-average CPI-U mean on this page, rounded to a tenth of a percent.' },
    { key: 'prop13', label: 'Prop 13 cap reference', inflation: 0.020, note: 'The statutory ceiling, not a price forecast. Shown because the assessed base cannot outrun it absent reassessment.' },
    { key: 'high', label: 'High', inflation: 0.040, note: 'Sustained inflation well above the observed average but below the 2021-2023 experience.' },
    { key: 'severe', label: 'Severe', inflation: 0.070, note: 'Near the worst single year in the observed record (2022: 8.00%). Sustained for decades this is severe.' }
  ]);

  /* Growth of a nominal amount under a band, and the real (deflated) value.
     real = nominal growth / inflation growth. */
  function project(band, years, nominalGrowth) {
    const infl = Math.pow(1 + band.inflation, years);
    const nom = Math.pow(1 + nominalGrowth, years);
    return { inflationMultiple: infl, nominalMultiple: nom, realMultiple: nom / infl };
  }

  window.CONDITIONS = {
    SRC, CPI_ANNUAL, PROP13_FACTORS, BANDS,
    inflation, prop13, round10, pct, cagr, project
  };
})();
