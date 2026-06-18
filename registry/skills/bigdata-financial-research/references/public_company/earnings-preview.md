# Earnings Preview Workflow

Create a forward-looking earnings preview analyzing recent developments, industry trends, bull/bear cases, and key metrics to watch ahead of earnings releases.

## When to Use

- User asks: "Create an earnings preview for [company]"
- User asks: "Preview [company] earnings"
- User requests pre-earnings analysis
- User wants to know what to expect before earnings

**Optional depth:** Full reverse-DCF mechanics: [../equity-analysis/valuation/reverse-dcf.md](../equity-analysis/valuation/reverse-dcf.md). Full memo: [../../assets/templates/investment-memo.md](../../assets/templates/investment-memo.md).

## Workflow Steps

### Step 1: Identify the Company

Call `find_securities` with the company name to get the RavenPack entity_id.

### Step 2: Get Financial Baseline

Call `bigdata_company_tearsheet` with the entity_id to get:
- Recent quarterly performance trends
- Historical earnings surprises
- Analyst estimates for upcoming quarter
- Key financial metrics and margins
- Year-over-year comparisons
- **Positioning / sentiment fields when exposed** (e.g. sentiment scores, news/social metrics, ownership concentration, insider summary, options or short interest—capture whatever the tool returns; do not substitute analyst headlines for systematic data when numbers exist)

### Step 2b: Earnings quality quick screen (from tearsheet + quick search if needed)

Before building narratives, record a **credibility table** with a **forward-looking “watch for”** column (approximate if necessary; flag data gaps):

| Check | This period / trend | Red-flag threshold / note | **Watch for (next quarter / print)** |
|-------|---------------------|---------------------------|--------------------------------------|
| OCF / Net income | | Healthy often >0.8 sustained; <0.6 or widening gap → dig | e.g. further OCF/NI divergence; one-time boosts rolling off |
| DSO vs revenue growth | | DSO rising faster than revenue → recognition risk | e.g. DSO days vs rev growth; channel inventory mentions |
| GAAP vs non-GAAP EPS gap | | Large or widening gap → quality question | e.g. stock comp, restructuring, “adjusted” adds |

If tearsheet lacks a line, use `bigdata_search` for the latest quarter: "[Company] operating cash flow vs net income non-GAAP reconciliation".

Deeper framework: [../equity-analysis/financial-analysis/quality-of-earnings.md](../equity-analysis/financial-analysis/quality-of-earnings.md).

### Step 3: Identify the date of the next company's earnings call

Call `bigdata_events_calendar` with the entity_id to find out when the next earnings call is.

### Step 4: Search for recent developments, **legal/regulatory**, and positioning

Cast a **wide net** so material non-operational risks (e.g. court rulings, regulatory probes, tax disputes) are not missed. Use `bigdata_search` over the last **60–90 days** (extend if needed).

**Core company & industry:**
- "[Company Name] recent developments last 90 days"
- "[Company Name] product launches initiatives"
- "[Company Name] guidance commentary management"
- "[Company Name] analyst expectations earnings preview"
- "[Industry] trends headwinds tailwinds"

**Regulatory, legal, and policy (mandatory):**
- "[Company Name] lawsuit litigation court ruling settlement regulatory investigation last 90 days"
- "[Company Name] SEC investigation DOJ antitrust fine penalty Europe"
- "[Company Name] tax dispute regulatory approval compliance"

**Market positioning & flows (mandatory—fill structured table in output):**
- "[Company Name] insider buying selling Form 4 transactions last 90 days"
- "[Company Name] institutional ownership 13F changes fund flows"
- "[Company Name] short interest options put call ratio open interest" (or closest available)
- "[Company Name] RavenPack sentiment" OR "[Company Name] news sentiment score" (use what exists)

Conduct **at least 8–10 targeted queries** across the buckets above (merge redundant results). Then apply [analytical-frameworks.md](./analytical-frameworks.md): **which 2–3 themes actually matter** for this print and this stock, and document **EPIC** for each chosen driver.

### Step 4b: Sentiment & positioning (structured, not anecdotes)

Build a **table** for the output section (do not replace with a single Goldman note):

1. Pull every **numeric** sentiment / flow / positioning field from `bigdata_company_tearsheet`.  
2. Use Step 4 search results to **fill gaps** (insider trades, large holder moves, options/skew, quantified sentiment).  
3. If a cell is unavailable, write **“Not available in data”**—the section still appears.

FaVeS reference: [../equity-analysis/variant-perception/faves-framework.md](../equity-analysis/variant-perception/faves-framework.md).

### Step 5: What’s priced in + valuation cross-check

**Before** bull/bear narratives, answer what the **current price embeds** for this quarter and near-term trajectory. Use tearsheet multiples, consensus, and reverse-DCF-style reasoning (conceptual is fine—see [../equity-analysis/valuation/reverse-dcf.md](../equity-analysis/valuation/reverse-dcf.md)).

