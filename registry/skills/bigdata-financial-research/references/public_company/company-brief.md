# Company Brief Workflow

Generate a comprehensive 30-day summary of recent developments for a specified company.

## When to Use

- User asks: "Create a brief for [company]"
- User asks: "What's happening with [company]"
- User requests company summary or recent developments
- User wants to know about recent news over the past month

**Optional depth:** For an **investment memo** or **variant-perception** framing after gathering facts, use [../../assets/templates/investment-memo.md](../../assets/templates/investment-memo.md) or [../equity-analysis/main.md](../equity-analysis/main.md).

## Workflow Steps

### Step 1: Identify the Company

Call `find_securities` with the company name to get the RavenPack entity_id.

### Step 2: Gather Business Context

Call `bigdata_company_tearsheet` with the entity_id to get:
- Company profile (sector, industry, description)
- Financial position
- Recent performance metrics

This context helps interpret the significance of news events.

### Step 2b: Competitive context (one pass)

Use `bigdata_search` at least once for industry structure and positioning:

- "[Company Name] competitive landscape market share"
- "[Company Name] vs competitors [Industry]"

You do **not** need a full Porter five-forces write-up; **2–4 sentences** on structure (concentration, pricing power, disruption risk) lift quality. Mental model: [../equity-analysis/competitive-analysis/porter-five-forces.md](../equity-analysis/competitive-analysis/porter-five-forces.md).

### Step 3: Search Recent News

Use `bigdata_search` to find news from the last 30 days. Use natural language queries that include the company name and temporal reference.

**Example search queries:**
- "[Company Name] news last 30 days"
- "[Company Name] recent developments"
- "[Company Name] earnings announcement"
- "[Company Name] product launches partnerships"
- "[Company Name] regulatory legal updates"
- "[Company Name] lawsuit litigation court ruling investigation settlement last 30 days" (catch material legal/regulatory items, not only earnings headlines)

Conduct multiple searches to cover different aspects:
- Financial developments
- Product/technology announcements
- Partnerships and M&A
- Regulatory and legal matters
- Management changes

### Step 4: Categorize Findings

Apply [analytical-frameworks.md](./analytical-frameworks.md): while categorizing, mark which items are **primary** (material to value or narrative) vs **secondary**.

Organize all findings into these categories:

**Financial Results**
- Earnings reports, revenue updates, profit/loss statements
- For each: Date, key metrics, performance vs. expectations

**Product/Tech Launches**
- New products, features, or technology announcements
- For each: Date, product details, market implications

**M&A and Partnerships**
- Acquisitions, mergers, strategic partnerships, investments
- For each: Date, parties involved, deal terms (if disclosed), strategic rationale

**Regulatory/Legal Updates**
- Legal proceedings, regulatory filings, compliance issues
- For each: Date, nature of issue, potential impact

**Management Changes**
- Executive appointments, departures, board changes
- For each: Date, personnel details, role significance

**Other Material Events**
- Any significant events not covered above
- For each: Date, event description, relevance

### Step 5: Investment implications (“so what”)

For each **material** categorized event, provide:
- **Date:** When the event occurred or was announced  
- **Facts:** Objective summary of what happened  
- **Investment implication:** Bullish / Bearish / Neutral — and **tie to value drivers** where possible (e.g. revenue run-rate, margin bps, multiple narrative, balance sheet, regulatory overhang **lifted or worsened**). Avoid generic labels: replace “bullish for stock” with “**could support X** (e.g. +$Nm revenue / +Ybps margin / de-risk [issue])” when inferable; if not quantifiable, state the **specific mechanism** (e.g. “reduces regulatory overhang on segment Z”).  

After categorization, **rank** the top **2–3** items for the overall period and reflect that ranking in the executive summary.

## Output Format

Add inline citation with Superscript Numbers [1], [2] immediately after claims and add a hyperlink pointing to the document url.

Structure the report as:

```
# Company Brief: [Company Name]
Period: [Date Range - Last 30 Days]

## Executive Summary
[2-3 sentences: **only the developments that matter most** for value or narrative this month—see [analytical-frameworks.md](./analytical-frameworks.md)]

## Competitive context
[Short industry/positioning snapshot]

## Financial Results
[Categorized findings with dates, facts, implications]

## Product/Tech Launches
[Categorized findings with dates, facts, implications]

## M&A and Partnerships
[Categorized findings with dates, facts, implications]

## Regulatory/Legal Updates
[Categorized findings with dates, facts, implications]

## Management Changes
[Categorized findings with dates, facts, implications]

## Other Material Events
[Categorized findings with dates, facts, implications]

## Overall Assessment
[Brief synthesis; **net tilt** and **why**]

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

- Read [analytical-frameworks.md](./analytical-frameworks.md); **do not** equal-weight every category in the narrative  
- Include **competitive context** (Step 2b)  
- Call `bigdata_search` multiple times (5–10 searches) for coverage, then **compress** into what matters  
- Use **“so what”** implications tied to mechanisms or rough value levers  
- If no events found in a category, note "No significant developments in this period"  
- Prioritize material events over minor announcements  


## Example Queries to User

If no significant developments:
- "I haven't found any significant developments for [Company] in the last 30 days. Would you like me to extend the search period or focus on specific topics?"
