# COORDINATION — shared task board

> **Privacy rule for this file and this whole repository.** The repository and its GitHub Pages site are
> **public**. Nothing personal may be committed anywhere in it: no names, street addresses, parcel numbers,
> account numbers, or exact parcel-specific dollar figures. Use placeholders such as `[OWNER]`, `[HEIR]`,
> `[TRUSTEE]`, `[PROPERTY A]`, `[PROPERTY B]`. There is no "internal use only" location inside a public repo.

Statuses: `unclaimed` · `in progress` · `done` · `needs review` (published on the Flagged for Review page; does not block anything).

---

## 1. Sessions observed

All times UTC, 2026-11-10. Checked with `git ls-remote --heads origin`.

| Session ID | Branch | First claim commit | Board location | Notes |
|---|---|---|---|---|
| `1dab34fa` (calls itself `session-arena`) | `arena/1dab34fa-tino2` | `1e2c1be` at 06:04:43 | `COORDINATION.md` on its own branch only | States it is a "single agent session" |
| `8c4d9e77` | `arena/8c4d9e77-tino2` | `b304453` at 06:05:23 | `COORDINATION.md` on its own branch only | Log says "no other task claims existed" |
| `5a1bd5be` (**this file's author**) | `arena/5a1bd5be-tino2` | this commit, 06:11 | `COORDINATION.md` on its own branch | Third to start; the only session that has seen all three boards |

Branch naming: the instructions ask for `session-<id>/<task>` branches. The hosting environment pins every
session to a fixed `arena/<id>-tino2` branch and no session can push to `main` directly, so that naming is
not possible. Session ID = the 8-character id in the branch name.

---

## 2. Claims made by the other sessions (summarised, not edited — originals are authoritative)

Read from the other branches at the SHAs above. Their files are **not** modified by this session.

| Owner | Task (as written by the owner) | Status (as written by the owner) | File scope claimed by the owner |
|---|---|---|---|
| `1dab34fa` | 1. Create coordination board | in progress | `COORDINATION.md` |
| `1dab34fa` | 2. Research: county/city property tax, base-year assessment, parent-child transfer rules (Property A) | unclaimed, owner column = itself | `research/scc-property-tax.md` |
| `1dab34fa` | 3. Research: San Francisco property tax, assessment, rental tax treatment (Property B) | unclaimed, owner column = itself | `research/sf-property-tax.md` |
| `1dab34fa` | 4. Research: homeowners / rental-property insurance costs | unclaimed, owner column = itself | `research/insurance-costs.md` |
| `1dab34fa` | 5. Research: water and electricity (solar net metering) costs | unclaimed, owner column = itself | `research/utilities.md` |
| `1dab34fa` | 6. Research: federal estate tax exemption, California estate/inheritance tax, pending changes | unclaimed, owner column = itself | `research/inheritance-tax.md` |
| `1dab34fa` | 7. Research: step-up in basis, capital gains, home-sale exclusion, rental income tax | unclaimed, owner column = itself | `research/basis-capital-gains.md` |
| `1dab34fa` | 8. Decision model and projections | unclaimed, owner column = itself | `data/projections.md` |
| `1dab34fa` | 9. Executive summary | unclaimed, owner column = itself | `docs/executive-summary.md` |
| `1dab34fa` | 10. GitHub Pages site | unclaimed, owner column = itself | `index.html`, `pages/*`, `assets/*`, site config |
| `1dab34fa` | 11. Verify every table row; flag unverified items | unclaimed, owner column = itself | `FLAGGED-FOR-REVIEW.md` |
| `1dab34fa` | 12. Enable GitHub Pages, confirm build | unclaimed, owner column = itself | GitHub Pages settings |
| `1dab34fa` | 13. Pull request, merge, record result | unclaimed, owner column = itself | (GitHub PR) |
| `8c4d9e77` | Build inheritance-planning research dashboard, source-backed findings, and GitHub Pages workflow | in progress | `index.html`, `assets/**`, `data/**`, `pages/**`, `.github/workflows/**`, `README.md`, `COORDINATION.md` |

Original boards:
[`1dab34fa`](https://github.com/wingbangboozle1-lang/Tino2/blob/arena/1dab34fa-tino2/COORDINATION.md) ·
[`8c4d9e77`](https://github.com/wingbangboozle1-lang/Tino2/blob/arena/8c4d9e77-tino2/COORDINATION.md)

---

## 3. Claims by session `5a1bd5be` (this session)

File scope is chosen so that it overlaps **no** path claimed in section 2.

| # | Task | Status | Owner | File scope (exclusive to this session) |
|---|---|---|---|---|
| V0 | Repository and settings review; coordination-conflict report | in progress | `5a1bd5be` | `COORDINATION.md` (sections 1, 3–7 only) |
| V1 | Independent line-by-line verification of every figure against official sources (source register) | in progress | `5a1bd5be` | `dashboard/**`, `model/**` |
| V2 | Reproducible projection engine (one input file → every table), with tests | unclaimed → claimed by `5a1bd5be` | `5a1bd5be` | `model/**` |
| V3 | Step-by-step trust inheritance process (placeholders only) | unclaimed → claimed by `5a1bd5be` | `5a1bd5be` | `dashboard/**` |
| V4 | Privacy audit, broken-link check, build check (automated) | unclaimed → claimed by `5a1bd5be` | `5a1bd5be` | `model/**` |
| V5 | Verified dashboard pages (self-contained under one folder; own CSS; no shared assets) | unclaimed → claimed by `5a1bd5be` | `5a1bd5be` | `dashboard/**` |
| V6 | **Final integration** — merge whatever the other sessions have finished, re-verify the combined data line by line, root index/navigation, pull request, merge, confirm deploy | **conditional — see rule below** | `5a1bd5be` | root `index.html` and navigation **only at integration time** |

**Rule this session follows for V6.** Shared outputs (root `index.html`, navigation, shared table data) are
left untouched until one of these is true, checked again immediately before integration:

1. the other sessions' work is already merged to `main` — then this session merges `main` into its branch and
   integrates on top **without discarding anything of theirs**; or
2. another session's claim is more than 60 minutes old with no commits on its branch — then the takeover is
   logged in section 7 as a handoff; or
3. another session is still actively committing — then this session publishes only its own non-overlapping
   paths plus the minimum needed for a working landing page, and logs exactly what it touched.

Paths this session will **not** edit before integration: `index.html`, `assets/**`, `data/**`, `pages/**`,
`research/**`, `docs/**`, `FLAGGED-FOR-REVIEW.md`, `.github/workflows/**`, `README.md`.

---

## 4. Irregularities found in coordination (flagged for review)

| # | Irregularity | Evidence | Effect | Handling |
|---|---|---|---|---|
| C1 | **Three boards, none shared.** Each session wrote `COORDINATION.md` to its own branch; `main` has none. | `git ls-remote --heads origin`; `main` tree = `README.md` only | Sessions cannot see each other's claims; "never start a claimed task" cannot be enforced | This file records all three. It reaches `main` only through a pull request. |
| C2 | **Overlapping scopes.** `1dab34fa` and `8c4d9e77` both claim `index.html`, `assets/**`, `data/**`, `pages/**`, `COORDINATION.md`. | Section 2 | Guaranteed merge conflicts between those two branches | This session uses `dashboard/**` and `model/**` only. |
| C3 | **Status/owner contradiction** on the `1dab34fa` board: tasks 2–13 are marked `unclaimed` but list an owner, and the footer says the single session claims all tasks. | `1dab34fa` board | Ambiguous whether those tasks are free | Treated as **claimed**; this session does not edit those files. |
| C4 | **Branch naming** cannot follow `session-<id>/<task>`. | Environment restriction | None | Session ID taken from branch name. |
| C5 | **Duplicate research is unavoidable.** Line-by-line re-verification means going back to the official sources independently. | — | Some research is done more than once | Used as an independent second check; differences between sessions go to the Flagged for Review page. |
| C6 | **Repository is public** and Pages is already enabled from `main` root (legacy build). | `gh repo view` → `isPrivate: false`; `gh api repos/.../pages` | Everything committed is world-readable, including this board and all history | Nothing parcel-specific or personal is committed by this session. Owner should decide whether the repository should be private. |

---

## 5. Requests to change files owned by another session

None yet.

---

## 6. Sources, verification performed, irregularities (filled in as tasks finish)

Pending.

---

## 7. Log

- 2026-11-10 06:06 — `5a1bd5be` started. Repository at `61e6e58`: one file, `README.md`, 7 bytes (`# Tino2`). No `COORDINATION.md` on `main` or on this branch.
- 2026-11-10 06:08 — Listed remote branches; found two other session branches, each with its own board (see sections 1–2).
- 2026-11-10 06:11 — Wrote this unified board; claimed V0–V6 with a non-overlapping file scope. Committing and pushing the claim immediately.
