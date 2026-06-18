# Sum-of-the-Parts Valuation

## Overview

Sum-of-the-Parts (SOTP) valuation disaggregates a diversified company into its constituent businesses, values each independently, and aggregates to derive total enterprise value. This approach reveals hidden value (or destruction) within conglomerates and multi-segment companies.

## Table of Contents
1. [When to Use SOTP](#when-to-use-sotp)
2. [Segment Identification](#segment-identification)
3. [Segment Valuation Methodology](#segment-valuation-methodology)
4. [Conglomerate Discount Analysis](#conglomerate-discount-analysis)
5. [Adjustments](#adjustments)
6. [SOTP Summary Table](#sotp-summary-table)
7. [Catalyst Identification](#catalyst-identification)
8. [Output Format](#output-format)

---

## When to Use SOTP

SOTP is appropriate when:

| Criterion | Rationale |
|-----------|-----------|
| **Diversified segments** | Segments operate in different industries with different valuation characteristics |
| **Segment financials available** | Company reports segment revenue, EBITDA, or operating income |
| **Different growth profiles** | High-growth segment obscured by mature segment (or vice versa) |
| **Potential breakup candidate** | Activist pressure, strategic review, spin-off speculation |
| **Hidden asset value** | Real estate, investments, or IP not reflected in consolidated multiples |
| **Acquisition analysis** | Buyer interested in specific segment only |

SOTP is less useful when:
- Segments are highly integrated with shared infrastructure
- Segment reporting lacks profitability detail
- Company operates single focused business

---

## Segment Identification

### Step 1: Define Segments

Use company-reported segments as the starting point. Supplement with:

| Source | Information Provided |
|--------|---------------------|
| 10-K segment disclosures | Revenue, operating income, assets by segment |
| Investor presentations | Management's view of business units |
| Industry classifications | Appropriate peer groups for each segment |
| M&A precedents | How similar divisions were valued in transactions |

### Step 2: Map Segments to Peer Groups

Each segment requires its own comparable company set:

| Company Segment | Comparable Universe | Primary Multiple |
|----------------|---------------------|------------------|
| Segment A: Software | Pure-play enterprise software | EV/Revenue |
| Segment B: Hardware | Hardware/components manufacturers | EV/EBITDA |
| Segment C: Services | IT services providers | EV/EBIT |

---

## Segment Valuation Methodology

Value each segment using the most appropriate method:

### Method 1: Comparable Company Multiples

```
Segment EV = Segment Metric * Peer Median Multiple
```

| Segment | Metric | Multiple | Peer Median | Segment EV |
|---------|--------|----------|-------------|------------|
| A | Revenue | EV/Rev | 5.0x | $X |
| B | EBITDA | EV/EBITDA | 8.0x | $Y |
| C | EBIT | EV/EBIT | 12.0x | $Z |

### Method 2: DCF per Segment

For segments with sufficient disclosure, build standalone DCF:
- Segment-specific growth rates and margins
- Segment-appropriate WACC (different risk profiles)
- Standalone capital structure assumptions

### Method 3: Transaction Multiples

Use precedent transactions for segments with M&A activity:
- Acquisitions of similar businesses
- Includes control premium
- Adjust for transaction timing and market conditions

---

## Conglomerate Discount Analysis

Diversified companies typically trade at a discount to SOTP value.

### Typical Discount Range

| Discount Level | Typical Range | Characteristics |
|---------------|---------------|-----------------|
| Minimal | 0-10% | Focused conglomerate, synergies evident |
| Moderate | 10-20% | Some diversification, decent disclosure |
| Significant | 20-30% | True conglomerate, limited synergies |
| Severe | 30%+ | Governance issues, capital misallocation |

### Discount Drivers

| Factor | Increases Discount | Decreases Discount |
|--------|-------------------|-------------------|
| Transparency | Poor segment disclosure | Detailed reporting |
| Capital allocation | Cross-subsidization | Disciplined reinvestment |
| Synergies | None evident | Clear cost/revenue synergies |
| Management | Conglomerate mentality | Segment accountability |
| Activism potential | Entrenched, defensive | Open to strategic review |
| Complexity | Too many segments | Coherent portfolio |

### Calculating Implied Discount

```
Implied Discount = 1 - (Current EV / SOTP EV)
```

If discount exceeds historical or peer norms, potential catalyst for value realization.

---

## Adjustments

After summing segment values, apply corporate-level adjustments:

### 1. Corporate Overhead

```
Corporate Overhead PV = Annual Overhead / WACC
```

Or capitalize at 6-8x annual overhead as a deduction.

| Item | Treatment |
|------|-----------|
| Corporate SG&A | Deduct present value |
| Shared services | Allocate to segments or deduct centrally |
| Stranded costs post-breakup | Estimate and deduct if analyzing spin-off |

### 2. Net Debt

```
SOTP Equity Value = Sum of Segment EVs - Corporate Overhead PV - Net Debt
```

Allocate debt to segments if segment-specific, otherwise deduct at corporate level.

### 3. Minority Interests

- Deduct at fair value (not book)
- Value minority stake using segment multiple
- Common in JVs and partially-owned subsidiaries

### 4. Other Adjustments

| Item | Treatment |
|------|-----------|
| Pension deficit | Deduct unfunded liability |
| Tax assets (NOLs) | Add present value if usable |
| Investments/Associates | Add at fair value or proportional EV |
| Excess real estate | Add appraised value |
| Contingent liabilities | Deduct expected value |

---

## SOTP Summary Table

| Component | Value | Method |
|-----------|-------|--------|
| Segment A | $X | EV/Revenue @ 5.0x |
| Segment B | $Y | EV/EBITDA @ 8.0x |
| Segment C | $Z | DCF |
| **Gross SOTP EV** | **$XX** | |
| Less: Corporate overhead | ($A) | 7x annual |
| Less: Net debt | ($B) | Book value |
| Less: Minority interest | ($C) | Fair value |
| Less: Pension deficit | ($D) | Unfunded |
| **SOTP Equity Value** | **$YY** | |
| Shares outstanding | #M | Diluted |
| **SOTP per Share** | **$ZZ** | |
| Current price | $PP | |
| **Implied Discount** | XX% | |

---

## Catalyst Identification

SOTP valuation is most actionable when catalysts exist to close the discount:

| Catalyst | Mechanism |
|----------|-----------|
| Spin-off | Tax-free separation, pure-play re-rating |
| Divestiture | Sale of segment, cash return to shareholders |
| Activist involvement | Pressure for strategic alternatives |
| Management change | New CEO with simplification mandate |
| IPO of segment | Establishes public market value |
| Strategic review | Board-initiated portfolio evaluation |

---

## Output Format

Present SOTP analysis as:

1. **Segment breakdown table**: Revenue, EBITDA, multiple, segment EV
2. **Peer group detail**: Comps used for each segment with rationale
3. **Adjustments bridge**: Corporate costs, debt, minorities
4. **SOTP equity value and per-share value**
5. **Implied discount vs current price**
6. **Catalyst discussion**: What could close the gap
