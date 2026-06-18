# Sector Analysis Workflow

## When to Use
- "Analyze [sector] sector"
- "What's happening in [sector]?"
- Sector performance, trends, or outlook requests

## Workflow Steps

### Step 1: Gather Sector Context
Use `bigdata_search` with queries:
- "[Sector] sector outlook trends analysis"
- "[Sector] sector earnings performance"
- "[Sector] sector headwinds tailwinds"
- "[Sector] sector valuations multiples"
- "[Sector] sector regulatory policy"

### Step 1b: Sector-specific KPI lens (GICS)

Do **not** rely only on generic P/E, P/S, EV/EBITDA. Map the sector to **primary operating and valuation KPIs** (condensed lookup below). For full playbooks, see [../equity-analysis/sector-routing.md](../equity-analysis/sector-routing.md) and the matching file under [../equity-analysis/sectors/](../equity-analysis/sectors/).

| GICS sector | Emphasize these KPIs (examples) |
|-------------|----------------------------------|
| Information Technology / Software-SaaS | ARR growth, NRR, Rule of 40, FCF margin, payback |
| Financials | NIM, CET1 / capital, credit costs, ROTCE, efficiency |
| Health Care (incl. Pharma) | Growth drivers, pipeline / patent, R&D, payer mix, regulatory |
| Real Estate (REITs) | AFFO, NAV, cap rates vs bonds, same-store NOI |
| Industrials | Backlog, book-to-bill, margin mix, OEM / capex cycle |
| Consumer Discretionary / Staples | Same-store sales, promo, input costs, private label |
| Energy | Commodity linkage, breakeven, FCF at forward curve, capital discipline |
| Materials | Price/volume, capacity, inventory, China / construction linkage |
| Communication Services | Subscribers, ARPU, churn, ad market / streaming economics |
| Utilities | Allowed ROE, rate case risk, weather / load growth |
| (Other) | Default to margin trajectory, ROIC vs peers, and segment growth |

### Step 2: Identify Key Companies
Use `find_securities` for 5-10 major sector companies, then `bigdata_company_tearsheet` for each:
- Financial metrics and performance
- Analyst estimates and sentiment
- Revenue segmentation
- ESG scores

### Step 3: Aggregate Sector Metrics
From tearsheets, compile:
- **Sector-relevant multiples** (from Step 1b—not only P/E, P/S, EV/EBITDA)
- **Sector KPIs** from Step 1b where visible on tearsheets or estimates
- Revenue/earnings growth trends
- Analyst rating distribution
- Sentiment indicators

### Step 3b: Cycle and profitability positioning

Add **institutional-style cycle context** (brief, evidence-based):

- Use `bigdata_search`: "[Sector] sector ROIC profitability cycle outlook" and "[Sector] margin cycle vs history".  
- State whether **ROIC (or sector proxy)** and margins appear **early / mid / late** vs a normal cycle, or flag **data limits**.  
- Mental model for industry economics: [../equity-analysis/competitive-analysis/porter-five-forces.md](../equity-analysis/competitive-analysis/porter-five-forces.md) (full **competitive advantage period** / ROIC vs WACC discussion lives in equity-analysis valuation and sector files).

### Step 4: Search Sector Catalysts
Use `bigdata_search`:
- "[Sector] regulatory changes policy"
- "[Sector] technology disruption"
- "[Sector] M&A consolidation"
- "[Sector] earnings expectations"
- "[Sector] supply chain tariffs"

### Step 5: Events Calendar
Use `bigdata_events_calendar` for upcoming earnings/conferences.

## Output Template

```markdown
# Sector Analysis: [Sector Name]
Report Date: [Date]

## Executive Summary
[3-4 sentence overview]

## Sector Performance Overview

### Key Metrics
| Metric | Current | YoY Change | vs. S&P 500 |
|--------|---------|------------|-------------|
| Avg P/E | X.Xx | +/-X% | Premium/Discount |
| Revenue Growth (TTM) | X.X% | +/- bps | Outperform/Underperform |

### Sector-specific KPIs (from Step 1b)
| KPI | Sector read | Comment |
|-----|-------------|---------|
| [e.g. Rule of 40] | | |

### Cycle / profitability positioning
[ROIC or margin vs history; early/mid/late read; caveats]

### Analyst Sentiment
| Rating | % of Coverage |
|--------|---------------|
| Strong Buy/Buy | X% |
| Hold | X% |
| Sell | X% |

## Key Themes & Drivers

### Tailwinds
1. **[Theme]** - [Description], Impact: [Timeline], Beneficiaries: [List]

### Headwinds
1. **[Risk]** - [Description], Severity: [H/M/L], Exposed: [List]

## Sub-Industry Breakdown
| Sub-Industry | Performance | Valuation | Outlook |
|--------------|-------------|-----------|---------|

## Upcoming Catalysts

### Earnings Calendar (Next 30 Days)
| Company | Date | Consensus EPS | Key Metrics |
|---------|------|---------------|-------------|

## Investment Implications
- **Positioning**: [Overweight/Neutral/Underweight]
- **Top Picks**: [Companies with brief thesis]
- **Avoid**: [Areas with rationale]

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

## GICS Sectors Reference
Information Technology, Health Care, Financials, Consumer Discretionary, Consumer Staples, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities
