"""Explicit review boundary for the public guide. No personal data belongs here."""
PUBLIC_FILES = {
    'index.html', 'robots.txt', 'assets/safe.css', 'assets/safe.js',
    *('guide/' + name + '.html' for name in (
        'decision', 'stress', 'conditions', 'brief', 'property', 'tax', 'process',
        'questions', 'suggestions', 'review', 'sources')),
    *('guide/data/' + name + '.js' for name in (
        'model', 'stress', 'conditions', 'breakeven',
        'decision-page', 'stress-page', 'tax-page', 'conditions-page',
        'brief-page')),
}