| Lens | Implied by market (price + multiples) | Consensus (estimates) | Your assessment |
|------|----------------------------------------|----------------------|-----------------|
| Growth (revenue / key volume) | | | |
| Margin level or expansion | | | |
| Beat magnitude / “whisper” vs published consensus | | | |

**Multiples sanity check (tearsheet):** Current **EV/EBITDA**, **P/E**, **FCF yield** (or sector-standard multiples) vs **~5-year range** or **peer median** when data allows. State whether valuation implies **optimism**, **consensus**, or **pessimism** relative to the setup.

### Step 6: Variant perception (FaVeS) + scenarios

**FaVeS (mandatory structure in output):**  
- **Fundamentals** — 2–3 KPIs that drive the quarter; where consensus could be wrong (link to bull/bear).  
- **Valuation** — tie to the **What’s priced in** table and **valuation cross-check** (do not repeat prose—cross-reference).  
- **Sentiment** — tie to the **Sentiment & positioning** table; state what is **priced in behaviorally** vs fundamentally.

**Scenario analysis (mandatory):** Build **Bull / Base / Bear** with:

- **Probability weights** that sum to ~100% (e.g. 30% / 50% / 20%)—justify briefly.  
- **Key assumptions** per scenario (growth, margin, one-timers, legal outcomes if relevant).  
- **Price level or range** per scenario (use spot, consensus PT band, or rough DCF/multiple bridge—**show assumptions**).  
- **Probability-weighted expected value** (e.g. EV price = Σ p×P; or expected upside % vs spot) with arithmetic shown.

Methodology: [../equity-analysis/variant-perception/thesis-construction.md](../equity-analysis/variant-perception/thesis-construction.md). Use [scripts/scenario_probability.py](../../scripts/scenario_probability.py) only if the user asks for scripted math; otherwise compute in prose/table.

### Step 7: Analyze and synthesize

Apply [analytical-frameworks.md](./analytical-frameworks.md): lead with **2–3 primary drivers** with **explicit EPIC** documentation; do not give equal weight to every search hit.

**Recent Developments and Initiatives** (prioritize material items only)
- Product launches or major announcements
- Strategic partnerships or acquisitions
- Operational improvements or challenges
- Geographic expansion or market share changes

**Industry Trends and Sector Dynamics**
- Macro trends affecting the industry
- Competitive landscape changes
- Supply chain or cost pressures
- Regulatory or policy impacts

**Bull case (FaVeS-style discipline)**

Each bull point must be **specific, measurable, defensible with evidence**, and **resolvable** over a sensible horizon—not generic tailwinds.

- Tie to **consensus line items** where possible (e.g. “consensus models X% growth in segment Y; channel evidence suggests Z%, ~$Nm revenue upside”).  
- Cite **source** (tearsheet, filing, search) per claim.

**Bear case (same discipline)**

- Quantify **downside to metrics** where possible (margin bps, revenue %, one-time vs recurring).

**Key Metrics to Watch**
- Most important KPIs for this company **this quarter**
- Metrics that could move the stock **given what’s priced in**
- Where **surprise volatility** is highest vs whisper/consensus

## Output Format

Add inline citation with Superscript Numbers [1], [2] immediately after claims and add a hyperlink pointing to the document url.

Structure the report as:

