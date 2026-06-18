# Distressed Debt and Equity Analysis Framework

## Overview

Distressed investing involves purchasing securities of companies experiencing financial stress, bankruptcy, or restructuring. Success requires understanding the claims waterfall, identifying the fulcrum security, and assessing recovery values under various scenarios.

## Table of Contents
1. [Overview](#overview)
2. [Claims Waterfall Analysis](#claims-waterfall-analysis)
3. [Fulcrum Security Identification](#fulcrum-security-identification)
4. [Recovery Analysis Methodology](#recovery-analysis-methodology)
5. [Investment Strategies](#investment-strategies)
6. [Valuation Considerations](#valuation-considerations)
7. [Red Flags](#red-flags)
8. [Process Timeline](#process-timeline)
9. [Checklist](#checklist)

## Claims Waterfall Analysis

### Priority of Claims (Highest to Lowest)

| Priority | Claim Type | Characteristics |
|----------|-----------|-----------------|
| 1 | **DIP Financing** | Debtor-in-possession loans; super-priority; typically fully recovered |
| 2 | **Administrative Claims** | Professional fees, post-petition obligations; paid in full |
| 3 | **Priority Tax Claims** | Certain tax obligations; paid in full or over time |
| 4 | **Secured Debt (1st Lien)** | Collateralized claims; recovery depends on collateral value |
| 5 | **Secured Debt (2nd Lien)** | Junior secured claims; recover after 1st lien satisfied |
| 6 | **Senior Unsecured Debt** | Bonds, term loans without collateral |
| 7 | **Subordinated Debt** | Junior bonds, mezzanine debt |
| 8 | **Trade Claims** | Vendor obligations, accounts payable |
| 9 | **Preferred Equity** | Liquidation preference, but junior to all debt |
| 10 | **Common Equity** | Residual claim; typically wiped out in restructuring |

### Key Waterfall Concepts

**Absolute Priority Rule**: Senior claims must be paid in full before junior claims receive any recovery. Deviations ("gifting") sometimes occur to gain creditor support but are increasingly challenged.

**Intercompany Claims**: Complex corporate structures create intercompany claims that can shift value between subsidiaries. Map legal entity structure carefully.

**Guarantee Analysis**: Parent or subsidiary guarantees can elevate or subordinate claims across entities.

## Fulcrum Security Identification

The fulcrum security is the claim where enterprise value "breaks" - the class that receives partial recovery and drives the restructuring negotiation.

### Fulcrum Identification Process

1. **Estimate Enterprise Value**: Use conservative DCF, comparable transactions, or liquidation analysis
2. **Map Claims Outstanding**: Aggregate all debt claims by priority level
3. **Apply Waterfall**: Distribute enterprise value starting from senior claims
4. **Identify Break Point**: The claim class receiving partial recovery is the fulcrum

**Example**:
```
Enterprise Value Estimate: $500M

Claims:
- 1st Lien Secured: $300M --> Recovery: 100% ($300M)
- 2nd Lien Secured: $150M --> Recovery: 100% ($150M)
- Senior Unsecured: $200M --> Recovery: 25% ($50M) <-- FULCRUM
- Subordinated: $100M --> Recovery: 0%
- Equity: -- --> Recovery: 0%
```

### Why Fulcrum Matters

- Fulcrum holders control the restructuring negotiation
- They receive equity in the reorganized company
- Best risk-adjusted returns often come from buying fulcrum securities at distressed prices
- Fulcrum can shift as enterprise value estimates change

## Recovery Analysis Methodology

### Enterprise Value Approaches

**Going Concern DCF**:
- Use conservative revenue assumptions (no turnaround premium)
- Apply appropriate distressed company discount rate (15-25%)
- Model realistic emergence capital structure
- Sensitivity test key assumptions extensively

**Comparable Transactions**:
- Analyze recent distressed M&A in the sector
- Apply EV/EBITDA multiples from similar situations
- Adjust for company-specific factors

**Liquidation Analysis**:
- Value assets at orderly liquidation prices (60-80% of book for hard assets)
- Apply fire-sale discounts for forced liquidation scenarios
- Establishes absolute floor for recovery values

### Recovery Sensitivity

Build recovery matrix across enterprise value and claims scenarios:

| EV Scenario | 1st Lien | 2nd Lien | Unsecured | Equity |
|-------------|----------|----------|-----------|--------|
| $400M | 100% | 67% | 0% | 0% |
| $500M | 100% | 100% | 25% | 0% |
| $600M | 100% | 100% | 75% | 0% |
| $700M | 100% | 100% | 100% | Residual |

## Investment Strategies

### Active / Control Investing

- Acquire controlling position in fulcrum security
- Drive restructuring process and outcomes
- Requires significant capital and restructuring expertise
- Often converts debt to majority equity ownership post-emergence

### Passive Investing

- Take positions without seeking control
- Rely on other sophisticated creditors to drive process
- Lower resource requirements, lower potential returns
- Exit through secondary market or emergence equity

### DIP Financing

- Provide new money to fund company through bankruptcy
- Super-priority position with significant protections
- Requires specialized underwriting and monitoring capabilities
- Lower risk, lower return than fulcrum investing

### Post-Reorg Equity

- Purchase equity of companies emerging from bankruptcy
- Clean balance sheet, operational improvements already implemented
- Requires patience as equity often overhang-constrained initially

## Valuation Considerations

### Conservative Bias

- Use bear case revenue assumptions
- Apply trough margins, not normalized
- Assume no synergies or operational improvements initially
- Discount for execution risk on turnaround plans

### Key Adjustments

| Factor | Consideration |
|--------|--------------|
| Pension liabilities | Often understated; use realistic discount rates |
| Environmental claims | Can be priority or administrative; investigate carefully |
| Lease obligations | FASB changes affect comparability; adjust for operating leases |
| Working capital | Distressed companies often have bloated receivables, inventory |
| Deferred revenue | Liability that must be serviced or refunded |
| Contingent liabilities | Litigation, product liability, contract disputes |

### Liquidation Floor

Always calculate liquidation value as downside protection:

```
Liquidation Value =
  Cash + (Receivables x 70-85%) + (Inventory x 50-70%) +
  (PP&E x 40-60%) + (Real Estate x 70-90%) -
  Administrative Costs - Wind-Down Costs
```

## Red Flags

| Red Flag | Concern |
|----------|---------|
| **Liability Management Exercises (LMEs)** | Pre-bankruptcy transactions shifting collateral or priority; fulcrum may move unexpectedly |
| **Loose covenant documentation** | Allows value-destructive transactions before creditors can act |
| **Complex multi-entity structures** | Intercompany claims and guarantees create uncertainty |
| **High administrative costs** | Professional fees consume recovery value in protracted cases |
| **Management retention plans** | May create incentives misaligned with creditor recoveries |
| **Litigation overhang** | Unquantified claims create wide recovery ranges |
| **Key man risk** | Turnaround depends on specific individuals who may leave |
| **Regulatory/licensing risk** | Bankruptcy may trigger license revocations (healthcare, gaming, telecom) |
| **Customer concentration** | Major customers may accelerate departure during distress |
| **Vendor terms tightening** | COD requirements increase working capital needs |

## Process Timeline

| Phase | Typical Duration | Key Activities |
|-------|------------------|----------------|
| Pre-Filing | 1-6 months | RSA negotiation, DIP arrangement, first-day motions prep |
| First Day | Day 1 | Critical vendor motions, DIP approval, employee payments |
| Exclusivity | 120+ days | Plan development, creditor negotiation |
| Disclosure Statement | 30-60 days | Plan disclosure approval, voting |
| Confirmation | 30-60 days | Court approval, objection resolution |
| Emergence | Immediate | Plan effective, new equity issued |

Total Chapter 11 duration typically 6-18 months for complex cases.

## Checklist

Pre-Investment:
- [ ] Mapped complete capital structure including all tranches and guarantees
- [ ] Estimated enterprise value using multiple methodologies
- [ ] Identified fulcrum security and sensitized to EV ranges
- [ ] Calculated liquidation floor value
- [ ] Reviewed loan documentation for covenant and collateral details
- [ ] Assessed LME risk and recent liability management activity
- [ ] Analyzed management incentives and retention arrangements
- [ ] Evaluated restructuring timeline and key milestones

Process Monitoring:
- [ ] Track court docket and key filings
- [ ] Monitor DIP budget and liquidity position
- [ ] Follow ad hoc creditor group formations
- [ ] Assess plan proposals and recovery implications
- [ ] Watch for claim trading activity as price discovery
- [ ] Review disclosure statement for updated valuation
