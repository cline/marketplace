# Healthcare Sector: Pharma and Biotech Analysis

## Overview

Pharmaceutical and biotechnology companies present unique valuation challenges due to binary clinical trial outcomes, patent cliffs, long development timelines, and highly uncertain revenue projections. Traditional earnings-based valuation fails to capture pipeline optionality. The standard approach uses risk-adjusted net present value (rNPV) to probability-weight future cash flows based on clinical and regulatory success rates.

## Table of Contents
1. [Core KPIs and Formulas](#core-kpis-and-formulas)
2. [Performance Benchmarks](#performance-benchmarks)
3. [Clinical Trial Success Rates by Indication](#clinical-trial-success-rates-by-indication)
4. [Pipeline NPV Methodology](#pipeline-npv-methodology)
5. [Valuation Framework](#valuation-framework)
6. [Common Analytical Pitfalls](#common-analytical-pitfalls)
7. [Red Flags](#red-flags)
8. [Due Diligence Checklist](#due-diligence-checklist)

## Core KPIs and Formulas

### Pipeline Metrics

**Risk-Adjusted Net Present Value (rNPV)**
```
rNPV = Sum of [Probability * (Revenue_t - Cost_t) / (1+r)^t] - Development Costs

For each asset:
rNPV = (Peak Sales * Duration Factor * Margin) * PTRS / (1+r)^years_to_launch - Remaining Development Cost
```

**Probability of Technical and Regulatory Success (PTRS)**

PTRS represents the cumulative probability of reaching market from current development stage:

| Current Phase | PTRS to Approval |
|---------------|------------------|
| Preclinical | 5-8% |
| Phase I | 10-15% |
| Phase II | 15-25% |
| Phase III | 50-70% |
| Filed/Under Review | 85-95% |

Note: PTRS varies significantly by therapeutic area and modality.

**Phase Transition Success Rates**

| Transition | Historical Average | Range by Indication |
|------------|-------------------|---------------------|
| Phase I to II | 60-65% | 50-75% |
| Phase II to III | 30-35% | 20-50% |
| Phase III to Approval | 55-65% | 40-80% |
| Overall (Phase I to Approval) | 9-14% | 5-25% |

Oncology typically at lower end; vaccines and anti-infectives at higher end.

### Commercial Metrics

**Loss of Exclusivity (LOE) Exposure**
```
LOE Exposure = Revenue from products losing exclusivity within N years / Total Revenue
```
Typically analyzed over 3-5 year windows. Healthy exposure <15% of revenue at risk in any single year.

**Peak Sales Estimation**
```
Peak Sales = Patient Population * Diagnosis Rate * Treatment Rate * Market Share * Price * Compliance
```

**Revenue Durability**
```
Weighted Average Patent Life = Sum of (Product Revenue * Years to LOE) / Total Revenue
```

### R&D Productivity

**R&D IRR (Internal Rate of Return)**
```
R&D IRR = Rate where NPV of launched product revenues equals cumulative R&D investment

Solve for r: Sum of [Revenue_t / (1+r)^t] = Total R&D Cost
```
Industry average R&D IRR has declined from >10% historically to approximately 1-5% in recent years.

**Cost per Approval**
```
Cost per NME Approval = Total R&D Spend over period / Number of NME Approvals

Industry average: $1.5-2.5 billion per approved drug (fully capitalized)
```

## Performance Benchmarks

| Metric | Concerning | Adequate | Strong | Excellent |
|--------|------------|----------|--------|-----------|
| LOE Exposure (3yr) | >30% | 20-30% | 10-20% | <10% |
| Pipeline PTRS-weighted NPV / Market Cap | <0.2x | 0.2-0.5x | 0.5-1.0x | >1.0x |
| R&D / Revenue | <10% | 10-15% | 15-20% | 15-25% |
| R&D IRR | <0% | 0-5% | 5-10% | >10% |
| Late-stage pipeline assets | 0-2 | 3-5 | 6-10 | >10 |
| Gross Margin | <60% | 60-70% | 70-80% | >80% |

## Clinical Trial Success Rates by Indication

| Therapeutic Area | Phase II to III | Overall (Ph I to Approval) |
|------------------|-----------------|---------------------------|
| Oncology (solid tumor) | 25-30% | 5-8% |
| Oncology (hematologic) | 35-40% | 10-12% |
| Immunology/Inflammation | 30-35% | 10-15% |
| CNS/Neurology | 25-30% | 6-10% |
| Cardiovascular | 35-40% | 8-12% |
| Infectious Disease | 45-55% | 15-20% |
| Rare Disease/Orphan | 40-50% | 15-25% |
| Vaccines | 50-60% | 20-30% |

## Pipeline NPV Methodology

### Step-by-Step rNPV Calculation

**1. Estimate Peak Sales**
```
Addressable Population (diagnosed, treated)
x Market share assumption (10-40% for first-in-class, 5-15% for me-too)
x Annual price ($50K-$500K+ depending on indication)
= Peak Annual Revenue
```

**2. Build Revenue Curve**
- Launch year based on trial timeline + regulatory review
- Ramp to peak over 3-5 years (faster for orphan, slower for primary care)
- Duration at peak: 3-7 years depending on competitive dynamics
- Post-LOE decline: 70-90% erosion over 2-3 years

**3. Apply Development Costs**
```
Phase I: $15-30M
Phase II: $30-100M
Phase III: $100-400M (more for large CV/outcomes trials)
Regulatory: $10-20M
```

**4. Calculate NPV with Stage-Appropriate Discount Rate**

| Stage | Discount Rate |
|-------|---------------|
| Preclinical | 40-50% |
| Phase I | 30-40% |
| Phase II | 20-30% |
| Phase III | 15-20% |
| Filed/Approved | 10-12% |

**5. Apply PTRS**
```
rNPV = NPV * PTRS
```

### Portfolio Aggregation

```
Total Pipeline Value = Sum of individual asset rNPVs

Equity Value = Commercial Business Value + Pipeline Value - Net Debt
```

## Valuation Framework

### Sum-of-Parts rNPV

The standard pharma/biotech valuation:

```
Enterprise Value =
  NPV of Existing Products (DCF to LOE) +
  rNPV of Pipeline Assets +
  Terminal Value of Platform/R&D Capability

Equity Value = EV - Net Debt - Preferred - Minority Interests
```

**Existing Products**: DCF with high confidence, low discount rate (8-10%), explicit modeling through patent expiry.

**Pipeline Assets**: rNPV with probability weighting and stage-appropriate discount rates.

**Terminal Value**: Represents ongoing R&D platform value. Can be:
- Perpetuity on normalized R&D spend with assumed return
- Multiple of projected pipeline assets
- Often 10-20% of total value

### Comparable Company Analysis

Use with caution given pipeline heterogeneity:

| Stage | Common Multiples |
|-------|------------------|
| Large-cap pharma | EV/EBITDA (8-12x), P/E (12-18x) |
| Mid-cap biotech | EV/Revenue (3-8x), Price/Pipeline |
| Early-stage biotech | Price/Cash (implies burn runway), EV/Lead Asset Value |

### Scenario Analysis

Given binary outcomes, scenario analysis is essential:

```
Expected Value = P(success) * Success Value + P(failure) * Failure Value

Success Value = rNPV with PTRS = 100%
Failure Value = Cash - Remaining development obligations
```

## Common Analytical Pitfalls

### Flat Discount Rates Across Pipeline

**Problem**: Applying uniform 10-12% discount rate to all pipeline assets regardless of stage.

**Impact**: Massively overvalues early-stage assets. A preclinical asset with 5% PTRS requires 40-50% discount rate to reflect risk; using 10% overstates value by 3-5x.

**Correct approach**: Use stage-appropriate discount rates that decline as assets de-risk through development.

### Ignoring Loss of Exclusivity Dynamics

**Problem**: Extrapolating current product revenue without explicit LOE modeling.

**Impact**: Overvalues near-term revenue, ignores looming patent cliffs.

**Correct approach**:
- Model each product explicitly through its LOE date
- Apply post-LOE erosion assumptions (70-90% decline)
- Assess biosimilar vs. generic competition differently (biosimilars erode slower)

### Modality-Blind Success Rates

**Problem**: Applying overall industry PTRS to novel modalities (cell therapy, gene therapy, RNA therapeutics).

**Impact**: Misprices risk for modalities with limited historical data.

**Correct approach**:
- Use modality-specific success rates where available
- Apply additional uncertainty premium for novel mechanisms
- Consider manufacturing and delivery challenges specific to modality

### Peak Sales Overestimation

**Problem**: Assuming 30%+ market share for competitive indications or pricing without payor pushback.

**Common errors**:
- Ignoring competitive launches during development timeline
- Assuming full label without restrictions
- Underestimating payor access barriers
- Projecting US pricing for global markets

**Correct approach**:
- Explicitly model competitive landscape evolution
- Apply probability-weighted label scenarios
- Build in access/discount assumptions by market
- Validate peak sales against therapeutic area benchmarks

### Ignoring Development Timeline Risk

**Problem**: Using management guidance for trial completion without slippage buffer.

**Reality**: Phase III trials frequently face 6-18 month delays from enrollment challenges, protocol amendments, and regulatory requests.

**Correct approach**: Add 6-12 month buffer to disclosed timelines; this affects both NPV timing and competitive dynamics.

## Red Flags

- LOE concentration with >25% revenue at risk in single year
- Repeated late-stage trial failures indicating platform issues
- Declining R&D productivity without strategic pivot
- Heavy reliance on single asset for pipeline value
- Accelerated approval without confirmatory trial clarity
- Management projections materially above analyst consensus
- M&A strategy focused on revenue replacement vs. innovation
- Manufacturing capacity constraints for biologic assets
- Deteriorating pricing/access trends in core franchises
- Clinical hold or FDA warning letters

## Due Diligence Checklist

1. Map complete pipeline with development stage, indication, and timeline
2. Verify PTRS assumptions against indication-specific historical rates
3. Model each major asset's peak sales with explicit assumptions
4. Apply stage-appropriate discount rates to pipeline rNPV
5. Build LOE waterfall for next 10 years
6. Stress-test peak sales with competitive scenario analysis
7. Verify manufacturing capacity and supply chain for lead assets
8. Assess IP landscape (freedom to operate, patent strength)
9. Review regulatory interactions and guidance letter content
10. Analyze payor coverage and access trends in target indications
11. Benchmark R&D productivity against therapeutic area peers
12. Evaluate management track record on clinical development execution
