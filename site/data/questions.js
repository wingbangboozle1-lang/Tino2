/*
  Decision gate (session 62245584, 12 Nov 2026).

  The brief asks for "a clear list of questions, informations and answers that need to be
  addressed before any decision can be reasonably made" plus "suggestions ... to discover
  missing information". This file is that list. It is deliberately NOT a copy of the
  Flagged for Review register: that register records what is unknown and what the model does
  meanwhile. This file records, question by question, whether the answer is settled, and
  which of the four plans (sell / rent / live / estate) cannot be implemented without it.

  Rules obeyed here:
    - No personal information. Parties appear as [OWNER], [TRUSTEE], [DECEDENT], [HEIR].
      Properties appear as Property A (Cupertino, inherited) and Property B (San Francisco,
      already owned by the heir).
    - No household figure is typed in this file. Where a question needs one, the answer
      reads it from the published MODEL.BASE, so the page can never disagree with the model.
    - Every item carries an official https source key from site/data/sources.js, or the
      official route that would settle it. Nothing is inferred.
    - Dollar amounts are formatted through MODEL.fmtMoney, which rounds to the nearest $10.
*/
(function () {
  const B = window.MODEL.BASE;
  const money = window.MODEL.fmtMoney;

  /* Status vocabulary. Three states only, and each one has a fixed meaning on the page:
       settled    the answer is fixed by an official source. It does not change with our views.
       household  the answer exists only as an unverified household input. Usable, but it must
                  be replaced by a document before money is committed on it.
       missing    no answer exists in the record. A plan that depends on it cannot be finalised. */
  const STATUS = {
    settled: { label: "Settled by official source", short: "Settled", badge: "" },
    household: { label: "Household input, unverified", short: "Household input", badge: "gold" },
    missing: { label: "Missing — no answer in the record", short: "Missing", badge: "red" }
  };

  /* Plans. A question lists the plans that cannot be implemented until it is answered.
     "estate" is the inheritance transfer itself, which stands ahead of the three uses of the house. */
  const PLAN_LABEL = {
    sell: "Sell and reinvest",
    rent: "Rent out",
    live: "Live in it",
    estate: "The transfer itself"
  };

  const GROUPS = [
    {
      id: "transfer",
      title: "The transfer: what is actually being inherited",
      intro: "These come before any choice about the house. Each one is a document, not an opinion, and each one has an owner who already holds it.",
      items: [
        {
          id: "Q-01",
          q: "Is Property A inside the trust, with title in the trust's name?",
          a: "Not in the record. The brief says the house is expected to pass by trust around 2040–2050; the deed, the schedule of assets and the trust instrument were not supplied.",
          status: "missing",
          why: "Two things follow. First, if the house is inside the trust it passes by the trust's terms and no probate is needed; if it is outside, a probate applies statutory fees to the representative and again to the attorney. Second, and larger: the basis reset at death applies only to property included in the gross estate or treated as acquired from the decedent. Property in a revocable trust is treated as acquired from the decedent; assets of an irrevocable trust that are not included in the estate keep the old basis. So a house held in the wrong kind of trust can lose the step-up the whole sell case rests on.",
          action: "Read the deed and the trust's schedule of assets. Ask the [TRUSTEE] for a copy of the current schedule, and ask the preparer to confirm in writing that the house is included in the gross estate or is in a revocable trust at death.",
          src: "irsRevRul20232",
          affects: ["estate"]
        },
        {
          id: "Q-02",
          q: "What kind of trust is it, and does it become irrevocable at the first death?",
          a: "Not in the record. A revocable trust normally becomes irrevocable when the [DECEDENT] dies, or when the instrument says it does within one year of the death.",
          status: "missing",
          why: "Irrevocability is what starts the trustee's duty to serve notice on every beneficiary and heir within 60 days.",
          action: "Identify the trust type from the instrument and the date each part becomes irrevocable.",
          src: "caTrustNotice",
          affects: ["estate"]
        },
        {
          id: "Q-03",
          q: "Does the trust give Property A to the heir outright, or does it stay in trust?",
          a: "Not in the record. The brief treats the heir as the inheritor of the house; the distribution terms were not supplied.",
          status: "missing",
          why: "A house that stays in trust is not the heir's to sell, rent or occupy freely, and the trustee's powers decide every later step.",
          action: "Read the distribution article of the trust instrument.",
          src: "caTrustNotice",
          affects: ["estate", "sell", "rent", "live"]
        },
        {
          id: "Q-04",
          q: "Are there other beneficiaries or heirs who share in Property A?",
          a: "Not in the record. The brief names one inheritor; it does not say whether anyone else shares in the house.",
          status: "missing",
          why: "Sharing changes who must sign, whether a buy-out is needed, and whether a later sale between siblings is itself a reassessable transfer.",
          action: "List every beneficiary and heir, and confirm whether the trust permits a non-pro-rata distribution of the home.",
          src: "sccProp19",
          affects: ["estate", "sell"]
        },
        {
          id: "Q-05",
          q: "What will Property A be worth on the date of death?",
          a: () => `Unknown. The working figure is ${money(B.aValue)} as of November 2026, which is a household estimate, not an appraisal. The date of death is expected between 2040 and 2050.`,
          status: "household",
          why: "The value at death is the heir's tax basis for a later sale, and it is the assessed value a rented house is reassessed to. Every projection in this site is anchored on it.",
          action: "Obtain a date-of-death appraisal, or the executor's Form 706 valuation if one is filed.",
          src: "irsInherited",
          affects: ["estate", "sell", "rent", "live"]
        },
        {
          id: "Q-06",
          q: "What is the total gross estate, including cash, securities and the house?",
          a: "Unknown. The brief says the inheritance includes a considerable amount of money that may exceed the tax-free amount, but gives no figure and no account types.",
          status: "missing",
          why: "Federal estate tax starts at 40% of everything above the exclusion. Property A alone is far below the exclusion, so the answer turns on the money, not the house.",
          action: "List every account with its type, balance, owner and named beneficiary; add the house and any life insurance the [DECEDENT] owned.",
          src: "irsEstateTax",
          affects: ["estate"]
        },
        {
          id: "Q-07",
          q: "Have lifetime gifts been made above the yearly exclusion?",
          a: "Unknown. Gifts are added back to the estate before the tax is computed.",
          status: "missing",
          why: "Adjusted taxable gifts made since 1977 increase the amount the tax is computed on, even though they are not in the estate at death.",
          action: "Ask the [TRUSTEE] and the preparer whether any Form 709 was ever filed. The yearly exclusion is $19,000 per recipient for 2026 and $20,000 for 2027.",
          src: "irs2027",
          affects: ["estate"]
        },
        {
          id: "Q-08",
          q: "Will a portability election be available from the first death?",
          a: "Unknown. Portability passes an unused exclusion to the surviving spouse, but only if a timely Form 706 is filed for the first death.",
          status: "missing",
          why: "Where there is a surviving spouse, an unfiled Form 706 can waste one exclusion outright. That can double the tax on a large money inheritance.",
          action: "Confirm the marital status at each death and instruct the preparer to file Form 706 for the first death if portability could matter.",
          src: "irs706",
          affects: ["estate"]
        },
        {
          id: "Q-09",
          q: "What kinds of money are in the inheritance?",
          a: "Unknown. Bank deposits, a brokerage account, a retirement account, Roth money and life insurance each follow different rules.",
          status: "missing",
          why: "A non-spouse heir generally must empty an inherited retirement account within ten years, and those distributions are ordinary income. Life insurance and inheritances themselves are not income.",
          action: "List each account by type, because the tax treatment differs by type, not by amount.",
          src: "irsTopic559",
          affects: ["estate"]
        },
        {
          id: "Q-10",
          q: "Are the [DECEDENT] and the [HEIR] citizens or residents of the United States?",
          a: "Unknown. The brief does not say.",
          status: "missing",
          why: "Different exclusion amounts and filing rules apply to a nonresident who is not a citizen, and a non-citizen spouse cannot use the unlimited marital deduction the same way.",
          action: "Confirm citizenship and residence for both, before relying on any exclusion figure.",
          src: "irsEstateTax",
          affects: ["estate"]
        }
      ]
    },
    {
      id: "tax",
      title: "Property tax: the single largest number in the decision",
      intro: "Property tax is what separates a lived-in house from a rented one. These questions decide which rules apply, and one of them is a question of intent that only the heir can answer.",
      items: [
        {
          id: "Q-11",
          q: "Will the heir make Property A their principal residence within one year of the transfer?",
          a: "Undecided. This is the choice the whole site exists to answer, and it has a deadline attached to it: the exclusion requires a homeowners' or disabled veterans' exemption claim within one year of the transfer.",
          status: "missing",
          why: "This single answer decides whether the house is reassessed to market value or keeps part of the parent's low assessed value. It is worth more than every operating cost on this site combined.",
          action: "Decide before the transfer, not after. The claim is due within one year, and a late claim gives prospective relief only.",
          src: "boeProp19",
          affects: ["live", "rent", "sell"]
        },
        {
          id: "Q-12",
          q: "What is the rule if the house is rented instead of lived in?",
          a: "Settled: there is no parent-child exclusion for a rented home. It is reassessed to market value at the date of transfer, and a rented home is not eligible for the homeowners' exemption.",
          status: "settled",
          why: "Renting therefore converts the lowest property tax in the comparison into the highest. This is the arithmetic behind the published ranking.",
          action: "Nothing to obtain. This is the rule as written.",
          src: "boeProp19",
          affects: ["rent"]
        },
        {
          id: "Q-13",
          q: "How much of the parent's assessed value survives, if the heir lives there?",
          a: () => `Settled method, unknown inputs. The cap is the factored base year value plus the adjusted $1 million amount. For transfers from 16 February 2025 to 15 February 2027 that amount is $1,044,586, and the next adjustment is due in February 2027. The assessed value carried forward today is ${money(B.aAssessed)}, which is a household figure.`,
          status: "settled",
          why: "Above the cap, everything else is added to the taxable value. Below it, the parent's whole assessed value survives.",
          action: "Apply the official formula to the date-of-death appraisal once it exists. The 2040–2050 amount is not yet published and is projected here, labelled as a scenario.",
          src: "boeLta2025009",
          affects: ["live"]
        },
        {
          id: "Q-14",
          q: "Which tax rate area is Property A in, and what direct charges are on its bill?",
          a: "Not in the record. The published model uses a hypothetical 1.2% combined levy for Property A.",
          status: "missing",
          why: "Beyond the 1% general levy, bond and special-district rates differ by tax rate area. Using the wrong area moves the yearly bill.",
          action: "Read the tax rate area on the bill, then use the county rate book for that area. The rate book for FY 2025-26 is published.",
          src: "sccTaxBook",
          affects: ["live", "rent"]
        },
        {
          id: "Q-15",
          q: "Does the heir claim Property B as their principal residence?",
          a: "Yes, on the brief: the heir already owns Property B in San Francisco and can live there without losing rent.",
          status: "household",
          why: "A person has one principal residence for this purpose. If the heir stays in San Francisco and claims it, Property A cannot also carry the parent-child relief.",
          action: "Confirm which property will be the principal residence for the year of the transfer, and keep the homeowner exemption claim consistent with it.",
          src: "sccProp19",
          affects: ["live", "rent"]
        },
        {
          id: "Q-16",
          q: "Could the pre-2021 parent-child rule come back?",
          a: "Currently no. An initiative to restore it failed to qualify on 18 May 2026. If it returned, a rented house could keep the parent's assessed value.",
          status: "settled",
          why: "This is the one legal change that could reverse part of the ranking. It is the reason the site flags the recommendation as resting on today's rule.",
          action: "Check the Secretary of State's initiative list before each general election, and again before any sale.",
          src: "boeProp19",
          affects: ["rent"]
        }
      ]
    },
    {
      id: "sell",
      title: "Selling: what the sale actually nets",
      intro: "A sale soon after the inheritance is the simplest case, because the tax basis resets at death. The questions left are about the mechanics and the price of the exit.",
      items: [
        {
          id: "Q-17",
          q: "What is the tax basis of Property A in the heir's hands?",
          a: "Generally the fair market value on the date of death, so selling for more than that is a taxable gain and selling at that value leaves little or no gain. But this is conditional: the step-up applies to property included in the gross estate or treated as acquired from the decedent. Assets of an irrevocable trust that are not included in the estate keep their old basis, which is the rule in Revenue Ruling 2023-2. Whether the house falls on the right side of that line is question Q-01.",
          status: "missing",
          why: "This is the single assumption the whole sell case rests on. If the basis does not step up, a prompt sale is taxed on decades of gain and the lead of selling narrows sharply.",
          action: "Get Q-01 answered first, then obtain the date-of-death appraisal as the basis and keep it with the closing file.",
          src: "irsInherited",
          affects: ["sell"]
        },
        {
          id: "Q-18",
          q: "Will a capital-gain tax apply to a prompt sale?",
          a: "Little or none if the sale price is close to the date-of-death value. The gain would be the amount above basis, less selling costs.",
          status: "settled",
          why: "California gives no lower rate for capital gains; they are taxed as ordinary income. So a large gain later is expensive at the state level as well as the federal.",
          action: "Model the actual gain once the appraisal and the sale price exist.",
          src: "caCapGains",
          affects: ["sell"]
        },
        {
          id: "Q-19",
          q: "Will California withhold part of the sale price at closing?",
          a: "Yes, by default: 3 1/3% of the sales price is withheld unless the seller certifies an exemption on Form 593 before the close of the transaction.",
          status: "settled",
          why: "After closing, the withheld amount can only be recovered as a credit on a tax return. Before closing, a certificate avoids it.",
          action: "Budget for the withholding or file the certificate before closing. Withheld tax is not a fine, but it ties up cash.",
          src: "ftb593",
          affects: ["sell"]
        },
        {
          id: "Q-20",
          q: "What selling costs should be assumed?",
          a: "The model assumes 6% of the price. That is an assumption, not an official figure; no agency publishes a commission.",
          status: "household",
          why: "Commission and closing costs come straight off the proceeds before the money is reinvested, so they move the comparison.",
          action: "Replace the 6% with two written listing proposals closer to the date.",
          src: "irsTopic701",
          affects: ["sell"]
        },
        {
          id: "Q-21",
          q: "Should the home-sale exclusion of $250,000 be relied on?",
          a: "No, not for a prompt sale. It requires ownership and use for at least 24 months of the five years before the sale, and the basis already resets at death, so there is little gain left to exclude.",
          status: "settled",
          why: "It is only relevant if the heir lives in the house for two years or more and then sells at a large gain, which is the 'live in it' plan.",
          action: "If the 'live in it' plan is chosen, count the two years carefully; if not, ignore this exclusion.",
          src: "irsTopic701",
          affects: ["live", "sell"]
        },
        {
          id: "Q-22",
          q: "Is a like-kind exchange available to shelter the sale?",
          a: "No. A section 1031 exchange applies only to real property held for business or investment, and it must be replaced with other real property. Moving the proceeds into shares is a taxable sale.",
          status: "settled",
          why: "The 'sell and reinvest in the stock market' plan is therefore fully taxable on any gain, which is why the basis reset matters so much.",
          action: "Nothing to obtain. Plan the reinvestment on an after-tax basis.",
          src: "irsTopic409",
          affects: ["sell"]
        }
      ]
    },
    {
      id: "rent",
      title: "Renting: whether the house would actually pay",
      intro: "Renting keeps the house and its upkeep. Before the rental case can be treated as real, the rent has to be a benchmark rather than a guess, and the land/building split has to exist.",
      items: [
        {
          id: "Q-23",
          q: "What rent would Property A fetch?",
          a: () => `A benchmark, not a lease. The model uses ${money(B.aRent4BR)} a month for a four-bedroom home, the federal Small Area Fair Market Rent for the ZIP code in FY2026, and ${money(B.aRent3BR)} for a three-bedroom.`,
          status: "household",
          why: "Rent is the revenue line of the rental case. A 10% error moves the ten-year answer by more than a million dollars.",
          action: "Read the current fiscal year's row for the ZIP code, then replace it with two written appraisals of achievable rent.",
          src: "hudA",
          affects: ["rent"]
        },
        {
          id: "Q-24",
          q: "Is the rent benchmark the current fiscal year?",
          a: "No. It is one year behind: FY2027 took effect on 1 October 2026 and the model still carries FY2026.",
          status: "missing",
          why: "The gap is small against a 3%/yr rent assumption but it is a known, dated defect in the input.",
          action: "Open the federal rent lookup for the ZIP code and read the FY2027 row.",
          src: "hudMethod",
          affects: ["rent"]
        },
        {
          id: "Q-25",
          q: "What share of Property A's value is the building?",
          a: "Unknown. The assessor's split between land and improvements was not supplied.",
          status: "missing",
          why: "Depreciation is taken on the building only, so the split decides how much of the rental income is sheltered. The rental case is published with no depreciation at all.",
          action: "Read the land and improvement values on the assessor's roll, or get an appraiser's allocation.",
          src: "irsTopic704",
          affects: ["rent"]
        },
        {
          id: "Q-26",
          q: "What is the heir's other income?",
          a: "Unknown. The brief gives no figure.",
          status: "missing",
          why: "Rental losses are generally passive and limited; they cannot shelter salary, and the released losses only arrive on a full sale. The 3.8% net investment income tax also depends on income.",
          action: "Model the rental case with the heir's actual income, because the tax result changes with it.",
          src: "irsNIIT",
          affects: ["rent"]
        },
        {
          id: "Q-27",
          q: "Would a rent increase on Property A be capped?",
          a: "Likely yes under the state tenant protection law, which caps most increases at 5% plus inflation to a maximum of 10%. A local ordinance could be tighter.",
          status: "settled",
          why: "The model grows rent at 3% a year, which sits under the cap, but the cap is a ceiling and not a forecast.",
          action: "Confirm the state cap for the year, and check whether the city has its own ordinance.",
          src: "caRentCaps",
          affects: ["rent"]
        },
        {
          id: "Q-28",
          q: "What vacancy and management costs should be assumed?",
          a: () => `Assumptions, not official figures: ${Math.round(B.vacancy * 100)}% vacancy and ${Math.round(B.management * 100)}% of collected rent for management.`,
          status: "household",
          why: "Both are real costs of renting that a lived-in house does not carry, and both are estimates.",
          action: "Replace with a property manager's written fee schedule.",
          src: "irsRental",
          affects: ["rent"]
        }
      ]
    },
    {
      id: "live",
      title: "Living in it: the cost of holding a second home",
      intro: "This plan pays no rent and receives none. Its whole cost is the bill, so every line of the bill has to be known.",
      items: [
        {
          id: "Q-29",
          q: "What would it cost to rebuild Property A?",
          a: "Unknown. The brief gives no rebuild cost, and the value of the land is not the cost of the house.",
          status: "missing",
          why: "A homeowners premium follows the dwelling limit, which is the rebuild cost. The state regulator's 2026 survey shows the middle premium roughly doubling between a $500,000 and a $1,000,000 dwelling limit.",
          action: "Ask a builder or an insurer for a rebuild estimate, then get a written quote on that limit.",
          src: "insuranceGuide",
          affects: ["live", "rent"]
        },
        {
          id: "Q-30",
          q: "What is the actual insurance premium for Property A?",
          a: "Not in the record. The model carries the household's estimate, labelled as an input. No official source publishes a premium for this house.",
          status: "household",
          why: "The premium is a real yearly cost, but the survey range is narrow enough that no premium in it changes the ranking.",
          action: "Obtain two binding quotes: one owner-occupied policy, and one landlord policy if renting.",
          src: "cdiSurveyCup40_1000",
          affects: ["live", "rent"]
        },
        {
          id: "Q-31",
          q: "Would earthquake damage be covered?",
          a: "Not by a homeowners policy. Earthquake cover is a separate policy, and 13 of the 40 insurers in the regulator's survey sell it through the California Earthquake Authority.",
          status: "settled",
          why: "Not modelled. Both houses sit in one seismic region, so an uninsured loss would hit the household twice.",
          action: "Decide explicitly whether to carry earthquake cover on each property, get a quote, and add the premium if so.",
          src: "cdiSurveyEqCup",
          affects: ["live", "rent"]
        },
        {
          id: "Q-32",
          q: "What happens to the cover if the house stands empty?",
          a: "Settled: losses to a house vacant for 60 days or more are generally not covered.",
          status: "settled",
          why: "The slow period between a death and a decision is exactly when a house stands empty, so the gap in cover arrives at the worst time.",
          action: "Ask the insurer in writing for the vacancy term of any policy, before relying on it during the transfer.",
          src: "insuranceGuide",
          affects: ["rent", "sell", "live"]
        },
        {
          id: "Q-33",
          q: "What are the water and electricity costs, and does the solar system pay?",
          a: () => `Household inputs: water ${money(B.aWaterMonthly)} a month, and a net solar credit of ${money(B.aSolarMonthlyCredit)} a month rather than a bill. Three different water systems serve the ZIP code, and the provider was not confirmed.`,
          status: "household",
          why: "These are small against property tax, but the solar credit depends on which tariff applies, and the legacy net-metering term runs 20 years from permission to operate.",
          action: "Read the provider's name on a water bill, and read the permission-to-operate date from the solar interconnection paperwork.",
          src: "solar",
          affects: ["live", "rent"]
        },
        {
          id: "Q-34",
          q: "What are the regular maintenance and repair costs?",
          a: () => `An assumption: ${(B.maintenanceA * 100).toFixed(1)}% of value a year for Property A and ${(B.maintenanceB * 100).toFixed(0)}% for Property B. No Bay Area agency publishes a maintenance benchmark by building.`,
          status: "household",
          why: "On a house this old, upkeep is a permanent cost that a portfolio does not carry. Over ten years it is a five-figure sum either way.",
          action: "Replace the percentage with three years of actual repair records, or contractor estimates.",
          src: "irsRental",
          affects: ["live", "rent"]
        },
        {
          id: "Q-35",
          q: "Does living in Property A really displace anything?",
          a: "No. The heir can live in Property B's third unit without giving up either rent. So living in Property A is a preference, not a housing need.",
          status: "household",
          why: "This is the distinction the brief asked to see. It is why the 'live in it' plan finishes last on money rather than first.",
          action: "Confirm the third unit in Property B is legally habitable and does not disturb the two tenancies.",
          src: "sfRent",
          affects: ["live"]
        }
      ]
    },
    {
      id: "estate",
      title: "The money and the years after",
      intro: "The inheritance is not only a house. These questions decide what happens to the money, and what the heir's own estate will owe later.",
      items: [
        {
          id: "Q-36",
          q: "What is the federal amount that can pass before estate tax?",
          a: () => `Settled and dated: $15,000,000 for a death in 2026, and $15,480,000 for a death in 2027, indexed after that. Property A alone leaves about ${money(window.MODEL.estateRow(2027).headroom)} of room in 2027.`,
          status: "settled",
          why: "No California estate tax return is required for any death on or after 1 January 2005, so the federal figure is the only inheritance threshold that applies.",
          action: "Re-read the federal amount for the actual year of death. It is published annually, and the 2040s amount cannot be known now.",
          src: "irs2027",
          affects: ["estate"]
        },
        {
          id: "Q-37",
          q: "Is there any California inheritance or estate tax?",
          a: "Settled: no. There is no requirement to file a California estate tax return for a death on or after 1 January 2005, and no inheritance tax for a death after 1982.",
          status: "settled",
          why: "This removes a whole layer of tax that residents of other states face, and it means the plan only has to manage the federal threshold.",
          action: "Nothing to obtain while the law stands. Watch for proposals, which the Sources page tracks.",
          src: "caEstate",
          affects: ["estate"]
        },
        {
          id: "Q-38",
          q: "What return does the reinvested money have to earn to beat the house?",
          a: () => `The model uses ${(window.MODEL.afterTaxPortfolioReturn() * 100).toFixed(0)}% a year after tax against home prices at ${(B.appreciation * 100).toFixed(1)}% a year. Those are assumptions placed beside official long-run projections, not forecasts.`,
          status: "household",
          why: "The ranking is more sensitive to this pair of numbers than to any bill. It is the honest centre of the uncertainty.",
          action: "Read the official long-run projections again each year; the Verified facts page records them.",
          src: "cbo",
          affects: ["sell"]
        },
        {
          id: "Q-39",
          q: "Where would the sale proceeds be held, and is that insured?",
          a: "Undecided. Deposit insurance covers $250,000 per depositor, per bank, for each ownership category; investments are not insured at all.",
          status: "settled",
          why: "A sum this size cannot sit in one bank account, and uninsured deposits are a real risk that a house does not carry.",
          action: "Plan the placement in advance: split across banks or use different ownership categories, and diversify investments.",
          src: "fdic",
          affects: ["sell"]
        },
        {
          id: "Q-40",
          q: "Is the ranking an investment recommendation?",
          a: "No. It compares three uses of one asset on stated assumptions. It is not an appraisal, a tax return, a legal opinion or an insurance quote.",
          status: "settled",
          why: "The model deliberately leaves out depreciation, passive-loss benefits and the value of living in the house, so it cannot be treated as a complete answer.",
          action: "Have the chosen path checked by a CPA, an attorney and an insurance broker before anything is signed.",
          src: "investorRisk",
          affects: ["sell", "rent", "live"]
        }
      ]
    }
  ];

  /* Readiness: for each plan, which questions still block it.
     A "settled" answer never blocks. A "household" answer blocks, because it is not yet a document.
     A "missing" answer blocks. That rule is what makes the counts on the page mean something. */
  const ALL = GROUPS.flatMap(g => g.items.map(i => ({ ...i, group: g.id, groupTitle: g.title })));
  function answerOf(item) {
    return typeof item.a === "function" ? item.a() : item.a;
  }
  function blockers(plan) {
    return ALL.filter(i => i.affects.includes(plan) && i.status !== "settled");
  }
  function readiness(plan) {
    const b = blockers(plan);
    const total = ALL.filter(i => i.affects.includes(plan)).length;
    return { plan, label: PLAN_LABEL[plan], blockers: b, total, settled: total - b.length, ready: b.length === 0 };
  }

  window.QUESTIONS = {
    STATUS, PLAN_LABEL, GROUPS, ALL, answerOf, blockers, readiness,
    plans: ["estate", "sell", "rent", "live"],
    counts: {
      total: ALL.length,
      settled: ALL.filter(i => i.status === "settled").length,
      household: ALL.filter(i => i.status === "household").length,
      missing: ALL.filter(i => i.status === "missing").length
    }
  };
})();
