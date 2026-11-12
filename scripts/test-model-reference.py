#!/usr/bin/env python3
"""Independent arithmetic reconstruction of the public, purely fictional models.

No household data are read. Compares unrounded JS outputs against separate Python
formulas across control settings and every year of the five synthetic paths.
"""
import json
import math
import subprocess

script = r'''
global.window=global;
require('./guide/data/model.js'); require('./guide/data/stress.js');
const base=MODEL.BASE, decisions=[];
for (const year of [2040,2045,2050]) for (const horizon of [10,20,50])
for (const growth of [0.02,0.035,0.05]) for (const ret of [0.03,0.05,0.07]) {
  const c={...base,inheritYear:year,appreciation:growth,portfolioNet:ret};
  decisions.push({year,horizon,growth,ret,result:MODEL.decision(c,horizon),b:MODEL.sfAnnual(year,c)});
}
const paths=Object.fromEntries(Object.keys(STRESS.paths).map(k=>[k,STRESS.run(k)]));
console.log(JSON.stringify({base,decisions,paths}));
'''
obj=json.loads(subprocess.check_output(['node','-e',script],text=True))
b=obj['base']
checks=0

def near(actual,expected,label):
    global checks
    checks+=1
    if not math.isclose(actual,expected,rel_tol=2e-12,abs_tol=1e-5):
        raise AssertionError(f'{label}: independent reconstruction differs')

def series_a(year,c):
    n=year-c['startYear']
    market=c['aValue']*(1+c['appreciation'])**n
    base=c['aAssessed']*(1+c['assessmentGrowth'])**n
    return market,min(market,base)

