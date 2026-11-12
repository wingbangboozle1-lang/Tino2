/* Decision-readiness register (session a87f8523, 12 November 2026).
   Plain data only: no personal information, no unrounded household figure, no inferred value.
   Each row names at least one source key from site/data/sources.js; a blank field means "not known",
   never zero.  Amounts are the household's rounded planning inputs or figures a government body
   publishes.  Verified wording and access dates: verification/a87f8523/REPORT.md. */
window.READINESS = {
  checked: "12 November 2026",
  groups: [
    {
      id: "trust",
      title: "1 · Title, trust and the estate",
      intro: "These decide what is actually inherited, whether the tax basis resets, and who has to agree. Until they are answered, every dollar figure on this site rests on an assumption."
    },
    {
      id: "value",
      title: "2 · Value, assessment and tax",
      intro: "These set the number the house is taxed on and the number the heir is taxed on. They are different numbers, and both are unknown until the county and an appraiser act."
    },
    {
      id: "costs",
      title: "3 · What it costs to own, rent or sell",
      intro: "The operating costs are the household's own figures, rounded. The three largest can be replaced with real quotes; the rest are small enough to model."
    },
    {
      id: "money",
      title: "4 · The money, its liquidity and the plan for the proceeds",
      intro: "The house is only one asset in the estate. The federal threshold, the form of the money and what happens to the proceeds decide whether selling is even the right comparison."
    },
    {
      id: "home",
      title: "5 · The household, not the spreadsheet",
      intro: "One of these is not a research question at all: whether the heir wants to live in the house. The model can price the house; it cannot price that choice."
    },
    {
      id: "law",
      title: "6 · Law, prices and returns: what cannot be answered yet",
      intro: "These are listed so they are not mistaken for gaps in the research. No document settles them. The site plans around them with ranges, break-evens and monitoring dates."
    }
  ],
  open: [
    {
      id: "Q01", group: "trust", priority: "High",
      q: "Is Property A held in the trust, and is that trust counted in the parent’s estate?",
      why: "The whole sell-first answer depends on the heir’s tax basis being the value at death. That happens when the assets are included in the estate — as they are in a revocable trust. If the trust is irrevocable and outside the estate, the old basis carries over.",
      known: "Not supplied. Every result on this site assumes a revocable trust counted in the estate, so basis resets at death. Revenue Ruling 2023-2 holds that assets of an irrevocable trust that are not included in the estate do not get a basis adjustment at death.",
      src: ["irsInherited", "irsRevRul20232"],
      missing: "The trust document; whether it is revocable; the schedule of assets showing the house; the trustee’s powers to sell and distribute.",
      discover: "Ask the trustee and the trust attorney for the document and the schedule of assets. Ask in writing whether the trust is included in the estate for federal purposes.",
      flip: "If the basis does not reset: a sale is taxed on the gain since the parents bought, the sell-first lead shrinks or disappears, and the live/rent comparison has to be rebuilt with the original purchase price.",
      status: "open"
    },
    {
      id: "Q02", group: "trust", priority: "High",
      q: "Who are the beneficiaries, and may the house go to one of them without a buy-out?",
      why: "The site models one heir. With siblings, the parent-child exclusion can be lost when the home passes to one child for more than that child’s share, and a later buy-out between siblings is reassessed.",
      known: "One heir is assumed. The distribution clause has not been read. The county’s guidance sets out the uneven-distribution condition.",
      src: ["boeLta2026026", "sccProp19"],
      missing: "The beneficiary list, the distribution clause, any lifetime gifts to other children, and whether the siblings would keep or sell.",
      discover: "Read the distribution clause with the attorney while it can still be amended. Ask each beneficiary what they want before the death, not after.",
      flip: "A required buy-out or a forced sale adds a reassessment and a cash call; the ‘keep and rent’ option may then be unavailable regardless of the numbers.",
      status: "open"
    },
    {
      id: "Q03", group: "trust", priority: "High",
      q: "Will the house still be the parent’s principal residence on the date of death?",
      why: "Proposition 19 relief needs the home to be the transferor’s principal residence as well as the heir’s. Renting it outside the immediate family, or holding it in an LLC, can forfeit the relief before the inheritance ever happens.",
      known: "The parent lives there now. The conditions are published: principal residence of transferor and transferee, claim within three years, homeowners’ exemption within one year.",
      src: ["boeProp19", "boeLta2026026"],
      missing: "What happens if the parent moves to a care facility; whether the house would be rented in the meantime; how title is held. The Board’s guidance adds that the exclusion is removed if the home becomes ineligible for the homeowners’ or disabled veterans’ exemption.",
      discover: "Ask the county assessor in writing before any change of use or title. Keep the parent’s homeowners’ exemption and mail records.",
      flip: "Without relief, property tax on a rented Property A is levied on full market value, which is the single largest cost difference between the plans.",
      status: "open"
    },
    {
      id: "Q04", group: "trust", priority: "Medium",
      q: "How much cash and insurance will be in the estate, and who pays the estate’s bills?",
      why: "Federal estate tax, if any, is due nine months after death with the return; administration costs and the mortgage, if any, come first. A house-rich, cash-poor estate can be forced to sell.",
      known: "The 2026 federal filing threshold is $15,000,000 and the 2027 amount is $15,480,000. California imposes no estate or inheritance tax. The money in the estate was not supplied.",
      src: ["irsEstateTax", "caEstate", "irs706"],
      missing: "Account balances, life insurance, debts, prior taxable gifts, and whether the trust or the estate pays the tax.",
      discover: "Build one asset-and-liability list with the trustee and a CPA, including beneficiary designations and any filed gift tax returns.",
      flip: "If estate tax or a large cash need lands on the house, selling is forced and the timing is set by the IRS, not by the market.",
      status: "open"
    },
    {
      id: "Q05", group: "value", priority: "High",
      q: "What will the house be worth on the date of death?",
      why: "That single number is the heir’s tax basis, the value the assessor reassesses, the basis of the Proposition 19 cap, and the amount the sale would raise.",
      known: "Household estimate: $3,100,000 in November 2026, on an assessed value of about $550,540. The model grows it 3.5% a year, reaching $5,959,750 for a 2045 inheritance.",
      src: ["irsInherited", "sccBill"],
      missing: "A date-of-death appraisal, comparable sales at that date, and any decline-in-value review by the assessor.",
      discover: "Commission a date-of-death appraisal (retrospective if the death has already happened). Check the assessor’s annual report and the parcel record.",
      flip: "A lower appraisal lowers the basis and the sale proceeds, and reduces the property tax after reassessment. The ranking is sensitive to it only through the sale costs and the tax on later gain.",
      status: "open"
    },
    {
      id: "Q06", group: "value", priority: "High",
      q: "What is the tax-rate area on the Property A bill, and what total rate applies?",
      why: "The 1% general levy is only part of the bill. Voter-approved bonds and direct charges are added, and they differ by tax-rate area. The site uses a hypothetical 1.2% levy for Property A.",
      known: "The county publishes a rate book by agency and tax-rate area each year. The exact rate for this parcel was not supplied.",
      src: ["sccTaxBook", "sccBill"],
      missing: "The tax-rate area code, the current secured bill, any direct or special assessments, and any Mello-Roos district.",
      discover: "Open the current secured property tax bill or the assessor’s parcel page; match the rate area to the county rate book.",
      flip: "Each 0.1 point of rate is real money every year after reassessment. A high-rate area strengthens selling; a low-rate area narrows the gap.",
      status: "open"
    },
    {
      id: "Q07", group: "value", priority: "High",
      q: "Will the heir qualify for the parent-child exclusion, and for how much?",
      why: "The exclusion caps the assessed value at the parent’s factored base year value plus an inflation-adjusted amount. It is the difference between a property tax bill based on about $550,540 and one based on market value.",
      known: "The published cap is the factored base year value plus $1,044,586 for transfers from 16 February 2025 to 15 February 2027; it is adjusted every two years. Homeowners’ exemption within one year; exclusion claim within three years or before a transfer. The Board’s 2026 guidance states the exclusion is removed if the home becomes ineligible for the homeowners’ or disabled veterans’ exemption.",
      src: ["boeLta2025009", "boeProp19"],
      missing: "Whether the heir will move in within one year and stay; the amount set from 16 February 2027, which the Board had not published at this review.",
      discover: "Read the assessor’s claim form and instructions; file the homeowners’ exemption and the exclusion claim on time. Watch the Board’s February adjustment.",
      flip: "No move-in means no relief: the rented case pays tax on the full market value. Relief removes roughly the tax on the value above the cap, for as long as the heir lives there.",
      status: "open"
    },
    {
      id: "Q08", group: "value", priority: "Medium",
      q: "What is the heir’s basis in Property B, and how much assessed value would a sale give up?",
      why: "Property B is the household’s fallback and its rent pays the bills. Its assessed value is far below market, so a sale would both realise a taxable gain and reset the tax bill upward.",
      known: "Property B is already owned by the heir. Its 2026 assessed value in the model is about $114,250; the two rented units bring in about $7,150 a month.",
      src: ["sfAssessment", "boeProp13"],
      missing: "Purchase price and date, capitalised improvements, any depreciation taken, and the current assessed value on the bill.",
      discover: "Pull the closing statement and improvement records; read the current bill and the assessor’s parcel page.",
      flip: "This does not change the Property A ranking, but it sets the cost of ever using B as the source of cash — which is the fallback if the estate needs liquidity.",
      status: "open"
    },
    {
      id: "Q09", group: "value", priority: "Medium",
      q: "What tax rate will apply to a sale, in the heir’s actual sale year?",
      why: "The model uses a 33.1% blended rate on gain. The real rate depends on filing status, other income, the federal 0/15/20% brackets, the 3.8% net investment income tax, and California’s brackets.",
      known: "Federal long-term rates are 0%, 15% and 20%; the net investment income tax is 3.8% above published thresholds; California taxes capital gains as ordinary income.",
      src: ["irsTopic409", "irsTopic559", "ftbCapGains"],
      missing: "The heir’s filing status, income in the sale year, deductions, and the size of the gain after the basis and selling costs.",
      discover: "Have a CPA run the sale year with and without the sale; ask for the marginal rate on the gain, not an average.",
      flip: "A prompt sale after a basis reset has little or no gain, so the rate matters most in the rent and live cases, which are already behind.",
      status: "open"
    },
    {
      id: "Q10", group: "costs", priority: "High",
      q: "What would it cost to rebuild the house?",
      why: "A homeowners policy is written on the cost to rebuild, not on the market value. The dwelling limit sets the premium, and the premium is one of the three blank inputs on the site.",
      known: "No rebuild figure was supplied. The state regulator’s 2026 survey prices a hypothetical Cupertino home at about $1,540 to $6,430 a year at a $1,000,000 dwelling limit, rounded to $10, depending on the insurer.",
      src: ["cdiSurveyCup40_1000", "cdiResGuide"],
      missing: "A rebuild estimate for this house: size, construction, age, foundation, roof, code upgrades, and site access.",
      discover: "Ask a local builder or an insurer for a replacement-cost estimate; then get written quotes at that dwelling limit.",
      flip: "It sets the premium, not the ranking. Every premium in the surveyed range still leaves selling first.",
      status: "open"
    },
    {
      id: "Q11", group: "costs", priority: "High",
      q: "What premiums will insurers actually charge: homeowner for A, landlord for A, landlord for B?",
      why: "The site carries $1,500 a year for each property as a household guess, labelled unverified. A landlord policy on a rented house and an owner policy are different products.",
      known: "The regulator’s survey covers owner-occupied homes only and has no profile for a rented two-to-four-unit building. Earthquake cover is a separate policy; the survey gives rates per $1,000 of cover.",
      src: ["cdiSurveyCup40_500", "cdiResGuide", "fairPlan"],
      missing: "Three written quotes, the dwelling limits, deductibles, and a decision on earthquake cover for each property.",
      discover: "Ask two or three brokers for all three quotes in writing, plus one earthquake quote per property. Ask whether the insurer writes new policies in each ZIP code.",
      flip: "Insurance is a small share of the yearly cost; the earthquake decision is the large one, because an uninsured loss is modelled on the stress pages.",
      status: "open"
    },
    {
      id: "Q12", group: "costs", priority: "Medium",
      q: "What are the water, electricity and solar terms on the accounts?",
      why: "Water is metered and tiered; the solar credit depends on the tariff and on when the system was interconnected. The household reports $100–$150 a month for water and a small net credit for electricity.",
      known: "The model uses about $130 a month for water and a $180-a-year solar credit. The utility rate schedules are published; the account terms are not. Statewide, the legacy net-metering tariffs are closed to new enrolments; since 15 April 2023 new interconnections take net billing, which pays for exported power at a value-of-generation rate.",
      src: ["waterA", "solar", "cpucNem"],
      missing: "Meter size, usage history, tariff name, interconnection date, true-up statement, and whether the credit survives a change of occupant.",
      discover: "Download twelve months of bills and the net-metering agreement; ask the utility which tariff applies in the heir’s name.",
      flip: "If a favourable tariff ends before the inheritance, the electricity credit should not be counted; a replaced roof may also require removing and reinstalling panels.",
      status: "open"
    },
    {
      id: "Q13", group: "costs", priority: "Medium",
      q: "What major repairs are due, and when?",
      why: "The model uses 0.5% of value a year for maintenance. That averages a roof, a furnace, a sewer lateral and a foundation repair into a smooth line, which is not how houses spend money.",
      known: "No inspection report or reserve schedule was supplied. Repair costs are generally deductible against rent; improvements are capitalised instead.",
      src: ["irsPub527", "irsRental"],
      missing: "Age and condition of roof, HVAC, electrical panel, plumbing, sewer lateral, foundation and drainage; any known structural issues.",
      discover: "Commission a pre-listing inspection now, while there is time to fix or price the items. Ask a contractor for a five-year reserve schedule.",
      flip: "One large repair in the first years can wipe out the narrow first-year rental margin, which is why the rental case is already the weaker option.",
      status: "open"
    },
    {
      id: "Q14", group: "costs", priority: "High",
      q: "What rent would Property A actually fetch, and what law governs increases?",
      why: "The rented case is the closest alternative to selling, and its income is the HUD benchmark, not a lease. Rent-growth rules decide what that income does over ten years.",
      known: "HUD’s FY2026 small-area benchmark for the ZIP code is $6,390 a month for four bedrooms and $5,870 for three. The statewide rent cap is 5% plus the change in the cost of living, maximum 10%, for most housing more than 15 years old, subject to exemptions.",
      src: ["hudA", "caRentCaps", "cupertinoADU"],
      missing: "A market rent opinion for this house, its condition and size, whether the statewide cap or a local ordinance covers it, and the tenancy terms the heir would offer.",
      discover: "Two written rental opinions from local agents; read the Attorney General’s rent-cap page and ask the city whether any local ordinance applies. The city also allows an ADU that may be rented but not sold separately — one more way to add income.",
      flip: "Higher rent narrows the gap to selling but does not close it in the base case; a rent-control exemption would raise the ten-year figure.",
      status: "open"
    },
    {
      id: "Q15", group: "costs", priority: "Medium",
      q: "How many months will the house be held before it sells, and what does that cost?",
      why: "The model sells on the day of death. In practice there are weeks or months of probate-free trust administration, clean-out, marketing and closing, during which the house is taxed, insured and empty.",
      known: "The model charges a 6% sale cost and nothing for the holding period. California withholds 3 1/3% of the price at closing unless an exemption is certified before the close.",
      src: ["ftb593", "boeProp19"],
      missing: "The realistic marketing period, clean-out and staging cost, and whether any repair is needed to sell.",
      discover: "Ask two agents for a net sheet and a marketing timeline; prepare the Form 593 exemption certificate with the trustee before closing.",
      flip: "A long hold adds cost and can push the sale into a later tax year; it does not reverse the ranking unless it runs for years.",
      status: "open"
    },
    {
      id: "Q16", group: "money", priority: "High",
      q: "How much money is in the estate, and in what form?",
      why: "Federal estate tax starts above the exclusion and reaches 40%. Retirement accounts, life insurance, joint accounts and property inside the trust are each treated differently, and some pass outside the will.",
      known: "Federal threshold $15,000,000 for 2026 and $15,480,000 for 2027; no California estate or inheritance tax; the amount and kind of money in this estate were not supplied.",
      src: ["irsEstateTax", "caEstate"],
      missing: "Balances by account type, beneficiary designations, prior taxable gifts, debts and administration expenses.",
      discover: "One inventory with the trustee and a CPA. List each account with owner, type, value and named beneficiary, and note any gift above the annual exclusion.",
      flip: "Above the threshold, each additional $1,000,000 of estate can cost up to $400,000 in federal tax, which can force a sale of the house for liquidity.",
      status: "open"
    },
    {
      id: "Q17", group: "money", priority: "High",
      q: "What will the sale proceeds be invested in, at what cost, and with what risk?",
      why: "The sell-first answer is really an answer about a diversified portfolio returning 5% a year after tax. Nothing in the site says what that portfolio is, what it costs, or who manages it.",
      known: "The model assumes 5% a year after tax. Insured deposits are covered to $250,000 per depositor, per bank, per ownership category. Diversification does not guarantee a result.",
      src: ["fdic", "investorRisk"],
      missing: "A written investment policy: allocation, expected return and volatility, fees, tax location, rebalancing rule, and who decides.",
      discover: "Write a one-page policy before the sale. Compare at least two low-cost providers and ask for all-in fee disclosure.",
      flip: "If the proceeds earn 3% instead of 5% a year after tax, the lead over renting shrinks sharply; below about 4% on equal tax terms the two are close.",
      status: "open"
    },
    {
      id: "Q18", group: "money", priority: "Medium",
      q: "Is there cash outside the house for the first year of bills, fees and taxes?",
      why: "Between the death and the sale or move-in, the household pays property tax, insurance, utilities, legal fees and possibly an appraisal — before any rent or sale proceeds arrive.",
      known: "The 2026 first-year costs of holding Property A are modelled on the Properties page. Statutory probate fees, if the house is outside the trust, follow a published scale: 4% of the first $100,000 down to 0.5% of the next $15,000,000.",
      src: ["prob10800", "fdicDeath"],
      missing: "The estate’s liquid reserves, which accounts are payable on death, and whether the trust can advance costs.",
      discover: "Ask the trustee what can be released and when; keep a separate reserve outside the estate if possible.",
      flip: "Without liquidity, the sale happens on someone else’s timetable, which is the most expensive way to sell a house.",
      status: "open"
    },
    {
      id: "Q19", group: "home", priority: "High",
      q: "Does the heir want to live in Cupertino, and would the household actually move?",
      why: "This is the only question the model cannot answer. Living in Property A ranks last on money because it gives up the rent and the invested proceeds; if the household values the house, schools or the commute, that is a legitimate reason to choose it anyway.",
      known: "The heir can live in Property B’s third unit without losing either rent. Both the sale exclusion and Proposition 19 depend on which home is the principal residence.",
      src: ["irsTopic701", "boeProp19"],
      missing: "A written list of what the household wants from the house, and what it would give up. Timing, schools, work location, care responsibilities.",
      discover: "Write the non-financial criteria down before looking at the tables again. Decide which of them would justify a five- or six-figure difference.",
      flip: "If the answer is yes, plan 3 or 4 applies and the Prop 19 deadlines become the first thing to diarise. The money comparison then becomes the price of that choice, not a veto.",
      status: "open"
    },
    {
      id: "Q20", group: "home", priority: "Medium",
      q: "Would the household keep two houses in one earthquake region, and can it manage a rental?",
      why: "Keeping Property A concentrates the household’s wealth in one regional housing market and one fault system, and adds landlord duties in a second city.",
      known: "Both properties are in the Bay Area. A homeowners policy generally excludes earthquake; separate cover is available. USGS puts the chance of a magnitude 6.7 or greater earthquake in the Bay Area within 30 years at 72%, and 51% at magnitude 7 or greater.",
      src: ["usgsQuake", "cdiResGuide"],
      missing: "The household’s tolerance for concentration and management, a property-manager quote, and an earthquake quote for each property.",
      discover: "Price a manager and an earthquake policy. Compare the combined exposure with the portfolio alternative on the Best plan page.",
      flip: "If a manager plus earthquake cover costs more than the rental margin, the rented case loses its remaining advantage.",
      status: "open"
    },
    {
      id: "Q21", group: "law", priority: "Medium",
      q: "Will the step-up in basis, Proposition 19 or the federal exclusion change before the inheritance?",
      why: "These are the rules the answer is built on. Each has been proposed for change; none has been enacted.",
      known: "Current law applies: basis resets at death, Proposition 19 relief is capped and conditioned, and the federal exclusion is $15,000,000 for 2026 and $15,480,000 for 2027. A 2026 initiative to restore the pre-2021 reassessment rule failed to qualify.",
      src: ["hr1301", "sosInitiative1994", "boeProp19"],
      missing: "Future legislation. Nothing can supply it.",
      discover: "Watch Congress.gov bill status, the Board of Equalization letters and the Secretary of State’s initiative list each year. The site keeps a watchlist on the Sources page.",
      flip: "A repeal of the step-up would hurt every plan that sells later, and would weaken the case for selling at once. The Other options page tests the pre-2021 rule.",
      status: "unknowable"
    },
    {
      id: "Q22", group: "law", priority: "Medium",
      q: "What will home prices, inflation and investment returns do over the next fifty years?",
      why: "The base case is a straight line. Real decades are not straight, and the ranking depends on the difference between home-price growth and portfolio returns.",
      known: "Recorded official series, 1970–2025, and 2,000 random histories built from them. On equal tax terms, renting overtakes selling at about 5.3% yearly home growth or a portfolio return below about 4.0% after tax.",
      src: ["fredSJ", "blsCpiHistory", "cboOutlook2026"],
      missing: "The future. Use ranges, break-evens and a decision rule instead of a point forecast.",
      discover: "Re-run the stress pages when prices, rates or insurance move sharply. Set the triggers in advance.",
      flip: "In the recorded replay of the last 49 years and in a 1970s-style stagflation, keeping the house wins. That is the honest counter-case to the base answer.",
      status: "unknowable"
    }
  ],
  answered: [
    {
      id: "A01",
      q: "How much can pass free of federal estate tax?",
      answer: "$15,000,000 for a death in 2026 and $15,480,000 for 2027. Above the exclusion the rate reaches 40%.",
      src: ["irsEstateTax", "irs2027"],
      effect: "Room after Property A is about $11,900,000 (2026) and $12,271,500 (2027) before other assets. Whether this estate is above it is unknown."
    },
    {
      id: "A02",
      q: "Does California tax an inheritance?",
      answer: "No. No California estate tax return has been required for deaths on or after 1 January 2005, and there is no inheritance tax.",
      src: ["caEstate"],
      effect: "Only the federal level and the property-tax reassessment matter for this estate."
    },
    {
      id: "A03",
      q: "What is the heir’s tax basis in the house?",
      answer: "Generally the fair market value on the date of death, whether or not a federal estate return is filed.",
      src: ["irsInherited"],
      effect: "A prompt sale has little or no taxable gain — the main reason selling first leads."
    },
    {
      id: "A04",
      q: "What are the parent-child reassessment conditions and deadlines?",
      answer: "Principal residence of both parent and child; capped at the factored base year value plus $1,044,586 for transfers to 15 February 2027; homeowners’ exemption within one year; exclusion claim within three years or before a transfer to a third party.",
      src: ["boeProp19", "boeLta2025009"],
      effect: "Sets the property tax in the live case and removes it from the rented case."
    },
    {
      id: "A05",
      q: "How much gain can be excluded on a home sale?",
      answer: "Up to $250,000, or $500,000 on a joint return, if the ownership and use tests are met: 24 months of each in the five years before the sale.",
      src: ["irsTopic701"],
      effect: "Relevant only if the heir lives in the house for two years; a sale right after death has almost no gain to exclude."
    },
    {
      id: "A06",
      q: "Is tax withheld when the house is sold?",
      answer: "California withholds 3 1/3% of the price unless the seller certifies an exemption before the close. The withheld amount is recovered only as a credit on the tax return.",
      src: ["ftb593"],
      effect: "A cash-flow item at closing, not a final cost. Plan the exemption certificate before the sale."
    },
    {
      id: "A07",
      q: "What does San Francisco charge per rental unit, and when?",
      answer: "$59 per dwelling unit for 2026–27, due 1 March, with 5% late penalties to a 15% cap. Exemption requests for the 2027 fee are due 14 December 2026.",
      src: ["sfRentFee"],
      effect: "Two rented units at $59 is about $120 a year; a vacant unit is still billed unless an exemption is approved."
    },
    {
      id: "A08",
      q: "What would probate cost if the house is not in the trust?",
      answer: "Statutory compensation is 4% of the first $100,000, 3% of the next $100,000, 2% of the next $800,000, 1% of the next $9,000,000 and 0.5% of the next $15,000,000, for the representative and again for the attorney.",
      src: ["prob10800"],
      effect: "Avoidable by holding title in the trust; expensive if not."
    },
    {
      id: "A09",
      q: "How much deposit insurance applies to sale proceeds?",
      answer: "$250,000 per depositor, per bank, per ownership category. Investments and mutual funds are not deposits.",
      src: ["fdic"],
      effect: "Sale proceeds cannot all sit in one bank account; a Treasury or money-market plan is needed while the portfolio is set up."
    },
    {
      id: "A10",
      q: "What must the trustee do, and by when?",
      answer: "Serve notification on beneficiaries and heirs within 60 days of becoming trustee; report a change of ownership to the assessor within 150 days of the death.",
      src: ["probate160617", "rtc480"],
      effect: "Sets the clock for challenges and avoids the assessor’s penalty."
    },
    {
      id: "A11",
      q: "Is there a statewide limit on rent increases?",
      answer: "Yes: 5% plus the change in the cost of living, capped at 10% a year, for most housing more than 15 years old, subject to statutory exemptions and local ordinances.",
      src: ["caRentCaps"],
      effect: "Constrains rent growth in the rented case. Whether an individually owned single-family home is exempt has to be confirmed."
    },
    {
      id: "A12",
      q: "When is the federal estate return due?",
      answer: "Nine months after death. The representative may ask for an extension of time to file of up to six months.",
      src: ["irs706"],
      effect: "The first hard deadline in any plan that involves federal estate tax."
    }
  ],
  unknowable: [
    { id: "U01", q: "The date of death, and therefore the inheritance year", why: "The parent is alive; the brief sets a 2040–2050 window.", handling: "The model runs 2040, 2045 and 2050. Selling leads in all three.", trigger: "Re-run when health or living arrangements change.", src: ["irsInherited"] },
    { id: "U02", q: "Home prices and investment returns after the inheritance", why: "No official body forecasts a 50-year path for one ZIP code.", handling: "Recorded series 1970–2025, 12 scenario replays and 2,000 random histories; break-even rates are published.", trigger: "Re-run the stress pages when prices or rates move sharply.", src: ["fredSJ", "blsCpiHistory"] },
    { id: "U03", q: "Federal and state law in 2040–2050", why: "Legislation cannot be verified before it exists.", handling: "Current law is used everywhere; pending bills are listed as proposals only.", trigger: "Check the watchlist each February and after each election.", src: ["hr1301", "sosInitiative1994"] },
    { id: "U04", q: "The insurance market and the FAIR Plan in 2040", why: "Premiums and insurer appetite change yearly.", handling: "The decision is tested across the regulator’s surveyed range; the rankings do not move.", trigger: "Re-quote at every renewal.", src: ["insurance", "fairPlan"] },
    { id: "U05", q: "Whether an earthquake strikes while the house is owned", why: "The probability is published; the timing is not.", handling: "An uninsured structural loss is modelled as a stress case; earthquake cover is priced separately.", trigger: "Decide on cover before the inheritance, not after.", src: ["usgsQuake", "cdiSurveyEqCup"] },
    { id: "U06", q: "The property tax rate after reassessment", why: "Voter-approved bond rates change at each election.", handling: "A 1.2% levy is used for Property A and the county rate book is linked; the rate is applied to the assessed value.", trigger: "Read the new bill in the first year after the transfer.", src: ["sccTaxBook"] },
    { id: "U07", q: "The heir’s income and filing status in the sale year", why: "Future income, marriage and retirement all change the brackets.", handling: "A 33.1% blended rate is used; the sensitivity shows the effect of the rate on the rent and live cases only.", trigger: "Have a CPA compute the actual year before selling.", src: ["ftbCapGains", "irsTopic409"] },
    { id: "U08", q: "Whether the heir will want to live in the house", why: "A preference, not a fact.", handling: "The live case is shown on money alone, with a note that housing value is excluded.", trigger: "The household decides; the model then prices the choice.", src: ["irsTopic701"] }
  ],
  discovery: [
    { id: "D01", doc: "Trust document, schedule of assets and distribution clause", where: "Trustee or the parent’s trust attorney", closes: "Q01, Q02, Q04", src: ["probate160617"], effort: "1–2 hours to read with advice" },
    { id: "D02", doc: "Current secured property tax bill and assessor parcel record", where: "Santa Clara County Department of Tax and Collections; assessor", closes: "Q05, Q06, Q07", src: ["sccBill"], effort: "About 30 minutes online" },
    { id: "D03", doc: "County tax-rate book for the parcel’s tax-rate area", where: "Santa Clara County Controller–Treasurer", closes: "Q06, U06", src: ["sccTaxBook"], effort: "About 30 minutes" },
    { id: "D04", doc: "Three insurance quotes plus earthquake quotes", where: "Brokers and insurers writing in both ZIP codes; the regulator’s comparison tool for a benchmark", closes: "Q10, Q11, Q20", src: ["insurance"], effort: "2–4 hours including calls" },
    { id: "D05", doc: "Twelve months of utility bills and the solar net-metering agreement", where: "San Jose Water and PG&E account portals", closes: "Q12", src: ["solar", "waterA"], effort: "About 1 hour" },
    { id: "D06", doc: "Pre-sale inspection and a five-year repair reserve", where: "A licensed inspector and a contractor", closes: "Q13", src: ["irsPub527"], effort: "Half a day plus the report" },
    { id: "D07", doc: "Two written rental opinions and the rent-increase rules", where: "Local letting agents; Attorney General and the city", closes: "Q14", src: ["caRentCaps", "hudA"], effort: "2–3 hours" },
    { id: "D08", doc: "Estate inventory with beneficiary designations", where: "Trustee, CPA and the account statements", closes: "Q04, Q16, Q18", src: ["irsEstateTax"], effort: "3–5 hours, once" },
    { id: "D09", doc: "CPA projection of the sale year and of estate tax", where: "CPA or enrolled agent", closes: "Q09, Q16, Q17", src: ["irs706"], effort: "One meeting plus documents" },
    { id: "D10", doc: "Written investment policy for the sale proceeds", where: "The household, with any adviser; fee disclosures from providers", closes: "Q17", src: ["investorRisk", "fdic"], effort: "2–3 hours" },
    { id: "D11", doc: "Date-of-death appraisal and original purchase records", where: "A licensed appraiser; the trust file", closes: "Q05, Q08", src: ["irsInherited"], effort: "Arranged at the death" },
    { id: "D12", doc: "Confirmation of cover and deadlines from the assessor and the trustee", where: "County assessor; trustee; San Francisco Rent Board portal", closes: "Q03, Q07, A07, A10", src: ["boeProp19", "sfRentFee"], effort: "About 1 hour" }
  ]
};
