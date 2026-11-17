#!/usr/bin/env python3
"""The two calculators on this site must answer the same question the same way.

Why this test exists
--------------------
The site publishes two calculators: the monthly Python engine that produces the static
tables, and the annual JavaScript engine in ``guide/data/`` that drives the interactive
controls. For a while they disagreed about the same question on the same page, and a peer
review found the worst version of it: the JavaScript engine credited the living path with
**no** housing value, so the two engines picked **opposite** leading paths at the 10-year
horizon and the JavaScript living path even produced a negative terminal wealth at 50
years — impossible for someone who still owns a house.

Two conventions now bind them together:

  1. the living path is credited the rent an owner avoids by occupying the home, at the
     same growth rate as the rent it replaces, and that credit is not taxed; and
  2. a path that still holds the house at the endpoint is worth the house at its market
     value plus the cash it accumulated — no hypothetical sale, and therefore no gain tax
     charged on a sale that is not modelled.

This test pins both conventions and the agreement they are supposed to produce, so the
site cannot quietly start contradicting itself again. It is synthetic throughout: no
household value, no identifier, and no forecast.
"""
import json
import math
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))

import analysis_model as AM          # noqa: E402
import analysis_pages as AP           # noqa: E402

HORIZONS = (10, 20, 25, 30, 50)
JS_SCRIPT = r'''
global.window=global;
require('./guide/data/model.js');
const base=MODEL.BASE, out={base,rows:[]};
for (const horizon of %s) {
  const c={...base,inheritYear:2045};
  const d=MODEL.decision(c,horizon);
  out.rows.push({horizon,winner:d.winner,sell:d.sell.terminal,rent:d.rent.terminal,live:d.live.terminal});
  const z=MODEL.decision({...c,imputedRentMonthly:0},horizon);
  out.rows[out.rows.length-1].zeroLive=z.live.terminal; out.rows[out.rows.length-1].zeroWinner=z.winner;
}
console.log(JSON.stringify(out));
''' % str(list(HORIZONS)).replace("'", '"')


def main():
    checks = 0
    failures = []

    def require(condition, message):
        nonlocal checks
        checks += 1
        if not condition:
            failures.append(message)

    js = json.loads(subprocess.check_output(['node', '-e', JS_SCRIPT], cwd=ROOT, text=True))
    base = js['base']
    params = dict(AP.ACTIVE_PARAMS)
    prop = AP.ACTIVE_A

    # 1. The two engines run the same scenario. If this fails, the agreement checks below
    #    would be meaningless, so it is checked first and separately.
    require(abs(base['appreciation'] - params['g_post']) < 0.002,
            f"home-price growth differs: JS {base['appreciation']} vs engine {params['g_post']}")
    require(abs(base['portfolioNet'] - params['mu_equity']) < 0.002,
            f"portfolio return differs: JS {base['portfolioNet']} vs engine {params['mu_equity']}")
    require(abs(base['vacancy'] - params['vacancy']) < 1e-9,
            f"vacancy differs: JS {base['vacancy']} vs engine {params['vacancy']}")
    require(abs(base['saleCost'] - params['sale_cost']) < 1e-9,
            f"sale cost differs: JS {base['saleCost']} vs engine {params['sale_cost']}")
    require(abs(base['expenseInflation'] - params['cpi']) < 0.002,
            f"inflation differs: JS {base['expenseInflation']} vs engine {params['cpi']}")

    for row in js['rows']:
        horizon = row['horizon']
        engine = {path: AM.simulate(path, 'base', params, prop, horizon)['total']
                  for path in ('sell_lump', 'rent', 'live')}
        engine_winner = max(engine, key=engine.get)
        js_winner = {'sell': 'sell_lump', 'rent': 'rent', 'live': 'live'}[row['winner']]

        # 2. The leading path is the same in both engines, at every published horizon.
        require(engine_winner == js_winner,
                f"{horizon}-year horizon: the engines disagree on the leading path "
                f"(browser says {row['winner']}, published tables say {engine_winner})")

        # 3. The sell path is a straight compounding of the same starting value, so the two
        #    engines must agree on it closely. This is the strongest available check that
        #    the two are running the same scenario.
        require(abs(row['sell'] - engine['sell_lump']) / engine['sell_lump'] < 0.005,
                f"{horizon}-year horizon: the sell path differs by more than 0.5% "
                f"({row['sell']:.0f} vs {engine['sell_lump']:.0f})")

        # 4. The holding paths are worth the house at market plus accumulated cash in both
        #    engines. They agree closely, but not exactly: one compounds monthly and the
        #    other annually, and their inflation timings differ.
        for path, key in (('live', 'live'), ('rent', 'rent')):
            require(abs(row[key] - engine[path]) / engine[path] < 0.06,
                    f"{horizon}-year horizon: the {path} path differs by more than 6% "
                    f"({row[key]:.0f} vs {engine[path]:.0f})")

        # 5. A path still holding a house cannot have negative wealth.
        require(row['live'] > 0, f"{horizon}-year horizon: the living path is negative "
                                  f"({row['live']:.0f}) — a household that still owns the house "
                                  "cannot end up with negative wealth")

        # 6. Removing the imputed rent must move both engines the same way: at the short
        #    horizon it is what decides the ranking, so with no credit a selling path must
        #    lead in both calculators.
        zero = dict(params)
        zero['imputed_rent_mo'] = 0.0
        engine_zero = AM.simulate('live', 'base', zero, prop, horizon)['total']
        require(row['zeroLive'] < row['live'],
                f"{horizon}-year horizon: removing the imputed rent did not reduce the "
                "browser living path")
        require(engine_zero < engine['live'],
                f"{horizon}-year horizon: removing the imputed rent did not reduce the "
                "published living path")
        if horizon == 10:
            require(row['zeroWinner'] == 'sell',
                    "10-year horizon: with no imputed rent the browser calculator should "
                    f"pick a selling path, not {row['zeroWinner']}")
            engine_zero_winner = max(
                {'sell_lump': AM.simulate('sell_lump', 'base', zero, prop, horizon)['total'],
                 'live': engine_zero}, key=lambda k: {'sell_lump': AM.simulate(
                     'sell_lump', 'base', zero, prop, horizon)['total'],
                     'live': engine_zero}[k])
            require(engine_zero_winner == 'sell_lump',
                    "10-year horizon: with no imputed rent the published tables should pick "
                    f"a selling path, not {engine_zero_winner}")

    if failures:
        for line in failures:
            print('FAIL:', line)
        return 1
    print(f'PASS: the browser calculator and the published monthly engine run the same '
          f'scenario, pick the same leading path at all {len(HORIZONS)} horizons, agree on '
          f'the sell path within 0.5%, and move together when the imputed rent is removed; '
          f'{checks} checks.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
