# Financial Services Sector: Banks Analysis

## Overview

Banks operate fundamentally different business models than industrial companies. Their primary asset is their balance sheet, and profitability derives from the spread between funding costs and asset yields while managing credit, interest rate, and liquidity risks. Traditional valuation approaches (DCF, EV/EBITDA) fail for banks due to the nature of debt as an operating liability and regulatory capital constraints that limit growth capacity.

## Table of Contents
1. [Core KPIs and Formulas](#core-kpis-and-formulas)
2. [Performance Benchmarks](#performance-benchmarks)
3. [Why Traditional DCF Fails for Banks](#why-traditional-dcf-fails-for-banks)
4. [Valuation Framework](#valuation-framework)
5. [Common Analytical Pitfalls](#common-analytical-pitfalls)
6. [Red Flags](#red-flags)
7. [Due Diligence Checklist](#due-diligence-checklist)

## Core KPIs and Formulas

### Profitability Metrics

**Net Interest Margin (NIM)**
```
NIM = Net Interest Income / Average Earning Assets

Net Interest Income = Interest Income - Interest Expense
Earning Assets = Loans + Securities + Interest-bearing deposits at other banks
```
Express as percentage, typically annualized from quarterly figures.

**Net Interest Income (NII)**
```
NII = (Average Earning Assets * Asset Yield) - (Average Interest-bearing Liabilities * Funding Cost)
```
NII is the core driver of bank profitability. Analyze NII changes by decomposing into volume (balance sheet growth) and rate (spread) components.

**Return on Tangible Common Equity (ROTCE)**
```
ROTCE = Net Income to Common / Average Tangible Common Equity

Tangible Common Equity = Total Equity - Preferred Equity - Goodwill - Intangible Assets
```
ROTCE is the primary profitability benchmark for banks, as it reflects returns on the capital base that absorbs losses.

**Pre-Provision Net Revenue (PPNR)**
```
PPNR = Net Revenue - Non-interest Expense
     = NII + Non-interest Income - Non-interest Expense
```
PPNR measures earning power before credit costs, useful for comparing banks across credit cycles.

**Efficiency Ratio**
```
Efficiency Ratio = Non-interest Expense / (NII + Non-interest Income)
```
Lower is better. Measures operating leverage and expense discipline.

### Asset Quality Metrics

**Provision for Credit Losses (PCL) Ratio**
```
PCL Ratio = Provision for Credit Losses / Average Loans
```
Express as annualized percentage. Provisions represent management's estimate of expected credit losses.

**Non-Performing Loan (NPL) Ratio**
```
NPL Ratio = Non-performing Loans / Total Loans

Non-performing = 90+ days past due or non-accrual
```

**Allowance Coverage Ratio**
```
Coverage Ratio = Allowance for Credit Losses / Non-performing Loans
```
Higher coverage indicates greater cushion against realized losses.

**Net Charge-Off (NCO) Ratio**
```
NCO Ratio = (Gross Charge-offs - Recoveries) / Average Loans
```
NCOs represent actual realized losses, while provisions are forward-looking estimates.

### Capital and Liquidity

**Common Equity Tier 1 (CET1) Ratio**
```
CET1 Ratio = Common Equity Tier 1 Capital / Risk-Weighted Assets
```
Primary regulatory capital measure. Minimum requirements typically 4.5% plus buffers; well-capitalized banks target 10-13%.

**Tangible Book Value (TBV) Per Share**
```
TBV per Share = Tangible Common Equity / Diluted Shares Outstanding
```

**Loan-to-Deposit Ratio (LDR)**
```
LDR = Total Loans / Total Deposits
```
Indicates funding stability and growth capacity. Very high LDR (>100%) signals reliance on wholesale funding.

## Performance Benchmarks

| Metric | Poor | Adequate | Good | Excellent |
|--------|------|----------|------|-----------|
| ROTCE | <8% | 8-12% | 12-15% | >15% |
| NIM | <2.5% | 2.5-3.0% | 3.0-3.5% | >3.5% |
| Efficiency Ratio | >65% | 60-65% | 55-60% | <55% |
| CET1 Ratio | <10% | 10-11% | 11-12% | >12% |
| NPL Ratio | >3% | 2-3% | 1-2% | <1% |
| NCO Ratio | >1.5% | 1.0-1.5% | 0.5-1.0% | <0.5% |
| Coverage Ratio | <100% | 100-125% | 125-175% | >175% |
| LDR | >100% | 90-100% | 80-90% | 70-85% |

## Why Traditional DCF Fails for Banks

### Debt is an Operating Liability

For industrial companies, debt is a financing decision separable from operations. For banks, deposits and wholesale borrowings are the raw material of the business. You cannot calculate enterprise value or unlevered free cash flow in a meaningful way because removing debt removes the business itself.

### Regulatory Capital Constraints

Bank growth is constrained by capital requirements, not just profitable opportunities. A bank earning high returns cannot simply reinvest all earnings; it must maintain regulatory capital ratios. This makes standard growth assumptions inappropriate.

### Interest Expense is Operating Cost

Interest expense for banks is analogous to COGS for manufacturers. EBIT and EBITDA metrics are meaningless because they exclude the primary operating cost.

### Cash Flow Distortions

Bank cash flow statements are distorted by:
- Loan originations and payoffs (operating cash flow)
- Securities purchases (investing vs. operating ambiguity)
- Deposit flows (financing vs. operating)

Free cash flow as traditionally calculated has no coherent meaning for banks.

## Valuation Framework

### Price-to-Tangible Book Value (P/TBV)

The primary valuation metric for banks. Fair P/TBV is a function of ROTCE relative to cost of equity:

```
Fair P/TBV = (ROTCE - g) / (CoE - g)

Simplified (assuming g = 0): P/TBV = ROTCE / CoE
```

| ROTCE | Implied P/TBV (10% CoE) |
|-------|-------------------------|
| 8% | 0.8x |
| 10% | 1.0x |
| 12% | 1.2x |
| 15% | 1.5x |
| 18% | 1.8x |

Banks trading below TBV are priced for returns below cost of equity (value destruction). Banks trading above TBV are priced for sustained excess returns.

**ROTCE Adjustment for Cycle**

Normalize ROTCE for credit cycle:
```
Adjusted ROTCE = PPNR Margin - Normalized NCO Rate * (1 - Tax Rate)

Normalized NCO = Long-term average NCO through full credit cycle
```

### Dividend Discount Model (DDM)

Banks are suited to DDM because:
- Regulatory capital requirements cap retained earnings
- Dividend payout ratios are relatively stable and predictable
- Excess capital must be returned (dividends or buybacks)

```
Value = D1 / (r - g)

D1 = Expected dividend next year
r = Cost of equity (typically 9-12% for large banks)
g = Long-term dividend growth (typically 3-5%)
```

For two-stage DDM:
```
Value = Sum of [Dt / (1+r)^t] + Terminal Value / (1+r)^n

Terminal Value = Dn+1 / (r - g_terminal)
```

### Residual Income (Excess Return) Model

```
Value = Book Value + Sum of [Residual Income_t / (1+r)^t]

Residual Income = Net Income - (Equity * Cost of Equity)
                = Equity * (ROTCE - CoE)
```

This approach explicitly values the premium (or discount) to book value based on the ability to earn returns above cost of capital.

## Common Analytical Pitfalls

### Misinterpreting High NIM

**Problem**: Assuming high NIM indicates superior profitability.

**Reality**: High NIM often reflects higher credit risk (subprime lending, unsecured consumer) or asset-liability mismatch (borrowing short, lending long). Always analyze NIM alongside:
- Loan portfolio composition and risk profile
- NCO and NPL trends
- Duration gap and interest rate sensitivity

A bank with 4% NIM and 2% NCOs generates less risk-adjusted return than a bank with 3% NIM and 0.3% NCOs.

### Ignoring Balance Sheet Growth

**Problem**: Focusing only on NIM and efficiency without analyzing earning asset growth.

**Reality**: NII is driven by both margin and volume. A bank with compressing NIM but strong loan growth may still grow NII. Decompose NII changes:
```
Delta NII = Volume Effect + Rate Effect + Mix Effect

Volume Effect = Change in Average Earning Assets * Prior Period NIM
Rate Effect = Prior Period Average Earning Assets * Change in NIM
```

### Confusing Provisions with Actual Losses

**Problem**: Treating provision expense as equivalent to credit losses.

**Reality**: Provisions are forward-looking estimates subject to management discretion. Compare:
- PCL ratio vs. NCO ratio (provisions vs. actuals)
- Reserve build vs. release trends
- Allowance adequacy relative to loan portfolio risk

Banks can smooth earnings through provision timing. Rising NCOs with flat provisions signals under-reserving.

### Overlooking Deposit Franchise Value

**Problem**: Ignoring deposit mix and cost in valuation.

**Reality**: Low-cost, stable deposits (checking, savings) provide structural funding advantage. Compare:
- Non-interest bearing deposits as % of total deposits
- Deposit beta (sensitivity to rate changes)
- Core deposits vs. rate-sensitive/brokered deposits

Banks with high-quality deposit franchises deserve premium valuations for lower funding risk and better NIM stability.

### Misapplying Industrial Valuation Metrics

**Problem**: Using EV/EBITDA, P/S, or unlevered DCF for banks.

**Reality**: These metrics are meaningless for financial institutions. Always use:
- P/TBV with ROTCE context
- P/E relative to normalized earnings
- DDM or residual income for intrinsic value

## Red Flags

- Rapid loan growth (>15% annually) without corresponding infrastructure investment
- NPL ratio increasing while provisions remain flat
- CET1 ratio declining toward regulatory minimums
- Efficiency ratio increasing while revenue grows
- Heavy reliance on wholesale funding (LDR >100%)
- Concentrated loan portfolio (single industry >25%)
- Declining deposit base requiring rate increases to retain
- Mismatched duration (short liabilities, long assets) in rising rate environment
- Goodwill from acquisitions exceeding tangible equity
- Consistent provision releases to meet earnings targets

## Due Diligence Checklist

1. Decompose NII into volume, rate, and mix effects
2. Analyze loan portfolio composition by risk category
3. Compare PCL to NCO trends over multiple quarters
4. Assess deposit franchise quality (mix, cost, beta)
5. Review interest rate sensitivity disclosures (rate shock scenarios)
6. Verify CET1 includes all regulatory adjustments
7. Calculate ROTCE on fully-loaded capital base
8. Stress-test credit losses against allowance adequacy
9. Compare efficiency ratio trends to peer group
10. Analyze fee income sustainability and growth drivers
