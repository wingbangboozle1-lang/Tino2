# Insurance research — session `60ca3e1f`, 12 November 2026

Repository-only note (not part of the published site). No personal information. Dollar figures are rounded to $10 unless a government body publishes the exact amount. Nothing here is a quote, and nothing here is the premium for either property.

## What was asked and what was found

The brief asks for the insurance cost of both properties from official sources. Earlier sessions left both premiums blank because the regulator's comparison tool could not be read. This session read it.

| Question | Answer | Official source |
|---|---|---|
| Does any official body publish a premium for a specific home? | No. Both premiums stay blank. | [Department of Insurance: results are not quotes](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/index.cfm) |
| What does the regulator's 2026 survey show for a made-up home in Cupertino? | See the table below. | [Result page, $1,000,000 dwelling](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,40%20Years,1000000,Y) |
| What sets the premium? | The dwelling limit, which is the cost of rebuilding the house, not the market value of the property. | [Residential guide](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm) |
| Is there a survey profile for a rented three-unit building? | No. The profiles are homeowners, condominium, renters and earthquake. | [Survey profiles](https://www.insurance.ca.gov/01-consumers/105-type/9-compare-prem/homeowners-profile.cfm) |
| Is an empty house covered? | The guide lists "Losses to house vacant for 60 days or more" among perils generally not covered. The policy itself decides. | [Residential guide](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm) |
| Is earthquake damage covered? | Generally not. It is a separate policy that the insurer must offer. | [Residential guide](https://www.insurance.ca.gov/01-consumers/105-type/95-guides/03-res/res-ins-guide.cfm) |

## The survey, as read

Premiums in force on 1 May 2026, new policy, $2,500 deductible. "Middle" is the median of the insurers that show a premium, calculated here and rounded to $10. Lowest and highest are the published amounts.

| Hypothetical home | Insurers showing a premium | Lowest | Middle | Highest | At or below $1,500 | Official source |
|---|---|---|---|---|---|---|
| Cupertino, 40 years old, $500,000 to rebuild | 35 of 37 | $790 | $1,380 | $3,371 | 20 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,40%20Years,500000,Y) |
| Cupertino, 40 years old, $750,000 to rebuild | 35 of 37 | $1,167 | $2,020 | $4,901 | 4 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,40%20Years,750000,Y) |
| Cupertino, 40 years old, $1,000,000 to rebuild | 35 of 37 | $1,543 | $2,690 | $6,430 | 0 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,40%20Years,1000000,Y) |
| Cupertino, 70 years old, $1,000,000 to rebuild | 34 of 36 | $1,598 | $2,740 | $4,968 | 0 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,HOMEOWNERS,70%20Years,1000000,Y) |
| San Francisco Sunset, 40 years old, $1,000,000 to rebuild | 35 of 37 | $1,328 | $3,350 | $10,384 | 1 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SAN%20FRANCISCO%20SAN%20FRANCISCO-Sunset%20District,HOMEOWNERS,40%20Years,1000000,Y) |
| San Francisco Sunset, 70 years old, $1,000,000 to rebuild | 34 of 36 | $1,413 | $3,190 | $10,384 | 1 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:SAN%20FRANCISCO%20SAN%20FRANCISCO-Sunset%20District,HOMEOWNERS,70%20Years,1000000,Y) |

Every row of every page is in `build_insurance_survey.py`; the statistics are in `insurance-survey-2026.json`.

**What this says about the household's $1,500.** It fits a Cupertino house that costs about $500,000 to rebuild. It is low for $750,000 (4 of 35 insurers at or below it) and below every surveyed insurer at $1,000,000. The rebuild cost of Property A was not supplied, so the estimate is neither confirmed nor ruled out.

**What the survey leaves out.** Wildfire surcharges, which the tool's own page says can range from 15% to over 300%. Any discount. Any insurer that is not taking new customers in the ZIP code.

**Property B.** A three-unit building with two rented units needs a landlord policy. The survey has no such profile. The Sunset rows are for an owner-occupied single-family home and are context only.

## Earthquake

The survey gives a yearly rate for each $1,000 of cover, not a premium. Single-family profile 901.

| Survey location | Insurers listed | Showing a rate | Lowest | Middle | Highest | Sell through the California Earthquake Authority | Refer to footnotes | Official source |
|---|---|---|---|---|---|---|---|---|
| Cupertino | 40 | 19 | $1.15 | $3.10 | $15.00 | 13 | 8 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_SUBMIT:SANTA%20CLARA%20CUPERTINO,EARTHQUAKE%20-%20Single%20Family,Y) |
| San Francisco Sunset | 40 | 19 | $1.13 | $3.29 | $15.00 | 13 | 8 | [result page](https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_SUBMIT:SAN%20FRANCISCO%20SAN%20FRANCISCO-Sunset%20District,EARTHQUAKE%20-%20Single%20Family,Y) |

