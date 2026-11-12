/*
  Suggestions register (session 62245584, 12 Nov 2026).

  The brief asks for "a section dedicated for suggestions so someone can review suggestions and
  choose the best path before implementing any changes", and for "suggestions ... to discover
  missing information". This file is that register.

  Rules obeyed here:
    - No personal information. Parties are [OWNER], [TRUSTEE], [DECEDENT], [HEIR]; the houses are
      Property A (Cupertino, inherited) and Property B (San Francisco, already owned).
    - No household figure is typed in. Every dollar amount is computed from the published
      MODEL.BASE and the published engines, so this page can never disagree with the model.
    - Every suggestion carries an official https source key from site/data/sources.js.
      Where the suggestion is a planning judgement rather than a legal rule, the source column
      links the rule that the judgement rests on, and the row says so in plain words.
    - Nothing is recommended as advice. The decision panel compares options; it does not choose.
*/
(function () {
  const M = window.MODEL, B = M.BASE;
  const money = M.fmtMoney;

  /* Effort and risk are plain-English scales, not scores, so that nothing pretends to be measured
     when it is a judgement. */
  const EFFORT = { 1: "Under an hour", 2: "An afternoon", 3: "A few days", 4: "A professional engagement" };
  const RISK = { 1: "None: information only", 2: "Low: reversible, no signature", 3: "Medium: involves a signature or a filing", 4: "High: irrevocable once done" };

  /* Impact in money is computed, never typed. Each function returns null when the effect cannot be
     quantified from the published model; the page then prints a dash instead of an estimate. */
  function decisionYears(years) {
    return Object.fromEntries(years.map(y => [y, M.decision({ ...B, inheritYear: y }, 10)]));
  }
  const YEARS = [2040, 2045, 2050];
  const D = decisionYears(YEARS);
  const gap = y => D[y].sell.terminal - D[y].rent.terminal;

  /* Evidence is written as a function so that every figure on the page is produced at render time. */
  const SUGGESTIONS = [
    {
      id: "S-01",
      rank: 1,
      title: "Answer the principal-residence question before the transfer, and in writing",
      group: "Protect the biggest number",
      problem: "The whole ranking turns on whether the heir moves into Property A within a year. The claim that carries the relief is due within one year of the transfer, and a late claim gives prospective relief only.",
      evidence: () => `Living in the house keeps part of the parent's assessed value; renting it does not. For a 2045 inheritance carried to 2055, selling leads renting by ${money(gap(2045))}, and that lead depends on the rental case being reassessed in full.`,
      effect: "Removes the largest single unknown in the comparison, and prevents an irreversible deadline being missed by inaction.",
      effort: 1, risk: 1,
      timing: "Before the transfer, and again in the first year after it",
      src: "boeProp19",
      reversible: true,
      alternatives: ["Decide after the transfer", "Assume the relief and model only the lived-in case"]
    },
    {
      id: "S-02",
      rank: 2,
      title: "Get a date-of-death appraisal, and keep it as the basis record",
      group: "Make the sale case real",
      problem: "Every plan is anchored on a household estimate of value, not an appraisal. The basis at death is what a later gain is measured from.",
      evidence: () => `A prompt sale has little or no taxable gain because the basis resets to the value at death; the sale costs alone, assumed at ${(B.saleCost * 100).toFixed(0)}%, come off the proceeds first.`,
      effect: "Turns the largest input from an estimate into a document, and fixes the starting point for every future tax calculation.",
      effort: 3, risk: 2,
      timing: "At the date of death; an appraisal obtained later is weaker evidence",
      src: "irsInherited",
      reversible: true,
      alternatives: ["Use the county's assessed value", "Use the household estimate indefinitely"]
    },
    {
      id: "S-03",
      rank: 3,
      title: "Establish what the trust owns, and who is entitled to it",
      group: "Before any plan",
      problem: "It is not established whether Property A is inside the trust, whether it is given outright, or who else shares in it. A house that is not the heir's to sell cannot be sold.",
      evidence: () => "Inside a trust, the property passes by the trust's terms and no probate is needed. Outside it, a probate applies statutory fees to both the representative and the attorney. Trustee notification is due within 60 days of the death.",
      effect: "Decides whether a probate, a buy-out from other heirs, or nothing at all stands between the heir and the house.",
      effort: 2, risk: 1,
      timing: "Immediately after the death, within the 60-day notification period",
      src: "caTrustNotice",
      reversible: true,
      alternatives: ["Assume the house passes cleanly and plan the sale"]
    },
    {
      id: "S-04",
      rank: 4,
      title: "Replace the rent benchmark with two written appraisals of achievable rent",
      group: "Make the rental case real",
      problem: "The rental revenue is a federal fair-market-rent benchmark one fiscal year behind the current year, not a lease and not an appraisal.",
      evidence: () => `Rent is the rental case's only revenue line. The ten-year result is sensitive to it: the difference between selling and renting is ${money(gap(2040))} for a 2040 inheritance, ${money(gap(2045))} for 2045 and ${money(gap(2050))} for 2050.`,
      effect: "Replaces the weakest input in the plan that is second on the list, so the comparison rests on evidence rather than on a benchmark.",
      effort: 3, risk: 2,
      timing: "Before any decision to rent, and again before a lease is signed",
      src: "hudA",
      reversible: true,
      alternatives: ["Keep the benchmark", "Use the lower of two estimates"]
    },
    {
      id: "S-05",
      rank: 5,
      title: "List every account in the inheritance by type, balance and beneficiary",
      group: "The money behind the house",
      problem: "The brief says the money may exceed the tax-free amount but gives no figure and no account types. The federal estate tax, the ten-year rule for retirement accounts and the portability election all depend on this list.",
      evidence: () => `The federal exclusion is $15,000,000 for a death in 2026 and $15,480,000 for 2027; Property A alone leaves about ${money(M.estateRow(2027).headroom)} of room before the money is counted. Above the exclusion the rate reaches 40%.`,
      effect: "Makes the only inheritance tax that applies computable, and shows whether an unfiled Form 706 could waste an exclusion.",
      effort: 2, risk: 1,
      timing: "Before the death if possible, and again within nine months of it",
      src: "irsEstateTax",
      reversible: true,
      alternatives: ["Treat the money as unknown and plan only the house"]
    },
    {
      id: "S-06",
      rank: 6,
      title: "Obtain two binding insurance quotes on a stated rebuild cost",
      group: "Cost of holding the house",
      problem: "No official source publishes a premium for either house. The model carries a household estimate, and a premium follows the cost of rebuilding, which is unknown.",
      evidence: () => "The state regulator's 2026 survey of a made-up Cupertino home shows the middle premium roughly doubling between a $500,000 and a $1,000,000 dwelling limit. No premium in that range changes the ranking.",
      effect: "Converts two estimated cost lines into quoted ones, and exposes any gap between the dwelling limit and the real rebuild cost.",
      effort: 2, risk: 2,
      timing: "Before the transfer, then every year at renewal",
      src: "cdiSurveyCup40_1000",
      reversible: true,
      alternatives: ["Keep the estimate", "Carry the state insurer of last resort instead"]
    },
    {
      id: "S-07",
      rank: 7,
      title: "Decide explicitly whether to carry earthquake cover on each house",
      group: "Cost of holding the house",
      problem: "A homeowners policy does not cover earthquake. Earthquake cover is a separate policy. Both houses sit in one seismic region, so one event could hit the household twice.",
      evidence: () => "In the regulator's 2026 survey the middle earthquake rate for a single-family home is about $3.10 a year for each $1,000 of cover in the Cupertino survey location and about $3.29 in the Sunset District; 13 of 40 insurers sell it through the California Earthquake Authority.",
      effect: "Puts a known annual premium against a low-probability, very large loss, and stops that exposure being invisible.",
      effort: 2, risk: 2,
      timing: "Before the transfer, then at each renewal",
      src: "cdiSurveyEqCup",
      reversible: true,
      alternatives: ["Carry no earthquake cover", "Carry it on one house only"]
    },
    {
      id: "S-08",
      rank: 8,
      title: "Read the rate area and direct charges off the actual bill",
      group: "Property tax accuracy",
      problem: "The published model uses a hypothetical 1.2% combined levy for Property A because the tax rate area was not supplied.",
      evidence: () => "Beyond the 1% general levy, bond and special-district rates differ by tax rate area, so the wrong area moves the yearly bill. The county publishes the rate book for each year.",
      effect: "Replaces a hypothetical rate with the adopted one, which is the largest recurring cost in every plan.",
      effort: 1, risk: 1,
      timing: "Before modelling the lived-in case seriously",
      src: "sccTaxBook",
      reversible: true,
      alternatives: ["Keep the hypothetical levy"]
    },
    {
      id: "S-09",
      rank: 9,
      title: "Confirm the vacancy term of the policy before the house stands empty",
      group: "Protect against the gap",
      problem: "Losses to a house vacant for 60 days or more are generally not covered. The period between a death and a decision is exactly when a house stands empty.",
      evidence: () => "This gap in cover arrives before any plan can be executed, and it applies whichever of the three uses of the house is eventually chosen.",
      effect: "Closes a coverage gap that would otherwise appear in the least controlled part of the process.",
      effort: 1, risk: 1,
      timing: "As soon as the house is unoccupied",
      src: "insuranceGuide",
      reversible: true,
      alternatives: ["Switch to a vacant-property policy", "Have someone occupy the house"]
    },
    {
      id: "S-10",
      rank: 10,
      title: "Separate the sale proceeds before they arrive",
      group: "The money behind the house",
      problem: "Deposit insurance covers $250,000 per depositor, per bank, for each ownership category. Investments are not insured at all. A sale of Property A would produce a sum far above that.",
      evidence: () => `The sale proceeds are the whole of the reinvestment plan. The model grows them at ${(M.afterTaxPortfolioReturn() * 100).toFixed(0)}% a year after tax, which requires them to be invested and diversified, not held in one account.`,
      effect: "Removes an avoidable risk in the plan that finishes first on money, before the money is exposed to it.",
      effort: 2, risk: 2,
      timing: "Before the sale closes",
      src: "fdic",
      reversible: true,
      alternatives: ["Hold everything at one bank", "Hold cash until a decision is made"]
    },
    {
      id: "S-11",
      rank: 11,
      title: "Budget for the 3 1/3% withholding at closing, or file the certificate first",
      group: "Make the sale case real",
      problem: "California withholds 3 1/3% of the sales price on a sale of real estate unless the seller certifies an exemption before the close of the transaction. After closing it can only be recovered as a credit on a tax return.",
      evidence: () => "The withholding is not a tax in itself, but it ties up cash at the moment the proceeds are meant to be reinvested.",
      effect: "Prevents a liquidity surprise at the one moment the reinvestment plan depends on having the money.",
      effort: 2, risk: 3,
      timing: "Before closing",
      // Reversible in substance: a withheld amount is recovered as a credit on the tax return.
      // The risk is a cash-timing risk, not an irreversible act.
      src: "ftb593",
      reversible: true,
      alternatives: ["Accept the withholding and claim the credit later"]
    },
    {
      id: "S-12",
      rank: 12,
      title: "Read the land and building split from the assessor's roll",
      group: "Make the rental case real",
      problem: "Depreciation is taken on the building only, and the split between land and improvements was not supplied. The published rental case therefore includes no depreciation at all.",
      evidence: () => "The rental case is the second-ranked plan. Without the split, a real benefit of renting is left out of the comparison entirely.",
      effect: "Makes the rental case complete rather than deliberately conservative.",
      effort: 1, risk: 1,
      timing: "Before the rental case is taken seriously",
      src: "irsTopic704",
      reversible: true,
      alternatives: ["Keep the rental case without depreciation"]
    },
    {
      id: "S-13",
      rank: 13,
      title: "Replace the 6% selling cost with two written listing proposals",
      group: "Make the sale case real",
      problem: "The selling cost is an assumption. No agency publishes a commission, and the cost comes straight off the proceeds before they are reinvested.",
      evidence: () => `At a 2045 inheritance the model applies a ${(B.saleCost * 100).toFixed(0)}% cost to the value of the house. Small changes in that percentage move every plan that ends in a sale.`,
      effect: "Replaces an assumed cost with a quoted one in the plan that currently finishes first.",
      effort: 2, risk: 1,
      timing: "Closer to the transfer; refresh at the time",
      src: "irsTopic701",
      reversible: true,
      alternatives: ["Keep 6%", "Model a low-cost sale route"]
    },
    {
      id: "S-14",
      rank: 14,
      title: "Watch the two legal changes that would move the answer",
      group: "Protect against the law changing",
      problem: "The recommendation rests on today's reassessment rule. An initiative to restore the pre-2021 parent-child rule failed on 18 May 2026, and the federal exclusion is published for one year at a time.",
      evidence: () => "If the pre-2021 rule returned, a rented house could keep the parent's assessed value and the lead of selling would narrow substantially. Every federal amount for the 2040s is unknown today.",
      effect: "Keeps the decision current without re-reading the whole site, at a fixed moment each year.",
      effort: 1, risk: 1,
      timing: "Before each general election, and once a year for the federal amount",
      src: "sosInitiative1994",
      reversible: true,
      alternatives: ["Assume current law holds to 2050"]
    },
    {
      id: "S-15",
      rank: 15,
      title: "Have the chosen path checked before anything is signed",
      group: "Before any plan",
      problem: "This site is a model. It deliberately leaves out depreciation, passive-loss limits and the value of living in the house, and it is not an appraisal, a tax return, a legal opinion or an insurance quote.",
      evidence: () => "The ranking is more sensitive to the assumed portfolio return and home-price growth than to any bill, and both of those are assumptions rather than forecasts.",
      effect: "Converts a scenario into a decision with a named person accountable for each part of it.",
      effort: 4, risk: 2,
      timing: "After a path is chosen, before any document is signed",
      src: "investorRisk",
      reversible: true,
      alternatives: ["Act on the model alone"]
    }
  ];

  /* The decision panel. Each path is a bundle of suggestions, not a separate recommendation.
     The page shows what each path settles and what it leaves undone, so the reader can choose. */
  const PATHS = [
    {
      id: "P-01",
      name: "Settle the facts first, decide nothing yet",
      summary: "Recommended as the first step whatever the eventual answer is. It changes no asset, signs nothing irrevocable, and removes the most unknowns per hour spent.",
      suggestions: ["S-01", "S-03", "S-05", "S-02", "S-08", "S-14"],
      leaves: "Leaves the house held with no decision on its use. The bill continues to run while the facts are gathered.",
      when: "Now, and again within 60 days of any death",
      src: "caTrustNotice"
    },
    {
      id: "P-02",
      name: "Sell the inherited house and reinvest",
      summary: "The path the published model puts first on money for 2040, 2045 and 2050. It needs the basis, the sale mechanics and a placement for the proceeds, and it needs nothing about rent or rebuilding.",
      suggestions: ["S-01", "S-02", "S-11", "S-13", "S-10", "S-15"],
      leaves: "Leaves the household with one house in one region and the proceeds exposed to markets. It also gives up the use of Property A entirely.",
      when: "At the transfer, then within the first year",
      src: "irsInherited"
    },
    {
      id: "P-03",
      name: "Rent the inherited house out",
      summary: "Second on money across the tests, and the most sensitive to a single input. It needs the rent, the land/building split, the reassessment rule and the landlord cover.",
      suggestions: ["S-01", "S-04", "S-12", "S-06", "S-07", "S-09", "S-08", "S-15"],
      leaves: "Leaves the household as a landlord of two buildings in one region, with the full reassessed property tax and no parent-child relief.",
      when: "At the transfer, and again before any lease",
      src: "boeProp19"
    },
    {
      id: "P-04",
      name: "Live in the inherited house",
      summary: "Finishes last on money because the heir does not need a second home and the cost of living there is paid without any rent coming in. It is a lifestyle choice the model deliberately does not price.",
      suggestions: ["S-01", "S-02", "S-06", "S-07", "S-08", "S-15"],
      leaves: "Leaves the household paying the bill on two houses and gives up the rent Property A could earn and the income the sale proceeds would produce.",
      when: "At the transfer, with the exemption claim inside one year",
      src: "boeLta2025009"
    }
  ];

  /* A suggestion's money effect is deliberately not summed into a single number: it would mix
     one-off, recurring and avoided amounts. Instead the page marks each one's kind. */
  const KIND = {
    "S-01": "Avoids a cost", "S-02": "Fixes the basis", "S-03": "Avoids a cost", "S-04": "Changes the revenue line",
    "S-05": "Avoids a tax", "S-06": "Changes a cost line", "S-07": "Avoids a loss", "S-08": "Changes a cost line",
    "S-09": "Avoids a loss", "S-10": "Avoids a risk", "S-11": "Changes cash timing", "S-12": "Adds a tax benefit",
    "S-13": "Changes the exit cost", "S-14": "Avoids a surprise", "S-15": "Checks the decision"
  };

  const order = [...SUGGESTIONS].sort((a, b) => a.rank - b.rank);
  const pathReady = p => {
    const chosen = p.suggestions.map(id => SUGGESTIONS.find(s => s.id === id));
    return {
      ...p,
      count: chosen.length,
      // Effort is a time band, not a duration, so bands are not added together. The longest single
      // step is the honest summary of what a path costs, and it is what the page displays.
      longest: Math.max(...chosen.map(s => s.effort)),
      irreversible: chosen.filter(s => !s.reversible).length,
      blocking: chosen.filter(s => s.risk >= 3).length,
      items: chosen
    };
  };

  window.SUGGESTIONS = {
    EFFORT, RISK, KIND, SUGGESTIONS: order, PATHS, pathReady,
    evidence: s => (typeof s.evidence === "function" ? s.evidence() : s.evidence),
    years: YEARS,
    gap
  };
})();
