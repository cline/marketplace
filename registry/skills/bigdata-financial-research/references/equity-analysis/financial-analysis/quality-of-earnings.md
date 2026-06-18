# Quality of Earnings Analysis

A rigorous assessment of earnings quality distinguishes sustainable, cash-backed profits from accounting artifacts. This framework enables systematic evaluation of reported earnings reliability.

## Table of Contents
1. [Operating Cash Flow to Net Income Ratio](#operating-cash-flow-to-net-income-ratio)
2. [Accrual Quality Analysis](#accrual-quality-analysis)
3. [Working Capital Analysis](#working-capital-analysis)
4. [GAAP vs Non-GAAP Reconciliation](#gaap-vs-non-gaap-reconciliation)
5. [Stock-Based Compensation Treatment](#stock-based-compensation-treatment)
6. [Quality of Earnings Checklist](#quality-of-earnings-checklist)
7. [Application Process](#application-process)

---

## Operating Cash Flow to Net Income Ratio

The OCF/Net Income ratio is the primary screening metric for earnings quality. Persistent divergence between cash generation and reported profits signals potential quality issues.

### Interpretation Thresholds

| OCF/NI Ratio | Assessment | Implication |
|:-------------|:-----------|:------------|
| > 1.2 | Strong | Cash generation exceeds reported income; conservative accounting |
| 0.8 - 1.2 | Healthy | Normal operating accruals; sustainable earnings |
| 0.6 - 0.8 | Caution | Elevated accruals; investigate drivers |
| < 0.6 | Warning | Earnings materially exceed cash; high manipulation risk |
| Negative NI, Positive OCF | Investigate | Non-cash charges may obscure healthy operations |
| Positive NI, Negative OCF | Red Flag | Reported profits not converting to cash |

### Calculation

```
OCF/NI Ratio = Operating Cash Flow / Net Income
```

Adjust for one-time items in both numerator and denominator. Use trailing twelve months for cyclical businesses.

### Trend Analysis

Single-period ratios are insufficient. Track OCF/NI over 5+ years:
- Stable ratio near 1.0: High quality, predictable earnings
- Declining trend: Deteriorating quality; investigate accrual growth
- High volatility: Earnings timing issues or accounting flexibility

---

## Accrual Quality Analysis

### The Sloan Accrual Anomaly

Richard Sloan (1996) demonstrated that the accrual component of earnings is less persistent than the cash component. High-accrual firms systematically underperform.

**Total Accruals Formula:**

```
Total Accruals = Net Income - Operating Cash Flow
```

**Balance Sheet Approach (Richardson et al.):**

```
Total Accruals = (Change in Non-Cash Current Assets - Change in Current Liabilities ex. STD)
                 - Depreciation and Amortization
```

### Accrual Ratio

```
Accrual Ratio = Total Accruals / Average Total Assets
```

| Accrual Ratio | Interpretation |
|:--------------|:---------------|
| < -5% | Very conservative; possible under-earning |
| -5% to +5% | Normal accrual levels |
| +5% to +10% | Elevated; warrants investigation |
| > +10% | High manipulation risk; likely mean reversion |

### Cash vs Accrual Decomposition

Decompose earnings into components for persistence analysis:

```
Earnings = Cash Component + Accrual Component

Cash Component = Operating Cash Flow / Average Assets
Accrual Component = Total Accruals / Average Assets
```

The cash component exhibits 0.8+ persistence (autocorrelation), while accrual component shows only 0.4-0.5 persistence. Weight cash component more heavily in forecasting.

---

## Working Capital Analysis

Working capital changes drive short-term accruals. Analyze efficiency metrics to assess whether accrual changes reflect operational improvements or accounting manipulation.

### Days Sales Outstanding (DSO)

```
DSO = (Accounts Receivable / Revenue) x 365
```

- Rising DSO with flat revenue growth: Potential revenue recognition issues
- DSO significantly above industry peers: Credit quality or collection concerns
- Sudden DSO improvement: Possible factoring or channel stuffing reversal

### Days Inventory Outstanding (DIO)

```
DIO = (Inventory / Cost of Goods Sold) x 365
```

- Rising DIO: Obsolescence risk, demand weakness, or cost capitalization
- Falling DIO with rising gross margin: Investigate cost flow assumptions
- Compare raw materials vs finished goods trends separately

### Days Payable Outstanding (DPO)

```
DPO = (Accounts Payable / Cost of Goods Sold) x 365
```

- Rising DPO: May indicate cash preservation or supplier stress
- Extended payables can inflate near-term OCF at expense of relationships
- Compare to supplier payment terms for context

### Cash Conversion Cycle (CCC)

```
CCC = DSO + DIO - DPO
```

The CCC measures days between cash outflow for inventory and cash inflow from sales.

| CCC Trend | Implication |
|:----------|:------------|
| Declining | Improved working capital efficiency; positive for FCF |
| Rising | Cash tied up in operations; investigate component drivers |
| Negative | Favorable payment terms; common in retail (receives cash before paying suppliers) |

**Quality Signal:** Improving earnings with deteriorating CCC is a warning sign. Earnings should translate to cash.

---

## GAAP vs Non-GAAP Reconciliation

Non-GAAP metrics can provide operational insight or obscure economic reality. Systematic reconciliation analysis is essential.

### Reconciliation Framework

1. **Obtain Full Reconciliation:** Require complete bridge from GAAP to non-GAAP
2. **Categorize Adjustments:**
   - Legitimate: D&A of acquired intangibles, one-time restructuring, M&A costs
   - Questionable: Recurring restructuring, regular asset impairments
   - Aggressive: SBC, amortization of capitalized software, recurring legal costs
3. **Calculate Adjustment Magnitude:**
   ```
   Adjustment Gap = (Non-GAAP EPS - GAAP EPS) / |GAAP EPS|
   ```
4. **Track Adjustment Trend:** Growing gaps indicate aggressive posturing

### Red Flags in Non-GAAP Metrics

- Excluding SBC in capital-intensive hiring periods
- Recurring items labeled as non-recurring for 3+ consecutive years
- Non-GAAP revenue adjustments (extremely rare legitimate cases)
- Adjustment categories changing year-over-year
- Non-GAAP margins consistently at guidance while GAAP deteriorates

---

## Stock-Based Compensation Treatment

SBC represents real economic cost that must be incorporated into quality assessment.

### SBC as Percentage of Revenue

```
SBC Intensity = Stock-Based Compensation / Revenue
```

| SBC/Revenue | Assessment |
|:------------|:-----------|
| < 3% | Modest; normal for mature companies |
| 3% - 8% | Moderate; acceptable for growth companies |
| 8% - 15% | Elevated; meaningful dilution drag |
| > 15% | Excessive; unsustainable compensation model |

### FCF Adjustment

Many companies report FCF excluding SBC. Calculate true economic FCF:

```
Adjusted FCF = Reported FCF - SBC + Tax Benefit of SBC
```

Or equivalently, use GAAP Operating Income as starting point.

### Dilution Analysis

```
Annual Dilution Rate = (Options/RSUs Granted - Buybacks) / Shares Outstanding
```

Compare dilution rate to SBC expense. High SBC with low dilution suggests underwater options being replaced with new grants at lower strikes.

---

## Quality of Earnings Checklist

| Factor | Strong Quality | Weak Quality |
|:-------|:---------------|:-------------|
| OCF/NI Ratio | > 0.8 consistently | < 0.6 or volatile |
| Accrual Trend | Stable or declining | Rising as % of assets |
| Cash Conversion Cycle | Stable or improving | Deteriorating |
| DSO Trend | Stable vs revenue | Rising faster than revenue |
| GAAP/Non-GAAP Gap | Small, stable | Large, growing |
| SBC Intensity | Below peer median | Above peer median |
| Audit Opinion | Clean | Qualified, going concern |
| Revenue Recognition | Point-in-time, clear | % completion, estimates |
| Customer Concentration | Diversified | Top 3 > 50% |

---

## Application Process

1. Calculate OCF/NI for trailing 5 years; flag if below 0.8 in any period
2. Compute accrual ratios; investigate if > 5%
3. Analyze working capital efficiency trends (DSO, DIO, DPO, CCC)
4. Build full GAAP to non-GAAP reconciliation; assess adjustment quality
5. Calculate true FCF including SBC; compare to management's FCF
6. Document findings in quality assessment memo before proceeding to valuation
