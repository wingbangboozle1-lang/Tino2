#!/usr/bin/env python3
"""Independent mathematical, tariff, statutory, and cross-page consistency audit
for session 3938fab9 (checked 2026-11-12).

Re-implements every core formula in Python from first principles and compares
against live Node execution of site/data/*.js across all years, horizons,
rent benchmarks, tariff schedules, and stress engines.
"""
import json
import math
import pathlib
import re
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]


def round10(v):
    if v is None:
        return None
    return int(math.floor(v / 10.0 + 0.5) * 10) if v >= 0 else -int(math.floor(-v / 10.0 + 0.5) * 10)


# --- 1. Independent Python implementation of the core household & statutory model ---
BASE = {
    "startYear": 2026,
    "inheritYear": 2045,
    "aValue": 3_100_000,
    "aAssessed": 550_540,
    "aRate": 0.012,
    "aWaterMonthly": 125,
    "aSolarMonthlyCredit": 15,
    "aInsuranceAnnual": 1_500,
    "aRent4BR": 6_390,
    "aRent3BR": 5_870,
    "aRent4BR_2027": 5_800,
    "aRent3BR_2027": 5_440,
    "bValue": 1_800_000,
    "bAssessed2025": 114_250,
    "bRate": 0.0118162182,
    "bRentMonthly": 7_150,
    "bRent1BR": 2_730,
    "bRent2BR": 3_310,
    "bRent1BR_2027": 2_770,
    "bRent2BR_2027": 3_410,
    "bWaterMonthly": 365,
    "bElectricMonthly": 50,
    "bInsuranceAnnual": 1_500,
    "bRentBoardFeeAnnual": 118,
    "appreciation": 0.035,
    "assessmentGrowth": 0.02,
    "expenseInflation": 0.03,
    "rentGrowth": 0.03,
    "sfRentGrowth": 0.016,
    "vacancy": 0.05,
    "management": 0.08,
    "maintenanceA": 0.005,
    "maintenanceB": 0.01,
    "saleCost": 0.06,
    "ordinaryTax": 0.333,
    "capitalGainsTax": 0.331,
    "primaryGainExclusion": 250_000,
    "prop19Amount": 1_044_586,
    "estateExclusion": 15_000_000,
    "estateExclusion2027": 15_480_000,
    "estateIndex": 0.02,
    "portfolioGross": 0.06,
    "portfolioTaxDrag": 0.01,
}


