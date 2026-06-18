# Financial Statement Red Flags Checklist

This reference provides systematic methods for detecting earnings manipulation, financial distress, and accounting irregularities. Based on established academic research and forensic accounting frameworks.

## Table of Contents
1. [Schilit's Seven Categories of Earnings Manipulation](#schilits-seven-categories-of-earnings-manipulation)
2. [Beneish M-Score](#beneish-m-score)
3. [Cash Flow Manipulation Patterns](#cash-flow-manipulation-patterns)
4. [Balance Sheet Forensics Checklist](#balance-sheet-forensics-checklist)
5. [Altman Z-Score for Distress Prediction](#altman-z-score-for-distress-prediction)
6. [Comprehensive Red Flag Summary](#comprehensive-red-flag-summary)

---

## Schilit's Seven Categories of Earnings Manipulation

Howard Schilit's framework identifies the primary methods companies use to manipulate reported results. Each category includes detection techniques.

### 1. Recording Revenue Too Soon

**Methods:**
- Recognizing revenue before shipment or service delivery
- Recording revenue when significant obligations remain
- Bill-and-hold arrangements without legitimate business purpose
- Channel stuffing near quarter-end
- Recognizing long-term contract revenue prematurely

**Detection Techniques:**
- Compare revenue growth to industry and peer trends
- Analyze DSO trends; unexplained increases signal early recognition
- Review Q4/Q1 revenue patterns for quarter-end loading
- Examine deferred revenue; declining balances may indicate pull-forward
- Check 10-K footnotes for revenue recognition policy changes
- Compare revenue growth to backlog growth; divergence is concerning

**Key Ratios:**
```
Revenue Growth vs Receivables Growth
If Receivables Growth >> Revenue Growth: Investigate
```

### 2. Recording Bogus Revenue

**Methods:**
- Recording revenue from fictitious transactions
- Inflating revenue through round-trip transactions
- Recording rebates, refunds, or financing as revenue
- Misclassifying balance sheet items as revenue
- Related-party transactions at non-arm's-length terms

**Detection Techniques:**
- Identify unusual related-party transactions in footnotes
- Verify revenue from top customers through independent sources
- Analyze gross margin trends; bogus revenue often has 100% margin
- Check for unusual barter or non-cash transactions
- Compare auditor fees to company size; low fees may indicate inadequate scrutiny
- Review geographic revenue mix for unexplained shifts

### 3. Boosting Income with One-Time Gains

**Methods:**
- Selling undervalued assets to generate gains
- Classifying one-time gains as operating income
- Recording investment gains as revenue
- Pension income from assumption changes
- Gain recognition from debt restructuring

**Detection Techniques:**
- Isolate non-operating income line items
- Review asset sales for timing and magnitude
- Analyze pension footnotes for assumption changes (discount rate, return assumptions)
- Calculate core operating income excluding all below-the-line items
- Check for gain/loss asymmetry (recognizing gains, deferring losses)

**Key Analysis:**
```
Core Operating Income = Operating Income - Investment Gains
                        - Asset Sale Gains - Pension Income Adjustments
```

### 4. Shifting Current Expenses to Later Periods

**Methods:**
- Capitalizing operating expenses inappropriately
- Extending depreciation/amortization lives
- Understating reserves and allowances
- Failing to write down impaired assets
- Deferring costs that should be expensed

**Detection Techniques:**
- Compare CapEx as % of revenue to peers; outliers warrant investigation
- Review D&A policies versus industry norms
- Analyze capitalized software, development costs, or customer acquisition costs
- Track asset impairment patterns; lack of impairments during downturns is suspicious
- Check if SG&A as % of revenue declining while revenue grows modestly

**Key Ratios:**
```
Capitalized Costs / Total Assets (trend analysis)
D&A Expense / Gross PP&E (compare to peers)
```

### 5. Failing to Record or Improperly Reducing Liabilities

**Methods:**
- Understating accounts payable and accrued expenses
- Releasing reserves inappropriately to boost income
- Failing to accrue for known liabilities
- Off-balance-sheet obligations
- Underfunded pension and benefit obligations

**Detection Techniques:**
- Track reserve accounts (warranty, litigation, restructuring) over time
- Analyze reserve releases as % of pre-tax income
- Compare days payable outstanding to peers; low DPO may signal understated payables
- Review contingent liability footnotes thoroughly
- Check pension funding status and assumptions
- Identify operating lease obligations and adjust debt metrics

**Off-Balance-Sheet Checklist:**
- Operating leases (pre-ASC 842 for historical analysis)
- Purchase commitments
- Guarantee obligations
- Variable interest entities
- Factored receivables (with recourse)

### 6. Shifting Current Income to Later Periods (Cookie Jar Reserves)

**Methods:**
- Over-accruing expenses in strong periods
- Creating excessive reserves during acquisitions
- Building hidden cushions through conservative accounting
- Deferring revenue recognition when not required

**Detection Techniques:**
- Analyze reserve levels as % of relevant base (e.g., warranty reserve / revenue)
- Track reserve changes relative to business trends
- Review acquisition accounting for excessive goodwill/intangible allocation
- Check for income smoothing patterns (unusually stable earnings)
- Compare deferred revenue policies to peers

**Note:** Cookie jar accounting, while creating future flexibility, is still manipulation.

### 7. Shifting Future Expenses to Current Period (Big Bath)

**Methods:**
- Excessive restructuring charges
- Impairment charges beyond economic reality
- Writing off good assets alongside impaired assets
- Accelerating depreciation unnecessarily
- Kitchen-sink charges during management transitions

**Detection Techniques:**
- Review restructuring charge frequency; recurring charges are not one-time
- Analyze impairment triggers and timing (often coincide with CEO changes)
- Track reversal of charges in subsequent periods
- Compare charge magnitude to actual cash outflows
- Examine earnings trajectory post-big-bath

---

## Beneish M-Score

Messod Beneish developed an eight-variable model to detect earnings manipulation. The model generates a probability score based on financial statement relationships.

### Formula

```
M-Score = -4.84 + 0.920(DSRI) + 0.528(GMI) + 0.404(AQI) + 0.892(SGI)
          + 0.115(DEPI) - 0.172(SGAI) + 4.679(TATA) - 0.327(LVGI)
```

### Variable Definitions and Calculations

| Variable | Formula | Interpretation |
|:---------|:--------|:---------------|
| DSRI (Days Sales Receivable Index) | (Receivables_t / Sales_t) / (Receivables_t-1 / Sales_t-1) | > 1.0 suggests revenue recognition issues |
| GMI (Gross Margin Index) | GM_t-1 / GM_t | > 1.0 indicates declining margins |
| AQI (Asset Quality Index) | [1 - (CA_t + PP&E_t) / TA_t] / [1 - (CA_t-1 + PP&E_t-1) / TA_t-1] | > 1.0 suggests increased capitalization |
| SGI (Sales Growth Index) | Sales_t / Sales_t-1 | High growth correlates with manipulation |
| DEPI (Depreciation Index) | Depr Rate_t-1 / Depr Rate_t | > 1.0 indicates slowing depreciation |
| SGAI (SG&A Index) | (SG&A_t / Sales_t) / (SG&A_t-1 / Sales_t-1) | Not directionally clear |
| TATA (Total Accruals to Total Assets) | (Working Capital Change - Cash Change - D&A) / TA | High accruals indicate manipulation |
| LVGI (Leverage Index) | [(LTD_t + CL_t) / TA_t] / [(LTD_t-1 + CL_t-1) / TA_t-1] | Increasing leverage |

### Interpretation Thresholds

| M-Score | Interpretation |
|:--------|:---------------|
| < -2.22 | Low probability of manipulation |
| -2.22 to -1.78 | Gray zone; warrants additional scrutiny |
| > -1.78 | High probability of manipulation |

### Application Notes

- Calculate annually using year-end figures
- Requires two consecutive years of data
- Most effective for industrial companies; adjust interpretation for financials and tech
- Use as screening tool, not definitive verdict
- Combine with qualitative assessment

---

## Cash Flow Manipulation Patterns

Cash flow from operations is harder to manipulate than net income but not immune.

### Common OCF Manipulation Techniques

| Technique | Detection Method |
|:----------|:-----------------|
| Factoring receivables | Check financing footnotes; adds to OCF short-term |
| Stretching payables | Analyze DPO trends; unsustainably high DPO will reverse |
| Capitalizing operating costs | Compare CapEx/Revenue to peers |
| Reclassifying investing/financing items | Review cash flow statement classifications |
| Timing of collections/payments | Analyze quarterly OCF patterns |

### Free Cash Flow Validation

```
Sustainable FCF = OCF - Maintenance CapEx - SBC

Cross-check: EBITDA - Interest - Taxes - Maintenance CapEx - Working Capital Investment
```

Significant divergence between calculation methods warrants investigation.

---

## Balance Sheet Forensics Checklist

### Asset Quality Assessment

| Item | Red Flag Indicators |
|:-----|:--------------------|
| Receivables | Growing faster than revenue; aging deterioration |
| Inventory | Growing faster than COGS; LIFO reserve changes |
| Prepaid Expenses | Unusual increases without business justification |
| Goodwill | No impairments despite declining business |
| Intangibles | Extended useful lives; large capitalized software balances |
| Other Assets | Vague descriptions; material balances |

### Hidden Liabilities Checklist

- [ ] Operating lease obligations (capitalize at appropriate discount rate)
- [ ] Purchase commitments and take-or-pay contracts
- [ ] Pension and OPEB underfunding
- [ ] Legal contingencies (especially those disclosed but not accrued)
- [ ] Environmental liabilities
- [ ] Product warranty obligations
- [ ] Deferred tax valuation allowance adequacy
- [ ] Off-balance-sheet variable interest entities
- [ ] Guarantee obligations
- [ ] Unconditional purchase obligations

---

## Altman Z-Score for Distress Prediction

Edward Altman's Z-Score predicts bankruptcy probability for manufacturing firms.

### Formula (Original Manufacturing)

```
Z-Score = 1.2(X1) + 1.4(X2) + 3.3(X3) + 0.6(X4) + 1.0(X5)
```

| Variable | Calculation |
|:---------|:------------|
| X1 | Working Capital / Total Assets |
| X2 | Retained Earnings / Total Assets |
| X3 | EBIT / Total Assets |
| X4 | Market Value Equity / Total Liabilities |
| X5 | Sales / Total Assets |

### Formula (Private Companies)

```
Z'-Score = 0.717(X1) + 0.847(X2) + 3.107(X3) + 0.420(X4') + 0.998(X5)

Where X4' = Book Value Equity / Total Liabilities
```

### Formula (Non-Manufacturing/Service)

```
Z''-Score = 6.56(X1) + 3.26(X2) + 6.72(X3) + 1.05(X4)

Note: Excludes X5 (asset turnover) which varies significantly by industry
```

### Interpretation Thresholds

| Z-Score (Original) | Z'-Score (Private) | Z''-Score (Service) | Zone |
|:-------------------|:-------------------|:--------------------|:-----|
| > 2.99 | > 2.90 | > 2.60 | Safe Zone |
| 1.81 - 2.99 | 1.23 - 2.90 | 1.10 - 2.60 | Gray Zone |
| < 1.81 | < 1.23 | < 1.10 | Distress Zone |

### Application Notes

- Most predictive 1-2 years before distress
- Track trend over time; declining Z-Score is warning sign
- Combine with liquidity analysis and debt covenant review
- Less reliable for financial services companies

---

## Comprehensive Red Flag Summary

### Immediate Investigation Required

- [ ] Auditor resignation or change with disagreements
- [ ] CFO or Controller departure
- [ ] Restatements or material weaknesses
- [ ] SEC comment letters with aggressive follow-up
- [ ] Significant related-party transactions
- [ ] Revenue growing materially faster than OCF
- [ ] M-Score > -1.78
- [ ] Z-Score in distress zone with negative trend

### Elevated Scrutiny Warranted

- [ ] DSO increasing faster than revenue growth
- [ ] Accrual ratio > 5% of assets
- [ ] Recurring non-GAAP adjustments exceeding 20% of GAAP earnings
- [ ] SBC intensity > 10% of revenue
- [ ] Capitalized costs growing faster than revenue
- [ ] Reserve releases contributing to earnings beat
- [ ] Aggressive pension assumptions versus peers
- [ ] Cash conversion cycle deteriorating

### Document and Monitor

- [ ] Auditor fees below peer median
- [ ] Minimal board independence or audit committee expertise
- [ ] Complex corporate structure with numerous subsidiaries
- [ ] Geographic concentration in high-risk jurisdictions
- [ ] Customer concentration > 25% single customer
- [ ] Aggressive revenue recognition policy versus peers
