# Merger Arbitrage Analysis Framework

## Overview

Merger arbitrage involves purchasing shares of an announced acquisition target at a discount to the deal price, profiting when the transaction closes. The spread between current price and deal price compensates for deal risk and time value.

## Table of Contents
1. [Overview](#overview)
2. [Spread Analysis Framework](#spread-analysis-framework)
3. [Deal Risk Assessment](#deal-risk-assessment)
4. [Deal Types and Hedging](#deal-types-and-hedging)
5. [Position Sizing](#position-sizing)
6. [Completion Probability Assessment](#completion-probability-assessment)
7. [Red Flags](#red-flags)
8. [Checklist](#checklist)

## Spread Analysis Framework

### Basic Spread Calculation

**Gross Spread** = (Deal Price - Current Price) / Current Price

**Annualized Spread** = Gross Spread x (365 / Days to Close)

Example:
- Deal Price: $50.00
- Current Price: $48.50
- Expected Days to Close: 120

Gross Spread = ($50.00 - $48.50) / $48.50 = 3.09%
Annualized Spread = 3.09% x (365 / 120) = 9.4%

### Expected Value Framework

Simple expected value calculation:

**Expected Return** = (Probability of Close x Upside) - (Probability of Break x Downside)

Where:
- Upside = Deal Price - Current Price
- Downside = Current Price - Unaffected Price (price before deal announcement)

Example:
- Current Price: $48.50
- Deal Price: $50.00
- Unaffected Price: $35.00
- Probability of Close: 90%

Expected Return = (90% x $1.50) - (10% x $13.50) = $1.35 - $1.35 = $0.00

This illustrates why spreads exist: they compensate for asymmetric downside risk.

## Deal Risk Assessment

### Regulatory Risk

| Jurisdiction | Typical Timeline | Key Considerations |
|--------------|------------------|---------------------|
| US (HSR/DOJ/FTC) | 30 days - 18 months | Market concentration, vertical effects |
| EU (EC) | 25-125 working days | Remedies often required, Phase II risk |
| China (SAMR) | 30-180 days | Geopolitical overlay, unpredictable |
| UK (CMA) | 40-120 working days | Phase II increasingly common |

**Regulatory Risk Factors**:
- Combined market share above 30% in any relevant market
- Elimination of close competitor (horizontal overlap)
- Vertical integration concerns (foreclosure risk)
- Parallel DOJ/FTC investigations
- Multi-jurisdictional review with conflicting interests

### Financing Risk

**Financing Condition Assessment**:
- Is financing committed or subject to conditions?
- What is acquirer's credit profile and capacity for bridge financing?
- Has debt financing closed since announcement?
- Are there material adverse change (MAC) provisions in financing commitments?

Cash deals without financing conditions carry minimal financing risk. Deals with financing contingencies require credit spread and acquirer financial health monitoring.

### Shareholder Approval Risk

- What percentage is required for approval? (50%, 66.7%, 80%?)
- What is current shareholder composition (arbs vs. fundamental holders)?
- Have major shareholders indicated support?
- Are there activist shareholders opposing the deal?
- Does target have defensive provisions (staggered board, poison pill)?

### MAC Clause Analysis

Material Adverse Change clauses allow buyers to terminate if target's business deteriorates significantly. Key questions:

- Does MAC include carve-outs for general economic conditions?
- Are pandemic-related carve-outs present?
- Is there a materiality threshold specified?
- What is acquirer's historical behavior regarding MAC invocations?

## Deal Types and Hedging

### Cash Deals

Straightforward: buy target, collect deal price at close.

Position = Long target shares

### Stock Deals (Fixed Ratio)

Acquirer offers fixed number of its shares per target share.

Position = Long target shares + Short acquirer shares (hedge ratio = exchange ratio)

Example: 0.5x exchange ratio means short 0.5 acquirer shares per 1 target share held.

This hedges acquirer stock price movements and isolates pure deal spread.

### Stock Deals (Fixed Value)

Deal value is fixed; exchange ratio floats with acquirer stock price.

More complex hedging required; ratio resets create basis risk.

### Collar Deals

Exchange ratio floats within a band, then fixes outside band.

Requires dynamic hedging as acquirer price moves relative to collar thresholds.

## Position Sizing

Position sizing should reflect risk-reward asymmetry:

**Conservative Formula**:
```
Position Size = (Expected Value / Downside Risk) x Base Position Size
```

**Risk Parameters**:
- Maximum single-deal exposure: 5-10% of portfolio
- Maximum sector concentration: 20-25% of portfolio
- Maximum regulatory jurisdiction exposure: 30-40% of portfolio

**Correlation Consideration**: Multiple deals facing same regulatory review (e.g., DOJ antitrust) have correlated break risk. Reduce aggregate exposure to correlated deals.

## Completion Probability Assessment

| Factor | Higher Probability | Lower Probability |
|--------|-------------------|-------------------|
| Strategic rationale | Strong synergies, transformational | Unclear or solely financial |
| Acquirer commitment | CEO reputation at stake, public statements | Conditional language, financing outs |
| Regulatory complexity | No overlap, different markets | Significant horizontal overlap |
| Financing | Cash on hand, investment grade debt | Leveraged, uncommitted financing |
| Shareholder support | Majority locked up, premium to peers | Opposition from large holders |
| MAC risk | Stable business, carve-outs present | Cyclical business, broad MAC language |

## Red Flags

| Red Flag | Concern |
|----------|---------|
| **Spread wider than historical norms without explanation** | Market pricing in risk you may not see |
| **Acquirer stock declining post-announcement** | Market questions deal value; potential renegotiation |
| **Acquirer history of broken deals** | Pattern of walking away when convenient |
| **Unusual financing structure** | Complex structures suggest marginal economics |
| **Target insiders selling** | May know approval or business issues not public |
| **Proxy advisors recommend against** | Increases shareholder approval risk |
| **Competing bidder rumors without topping bid** | May be distraction rather than genuine interest |
| **Extended regulatory timeline without updates** | Often indicates second request or Phase II |

## Checklist

Deal Initiation:
- [ ] Calculated gross and annualized spread
- [ ] Assessed regulatory pathway and timeline
- [ ] Reviewed financing commitment letters
- [ ] Analyzed shareholder base and approval threshold
- [ ] Read merger agreement for MAC clause details
- [ ] Modeled expected value with explicit probability assumptions
- [ ] Sized position based on risk-reward asymmetry

Ongoing Monitoring:
- [ ] Track regulatory filings and timeline updates
- [ ] Monitor spread movements for information content
- [ ] Watch acquirer credit spreads if financing contingent
- [ ] Follow proxy advisory firm recommendations
- [ ] Review any amended filings or deal term changes