```
# Earnings Preview: [Company Name]
Upcoming Earnings: [Date if known]
Reporting for: [Quarter and Fiscal Year]

## Executive Summary
[2-3 sentences. **Number the thesis:** **Driver 1:** … **Driver 2:** … **Driver 3:** … (or fewer if only 2 pass EPIC). No generic headline recap.]

## Primary drivers — EPIC documentation (mandatory)
| Driver | E (material) | P (forecastable) | I (consensus blind spot) | C (your gap vs consensus) | Why prioritized vs. deprioritized factors |
|--------|--------------|------------------|--------------------------|---------------------------|---------------------------------------------|
| 1. [Name] | ✓/— / note | ✓/— / note | ✓/— / note | ✓/— / note | [one line] |
| 2. [Name] | | | | | |
| 3. [Name] | | | | | |

## Earnings quality quick screen
| Check | Observation | Implication | **Watch for (forward)** |
|-------|-------------|-------------|-------------------------|
| OCF / NI | | | |
| DSO trend | | | |
| GAAP vs non-GAAP | | | |

## Financial Expectations

### Consensus Estimates
- Revenue: [Estimate] (YoY growth: X%)
- EPS: [Estimate] (YoY change: X%)
- Operating Margin: [Estimate]
- [Other key metrics]

### Recent Performance Context
[Brief summary of last quarter's results and trends]

## Sentiment & positioning (mandatory structured table)
*Pull tearsheet fields first; use search to fill gaps. Use **“Not available”** if missing—do not omit the section.*

| Data type | Metric / fact | Source (tearsheet / search / filing) | As of |
|-----------|---------------|----------------------------------------|-------|
| Quantified news / social sentiment | e.g. score, percentile | | |
| Options / derivatives positioning | e.g. put/call, skew, OI | | |
| Short interest / borrow (if relevant) | | | |
| Institutional ownership / 13F changes | e.g. large holder Δ | | |
| Insider transactions | buys / sells / Form 4 | | |
| Sell-side posture | mean PT, # upgrades vs downgrades | | |

## Recent Developments and Initiatives
[Bulleted list of key developments since last earnings—including **legal/regulatory** items from search]
- [Development 1 with date and implication]
- [Development 2 with date and implication]

## Industry Trends and Sector Dynamics
[Analysis of broader industry context]
- [Trend 1 and impact on company]
- [Trend 2 and impact on company]

## What’s priced in
| Lens | Implied by market | Consensus | Your view |
|------|-------------------|-----------|-----------|
| Growth | | | |
| Margins | | | |
| Beat / miss bar | | | |

## Valuation cross-check
[Current EV/EBITDA, P/E, FCF yield vs history/peers; cheap/fair/rich vs embedded expectations]

## Variant perception (FaVeS) — mandatory structure
### Fundamentals
[2–3 KPIs that drive value this quarter; where consensus may be wrong—link to Drivers 1–3 and bull/bear below]

### Valuation
[2–4 sentences bridging **What’s priced in** + **Valuation cross-check**; state implied expectations in plain English]

### Sentiment
[2–4 sentences bridging **Sentiment & positioning** table; distinguish **positioning / flows** from single analyst calls]

## Bull Case: Drivers for Upside Surprise
1. [Specific, measurable bull point tied to consensus lines / KPIs]
   - Evidence: [source]
   - Impact: [quantify if possible]

2. [Same structure]

## Bear Case: Risks to Consensus
1. [Specific bear point; sustainable vs one-time where relevant—including legal/regulatory if material]
   - Evidence: [source]
   - Impact: [quantify if possible]

2. [Same structure]

## Scenario analysis (mandatory)
| Scenario | Probability (%) | Key assumptions | Price / value (range or PT) | Implied return vs spot |
|----------|-----------------|-----------------|-----------------------------|-------------------------|
| Bull | | | | |
| Base | | | | |
| Bear | | | | |
| **Total** | **~100%** | | | |

**Probability-weighted view:** [Show EV calculation—e.g. EV = p_Bull×P_Bull + p_Base×P_Base + p_Bear×P_Bear; state **expected upside/downside %** vs spot]

## Key Metrics to Watch
1. **[Metric 1]:** Why it matters and what to look for
2. **[Metric 2]:** Why it matters and what to look for
3. **[Metric 3]:** Why it matters and what to look for

## Management Guidance Focus Areas
[What to listen for in guidance and Q&A]
- [Topic 1]
- [Topic 2]

## Investment Implications
[Balanced risk/reward **given what’s priced in** and **scenario EV**]

**Closing (structured):** Net assessment: [Positive/Negative/Neutral] because [specific]; key risk: [X]; next catalyst: [Y].

## Sources
  ALWAYS include a "Sources" section at the end listing ALL documents referenced with:
   - Reference number matching the inline Superscript Numbers
   - Source name and Publication date (MMM DD, YYYY format) with a hyperlink to the URL
  
   **Example:**
   [1] (NVIDIA Q3 2026 Earnings Call - Nov 19, 2025)[https://www.benzinga.com/node/...]
   [2] (Benzinga - Nov 20, 2025)[https://www.benzinga.com/node/...]
   [3] (Yahoo! Finance - Jan 18, 2026)[https://finance.yahoo.com/news/...]


---

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

## Best Practices

- Apply [analytical-frameworks.md](./analytical-frameworks.md): **EPIC table** for each elevated driver; **FaVeS** section filled, not placeholder  
- **Scenario table** every time: probabilities, prices, **show EV math**  
- **Sentiment & positioning** as **structured data**—tearsheet first, then search; never replace with a single upgrade headline  
- **Regulatory/legal** queries every preview; surface material litigation or policy items in developments and bear case  
- **Watch for** column on quality screen—forward monitoring, not only backward checks  
- Build **what’s priced in** before bull/bear so cases are **relative to embedded expectations**  
- Balance bull and bear with **specificity** (numbers, sources, falsifiable claims)  
- Cite analyst consensus where available from tearsheet  
- Search 60–90 days (more if quiet); **trim noise** in prose while keeping **material** legal/positioning facts  

## Key Differences from Other Workflows

- **vs. Company Brief:** Preview is forward-looking; Brief is retrospective summary
- **vs. Earnings Digest:** Preview is before earnings; Digest is after earnings analysis
- **vs. Risk Assessment:** Preview focuses on near-term earnings drivers; Risk Assessment is comprehensive risk analysis  
- **vs. Valuation snapshot:** Preview is print-focused; [valuation-snapshot.md](./valuation-snapshot.md) answers “what is it worth” without an earnings event

## Example Queries to User

If earnings date unknown:
- "I don't have the exact earnings date yet. Shall I proceed with the preview based on recent developments and expectations?"

If limited recent news:
- "There's been limited news recently. Would you like me to expand the search period or focus on industry trends?"
