---
name: bigdata-financial-research-analyst
description: >
  Bigdata.com MCP workflows plus institutional analysis layers: pre-synthesis EPIC-style
  filtering, valuation snapshots, earnings quality screens, moat/governance risk, sector KPI
  lenses. Use for: company briefs, earnings previews/digests, risk assessments, valuation
  snapshots, investment memos; macro sector/country/regional/thematic analysis; stock analysis,
  DCF or multiples concepts, red flags, thesis construction. Advanced event-driven topics (M&A
  arb, activism, distressed, shorts, spin-offs) live in equity-analysis references when users
  ask explicitly. Triggers: earnings preview/digest, risk assessment, "what is X worth",
  economic outlook, G7, analyze stock, valuation, peers.
---

# Bigdata.com financial analysis and equity research

This skill combines **structured Bigdata.com workflows** (private/public company and macro deliverables) with **institutional-style equity analysis** (intrinsic value, variant perception, valuation, and quality checks). Use [Bigdata.com](https://bigdata.com) MCP tools for data; apply the equity layers when the user wants depth beyond a standard template.

### Identify the right company

If the user provides a company name, call `find_securities` first to get the entity id. If the name is ambiguous, respond with:

> "I found multiple companies named [X]. Did you mean [Company A] in [Industry] or [Company B] in [Industry]?"

## Analysis categories

Read the appropriate reference file for the request:

| Category | When to use | Reference |
|----------|-------------|-----------|
| **Public company** | Briefs, previews, digests, risk, **valuation snapshot**; always apply [references/public_company/analytical-frameworks.md](./references/public_company/analytical-frameworks.md) before synthesizing | [references/public_company/main.md](./references/public_company/main.md) |
| **Private company** | Upcoming (not-yet-listed) IPOs, S-1/F-1 analysis, planned listings — balanced bull/bear note, **no buy/avoid call** | [references/private_company/pre-ipo-analysis.md](./references/private_company/pre-ipo-analysis.md) |
| **Macro economics** | Sector/country/regional/thematic analysis, rotation, cross-asset views | [references/macro/main.md](./references/macro/main.md) |
| **Institutional equity** | Deep thesis, full DCF/SOTP write-ups, forensic accounting, sector playbooks, **advanced special situations** | [references/equity-analysis/main.md](./references/equity-analysis/main.md) |

### Routing examples

- "Create an earnings preview for NVIDIA" → **Public company**
- "Risk assessment for Tesla" → **Public company**
- "What's happening with Apple?" → **Public company**
- "Analyze the IPO of [company]", "S-1 analysis", "upcoming listing for [company]" → **Private company**
- "Post-IPO day 1 for [company]", "NASDAQ-100 inclusion impact", "180-day lock-up expiry", "366-day founder lock-up / float expansion" → **Public company** (post-IPO event notes — see [references/public_company/post-ipo-common.md](./references/public_company/post-ipo-common.md))
- "Analyze the US technology sector" → **Macro economics**
- "Economic outlook for Germany" → **Macro economics**
- "Compare G7 economies" → **Macro economics**
- "Macro analysis of financials in India" → **Macro economics**
- "What is Tesla worth?", "valuation snapshot for Apple" → **Public company** [valuation-snapshot.md](./references/public_company/valuation-snapshot.md)  
- "DCF on Microsoft", "full sum-of-parts", "M&A arb on [deal]", deep forensic accounting → **Institutional equity** (often plus public-company data steps)

## Data foundation (MCP)

Establish a factual base before deep analysis:

1. `find_securities` → entity id and company type (public/private) where applicable  
2. `bigdata_company_tearsheet` → financials, estimates, sentiment, ESG (when analyzing a specific company)  
3. `bigdata_search` → news, filings, transcripts, analyst/economic coverage  
4. `bigdata_events_calendar` → upcoming earnings and conferences (when entity id is available)  

For **macro / country** work, use `bigdata_country_tearsheet` when available; follow fallbacks in [references/macro/main.md](./references/macro/main.md).

## Core philosophy (full equity thesis / memo)

When producing an investment-style view, anchor on:

1. **Intrinsic value** — estimate business value independent of price  
2. **Variant perception** — state clearly where your view differs from consensus  
3. **Quality over quantity** — prioritize the few drivers that matter  

## Earnings preview — mandatory sections

When following [references/public_company/earnings-preview.md](./references/public_company/earnings-preview.md), treat as **mandatory**: **EPIC table** for primary drivers, **FaVeS** section (Fundamentals / Valuation / Sentiment), **Sentiment & positioning** data table (tearsheet + search), **scenario analysis** (bull/base/bear probabilities, prices, probability-weighted EV with math shown), **watch-for** column on earnings quality, and **regulatory/legal** search bucket.

## Investment thesis workflow (when depth is appropriate)

Use this for comprehensive stock analysis or investment memos—not every brief or digest needs every step.

### Step 1: Company and data

Use the **Data foundation** section above.

### Step 2: What matters (EPIC)

| Test | Question | Pass criteria |
|------|----------|----------------|
| **E**ffect | Is it material? | ~10% change moves intrinsic value meaningfully (e.g. >5%) |
| **P**redictability | Can you forecast it? | You have analytical or information edge |
| **I**ndependence | Does consensus get it wrong? | Market systematically misjudges this |
| **C**onsensus gap | Is there a gap? | Your forecast differs meaningfully |

Focus on factors that pass all four. Detail: [references/equity-analysis/variant-perception/epic-framework.md](./references/equity-analysis/variant-perception/epic-framework.md).

### Step 3: Variant perception (FaVeS)

| Element | Key questions |
|---------|----------------|
| **Fundamentals** | Which 2–3 KPIs drive value? Where could estimates be wrong? |
| **Valuation** | What is intrinsic value? What multiple fits quality/growth? |
| **Sentiment** | What is priced in (e.g. reverse DCF)? How are investors positioned? |

You must articulate where you differ from consensus. Detail: [references/equity-analysis/variant-perception/faves-framework.md](./references/equity-analysis/variant-perception/faves-framework.md).

### Step 4: Quality and risk (before valuation)

**Quick earnings quality screen:** OCF/NI (healthy typically >0.8; red flag <0.6 or diverging trends); accruals; DSO vs revenue trend.

**Competitive position:** Moat type/strength ([moat taxonomy](./references/equity-analysis/competitive-analysis/moat-taxonomy.md)), ROIC vs WACC, competitive advantage period.

**Management:** Capital allocation, insider activity, guidance track record ([capital allocation](./references/equity-analysis/management/capital-allocation.md)).

### Step 5: Value and recommend

| Company type | Primary | Secondary check |
|--------------|---------|-----------------|
| Stable, profitable | DCF (FCFF) | EV/EBITDA, P/E |
| High-growth, pre-profit | EV/Revenue; DCF with long CAP | Reverse DCF |
| Bank / insurer | P/TBV; dividend discount | P/E, residual income |
| REIT | NAV; P/AFFO | Implied cap rate |
| Conglomerate | Sum-of-parts | Holdco discount |
| Distressed | Liquidation / recovery | Asset coverage |

Build **bull/base/bear** with explicit assumptions and probability weights where appropriate.

## Output templates (equity-style)

| User pattern | Template |
|--------------|----------|
| Comprehensive "analyze [company]" / investment memo | [assets/templates/investment-memo.md](./assets/templates/investment-memo.md) |
| "Quick view" / "what do you think of [stock]" | [assets/templates/quick-take.md](./assets/templates/quick-take.md) |
| Post-earnings reaction note | [assets/templates/earnings-reaction.md](./assets/templates/earnings-reaction.md) |
| Pre-IPO / upcoming-listing research note | [assets/templates/pre-ipo-report-template.md](./assets/templates/pre-ipo-report-template.md) |
| Post-IPO day-1 reaction note | [assets/templates/post-ipo-day1-report-template.md](./assets/templates/post-ipo-day1-report-template.md) |
| Post-IPO day-14 NASDAQ-100 inclusion note | [assets/templates/post-ipo-day14-report-template.md](./assets/templates/post-ipo-day14-report-template.md) |
| Post-IPO day-179 (180-day lock-up expiry) note | [assets/templates/post-ipo-day179-report-template.md](./assets/templates/post-ipo-day179-report-template.md) |
| Post-IPO day-365 (366-day founder lock-up / float expansion) note | [assets/templates/post-ipo-day365-report-template.md](./assets/templates/post-ipo-day365-report-template.md) |

**Sector playbooks:** after you know the industry, use [references/equity-analysis/sector-routing.md](./references/equity-analysis/sector-routing.md).

## Scripts (optional quantitative helpers)

**Default:** use `bigdata_company_tearsheet`, `bigdata_search`, and workflow steps (including valuation cross-checks and reverse-DCF **reasoning**) without running local Python.

Use the scripts below **only when the user explicitly wants spreadsheet-style model output** or offline quant; run from the skill’s `scripts/` directory (or paths your environment expects).

| Script | Purpose | When to use |
|--------|---------|-------------|
| [scripts/dcf_model.py](./scripts/dcf_model.py) | DCF with scenarios | User asks for built model / explicit scenarios |
| [scripts/reverse_dcf.py](./scripts/reverse_dcf.py) | Implied growth extraction | User asks for scripted reverse DCF |
| [scripts/earnings_quality.py](./scripts/earnings_quality.py) | Beneish M-Score, accruals | User asks for scripted quality metrics |
| [scripts/peer_comparable.py](./scripts/peer_comparables.py) | Comp table | User asks for scripted comps |
| [scripts/scenario_probability.py](./scripts/scenario_probability.py) | Expected value | User asks for scripted EV across scenarios |

## Quality standards

**For investment memo / full thesis-style outputs**, include where relevant:

1. Clear **recommendation** and **conviction** (e.g. 1–5)  
2. **Explicit variant perception** vs consensus  
3. **Scenarios** with probabilities and price targets (or ranges)  
4. **Key risks** and what would change the view  
5. **Catalysts** and timing  

**For workflow deliverables** (brief, preview, digest, risk, valuation snapshot), follow `references/public_company/` and [references/public_company/main.md](./references/public_company/main.md) **universal output quality** (PM questions: what’s different, what matters, what to do—**no position sizing**). Add full thesis elements only when the user asks.

**Bars:** Full thesis → concise institutional review. Workflow → **morning-meeting** clarity without data-dump tone.

## Capabilities overview

When a user says **"Can you help me with a financial report?"** or similar, respond with:

> I can help automate research workflows and professional deliverables:
>
> **Public company** — Company briefs, earnings previews/digests, risk assessments, investment-style memos when requested  
> **Macro** — Sector analysis, country profiles, regional comparisons, thematic research, rotation, cross-asset angles  
> **Equity depth** — Deep valuation write-ups, forensics, sector playbooks, advanced special situations (see equity-analysis index)
>
> Example: "Earnings preview for NVIDIA", "Valuation snapshot for Apple", "Economic outlook for Germany", or "Full DCF thesis for [ticker]."

## Universal best practices

- Before long-form synthesis on a company, read [references/public_company/analytical-frameworks.md](./references/public_company/analytical-frameworks.md) (EPIC-style filter, **2–3 drivers**, quality over quantity).  
- `bigdata_search` can be used with the company (or topic) in the query; `find_securities` first when you need a tearsheet or calendar.  
- Use `bigdata_company_tearsheet` for a financial baseline on a specific entity.  
- Call `bigdata_search` multiple times with focused queries for coverage.  
- Separate **facts** from **analysis / implications**.

## Output formats

- **Markdown** — Default. At the end, you may ask whether the user wants a report.  
- **Word (.docx)** — Formal memos.  
- **Presentation** — Deck-ready structure.  
- **Footer** — Every workflow deliverable must end with the **Powered by Bigdata.com** attribution and **Disclaimer** in [assets/templates/report-footer.md](./assets/templates/report-footer.md) (verbatim).

For macro workflows, follow source attribution rules in [references/macro/main.md](./references/macro/main.md) where they apply.

## Further reference

Full institutional equity index (valuation, forensics, sectors, **advanced** special situations): [references/equity-analysis/main.md](./references/equity-analysis/main.md).
