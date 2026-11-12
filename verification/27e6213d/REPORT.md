# Session 27e6213d — Independent verification pass (2026-11-12)

Branch: `arena/27e6213d-tino2`, based on `main` `052e626` (PR #52).
No open PRs and no live claims at claim time. This session verified the published
site; it did not repeat prior research.

## Automated checks (all PASS)

| Check | Result |
|---|---|
| `node scripts/validate.js` | PASS: 1,561 checks, 18 pages, 177 official sources |
| `node scripts/stress-test.js` | PASS: 50-year paths, estate ownership, privacy, real-dollar, shock tests |
| `python3 scripts/package-site.py` | PASS: canonical site only; rounding rule passed |
| `python3 scripts/check-publication.py --self-test` | PASS: 34 reviewed public files only |
| `node scripts/runtime-test.cjs` | PASS: 18 rendered pages, 1,583 rendered rows source-linked, no runtime errors or broken local links |
| `node qa/tools/gate.cjs` | PASS: 18 pages, 1,583 rows (1,574 with own official link, 9 calculated rows with context link), 4,985 dollar amounts (115 official exact figures), 0 errors, 0 warnings |
| `python3 integration/tools/privacy_scan.py` | 0 errors (228 warnings, all in excluded `verification/` reports of prior sessions) |
| `python3 src/check_links.py .` | 68 pages, 887 table rows, 128 distinct external links |

Base case reproduced: 2040→2050 sell $7,683,290 / rent $6,249,830 / live $5,135,780.

## Official figures re-opened live this session (12 Nov 2026)

| Figure on site | Official page opened | Wording found | Match |
|---|---|---|---|
| 2027 federal basic exclusion $15,480,000; 2026 $15,000,000 | IRS IR-2026-133 | "Estates of decedents who die during 2027 have a basic exclusion amount of $15,480,000, up from a total of $15,000,000 for estates of decedents who died in 2026." | ✓ |
| Prop 19 amount $1,044,586 (16 Feb 2025–15 Feb 2027) | BOE NR 25-02 | "increased by 2.15 percent, from $1,022,600 to $1,044,586" | ✓ |
| HUD FY2027 SAFMR 95014: 3BR $5,440, 4BR $5,800 (0BR $3,040, 1BR $3,440, 2BR $4,050) | HUD FY2027 zip-calc 95014 | Table matches all five bedroom sizes; FY2026 floor $5,760 (4BR) not binding | ✓ |
| HUD FY2027 SAFMR 94122: 1BR $2,770, 2BR $3,410 (0BR $2,370, 3BR $4,460, 4BR $5,020) | HUD FY2027 zip-calc 94122 | Table matches all five bedroom sizes | ✓ |
| SF secured property tax rate FY2026-27 1.18162182% | SF Treasurer & Tax Collector | "The secured property tax rate for Fiscal Year 2026-27 is 1.18162182%." | ✓ |
| SF Rent Board fee $59/unit, $29.50 guest, 50% recovery, due 1 Mar, exemption deadline 14 Dec 2026 | SF Rent Board | All amounts and dates match | ✓ |
| No California estate tax for deaths on/after 1 Jan 2005 | CA State Controller | "For decedents that die on or after January 1, 2005, there is no longer a requirement to file a California Estate Tax Return." | ✓ |
| Documentary transfer tax does not apply to a transfer by reason of death, outright or in trust | RTC § 11930 (leginfo) | "…if by reason of such inter vivos gift or by reason of the death of any person, such lands … are transferred outright to, or in trust for the benefit of, any person or entity." | ✓ |
| County rate $0.55 per $500 | RTC § 11911(a) (leginfo) | "a tax at the rate of fifty-five cents ($0.55) for each five hundred dollars ($500) or fractional part thereof"; (b) a city may impose half that rate; (c) city tax is credited against the county tax | ✓ |

## Privacy check on the published artifact (`_public/`)

- No personal names, street addresses, parcel numbers, or account identifiers.
  Parties appear only as placeholders `[OWNER]`, `[TRUSTEE]`, `[DECEDENT]`, `[HEIR]`.
- Unrounded dollar amounts present are official published rates only (SFPUC
  tariffs, relocation payments, PG&E minimum delivery) — covered by the gate
  check's 115 official exact figures.
- `_config.yml` excludes all legacy root HTML, `docs/`, `research/`,
  `verification/`, `scripts/`, `qa/`, `src/`, `dashboard/`, `pages/`, `css/`,
  and the unreferenced `assets/style.css` / `assets/style.css-alternate.css`.
  Only `assets/app.js` and `assets/styles.css` are published.
- `robots.txt` disallows all crawlers.

## Defects found

None requiring a code or data change. No shared file was edited; this session's
only repo additions are this report and its coordination block.

## Observations (no change made, logged for the owner)

- **O-1 — wording, `rtc11911` source note.** The note at `site/data/sources.js`
  reads "a city may take half as a credit". The statute is narrower: a city may
  *impose* half the county rate (subd. (b)) and that city tax is then *credited*
  against the county tax (subd. (c)). The substance (city receives up to the
  second half of the 0.55%) is right; the mechanism is loose. Low impact — San
  Francisco's actual combined rate comes from its own ordinance, not from this
  note. Left to the next session that owns `sources.js` to reword, because
  editing a shared data file to fix a sentence risks a needless merge conflict.
- **O-2 — hypothetical Property A levy.** `MODEL.BASE.aRate` is 1.2% and is
  labelled in the file itself as a "hypothetical combined levy; actual parcel
  rate unverified". This is the correct treatment: the real rate depends on the
  parcel's tax rate area, which is not public information that can be tied to
  this property without exposing identifying detail. Property B instead uses the
  official 1.18162182% (verified above). Both are surfaced as such on the site.
- **O-3 — model assumptions.** `capitalGainsTax` 0.331 and `estateIndex` 0.02
  are assumptions, not law, and are labelled as assumptions in `model.js`. The
  statutory anchors beside them (exclusion $15,000,000 / $15,480,000, Prop 19
  $1,044,586, §121 $250,000) are all verified above or in the ledger.

## Irregularities

- None new. Known carried-forward items remain on the site's Flagged for Review
  page (unverified household bills, insurance premiums left blank, git-history
  privacy risk) and do not block publication.
