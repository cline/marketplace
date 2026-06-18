# Technology Sector: SaaS and Software Analysis

## Overview

Software-as-a-Service (SaaS) businesses operate under a subscription revenue model with distinct unit economics that require specialized metrics beyond traditional financial analysis. The key to SaaS valuation lies in understanding recurring revenue quality, customer retention dynamics, and the efficiency of growth investments.

## Table of Contents
1. [Core KPIs and Formulas](#core-kpis-and-formulas)
2. [Performance Benchmarks](#performance-benchmarks)
3. [Valuation Framework](#valuation-framework)
4. [Common Analytical Pitfalls](#common-analytical-pitfalls)
5. [Red Flags](#red-flags)
6. [Due Diligence Checklist](#due-diligence-checklist)

## Core KPIs and Formulas

### Revenue Metrics

**Annual Recurring Revenue (ARR)**
```
ARR = MRR * 12
where MRR = Monthly Recurring Revenue from active subscriptions
```
ARR excludes one-time fees, professional services, and usage-based overages unless contractually committed. Always verify whether reported ARR includes multi-year contract discounting.

**Net Revenue Retention (NRR)**
```
NRR = (Starting ARR + Expansion - Contraction - Churn) / Starting ARR
Measured over 12-month cohort
```
NRR measures revenue growth from existing customers, capturing both retention and expansion. Values above 100% indicate the installed base generates growth independent of new customer acquisition.

**Gross Revenue Retention (GRR)**
```
GRR = (Starting ARR - Contraction - Churn) / Starting ARR
```
GRR isolates pure retention by excluding expansion revenue. This metric reveals the true stickiness of the product, as it removes the masking effect of upselling.

### Unit Economics

**LTV:CAC Ratio**
```
LTV = (ARPU * Gross Margin) / Churn Rate
CAC = (Sales + Marketing Expense) / New Customers Acquired

LTV:CAC = LTV / CAC
```
For cohort-based analysis, use actual customer contribution margins over observed lifetimes rather than formula-derived estimates.

**CAC Payback Period**
```
CAC Payback (months) = CAC / (ARPU * Gross Margin)
Alternative: CAC / (Net New ARR per Customer * Gross Margin / 12)
```
Payback should be measured on a gross margin basis, not revenue basis, to reflect actual cash recovery.

**Rule of 40**
```
Rule of 40 = Revenue Growth Rate (%) + FCF Margin (%)
Alternative: ARR Growth Rate (%) + Operating Margin (%)
```

### Profitability Metrics

**Subscription Gross Margin**
```
Subscription Gross Margin = (Subscription Revenue - Cost of Revenue) / Subscription Revenue

Cost of Revenue includes:
- Hosting/infrastructure costs
- Customer support
- Professional services COGS
- Amortization of capitalized software
```

**Operating Efficiency**
```
Magic Number = Net New ARR (quarter) / Sales & Marketing Spend (prior quarter)
```
The one-quarter lag accounts for the typical sales cycle and ramp time.

## Performance Benchmarks

| Metric | Poor | Adequate | Good | Best-in-Class |
|--------|------|----------|------|---------------|
| NRR | <100% | 100-110% | 110-120% | >130% |
| GRR | <80% | 80-85% | 85-90% | >95% |
| LTV:CAC | <2:1 | 2-3:1 | 3-5:1 | >5:1 |
| CAC Payback | >24mo | 18-24mo | 12-18mo | <12mo |
| Subscription Gross Margin | <65% | 65-72% | 72-80% | >80% |
| Rule of 40 | <20 | 20-30 | 30-40 | >50 |
| Magic Number | <0.5 | 0.5-0.75 | 0.75-1.0 | >1.0 |
| Logo Churn (annual) | >15% | 10-15% | 5-10% | <5% |

## Valuation Framework

### EV/ARR Multiples

Base multiple ranges depend on growth profile and retention:

| Growth Profile | EV/ARR Range |
|----------------|--------------|
| <20% ARR growth | 2-4x |
| 20-40% ARR growth | 4-7x |
| 40-60% ARR growth | 7-12x |
| >60% ARR growth | 10-20x |

**NRR Premium Adjustment**
```
Adjusted Multiple = Base Multiple * (1 + (NRR - 100%) * 2)

Example: Base 8x with 125% NRR
Adjusted = 8 * (1 + 0.25 * 2) = 8 * 1.5 = 12x
```

**Rule of 40 Premium**
Companies exceeding Rule of 40 typically command 20-40% multiple premiums relative to peers with similar growth but lower profitability.

### DCF Considerations

For growth-stage SaaS, traditional DCF requires careful handling:
- Terminal growth rates should not exceed GDP growth (2-3%)
- Terminal margins should reflect scaled infrastructure businesses (20-30% FCF margin)
- Discount rates typically 10-15% depending on profitability visibility

### Scenario Analysis Framework

Weight scenarios by probability:
1. **Bull case (20%)**: Sustained NRR >120%, TAM expansion, improving unit economics
2. **Base case (60%)**: Gradual NRR compression to 110%, moderate growth deceleration
3. **Bear case (20%)**: Competitive pressure, NRR <100%, margin compression

## Common Analytical Pitfalls

### CAC Calculation Errors

**Problem**: Including only direct sales costs, excluding marketing overhead, sales operations, and allocated G&A.

**Correct approach**: Include fully-loaded sales and marketing expense. For enterprise deals, account for longer sales cycles by using average spend over the sales cycle length, not single-quarter spend.

**Problem**: Mixing blended CAC across segments with vastly different economics.

**Correct approach**: Calculate segment-specific CAC (SMB vs. Mid-Market vs. Enterprise) and weight by contribution.

### LTV Overestimation

**Problem**: Using implied churn from NRR formula rather than actual observed customer lifetimes.

**Correct approach**: Use cohort analysis with actual customer tenure data. Formula-derived LTV systematically overstates for businesses with non-linear churn patterns (high early churn, stable mature cohorts).

**Problem**: Assuming constant expansion rates that rely on aggressive upsell capacity.

**Correct approach**: Apply expansion decay assumptions as installed base matures and expansion opportunities within accounts diminish.

### Timing Inconsistencies

**Problem**: Comparing ARR at period end with expenses averaged over the period.

**Correct approach**: Use period-average ARR when calculating efficiency metrics, or annualize ending ARR only when growth is linear.

**Problem**: Recognizing multi-year contract ARR upfront while spreading costs.

**Correct approach**: Normalize multi-year deals to annual equivalent or analyze cohorts by contract structure separately.

### GAAP vs. Operating Metrics Divergence

Stock-based compensation can represent 15-30% of revenue for growth-stage SaaS. Always analyze:
- FCF margin including SBC dilution cost
- Operating margin with and without SBC
- Burn multiple (cash burned / net new ARR) for pre-profit companies

### Deferred Revenue Traps

Rising deferred revenue indicates strong billings but requires context:
- Lengthening payment terms inflate deferred revenue without improving economics
- Shift from monthly to annual billing mechanically increases deferred revenue
- Analyze billings growth alongside deferred revenue changes

## Red Flags

- NRR declining sequentially for 3+ quarters
- CAC payback extending while growth decelerates
- Gross margin compression from scaling costs (suggests infrastructure inefficiency)
- Rising sales cycle length without corresponding ACV increase
- Customer concentration >10% from single account
- Declining logo count while ARR grows (over-reliance on expansion)
- Professional services revenue growing faster than subscription (implementation complexity)
- Capitalized software costs growing faster than R&D (aggressive capitalization policy)

## Due Diligence Checklist

1. Reconcile ARR disclosure to GAAP subscription revenue
2. Verify NRR calculation methodology (gross vs. net, cohort definition)
3. Segment unit economics by customer size and geography
4. Analyze cohort retention curves, not just blended metrics
5. Stress-test LTV assumptions with bear case churn scenarios
6. Verify gross margin excludes hosting credits and one-time adjustments
7. Compare Rule of 40 using both GAAP operating margin and FCF margin
