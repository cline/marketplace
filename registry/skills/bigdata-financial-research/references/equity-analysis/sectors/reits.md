# Real Estate Investment Trusts (REITs) Analysis

## Overview

REITs are pass-through entities that must distribute at least 90% of taxable income as dividends, avoiding corporate-level taxation. This structure makes GAAP net income largely meaningless for analysis due to heavy non-cash depreciation charges that distort reported earnings. REIT analysis centers on cash-generating ability through Funds from Operations (FFO) and Adjusted FFO (AFFO), with valuation anchored to Net Asset Value (NAV).

## Table of Contents
1. [Core KPIs and Formulas](#core-kpis-and-formulas)
2. [Performance Benchmarks](#performance-benchmarks)
3. [Why GAAP Earnings Mislead for REITs](#why-gaap-earnings-mislead-for-reits)
4. [Valuation Framework](#valuation-framework)
5. [Common Analytical Pitfalls](#common-analytical-pitfalls)
6. [Red Flags](#red-flags)
7. [Due Diligence Checklist](#due-diligence-checklist)

## Core KPIs and Formulas

### Cash Flow Metrics

**Funds from Operations (FFO)**
```
FFO = Net Income
    + Real Estate Depreciation and Amortization
    + Impairment Charges on Real Estate
    - Gains (+ Losses) on Property Sales
    - Gains (+ Losses) on Debt Restructuring
```
FFO is defined by NAREIT (National Association of Real Estate Investment Trusts) and represents recurring cash earnings before capital expenditure requirements.

**Adjusted Funds from Operations (AFFO)**
```
AFFO = FFO
     - Recurring Capital Expenditures (Maintenance CapEx)
     - Straight-line Rent Adjustment
     - Amortization of Lease Intangibles
     - Amortization of Above/Below Market Leases
     +/- Other Non-cash Items (Stock Compensation, etc.)
```
AFFO better approximates true cash available for distribution by subtracting maintenance requirements. Also called CAD (Cash Available for Distribution) or FAD (Funds Available for Distribution).

**Maintenance vs. Growth CapEx**
```
Maintenance CapEx = Expenditures to maintain current NOI-generating capacity
                  = Tenant improvements on renewals + Building maintenance + Leasing commissions on renewals

Growth CapEx = Development spending + Acquisitions + TIs for new leases
```
The distinction is critical: maintenance CapEx reduces recurring cash flow, while growth CapEx represents optional investment.

### Property-Level Metrics

**Net Operating Income (NOI)**
```
NOI = Property Revenue - Property Operating Expenses

Property Revenue = Base rent + Percentage rent + Tenant reimbursements + Other income
Operating Expenses = Property taxes + Insurance + Utilities + Repairs + Management fees
```
NOI excludes depreciation, interest, corporate G&A, and capital expenditures.

**Same-Store NOI Growth**
```
Same-Store NOI Growth = (NOI_current - NOI_prior) / NOI_prior

Same-store portfolio: Properties owned and operated for full comparable periods
```
Isolates organic growth from acquisition effects. The definition of "same-store" varies by company; verify methodology.

**Capitalization Rate (Cap Rate)**
```
Cap Rate = NOI / Property Value

Implied Property Value = NOI / Cap Rate
```

**Occupancy Rate**
```
Occupancy = Leased Square Feet / Total Leasable Square Feet

Economic Occupancy = Actual Rent Collected / Potential Gross Rent
```
Physical occupancy can exceed economic occupancy due to free rent periods and tenant defaults.

### Leasing Metrics

**Rent Spreads**
```
Cash Rent Spread = (New Cash Rent - Expiring Cash Rent) / Expiring Cash Rent

GAAP Rent Spread = (New GAAP Rent - Expiring GAAP Rent) / Expiring GAAP Rent
```
Cash spreads reflect immediate impact; GAAP spreads include straight-line rent over lease term.

**Weighted Average Lease Term (WALT)**
```
WALT = Sum of (Lease Expiration Year * Annual Rent) / Total Annual Rent
```
Longer WALT indicates more stable, predictable cash flows but less near-term upside from re-leasing.

### Balance Sheet Metrics

**Debt / EBITDA**
```
Debt / EBITDA = Total Debt / Annualized EBITDA

EBITDA = NOI - G&A + Other Income (non-real estate)
```

**Fixed Charge Coverage**
```
Fixed Charge Coverage = EBITDA / (Interest Expense + Principal Payments + Preferred Dividends)
```

**Debt / Market Cap**
```
Debt to Market Cap = Total Debt / (Total Debt + Market Cap of Equity)
```

## Performance Benchmarks

| Metric | Weak | Adequate | Strong | Excellent |
|--------|------|----------|--------|-----------|
| Same-Store NOI Growth | <0% | 0-2% | 2-3% | >3% |
| Occupancy Rate | <90% | 90-94% | 94-96% | >96% |
| Cash Rent Spreads | Negative | 0-5% | 5-10% | >10% |
| Debt / EBITDA | >8x | 6-8x | 5-6x | <5x |
| Fixed Charge Coverage | <2.0x | 2.0-2.5x | 2.5-3.5x | >3.5x |
| AFFO Payout Ratio | >100% | 85-100% | 70-85% | <70% |
| AFFO per Share Growth | <0% | 0-3% | 3-5% | >5% |

**Sector-Specific Occupancy Targets:**

| REIT Type | Target Occupancy |
|-----------|------------------|
| Office | >90% |
| Industrial | >95% |
| Retail (non-mall) | >93% |
| Multifamily | >94% |
| Self-Storage | >88-92% |
| Healthcare | >85% |
| Hotels (RevPAR focus) | 65-75% |

## Why GAAP Earnings Mislead for REITs

### Depreciation Overstates Expense

Real estate depreciation follows IRS schedules (39 years for commercial, 27.5 years for residential) that rarely reflect economic reality. Well-maintained properties often appreciate rather than depreciate, and land (typically 15-25% of property value) does not depreciate at all. Adding back depreciation through FFO corrects this distortion.

### Gains/Losses Distort Recurring Performance

Property sales generate large one-time gains or losses that distort period-over-period comparisons. A REIT selling appreciated properties at a profit shows elevated net income that says nothing about recurring cash generation.

### Capitalization Policies Vary

REITs have discretion in capitalizing vs. expensing certain costs (leasing commissions, tenant improvements). Aggressive capitalization inflates both net income and FFO in the short term while building future amortization charges.

### Straight-Line Rent Creates Phantom Income

GAAP requires recognizing rent evenly over lease terms, even when actual cash payments escalate. A lease with $10/sf in year 1 rising to $15/sf in year 10 would show $12.50/sf GAAP revenue annually, overstating cash in early years.

## Valuation Framework

### Net Asset Value (NAV)

The foundational REIT valuation approach:

```
Gross Asset Value = NOI / Cap Rate (for each property or portfolio)

NAV = Gross Asset Value
    + Cash and Equivalents
    + Value of Development Pipeline
    + Value of Land Held
    + Other Assets (Management fees, etc.)
    - Total Debt
    - Preferred Equity
    - Other Liabilities

NAV per Share = NAV / Diluted Shares Outstanding
```

**Cap Rate Selection:**
- Use transaction comparables for similar assets
- Adjust for asset quality, location, lease term, tenant credit
- Apply range to stress-test valuation

| Property Type | Cap Rate Range |
|---------------|----------------|
| Class A Office (Gateway) | 4.5-5.5% |
| Class B Office | 6.0-7.5% |
| Industrial (Logistics) | 4.0-5.5% |
| Retail (Grocery-anchored) | 5.5-7.0% |
| Multifamily (Core) | 4.0-5.5% |
| Self-Storage | 5.0-6.5% |
| Healthcare | 6.0-8.0% |

**Premium/Discount to NAV:**
- Most REITs trade within +/- 15% of NAV
- Persistent premium suggests market expects above-average growth
- Persistent discount suggests capital allocation or portfolio concerns

### FFO and AFFO Multiples

```
P/FFO = Share Price / FFO per Share
P/AFFO = Share Price / AFFO per Share
```

| Sector | Typical P/FFO Range | Typical P/AFFO Range |
|--------|--------------------|--------------------|
| Industrial | 20-30x | 25-40x |
| Multifamily | 15-25x | 18-30x |
| Self-Storage | 18-25x | 22-32x |
| Retail | 10-16x | 12-20x |
| Office | 8-14x | 10-18x |
| Healthcare | 10-16x | 12-20x |
| Hotels | 8-12x | 10-15x |

Higher multiples reflect growth expectations and asset quality; use sector-specific ranges.

### Dividend Discount Model (DDM)

Appropriate given mandatory distribution requirements:

```
Value = D1 / (r - g)

D1 = Expected dividend per share next year
r = Cost of equity (typically 6-10% for REITs)
g = Long-term dividend growth rate (typically 2-4%)
```

For two-stage DDM with above-average near-term growth:
```
Value = Sum of [Dt / (1+r)^t] + Terminal Value / (1+r)^n
```

## Common Analytical Pitfalls

### Cap Rate Estimation Errors

**Problem**: Using portfolio-wide average cap rates without asset-level granularity.

**Impact**: Undervalues high-quality assets and overvalues marginal properties.

**Correct approach**:
- Segment portfolio by quality tier and geography
- Apply appropriate cap rates to each segment
- Weight by NOI contribution, not property count
- Use transaction evidence from comparable sales

**Problem**: Ignoring cap rate expansion risk in rising rate environments.

**Correct approach**: Stress-test NAV with cap rate expansion scenarios (+50-100bps).

### Undercounting CapEx

**Problem**: Using company-disclosed "maintenance CapEx" without verification.

**Impact**: Overstates AFFO if company under-reports recurring capital needs.

**Common understatements**:
- Classifying renewal TIs as growth CapEx
- Deferring maintenance to boost near-term results
- Ignoring cyclical major repairs (roofs, HVAC, parking lots)

**Correct approach**:
- Analyze CapEx as % of revenue over multiple years
- Compare to sector peers (office typically 10-15% of NOI, industrial 5-10%)
- Review CapEx reserves in debt covenants
- Add 10-20% buffer to disclosed maintenance CapEx

### Straight-Line Rent Distortions

**Problem**: Ignoring the gap between GAAP rent and cash rent.

**Impact**: Overstates near-term cash generation for portfolios with long-term escalating leases.

**Analysis**:
```
Straight-line Rent Adjustment = GAAP Rent Revenue - Cash Rent Collected
```
Positive adjustment means GAAP revenue exceeds cash; this reverses over lease term.

**Correct approach**: Always use AFFO (which backs out straight-line adjustments) for payout ratio and yield analysis.

### Ignoring Lease Maturity Risk

**Problem**: Focusing only on current occupancy without analyzing lease rollover.

**Impact**: Misses re-leasing risk concentration.

**Analysis**:
- Build lease expiration schedule by year
- Identify years with >15% of rent rolling
- Assess market rent vs. in-place rent for rolling leases
- Consider tenant credit quality for large expirations

### Development Pipeline Mispricing

**Problem**: Valuing development assets at cost rather than stabilized value.

**Impact**: Understates value of active developers, overstates value of troubled projects.

**Correct approach**:
- Value at cost until significant de-risking (pre-leasing, completion)
- Apply discount to stabilized value for time and execution risk
- Verify yield-on-cost claims against market cap rates

## Red Flags

- AFFO payout ratio >100% (dividend not covered by cash flow)
- Same-store NOI declining while acquisitions mask weakness
- Persistent discount to NAV without catalyst
- Rising vacancy with declining rent spreads
- Debt/EBITDA >8x or approaching covenant limits
- Significant near-term lease expirations in soft market
- Large straight-line rent adjustments relative to cash NOI
- Declining portfolio quality (selling better assets, retaining weaker)
- Subordinated debt or mezzanine financing dependency
- Frequent equity issuance at discount to NAV
- Development pipeline exceeding balance sheet capacity

## Due Diligence Checklist

1. Reconcile FFO to net income with each adjustment verified
2. Calculate AFFO with explicit maintenance CapEx assumptions
3. Build property-level NAV with appropriate cap rates by segment
4. Analyze lease expiration schedule and mark-to-market opportunity
5. Compare same-store NOI definition to peers
6. Verify straight-line rent adjustment trends
7. Stress-test NAV with cap rate expansion scenarios
8. Review debt maturity schedule and refinancing assumptions
9. Assess tenant concentration and credit quality
10. Benchmark CapEx intensity against sector peers
11. Evaluate dividend coverage under stress scenarios
12. Analyze insider ownership and management incentive alignment
