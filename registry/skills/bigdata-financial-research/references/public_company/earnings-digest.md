# Earnings Digest Workflow

Analyze the latest earnings results with detailed breakdown of revenue, margins, segment performance, management guidance, and surprises versus expectations.

## When to Use

- User asks: "Analyze [company] earnings"
- User asks: "Create earnings digest for [company]"
- User requests post-earnings analysis
- User wants breakdown of latest quarterly results

**Optional depth:** For **earnings quality** or **red flag** angles on the print, see [../equity-analysis/financial-analysis/quality-of-earnings.md](../equity-analysis/financial-analysis/quality-of-earnings.md) and [../../assets/templates/earnings-reaction.md](../../assets/templates/earnings-reaction.md).

## Workflow Steps

### Step 1: Identify the Company

Call `find_securities` with the company name to get the RavenPack entity_id.

### Step 2: Get Financial Data

Call `bigdata_company_tearsheet` with the entity_id to get:
- Latest quarterly results (most recent Q)
- Analyst estimates and consensus
- Latest earnings surprise data
- Historical trends for comparison
- Segment performance breakdown
- **Sentiment, ownership, insider, options/short** fields when the tearsheet exposes them (for the structured **Sentiment & positioning** table)

This provides the quantitative foundation for analysis.

### Step 3: Identify the date of the last company's earnings call

Call `bigdata_events_calendar` with the entity_id to find out when the most recent earnings call was.

### Step 4: Search for Earnings Materials

Use `bigdata_search` to find earnings-related content:

**Recommended searches:**
- "[Company Name] earnings results Q[X] [Fiscal Year]"
- "[Company Name] earnings transcript conference call"
- "[Company Name] analyst reactions upgrades downgrades"
- "[Company Name] guidance outlook management commentary"
- "[Company Name] earnings surprise beat miss"
- "[Company Name] lawsuit litigation regulatory ruling investigation" (post-print legal overhang)

Conduct 5–7 targeted searches covering:
- Official earnings release and metrics
- Earnings call transcript highlights
- Analyst reactions and rating changes
- Management guidance and commentary
- Market reaction and investor sentiment

### Step 5: Synthesize Findings

Before the full write-up, apply [analytical-frameworks.md](./analytical-frameworks.md): **2–3 factors** that dominate the forward debate after this print.

Create comprehensive analysis organized by:

**Revenue and Margin Analysis**
- Total revenue vs. consensus
- Revenue by segment/geography
- Gross margin, operating margin trends
- YoY and QoQ comparisons

**Operating Metrics and Segment Performance**
- Key operational KPIs
- Segment-level results and trends
- Customer/user metrics if applicable
- Geographic performance

**Management Guidance and Commentary**
- Forward guidance for next quarter/full year
- Strategic initiatives discussed
- Market conditions commentary
- Capital allocation priorities

**Cash Flow and Balance Sheet**
- Operating cash flow trends
- Free cash flow generation
- Balance sheet strength/concerns
- Capital expenditures and investments

**Surprises vs. Expectations**
- Where company beat/missed vs. consensus
- **Magnitude framing:** approximate **standard deviations** vs typical surprise volatility if data allows; label beat/miss **sustainable vs one-time** (revenue volume/price vs buyback/tax/timing)  
- Unexpected positives or negatives
- Changes from prior guidance
- Market reaction drivers

**Thesis check (forward-looking)**

Even without a prior user thesis, frame:

- **For bulls:** this quarter **[strengthened / weakened / left unchanged]** the bull case because [specific evidence].  
- **For bears:** this quarter **[strengthened / weakened / left unchanged]** the bear case because [specific evidence].

(Optional: if the user supplied a thesis, use **Intact / Strengthened / Weakened / Broken** explicitly—see [../../assets/templates/earnings-reaction.md](../../assets/templates/earnings-reaction.md).)

**Quality signals (tearsheet + quarter data)**

| Signal | This quarter | Prior quarter | Trend / note | **Watch for (forward)** |
|--------|--------------|---------------|--------------|-------------------------|
| OCF vs net income | | | | |
| DSO | | | | |
| Inventory (if material) | | | | |
| Guidance vs actual (credibility) | | | | |

**Sentiment & positioning (structured)**

Same discipline as earnings preview: table with **quantified sentiment** (if available), **insider**, **13F / flows**, **options/short** from tearsheet + search; use **Not available** if missing.

**Scenario refresh (post-print, recommended)**

| Scenario | Probability (%) | Updated assumption vs pre-print | Price / range | Implied return |
|----------|-----------------|----------------------------------|---------------|----------------|
| Bull | | | | |
| Base | | | | |
| Bear | | | | |

**Probability-weighted view:** [EV or expected upside %—show math]

**Valuation cross-check**

From tearsheet: **EV/EBITDA, P/E, FCF yield** vs recent history and peers; does the reaction **fit** the surprise and guidance?

## Output Format

Add inline citation with Superscript Numbers [1], [2] immediately after claims and add a hyperlink pointing to the document url.

Structure the report as:

```
# Earnings Digest: [Company Name]
Period: [Quarter and Fiscal Year]
Reported: [Date]

## Executive Summary
[2-3 sentences: **headline result + what changed for the bull/bear debate + what’s priced in next**]

## Thesis check
### Bull narrative
- **Status:** Strengthened / Weakened / Unchanged  
- **Because:** [evidence]

### Bear narrative
- **Status:** Strengthened / Weakened / Unchanged  
- **Because:** [evidence]

## Quality signals
| Signal | This Q | Prior Q | Trend | **Watch for** |
|--------|--------|---------|-------|---------------|
| OCF vs NI | | | | |
| DSO | | | | |
| Inventory | | | | |
| Guidance credibility | | | | |

## Sentiment & positioning
| Data type | Metric / fact | Source | As of |
|-----------|---------------|--------|-------|
| Sentiment (quantified) | | | |
| Options / short | | | |
| Institutional / 13F | | | |
| Insider | | | |

## Financial Results Summary

### Headline Numbers
| Metric | Actual | Consensus | Surprise | YoY Change |
|--------|--------|-----------|----------|------------|
| Revenue | $X.XB | $X.XB | +X% | +X% |
| EPS | $X.XX | $X.XX | +X% | +X% |
| Operating Margin | X.X% | X.X% | Xbps | Xbps |

### Key Highlights
- [Highlight 1]
- [Highlight 2]
- [Highlight 3]

## Revenue and Margin Analysis

### Revenue Performance
- **Total Revenue:** $X.XB (+X% YoY, +X% QoQ)
  - Beat/missed consensus by $XXM (X%)
  - Key drivers: [Brief explanation]

### Margins
- **Gross Margin:** X.X% (vs. X.X% prior year)
- **Operating Margin:** X.X% (vs. X.X% prior year)
- **Net Margin:** X.X% (vs. X.X% prior year)
- Margin drivers: [Brief explanation]

## Operating Metrics and Segment Performance

### [Segment 1]
- Revenue: $X.XB (+X% YoY)
- Key metrics and performance drivers

### [Segment 2]
- Revenue: $X.XB (+X% YoY)
- Key metrics and performance drivers

### Operational KPIs
- [KPI 1]: [Value and trend]
- [KPI 2]: [Value and trend]

## Management Guidance and Commentary

### Forward Guidance
- **Q[X] [Year] Revenue:** $X.XB - $X.XB (vs. consensus $X.XB)
- **Q[X] [Year] EPS:** $X.XX - $X.XX (vs. consensus $X.XX)
- **Full Year [Year]:** [If provided]

### Strategic Priorities
[Key themes from management commentary]
1. [Priority 1]
2. [Priority 2]

### Market Conditions
[Management's view on demand environment, competition, macro]

## Cash Flow and Balance Sheet

### Cash Generation
- **Operating Cash Flow:** $X.XB (+X% YoY)
- **Free Cash Flow:** $X.XB (+X% YoY)
- **FCF Margin:** X.X%

### Balance Sheet
- **Cash and Equivalents:** $X.XB
- **Total Debt:** $X.XB
- **Net Debt:** $X.XB (Debt/EBITDA: X.Xx)

### Capital Allocation
[Discussion of buybacks, dividends, capex, M&A]

## Key Surprises vs. Expectations

### Magnitude and quality
- [Beat/miss vs consensus in **% or bps**; **sigma** vs historical surprise distribution if estimable]  
- **Quality of beat/miss:** revenue vs margin vs buyback vs tax vs one-timers  

### Positive Surprises
1. [Surprise; sustainability; line-item]

### Negative Surprises
1. [Surprise; sustainability; line-item]

### Guidance Implications
[How guidance compared to expectations]

## Analyst Reactions

### Rating Changes
- [Firm 1]: [Action and price target]
- [Firm 2]: [Action and price target]

### Consensus View
[Summary of analyst sentiment]

## Scenario refresh (post-print)
| Scenario | Probability (%) | Updated vs pre-print | Price / range | Implied return vs spot |
|----------|-----------------|----------------------|---------------|-------------------------|
| Bull | | | | |
| Base | | | | |
| Bear | | | | |

**Probability-weighted view:** [Show EV math]

## Valuation cross-check
[Multiples vs history/peers post-print; does price embed the new guidance?]

## Investment Implications

### Business Fundamentals Assessment
[Objective assessment of results quality]

### Forward Outlook
[Implications for future quarters based on guidance and trends]

### Key Risks and Opportunities
[Balance of concerns and positive drivers]

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

- Use [analytical-frameworks.md](./analytical-frameworks.md): **lead with what matters** for the forward story  
- **Focus on business fundamentals**, not just stock price movement  
- Compare results to consensus from tearsheet; **quantify surprise magnitude** where possible  
- Include **thesis check** (bull/bear) so the digest is forward-looking  
- **Quality signals:** include **Watch for** column (forward monitoring)  
- **Sentiment & positioning** table: tearsheet-first, then search—no anecdote-only sell-side notes  
- **Scenario refresh** after the print: probabilities, prices, **show EV math**  
- Add **valuation cross-check** so implications tie to price  
- Legal/regulatory search in Step 4 for overhangs not in the press release  
- Extract key quotes from transcript when available  
- Note accounting changes or one-time items explicitly  
- Assess **sustainable vs one-time** drivers of EPS and revenue

## Key Differences from Other Workflows

- **vs. Company Brief:** Digest is deep dive on one earnings event; Brief covers 25 days of all developments
- **vs. Earnings Preview:** Digest analyzes actual results; Preview sets expectations before release
- **vs. Risk Assessment:** Digest focuses on quarterly performance; Risk Assessment is comprehensive risk analysis  
- **vs. Valuation snapshot:** Digest is event-driven around a print; [valuation-snapshot.md](./valuation-snapshot.md) is multipurpose “what’s it worth”

## Example Queries to User

If multiple quarters available:
- "I see results for Q3 2024 (most recent) and Q2 2024. Should I analyze the latest Q3 results?"

If earnings call transcript not yet available:
- "The earnings call transcript isn't available yet. I'll analyze the press release and update once the call is published."
