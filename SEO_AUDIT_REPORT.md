# Game Guide Club — Content & SEO Audit Report

**Date:** 2026-07-03
**Site:** https://game-guide.club
**Repository:** /home/hermes/game-guide/
**Baseline comparison:** https://farminggames.help (/home/hermes/farminggames/)

---

## 1. Site Overview

| Metric | Value |
|--------|-------|
| Total `.md` files | 58 |
| Total word count (all .md) | ~100,848 |
| Index page word count | 601 |
| Games covered | 9 (Satisfactory, Factorio, DSP, Timberborn, Shapez 2, Valheim, Enshrouded, V Rising, Sons of the Forest, Grounded) |
| Interactive tools | 6 (Production Calc, Power Planner, Factory Planner, Game Map, Boss Tracker) |
| Avg words per article | ~1,738 |

### Word Count by Game

| Game | Words | Pages | Avg/page |
|------|-------|-------|----------|
| Timberborn | 17,358 | 8 | 2,170 |
| Satisfactory | 15,428 | 7 | 2,204 |
| Factorio | 10,746 | 6 | 1,791 |
| Dyson Sphere | 8,781 | 5 | 1,756 |
| Shapez 2 | 8,037 | 4 | 2,009 |
| V Rising | 7,362 | 5 | 1,472 |
| Sons of the Forest | 7,085 | 4 | 1,771 |
| Tools | 6,194 | 6 | 1,032 |
| Grounded | 6,182 | 3 | 2,061 |
| Enshrouded | 6,025 | 4 | 1,506 |
| Valheim | 5,665 | 3 | 1,888 |
| Game Comparison | 1,261 | 1 | 1,261 |
| Feedback | 123 | 1 | 123 |

### Top 10 Longest Articles

| Article | Words |
|---------|-------|
| shapez2/buildings.md | 3,692 |
| valheim/boss-strategies.md | 3,143 |
| timberborn/food.md | 3,000 |
| satisfactory/power.md | 2,979 |
| timberborn/buildings.md | 2,887 |
| timberborn/districts.md | 2,813 |
| timberborn/drought.md | 2,641 |
| sons-forest/caves-walkthrough.md | 2,607 |
| satisfactory/lines.md | 2,589 |
| factorio/rail-system.md | 2,577 |

---

## 2. SEO Configuration (mkdocs.yml)

### ✅ Strengths

- **`site_url`** set correctly → `https://game-guide.club`
- **`site_description`** present (~120 chars, good length)
- **`site_author`** set
- **Google Analytics** configured (`G-NENYIKVWHL`)
- **`generator: false`** hides "MkDocs" branding
- **Minify plugin** active (HTML, JS, CSS — all with `cache_safe: true`)
- **Git revision dates** enabled (timeago)
- **`glightbox`** for image lightbox (UX signal)
- **`redirects`** plugin set up for legacy URLs (timberborn.md, factorio.md, etc.)
- **Canonical URL** renders correctly via theme
- **Search** with highlight + suggest enabled
- **Navigation features**: tabs, sticky, sections, path, top, header autohide
- **Content code copy** enabled
- **robots.txt** blocks AI crawlers (GPTBot, ClaudeBot, etc.) while allowing Googlebot — asset for content protection

### ⚠️ Issues

1. **No JSON-LD / schema.org markup** — farminggames.help has `application/ld+json` (WebPage schema) on its homepage; game-guide.club has none on any page.
2. **No `site_name` reused in OG tags** — the OG title is hardcoded as "Factory Game Guides — game-guide.club" rather than pulling from `site_name` or per-page frontmatter.
3. **No `site_description` in OG tags** — OG description is a separate hardcoded string, not the global `site_description`.
4. **No social links** in `extra` (farminggames has a GitHub social icon).
5. **No table sorting with TOC** — Tables exist but no `sortable` extension enabled.
6. **Meta description on home page in HTML is correct** (verified live).
7. **Hreflang**: Not configured (likely fine for single-language EN site).

---

## 3. Homepage (docs/index.md) Content Quality

### ✅ Strengths

- **Frontmatter**: title, description, date all present
- **Visual hero section** with stats (45 guides, 6 tools, 9 games, 2 categories)
- **Two clear categories**: Factory Automation & Survival & Building
- **Game cards** with studio names, descriptions, and quick-link buttons
- **CTAs**: "View factory game comparison →" link, internal links to game sections
- **Tagline + search bar** (decorative but good UX)
- **Affiliate disclosure** in footer (legal compliance)
- **Overall tone**: friendly, gamer-oriented, emoji-rich
- **Update timestamp** shown via git-revision-date

