# Cross-Sector Comparison Workflow

## When to Use
- "Compare [sector A] vs [sector B]"
- "Which sectors look attractive?"
- Sector rotation analysis
- Relative value across sectors

## Workflow Steps

### Step 1: Define Sectors
GICS sectors: Technology, Health Care, Financials, Consumer Discretionary, Consumer Staples, Industrials, Energy, Materials, Real Estate, Communication Services, Utilities

### Step 2: Gather Sector Data
For each sector, use `bigdata_search`:
- "[Sector] sector performance valuation"
- "[Sector] sector earnings growth estimates"
- "[Sector] sector analyst recommendations"

### Step 3: Select Bellwethers
Use `find_securities` for 3-5 companies per sector, then `bigdata_company_tearsheet`.

### Step 4: Economic Cycle Analysis
Use `bigdata_search`:
- "sector rotation economic cycle"
- "cyclical vs defensive outlook"
- "interest rate sensitive sectors"

### Step 4b: Profitability and ROIC spread context

For **each sector** in scope, add a **short** read on **profitability vs history** (or vs cost of capital) using bellwether tearsheets and search:

- Query examples: "[Sector] sector ROIC margin cycle vs historical average", "sector profitability peak trough".  
- Goal: state whether current valuations sit on **peak**, **mid-cycle**, or **trough-like** earnings power **when evidence allows**—not a full model.  
- Deeper framework: [../equity-analysis/competitive-analysis/porter-five-forces.md](../equity-analysis/competitive-analysis/porter-five-forces.md) and sector files under [../equity-analysis/sectors/](../equity-analysis/sectors/).

## Output Template

```markdown
# Cross-Sector Comparison
Report Date: [Date]

## Executive Summary
[Overview of relative attractiveness]

## Sector Scorecard

| Sector | YTD | P/E | EPS Growth | Sentiment | Score |
|--------|-----|-----|------------|-----------|-------|
| Technology | +X.X% | XX.X | +X.X% | Bullish | ⭐⭐⭐⭐⭐ |
| Financials | +X.X% | XX.X | +X.X% | Neutral | ⭐⭐⭐⭐ |

## Economic Cycle Positioning

**Current Phase**: [Early/Mid/Late Cycle or Recession]

| Phase | Historical Winners | Current Signals |
|-------|-------------------|-----------------|
| Early | Financials, Consumer Disc, Industrials | [Assessment] |
| Mid | Technology, Communication | [Assessment] |
| Late | Energy, Materials, Health Care | [Assessment] |
| Recession | Staples, Utilities, Health Care | [Assessment] |

### ROIC / margin vs cycle (Step 4b)
| Sector | Profitability vs history (qual.) | Implication for relative value |
|--------|----------------------------------|----------------------------------|
| | | |

## Rotation Recommendations

### Overweight
1. **[Sector]** - Score: X/10, Rationale: [Brief], Plays: [Companies]

### Neutral
[Similar format]

### Underweight
[Similar format]

## Key Factors Driving Rotation
1. [Factor]: [Impact on sectors]

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```
