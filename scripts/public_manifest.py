"""Explicit review boundary for the public dashboard.

The published artifact is the real decision dashboard under site/, built from
the household's own figures rounded to the nearest $10 with Property A / Property B
placeholder labels. No personal data belongs here. Every packaged HTML page must
be listed so the publication gate can fail closed on missing, extra or altered files.
"""
from pathlib import Path

SITE_PAGES = (
    "black-swan", "briefing-sheet", "decision", "estate-tax", "executive-summary",
    "glossary", "inheritance", "operating-costs", "options", "plan", "properties",
    "questions", "questions-gate", "review", "san-francisco", "scenarios",
    "sources", "stress", "suggestions", "timeline", "verification",
)
SITE_DATA = (
    "costs", "gate", "history", "history-engine", "ledger", "model", "options",
    "questions", "scenarios", "sources", "stress", "suggestions",
)

# Root landing page plus the dashboard assets it depends on.
PUBLIC_FILES = {
    "index.html", "robots.txt", "assets/styles.css", "assets/app.js",
    *("site/" + name + ".html" for name in SITE_PAGES),
    *("site/data/" + name + ".js" for name in SITE_DATA),
}