### ⚠️ Issues

1. **Search bar HTML is static/decorative** — the `<input>` and `<button>` are not wired to MkDocs search; they're just visual elements. This could confuse users who try to use it.
2. **Stats are hardcoded** (45 guides, 6 tools, 9 games, 2 categories) — will drift out of sync as content grows.
3. **No "latest articles" section** — farminggames.help has a "Latest Guides" section; game-guide.club homepage lists all games statically without showing what's new.
4. **No sidebar TOC links** on homepage — just "Factory Automation" and "Survival & Building" anchors.
5. **Article previews / recent updates** — missing. Users land on a static listing with no sense of freshness.

---

## 4. OG Tags & Social (Live Check)

Extracted live from `https://game-guide.club/`:

```html
<meta description="Blueprints, calculators & guides for factory automation and survival games — Satisfactory, Factorio, Dyson Sphere Program, Valheim, and more.">
<link rel="canonical" href="https://game-guide.club/">
<meta property="og:title" content="Factory Game Guides — game-guide.club">
<meta property="og:description" content="Complete guides, interactive calculators, and tools for Satisfactory, Factorio, Dyson Sphere Program, Timberborn, and Shapez 2.">
<meta property="og:url" content="https://game-guide.club">
<meta property="og:image" content="https://game-guide.club/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:type" content="website">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Factory Game Guides — game-guide.club">
<meta name="twitter:description" content="Guides, calculators & tools for factory automation games.">
<meta name="twitter:image" content="https://game-guide.club/assets/img/og-image.png">
```

### ✅ Strengths

- All OG tags present (title, description, url, image, type)
- Twitter card configured (summary_large_image)
- OG image dimensions specified (1200x630 — optimal)
- Canonical URL correct
- Meta description matches frontmatter

### ⚠️ Issues

1. **OG tags are hardcoded in overrides/main.html** — every page shows the same OG title/description regardless of page content. Needs dynamic per-page OG tags.
2. **OG image alt text** — missing `og:image:alt` tag.
3. **OG locale** — missing `og:locale` (farminggames.help has `en_US`).
4. **OG site_name** — missing `og:site_name` (farminggames.help has this).
5. **No JSON-LD structured data** — farminggames.help has it; game-guide.club doesn't.

---

## 5. H1 Headings & Descriptions

All 58 pages were checked:

### ✅ H1 Coverage

- Every page has a single H1 heading ✓
- H1s are generally descriptive with game name + topic
- Emojis used consistently in H1s for visual appeal
- No duplicate H1s across the site

### ✅ Meta Descriptions

- **57 of 58 pages** have frontmatter `description:` ✓
- Descriptions are substantive (avg ~120–160 chars), contain keywords
- No generic/empty descriptions

### ⚠️ Issues

1. **`docs/vrising/redeem-codes.md`** — completely missing frontmatter `description:` meta tag. This is a thin page (311 words) with no SEO metadata.
2. **`docs/satisfactory/tiers.md`** — the frontmatter `description` field contains `"Last updated: June 2026 | Game version: 1.0+"` which is NOT a proper SEO description. This should be a real meta description.
3. **3 nav items have no emoji** — "Tiers" and "Parts" under Satisfactory, and "Buildings" under Shapez 2 use plain text while all others use emoji prefixes. Inconsistency.
4. **H1s missing target keywords** — none of the H1s include "blueprint", "calculator", or "guide database" — key search terms for this niche.

---

## 6. Technical SEO

| Check | Status |
|-------|--------|
| Sitemap.xml | ✅ Present, 58 URLs |
| robots.txt | ✅ Present, well-configured |
| Canonical tags | ✅ On every page |
| SSL/HTTPS | ✅ (Cloudflare) |
| Page speed | ✅ Minified assets (HTML/JS/CSS) |
| Mobile responsive | ✅ Material theme | 
| Favicon | ✅ |
| 404 page | ⚠️ Not customized (uses default MkDocs 404) |
| Hreflang | ❌ Not configured (acceptable for EN-only) |
| JSON-LD/Schema | ❌ Not present on any page |
| Breadcrumbs | ✅ (via `navigation.path`) |
| Performance budget | ⚠️ 7 vendor JS libs loaded (jQuery, DataTables, 4 tool scripts, glightbox) |

---

## 7. Comparison with farminggames.help

