# Country Economic Analysis Workflow

## When to Use
- "Economic outlook for [country]"
- "Analyze [country] economy"
- Country comparison or regional analysis
- Economic calendar or data releases
- Institutional, multilateral, or **academic / research** audiences (prioritize analytical depth and policy recommendations)

## Workflow Steps

### Step 1: Search Core Economic Indicators
Use `bigdata_search` with targeted queries for each key indicator:

```
bigdata_search("[Country] GDP growth economic outlook 2026")
bigdata_search("[Country] inflation CPI consumer prices trends")
bigdata_search("[Country] central bank interest rates monetary policy")
bigdata_search("[Country] unemployment rate labor market")
bigdata_search("[Country] fiscal policy government budget")
```

### Step 2: Search Monetary Policy
Use `bigdata_search`:
- "[Country] central bank rate decision outlook"
- "[Country] monetary policy inflation target"
- "Fed/ECB/BOJ/PBOC policy rate path expectations"

### Step 3: Search Economic Calendar & Events
Use `bigdata_search`:
- "[Country] economic data releases calendar"
- "[Country] central bank meeting schedule"
- "[Country] GDP CPI employment report dates"

### Step 4: Search Structural & Historical Context (required for analytical depth)
Use `bigdata_search` to support **structural and historical analysis** — do not produce a shallow, point-in-time-only report:
- "[Country] sector transformation structural change agriculture industry services"
- "[Country] labor productivity by sector comparison"
- "[Country] economic structure evolution [time range e.g. 1990 2020]"
- "[Country] sectoral GDP share history"
- "[Country] employment by sector productivity growth"

### Step 5: Search Debt Composition, Tax-to-GDP & PFM (required for depth)
Use `bigdata_search` for **debt mechanics, tax burden, and public financial management**:
- "[Country] public debt composition domestic external"
- "[Country] debt servicing interest cost weighted average rate"
- "[Country] debt crowding out private sector"
- "[Country] public financial management PFM reform budget execution"
- "[Country] tax revenue GDP fiscal consolidation"
- "[Country] tax to GDP ratio tax burden comparison"
- "[Country] tax-to-GDP revenue mobilization OECD IMF"

### Step 6: Search Labor Market in Depth (avoid "macro good, micro bad" without elaboration)
Use `bigdata_search` to substantiate labor narrative:
- "[Country] labor market informality underemployment"
- "[Country] youth unemployment sectoral employment"
- "[Country] real wages productivity labor share"
- "[Country] employment growth by sector"

### Step 7: Search Policy & Reform Context (for recommendations section)
Use `bigdata_search` to ground **policy recommendations**:
- "[Country] fiscal consolidation tax reform recommendations"
- "[Country] debt management strategy IMF World Bank"
- "[Country] structural reform priorities"
- "[Country] demographic dividend youth bulge policy"

### Step 8: Search Market Implications & FDI
Use `bigdata_search`:
- "[Country] equity market outlook"
- "[Country] bond market yields spreads"
- "[Country] currency forex outlook"
- "[Country] foreign investment flows"
- "[Country] FDI foreign direct investment inflows outflows"
- "[Country] FDI trajectory outlook 2026 greenfield M&A"
- "[Country] foreign direct investment by sector trend"

### Step 9: Search Regional Context (if applicable)
Use `bigdata_search`:
- "G7 economic comparison GDP inflation rates"
- "[Country] vs peers economic performance"
- "developed markets emerging markets outlook"

## Output Template

