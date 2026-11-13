"""Explicit review boundary for the public dashboard. No personal data belongs here.

This list must match the Jekyll output of the repository root exactly, so that
`check-publication.py` can audit what GitHub Pages actually publishes.
"""
PUBLIC_FILES = {
    'index.html',
    'robots.txt',
    'assets/app.js',
    'assets/styles.css',
    # site/** — the reviewed dashboard pages and the engines they load
    'site/black-swan.html',
    'site/data/costs.js',
    'site/data/gate.js',
    'site/data/history-engine.js',
    'site/data/history.js',
    'site/data/ledger.js',
    'site/data/model.js',
    'site/data/options.js',
    'site/data/questions.js',
    'site/data/scenarios.js',
    'site/data/sources.js',
    'site/data/stress.js',
    'site/data/suggestions.js',
    'site/decision.html',
    'site/estate-tax.html',
    'site/inheritance.html',
    'site/operating-costs.html',
    'site/options.html',
    'site/plan.html',
    'site/properties.html',
    'site/questions-gate.html',
    'site/questions.html',
    'site/review.html',
    'site/san-francisco.html',
    'site/scenarios.html',
    'site/sources.html',
    'site/stress.html',
    'site/suggestions.html',
    'site/verification.html',
}
