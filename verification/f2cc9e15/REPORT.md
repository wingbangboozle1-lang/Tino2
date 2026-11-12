# Session `f2cc9e15` — README accuracy pass + independent smoke verification (2026-11-12)

Branch: `arena/f2cc9e15-tino2`. Base: `052e626` (merge of PR #52); rebased onto `444be2e` (merge of PR #56) before the smoke verification below, keeping both sides of the one conflict (`COORDINATION.md`, tail block).

**No site content was changed.** `site/**`, `index.html`, `assets/**`, `scripts/**`, `qa/**` were not touched. PR #54 (`arena/9984092e-tino2`) was left untouched.

## 1 · What was asked vs what exists

The brief asks for an executive summary, suggestions and decision-readiness sections, black-swan stress cases, projections, sources, a Flagged-for-Review register and a live GitHub Pages site. All of these exist on `main` (18 pages under `site/` plus `index.html`) and were built and verified by earlier sessions (see `COORDINATION.md`; PRs #1–#56). This session did not rebuild any of it. Its two deliverables are the README correction in §3 and the independent smoke check in §2.

## 2 · Independent smoke verification (re-run on the rebased tree, 2026-11-12 ~22:3x UTC)

| Check | Command | Result |
|---|---|---|
| Model + syntax + links + sources | `node scripts/validate.js` | PASS — 1,561 checks, 18 pages, 177 official sources. Base case 2040→2050: sell $7,683,290 · rent $6,249,830 · live $5,135,780 |
| 50-year stress paths | `node scripts/stress-test.js` | PASS — 50-year paths, estate ownership, privacy, real-dollar and shock tests |
| Package allowlist | `python3 scripts/package-site.py` | PASS — packaged canonical site only; rounding rule passed |
| Publication boundary (fail-closed) | `python3 scripts/check-publication.py --self-test` | PASS — unlisted files / symlinks / missing pages rejected; 34 reviewed public files |
| Rendered-page gate | `node qa/tools/gate.cjs` | PASS — 18 rendered pages · 1,583 rows (1,574 with their own official link; 9 calculated rows with a context link only) · 4,985 dollar amounts checked (115 official exact figures) · 559 internal / 2,074 external links · 0 errors · 0 warnings |
| Internal links | `python3 src/check_links.py .` | PASS — 68 pages, 887 table rows, 128 distinct external links (not machine-checked from this sandbox) |
| Privacy scan | `python3 integration/tools/privacy_scan.py` | 0 errors, 228 standing warnings — all in repository-only files (`verification/**`, etc.), unchanged in kind from the records in `COORDINATION.md` (finding F-I1); the published allowlist artifact is clean under the gate |

GitHub Pages state at the time of the check (Pages API): source `main` / `/ (root)`, HTTPS enforced, latest build `built` with `error.message: null` for commit `052e626` (built 2026-11-12T15:55:48Z). `origin/main` had since advanced to `444be2e` (PRs #55 and #56, both verification-only); the merge of this session's PR triggers a fresh build, recorded on the PR.

Counts above are as printed by the tools, not re-derived. No official page was re-opened by this session and no new figure is claimed; the load-bearing figures were re-opened live by sessions `27e6213d`, `c96c185e` and `60ca3e1f` on 12 Nov 2026 and all matched.

## 3 · README accuracy pass (the one defect this session found and fixed)

Defect (documentation-only), found by reading `README.md` against `ls site/ site/data/`:

- `site/questions.html` was listed **twice** and `site/suggestions.html` **three times**, with mutually inconsistent one-line descriptions (e.g. "22 open questions" vs the 28 in `site/data/questions.js`).
- The list omitted `site/operating-costs.html`, `site/plan.html`, `site/questions-gate.html`, `site/verification.html`, `site/black-swan.html`.
- The data-file list omitted `site/data/gate.js`, `questions.js`, `suggestions.js`, `options.js`, `stress.js`, `costs.js`, `ledger.js`, `history.js`, `history-engine.js`.

Fix: the `Structure` section was rewritten from the files actually present. Descriptions are taken from each page's own `<meta name="description">` / `data-title`; counts were re-derived from the data files (`Q` 28, `A` 14, `U` 8, discovery plans 12, `S` 27 — all `sort -u` counts) or are the figures printed on the published pages (Decision gate "40 questions", recorded as live-verified by session `62245584`). No other line of the README was changed, and `index.html` / `site/**` were not touched. Irregularity logged as **F-R1 (fixed)**.

## 4 · Observations (not fixed here; not blocking)

- **F-O1.** Four independent verification sessions ran on 12 Nov 2026 (`c96c185e` PR #55, `27e6213d` PR #56, `9984092e` PR #54 still open, this one). Their reports agree; the duplication is wasteful but harmless, and none of them changed site content.
- **F-O2.** `check_links.py` does not machine-check the 128 distinct external links from this sandbox; external-link liveness remains a manual/periodic task (README already says so).
- **F-O3.** The standing `needs review` items (owner privacy decisions, blank household-specific figures) remain published on the Flagged for Review page and are unchanged.
- **F-O4.** `privacy_scan.py` warnings confined to repository-only files persist; the published artifact is clean. This is finding F-I1 and needs an owner decision, not an edit.

## 5 · Privacy

No personal information added. README and this report name files, pages and tool outputs only. No household figure is quoted. Household amounts remain rounded to $10 as already published.
