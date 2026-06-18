# Relative Valuation: Multiples Framework

## Overview

Relative valuation determines what the market is willing to pay for similar companies, then applies those multiples to the target. It provides a market-based reality check and is faster than DCF, but reflects current market sentiment rather than intrinsic value.

## Table of Contents
1. [EV Multiples vs Equity Multiples](#ev-multiples-vs-equity-multiples)
2. [Multiple Selection Decision Tree](#multiple-selection-decision-tree)
3. [Peer Group Selection Criteria](#peer-group-selection-criteria)
4. [Required Adjustments](#required-adjustments)
5. [Applying Multiples](#applying-multiples)
6. [Guardrails and Limitations](#guardrails-and-limitations)
7. [Multiple Triangulation](#multiple-triangulation)
8. [Output Format](#output-format)

---

## EV Multiples vs Equity Multiples

| Multiple Type | Numerator | Appropriate Metric | When to Use |
|--------------|-----------|-------------------|-------------|
| **Enterprise Value** | EV | EBITDA, EBIT, Revenue, Unlevered FCF | Different capital structures, M&A, capital-intensive |
| **Equity Value** | Market Cap or Price | Net Income, EPS, Book Value | Similar leverage, financial institutions |

**Critical Rule**: Match the numerator to the denominator. EV multiples use pre-interest metrics; equity multiples use post-interest metrics.

### EV Calculation

```
Enterprise Value = Market Cap + Total Debt + Preferred Stock + Minority Interest - Cash
```

For operating leases, capitalize and add to EV (IFRS 16/ASC 842 already does this).

---

## Multiple Selection Decision Tree

```
START: What industry/business model?
|
|-- Capital-intensive or varying depreciation policies?
|   |-- YES --> EV/EBITDA (removes D&A distortions)
|   |-- NO --> Continue
|
|-- Pre-profit or high-growth company?
|   |-- YES --> EV/Revenue (only positive metric available)
|   |-- NO --> Continue
|
|-- Financial institution (bank, insurer, REIT)?
|   |-- YES --> P/Book Value or P/E
|   |-- NO --> Continue
|
|-- Stable, profitable company with similar leverage to peers?
|   |-- YES --> P/E acceptable
|   |-- NO --> EV/EBITDA preferred
|
DEFAULT: EV/EBITDA is the most universally applicable multiple
```

### Multiple Selection by Sector

| Sector | Primary Multiple | Secondary | Rationale |
|--------|-----------------|-----------|-----------|
| Technology (SaaS) | EV/Revenue, EV/ARR | EV/Gross Profit | Pre-profit; revenue visibility |
| Industrials | EV/EBITDA | EV/EBIT | Capital intensity varies |
| Consumer Retail | EV/EBITDA | P/E | Lease adjustments matter |
| Financials (Banks) | P/TBV, P/E | | Assets = liabilities structure |
| REITs | P/FFO, P/NAV | | FFO adjusts for non-cash |
| E-commerce | EV/GMV, EV/Revenue | | Scale economics |
| Oil & Gas | EV/EBITDAX, EV/Reserves | | Exploration costs |
| Biotech | EV/Pipeline NPV | | No earnings, binary outcomes |

---

## Peer Group Selection Criteria

Select 8-10 comparable companies based on similarity across these dimensions:

### Primary Criteria (Must Match)

1. **Industry/Business Model**: Same revenue drivers, cost structure
2. **Geography**: Similar regulatory and macro exposure
3. **Size**: Within 0.5x to 2x market cap (or revenue if pre-profit)

### Secondary Criteria (Weight by Importance)

4. **Growth Profile**: Similar revenue/earnings growth trajectory
5. **Profitability**: Comparable margins (within 500bps)
6. **Capital Structure**: Similar leverage ratios
7. **Asset Intensity**: Comparable CapEx/Revenue and ROA
8. **Customer Base**: B2B vs B2C, enterprise vs SMB
9. **Stage of Lifecycle**: Growth vs mature vs turnaround

### Peer Selection Process

| Step | Action | Output |
|------|--------|--------|
| 1 | Identify industry classification (GICS, SIC) | Initial universe (20-30) |
| 2 | Screen for size (0.5x-2x revenue) | Narrowed list (15-20) |
| 3 | Filter for business model similarity | Refined list (10-12) |
| 4 | Rank by growth/margin similarity | Final peer set (8-10) |
| 5 | Document exclusions | Rationale for removed names |

**Document Why Excluded**: Always note why potential peers were dropped (e.g., conglomerate structure, different end market, recent M&A distortion).

---

## Required Adjustments

### 1. Normalize Earnings

Remove one-time items to get clean operating performance:

| Adjustment | Add Back / Subtract |
|------------|---------------------|
| Restructuring charges | Add back |
| Litigation settlements | Add back (expense) / Subtract (gain) |
| Asset impairments | Add back |
| Gain/loss on asset sales | Normalize out |
| Stock-based compensation | Debated; consistency is key |
| M&A transaction costs | Add back |

**Consistency Rule**: Apply the same adjustments to all peers and the target.

### 2. Calendarize Financials

When fiscal years differ, adjust to common period:

```
Calendarized Metric = (Months Overlap / 12) * FY1 + (Remaining Months / 12) * FY2
```

Example: Target has June FY, peers have December FY:
- Use H2 of prior FY + H1 of current FY for alignment

### 3. Accounting Differences

| Issue | Adjustment |
|-------|------------|
| Lease accounting (pre-IFRS 16) | Capitalize operating leases, add to debt |
| R&D capitalization | Expense or capitalize consistently |
| Inventory methods (LIFO/FIFO) | LIFO reserve adjustment |
| Pension accounting | Adjust for unfunded liabilities |
| Revenue recognition | Note differences, may not be adjustable |

### 4. Capital Structure Adjustments

For EV multiples, ensure EV calculation is consistent:
- Include all debt-like items (convertibles, preferred, operating leases, pensions)
- Subtract only true excess cash (not operating cash)

---

## Applying Multiples

### Trading Multiples (Public Comparables)

```
Implied Value = Target Metric * Peer Median Multiple
```

Use median (not mean) to reduce outlier influence.

| Statistic | When to Use |
|-----------|-------------|
| Median | Default; robust to outliers |
| Mean | Tight peer group, no outliers |
| Interquartile range | Show valuation range |

### Transaction Multiples (Precedent Transactions)

- Includes control premium (typically 20-40%)
- Use for M&A scenarios
- Adjust for market conditions at transaction time
- More relevant for private company valuations

---

## Guardrails and Limitations

### When Multiples Mislead

| Situation | Problem | Mitigation |
|-----------|---------|------------|
| Negative earnings | P/E undefined | Use EV/Revenue or EV/Gross Profit |
| Different growth rates | Higher growth deserves higher multiple | Adjust using PEG or growth-adjusted multiple |
| Cyclical peak/trough | Earnings distorted | Use mid-cycle normalized earnings |
| Different accounting | Multiples not comparable | Adjust to common basis |
| Small peer universe | Statistical noise | Widen criteria or weight by similarity |

### Premium/Discount Framework

Justify why target should trade at premium or discount to peers:

| Factor | Premium Justification | Discount Justification |
|--------|----------------------|------------------------|
| Growth | Faster than peers | Slower than peers |
| Margins | Higher and defensible | Lower, structurally challenged |
| ROIC | Superior capital efficiency | Below cost of capital |
| Management | Proven track record | Governance concerns |
| Balance sheet | Fortress, optionality | Overleveraged, refinancing risk |
| Market position | #1 with moat | Subscale, market share loss |

---

## Multiple Triangulation

Never rely on a single multiple. Use multiple approaches and triangulate:

| Method | Multiple | Implied Value | Weight |
|--------|----------|---------------|--------|
| Trading comps | EV/EBITDA | $XX | 40% |
| Trading comps | P/E | $XX | 20% |
| Transaction comps | EV/EBITDA | $XX | 20% |
| DCF | N/A | $XX | 20% |
| **Weighted Value** | | **$XX** | |

---

## Output Format

Present relative valuation as:

1. **Peer group table**: Ticker, market cap, multiples, growth, margins
2. **Median/mean statistics**: For each multiple
3. **Implied valuation range**: Low (25th percentile), mid (median), high (75th percentile)
4. **Premium/discount discussion**: Why target differs from median
5. **Football field chart**: Visual range across methodologies
