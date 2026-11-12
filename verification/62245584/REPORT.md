# Session `62245584` verification report — 12 November 2026

Repository-only record. Not published. Contains no personal information and repeats no household
figure: the figures cited below are either official amounts or values the published model computes.

## 1. What was asked and what was found

The brief asks for two things. This session checked whether the published site already had them.

| Requirement, in the brief's own words | Found on `main` at `bfb2268` | Action |
|---|---|---|
| "a section dedicated for suggestions so someone can review suggestions and choose the best path before implementing any changes" | **Absent.** `grep -ric suggestion site/*.html index.html` returns `0` for all 16 pages. No page, section or data file used the word. | Built `site/suggestions.html` and `site/data/suggestions.js` |
| "a clear list of questions, informations and answers that need to be addressed before any decision can be reasonably made" | **Partly absent.** `site/review.html` is an uncertainty register: priority, item, why it matters, current treatment, resolution route. It does not state what the answer is today, nor whether a plan can be decided. | Built `site/questions.html` and `site/data/questions.js` |
| "Suggestions need to be made to discover missing information" | Absent as a category. | 9 of the 15 suggestions exist specifically to obtain a missing input; each names the document that would settle it. |

Nothing published was changed or removed. The work is additive, plus navigation entries and the
publication manifest.

## 2. Official pages opened and read by this session

Every "settled" answer on the new pages is the rule as written on one of these pages. The wording
quoted is from the page as read on 12 November 2026.

| # | Official page | URL | Wording found | Used for |
|---|---|---|---|---|
| 1 | IRS — Estate tax | https://www.irs.gov/businesses/small-businesses-self-employed/estate-tax | "A filing is required if the gross estate of the decedent, increased by the decedent's adjusted taxable gifts and specific gift tax exemption, is valued at more than the filing threshold for the year of the decedent's death"; table gives 2025 `$13,990,000`, 2026 `$15,000,000` | Q-06, Q-07, Q-10 |
| 2 | IRS — What's new: estate and gift tax | https://www.irs.gov/businesses/small-businesses-self-employed/whats-new-estate-and-gift-tax | "Public Law 119-21 … amends § 2010(c)(3) by increasing the basic exclusion amount to $15,000,000 for calendar year 2026" | Q-36 |
| 3 | IRS — IR-2026-133 (5 Nov 2026) | https://www.irs.gov/newsroom/irs-releases-tax-inflation-adjustments-for-tax-year-2027-taxpayers-continue-to-benefit-from-the-working-families-tax-cuts | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000 … the first $20,000 of gifts to any person … up from $19,000 for calendar year 2026" | Q-07, Q-36, S-05 |
| 4 | IRS — FAQ, Gifts & inheritances | https://www.irs.gov/faqs/interest-dividends-other-types-of-income/gifts-inheritances/gifts-inheritances | "The basis of property inherited from a decedent is generally … the fair market value (FMV) of the property on the date of the decedent's death"; "If you sell the property for more than your basis, you have a taxable gain" | Q-05, Q-17, S-02 |
| 5 | IRS — Topic no. 701, Sale of your home | https://www.irs.gov/taxtopics/tc701 | "you may qualify to exclude up to $250,000 of that gain … if you file a joint return"; "owned the home for at least 24 months (2 years) out of the last 5 years" | Q-20, Q-21, S-13 |
| 6 | California State Controller — Estate tax | https://www.sco.ca.gov/ardtax_estate_tax.html | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return"; "For gifts made prior to June 8, 1982, the State Controller's Office will continue to collect the Gift Tax" | Q-37 |
| 7 | BOE — Proposition 19 | https://boe.ca.gov/prop19/ | Parent-child exclusion: "Principal residence of transferor and transferee"; "Value limit of current taxable value plus $1,000,000 (as biennially adjusted)"; "File for homeowners' exemption within 1 year of transfer; File claim for exclusion within 3 years" | Q-11, Q-12, S-01 |
| 8 | BOE — Letter To Assessors 2025/009 (7 Mar 2025) | https://www.boe.ca.gov/proptaxes/pdf/lta25009.pdf | "the $1 million amount is adjusted to **$1,044,586**"; "for transfers that occur February 16, 2025 through February 15, 2027"; "The next adjustment … will occur in February 2027" | Q-13 |
| 9 | Santa Clara County Assessor — Parent-Child Transfer (Proposition 19) | https://asr.santaclaracounty.gov/tax-savings/transferring-your-assessed-value/parent-to-child-2 | "both the parents prior to the transfer and at least one child after the transfer must be the principal resident within one year of the transfer"; "The value limit is equal to the home's taxable value at time of transfer plus $1 million" | Q-04, Q-15 |
| 10 | Probate Code § 16061.7 (leginfo) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=16061.7.&lawCode=PROB | "The notification by trustee shall be served not later than 60 days following the occurrence of the event"; served on "Each beneficiary of the irrevocable trust … Each heir of the deceased settlor" | Q-01, Q-02, S-03 |
| 11 | Revenue & Taxation Code § 480 (leginfo) | https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=480&lawCode=RTC | "the change in ownership statement or statements shall be filed by the trustee (if the property was held in trust) or the transferee … within 150 days after the date of death"; penalty "one hundred dollars ($100)… not to exceed five thousand dollars ($5,000)" | Q-01 |
| 12 | FTB — 2026 Instructions for Form 593 | https://www.ftb.ca.gov/forms/2026/2026-593-instructions.html | "Withholding is required when California real estate is sold or transferred"; "The sales price is $100,000 or less" is one of the exemptions; "the seller/transferor must submit Form 593 before the close of the real estate transaction to prevent withholding" | Q-19, S-11 |

