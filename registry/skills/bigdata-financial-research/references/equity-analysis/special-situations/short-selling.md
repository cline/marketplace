# Short Selling Analysis Framework

## Overview

Short selling involves borrowing shares to sell, profiting if the stock price declines. Successful short selling requires identifying overvalued securities, constructing a defensible thesis, and managing the asymmetric risk inherent in short positions.

## Table of Contents
1. [Overview](#overview)
2. [Short Thesis Construction](#short-thesis-construction)
3. [Risk Management](#risk-management)
4. [Instruments and Structures](#instruments-and-structures)
5. [Dangerous Short Characteristics](#dangerous-short-characteristics)
6. [Checklist](#checklist)

## Short Thesis Construction

### Valuation-Based Shorts

Identify securities trading significantly above intrinsic value:

| Factor | Indicators |
|--------|-----------|
| Multiple Expansion | Valuation multiples at historical highs without fundamental support |
| Peak Margins | Margins unsustainably elevated vs. competitive dynamics |
| Cyclical Peak | Earnings at cycle peak being capitalized as permanent |
| Growth Extrapolation | Market pricing growth rate continuation beyond reasonable period |
| Comp Misclassification | Stock valued as growth/tech when fundamentals are mature/industrial |

**Catalyst Identification**: Pure valuation shorts require patience. Identify what will cause the market to re-rate:
- Earnings miss / guidance cut
- Competitive response
- Demand saturation
- Margin compression
- Key customer loss
- Management credibility erosion

### Fraud Indicators

More aggressive thesis based on suspected financial manipulation:

**Financial Statement Red Flags**:
- Revenue growing faster than industry without clear explanation
- Revenue growing faster than receivables or cash flow
- Gross margin improvement when competitors show pressure
- Consistent earnings beats while peers struggle
- Cash flow from operations persistently below net income
- Frequent "non-recurring" charges that recur
- Complex revenue recognition (percentage of completion, bill-and-hold)
- Related party transactions at non-market terms
- Unusual seasonality patterns
- Accounts receivable days increasing over time
- Inventory growing faster than sales

**Operational Red Flags**:
- Key documents unavailable (contracts, customer references)
- Suppliers and customers difficult to verify independently
- Vendors with overlapping ownership or management
- Employee profiles inconsistent with claimed operations
- Facility size/location inconsistent with reported revenue
- Third-party verification produces different data than company reports
- Customer testimonials that cannot be verified
- Unusual geographic concentration (harder to verify)

**Organizational Red Flags**:
- High CFO or auditor turnover
- Auditor is small/unknown for company of that size
- Aggressive management compensation tied to revenue targets
- Excessive promotional activity by management
- History of securities violations or regulatory issues
- Complex corporate structure without clear business rationale
- Opaque subsidiary accounting
- Frequent changes to segment reporting
- Material weaknesses in internal controls

## Risk Management

### Position Sizing

Short positions require smaller sizing than longs due to asymmetric risk:

**Maximum Position Guidelines**:
- Single short position: 2-5% of portfolio NAV
- Total short exposure: 20-50% of portfolio NAV (gross)
- Net exposure: Adjust based on market environment

**Sizing Factors**:
```
Position Size = Base Size x Liquidity Factor x Catalyst Proximity x Borrow Stability
```

Where:
- Base Size: 3% for typical conviction level
- Liquidity Factor: Reduce for illiquid names (ability to cover)
- Catalyst Proximity: Increase when catalyst is imminent
- Borrow Stability: Reduce for hard-to-borrow situations

### Borrow Cost Management

| Borrow Status | Typical Cost | Considerations |
|---------------|--------------|----------------|
| General Collateral (GC) | 0.25-0.50% annualized | Stable, low cost |
| Special | 1-5% annualized | Moderate cost, some recall risk |
| Hard to Borrow | 5-50%+ annualized | High cost, significant recall risk |
| Threshold | Varies | Delivery failure risk, regulatory attention |

**Borrow Cost Break-Even**:
If paying 20% annualized borrow cost, stock must decline >20% annually just to break even.

### Recall Risk

Shares can be recalled by the lender at any time:
- Increases during periods of high buying demand
- Prime broker may force buy-in at unfavorable prices
- Lock-up agreements with lenders can mitigate but not eliminate
- Multiple prime broker relationships provide redundancy

### Squeeze Risk

Short squeezes occur when rapid price increase forces short covering, amplifying the move:

**Squeeze Indicators**:
- Short interest > 20% of float
- Days to cover > 5 (short interest / average daily volume)
- Borrow rate spiking
- Positive momentum building
- Retail investor attention increasing
- Options market showing unusual call buying

## Instruments and Structures

### Direct Short Sale

- Borrow shares and sell
- Unlimited theoretical loss (stock can rise infinitely)
- Ongoing borrow costs
- Dividend payments owed to share lender
- Subject to locate and delivery requirements

### Put Options

**Advantages**:
- Defined maximum loss (premium paid)
- No borrow required
- Leverage (less capital outlay)
- No dividend exposure

**Disadvantages**:
- Time decay (theta)
- Implied volatility risk
- Position must be rolled if thesis takes time to play out
- May be expensive if stock is already heavily shorted

### Put Spreads

Long put + short put at lower strike:
- Reduced premium cost vs. outright put
- Capped profit potential
- Lower break-even than outright put
- Time decay reduced (theta partially offset)

**Example Bear Put Spread**:
- Long $50 put (pay $4.00)
- Short $40 put (receive $1.50)
- Net cost: $2.50
- Max profit: $7.50 (if stock below $40)
- Break-even: $47.50

### CDS / Credit Shorts

For companies with traded debt:
- Buy credit default protection
- Profits if spreads widen or default occurs
- No equity borrow required
- Requires ISDA documentation and counterparty

## Dangerous Short Characteristics

| Red Flag | Why Dangerous |
|----------|---------------|
| **Hard-to-borrow status** | High borrow cost erodes returns; recall risk |
| **Short interest > 30% of float** | Squeeze risk; crowded trade |
| **Days to cover > 10** | Extended time to exit if thesis changes |
| **Meme stock characteristics** | Retail coordination; unpredictable price action |
| **Small float / low liquidity** | Difficult to exit; price impact on covering |
| **Strong promotional management** | Can generate positive narratives, delay reckoning |
| **Upcoming binary events** | Takeover, drug approval, legal verdict create gap risk |
| **Recent earnings beat** | Momentum against position |
| **Insider buying** | Signal of undervaluation or coming positive news |
| **Declining borrow availability** | Leading indicator of squeeze potential |
| **Negative rebate** | Paying significant cost to maintain position |

## Checklist

Pre-Short:
- [ ] Documented specific thesis with identified catalyst
- [ ] Analyzed valuation with defensible fair value estimate
- [ ] Reviewed financial statements for fraud indicators (if applicable)
- [ ] Conducted primary research to verify thesis
- [ ] Assessed short interest and squeeze risk metrics
- [ ] Confirmed borrow availability and cost
- [ ] Sized position appropriately for risk
- [ ] Identified exit criteria (both profit target and stop loss)
- [ ] Considered alternative structures (options, spreads)

Ongoing Management:
- [ ] Monitor borrow cost and availability daily
- [ ] Track short interest changes (bi-monthly release)
- [ ] Watch for thesis-changing fundamental developments
- [ ] Review options market for unusual activity
- [ ] Assess social media sentiment for squeeze coordination
- [ ] Maintain stop-loss discipline
- [ ] Re-underwrite position at earnings and major events

Exit Criteria:
- [ ] Catalyst has occurred and thesis played out
- [ ] Thesis invalidated by new information
- [ ] Position sizing breached due to adverse price move
- [ ] Borrow costs exceed acceptable threshold
- [ ] Squeeze risk metrics reach dangerous levels
- [ ] Better risk-reward opportunities identified elsewhere