| Feature | game-guide.club | farminggames.help |
|---------|----------------|-------------------|
| Language | English | English |
| Pages | 58 .md files | ~200+ pages |
| JSON-LD Schema | ❌ Missing | ✅ WebPage schema |
| OG Tags | ✅ Hardcoded in overrides | ✅ Theme-native (in head) |
| OG locale | ❌ Missing | ✅ `og:locale: en_US` |
| OG site_name | ❌ Missing | ✅ `og:site_name: Farming Games Help` |
| Social links | ❌ None | ✅ GitHub link in footer |
| Latest articles | ❌ Static cards | ✅ Dynamic preview cards |
| Article previews | ❌ No thumbnails | ✅ Article cards with date & read time |
| 404 page | ❌ Default | ❌ Default |
| Analytics | ✅ Google (G-NENYIKVWHL) | ✅ Google (G-YSB3RE462B) |
| Minify/compress | ✅ (plugin) | ❌ Not configured |
| Git dates | ✅ | ❌ Not configured |
| Redirects | ✅ Legacy redirects | ❌ Not configured |
| AI crawler blocks | ✅ robots.txt blocks GPTBot/ClaudeBot | ❌ Default robots.txt |
| Custom OG per page | ❌ Same for all pages | ❌ Same for all pages |
| Affiliate disclosure | ✅ In footer | ✅ In footer |
| Generator hidden | ✅ | ✅ |

---

## 8. Critical Issues (Fix Priority)

### 🔴 P1 — Must Fix

1. **`docs/vrising/redeem-codes.md` missing description** — Add frontmatter `description:` field immediately. This page has 0 SEO metadata.
2. **`docs/satisfactory/tiers.md` wrong description** — Replace with a proper keyword-rich meta description.
3. **Missing JSON-LD schema.org markup** — Add `WebPage` and `WebSite` schema to the base template. farminggames has it; without it game-guide.club loses rich snippet eligibility.

### 🟠 P2 — Should Fix

4. **OG tags hardcoded per-page** — Override `extrahead` to load per-page title/description from frontmatter instead of the same string for every page. Currently sharing on social media always says "Factory Game Guides — game-guide.club" regardless of which page is shared.
5. **Missing `og:locale` and `og:site_name`** — Add to overrides/main.html.
6. **No "latest articles" section on homepage** — Add to improve freshness signal.

### 🟡 P3 — Nice to Have

7. **Static search bar on homepage** — Either wire it to MkDocs search or remove it.
8. **Hardcoded stats on homepage** — Should be programmatically generated.
9. **Inconsistent emoji in nav** — "Tiers", "Parts", "Buildings" items missing emoji prefixes.
10. **No custom 404 page** — Add a custom 404 with search and popular links.
11. **No social links in footer** — GitHub or Discord links for community building.

---

## 9. Content Quality Summary

| Metric | Score | Notes |
|--------|-------|-------|
| Article depth | ⭐⭐⭐⭐ | Avg ~1,738 words, substantive guides with data tables |
| SEO metadata | ⭐⭐⭐ | 57/58 pages have descriptions; missing schema |
| Readability | ⭐⭐⭐⭐ | Good structure (H2, tables, lists, admonitions) |
| Visual content | ⭐⭐⭐ | Data tables + lightbox images but no diagrams/charts |
| Internal linking | ⭐⭐⭐ | Game pages link to each other, but limited cross-linking |
| Freshness | ⭐⭐⭐ | Git dates visible; some pages stale |
| Mobile UX | ⭐⭐⭐⭐ | Material theme, responsive by default |
| Accessibility | ⭐⭐⭐ | Emoji as icons may not have alt text; skip-to-content exists |

---

## 10. Recommendations

### Quick Wins (this week)
1. Add `description:` frontmatter to `vrising/redeem-codes.md`
2. Fix `satisfactory/tiers.md` description
3. Add `og:locale` and `og:site_name` to `overrides/main.html`
4. Fix emoji inconsistency in nav for "Tiers", "Parts", "Buildings"

### Short-term (1-2 weeks)
5. Add JSON-LD schema to base template (`WebSite` + `WebPage`)
6. Make OG tags dynamic per-page using page frontmatter
7. Add "latest articles" section to homepage with dates
8. Write a custom 404 page

### Medium-term (1 month)
9. Add social links to footer (GitHub, Discord)
10. Replace hardcoded homepage stats with dynamic counts
11. Add structured data for tool pages (e.g., `SoftwareApplication` schema for calculators)
12. Audit thin content pages (< 500 words) for expansion

---

*Generated by Hermes Agent content audit — 2026-07-03*
