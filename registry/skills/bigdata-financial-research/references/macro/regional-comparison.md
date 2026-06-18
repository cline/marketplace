# Regional Comparison Workflow

## When to Use
- "Compare US vs Europe vs Asia"
- "Which regions look attractive?"
- G7/G20 analysis
- Regional allocation decisions

## Workflow Steps

### Step 1: Search Economic Data for Each Region
Use `bigdata_search` with targeted queries for each region:

**For US:**
```
bigdata_search("United States GDP growth economic outlook 2026")
bigdata_search("US inflation Federal Reserve interest rates")
bigdata_search("US unemployment labor market")
```

**For Europe:**
```
bigdata_search("Eurozone GDP growth economic outlook 2026")
bigdata_search("ECB interest rates inflation monetary policy")
bigdata_search("Europe unemployment economic data")
```

**For Asia:**
```
bigdata_search("Japan GDP growth BOJ monetary policy")
bigdata_search("China economic outlook GDP growth")
bigdata_search("India economic growth outlook")
```

### Step 2: Search Comparative Analysis
Use `bigdata_search`:
- "G7 economic comparison GDP growth rates"
- "US Europe Asia economic outlook comparison"
- "developed vs emerging markets allocation"
- "global economic outlook regional comparison"

### Step 3: Search Regional Market Implications
Use `bigdata_search`:
- "regional equity valuations US Europe Asia"
- "currency outlook major currencies USD EUR JPY"
- "global fixed income yields comparison"

### Step 4: Cross-Asset Views
Search for fixed income and currency perspectives for each region.

## Output Template

```markdown
# Regional Macro Comparison
Report Date: [Date]

## Executive Summary
[Overview of relative regional attractiveness]

## Regional Scorecard

| Region | GDP | CPI | Rate | Equity YTD | FX YTD | Score |
|--------|-----|-----|------|------------|--------|-------|
| US | X.X% | X.X% | X.X% | +X.X% | +X.X% | X/10 |
| Europe | X.X% | X.X% | X.X% | +X.X% | +X.X% | X/10 |
| Japan | X.X% | X.X% | X.X% | +X.X% | +X.X% | X/10 |
| China | X.X% | X.X% | X.X% | +X.X% | +X.X% | X/10 |
| EM ex-CN | X.X% | X.X% | X.X% | +X.X% | +X.X% | X/10 |

## Regional Deep Dives

### United States
- **Growth**: [Assessment]
- **Policy**: [Fed outlook]
- **Markets**: [Equity/FI/FX view]
- **Key Risk**: [Primary concern]

### Europe
[Same structure]

### Asia
[Same structure]

## Allocation Recommendations

| Region | Current | Recommended | Change |
|--------|---------|-------------|--------|
| US | X% | X% | +/-X% |
| Europe | X% | X% | +/-X% |
| Japan | X% | X% | +/-X% |
| EM | X% | X% | +/-X% |

## Key Differentiators
1. **Growth**: [Regional comparison]
2. **Policy**: [Divergence/convergence]
3. **Valuations**: [Relative attractiveness]
4. **Currency**: [FX implications]

## Risks by Region
| Region | Primary Risk | Secondary Risk |
|--------|--------------|----------------|

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```
