# Privacy remediation runbook — repository history and access

**Internal document. It is not published to the site** (`_config.yml` excludes `docs/`).
Written 16 Nov 2026 by session `e3f08d9e` for the repository **administrator/owner**. It answers
the standing owner item "scrub pre-rounding Git history / keep the repo privacy-first"
(board rows L-D2 and P-4), which a session branch cannot complete: no session rewrites shared
refs, and no session changes repository visibility.

Nothing in this file is a personal identifier or a household amount. It describes what to run and
what to expect.

---

## 1. Where the exposure actually is

Three separate layers, each with a different control. Conflating them is how a "we rounded the
numbers" decision got made earlier in this project's history.

| Layer | What it contains | What controls it | Status as this session reads it |
| --- | --- | --- | --- |
| Published Pages site | `index.html`, `guide/**`, `assets/safe.*` — synthetic examples only | `scripts/public_manifest.py`, `scripts/package-site.py`, `scripts/check-publication.py` | Clean: the packaged set is 32 files, the gate rejects anything extra, and `scripts/privacy-audit.cjs` scans the packaged source **and** the rendered text |
| Repository at HEAD (all other tracked files) | the retained analysis tree: `docs/`, `research/`, `pages/`, `dashboard/`, `site/`, `qa/`, `src/`, `integration/`, `verification/`, root `*.html` | repository **visibility**, or deleting that tree from the default branch | Identifiers masked and household-scale amounts rounded to $10 by the 15 Nov 2026 scrub, and `scripts/privacy-gate.py` fails a build that re-introduces either. Prose in those files still narrates one household's situation, and a public repository is indexed by GitHub code search at HEAD |
| Git history, other refs, PR refs, caches, forks, clones | every earlier commit, including pre-rounding figures | history rewrite + GitHub Support + coordination with anyone holding a copy | **Open.** Rounding in a later commit does not change an earlier one. This is the item this runbook is for |

## 2. Measure before you act

From a **full** clone (a shallow clone cannot answer the question — it has nothing to look at):

```sh
git clone https://github.com/<owner>/<repo>.git        # not --depth; a mirror clone is better
cd <repo>
python3 scripts/privacy-history-audit.py               # counts + flagged paths, never matched text
python3 scripts/privacy-history-audit.py --json         # for a ticket
python3 scripts/privacy-history-audit.py --self-test     # proves the detectors fire
python3 scripts/privacy-history-audit.py --strict         # exits 1 on any finding, for a hard gate
```

The audit reuses `scripts/privacy-gate.py`, so it enforces exactly the working-tree policy:
blocked-identifier hashes (from `scripts/privacy-blocklist.json`, hashes only), the $10 rounding
rule inside the analysis scope, and the contact/parcel/address patterns. It prints each flagged
**path** and **blob id** and how many times each rule fired — never a match, so its own output is
safe to paste into an issue or a commit message. Say `git clone --mirror` instead of a normal clone
to include every ref:

```sh
git clone --mirror https://github.com/<owner>/<repo>.git
```

Expected result today: a non-empty list, because the pre-rounding figures are in history. Zero
findings in a shallow clone means "not inspected", not "clean" — the tool says so.

Proof the instrument is not vacuous (run 16 Nov 2026, in a throwaway three-commit repository):
`docs/bad.md` carrying a registered identifier and an un-rounded amount (1,234 dollars, not a
multiple of $10) was committed, then amended
twice. The audit reported `flagged blobs: 4`, `findings by rule: BLOCKED-IDENTIFIER×4, ROUNDING×2`,
named `docs/bad.md` with two blob ids, printed no matched text, exited 0 by default and 1 under
`--strict`. The clean sibling file was not flagged. So a blob that stops being reachable from HEAD
but stays reachable from a branch is still seen, which is exactly the failure mode the working-tree
gate cannot cover.

The same script now runs in `.github/workflows/pages.yml`: the verify job runs `--self-test` (a
blocking proof that the audit and the gate share one policy), and a separate **non-blocking**
`history-audit` job fetches the full history of every ref Actions checks out (`fetch-depth: 0`, which is all
branches and tags on the default remote, and still not `refs/pull/*`) and writes its report into the **run
summary** as well as the log — counts, rule names, paths and blob ids, no matched text — with `--json` alongside
for a ticket. CI measures; it does not block a merge on a history finding, because the remediation itself is the
owner's decision (Suggestions S16 and S25). Both jobs were green on the run that introduced them (16 Nov 2026).

## 3. Options, with the consequence that is usually discovered afterwards

Official sources for every claim in this table are listed under Sources. Read them before choosing;
they are short.

