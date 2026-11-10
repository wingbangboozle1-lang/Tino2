/*
 * Page content: Summary, Decision, Projections — session 5a1bd5be.
 * Reference pages are in pages_ref.js. All dollar figures here go through Fmt.usd (nearest $10).
 */
'use strict';

exports.build = function (c) {
  const { E, I, S, FL, Fmt, L, p0, sim, field, base, B, series, grid } = c;
  const usd = Fmt.usd, pct = Fmt.pct;
  const T = p0.inheritYear, H = p0.horizon, END = T + H;
  const SC = I.SCENARIOS;
  const NAME = { SELL: 'Sell and invest', LIVE: 'Live in it', RENT: 'Rent it out' };
  const houseLabel = k => `${SC.house[k].label} (${pct(SC.house[k].aGrowth, 2)} a year)`;
  const retLabel = k => `${SC.returns[k].label} (${pct(SC.returns[k].investReturn, 2)} a year)`;
  const real = c.real;

  const liveY1 = base.live.years[0], rentY1 = base.rent.years[0];
  const p19Saving = rentY1.propertyTax - liveY1.propertyTax;
  const sellBest = grid.filter(g => g.best === 'SELL').length;
  const notSell = grid.filter(g => g.best !== 'SELL');
  const liveCostYear = base.costOfLivingPerYear;
  const count = st => I.FIELDS.filter(f => f.status === st).length;
  const high = FL.FLAGS.filter(f => f.level === 'high').length;
  const ownerTaxT = c.series.find(r => r.year === T).aTaxOwner;

  const strategyBars = (s, id) => L.bars([
    { label: NAME.SELL, value: s.sell.wealthLiquid, cls: 'f-sell', best: s.best === 'SELL' },
    { label: NAME.RENT, value: s.rent.wealthLiquid, cls: 'f-rent', best: s.best === 'RENT' },
    { label: NAME.LIVE, value: s.live.wealthLiquid, cls: 'f-live', best: s.best === 'LIVE' }
  ], { id });

  // =========================================================================== SUMMARY
  const keyRows = [
    { c: ['Property A: market value today', usd(p0.aValue2026)], status: 'brief', flag: 'F-VALUE-A' },
    { c: [`Property A: value in ${T} at ${pct(p0.aGrowth, 2)} a year`, usd(base.valueAtDeath)], status: 'model', src: ['H1'], flag: 'F-GROWTH' },
    { c: ['Federal estate tax: amount one person can leave tax-free, 2026', usd(p0.estateExclusion2026)], status: 'verified', src: ['F1', 'F3'] },
    { c: [`Federal estate tax: the same amount projected to ${T}`, usd(base.estate.exclusion)], status: 'model', src: ['F1', 'F2'], flag: 'F-ESTATE' },
    { c: [`Federal estate tax on Property A alone in ${T}`, usd(E.estateTax(base.valueAtDeath, base.estate.exclusion, p0.estateRate, 1).tax)], status: 'model', src: ['F6'], flag: 'F-ESTATE' },
    { c: ['California estate or inheritance tax', 'None'], status: 'verified', src: ['C1', 'C2'] },
    { c: ['Income tax on the gain if Property A is sold at its value on the date of death', usd(0)], status: 'verified', src: ['I1'] },
    { c: ['Property A: property tax bill, 2025', usd(p0.aBill2025)], status: 'brief', flag: 'F-BRIEF' },
    { c: [`Property A: property tax in ${T} if [OWNER] still owns it`, usd(ownerTaxT)], status: 'model', src: ['B1', 'L2'], flag: 'F-FIXED' },
    { c: [`Property A: property tax in ${T} if an heir moves in within a year`, usd(liveY1.propertyTax)], status: 'model', src: ['P1', 'P9', 'L2'], flag: 'F-P19AMOUNT' },
    { c: [`Property A: property tax in ${T} if it is rented out or left empty`, usd(rentY1.propertyTax)], status: 'model', src: ['B2', 'P1', 'L2'], flag: 'F-GROWTH' },
    { c: [`Property A: rent left after costs in ${T} if rented out`, usd(rentY1.cash)], status: 'model', src: ['HUD1'], flag: 'F-RENT-A' },
    { c: [`Property A: first-year return if sold and invested at ${pct(p0.investReturn, 2)}, before tax`, usd(base.sell.firstYearReturn)], status: 'model', src: ['TSP', 'TSPG'], flag: 'F-RETURN' },
    { c: ['Property B: property tax bill, 2025', usd(p0.bBill2025)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Property B: rent from two units, a year', usd(B.rent)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Property B: rent left after costs, a year', usd(B.net)], status: 'model', src: ['L1'], flag: 'F-MAINT' },
    { c: ['Property B: property tax a new owner would pay at today’s value', usd(B.taxIfReassessed)], status: 'model', src: ['L1', 'B2'], flag: 'F-VALUE-B' }
  ];

  const index = L.page('index.html', 'Summary',
    `Two homes and one inheritance expected between 2040 and 2050. The answer comes first. Every figure below links to the official page it came from, or to the list of things that still need checking.`,
    `
<section class="answer" aria-labelledby="h-answer">
<h2 id="h-answer">Short answer</h2>
<div class="cards two">
  <article class="card rec">
    <p class="eyebrow">Property A · Cupertino · to be inherited</p>
    <h3>Sell it soon after inheriting and invest the money — unless a family member wants to live in it.</h3>
    <ul>
      <li>At death the tax basis resets to the house’s value that day, so a prompt sale leaves <strong>${usd(0)}</strong> of taxable gain.</li>
      <li>Kept as a rental, the house is re-taxed on its full market value: about <strong>${usd(rentY1.propertyTax)}</strong> a year in ${T}, which leaves about <strong>${usd(rentY1.cash)}</strong> of rent after costs on a house worth <strong>${usd(base.valueAtDeath)}</strong>.</li>
      <li>Sold, the same money earns about <strong>${usd(base.sell.firstYearReturn)}</strong> in its first year at the middle return (${pct(p0.investReturn, 2)}), before tax.</li>
      <li>Living in it is a choice with a price: about <strong>${usd(liveCostYear)}</strong> a year over ${H} years compared with selling (${usd(real(liveCostYear, T))} in 2026 dollars).</li>
    </ul>
  </article>
  <article class="card rec">
    <p class="eyebrow">Property B · San Francisco · the household’s home</p>
    <h3>Keep it.</h3>
    <ul>
      <li>The two rented units leave about <strong>${usd(B.net)}</strong> a year after costs, and the household lives in the third.</li>
      <li>Its property tax is <strong>${usd(p0.bBill2025)}</strong> a year. A buyer would pay about <strong>${usd(B.taxIfReassessed)}</strong> on the same building. That advantage ends for good when it is sold.</li>
      <li>To do as well after a sale, the money left would have to earn <strong>${pct(B.noTax.toMatchEverything, 1)} to ${pct(B.maxTax.toMatchEverything, 1)}</strong> a year. The middle return in this model is ${pct(p0.investReturn, 2)}.</li>
    </ul>
  </article>
</div>
<p class="note">These are money results. They do not put a price on what the family wants from either home. One open question could change the picture for Property B: <a href="flagged.html#F-OWNER-B">who holds its title today</a>.</p>
</section>

<section aria-labelledby="h-compare">
<h2 id="h-compare">What the heirs would have ${H} years after inheriting Property A in ${T}</h2>
<p>After selling everything and paying tax, in ${END} dollars. Middle house-price growth (${pct(p0.aGrowth, 2)} a year) and middle investment return (${pct(p0.investReturn, 2)} a year).</p>
${strategyBars(base)}
<p class="tablenote">Sell and invest ends ${usd(base.costOfRenting)} ahead of renting and ${usd(base.costOfLiving)} ahead of living in the house. In 2026 dollars the three results are ${usd(real(base.sell.wealthLiquid, END))}, ${usd(real(base.rent.wealthLiquid, END))} and ${usd(real(base.live.wealthLiquid, END))}. Full working: <a href="decision.html">Decision</a>.</p>
</section>

<section aria-labelledby="h-change">
<h2 id="h-change">What would change the answer</h2>
<div class="cards three">
  <article class="card"><h3>Low investment returns</h3><p>Selling stops being best if the invested money earns less than <strong>${pct(c.beRentRet, 1)}</strong> a year (against renting) or <strong>${pct(c.beLive, 1)}</strong> (against living there). Treasury securities have paid ${pct(SC.returns.low.investReturn, 2)} a year since 1987.</p></article>
  <article class="card"><h3>Fast house-price growth</h3><p>Across three house-price histories and three return histories, selling is best in <strong>${sellBest} of 9</strong> combinations. The others: ${notSell.map(g => `${SC.house[g.house].label.toLowerCase()} house growth with ${SC.returns[g.returns].label.toLowerCase()} returns (${NAME[g.best].toLowerCase()} wins)`).join('; ')}.</p></article>
  <article class="card"><h3>Someone wants to live there</h3><p>Moving in within one year keeps part of the old tax base. In ${T} that saves about <strong>${usd(p19Saving)}</strong> a year in property tax against renting it out, for as long as the heir lives there.</p></article>
</div>
</section>

<section aria-labelledby="h-first">
<h2 id="h-first">Do these first</h2>
<ol class="steps">
  <li><strong>Check two documents now.</strong> The deed to Property B (<a href="flagged.html#F-OWNER-B">who owns it</a>) and the trust that holds Property A (<a href="flagged.html#F-TRUST">what it allows</a>).</li>
  <li><strong>Protect the exclusion.</strong> Keep Property A as [OWNER]’s principal residence. Do not rent it out and do not move it into an LLC.</li>
  <li><strong>Add up the whole estate.</strong> Property A alone is far below the federal exclusion; the “considerable amount of money” is what decides whether estate tax applies. See the <a href="taxes.html#estate-room">room left under the exclusion</a>.</li>
  <li><strong>At the death, get an appraisal dated that day</strong> and follow the <a href="process.html">deadlines</a>: 60 days, 150 days, nine months, one year, three years.</li>
  <li><strong>Decide within the first year whether anyone will live in Property A.</strong> The one-year rule has no exceptions.</li>
</ol>
</section>

<section aria-labelledby="h-solid">
<h2 id="h-solid">How solid is this</h2>
<div class="cards four stats">
  <div class="card stat"><div class="big">${S.SOURCES.length}</div><div>official pages read on ${S.READ}</div></div>
  <div class="card stat"><div class="big">${count('verified') + count('calculated')}</div><div>model inputs verified or calculated from official figures</div></div>
  <div class="card stat"><div class="big">${count('brief') + count('assumption')}</div><div>inputs from the brief or assumed — all adjustable in the <a href="decision.html#calculator">calculator</a></div></div>
  <div class="card stat"><div class="big">${FL.FLAGS.length}</div><div>items <a href="flagged.html">flagged for review</a>, ${high} of them able to change the answer</div></div>
</div>
<p>Future house prices and investment returns are histories, not forecasts. Several sets of pages in this repository answer the same brief with different assumptions; <a href="compare.html">this page explains the differences</a>.</p>
</section>

<section aria-labelledby="h-key">
<h2 id="h-key">Key figures</h2>
${L.table({ caption: 'Key figures and where each comes from', head: ['Figure', 'Amount'], num: [1], rows: keyRows })}
</section>
`, { description: 'Executive summary: what to do with two California homes when one is inherited through a trust.' });

  // =========================================================================== DECISION
  const resultRow = (s, k, extraSrc, flag) => {
    const o = s[k.toLowerCase()];
    const bestV = Math.max(s.sell.wealthLiquid, s.live.wealthLiquid, s.rent.wealthLiquid);
    return { c: [NAME[k] + (s.best === k ? ' <span class="tag">highest</span>' : ''), k === 'SELL' ? usd(o.firstYearReturn) + ' <span class="small">(return, before tax)</span>' : usd(o.firstYearCash),
      usd(o.wealthLiquid), usd(real(o.wealthLiquid, s.endYear)), o.wealthLiquid === bestV ? '—' : usd(o.wealthLiquid - bestV)],
      status: 'model', src: extraSrc, flag, cls: s.best === k ? 'bestrow' : '' };
  };
  const caseRows = [];
  for (const TT of [2040, 2045, 2050]) for (const HH of [10, 20]) {
    const s = sim({ inheritYear: TT, horizon: HH });
    caseRows.push({ c: [`${TT}, followed ${HH} years (to ${TT + HH})`, usd(s.valueAtDeath), usd(s.sell.wealthLiquid), usd(s.rent.wealthLiquid), usd(s.live.wealthLiquid), NAME[s.best]],
      status: 'model', src: ['I1', 'P1', 'H1'], flag: 'F-GROWTH' });
  }
  const bests = new Set(caseRows.map(r => r.c[5]));
  const sameBest = bests.size === 1 ? `${Array.from(bests)[0]} is highest in all six cases.` : 'The highest choice is not the same in every case.';
  const beatsList = need => { const l = Object.keys(SC.returns).filter(k => need > SC.returns[k].investReturn).map(k => `${SC.returns[k].label.toLowerCase()} (${pct(SC.returns[k].investReturn, 2)})`); return l.length ? l.join(', ') : 'none of the three'; };
  const gridRows = grid.map(g => ({
    c: [houseLabel(g.house), retLabel(g.returns), usd(g.sell), usd(g.rent), usd(g.live), NAME[g.best], usd(Math.max(g.rent, g.live) - g.sell)],
    status: 'model', src: ['H1', 'TSP', 'TSPG'], flag: 'F-GROWTH', cls: g.best === 'SELL' ? '' : 'altrow' }));

  const sellRows = [
    { c: [`Sale price: the house’s value in ${T}`, usd(base.valueAtDeath)], status: 'model', src: ['H1'], flag: 'F-GROWTH' },
    { c: [`Cost of selling (${pct(p0.sellCost, 1)})`, usd(-base.sell.saleCosts)], status: 'assumption', src: ['T1', 'T3'], flag: 'F-SELLCOST' },
    { c: ['Income tax on the gain (basis is the value at death)', usd(-base.sell.saleTax)], status: 'verified', src: ['I1'] },
    { c: ['Money invested', usd(base.sell.proceeds)], status: 'model', src: ['I1'], flag: 'F-SELLCOST' },
    { c: [`First-year return at ${pct(p0.investReturn, 2)}, before tax`, usd(base.sell.firstYearReturn)], status: 'model', src: ['TSP', 'TSPG'], flag: 'F-RETURN' }
  ];
  const liveRows = [
    { c: [`Property tax on a taxable value of ${usd(liveY1.taxableValue)}`, usd(-liveY1.propertyTax)], status: 'model', src: ['P1', 'P9', 'L2'], flag: 'F-P19AMOUNT' },
    { c: ['Insurance', usd(-liveY1.insurance)], status: 'brief', flag: 'F-INSURANCE' },
    { c: ['Maintenance and repairs', usd(-liveY1.maintenance)], status: 'assumption', flag: 'F-MAINT' },
    { c: ['Water and power', usd(-liveY1.utilities)], status: 'brief', flag: 'F-UTIL' },
    { c: ['Rent from the unit the household leaves in Property B', usd(liveY1.unitRent)], status: 'assumption', src: ['HUD2'], flag: 'F-RENT-B' },
    { c: [`Income tax on that rent (${pct(p0.taxOrdinary, 1)})`, usd(-liveY1.unitRentTax)], status: 'assumption', src: ['F2', 'C5'], flag: 'F-TAXRATES' },
    { c: ['<strong>Net cash for the year</strong>', `<strong>${usd(liveY1.cash)}</strong>`], status: 'model', src: ['P1'], flag: 'F-RENT-B' }
  ];
  const rentRows = [
    { c: [`Rent received, after ${pct(p0.vacancy, 0)} vacancy`, usd(rentY1.grossRent)], status: 'assumption', src: ['HUD1'], flag: 'F-RENT-A' },
    { c: [`Property tax on full market value, ${usd(rentY1.taxableValue)}`, usd(-rentY1.propertyTax)], status: 'model', src: ['B2', 'P1', 'L2'], flag: 'F-GROWTH' },
    { c: ['Insurance', usd(-rentY1.insurance)], status: 'brief', flag: 'F-INSURANCE' },
    { c: ['Maintenance and repairs', usd(-rentY1.maintenance)], status: 'assumption', flag: 'F-MAINT' },
    { c: ['Property manager', usd(-rentY1.management)], status: 'assumption', flag: 'F-MGMT' },
    { c: [`Income tax (depreciation of ${usd(rentY1.depreciation)} is more than the rent left, so none is due; the unused part carries forward)`, usd(-rentY1.incomeTax)], status: 'model', src: ['D1', 'I6'], flag: 'F-SPLIT' },
    { c: ['<strong>Net cash for the year</strong>', `<strong>${usd(rentY1.cash)}</strong>`], status: 'model', src: ['D1'], flag: 'F-RENT-A' }
  ];
  const endRows = [
    { c: ['Sell and invest: account balance', usd(base.sell.account.balance), usd(base.sell.account.balance - base.sell.wealthLiquid), usd(base.sell.wealthLiquid)], status: 'model', src: ['I2', 'C4'], flag: 'F-TAXRATES' },
    { c: [`Rent it out: house sold for ${usd(base.rent.houseValueEnd)} less ${pct(p0.sellCost, 1)}, plus saved rent`, usd(base.rent.saleNet + base.rent.account.balance), usd(base.rent.saleNet + base.rent.account.balance - base.rent.wealthLiquid), usd(base.rent.wealthLiquid)], status: 'model', src: ['I2', 'D1', 'C4'], flag: 'F-TAXRATES' },
    { c: [`Live in it: house sold for ${usd(base.live.houseValueEnd)} less ${pct(p0.sellCost, 1)}, less the yearly costs paid`, usd(base.live.saleNet + base.live.account.balance), usd(base.live.saleNet + base.live.account.balance - base.live.wealthLiquid), usd(base.live.wealthLiquid)], status: 'model', src: ['I3', 'I2', 'C4'], flag: 'F-TAXRATES' }
  ];
  const beRows = [
    { c: ['Investment return below which <em>renting</em> beats selling', pct(c.beRentRet, 2) + ' a year'], status: 'model', src: ['TSP', 'TSPG'], flag: 'F-RETURN' },
    { c: ['Investment return below which <em>living in it</em> beats selling', pct(c.beLive, 2) + ' a year'], status: 'model', src: ['TSP', 'TSPG'], flag: 'F-RETURN' },
    { c: ['Monthly rent, in 2026 dollars, at which renting matches selling', c.beRent === null ? 'Not reached' : usd(c.beRent)], status: 'model', src: ['HUD1'], flag: 'F-RENT-A' },
    { c: ['Rent assumed in the model, in 2026 dollars', usd(p0.aRent2026)], status: 'assumption', src: ['HUD1'], flag: 'F-RENT-A' },
    { c: [`Yearly price of living in Property A instead of selling (${T} to ${END - 1})`, usd(liveCostYear)], status: 'model', src: ['P1'], flag: 'F-RETURN' },
    { c: [`Property tax saved each year by moving in rather than renting, ${T}`, usd(p19Saving)], status: 'model', src: ['P1', 'P9', 'L2'], flag: 'F-P19AMOUNT' }
  ];
  const bRows = [
    { c: ['Rent from the two rented units', usd(B.rent)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Property tax', usd(-B.costs.propertyTax)], status: 'brief', flag: 'F-BRIEF' },
    { c: ['Insurance', usd(-B.costs.insurance)], status: 'brief', flag: 'F-INSURANCE' },
    { c: ['Water, all three units', usd(-B.costs.water)], status: 'brief', flag: 'F-UTIL' },
    { c: ['Electricity', usd(-B.costs.power)], status: 'brief', flag: 'F-UTIL' },
    { c: ['Maintenance and repairs', usd(-B.costs.maintenance)], status: 'assumption', flag: 'F-MAINT' },
    { c: ['<strong>Rent left after costs, before income tax</strong>', `<strong>${usd(B.net)}</strong>`], status: 'model', src: ['L1'], flag: 'F-MAINT' },
    { c: ['Value of living there: what a comparable rental would cost the household', usd(B.housing)], status: 'assumption', src: ['HUD2'], flag: 'F-RENT-B' },
    { c: [`Rise in the building’s value at ${pct(p0.bGrowth, 2)} a year`, usd(B.growth)], status: 'model', src: ['H2'], flag: 'F-GROWTH' },
    { c: [`If sold today: price less ${pct(p0.sellCost, 1)} selling cost`, usd(B.saleNet)], status: 'model', src: ['T4'], flag: 'F-SELLCOST' },
    { c: ['If sold today: income tax on the gain', `${usd(0)} to ${usd(B.taxMax)}`], status: 'unverified', src: ['I2', 'C4'], flag: 'F-BASIS-B' },
    { c: ['Return the money left would need, to replace the rent alone', `${pct(B.noTax.toReplaceRent, 1)} to ${pct(B.maxTax.toReplaceRent, 1)} a year`], status: 'model', src: ['TSP'], flag: 'F-BASIS-B' },
    { c: ['… to replace the rent and pay for a home', `${pct(B.noTax.toReplaceRentAndHome, 1)} to ${pct(B.maxTax.toReplaceRentAndHome, 1)} a year`], status: 'model', src: ['TSP', 'HUD2'], flag: 'F-BASIS-B' },
    { c: ['… and to match the building’s rise in value as well', `${pct(B.noTax.toMatchEverything, 1)} to ${pct(B.maxTax.toMatchEverything, 1)} a year`], status: 'model', src: ['TSP', 'H2'], flag: 'F-BASIS-B' },
    { c: ['Property tax a new owner would pay at today’s value', usd(B.taxIfReassessed)], status: 'model', src: ['L1', 'B2'], flag: 'F-VALUE-B' }
  ];

  // ---- calculator form
  const groups = [];
  I.FIELDS.filter(f => !f.fixed).forEach(f => { let g = groups.find(x => x.name === f.group); if (!g) groups.push(g = { name: f.group, fields: [] }); g.fields.push(f); });
  const control = f => {
    const id = 'in-' + f.key;
    let input;
    if (f.kind === 'choice') input = `<select id="${id}" data-key="${f.key}" data-kind="choice" data-default="${f.value}">${f.choices.map(ch => `<option value="${ch[0]}"${ch[0] === f.value ? ' selected' : ''}>${L.esc(ch[1].replace(/\$([\d,]+)/g, (m, n) => usd(Number(n.replace(/,/g, '')))))}</option>`).join('')}</select>`;
    else if (f.kind === 'pct') { const v = String(Math.round(f.value * 1e6) / 1e4); input = `<span class="unit"><input id="${id}" type="number" inputmode="decimal" step="${f.digits >= 2 ? '0.01' : '0.1'}" data-key="${f.key}" data-kind="pct" value="${v}" data-default="${v}"><span>%</span></span>`; }
    else if (f.kind === 'num') input = `<input id="${id}" type="number" inputmode="decimal" step="0.05" data-key="${f.key}" data-kind="num" value="${f.value}" data-default="${f.value}">`;
    else input = `<span class="unit"><span>$</span><input id="${id}" type="number" inputmode="numeric" step="10" min="0" data-key="${f.key}" data-kind="usd" value="${f.value}" data-default="${f.value}">${f.kind === 'usdm' ? '<span>/mo</span>' : ''}</span>`;
    return `<div class="field"><label for="${id}">${L.esc(f.label)}</label>${input}<div class="fieldmeta">${L.chip(f.status)} <a href="method.html#m-${f.key}">why this value</a></div></div>`;
  };
  const calculator = `
<section id="calculator" aria-labelledby="h-calc">
<h2 id="h-calc">Calculator</h2>
<p>Change any input and the three results are recalculated in your browser by the same code that built the tables above. Nothing is sent anywhere. Amounts are rounded to the nearest $10.</p>
<div class="calcgrid">
<form id="calc" class="calc" autocomplete="off">
  <div class="presets" role="group" aria-label="Scenarios">
    <span>House prices:</span>
    ${Object.keys(SC.house).map(k => `<button type="button" data-house="${k}">${SC.house[k].label}</button>`).join('')}
    <span>Returns:</span>
    ${Object.keys(SC.returns).map(k => `<button type="button" data-returns="${k}">${SC.returns[k].label}</button>`).join('')}
    <button type="button" id="calc-reset" class="ghost">Reset</button>
  </div>
  ${groups.map(g => `<fieldset><legend>${L.esc(g.name)}</legend>${g.fields.map(control).join('')}</fieldset>`).join('\n  ')}
</form>
<div class="calcout" id="calc-out" aria-live="polite">
  <noscript><p class="note">The calculator needs JavaScript. The tables above show the same results for the default inputs.</p></noscript>
  <h3 id="calc-title">Result</h3>
  <div id="calc-bars"></div>
  <table class="plain"><tbody id="calc-rows"></tbody></table>
  <p class="small">Results use the inputs on the left; each input’s status and source are on the <a href="method.html#inputs">Method</a> page, and every assumption is on the <a href="flagged.html">Flagged</a> page.</p>
</div>
</div>
</section>`;

  const decision = L.page('decision.html', 'Decision',
    `Three things can be done with Property A after it is inherited. This page compares them in money, shows what would have to be true for the answer to change, and then looks at Property B.`,
    `
<section aria-labelledby="h-choices">
<h2 id="h-choices">The three choices</h2>
<div class="cards three">
  <article class="card"><h3><span class="dot f-sell"></span>Sell and invest</h3><p>Sell within months of the death at the appraised value. No gain is taxed, because the basis is the value at death. Invest what is left after selling costs. The household stays in Property B.</p></article>
  <article class="card"><h3><span class="dot f-rent"></span>Rent it out</h3><p>Keep the house and let it. It is re-taxed on its full market value. Rent is taxed after expenses and depreciation; the depreciation is taxed back when the house is sold. The household stays in Property B.</p></article>
  <article class="card"><h3><span class="dot f-live"></span>Live in it</h3><p>Move in within one year and claim the parent-to-child exclusion, which keeps part of the old tax base. The unit left empty in Property B is rented. Up to ${usd(p0.homeSaleExclusion)} of later gain is tax-free on sale.</p></article>
</div>
<p>All three are followed for the same number of years, and then everything is sold and taxed, so that a house and an investment account can be compared like for like. Property B’s own rent and costs are the same in all three and are left out.</p>
</section>

<section aria-labelledby="h-result">
<h2 id="h-result">Result: inherited in ${T}, measured in ${END}</h2>
${strategyBars(base)}
${L.table({ caption: `Middle case: house prices +${pct(p0.aGrowth, 2)} a year, investments +${pct(p0.investReturn, 2)} a year, inflation ${pct(p0.inflation, 2)} a year`,
    head: ['Choice', `Cash in the first year (${T})`, `What the heirs have in ${END}, after tax`, 'The same in 2026 dollars', 'Behind the highest by'], num: [1, 2, 3, 4],
    rows: [resultRow(base, 'SELL', ['I1', 'TSP', 'TSPG'], 'F-RETURN'), resultRow(base, 'RENT', ['B2', 'D1', 'HUD1'], 'F-RENT-A'), resultRow(base, 'LIVE', ['P1', 'P9', 'I3'], 'F-RENT-B')] })}
</section>

<section aria-labelledby="h-years">
<h2 id="h-years">Does the year of inheritance matter?</h2>
${L.table({ caption: 'Same middle case, for each inheritance year in the brief’s window and two holding periods', head: ['Inherited in', 'Value of Property A that year', NAME.SELL, NAME.RENT, NAME.LIVE, 'Highest'], num: [1, 2, 3, 4], rows: caseRows,
    note: 'Amounts are after tax, in dollars of the final year. ' + sameBest })}
</section>

<section aria-labelledby="h-grid">
<h2 id="h-grid">What if prices or returns turn out differently?</h2>
<p>Three house-price histories and three investment histories give nine combinations. None is a forecast.</p>
${L.table({ caption: `Inherited in ${T}, measured in ${END}, after tax`, head: ['House prices', 'Investment return', NAME.SELL, NAME.RENT, NAME.LIVE, 'Highest', 'Best way of keeping the house, against selling'], num: [2, 3, 4, 6], rows: gridRows,
    note: `Selling is highest in ${sellBest} of 9. House-price windows: ${Object.keys(SC.house).map(k => `${SC.house[k].label.toLowerCase()} = ${SC.house[k].window}`).join('; ')}. Between 2006 and 2012 the same index fell by about a quarter.` })}
</section>

<section aria-labelledby="h-be">
<h2 id="h-be">Break-even points</h2>
${L.table({ caption: 'How far an assumption would have to move to change the answer (middle case)', head: ['Question', 'Answer'], num: [1], rows: beRows })}
</section>

<section aria-labelledby="h-first-year">
<h2 id="h-first-year">Where the money goes in the first year (${T})</h2>
${L.table({ caption: 'Sell and invest', head: ['Item', 'Amount'], num: [1], rows: sellRows })}
${L.table({ caption: 'Rent it out', head: ['Item', 'Amount'], num: [1], rows: rentRows })}
${L.table({ caption: 'Live in it', head: ['Item', 'Amount'], num: [1], rows: liveRows })}
${L.table({ caption: `At the end (${END}): selling up and paying tax`, head: ['Choice', 'Before tax', 'Tax', 'After tax'], num: [1, 2, 3], rows: endRows,
    note: `Tax rates used: ${pct(p0.taxGain, 1)} on gains, ${pct(p0.taxRecapture, 1)} on depreciation taken back. The first ${usd(p0.homeSaleExclusion)} of gain on a home lived in for two of the last five years is not taxed.` })}
</section>

<section aria-labelledby="h-left-out">
<h2 id="h-left-out">What the money figures leave out</h2>
<ul>
  <li><strong>What the family wants.</strong> A larger home, a school district, a place with memories: none has a price here. The figure to weigh them against is the yearly price of living in Property A, above.</li>
  <li><strong>Work and risk of being a landlord</strong> for a single house: vacancies, repairs, one tenant.</li>
  <li><strong>Concentration.</strong> Keeping both homes leaves most of the family’s wealth in Bay Area housing. The house-price index for both areas fell by about a quarter after 2006.</li>
  <li><strong>Market risk the other way.</strong> Invested money can also fall sharply in a single year; the returns used are long-run averages.</li>
  <li><strong>A later step-up.</strong> Assets held until the heirs’ own deaths get a new basis under today’s law, whether they are houses or shares, so this does not favour one choice.</li>
</ul>
</section>

<section id="property-b" aria-labelledby="h-b">
<h2 id="h-b">Property B: keep or sell</h2>
<p>Keep it. The table shows why: low tax, rent from two units, a home in the third, and a tax bill on sale that cannot be worked out without records the brief did not include.</p>
${L.table({ caption: 'Property B as it stands today, a year', head: ['Item', 'Amount'], num: [1], rows: bRows,
    note: `The range for tax on a sale runs from nothing to tax on everything above the assessed value. Return histories that keeping Property B beats: ${beatsList(B.noTax.toMatchEverything)} if a sale were untaxed; ${beatsList(B.maxTax.toMatchEverything)} if it were fully taxed.` })}
</section>
${calculator}
`, { description: 'Decision analysis: live in, rent out or sell an inherited house; keep or sell the current home.',
    scripts: '<script src="src/format.js"></script>\n<script src="src/engine.js"></script>\n<script src="src/inputs.js"></script>\n<script src="assets/calc.js"></script>' });

  // =========================================================================== PROJECTIONS
  const aRows = series.map(r => ({ c: [String(r.year), usd(r.aValue), usd(r.aAssessed), usd(r.aTaxOwner), usd(r.prop19Amount), usd(r.aLiveTaxable), usd(r.aLiveTax), usd(r.aFullTax)],
    status: 'model', src: ['H1', 'B1', 'L2', 'P9'], flag: 'F-GROWTH' }));
  const bCost0 = B.costs.insurance + B.costs.water + B.costs.power + B.costs.maintenance;
  const bRowsP = series.map(r => {
    const k = r.year - E.BASE_YEAR;
    const rent = B.rent * Math.pow(1 + p0.inflation * p0.rentCapShare, k);
    const costs = bCost0 * Math.pow(1 + p0.inflation, k);
    return { c: [String(r.year), usd(r.bValue), usd(r.bAssessed), usd(r.bTaxOwner), usd(rent), usd(costs), usd(rent - costs - r.bTaxOwner)],
      status: 'model', src: ['H2', 'B1', 'L1', 'R3'], flag: 'F-BRIEF' };
  });
  const eRows = series.map(r => ({ c: [String(r.year), usd(r.estateExclusion), usd(r.aValue), usd(r.estateExclusion - r.aValue), usd(2 * r.estateExclusion - r.aValue)],
    status: 'model', src: ['F1', 'F2'], flag: 'F-ESTATE' }));
  const scenRows = [];
  for (const k of Object.keys(SC.house)) {
    const h = SC.house[k];
    const v = y => E.marketValue(p0.aValue2026, h.aGrowth, y), w = y => E.marketValue(p0.bValue2026, h.bGrowth, y);
    scenRows.push({ c: [`Property A, ${h.label.toLowerCase()}: ${pct(h.aGrowth, 2)} a year`, usd(v(2040)), usd(v(2045)), usd(v(2050))], status: 'model', src: ['H1'], flag: 'F-GROWTH' });
    scenRows.push({ c: [`Property B, ${h.label.toLowerCase()}: ${pct(h.bGrowth, 2)} a year`, usd(w(2040)), usd(w(2045)), usd(w(2050))], status: 'model', src: ['H2'], flag: 'F-GROWTH' });
  }
  const afterLive = base.live.years.map(y => ({ c: [String(y.year), usd(y.taxableValue), usd(-y.propertyTax), usd(-(y.insurance + y.maintenance + y.utilities)), usd(y.unitRent - y.unitRentTax), usd(y.cash)],
    status: 'model', src: ['P1', 'B1', 'L2'], flag: 'F-RENT-B' }));
  const afterRent = base.rent.years.map(y => ({ c: [String(y.year), usd(y.taxableValue), usd(y.grossRent), usd(-y.propertyTax), usd(-(y.insurance + y.maintenance + y.management)), usd(-y.incomeTax), usd(y.cash)],
    status: 'model', src: ['B2', 'B1', 'L2', 'D1'], flag: 'F-RENT-A' }));
  const afterSell = base.sell.years.map(y => ({ c: [String(y.year), usd(y.balance)], status: 'model', src: ['TSP', 'TSPG'], flag: 'F-RETURN' }));

  const chart = L.lineChart({
    title: 'Property A, 2026 to 2050: market value, the value taxed if an heir moves in, and the value taxed today',
    years: series.map(r => r.year),
    series: [
      { name: 'Market value (also the taxed value if rented out)', values: series.map(r => r.aValue) },
      { name: 'Taxed value if inherited that year and an heir moves in', values: series.map(r => r.aLiveTaxable) },
      { name: 'Taxed value while [OWNER] keeps it', values: series.map(r => r.aAssessed) }
    ],
    caption: 'The gap between the top two lines is the Proposition 19 amount. It is adjusted only every second year, so the gap widens slowly.'
  });

  const projections = L.page('projections.html', 'Projections 2026–2050',
    `Year-by-year figures for both properties under the middle case. They are arithmetic on today’s figures and past growth rates, not forecasts. All amounts are in dollars of the year shown, rounded to the nearest $10.`,
    `
<section aria-labelledby="h-a">
<h2 id="h-a">Property A (Cupertino)</h2>
${chart}
${L.table({ caption: `Property A: value and property tax, by the year in which it might be inherited (house prices +${pct(p0.aGrowth, 2)} a year; taxed value +${pct(p0.prop13Factor, 0)} a year; tax rate ${pct(p0.aRate, 4)})`,
    head: ['Year', 'Market value', 'Taxed value while [OWNER] keeps it', 'Tax bill while [OWNER] keeps it', 'Proposition 19 amount', 'Taxed value if inherited this year and an heir moves in', 'First tax bill if an heir moves in', 'First tax bill if rented out or left empty'], num: [1, 2, 3, 4, 5, 6, 7], rows: aRows,
    note: `The Proposition 19 amount for 2026 is the official figure rounded to $10; the exact figure is on the <a href="taxes.html#prop19">Taxes</a> page. Later amounts assume the California index rises ${pct(p0.caHpiChange, 2)} in each adjustment year.` })}
</section>

<section aria-labelledby="h-scen">
<h2 id="h-scen">Values under the three house-price histories</h2>
${L.table({ caption: 'Market value in each possible year of inheritance', head: ['Property and growth rate', '2040', '2045', '2050'], num: [1, 2, 3], rows: scenRows })}
</section>

<section aria-labelledby="h-after">
<h2 id="h-after">Property A after an inheritance in ${T}</h2>
${L.table({ caption: 'If an heir lives in it', head: ['Year', 'Taxed value', 'Property tax', 'Insurance, repairs, water and power', 'Rent from the unit left in Property B, after tax', 'Net cash'], num: [1, 2, 3, 4, 5], rows: afterLive })}
${L.table({ caption: 'If it is rented out', head: ['Year', 'Taxed value', 'Rent received', 'Property tax', 'Insurance, repairs, manager', 'Income tax', 'Net cash'], num: [1, 2, 3, 4, 5, 6], rows: afterRent,
    note: `Depreciation of ${usd(base.rent.depreciationPerYear)} a year covers the rent left after expenses, so no income tax is due in these years; ${usd(base.rent.accumulatedDepreciation)} of depreciation is taxed back at sale.` })}
${L.table({ caption: `If it is sold and ${usd(base.sell.proceeds)} is invested at ${pct(p0.investReturn, 2)} a year`, head: ['End of year', 'Account balance before tax'], num: [1], rows: afterSell })}
</section>

<section aria-labelledby="h-bp">
<h2 id="h-bp">Property B (San Francisco)</h2>
${L.table({ caption: `Property B, kept by its present owners (value +${pct(p0.bGrowth, 2)} a year; taxed value +${pct(p0.prop13Factor, 0)} a year; rent +${pct(p0.inflation * p0.rentCapShare, 2)} a year, which is 60% of inflation; costs +${pct(p0.inflation, 2)} a year)`,
    head: ['Year', 'Market value', 'Taxed value', 'Property tax', 'Rent from two units', 'Insurance, water, power, repairs', 'Rent left after costs'], num: [1, 2, 3, 4, 5, 6], rows: bRowsP,
    note: 'Rent rises at the allowed yearly increase only while the same tenants stay; a new tenancy starts at the market rent. Whether the building is covered by the Rent Ordinance was not checked.' })}
</section>

<section aria-labelledby="h-e">
<h2 id="h-e">Federal estate tax: the exclusion against Property A</h2>
${L.table({ caption: `Exclusion per person: official for 2026 and 2027, then +${pct(p0.estateIndexing, 2)} a year`, head: ['Year', 'Exclusion, one person', 'Property A market value', 'Room left for other assets, one exclusion', 'Room left, two exclusions'], num: [1, 2, 3, 4], rows: eRows,
    note: 'Estate tax is 40% of the estate above the exclusion. “Two exclusions” applies only if [OWNER] is the surviving spouse and the first estate elected portability on time.' })}
</section>
`, { description: 'Year-by-year projections 2026 to 2050 for both properties.' });

  const ref = require('./pages_ref.js').build(c, { NAME, houseLabel, retLabel, p19Saving, liveY1, rentY1 });
  return Object.assign({ 'index.html': index, 'decision.html': decision, 'projections.html': projections }, ref);
};