**Offline cross-check.** Figures already on the site (`$1,044,586`, `$15,000,000`, `$15,480,000`,
`$19,000`/`$20,000`, the 60-day trustee period, the 150-day change-of-ownership period, the 3 1/3%
withholding) match the pages above. No correction to a published figure was needed.

**Pages that could not be opened, and how they are treated.** Two source notes were relied on
without this session opening the page: IRS Topic 559 (retirement-account rules) and the IRS
Topic 409 page on like-kind exchanges. Both are used only to support a statement already published
elsewhere on the site and already recorded in `qa/ledger.json` (N-06, N-05). They are **not** claimed
as freshly verified here, and the rows that use them are marked "settled" on the strength of the
ledger entry, not of an independent read this session. Logged as X-I2 below.

## 3. What the two new pages do, and their rules

### `site/questions.html` — the decision gate

40 questions in 6 sequential groups. Each question carries an answer, a status, why it decides
something, what document would settle it, the plans it blocks, and an official source link.

- **Status vocabulary.** `settled` = an official page fixes it; `household` = it exists only as an
  unverified planning figure; `missing` = nothing in the record answers it, so it is left blank.
- **Blocking rule.** A plan is blocked by every question attached to it whose status is not
  `settled`. That rule is enforced in `scripts/validate.js`, question by question and plan by plan.
  Counts on the page are derived from it and cannot drift from the table.
- **Counts at publication.** 40 questions: 15 settled, 10 household input, 15 missing.
  By plan: the transfer 10 blocking of 12; sell 6 of 14; rent 14 of 20; live 10 of 15.
  **No plan is implementable today**, which is the honest answer and the reason the page exists.

### `site/suggestions.html` — the Suggestions section

15 suggestions, ranked 1–15 with no gap, each with problem, evidence, effort band, risk band,
timing, an alternative, and an official source link. Four paths, each a bundle of suggestions, with
a selector to review a path before anything is implemented.

- **Effort** is a time band (under an hour … a professional engagement), not a duration. Bands are
  deliberately **not** added together; the page shows the longest single step in a path instead.
  An earlier draft summed the bands, which was a meaningless number; that was corrected (X-I1).
- **Risk** is a four-point plain-English scale, not a score.
- **Reversibility.** No suggestion is marked irreversible. An earlier draft marked the California
  withholding suggestion irreversible; it is not, because a withheld amount is recovered as a credit
  on the tax return. Corrected (X-I1).
- **Money effects are computed, never typed.** Every dollar amount on both new pages is produced by
  `MODEL` or `MODEL.estateRow` at render time. `scripts/validate.js` proves this by halving the
  model's property value and asserting that a page answer changes.

## 4. Verification performed on this tree

Run on the final tree, in this order, after `python3 scripts/package-site.py`.

