# Verification report — session `707ec1e0` (branch `arena/707ec1e0-tino2`)

**Checked:** 16 Nov 2026 (UTC). **State at claim:** `origin/main` = `ace7057` (merge of PR #126, session `ddee2898`). One open PR at claim: **#119** (`arena/84257489-tino2`, verification-only, `CONFLICTING`, idle >16 h) — taken over (see §3). No household value, identifier or ZIP code appears in this file.

## 1. New official claim published by this session: the 2026 annual gift exclusion

| Figure published | Official source | How it was read | Result |
|---|---|---|---|
| For calendar year 2026, the first **$19,000** of gifts to any person (other than gifts of future interests in property) are not included in taxable gifts under §2503 | IRS, Rev. Proc. 2025-32 §4.42(1): https://www.irs.gov/pub/irs-drop/rp-25-32.pdf | The official IRS PDF was opened directly on 16 Nov 2026; §4.42(1) text read verbatim ("For calendar year 2026, the first $19,000 of gifts to any person … are not included in the total amount of taxable gifts under § 2503 made during that year"). Section 4.42's title ("Annual Exclusion for Gifts…") and the table of contents entry were read in the same document. | **MATCH** — this closes irregularity V-84-2 raised by session `84257489` (figure verified but displayed nowhere) |
| Context cross-check: 2026 federal estate basic exclusion **$15,000,000** | IRS, "Working Families Tax Cuts – Individuals and workers": https://www.irs.gov/newsroom/working-families-tax-cuts-individuals-and-workers | Opened and read 16 Nov 2026 ("Estate tax exclusion for tax year 2026 — Basic exclusion amount is $15,000,000"). | **MATCH** — the page the guide already cites; also confirms the current IRS URL that replaced the old "one-big-beautiful-bill" address (irregularity V-84-1) |

**Where the figure was published (all regenerated from `scripts/build-guide.py`):**

- `guide/tax.html` — new row "Annual gift exclusion" in the *Estate, gift and income tax* table, with the Rev. Proc. 2025-32 link in the Reference column.
- `guide/questions.html` — the estate-inventory question's "answer already known from official sources" now states the $19,000 annual exclusion beside the $15,000,000 filing threshold (text only; the register's 21-row structure is unchanged).
- `guide/sources.html` — new register row: "IRS Rev. Proc. 2025-32 — the 2026 annual gift exclusion of $19,000 per recipient (§4.42(1)), read 16 November 2026".
- `guide/figures/official-figures.json` — new ledger record `GIFT-ANNUAL-2026` (verified, `checked: 2026-11-16`, exact official amount `$19,000`).

