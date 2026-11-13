"""Explicit review boundary for the public dashboard. No personal data belongs here."""
PUBLIC_FILES = {
    'index.html', 'robots.txt', 'assets/safe.css', 'assets/safe.js',
    *('guide/' + name + '.html' for name in (
        'requirements', 'decision', 'stress', 'property', 'tax', 'inheritance',
        'questions', 'suggestions', 'review', 'sources', 'method')),
    *('guide/data/' + name + '.js' for name in (
        'model', 'stats', 'decision-page', 'property-page', 'summary-page')),
}
