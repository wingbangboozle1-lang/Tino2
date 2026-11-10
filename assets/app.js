/* Shared rendering helpers. All site assets are relative for GitHub Pages subpaths. */
(function () {
  const S = window.SOURCES;
  const M = window.MODEL;
  const path = location.pathname;
  const onHome = /(?:^|\/)index\.html$/.test(path) || /\/$/.test(path);
  const prefix = onHome ? "site/" : "";
  const home = onHome ? "index.html" : "../index.html";
  const current = onHome ? "home" : path.split("/").pop().replace(".html", "");
  const navItems = [
    ["home", home, "Overview"],
    ["properties", prefix + "properties.html", "Properties"],
    ["decision", prefix + "decision.html", "Decision"],
    ["inheritance", prefix + "inheritance.html", "Inheritance"],
    ["estate-tax", prefix + "estate-tax.html", "Estate tax"],
    ["san-francisco", prefix + "san-francisco.html", "SF property"],
    ["sources", prefix + "sources.html", "Sources"],
    ["review", prefix + "review.html", "Review"]
  ];
  const title = document.body.dataset.title || "Inheritance planning";
  document.title = title + " · Private-property dashboard";
  const header = document.createElement("header");
  header.className = "site-header";
  header.innerHTML = `<div class="container header-inner">
    <a class="brand" href="${home}" aria-label="Dashboard overview"><span class="brand-mark">H</span><span>Inheritance planning<small>Household records · 2026</small></span></a>
    <button class="menu-button" aria-label="Toggle navigation" aria-expanded="false">Menu</button>
    <nav class="nav" aria-label="Main navigation">${navItems.map(([id, href, label]) => `<a href="${href}" ${id === current ? 'class="active" aria-current="page"' : ""}>${label}${id === "review" ? " ⚑" : ""}</a>`).join("")}</nav>
  </div>`;
  document.body.prepend(header);
  const menu = header.querySelector(".menu-button");
  menu.addEventListener("click", () => {
    const nav = header.querySelector(".nav");
    const open = nav.classList.toggle("open");
    menu.setAttribute("aria-expanded", String(open));
  });
  const footerHost = document.querySelector("[data-footer]");
  if (footerHost) {
    footerHost.innerHTML = `<footer class="footer"><div class="container footer-inner"><div><strong>Privacy-safe planning dashboard</strong><br>Property labels are placeholders. No names, street addresses, parcel numbers, or account numbers are published.</div><div>Official-law review: 10 Nov 2026<br><a href="${prefix}sources.html">Source register</a> · <a href="${prefix}review.html">Flagged for review</a></div></div></footer>`;
  }
  window.UI = {
    source(key, label) {
      const source = S[key];
      if (!source) return '<span class="badge red">Missing source</span>';
      return `<a class="source-link" href="${source.url}" target="_blank" rel="noopener noreferrer">${label || source.agency} ↗</a><div class="tiny">${source.agency}</div>`;
    },
    money: M.fmtMoney,
    exact: M.fmtExact,
    pct: M.fmtPct,
    badge(text, kind = "") { return `<span class="badge ${kind}">${text}</span>`; },
    status(kind) {
      if (kind === "official") return UI.badge("Official source", "");
      if (kind === "input") return UI.badge("Household input", "neutral");
      if (kind === "derived") return UI.badge("Derived", "neutral");
      if (kind === "assumption") return UI.badge("Assumption", "gold");
      return UI.badge("Review", "red");
    },
    hero(eyebrow, heading, lead, actions = "") {
      return `<section class="hero compact"><div class="container"><div class="eyebrow">${eyebrow}</div><h1>${heading}</h1><p class="lead">${lead}</p>${actions ? `<div class="hero-actions">${actions}</div>` : ""}<div class="meta-row">${UI.badge("Dollar projections rounded to $10")}${UI.badge("Not legal, tax, or investment advice", "gold")}</div></div></section>`;
    },
    section(title, intro, body) {
      return `<section class="section"><div class="section-heading"><div><h2>${title}</h2>${intro ? `<p>${intro}</p>` : ""}</div></div>${body}</section>`;
    },
    options(id, values, selected) {
      return values.map(v => `<option value="${v[0]}" ${String(v[0]) === String(selected) ? "selected" : ""}>${v[1]}</option>`).join("");
    }
  };
})();
