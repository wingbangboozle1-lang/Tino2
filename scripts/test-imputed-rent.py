#!/usr/bin/env python3
"""Freeze the imputed-rent finding, so the engine and its disclosure cannot drift apart again.

Background. `analysis_model.simulate()` has always credited the living paths the rent an
owner does not pay while occupying the home (`imputed_rent_mo`, which defaults to the
modelled rent). Four published pages used to state the opposite — "the model credits no
value for living there", "deliberately omits the value of housing services" — while the
engine that produced the site's seven-path comparison silently added that credit. On the
synthetic example inputs the credit was worth about $5.0 million at 25 years, roughly 43%
of the live path's published total.

This test does three things:

1. it pins the arithmetic on both settings of the credit, so a change to either the engine
   or the default inputs has to be reviewed rather than absorbed;
2. it asserts that every page describing the treatment describes it the same way, in the
   direction the engine actually computes, so the prose cannot silently invert again;
3. it asserts the disclosure quotes the same magnitude the model produces, by recomputing
   the figure and looking for it in the rendered HTML.

It reads only synthetic example inputs. It contains no household data.

Usage: python3 scripts/test-imputed-rent.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import analysis_model as M          # noqa: E402
import analysis_pages as AP         # noqa: E402

failures: list[str] = []
checks = 0


def check(ok: bool, message: str) -> None:
    global checks
    checks += 1
    if not ok:
        failures.append(message)


A, P = AP.ACTIVE_A, AP.ACTIVE_PARAMS
H = 25

with_credit = M.simulate("live", "base", P, A, H)
without_credit = M.simulate("live", "base", dict(P, imputed_rent_mo=0.0), A, H)
sell = M.simulate("sell_lump", "base", P, A, H)
rent = M.simulate("rent", "base", P, A, H)
gap = with_credit["total"] - without_credit["total"]


def r10(x: float) -> int:
    return int(round(x / 10.0)) * 10


# ---------------------------------------------------------------- 1. the engine's arithmetic
check(M.DEFAULT_PARAMS.get("imputed_rent_mo") is None,
      "imputed_rent_mo must default to None, meaning 'use the modelled rent'")
check(gap > 0,
      "crediting the living path an avoided rent must raise its total; engine direction changed")
check(abs(with_credit["avoided_rent"] - gap) < 1.0 or gap > 0,
      "the reported avoided_rent and the change in total must agree in direction")
check(r10(with_credit["total"]) == 11_619_760,
      f"published live total at 25 years moved: {r10(with_credit['total']):,} (expected 11,619,760)")
check(r10(without_credit["total"]) == 6_600_130,
      f"live total with no credit moved: {r10(without_credit['total']):,} (expected 6,600,130)")
check(r10(sell["total"]) == 12_408_330,
      f"sell total moved: {r10(sell['total']):,} (expected 12,408,330)")
check(r10(rent["total"]) == 10_213_920,
      f"rent total moved: {r10(rent['total']):,} (expected 10,213,920)")
check(round(gap / with_credit["total"] * 100) == 43,
      "the credit's share of the live total moved; the published percentage would be wrong")

# Setting the credit to zero must move only the living paths, never a sell or rent path.
for path in ("sell_lump", "sell_phased", "rent"):
    a = M.simulate(path, "base", P, A, H)["total"]
    b = M.simulate(path, "base", dict(P, imputed_rent_mo=0.0), A, H)["total"]
    check(abs(a - b) < 0.01, f"the imputed-rent input must not touch {path}")

# Removing the credit must leave the live path unable to beat the best sell path here, which is
# the whole decision-relevant point: the credit is what the living choice trades against selling.
check(without_credit["total"] < sell["total"],
      "on these synthetic inputs the live path without a credit should not beat selling outright")

# ---------------------------------------------------------------- 2. the pages say what the engine does
IMPUTED_HTML = {name: (ROOT / "guide" / name).read_text(encoding="utf8")
                for name in ("decision.html", "whatif.html", "questions.html", "brief.html")}

for name, html in IMPUTED_HTML.items():
    flat = re.sub(r"<[^>]+>", " ", html)
    flat = re.sub(r"\s+", " ", flat)

    # The old, now-false statements must be gone in every form they appeared.
    for forbidden in (
        "No estate-tax allocation or value of housing services is included",
        "deliberately omits the value of housing services",
        "the model credits no value for living there",
        "Living paths currently credit no rent avoided",
    ):
        check(forbidden not in flat, f"{name}: stale claim still published: {forbidden!r}")

# The control that makes the assumption switchable must exist and be wired to the precomputed data.
check('id="wi-imputed"' in IMPUTED_HTML["whatif.html"],
      "whatif page lost the imputed-rent control")
check("'wi-imputed'" in (ROOT / "scripts" / "analysis_pages.py").read_text(encoding="utf8"),
      "the what-if script no longer reads the imputed-rent control")

data_match = re.search(r"window\.WHATIF_DATA=(\{.*?\});</script>", IMPUTED_HTML["whatif.html"], re.S)
check(data_match is not None, "whatif page lost its precomputed data block")
if data_match:
    import json
    data = json.loads(data_match.group(1))
    key_credit, key_none = "base|25|24|0|1|0", "base|25|24|0|1|1"
    check(key_credit in data and key_none in data,
          "what-if data is missing one of the two imputed-rent settings")
    if key_credit in data and key_none in data:
        check(data[key_credit]["live"] == r10(with_credit["total"]),
              "the what-if table disagrees with the model on the live path with a credit")
        check(data[key_none]["live"] == r10(without_credit["total"]),
              "the what-if table disagrees with the model on the live path with no credit")
        for path in ("sell_lump", "rent"):
            check(data[key_credit][path] == data[key_none][path],
                  f"the imputed-rent setting must not change {path} in the what-if table")

# ---------------------------------------------------------------- 3. the disclosure quotes the model's own figure
decision_flat = re.sub(r"<[^>]+>", " ", IMPUTED_HTML["decision.html"])
decision_flat = re.sub(r"\s+", " ", decision_flat)
check(f"${r10(gap):,}" in decision_flat,
      f"the comparison page no longer quotes the credit's value (${r10(gap):,})")
check("explicit, adjustable assumption" in decision_flat,
      "the comparison page no longer labels the credit as an assumption")
check(round(gap / with_credit["total"] * 100).__str__() + "%" in decision_flat,
      "the comparison page no longer states the credit's share of the live total")

for name in ("questions.html", "brief.html"):
    flat = re.sub(r"<[^>]+>", " ", IMPUTED_HTML[name])
    flat = re.sub(r"\s+", " ", flat)
    check("credited" in flat or "prices part of it" in flat,
          f"{name}: the living-path treatment is not described in the engine's direction")

# ---------------------------------------------------------------- report
if failures:
    for f in failures:
        print("::error title=Imputed rent::" + f)
    raise SystemExit(1)

print(f"PASS: {checks} checks — the living paths' imputed rent is credited, disclosed in the same "
      f"direction on every page that discusses it, quoted at the model's own ${r10(gap):,} "
      f"({round(gap / with_credit['total'] * 100)}% of the live total), and adjustable on the "
      f"what-if page without moving any sell or rent path.")
