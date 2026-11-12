/* Suggestions register (session a87f8523, 12 November 2026).
   Proposals only: nothing here is applied by reading or selecting it.  No personal information,
   no unrounded household figure, no invented price.  "closes" names an id in site/data/questions.js.
   Where no official price exists the cost field says so instead of guessing. */
window.SUGGESTIONS = {
  checked: "12 November 2026",
  kinds: { site: "Change to this site", research: "Research action", pro: "Professional review", privacy: "Privacy action" },
  items: [
    {
      id: "S01", kind: "site", priority: "High", hours: 0, effort: "Done",
      title: "Publish this suggestions page and a decision-readiness register",
      what: "Two pages: this one, so improvements can be reviewed and chosen before anything is built, and a register of the questions that must be settled first.",
      removes: "The gap between ‘the site has an answer’ and ‘the answer is ready to act on’.",
      closes: [],
      cost: "No charge", risk: "None. It publishes no new private data and changes no model input.",
      status: "done", note: "Published 12 November 2026 by session a87f8523. Registered on the coordination board before the files were touched."
    },
    {
      id: "S02", kind: "research", priority: "High", hours: 4, effort: "3–4 hours",
      title: "Get three written insurance quotes and a rebuild estimate",
      what: "One owner policy for Property A, one landlord policy for Property A, one landlord policy for Property B, plus an earthquake quote for each and a builder’s rebuild-cost figure.",
      removes: "The three blank premiums and the unknown dwelling limit — the largest unverified inputs in the yearly costs.",
      closes: ["Q10", "Q11", "Q20"],
      cost: "Quotes are free; no official price for the policies exists until they are quoted", risk: "A quote is not a contract. Premiums change at renewal and the survey’s benchmark is not a quote.",
      status: "proposed", note: "The regulator’s 2026 survey can be used today as a benchmark range."
    },
    {
      id: "S03", kind: "pro", priority: "High", hours: 3, effort: "One meeting, plus reading",
      title: "Read the trust with the trust attorney",
      what: "Confirm revocable or irrevocable, whether the house is in the schedule of assets, whether the trustee may sell, and whether the house can go to one beneficiary without a buy-out.",
      removes: "The assumption under every figure: that the tax basis resets at death and the trustee can act without probate.",
      closes: ["Q01", "Q02", "Q03", "Q04"],
      cost: "The attorney’s own hourly rate; no official price is published", risk: "None to the site. The finding may change the recommendation, which is the point.",
      status: "proposed", note: "The site already states that it assumes a revocable trust. This checks it."
    },
    {
      id: "S04", kind: "research", priority: "High", hours: 1, effort: "About 1 hour",
      title: "Pull the current property tax bill and match the tax-rate area",
      what: "Read the secured bill and the county rate book to replace the hypothetical 1.2% levy with the parcel’s actual total rate, including bonds and direct charges.",
      removes: "The guess in the property tax line for Property A after reassessment.",
      closes: ["Q06"],
      cost: "No charge — both records are public", risk: "The rate changes with each election, so it has to be re-read after reassessment.",
      status: "proposed", note: "Requires the parcel’s own bill, which is private and is not published here."
    },
    {
      id: "S05", kind: "research", priority: "High", hours: 3, effort: "2–3 hours",
      title: "Get two written rental opinions and confirm the rent-increase rules",
      what: "Two local agents’ opinions on achievable rent, plus a written answer on whether the statewide cap or any local ordinance covers an individually owned single-family home.",
      removes: "The gap between the HUD benchmark and a real lease, and the uncertainty over rent growth.",
      closes: ["Q14"],
      cost: "Opinions are usually free; no official price", risk: "An opinion is not a lease. The legal answer should come from the city or counsel.",
      status: "proposed", note: "The HUD benchmark stays as the neutral cross-check."
    },
    {
      id: "S06", kind: "pro", priority: "High", hours: 2, effort: "One meeting",
      title: "Have a CPA project the sale year and any estate tax",
      what: "Run the year of sale with and without the gain: federal brackets, the 3.8% net investment income tax, California brackets, and the estate return if the estate is near the threshold.",
      removes: "The 33.1% blended rate as a stand-in for the heir’s actual marginal rate.",
      closes: ["Q09", "Q16", "Q17"],
      cost: "The CPA’s own rate; no official price is published", risk: "Projections are estimates; the return is filed on actual numbers.",
      status: "proposed", note: "Ask for the marginal rate on the gain, not an average rate."
    },
    {
      id: "S07", kind: "site", priority: "Medium", hours: 6, effort: "4–6 hours of work",
      title: "Add depreciation and a land/building split to the rented case",
      what: "Model 27.5-year depreciation on the building share only, with the passive-loss limit, and show the recapture when the house is sold.",
      removes: "The largest known omission in the rented comparison. It narrows the gap but, on the current numbers, does not close it.",
      closes: [],
      cost: "No charge — a change to this site only", risk: "Adds complexity; the split between land and building is unknown and would be an assumption.",
      status: "proposed", note: "The Other options page already shows a sensitivity at 20%, 30% and 40% building share."
    },
    {
      id: "S08", kind: "research", priority: "High", hours: 3, effort: "2–3 hours",
      title: "Write a one-page investment policy for the sale proceeds",
      what: "Allocation, expected return and risk, all-in fees, where the money is held, who decides, and the rebalancing rule — before any sale.",
      removes: "The 5%-a-year assumption as an unexplained plug. It is the single largest lever in the sell case.",
      closes: ["Q17"],
      cost: "No charge to write; provider fees are the household’s choice", risk: "A policy can still lose money. It sets the plan, not the outcome.",
      status: "proposed", note: "Compare at least two providers on all-in cost."
    },
    {
      id: "S09", kind: "site", priority: "Medium", hours: 3, effort: "2–3 hours of work",
      title: "Add a deadline calendar for the first twelve months",
      what: "One dated list: trustee notice within 60 days, change-of-ownership statement within 150 days, homeowners’ exemption and exclusion claims, Form 593 before closing, Form 706 at nine months, the Rent Board exemption in December.",
      removes: "The risk of missing a deadline that costs relief, a penalty, or the ability to claim an exclusion.",
      closes: [],
      cost: "No charge", risk: "Dates depend on the death and on local filing practice; the page must link every date to its official source.",
      status: "proposed", note: "The Inheritance page already lists the steps; they are not yet on one dated page."
    },
    {
      id: "S10", kind: "site", priority: "Medium", hours: 3, effort: "3 hours of work, if it applies",
      title: "Add a sibling and buy-out case",
      what: "Model the house passing to two or more beneficiaries: unequal shares under the parent-child rules, a buy-out at market value, and the reassessment that follows.",
      removes: "The single-heir assumption, if it is wrong.",
      closes: [],
      cost: "No charge", risk: "Only worth building if the answer to Q02 shows more than one beneficiary.",
      status: "proposed", note: "The county’s guidance sets out the uneven-distribution condition."
    },
    {
      id: "S11", kind: "site", priority: "Medium", hours: 2, effort: "2 hours of work",
      title: "Add a monitoring calendar for the rules that reset",
      what: "February: the Proposition 19 amount. October: new HUD rents. March: San Francisco’s rent cap and the Rent Board fee. December: the exemption window. Each November: state and local measures. Each renewal: insurance.",
      removes: "Silent drift: figures that were right when checked and are wrong a year later.",
      closes: [],
      cost: "No charge", risk: "A calendar is a reminder, not a verification. Each entry still needs an official page.",
      status: "proposed", note: "The Sources page lists a revalidation cadence; this would put dates and owners beside it."
    },
    {
      id: "S12", kind: "privacy", priority: "High", hours: 1, effort: "15 minutes, plus an owner decision",
      title: "Finish the privacy hardening",
      what: "Turn on GitHub’s e-mail privacy setting, then decide what to do about the commits and old branches that still hold exact household figures: a fresh repository, a private repository, or deletion plus a support request.",
      removes: "The only irreversible risk in the project. Nothing on the site fixes it; only the owner can.",
      closes: [],
      cost: "No charge; a private repository with Pages may need a paid plan", risk: "Rewriting history is irreversible and affects every earlier session’s work.",
      status: "proposed", note: "Published on Flagged for Review since 11 November 2026."
    },
    {
      id: "S13", kind: "site", priority: "Medium", hours: 3, effort: "3 hours of work",
      title: "Produce a printable one-page brief for the professionals",
      what: "One sheet: the two properties, the three choices, the result, the assumptions, the five High questions and the deadlines — addressed to a trustee, a CPA or an assessor, with no private data.",
      removes: "The friction of explaining the project three times to three advisers.",
      closes: [],
      cost: "No charge", risk: "A summary can be read as advice; it must carry the same limits as the site.",
      status: "proposed", note: "The print stylesheet already hides navigation and controls."
    },
    {
      id: "S14", kind: "site", priority: "Low", hours: 3, effort: "3 hours of work",
      title: "Add a single assumptions register with one-click changes",
      what: "Every assumption in one table — growth, inflation, returns, costs, tax rate, sale cost — with the page and the result it feeds, and a link that opens the Decision lab with that one input changed.",
      removes: "Hunting through pages to find which assumption drives which number.",
      closes: [],
      cost: "No charge", risk: "Link-encoded inputs must never carry private figures into a URL that could be shared or logged.",
      status: "proposed", note: "The Decision lab already exposes the inputs; they are not collected in one place."
    },
    {
      id: "S15", kind: "site", priority: "Medium", hours: 4, effort: "4 hours of work",
      title: "Accessibility and mobile pass",
      what: "Skip link, visible focus states, table captions and scope attributes, colour contrast checks, and a mobile layout for the widest tables.",
      removes: "The risk that the person who needs this most cannot read it on a phone or with a screen reader.",
      closes: [],
      cost: "No charge", risk: "Layout changes can hide a column; the runtime test must be extended to catch it.",
      status: "proposed", note: "Not audited by this session; it would need a keyboard and screen-reader test."
    },
    {
      id: "S16", kind: "site", priority: "Low", hours: 2, effort: "2 hours of work",
      title: "Show a last-verified date on every page",
      what: "A badge in each footer stating when that page’s facts were last checked, plus one page listing the dates.",
      removes: "The ambiguity of ‘checked’ when different pages were checked on different days.",
      closes: [],
      cost: "No charge", risk: "A date is not a verification; it must reflect an actual read of the official page.",
      status: "proposed", note: "The footers currently carry one shared date."
    },
    {
      id: "S17", kind: "research", priority: "Low", hours: 2, effort: "2 hours",
      title: "Check whether a second unit could be added to Property A",
      what: "Ask Cupertino planning what the lot allows. The city’s own page says an ADU may be rented but not sold separately, that a permit is required, and that units of 800 square feet or less are exempt from floor-area, lot-coverage and open-space limits; it also sets size and count limits.",
      removes: "A possible third path: keep the house and add income instead of choosing between living and renting. It does not split the title or trigger a reassessment of the main house on its own.",
      closes: [],
      cost: "The city charges permit and plan-check fees; the amounts were not checked", risk: "Rent from a new unit is income the current model does not include, and construction cost is unknown. It must not enter the model before the city answers.",
      status: "proposed", note: "Rules read on the city’s page on 12 November 2026; buildability and cost were not assessed."
    },
    {
      id: "S18", kind: "research", priority: "Medium", hours: 3, effort: "Half a day, plus the report",
      title: "Commission an inspection and a five-year repair reserve",
      what: "Roof, HVAC, panel, plumbing, sewer lateral, foundation and drainage, priced, with the years the big items fall due.",
      removes: "The smooth 0.5%-a-year maintenance line, which hides lumpy and potentially large costs.",
      closes: ["Q13", "Q15"],
      cost: "Inspectors set their own price; no official figure is published", risk: "Findings can oblige disclosure in a later sale.",
      status: "proposed", note: "Best done while the parent still owns the house and repairs can be planned."
    },
    {
      id: "S19", kind: "site", priority: "Medium", hours: 2, effort: "2 hours of work",
      title: "Charge the months on market to the sell case",
      what: "Add a holding period (empty, insured, taxed) between the death and the closing instead of selling on the day of death.",
      removes: "An optimistic assumption in the plan that currently leads.",
      closes: [],
      cost: "No charge", risk: "The holding period is a guess until an agent gives a timeline.",
      status: "proposed", note: "It makes the sell case slightly worse, which is the conservative direction."
    },
    {
      id: "S20", kind: "research", priority: "Medium", hours: 2, effort: "2 hours",
      title: "Set the answer-by date for each High question",
      what: "Tie each of the five High questions to a date before the expected inheritance window, and put the dates in the calendar.",
      removes: "The failure mode where everything is researched after the death, when the deadlines are already running.",
      closes: [],
      cost: "No charge", risk: "None. It is a scheduling decision, not a change to the model.",
      status: "proposed", note: "The trust and the beneficiary decisions can only be made while the parent is alive."
    },
    {
      id: "S21", kind: "privacy", priority: "High", hours: 2, effort: "1–2 hours of planning, plus an owner decision",
      title: "Separate the private inputs from the published examples",
      what: "Keep household-specific inputs and outputs out of the public product and publish only synthetic examples; review access controls and every public reference before relying on it.",
      removes: "Further disclosure while keeping a public explanation of the method.",
      closes: [],
      cost: "Private hosting may need a paid plan", risk: "Existing history and copies still need a coordinated remediation plan. This proposal performs no history rewrite and changes no access setting.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25 on 12 Nov 2026, with its wording kept."
    },
    {
      id: "S22", kind: "site", priority: "Medium", hours: 5, effort: "4–6 hours of work",
      title: "Make the estate calculation conditional",
      what: "Show documented estate assets, debts, lifetime gifts and possible elections separately, and only then estimate any federal estate tax.",
      removes: "The risk of reading a property-only headroom figure as the amount that can pass tax-free.",
      closes: ["Q04", "Q16"],
      cost: "No charge", risk: "The actual amounts remain unknown and must stay private; the page can show a method and a range, not a liability.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25; the readiness register now holds the underlying questions."
    },
    {
      id: "S23", kind: "site", priority: "Medium", hours: 7, effort: "6–8 hours of work",
      title: "Match the sale endpoints and the tax basis across the three plans",
      what: "Show clearly labelled pre-liquidation and after-liquidation portfolio values beside the property sale proceeds, with basis and taxes applied consistently in every plan.",
      removes: "The ambiguity in comparing a plan that ends with a house sale against one that ends with a portfolio that has not been liquidated.",
      closes: ["Q09"],
      cost: "No charge", risk: "Needs account type, acquisition basis, gains, holding period and taxpayer treatment. The existing endpoint-tax sensitivity deliberately overstates part of the tax and is not a tax estimate.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25, which also flagged the endpoint wording on the Best plan and Decision pages."
    },
    {
      id: "S24", kind: "site", priority: "High", hours: 3, effort: "3 hours of work",
      title: "Add a documented Proposition 19 eligibility branch",
      what: "Separate a qualifying primary-residence transfer from a full reassessment, and put the one-year and three-year claim dates on the page.",
      removes: "The chance that a reader treats the live-in relief as automatic.",
      closes: ["Q07"],
      cost: "No charge", risk: "Eligibility and the adjusted allowance from February 2027 are unknown; the relationship, trust and residence facts must be confirmed privately with the assessor and counsel.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25."
    },
    {
      id: "S25", kind: "research", priority: "Medium", hours: 4, effort: "3–4 hours",
      title: "Replace the remaining cost proxies with reviewed ranges",
      what: "Maintenance, water and the solar credit, in addition to the insurance quotes in S02: an inspection, twelve months of bills and a net-metering statement.",
      removes: "Three modelled costs that are still household guesses rather than documents.",
      closes: ["Q12", "Q13"],
      cost: "An inspection is priced by the inspector; no official price", risk: "A range is not a bill. Keep the records private and distinguish a scenario from a verified cost.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25; S02 and S18 are the specific actions."
    },
    {
      id: "S26", kind: "site", priority: "Medium", hours: 4, effort: "4 hours of work",
      title: "Compare investment mixes and the downside",
      what: "Show liquidity, inflation, a bad return sequence and concentration beside the single 5%-a-year assumption, with deposit limits shown at their real level.",
      removes: "The impression that a central return assumption is a plan.",
      closes: ["Q17"],
      cost: "No charge", risk: "Returns are not guaranteed. Historical replays are not probabilities of future outcomes and must be labelled as such.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25."
    },
    {
      id: "S27", kind: "site", priority: "Low", hours: 3, effort: "3 hours of work",
      title: "Add legal and source freshness checks",
      what: "A dated check on each rule and benchmark the site relies on, with enacted, proposed and archived material kept visibly separate.",
      removes: "Quiet drift between what the law says and what the page says.",
      closes: ["Q21"],
      cost: "No charge", risk: "An automated check can detect that a page changed but cannot decide its legal effect; a professional must confirm that.",
      status: "proposed", note: "Carried from the shortlist published by session 6e6baf25; overlaps S11 and S16."
    }
  ],
  bundles: [
    {
      id: "P1", name: "Protect privacy first, change nothing else", audience: "If the only thing that must not go wrong is a private figure becoming public.",
      includes: ["S12", "S15", "S16"], effort: "About 6 hours",
      cost: "No charge, unless a private repository is chosen",
      outcome: "Closes no financial question. Removes the only irreversible risk and makes the site readable on a phone.",
      leaves: "Every number stays as it is: three premiums blank, the tax rate hypothetical, the trust unread."
    },
    {
      id: "P2", name: "Sharpen the numbers", audience: "If the plan will be acted on and the blanks should stop being blanks.",
      includes: ["S02", "S04", "S05", "S06", "S08", "S19"], effort: "About 14 hours, plus two professional meetings",
      cost: "Quotes and record pulls are free; CPA fees are the professional’s own rate",
      outcome: "Replaces the tax rate, all three premiums, the rent opinion and the tax rate on gain with written numbers, and adds the months on market to the sell case.",
      leaves: "The trust, the beneficiaries and the estate inventory stay unknown — the three items that could change the ranking rather than the margin."
    },
    {
      id: "P3", name: "Decision-grade file", audience: "If the household wants a file it can hand to a trustee, a CPA and an attorney and act on.",
      includes: ["S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S13", "S18", "S19", "S20", "S22", "S23", "S24", "S26"], effort: "About 45 hours of household time, plus professional time",
      cost: "Professional fees at their own rates; no official price exists for them",
      outcome: "Closes every open question a document can close, including all five High ones, and leaves a dated plan for the first twelve months.",
      leaves: "The eight unknowables — the date of death, future prices, returns, law and earthquakes. Those are planned around, not solved."
    },
    {
      id: "P4", name: "Wait and watch", audience: "If no decision needs to be made soon and the household wants to be told when one does.",
      includes: ["S11", "S16"], effort: "About 4 hours",
      cost: "No charge",
      outcome: "The site keeps its dates current and tells the household when a rule or a benchmark changes.",
      leaves: "Everything else. This is the status quo with a reminder attached, and it is a legitimate choice if the inheritance is decades away."
    }
  ],
  /* The seven decision questions on the shortlist published by session 6e6baf25 (site/suggestions.html before
     this session touched it). Kept, with their wording, and mapped to the register that now holds them. */
  carried: [
    { q: "What may be distributed, when, and by whom?", status: "— Trust terms and title not verified.", resolve: "Trust attorney and trustee review the signed trust, its amendments and the title.", closes: ["Q01", "Q02"], src: ["probate160617", "boeProp19"] },
    { q: "Will the family-home exclusion apply?", status: "— Relationship, residence and trust eligibility not verified. The live-in scenario assumes eligibility; the rental scenario does not.", resolve: "Confirm the facts and the filing dates with the county assessor and counsel.", closes: ["Q03", "Q07"], src: ["boeProp19"] },
    { q: "What is the full estate-tax exposure?", status: "— Other assets, debts, gifts and available elections are unknown; the future exclusion is a scenario.", resolve: "An estate CPA inventories assets and debts, prior gifts and any portability election before preparing a calculation.", closes: ["Q04", "Q16"], src: ["irsEstateTax"] },
    { q: "What are the correct basis and gain if sold?", status: "— Future appraised value, adjustments, proceeds and taxpayer facts are not verified.", resolve: "Obtain an appraisal and the closing records; have a tax adviser reconcile basis and the applicable exclusions.", closes: ["Q05", "Q09"], src: ["irsBasis", "irsTopic701"] },
    { q: "What will each property actually cost to insure and maintain?", status: "— Actual premiums and future repairs are unverified; the model inputs are illustrative.", resolve: "Compare owner-occupied and landlord quotes including deductibles and excluded hazards; obtain an inspection and repair estimates.", closes: ["Q10", "Q11", "Q13"], src: ["cdiResGuide"] },
    { q: "What rental income and restrictions apply?", status: "— Future rent, vacancy and the legal treatment of each unit are not verified. Property B is already owned, not inherited in this comparison.", resolve: "Review the leases and unit status privately; obtain a market-rent opinion and check the applicable local rules.", closes: ["Q14"], src: ["sfRentRates", "caRentCaps"] },
    { q: "How much risk and liquidity can the heir accept?", status: "— Investment goals, time horizon and account types are unknown.", resolve: "Discuss allocation, tax, deposit limits and withdrawal needs privately with a qualified adviser.", closes: ["Q17", "Q18"], src: ["investorRisk", "fdic"] }
  ],
  /* Privacy paths compared on the same shortlist. Kept because they are alternatives, not a claim that any is complete protection. */
  privacyPaths: [
    { name: "Private analysis, public generic examples", note: "Suggested privacy-first direction", benefit: "Keep household-specific inputs and outputs out of a public product; publish only synthetic examples.", tradeoff: "Less personalised public analysis. Existing history and copies still need a coordinated remediation plan. Review access controls and every public reference before relying on this path.", src: "githubSensitive" },
    { name: "Reduce the public detail", note: "", benefit: "Remove household history and granular contextual combinations from the current published pages.", tradeoff: "A new commit alone does not erase earlier history or copies. Generic labels and rounding are not a guarantee of anonymity; decide what exposure remains acceptable.", src: "githubSensitive" },
    { name: "Retain the current public scenarios", note: "", benefit: "Preserves the most detailed public explanation and model.", tradeoff: "The property and household context remains linkable even without names. Treat this as an unresolved privacy risk, not as anonymisation.", src: "githubSensitive" }
  ],
  /* Two earlier shortlists that occupied this page before this session's merge. Their IDs and titles are kept
     and each row points at the item or question that now carries it, so a reader of the old page can find it. */
  reconciled: {
    analysis: [
      ["A-01", "Confirm the trust type, and whether the house counts in the parent's estate", "Q01 · S03", "irsRevRul20232"],
      ["A-02", "Confirm the house is still the parent's principal residence at death", "Q03 · S03", "boeLta2026026"],
      ["A-03", "Get the cost to rebuild and one written homeowners quote at that limit", "S02 · Q10", "cdiSurveyCup40_1000"],
      ["A-04", "Decide whether to carry earthquake cover, and price it", "S02 · Q20", "cdiSurveyEqCup"],
      ["A-05", "Read the FY2027 rent benchmark for the ZIP code and update the rent input", "S11 · Q14", "hudA"],
      ["A-06", "Re-check the Proposition 19 amount when the Board of Equalization publishes it", "S11 · Q07", "boeLta2025009"],
      ["A-07", "Put every pending law change on a calendar with a named reviewer", "S27 · S11", "hr1301"],
      ["A-08", "List every asset, owner and beneficiary, then measure federal headroom", "S22 · Q16", "irsEstateTax"],
      ["A-09", "Record the assessor's land and building split, then read the depreciation rules", "S07 · Q06", "irsPub527"],
      ["A-10", "Read the recorded deed and the trust's schedule of assets", "S03 · Q01", "probate160617"],
      ["A-11", "Write the dated obligations into one calendar", "S09", "sfRentFee"],
      ["A-12", "Decide what the San Francisco owner unit is for", "Q19 · Q20", "sfRentRates"],
      ["A-13", "Confirm the solar tariff and interconnection date, then read the current water and power schedules", "S25 · Q12", "cpucNem"],
      ["A-14", "Test the ranking against a lower home-price assumption and write down the break-even", "S26 · Q22", "fredSJ"],
      ["A-15", "Keep every new fact out of this repository", "S21 · S12", "githubSensitive"]
    ],
    questions: [
      ["Q-01", "Is the trust revocable, or otherwise counted in the parent's estate?", "Q01", "irsRevRul20232"],
      ["Q-02", "Will the house be the parent's principal residence on the date of death?", "Q03", "boeLta2026026"],
      ["Q-03", "How much money is inherited, in what accounts, with which beneficiaries?", "Q16", "irsEstateTax"],
      ["Q-04", "What would it cost to rebuild, and what will a policy cost at that limit?", "Q10", "cdiSurveyCup40_1000"],
      ["Q-05", "Will earthquake cover be carried on either property?", "Q20", "cdiSurveyEqCup"],
      ["Q-06", "Which solar tariff governs the system, and when does it end?", "Q12", "cpucNem"],
      ["Q-07", "Will the heir live in the Cupertino house, or stay in San Francisco?", "Q19", "irsTopic701"],
      ["Q-08", "Will the San Francisco owner unit be rented?", "Q19", "sfRentFee"],
      ["Q-09", "What share of the property's value is the building?", "Q06 · Q13", "irsPub527"],
      ["Q-10", "What home-price growth should be assumed after the inheritance?", "Q22", "fredSJ"]
    ],
    site: [
      ["B-01", "A dated decision record beside the model", "The record on this page: choose an item, and the choice is kept in this browser with a date.", "Built here", "githubPages"],
      ["B-02", "A one-page printable brief for advisers", "S13", "Proposed", "irsEstateTax"],
      ["B-03", "A 'what changed' strip on the landing page", "S16", "Proposed", "githubPages"],
      ["B-04", "One assumptions register with a last-checked date and a CSV export", "S14", "Proposed", "irsBasis"],
      ["B-05", "A deadline calendar with an export", "S09", "Proposed", "probate160617"],
      ["B-06", "A source-freshness dashboard", "S27", "Proposed", "boeLta2025009"]
    ],
    sequence: [
      ["1", "This month · no cost but a meeting", "Answer the four questions that can change the answer: the trust and what it holds, the parent's occupancy and how title is held, the beneficiaries and the money, and whether the heir would live there.", "Q01 · Q02 · Q03 · Q16 · Q19", "irsRevRul20232"],
      ["2", "Next 90 days · free or low cost", "Replace the four assumptions with quotes and official figures: rebuild cost and a homeowners quote, an earthquake decision and quote, the FY2027 rent benchmark, and the parcel's tax-rate area.", "S02 · S04 · S05 · S25", "cdiSurveyCup40_1000"],
      ["3", "Every year, on a fixed date", "Run the calendar, not the whole site: February for the Proposition 19 amount, March for San Francisco's rent changes and the Rent Board fee, October for HUD rents, and the insurance renewal.", "S11 · S27", "boeLta2025009"],
      ["4", "In the inheritance year", "File first, then decide: the 60-day trustee notice, the 150-day change-of-ownership statement, the homeowners' exemption within one year, the exclusion claim within three years, and Form 593 before any closing.", "S09 · S20", "ftb593"],
      ["5", "After implementing anything", "Re-verify, then record the change: an official source, rounded figures, and a note on the Verified facts and this page.", "S01 · S27", "irsEstateTax"]
    ]
  },
  never: [
    ["Publish a name, street address, parcel number, account number or trust document", "The site is public and indexed. Placeholders are the only safe form.", "sccBill"],
    ["Publish an unrounded household figure or an exact tax bill", "A 4- to 6-digit amount can be searched. Rounding to $10 is the published rule.", "sccBill"],
    ["State a premium, a rent or a value that has not been quoted, appraised or published", "An inferred number reads like a fact. Blank and flagged is the rule.", "cdiResGuide"],
    ["Add analytics, external fonts, third-party scripts or a backend", "Every calculation runs in the browser today; nothing leaves the page. GitHub already logs a visitor’s IP address at the host, which is outside this site’s control.", "githubPages"],
    ["Apply a suggestion because it was selected here", "Selection is a note to the owner. A change is made only after it is chosen and logged — and on this host a published change goes live immediately.", "githubPages"],
    ["Mark a fact verified without opening the official page and recording the date", "The register is only worth what its weakest row is worth.", "irsEstateTax"]
  ]
};