def transfer(year,c):
    market,assessed=series_a(year,c)
    steps=max(0,(year-2025)//2)
    allowance=c['prop19Amount']*(1+c['appreciation'])**steps
    return market,assessed,allowance,min(market,max(assessed,market-allowance))

def holding(year,option,c):
    t=c['inheritYear']; market,_,_,live_base=transfer(t,c)
    value,_=series_a(year,c)
    assessed=min(value,(live_base if option=='live' else market)*(1+c['assessmentGrowth'])**(year-t))
    n=year-c['startYear']
    costs=assessed*c['aRate']+c['aWaterMonthly']*12*(1+c['expenseInflation'])**n
    costs+=c['aInsuranceAnnual']*(1+c['expenseInflation'])**n+value*c['maintenanceA']-c['aSolarMonthlyCredit']*12
    if option=='live': return -costs
    gross=c['aRentMonthly']*12*(1+c['rentGrowth'])**n
    noi=gross*(1-c['vacancy'])*(1-c['management'])-costs
    return noi-max(0,noi)*c['ordinaryTax']

for row in obj['decisions']:
    y,h,g,ret=row['year'],row['horizon'],row['growth'],row['ret']
    c={**b,'inheritYear':y,'appreciation':g,'portfolioNet':ret}
    result=row['result']; market,assessed,allowance,primary=transfer(y,c)
    near(result['transfer']['market'],market,'transfer market')
    near(result['transfer']['carryForwardAssessed'],assessed,'transfer prior assessment')
    near(result['transfer']['allowance'],allowance,'transfer scenario allowance')
    near(result['transfer']['primaryAssessed'],primary,'transfer scenario assessment')
    initial=market*(1-c['saleCost'])
    near(result['sell']['terminal'],initial*(1+ret)**h,'sell endpoint')
    near(result['sell']['firstYearCash'],initial*ret,'sell first-year value change')
    for option in ('rent','live'):
        cash=0
        for t in range(1,h+1):
            flow=holding(y+t,option,c)
            near(result[option]['yearly'][t-1]['afterTaxCash'],flow,f'{option} annual flow')
            cash=cash*(1+ret)+flow
        final_market,_=series_a(y+h,c)
        realized=final_market*(1-c['saleCost'])
        gain=max(0,realized-market)
        exclusion=min(c['primaryGainExclusion'],gain) if option=='live' and h>=2 else 0
        tax=max(0,gain-exclusion)*c['capitalGainsTax']
        near(result[option]['capitalGainsTax'],tax,f'{option} gain tax')
        near(result[option]['terminal'],realized-tax+cash,f'{option} endpoint')
    n=y-c['startYear']
    b_market=c['bValue']*(1+g)**n
    b_assessed=min(b_market,c['bAssessed']*(1+c['assessmentGrowth'])**n)
    gross=c['bRentMonthly']*12*(1+c['sfRentGrowth'])**n
    costs=(c['bWaterMonthly']*12+c['bElectricMonthly']*12+c['bInsuranceAnnual']+c['bFeeAnnual'])*(1+c['expenseInflation'])**n
    noi=gross*(1-c['vacancy'])*(1-c['management'])-b_assessed*c['bRate']-costs-b_market*c['maintenanceB']
    near(row['b']['noi'],noi,'B NOI')
    near(row['b']['assessed'],b_assessed,'B assessment')

homes=[.04,.05,.02,-.04,0,.06,.04,.03,.04,.03]
portfolios=[.08,.10,.03,-.12,.02,.13,.07,.05,.06,.06]
prices=[.025,.03,.04,.035,.02,.025,.03,.025,.02,.025]
for key,rows in obj['paths'].items():
    assert len(rows)==50
    c={**b,'inheritYear':2045}; market,_,_,primary=transfer(2045,c)
    inherited=market; fbase=market; livebase=primary
    sell=market*(1-c['saleCost']); reserve=live_reserve=0; index=1
    rent=c['aRentMonthly']*12*(1+c['rentGrowth'])**19
    water=c['aWaterMonthly']*12*(1+c['expenseInflation'])**19
    insurance=c['aInsuranceAnnual']*(1+c['expenseInflation'])**19
    for t,row in enumerate(rows,1):
        cycle=t-48 if key in ('crisis','late') and t>=48 else (t-1)%10
        home,portfolio,inflation=homes[cycle],portfolios[cycle],prices[cycle]
        rent_growth,vacancy,jump,repair=.025,.05,1,0
        if (key=='crisis' and t<=3) or (key=='late' and t>=48):
            i=t-1 if key=='crisis' else t-48
            home=[-.25,-.10,.04][i]; portfolio=[-.35,-.10,.12][i]; rent_growth=-.05; vacancy=.20
        if key=='inflation' and t<=5:
            home,portfolio,inflation,rent_growth,jump=0,.01,.08,.02,2 if t==1 else 1
        if key=='disaster' and t==10:
            home,vacancy,jump,repair=-.15,1,2,250000
        market*=1+home; fbase*=1+min(.02,max(0,inflation)); livebase*=1+min(.02,max(0,inflation))
        assessed=min(fbase,market); live_assessed=min(livebase,market)
        index*=1+inflation; rent*=1+rent_growth; water*=1+inflation; insurance*=(1+inflation)*jump
        tax=assessed*c['aRate']; costs=water+insurance+market*c['maintenanceA']+repair-c['aSolarMonthlyCredit']*12
        noi=rent*(1-vacancy)*(1-c['management'])-tax-costs
        cash=noi-max(0,noi)*c['ordinaryTax']
        sell*=1+portfolio; reserve=reserve*(1+portfolio)+cash
        live_reserve=live_reserve*(1+portfolio)-costs-live_assessed*c['aRate']
        realized=market*(1-c['saleCost'])
        rent_end=realized-max(0,realized-inherited)*c['capitalGainsTax']+reserve
        live_end=realized-max(0,realized-inherited-(c['primaryGainExclusion'] if t>=2 else 0))*c['capitalGainsTax']+live_reserve
        for name,value in [('market',market),('factoredBase',fbase),('assessed',assessed),('liveAssessed',live_assessed),
                           ('priceIndex',index),('cash',cash),('sell',sell),('rent',rent_end),('live',live_end),
                           ('realSell',sell/index),('realRent',rent_end/index),('realLive',live_end/index)]:
            near(row[name],value,f'{key} year {t} {name}')
print(f'PASS: independently reconstructed {len(obj["decisions"])} decision configurations and 250 stress years; {checks} unrounded arithmetic comparisons.')