**Display-rule check.** $19,000 is a government-published exact amount (the brief's stated exception) and a multiple of $10, so neither the `$10` display gate nor `check-figures.py` needs an exemption; no allowlist entry was added.

**Irregularity V-84-1 disposition.** The old IRS URL (`…/one-big-beautiful-bill-provisions-individuals-and-workers`) exists only in the unpublished legacy file `pages/inheritance-tax.html` (excluded from Pages by `_config.yml`). The published guide already uses the current 2027-adjustments URL; no published link was broken, and no published link was changed by this session.

## 2. Live-deployment confirmation of the privacy remediation (closes session `9ad78d96`'s open item)

Session `9ad78d96` recorded (PR #125) that the privacy remediation of PR #123 was merged but "live Pages had not yet updated at the last read-back". Status on 16 Nov 2026:

| Check | Result |
|---|---|
| GitHub Pages API (`/repos/…/pages`) | `status: built`, source `main` / `/`, `https_enforced: true`, no error |
| Actions on `main` | `Verify public Pages boundary` **success** (run 43785959920) and `pages build and deployment` **success** (run 43785959646) for the current `main` |
| Live read-back of `https://wingbangboozle1-lang.github.io/Tino2/guide/property.html` (16 Nov 2026) | Serves the synthetic-only guide: banner "Only synthetic example inputs are used. Household records and household-derived figures are not published"; the private-input tables show "— private appraisal required" / "— parcel bill required" placeholders; no property-specific amount. | 

**Conclusion:** the PR #123 privacy remediation is deployed and confirmed live. The standing history/tree exposure rows on the Flagged page are unchanged and remain owner/administrator actions.

## 3. Takeover of stale PR #119 (session `84257489`)

| Step | Result |
|---|---|
| Age/state at takeover | Opened 2026-11-16 01:07 UTC; no commit since; `mergeable: CONFLICTING` against `main`; idle ~16.5 h — far beyond the board's 60-minute rule |
| Diff read in full | **Verification-only**: append-only `COORDINATION.md` block + new `verification/84257489/REPORT.md`. No published page, figure, model input or shared site file |
| Content assessment | Sound. Its 16 Nov cross-check (IRS $15,000,000; Rev. Proc. §4.42(1) $19,000; BOE $1,044,586; Treasury 13 Nov 4.32%/4.88%) was independently re-derived by this session for the two IRS figures above; the BOE and Treasury figures were re-opened the same day by session `b193fff2` (PR #118) with matching results |
| Action | Content preserved **verbatim** in this branch (`verification/84257489/REPORT.md` + board block + takeover note), then PR #119 **closed with a handoff comment** — not merged raw, because merging a conflicting append-only diff could drop a sibling session's block |

## 4. Full local suite on the final tree (16 Nov 2026)

| Check | Result |
|---|---|
| `scripts/build-guide.py` + `scripts/check-generated.py` | PASS — 18 generated public pages up to date |
| `scripts/check-figures.py` | PASS — **40 ledger records, 40 verified, 0 unverified** (39 + this session's `GIFT-ANNUAL-2026`) |
| `scripts/package-site.py` + `scripts/check-publication.py --self-test` | PASS — 32 reviewed files packaged; extra/missing/altered files rejected |
| `scripts/test-guide.cjs` | PASS — 18 rendered pages, **1,055 source-linked rows** (was 1,053; +2 = new tax row + sources row), **12,394 checks** |
| `scripts/privacy-audit.cjs` | PASS — no hashed household-input token, locator or common identifier in the packaged tree |
| `scripts/privacy-gate.py` | PASS — 239 tracked text files |
| `scripts/test-model-reference.py` | PASS — 108 configurations, 250 stress years, 1,500 phased years, 20,736 comparisons |
| `scripts/test-phased.py` | PASS — 113 checks |
| `scripts/validate.js` | PASS — 1,610 checks / 19 pages / 178 official sources |
| `scripts/stress-test.js` | PASS — base case unchanged: sell $7,683,290 · rent $6,249,830 · live $5,135,780 (2040→2050) |

`scripts/test-browser.cjs` cannot start Chromium in this sandbox (`libnss3.so` absent); it runs in CI on the pull request, as every prior session recorded.

**Recommendation check (brief: "after any input changes, rebuild the model and the site and see whether the recommendation moved").** The only input changed is the publication of an official rule figure ($19,000 annual gift exclusion) that was already the law and already used in no model arithmetic — no model input, ranking or projection changed. The stress-test base case above is byte-identical to the pre-change run. **The recommendation did not move.**

## 5. Irregularities

| # | Irregularity | Severity | Disposition |
|---|---|---|---|
| 707-1 | V-84-1 (old IRS URL) exists only in the unpublished legacy `pages/` tree; the published guide was never affected | Low | No published change needed; recorded here and in the PR #119 handoff comment |
| 707-2 | V-84-2 (gift exclusion not displayed) — genuine gap against the brief's threshold requirement | Low → **closed** | Fixed in this session's change set with the primary source linked |
| 707-3 | Standing: pre-rounding history scrub (L-D2), repository visibility, household-document items (appraisal, TRA, leases, premiums) | High/Medium, standing | Unchanged; owner/administrator actions already on the Flagged page |
