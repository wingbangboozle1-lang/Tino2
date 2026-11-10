#!/usr/bin/env python3
"""Validate local navigation and source links in every published data-table row."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse
import sys

ROOT = Path(__file__).resolve().parents[1]
HTML_FILES = [ROOT / "index.html", *sorted((ROOT / "pages").glob("*.html"))]
# Government sources plus the official county assessor sites (which use .org).
OFFICIAL_HOSTS = {
    "irs.gov", "eitc.irs.gov", "boe.ca.gov", "leginfo.legislature.ca.gov",
    "sco.ca.gov", "ftb.ca.gov", "dre.ca.gov",
    "insurance.ca.gov", "cpuc.ca.gov", "bls.gov", "sec.gov",
    "congress.gov", "github.com",
}

class LinkAndTableParser(HTMLParser):
    def __init__(self, file_path: Path):
        super().__init__(convert_charrefs=True)
        self.file_path = file_path
        self.errors = []
        self.row = None
        self.cell = False
        self.cell_urls = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "a" and "href" in attrs:
            href = attrs["href"].strip()
            parsed = urlparse(href)
            if parsed.scheme in {"http", "https"}:
                host = (parsed.hostname or "").lower()
                if not any(host == allowed or host.endswith("." + allowed) for allowed in OFFICIAL_HOSTS):
                    self.errors.append(f"non-approved external host {host}: {href}")
                if self.row is not None:
                    self.cell_urls.append(href)
            elif href and not href.startswith("#"):
                target_part = href.split("#", 1)[0].split("?", 1)[0]
                target = (self.file_path.parent / target_part).resolve()
                if target_part and not target.exists():
                    self.errors.append(f"broken local link: {href}")
        elif tag == "tr":
            self.row = {"cells": 0, "urls": []}
        elif tag in {"td", "th"} and self.row is not None:
            self.cell = tag == "td"
            self.cell_urls = []
            if self.cell:
                self.row["cells"] += 1
        elif tag == "a" and self.row is not None and "href" not in attrs:
            pass

    def handle_endtag(self, tag):
        if tag == "a" and self.row is not None and self.cell:
            self.row["urls"].extend(self.cell_urls)
            self.cell_urls = []
        elif tag in {"td", "th"}:
            self.cell = False
        elif tag == "tr" and self.row is not None:
            if self.row["cells"] and not self.row["urls"]:
                self.errors.append("table data row has no external source link")
            elif self.row["cells"] and not any(self._official(url) for url in self.row["urls"]):
                self.errors.append("table data row has no whitelisted official source link")
            self.row = None
            self.cell = False

    @staticmethod
    def _official(url):
        host = (urlparse(url).hostname or "").lower()
        return any(host == allowed or host.endswith("." + allowed) for allowed in OFFICIAL_HOSTS)


def main():
    failed = False
    for file_path in HTML_FILES:
        parser = LinkAndTableParser(file_path)
        parser.feed(file_path.read_text(encoding="utf-8"))
        parser.close()
        if parser.errors:
            failed = True
            for error in parser.errors:
                print(f"FAIL {file_path.relative_to(ROOT)}: {error}")
        else:
            print(f"PASS {file_path.relative_to(ROOT)}")
    if failed:
        return 1
    print(f"Validated {len(HTML_FILES)} pages; every data-table row has an official source link and local links resolve.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