| Check | Result |
|---|---|
| `node scripts/validate.js` | **PASS** — 1,576 checks across 17 pages and 171 official sources (was 1,129 / 15 pages). Includes the new gate, suggestion and path assertions. |
| `node qa/tools/gate.cjs` | **PASS** — 17 rendered pages, 1,436 rows (1,427 with their own official link, 9 calculated rows with a context link only), 4,853 dollar amounts checked (104 official exact amounts), 406 internal and 1,864 external links, **0 errors, 0 warnings** |
| `node scripts/runtime-test.cjs` | **PASS** — 17 rendered pages, 1,436 rendered rows source-linked, no runtime error, no broken local link |
| `python3 scripts/check-publication.py --self-test` | **PASS** — fail-closed tests reject unlisted files, symlinks and missing pages; then **32 reviewed public files only** |
| `node scripts/stress-test.js` | **PASS** — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| `python3 src/check_links.py .` | **PASS** — 66 pages, 871 rows, 124 distinct external links, **0 errors** |
| `python3 integration/tools/privacy_scan.py` | **0 errors**, 198 warnings. **None of the warnings is in a file this session added or edited**; the count rose from 158 to 198 because the scan now covers four new files whose official exact amounts are not yet in the ledger allowlist, which is the known standing condition recorded by earlier sessions. Verified by `grep` on the two new pages: no warning line names `questions` or `suggestions`. |
| Ad-hoc identifier scan | The four new files were grepped for e-mail addresses, street addresses, parcel-number and SSN patterns: **clean**. |

**Rounding.** Every dollar amount added to the site is either a multiple of $10 or an official exact
amount (`$15,000,000`, `$15,480,000`, `$19,000`, `$20,000`, `$1,044,586`, `$250,000`, `$500,000`,
`$1,000,000`). The gate's R1 rule checks this on the rendered page and reported 0 errors.

**Privacy.** No name, street address, parcel number, account number or document was added. Parties
appear only as `[OWNER]`, `[TRUSTEE]`, `[DECEDENT]`, `[HEIR]`; the houses as Property A and
Property B. No household figure is typed into `questions.js` or `suggestions.js`: all of them are
read from `MODEL.BASE`. The only household-shaped number on the new pages is the property value and
the assessed value, and both come from the model at render time.

## 5. Irregularities

| ID | Finding | Severity | Disposition |
|---|---|---|---|
| X-I1 | **Found and corrected in this session, before publication.** The first draft of the suggestions page summed effort bands into a single figure (arithmetically meaningless) and marked the California withholding suggestion as irreversible (it is not: the withheld tax is recovered as a credit on the return). | corrected | Both corrected in `site/data/suggestions.js` and `site/suggestions.html`; the page now shows the longest single step, and no suggestion is marked irreversible. |
| X-I2 | Two sources used on the new pages were **not** re-opened by this session: IRS Topic 559 (inherited retirement accounts) and IRS Topic 409 (like-kind exchanges). Both support statements already published and already ledgered as N-06 and N-05. | Medium | Rows are marked settled on the strength of the existing ledger entry. The two pages are listed here so the next verification session opens them directly. Not a blocker. |
| X-I3 | The property-tax rate for Property A on the new pages is the model's **hypothetical 1.2%** combined levy, not a rate read from a tax rate area. | Medium | Stated on the page and in the questions register (Q-14, S-08). Standing item already on the Flagged for Review page; not created by this session and not hidden by it. |
| X-I4 | The rent benchmark used on the new pages is FY2026 while FY2027 is in force. | Medium | Standing item F-I3 from session `f344fcd1`, carried on the Flagged page and now also posed as question Q-24. Not re-opened here. |
| X-I5 | The new pages state that no plan is implementable today. That is a conclusion drawn from the gate's own rule, not from a legal opinion; a lawyer could advise that part of a plan may proceed on unverified inputs at the household's risk. | Low | Stated on the page: the gate lists what a decision depends on, and does not forbid acting. |

None of these blocks publication. All are published on the pages named above, and X-I2 to X-I4 are
also on the Flagged for Review page.

## 6. Files this session added or changed

Added: `site/questions.html`, `site/data/questions.js`, `site/suggestions.html`,
`site/data/suggestions.js`, `verification/62245584/REPORT.md` (this file).

Changed: `assets/app.js` (two navigation entries), `index.html` (two hero buttons and two category
cards), `scripts/check-publication.py` (four manifest entries), `scripts/validate.js` (page count
15→17 and the new engine checks), `COORDINATION.md` (this session's block only).

No published figure, plan, recommendation or other session's file was modified.
