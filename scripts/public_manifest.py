"""Explicit review boundary for the public guide. No personal data belongs here."""
PUBLIC_FILES = {
    'index.html', 'robots.txt', 'assets/safe.css', 'assets/safe.js',
    'guide/figures/official-figures.json',
    *('guide/' + name + '.html' for name in (
        'decision', 'stress', 'conditions', 'brief', 'property', 'tax', 'process', 'summary',
        'questions', 'suggestions', 'review', 'sources', 'precommit', 'tax-realism',
        'glossary', 'timeline', 'attorney-cpa', 'paths', 'whatif')),
    *('guide/data/' + name + '.js' for name in (
        'model', 'stress', 'conditions', 'breakeven',
        'decision-page', 'stress-page', 'tax-page', 'conditions-page',
        'brief-page', 'whatif-page',
        'tax-realism', 'tax-realism-page')),
}
