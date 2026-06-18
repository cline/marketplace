# Energy Sector Reference

## Sector Overview

The energy sector encompasses companies involved in exploration, production, refining, transportation, and marketing of oil, natural gas, and renewable energy. Each subsector operates with distinct economics, risk profiles, and valuation methodologies requiring specialized analytical approaches.

Key subsectors include:
- Upstream Exploration and Production (E&P)
- Midstream Infrastructure
- Downstream Refining and Marketing
- Integrated Oil Companies
- Oilfield Services and Equipment
- Renewable Energy and Clean Tech

## Table of Contents
1. [Upstream Exploration and Production](#upstream-exploration-and-production)
2. [Midstream Infrastructure](#midstream-infrastructure)
3. [Downstream Refining](#downstream-refining)
4. [Oilfield Services](#oilfield-services)
5. [Renewable Energy](#renewable-energy)
6. [Common Modeling Pitfalls](#common-modeling-pitfalls)
7. [Valuation Summary by Subsector](#valuation-summary-by-subsector)

## Upstream Exploration and Production

### Critical KPIs

| Metric | Definition | Healthy Range |
|--------|------------|---------------|
| Production Growth | YoY change in BOE/d | 3 - 10% (growth), 0 - 3% (mature) |
| Finding & Development Costs | Capex / Reserves Added | < $15/BOE (onshore), < $25/BOE (offshore) |
| Reserve Replacement Ratio | Reserves Added / Production | > 100% |
| Reserve Life Index | Proved Reserves / Annual Production | 8 - 15 years |
| Lease Operating Expense | Per BOE production cost | Basin-specific |
| All-in Breakeven | Full-cycle cost per BOE | < $50/BBL for profitability |

### Basin-Specific Breakevens

| Basin | WTI Breakeven | Key Characteristics |
|-------|---------------|---------------------|
| Permian (Delaware) | $35 - $45 | Highest productivity, multi-zone |
| Permian (Midland) | $38 - $48 | Mature development, infill risk |
| Bakken | $45 - $55 | Gas capture challenges |
| Eagle Ford | $40 - $50 | Oil/gas optionality |
| DJ Basin | $40 - $50 | Regulatory risk |
| Haynesville | $2.50 - $3.00/MCF | Pure gas play |
| Marcellus | $2.00 - $2.50/MCF | Lowest cost gas |

### NAV Valuation (PV-10)

Net Asset Value using PV-10 methodology represents the present value of future net revenues from proved reserves discounted at 10%.

| Component | Calculation |
|-----------|-------------|
| Proved Developed Producing (PDP) | Highest certainty, lowest risk discount |
| Proved Developed Non-Producing (PDNP) | Moderate discount for reactivation risk |
| Proved Undeveloped (PUD) | Highest discount for execution and capital risk |

**NAV Calculation**:
```
NAV = PDP Value + (PDNP Value x 0.8) + (PUD Value x 0.5) + Probable Value (risked) - Net Debt
```

Apply commodity price sensitivity analysis. A $5/BBL change in oil price typically moves NAV by 15-25%.

### E&P Valuation Multiples

| Metric | Low | Mid | High |
|--------|-----|-----|------|
| EV/EBITDAX | 3.0x | 4.0 - 5.0x | 6.0x+ |
| EV/BOE/D (flowing) | $25,000 | $35,000 - $50,000 | $70,000+ |
| EV/Proved Reserves | $5/BOE | $8 - $12/BOE | $15/BOE+ |
| Price/NAV | 0.6x | 0.8 - 1.0x | 1.2x+ |

## Midstream Infrastructure

### Business Model Fundamentals

Midstream companies generate revenue from gathering, processing, transporting, and storing hydrocarbons. Cash flow stability depends on contract structure.

| Contract Type | Volume Risk | Commodity Risk | Margin Stability |
|---------------|-------------|----------------|------------------|
| Fee-Based | Low | None | High |
| Cost-of-Service | Low | None | High |
| Percent-of-Proceeds | Medium | High | Low |
| Keep-Whole | Medium | High | Low |
| Percent-of-Index | Low | Medium | Medium |

Target fee-based contract exposure above 80% for defensive positioning.

### Critical KPIs

| Metric | Definition | Healthy Range |
|--------|------------|---------------|
| Distribution Coverage | DCF / Distributions | > 1.1x |
| Debt/EBITDA | Leverage ratio | < 4.0x |
| Contract Tenor | Weighted avg remaining term | > 5 years |
| Recontracting Risk | % contracts expiring in 2 years | < 20% |
| Volume Growth | Throughput change YoY | Aligned with basin activity |
| Capex/EBITDA | Growth investment intensity | 0.3 - 0.6x (growth), < 0.3x (mature) |

### Midstream Valuation

| Metric | Gathering & Processing | Pipelines | Terminals |
|--------|----------------------|-----------|-----------|
| EV/EBITDA | 6.0 - 9.0x | 8.0 - 12.0x | 10.0 - 14.0x |
| DCF Yield | 10 - 14% | 7 - 10% | 6 - 9% |
| Distribution Yield | 6 - 10% | 5 - 8% | 4 - 7% |

Apply discounts for:
- Volume concentration with single producer (2-3x discount)
- Commodity exposure above 20% (1-2x discount)
- Leverage above 4.5x (1-2x discount)

## Downstream Refining

### Critical KPIs

| Metric | Definition | Healthy Range |
|--------|------------|---------------|
| Crack Spread | Product price - crude price | $10 - $25/BBL (mid-cycle) |
| Refinery Utilization | Throughput / Capacity | > 90% |
| Nelson Complexity Index | Refinery upgrade capability | > 10 (advantaged) |
| Capture Rate | Actual margin / benchmark crack | > 90% |
| Turnaround Timing | Maintenance scheduling | Q1/Q4 (avoiding summer demand) |

### Regional Crack Spread Benchmarks

| Region | Benchmark | Mid-Cycle Range |
|--------|-----------|-----------------|
| US Gulf Coast | LLS 3-2-1 | $12 - $18/BBL |
| US Midwest | WTI 3-2-1 | $14 - $20/BBL |
| US West Coast | ANS 5-3-1-1 | $18 - $28/BBL |
| Northwest Europe | Dated Brent | $8 - $14/BBL |
| Singapore | Dubai | $6 - $12/BBL |

### Refining Valuation

| Metric | Simple Refinery | Complex Refinery |
|--------|-----------------|------------------|
| Mid-Cycle EV/EBITDA | 3.5 - 5.0x | 5.0 - 7.0x |
| EV/Complexity Barrel | $2,000 - $4,000 | $5,000 - $8,000 |
| Replacement Cost Multiple | 0.4 - 0.6x | 0.6 - 0.9x |

Normalize earnings to mid-cycle crack spreads. Current period earnings at peak spreads overstate intrinsic value.

## Oilfield Services

### Critical KPIs

| Metric | Definition | Healthy Range |
|--------|------------|---------------|
| Rig Count Correlation | Revenue sensitivity to active rigs | Track vs. Baker Hughes data |
| Fleet Utilization | Active equipment / Total fleet | > 80% |
| Pricing Index | Day rates / equipment rates | Cycle-dependent |
| Backlog | Contracted future revenue | > 1x annual revenue |
| Free Cash Flow Yield | FCF / Market Cap | > 8% mid-cycle |

### OFS Valuation

| Segment | Trough | Mid-Cycle | Peak |
|---------|--------|-----------|------|
| Drilling Contractors | 3.0 - 4.0x | 5.0 - 7.0x | 8.0 - 10.0x |
| Pressure Pumping | 2.5 - 4.0x | 5.0 - 6.5x | 7.0 - 9.0x |
| Completion Equipment | 4.0 - 6.0x | 7.0 - 9.0x | 10.0 - 12.0x |
| Production Equipment | 5.0 - 7.0x | 8.0 - 10.0x | 11.0 - 14.0x |

OFS earnings exhibit extreme cyclicality. Use through-cycle valuation with normalized margins and activity levels.

## Renewable Energy

### Critical KPIs

| Metric | Definition | Healthy Range |
|--------|------------|---------------|
| Contracted Capacity | MW under PPA | > 80% |
| PPA Tenor | Weighted avg contract life | > 10 years |
| Capacity Factor | Actual / Theoretical output | 25 - 35% (solar), 35 - 45% (wind) |
| Levelized Cost of Energy | All-in cost per MWh | Competitive with grid |
| Development Pipeline | MW in development stages | > 50% of operating capacity |
| Tax Equity Capacity | ITC/PTC monetization | Sufficient for growth plan |

### Renewable Valuation

| Stage | Valuation Approach | Typical Range |
|-------|-------------------|---------------|
| Operating (Contracted) | DCF at 6-8% WACC | $1.2 - $1.8M/MW |
| Construction | Risked DCF (80-90% probability) | $0.8 - $1.2M/MW |
| Development (Permitted) | Risked DCF (50-70% probability) | $0.3 - $0.6M/MW |
| Development (Early) | Risked DCF (20-40% probability) | $0.05 - $0.15M/MW |

Contracted cash flows from investment-grade counterparties warrant utility-like discount rates. Merchant exposure requires higher discount rates reflecting commodity and basis risk.

## Common Modeling Pitfalls

### E&P Reserve Extrapolation

Mistake: Assuming reserve replacement continues at historical rates indefinitely.

Reality: Proved reserves face decline without continuous investment. Model reserve additions explicitly based on capital program and drilling inventory depth. Validate type curves against actual well performance.

### Midstream Volume Assumptions

Mistake: Modeling volume growth independent of basin activity and producer economics.

Reality: Midstream volumes depend on upstream capital allocation. Track producer hedging, leverage, and breakevens in the basin. Volume growth assumptions must align with producer activity forecasts.

### Refining Margin Normalization

Mistake: Using current or recent crack spreads for terminal value.

Reality: Refining margins exhibit strong mean reversion. Use 10-year average crack spreads for normalized earnings. Current spreads above historical ranges will not persist.

### OFS Cycle Timing

Mistake: Assuming current activity levels represent sustainable demand.

Reality: OFS activity follows E&P capital cycles with a lag. Oil price changes translate to activity changes with 6-12 month delay. Model based on E&P capital budget announcements, not current spot prices.

## Valuation Summary by Subsector

| Subsector | Primary Method | Secondary Method | Key Driver |
|-----------|---------------|------------------|------------|
| E&P | NAV (PV-10) | EV/EBITDAX | Commodity prices, reserves |
| Midstream | DCF Yield | EV/EBITDA | Contract quality, leverage |
| Refining | Mid-cycle EV/EBITDA | Replacement cost | Crack spreads, utilization |
| OFS | Through-cycle EV/EBITDA | EV/Revenue | Activity levels, pricing |
| Renewables | DCF on contracted | EV/MW | PPA quality, pipeline |
