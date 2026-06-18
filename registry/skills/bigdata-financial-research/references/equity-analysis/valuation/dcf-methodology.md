# DCF Valuation Methodology

## Overview

Discounted Cash Flow (DCF) analysis values a company based on the present value of its future cash flows. This is the foundational intrinsic valuation methodology, providing a framework to convert operational forecasts into enterprise and equity value.

## Table of Contents
1. [FCFF vs FCFE Decision Tree](#fcff-vs-fcfe-decision-tree)
2. [Step-by-Step DCF Process](#step-by-step-dcf-process)
3. [Enterprise to Equity Bridge](#enterprise-to-equity-bridge)
4. [Common DCF Pitfalls](#common-dcf-pitfalls)
5. [DCF Quality Checks](#dcf-quality-checks)
6. [Sensitivity Analysis Guidance](#sensitivity-analysis-guidance)
7. [DCF Output Template](#dcf-output-template)

---

## FCFF vs FCFE Decision Tree

| Criterion | Use FCFF (to Enterprise) | Use FCFE (to Equity) |
|-----------|-------------------------|---------------------|
| Capital structure | Changing or optimal target | Stable leverage |
| Leverage | High or volatile | Low and predictable |
| Industry | Capital-intensive, M&A-heavy | Banks, insurers, REITs |
| Data quality | Limited debt schedules | Clear debt/interest forecasts |
| Valuation output | Enterprise value (subtract net debt) | Equity value directly |

**Default Choice**: Use FCFF for most industrial and technology companies. FCFE is reserved for financial institutions where assets and liabilities are intertwined.

### FCFF Formula

```
FCFF = EBIT(1-t) + D&A - CapEx - Change in NWC
```

Or equivalently:

```
FCFF = NOPAT + D&A - CapEx - Delta NWC
```

Where:
- NOPAT = Net Operating Profit After Tax = EBIT * (1 - marginal tax rate)
- D&A = Depreciation and Amortization
- CapEx = Capital Expenditures
- NWC = Net Working Capital (Current Assets - Current Liabilities, excluding cash and debt)

### FCFE Formula

```
FCFE = Net Income + D&A - CapEx - Delta NWC + Net Borrowing
```

---

## Step-by-Step DCF Process

### Step 1: Revenue Projection (3-10 Year Forecast)

Build revenue from fundamental drivers, not arbitrary growth rates.

**Bottom-Up Approach**:
- Volume x Price for each product/segment
- Market size x Market share trajectory
- Customer count x Revenue per customer

**Top-Down Sanity Check**:
- TAM penetration rates
- Historical growth decay patterns
- Industry growth benchmarks

| Forecast Year | 1-2 | 3-5 | 6-10 |
|--------------|-----|-----|------|
| Granularity | Quarterly drivers | Annual drivers | Fade to terminal |
| Confidence | High | Medium | Low (trend-based) |

### Step 2: Margin Trajectory

Project operating margins through the income statement:

1. **Gross Margin**: Input cost trends, pricing power, mix shift, scale benefits
2. **Operating Margin**: Operating leverage (fixed vs variable), SG&A efficiency, R&D intensity
3. **EBIT Margin**: Final operating profitability before financing costs

**Key Questions**:
- What is the mature-state margin for this business model?
- How quickly can the company reach that margin?
- Are there structural headwinds (competition, regulation) limiting margin expansion?

**Margin Benchmarking Table**:

| Business Type | Typical Mature EBIT Margin |
|--------------|---------------------------|
| Asset-light SaaS | 25-35% |
| Consumer staples | 15-20% |
| Industrial manufacturing | 10-15% |
| Retail | 5-10% |
| Airlines, commodities | 0-8% |

### Step 3: Capital Intensity

Model reinvestment requirements:

**CapEx Forecasting**:
- Maintenance CapEx: Typically 70-100% of D&A
- Growth CapEx: Function of revenue growth and capital intensity ratio
- Total CapEx/Revenue: Should trend toward industry norms at maturity

**Working Capital**:
- Model as percentage of revenue or days outstanding
- DSO (Days Sales Outstanding), DIO (Days Inventory Outstanding), DPO (Days Payables Outstanding)
- NWC as % of revenue typically ranges from -5% (negative working capital retailers) to +25% (capital goods)

```
NWC Change = (NWC/Revenue %) * Delta Revenue
```

### Step 4: Terminal Value Calculation

Terminal value typically represents 60-80% of total DCF value. Use two methods and triangulate.

#### Method 1: Gordon Growth Model (Perpetuity)

```
Terminal Value = FCFF_terminal * (1 + g) / (WACC - g)
```

Where g = perpetual growth rate (typically 2-3%, not exceeding long-term GDP growth)

**Sanity Checks**:
- Terminal growth should not exceed inflation + real GDP growth
- Terminal ROIC should converge toward WACC for competitive industries
- Terminal margins should reflect mature-state economics

#### Method 2: Exit Multiple

```
Terminal Value = EBITDA_terminal * Exit Multiple
```

Select exit multiple based on:
- Current comparable company trading multiples
- Historical average multiples for the sector
- Justified multiple based on terminal growth and ROIC

**Cross-Check**: Back-calculate implied perpetual growth from exit multiple:

```
Implied g = WACC - (FCFF / TV)
```

### Step 5: Discount Rate (WACC)

```
WACC = (E/V) * Ke + (D/V) * Kd * (1 - t)
```

Where:
- E/V = Equity weight (market value)
- D/V = Debt weight (market value)
- Ke = Cost of equity
- Kd = Cost of debt
- t = Marginal tax rate

#### Cost of Equity (CAPM)

```
Ke = Rf + Beta * (Rm - Rf) + Size Premium + Country Risk Premium
```

| Component | Source | Typical Range |
|-----------|--------|---------------|
| Risk-free rate (Rf) | 10Y government bond | 3-5% |
| Equity risk premium (Rm - Rf) | Historical/implied | 5-6% |
| Beta | Regression or peer unlevering | 0.8-1.5 |
| Size premium | Small cap adjustment | 0-3% |
| Country risk premium | Emerging markets | 0-5% |

#### Beta Unlevering/Relevering Process

**Step 1**: Collect peer betas (levered, regression-based)

**Step 2**: Unlever each peer beta:

```
Beta_unlevered = Beta_levered / [1 + (1-t) * (D/E)]
```

**Step 3**: Calculate median unlevered beta

**Step 4**: Relever to target capital structure:

```
Beta_relevered = Beta_unlevered * [1 + (1-t) * (Target D/E)]
```

**Cost of Debt**: Use yield on company bonds or synthetic rating approach based on interest coverage.

---

## Enterprise to Equity Bridge

```
Equity Value = Enterprise Value
             - Total Debt
             - Preferred Stock
             - Minority Interest
             - Unfunded Pension Liabilities
             + Cash and Equivalents
             + Non-operating Assets (investments, excess real estate)
```

```
Per Share Value = Equity Value / Diluted Shares Outstanding
```

Use treasury stock method for dilution from options and convertibles.

---

## Common DCF Pitfalls

| Pitfall | Problem | Solution |
|---------|---------|----------|
| Hockey stick projections | Unrealistic margin/growth inflection | Base case should be achievable, not aspirational |
| Terminal value dominance | 80%+ of value in terminal | Extend explicit forecast or reduce terminal growth |
| Circular WACC | Iterating equity value to calculate weights | Use target capital structure, iterate if needed |
| Ignoring reinvestment | High growth but low CapEx | Growth requires capital; ROIC must be consistent |
| Double-counting | Subtracting debt that's in FCFE | Match cash flows to discount rate |
| Tax rate errors | Using effective rate for WACC | Use marginal rate for NOPAT calculation |

---

## DCF Quality Checks

Before finalizing, verify:

1. **Implied multiples**: Calculate EV/EBITDA, P/E from DCF output. Are they reasonable vs peers?
2. **Terminal ROIC**: Does terminal ROIC exceed WACC? By how much and is it sustainable?
3. **Revenue CAGR**: Is the 5-10 year CAGR defensible given competitive dynamics?
4. **Cash conversion**: Is FCFF/Net Income ratio consistent with industry?
5. **Value per unit**: Does implied value per customer/subscriber/store make sense?

---

## Sensitivity Analysis Guidance

Create two-way sensitivity tables varying the most impacthat uncertain inputs:

**Standard Sensitivities**:

| Sensitivity Table 1 | WACC |
|---------------------|------|
| Terminal Growth | 7%, 8%, 9%, 10%, 11% (rows) |
| Terminal Growth | 1%, 2%, 3%, 4% (columns) |

| Sensitivity Table 2 | Terminal EBITDA Multiple |
|---------------------|--------------------------|
| Exit Multiple | 6x, 8x, 10x, 12x, 14x (rows) |
| Terminal Margin | Base -2%, Base, Base +2% (columns) |

**Scenario Analysis**:

| Scenario | Probability | Value | Weighted |
|----------|-------------|-------|----------|
| Bull | 25% | $XX | |
| Base | 50% | $XX | |
| Bear | 25% | $XX | |
| **Expected Value** | | | $XX |

---

## DCF Output Template

Present final valuation as:

1. **Summary**: Single intrinsic value per share
2. **Football field**: Range from sensitivity analysis
3. **Key assumptions table**: Revenue CAGR, terminal margin, WACC, terminal growth
4. **Bridge**: Enterprise to equity value walk
5. **Implied metrics**: What the market would need to believe for current price to be fair