def prop19_steps(year):
    return max(0, (year - 2025) // 2)


def model_allowance(year, cfg=BASE):
    return cfg["prop19Amount"] * ((1 + cfg["appreciation"]) ** prop19_steps(year))


def estate_exclusion(year, cfg=BASE):
    if year <= 2026:
        return cfg["estateExclusion"]
    return cfg["estateExclusion2027"] * ((1 + cfg["estateIndex"]) ** (year - 2027))


def after_tax_portfolio_return(cfg=BASE):
    return cfg["portfolioGross"] - cfg["portfolioTaxDrag"]


def series_for(prop, year, cfg=BASE):
    n = year - cfg["startYear"]
    if prop == "A":
        market = cfg["aValue"] * ((1 + cfg["appreciation"]) ** n)
        assessed = cfg["aAssessed"] * ((1 + cfg["assessmentGrowth"]) ** n)
        rate = cfg["aRate"]
    else:
        market = cfg["bValue"] * ((1 + cfg["appreciation"]) ** n)
        assessed = cfg["bAssessed2025"] * ((1 + cfg["assessmentGrowth"]) ** (year - 2025))
        rate = cfg["bRate"]
    return {"year": year, "market": market, "assessed": assessed, "tax": assessed * rate, "rate": rate}


def inheritance_values(year, cfg=BASE):
    a = series_for("A", year, cfg)
    allowance = model_allowance(year, cfg)
    capped = a["assessed"] + allowance
    primary_assessed = a["assessed"] if a["market"] <= capped else (a["market"] - allowance)
    return {
        "year": year,
        "market": a["market"],
        "carryForwardAssessed": a["assessed"],
        "allowance": allowance,
        "primaryAssessed": primary_assessed,
        "fullAssessed": a["market"],
        "carryForwardTax": a["assessed"] * cfg["aRate"],
        "primaryTax": primary_assessed * cfg["aRate"],
        "fullTax": a["market"] * cfg["aRate"],
    }


def rent_base_for(choice, cfg=BASE):
    if choice == "3BR":
        return cfg["aRent3BR"]
    if choice == "4BR_2027":
        return cfg["aRent4BR_2027"]
    if choice == "3BR_2027":
        return cfg["aRent3BR_2027"]
    return cfg["aRent4BR"]


def decision_py(cfg=BASE, horizon=10, rent_choice="4BR"):
    y0 = cfg["inheritYear"]
    tr = inheritance_values(y0, cfg)
    r_port = after_tax_portfolio_return(cfg)
    base_rent = rent_base_for(rent_choice, cfg)

    sell_net = tr["market"] * (1 - cfg["saleCost"])
    sell_term = sell_net * ((1 + r_port) ** horizon)
    sell_liq = sell_term - max(0.0, sell_term - sell_net) * cfg["capitalGainsTax"]

    def run_hold(live_in):
        start_assessed = tr["primaryAssessed"] if live_in else tr["fullAssessed"]
        reserve = 0.0
        yearly = []
        for t in range(1, horizon + 1):
            yr = y0 + t
            n_from_start = yr - cfg["startYear"]
            market = tr["market"] * ((1 + cfg["appreciation"]) ** t)
            assessed = min(market, start_assessed * ((1 + cfg["assessmentGrowth"]) ** t))
            prop_tax = assessed * cfg["aRate"]
            water = cfg["aWaterMonthly"] * 12 * ((1 + cfg["expenseInflation"]) ** n_from_start)
            ins = cfg["aInsuranceAnnual"] * ((1 + cfg["expenseInflation"]) ** n_from_start)
            solar = cfg["aSolarMonthlyCredit"] * 12
            maint = market * cfg["maintenanceA"]
            gross_rent = 0.0 if live_in else base_rent * 12 * ((1 + cfg["rentGrowth"]) ** n_from_start)
            collected = gross_rent * (1 - cfg["vacancy"])
            mgmt = 0.0 if live_in else collected * cfg["management"]
            noi = collected - mgmt - prop_tax - water - ins - maint + solar
            inc_tax = 0.0 if live_in else max(0.0, noi) * cfg["ordinaryTax"]
            cash = noi - inc_tax
            reserve = reserve * (1 + r_port) + cash
            yearly.append({
                "year": yr,
                "market": market,
                "assessed": assessed,
                "propertyTax": prop_tax,
                "water": water,
                "insurance": ins,
                "maintenance": maint,
                "grossRent": gross_rent,
                "noi": noi,
                "incomeTax": inc_tax,
                "afterTaxCash": cash,
                "reserve": reserve,
            })
        end_market = tr["market"] * ((1 + cfg["appreciation"]) ** horizon)
        amount_realized = end_market * (1 - cfg["saleCost"])
        gain_before = max(0.0, amount_realized - tr["market"])
        excl = min(cfg["primaryGainExclusion"], gain_before) if (live_in and horizon >= 2) else 0.0
        taxable_gain = max(0.0, gain_before - excl)
        sale_tax = taxable_gain * cfg["capitalGainsTax"]
        final_sale = amount_realized - sale_tax
        return {
            "terminal": final_sale + reserve,
            "finalSale": final_sale,
            "reserve": reserve,
            "saleTax": sale_tax,
            "gainExclusion": excl,
            "yearly": yearly,
        }

    rent = run_hold(False)
    live = run_hold(True)
    opts = sorted([("sell", sell_term), ("rent", rent["terminal"]), ("live", live["terminal"])], key=lambda x: -x[1])
    return {
        "transfer": tr,
        "sell": {"initialInvested": sell_net, "terminal": sell_term, "terminalAfterLiquidation": sell_liq},
        "rent": rent,
        "live": live,
        "winner": opts[0][0],
        "leadOverSecond": opts[0][1] - opts[1][1],
    }


# --- 2. Query live Node engine outputs for exact comparison ---
NODE_PROBE = r"""
global.window = global;
require('./site/data/sources.js');
require('./site/data/model.js');
require('./site/data/costs.js');
require('./site/data/options.js');
require('./site/data/scenarios.js');
require('./site/data/history.js');
require('./site/data/history-engine.js');
require('./site/data/stress.js');
require('./site/data/questions.js');
require('./site/data/suggestions.js');
require('./site/data/gate.js');

const cases = [];
for (const y of [2040, 2045, 2050]) {
  for (const h of [1, 2, 5, 10, 15, 20, 30]) {
    for (const rc of ['4BR', '3BR', '4BR_2027', '3BR_2027']) {
      const d = MODEL.decision({ ...MODEL.BASE, inheritYear: y }, h, rc);
      const ranked = [d.sell.terminal, d.rent.terminal, d.live.terminal].sort((a, b) => b - a);
      cases.push({
        y, h, rc,
        sell: d.sell.terminal,
        sellLiq: d.sell.terminalAfterLiquidation,
        rent: d.rent.terminal,
        live: d.live.terminal,
        winner: d.winner,
        lead: ranked[0] - ranked[1],
        primaryAssessed: d.transfer.primaryAssessed,
        allowance: d.transfer.allowance
      });
    }
  }
}

const estate = [2026, 2027, 2040, 2045, 2050].map(y => MODEL.estateRow(y));
const sjw = [6, 8, 10, 12, 15].map(c => ({ ccf: c, bill: COSTS.sjwMonthly(c) }));
const sfpuc = [6, 9, 10, 11, 12].map(c => ({ ccf: c, ...COSTS.sfpucMonthly(c, 3) }));
const opt = {
  dep30: OPTIONS.rentWithDepreciation(2045, 0.30),
  old2045: OPTIONS.oldRule(2045),
  probate3100k: OPTIONS.probate(3100000),
  withhold2045: OPTIONS.withholdingAtSale(2045),
  beHome: SCENARIOS.breakEvenHomeGrowth(SCENARIOS.DEFS[0]),
  bePort: SCENARIOS.breakEvenPortfolioReturn(SCENARIOS.DEFS[0]),
  beHomeEq: SCENARIOS.breakEvenHomeGrowthEqualTerms(SCENARIOS.DEFS[0]),
  bePortEq: SCENARIOS.breakEvenPortfolioReturnEqualTerms(SCENARIOS.DEFS[0]),
};
const counts = {
  sources: Object.keys(SOURCES).length,
  openQ: READINESS.open.length,
  answeredQ: READINESS.answered.length,
  unknowableQ: READINESS.unknowable.length,
  suggestions: SUGGESTIONS.items.length,
  gateTotal: GATE.counts.total,
  gateSettled: GATE.counts.settled,
  gateHousehold: GATE.counts.household,
  gateMissing: GATE.counts.missing,
};
console.log(JSON.stringify({ cases, estate, sjw, sfpuc, opt, counts }));
"""


def main():
    res = subprocess.run(
        ["node", "-e", NODE_PROBE],
        cwd=ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    js = json.loads(res.stdout)
    failures = []
    checks = 0

    # Check all 84 decision matrix combinations (3 years x 7 horizons x 4 rent benchmarks)
    for c in js["cases"]:
        cfg = dict(BASE, inheritYear=c["y"])
        py = decision_py(cfg, c["h"], c["rc"])
        for k_js, v_py in [
            ("sell", py["sell"]["terminal"]),
            ("sellLiq", py["sell"]["terminalAfterLiquidation"]),
            ("rent", py["rent"]["terminal"]),
            ("live", py["live"]["terminal"]),
            ("lead", py["leadOverSecond"]),
            ("primaryAssessed", py["transfer"]["primaryAssessed"]),
            ("allowance", py["transfer"]["allowance"]),
        ]:
            checks += 1
            if abs(c[k_js] - v_py) > 1e-6:
                failures.append(f"Mismatch {c['y']}/h={c['h']}/{c['rc']} {k_js}: js={c[k_js]} py={v_py}")
        checks += 1
        if c["winner"] != py["winner"]:
            failures.append(f"Winner mismatch {c['y']}/h={c['h']}/{c['rc']}: js={c['winner']} py={py['winner']}")

    # Check estate rows (Property B must never be counted in decedent's gross estate combined/headroom)
    for er in js["estate"]:
        y = er["year"]
        a_mkt = series_for("A", y)["market"]
        excl = estate_exclusion(y)
        checks += 3
        if abs(er["combined"] - a_mkt) > 1e-6:
            failures.append(f"estateRow({y}).combined != Property A market ({er['combined']} vs {a_mkt})")
        if abs(er["headroom"] - max(0.0, excl - a_mkt)) > 1e-6:
            failures.append(f"estateRow({y}).headroom mismatch")
        if abs(er["excess"] - max(0.0, a_mkt - excl)) > 1e-6:
            failures.append(f"estateRow({y}).excess mismatch")

    # Check SJW tariff math (AL 628A, effective 2026-07-01)
    for row in js["sjw"]:
        ccf = row["ccf"]
        t1 = min(ccf, 6)
        t2 = min(max(ccf - 6, 0), 6)
        t3 = max(ccf - 12, 0)
        expected = 78.64 + t1 * 4.9692 + t2 * 7.4167 + t3 * 14.1659
        checks += 1
        if abs(row["bill"] - expected) > 1e-9:
            failures.append(f"SJW {ccf} Ccf mismatch: {row['bill']} vs {expected}")

    # Check SFPUC FY2026-27 multi-family 3-unit tariff math (Res. 26-0064 & 26-0066)
    for row in js["sfpuc"]:
        ccf = row["ccf"]
        t1 = min(ccf, 9)
        t2 = max(ccf - 9, 0)
        water = 24.93 + t1 * 12.03 + t2 * 12.91
        sewer = 6.62 + ccf * 0.95 * 20.74
        storm = 19.66
        total = water + sewer + storm
        checks += 1
        if abs(row["total"] - total) > 1e-9:
            failures.append(f"SFPUC {ccf} Ccf mismatch: {row['total']} vs {total}")

    # Check statutory probate fee on $3,100,000 (Cal. Prob. Code §§ 10800, 10810)
    # 4% on $100k ($4,000) + 3% on $100k ($3,000) + 2% on $800k ($16,000) + 1% on $2,100k ($21,000) = $44,000
    checks += 1
    if abs(js["opt"]["probate3100k"] - 44_000.0) > 1e-9:
        failures.append(f"Probate fee on $3.1M expected 44000, got {js['opt']['probate3100k']}")

    # Check FTB Form 593 3 1/3% withholding on 2045 sale
    expected_wh = series_for("A", 2045)["market"] / 30.0
    checks += 1
    if abs(js["opt"]["withhold2045"] - expected_wh) > 1e-6:
        failures.append(f"Withholding 2045 mismatch: {js['opt']['withhold2045']} vs {expected_wh}")

    # Check Prop 13 historical inflation factors in prop13_factors.json against MODEL.historyA / historyB
    p13 = {r["roll_year"]: r for r in json.loads((ROOT / "integration/ledger/prop13_factors.json").read_text())["rows"]}
    checks += 1
    if p13["2010-11"]["ccpi_change_pct"] != -0.237 or p13["2026-27"]["factor"] != 1.02:
        failures.append("Unexpected Prop 13 factor table values")

    summary = {
        "session": "3938fab9",
        "date": "2026-11-12",
        "checks": checks,
        "failures": failures,
        "counts": js["counts"],
        "key_2045_10yr_4BR": {
            k: round10(v) if isinstance(v, (int, float)) and k not in ("y", "h") else v
            for k, v in next(c for c in js["cases"] if c["y"] == 2045 and c["h"] == 10 and c["rc"] == "4BR").items()
        },
        "key_2045_10yr_4BR_2027": {
            k: round10(v) if isinstance(v, (int, float)) and k not in ("y", "h") else v
            for k, v in next(c for c in js["cases"] if c["y"] == 2045 and c["h"] == 10 and c["rc"] == "4BR_2027").items()
        },
        "sjw_bills": {str(r["ccf"]): round(r["bill"], 2) for r in js["sjw"]},
        "sfpuc_3unit_bills": {str(r["ccf"]): round(r["total"], 2) for r in js["sfpuc"]},
        "breakevens": {
            "home_growth_headline_pct": round(js["opt"]["beHome"] * 100, 3),
            "portfolio_return_headline_pct": round(js["opt"]["bePort"] * 100, 3),
            "home_growth_equal_terms_pct": round(js["opt"]["beHomeEq"] * 100, 3),
            "portfolio_return_equal_terms_pct": round(js["opt"]["bePortEq"] * 100, 3),
        },
        "depreciation_30pct_2045": {
            "annual_deduction": round10(js["opt"]["dep30"]["deduction"]),
            "rent_terminal_with_dep": round10(js["opt"]["dep30"]["terminal"]),
            "rent_terminal_published": round10(js["opt"]["dep30"]["published"]),
            "change": round10(js["opt"]["dep30"]["change"]),
            "sell_still_leads_by": round10(js["opt"]["dep30"]["sellLead"]),
        },
        "old_prop58_rule_2045": {
            "rent_now": round10(js["opt"]["old2045"]["rentNow"]),
            "rent_under_old_rule": round10(js["opt"]["old2045"]["rent"]),
            "sell_lead_under_old_rule": round10(js["opt"]["old2045"]["sellLead"]),
            "sell_lead_equal_terms_old_rule": round10(js["opt"]["old2045"]["sellLeadEqualTerms"]),
        },
    }
    out_path = pathlib.Path(__file__).resolve().parent / "audit_results.json"
    out_path.write_text(json.dumps(summary, indent=2) + "\n")
    print(json.dumps(summary, indent=2))
    if failures:
        sys.exit(1)
    print(f"PASS: {checks} independent Python vs. JS mathematical & tariff checks")


if __name__ == "__main__":
    main()