The page's own example: $2.40 per thousand on $250,000 of cover is $600 a year. By the same arithmetic $3.10 on $1,000,000 is $3,100 a year. The model has no earthquake premium.

## The insurer of last resort, by ZIP code

Residential FAIR Plan policies in force at 30 September, as published.

| Area | 2022 | 2023 | 2024 | 2025 | 2026 | Official source |
|---|---|---|---|---|---|---|
| ZIP 95014 | 74 | 51 | 119 | 213 | 227 | [FAIR Plan, policies in force by ZIP code](https://www.cfpnet.com/wp-content/uploads/2026/10/CFP-5-yr-PIF-Zip-FY26-DWE-261020.pdf) |
| ZIP 94122 | 15 | 21 | 81 | 129 | 154 | [same file](https://www.cfpnet.com/wp-content/uploads/2026/10/CFP-5-yr-PIF-Zip-FY26-DWE-261020.pdf) |
| California | 265,909 | 320,572 | 449,832 | 621,234 | 665,673 | [same file](https://www.cfpnet.com/wp-content/uploads/2026/10/CFP-5-yr-PIF-Zip-FY26-DWE-261020.pdf) |

The file does not give the number of homes in a ZIP code, so no share is stated. The Department's guide describes a FAIR Plan policy as a basic fire policy without liability or theft cover.

## How fast premiums have risen

Statewide earned premium divided by earned exposures, all residential policy forms: about $730 in 2018 and about $1,130 in 2023. That is 9.05% a year. The model raises insurance 3% a year. Source: [SB 824 workbook](https://www.insurance.ca.gov/01-consumers/200-wrr/upload/Residential-Property-Coverage-Amounts-Wildfire-Risk-and-Losses.xlsx) (statewide sheet only; the ZIP sheets were not visible to the reading tool).

## What a different premium does to the decision

`insurance-sensitivity.cjs` loads `site/data/model.js` unchanged and runs it again with only the premium changed. "Sell ahead of rent" is the ten-year result of selling at once minus renting the house out.

| Premium assumed for Property A in 2026 | 2040 inheritance | 2045 inheritance | 2050 inheritance | Best plan |
|---|---|---|---|---|
| $1,500, rising 3% (the published model) | $1,433,470 | $1,729,720 | $2,085,880 | Sell |
| Survey middle at $500,000 to rebuild ($1,380) | $1,431,730 | $1,727,720 | $2,083,550 | Sell |
| Survey middle at $750,000 ($2,020) | $1,441,120 | $1,738,600 | $2,096,160 | Sell |
| Survey middle at $1,000,000 ($2,690) | $1,451,090 | $1,750,150 | $2,109,560 | Sell |
| Survey highest at $1,000,000 ($6,430) | $1,506,460 | $1,814,350 | $2,183,980 | Sell |
| $1,500, rising 9.05% a year | $1,479,210 | $1,808,790 | $2,220,120 | Sell |
| Survey middle at $1,000,000, rising 9.05% a year | $1,533,110 | $1,904,910 | $2,410,750 | Sell |

Insurance is a cost of keeping the house, so a higher premium widens the lead of selling. Property B's net operating income for 2026 in the model is $49,010 at $1,500; each extra dollar of premium takes one dollar off.

## Still blank

- The premium for Property A. Needs the rebuild cost and a written quote.
- The premium for Property B. Needs a landlord quote.
- Any earthquake premium. Needs a decision and a quote.
- The ZIP-level premium figures in the SB 824 workbook and the yearly figures in the Department's market report. The reading tool showed only the statewide sheet and all-years totals.
- The California Earthquake Authority's own calculator. Not opened.

## How the tool was read

The comparison tool is a form. Its result page opens directly with this address pattern, with no session:

`https://interactive.web.insurance.ca.gov/apex_extprd/f?p=111:21::SUBMIT:NO::P21_LOCATION,P21_TYPE,P21_HOME_AGE,P21_INSURANCE_AMOUNT,P21_SUBMIT:<LOCATION>,HOMEOWNERS,<AGE>,<AMOUNT>,Y`

For earthquake the age and amount are left out. The sandbox cannot reach the Department's servers, so the pages were read with the page-reading tool and the figures typed in. `verification/60ca3e1f/check.cjs` compares the typed figures with a second reading and checks them for internal consistency.

Figures from commercial comparison sites turned up in search results. They are not official and were not used.