```markdown
# Country Economic Analysis: [Country]
Report Date: [Date]

## Executive Summary
[3-4 sentence overview]

## Economic Snapshot

### Key Indicators
| Indicator | Current | Previous | Trend | Context |
|-----------|---------|----------|-------|---------|
| GDP Growth (YoY) | X.X% | X.X% | ↑/↓/→ | [vs peers] |
| Inflation (CPI YoY) | X.X% | X.X% | ↑/↓/→ | [vs target] |
| Unemployment | X.X% | X.X% | ↑/↓/→ | [context] |
| Policy Rate | X.X% | X.X% | [last action] | [outlook] |
| Tax to GDP | X.X% | X.X% | ↑/↓/→ | [vs peers / target] |

### Economic Health Assessment
| Dimension | Rating | Commentary |
|-----------|--------|------------|
| Growth Momentum | Strong/Moderate/Weak | [Brief] |
| Inflation | Contained/Elevated/Concerning | [Brief] |
| Labor Market | Tight/Balanced/Slack | [Brief] |
| Fiscal Position | Solid/Manageable/Stretched | [Brief] |

### Structural & Historical Context (include for analytical depth)
- **Sector transformation**: [e.g. agriculture → industry/services over 2–3 decades; cite time range and key shifts]
- **Labor productivity by sector**: [comparison across sectors, e.g. agriculture vs industry vs services; cite levels or growth rates where available]
- **Structural narrative**: [2–4 sentences on how the economy has evolved and what it implies for outlook]

### Debt & Fiscal Mechanics (include for depth)
- **Tax to GDP ratio**: [level and trend; comparison to peers or IMF/OECD benchmarks; revenue mobilization targets if cited]
- **Debt composition**: [domestic vs external share; maturity/currency mix if available]
- **Debt servicing**: [interest burden, weighted average rate if available; crowding-out or rollover risk]
- **PFM / budget**: [key PFM reforms, budget execution, revenue performance; tax-to-GDP or targets if cited]

### Labor Market (substantive; avoid one-line "macro good, micro bad")
- **Macro**: [aggregate unemployment/employment, participation]
- **Micro / structural**: [informality, underemployment, youth unemployment, sectoral gaps, real wages vs productivity]
- **Summary**: [1–2 sentences tying macro and micro to outlook]

## Monetary Policy Outlook

### Current Stance
- **Rate**: X.X%
- **Last Action**: [Hike/Cut/Hold] on [Date]
- **Guidance**: [Summary]

### Rate Path Expectations
| Timeframe | Expected | Commentary |
|-----------|----------|------------|
| Next meeting | | |
| Year-end | | |

## Key Economic Events to Watch
| Date | Event | Why It Matters |
|------|-------|----------------|

## Market Implications

### Equity
- **YTD**: +/-X.X%
- **Valuation**: Premium/Fair/Discount
- **Opportunities**: [Sectors]

### Fixed Income
- **10Y Yield**: X.X%
- **Curve**: Steep/Flat/Inverted
- **View**: Extend/Neutral/Shorten

### Currency
- **vs USD**: [Level]
- **YTD**: +/-X.X%
- **Outlook**: Bullish/Neutral/Bearish

### FDI Trajectory
- **Recent trend**: [inflows/outflows, YoY or latest data; greenfield vs M&A if available]
- **By sector or source**: [key sectors or origin countries if relevant]
- **Outlook**: [catalyst or headwind; policy or competitiveness driver]

## Investment Thesis
**Bull Case**: [Points]
**Bear Case**: [Points]
**Positioning**: [Recommendation]

## Key Risks
1. [Risk]: [Description and triggers]

## Policy Recommendations (dedicated section — required)
Provide a **dedicated policy recommendations section**, not just scattered mentions. Structure by pillar and cite specific targets or mechanisms where available.

### Fiscal consolidation
- [Concrete measures: revenue vs expenditure; tax-to-GDP or revenue targets if cited (e.g. 16–18%); base broadening, spending prioritization]

### Debt management
- [Strategy for domestic vs external; maturity/refinancing; cost reduction or reprofiling; any stated targets]

### Monetary policy
- [Stance consistency with inflation target; communication; financial stability considerations]

### Structural reforms
- [Sector-specific (e.g. agriculture, industry); PFM/budget execution; business environment; demographic dividend or youth/labor policies if relevant]

*Cite sources (e.g. IMF, World Bank, national authorities) for each recommendation where applicable.*

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

## Audience Suitability & Quality Bar
- **Academic / Research**: Reports should include **structural and historical context** (sector transformation over time, labor productivity comparisons), **detailed debt and PFM mechanics**, a **substantive labor market** section (macro and micro), and a **dedicated policy recommendations section** with multi-pronged, sourced recommendations and specific targets where available. Avoid shallow, point-in-time-only narrative.
- **Development finance / multilateral**: Same depth as above; emphasize policy recommendations and PFM/governance.
- **Investor / trading**: Retain data recency, consensus forecasts, and investment thesis; add the above depth where it does not conflict with brevity.
