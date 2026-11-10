# Tino2

Inheritance decision research for two California homes (Property A, Cupertino 95014; Property B, San Francisco 94122), published with GitHub Pages:
https://wingbangboozle1-lang.github.io/Tino2/

No names, addresses or parcel numbers are stored here; dollar figures are rounded to the nearest $10.

| Site section | Path | Built by |
|---|---|---|
| Landing page and summary pages | `index.html`, `cupertino.html`, `san-francisco.html`, `inheritance.html`, `taxes.html`, `decision.html`, `flagged.html`, `sources.html`, `css/`, `docs/` | session arena-7c9c2cc4 |
| Second set of pages | `pages/`, `assets/` | session 64131d11 |
| Scenario dashboard (year-by-year tables, break-even model, estate-tax headroom, flagged list) | `dashboard/` (generated), `src/` (model and build script) | session 6ed42dca |

Rebuild and check the scenario dashboard:

```
python3 src/build.py          # writes dashboard/
python3 src/check_links.py    # dashboard only: links, source link on every row, rounding
python3 src/check_links.py .  # internal links across the whole site
```

Coordination between the parallel sessions is recorded in `COORDINATION.md`.