| Option | What it achieves | What it does **not** achieve | GitHub's own warnings |
| --- | --- | --- | --- |
| **A. Make the repository private** | Access is restricted to people you invite; the retained analysis tree stops being reachable by anonymous readers and code search | It does not delete anything, and it **unpublishes the Pages site** on GitHub Free for personal accounts and organizations — the public guide goes offline. Public forks are **detached** into a new network and are **not** made private | "Any published GitHub Pages site will be automatically unpublished"; remove or update a custom domain's DNS records **before** the change, to avoid a domain-takeover risk; "GitHub will detach public forks … Public forks are not made private" |
| **B. Keep the site, delete the retained analysis tree from the default branch** | The searchable, human-readable tree at HEAD is gone; the site keeps running | History, other branches, PR refs, forks, caches and clones are untouched, so a determined reader with a link can still reach old commits — which is why **C** is the only real closure of the history question | The visibility page applies; nothing in GitHub's Pages or repository settings deletes history on your behalf |
| **C. Rewrite history with `git-filter-repo`, then ask GitHub Support** | Makes the sensitive commits unreachable from every branch and tag you push, and (via Support) removes cached views and pull-request references | It cannot touch other users' clones or forks. Force-pushing discards work anyone else built on the old history, and ~70 session branches exist on this repository | Rewriting is "irreversible" once you move past the check step; the push "will fail to push any refs starting with `refs/pull/`, since GitHub marks those as read-only"; Support "won't remove non-sensitive data, and will only assist … where the risk can't be mitigated by rotating" credentials; Support may offer "dereferencing", which preserves PR bodies and comments — so anything quoted **in** a comment stays |
| **D. Do nothing beyond the current gates** | The published artifact stays clean, and the gates keep it that way | The retained tree at HEAD and the history stay public | — |

The owner has to pick A/B/C. A reasonable sequence, if the exposure is judged real:
**A now** (one setting, reversible), then **C** on a mirror clone, then **B** as part of the same
rewrite, then re-open Pages from a fresh clean repository. Site continuity is the price of A on the
Free plan; the guide's content is generated from the repository, so it can be republished anywhere.

## 4. The procedure, as GitHub documents it (option C)

Do this on a quiet machine, with a code freeze, and with branch protection that would block force
pushes temporarily adjusted by an owner who accepts that.

1. Install `git-filter-repo`. GitHub's page requires a version with the `--sensitive-data-removal`
   flag, i.e. **at least 2.47** (`brew install git-filter-repo`, or the manual install in the
   tool's `INSTALL.md`).
2. `git clone --mirror https://github.com/<owner>/<repo>.git` and `cd` into it. A mirror, because a
   rewrite must cover every ref, and because `git-filter-repo` refuses to run in a repository with a
   configured remote in the normal layout (it removes the remote deliberately).
3. Run the removal per path, or better, rewrite the content with `--replace-text` if only certain
   strings must go:
   ```sh
   git-filter-repo --sensitive-data-removal --invert-paths --path docs/
   git-filter-repo --sensitive-data-removal --replace-text paths-to-strings.txt   # literal strings
   ```
   Use the **path**, not just the filename, as GitHub's page stresses. Note which files GitHub code
   search has actually indexed before deciding scope; `scripts/privacy-history-audit.py --json` gives
   the candidate list.
4. Check the blast radius GitHub tells you to check:
   ```sh
   grep '^refs/pull/.*/head$' .git/filter-repo/changed-refs
   ```
   Record the PR numbers and the `NOTE: First Changed Commit(s)` line from the tool's output —
   Support asks for both.
5. Push, then handle tags and releases: `git push --force --mirror origin`. The `refs/pull/*`
   failures are expected and are the reason step 6 exists.
6. Contact GitHub Support through the support portal with the owner/repo name, the affected pull
   request numbers, and the first changed commit(s). Ask for cached views and PR references to be
   removed.
7. Tell every collaborator and every automated session to **rebase, not merge**, onto the new
   history, or to re-clone. One merge commit can reintroduce the old objects — the reason this
   project's board forbids sessions from force-pushing at all.

Before any of it: rotate anything that looks like a credential. History rewriting is not a
credential-revocation tool, and Support says so.

## 5. What must be re-verified afterwards

* `python3 scripts/privacy-gate.py` and `python3 scripts/privacy-history-audit.py --strict` on the
  rewritten repository.
* The published boundary again: `python3 scripts/package-site.py && python3 scripts/check-publication.py --self-test`.
* That `scripts/privacy-blocklist.json` still matches `private/privacy-identifiers.txt` — the
  mapping lives **outside** git (`.gitignore`), and after a rewrite it is the only place the masked
  strings exist. Keep a copy off-GitHub before starting.
* That the ~70 open session branches and any forks you care about were either deleted or rewritten;
  a rewrite of `main` alone does not remove a branch that was pushed earlier.

## Sources (all read 16 Nov 2026)

* GitHub, *Removing sensitive data from a repository* — four-step framing (rewrite locally with
  git-filter-repo; force-push; coordinate other clones; prevent repeats), the `--sensitive-data-removal`
/ `--invert-paths` / `--path` form, the `changed-refs` check, the read-only `refs/pull/*` push
  failure, the Support request contents, dereferencing, and the "still accessible in clones, forks,
  cached views and pull requests" warning:
  <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository>
* GitHub, *Setting repository visibility* — Pages auto-unpublishing on GitHub Free, the custom-domain
  DNS warning, and public forks being detached and staying public:
  <https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/managing-repository-settings/setting-repository-visibility>
* `newren/git-filter-repo` — the tool GitHub's procedure names, its `--sensitive-data-removal` flag
  and `--invert-paths` / `--replace-text` options: <https://github.com/newren/git-filter-repo>
* This repository — the working-tree policy the audit reuses: `scripts/privacy-gate.py`,
  `scripts/privacy-scrub.py`, `scripts/privacy-audit.cjs`, `scripts/public_manifest.py`,
  `scripts/privacy-blocklist.json`; the exclusion list that keeps the analysis tree off Pages,
  `_config.yml`; and the board's standing rows L-D2 and P-4 in `COORDINATION.md`.
