# Reverse DCF: Expectations Investing Framework

## Overview

Reverse DCF inverts the traditional valuation process. Rather than projecting fundamentals to derive value, it extracts the growth and margin assumptions embedded in the current stock price. This approach, popularized by Michael Mauboussin and Alfred Rappaport, transforms valuation from a prediction exercise into an expectations assessment.

**Core Question**: What does the market believe about this company's future, and do I agree?

## Table of Contents
1. [Mauboussin's Framework](#mauboussins-framework)
2. [Reverse DCF Process](#reverse-dcf-process)
3. [Comparing Implied to Your Forecast](#comparing-implied-to-your-forecast)
4. [Identifying Variant Perception](#identifying-variant-perception)
5. [Key Insight: What's Priced In](#key-insight-whats-priced-in)
6. [Practical Application](#practical-application)
7. [Limitations](#limitations)
8. [Output Format](#output-format)

---

## Mauboussin's Framework

The expectations investing framework rests on three principles:

1. **Stock prices embed forecasts**: Current prices reflect the market's consensus expectations for future cash flows
2. **Expectations are identifiable**: Using reverse DCF, you can extract implied growth rates, margins, and duration of competitive advantage
3. **Variant perception creates alpha**: Outperformance comes from identifying where your expectations differ from the market's implied assumptions

### The Three-Step Process

| Step | Action | Output |
|------|--------|--------|
| 1. Extract | Solve for implied assumptions from current price | Implied growth, margins, ROIC, CAP |
| 2. Analyze | Compare implied assumptions to your own forecast | Gaps between market and your view |
| 3. Decide | Assess probability market is wrong | Buy/sell/hold based on variant perception |

---

## Reverse DCF Process

### Step 1: Establish Baseline Inputs

Fix the variables you consider "known" or have high confidence in:

| Fixed Input | Source | Typical Approach |
|-------------|--------|------------------|
| WACC | CAPM, peer analysis | Use your calculated WACC |
| Terminal growth | Long-term GDP/inflation | Fix at 2-3% |
| Current financials | Last reported period | Revenue, EBITDA, margins |
| Capital intensity | Historical average | CapEx/Revenue, NWC/Revenue |
| Tax rate | Statutory/effective | Marginal rate |

### Step 2: Solve for Implied Variable

With price as the "answer," solve for the unknown. Common approaches:

#### A. Implied Revenue Growth

Hold margins constant at current or target levels. Solve for the revenue CAGR that produces the current market cap.

```
Given: Current EV, WACC, terminal growth, margin trajectory
Solve for: Revenue growth rate over forecast period
```

#### B. Implied Margin Expansion

Hold revenue growth at consensus or industry rate. Solve for the terminal operating margin.

```
Given: Current EV, WACC, terminal growth, revenue forecast
Solve for: Terminal EBIT or EBITDA margin
```

#### C. Implied Competitive Advantage Period (CAP)

Solve for how long the market expects above-average returns to persist.

```
Given: Current EV, near-term forecasts, fade to terminal
Solve for: Number of years before ROIC = WACC
```

### Step 3: Calculation Mechanics

**Method 1: Goal Seek / Solver**
- Build standard DCF model
- Set target cell = Current Market Cap
- Vary assumption cell (growth rate, margin, etc.)
- Solve

**Method 2: Analytical Approximation**

For quick estimation, use the perpetuity shortcut:

```
EV = NOPAT * (1 + g) * (1 - g/ROIC) / (WACC - g)
```

Rearranging to solve for implied growth:

```
g_implied = (EV * WACC - NOPAT) / (EV - NOPAT/ROIC)
```

---

## Comparing Implied to Your Forecast

Once you extract implied assumptions, create a side-by-side comparison:

| Metric | Market Implied | Your Forecast | Variant? |
|--------|----------------|---------------|----------|
| Revenue CAGR (5Y) | 15% | 12% | Yes - Bearish |
| Terminal EBIT Margin | 28% | 32% | Yes - Bullish |
| Years of CAP | 12 | 8 | Yes - Bearish |
| Terminal ROIC | 22% | 18% | Yes - Bearish |
| WACC | (assumed) 9% | 9% | No |

### Interpretation Framework

| Your View vs Implied | Implication |
|---------------------|-------------|
| Your forecast > Implied | Stock potentially undervalued |
| Your forecast < Implied | Stock potentially overvalued |
| Your forecast = Implied | Fair value, no edge |

---

## Identifying Variant Perception

A variant perception exists when:

1. **Magnitude matters**: Small differences in growth (1-2%) may not be actionable. Look for meaningful gaps (>20% difference in key driver).

2. **You have evidence**: Variant perception must be grounded in differentiated research, not just optimism or pessimism.

3. **The market will learn**: There must be a catalyst or time horizon for expectations to converge to your view.

### Variant Perception Checklist

| Question | Required Answer for Conviction |
|----------|-------------------------------|
| What specific assumption am I disagreeing with? | Clear, quantifiable metric |
| Why does the market hold this view? | Understand the consensus logic |
| What evidence supports my differing view? | Primary research, data, analysis |
| What would prove me wrong? | Falsifiable thesis |
| When will the market recognize this? | Identifiable catalyst |
| What is my margin of safety? | Downside protection if wrong |

---

## Key Insight: What's Priced In

The power of reverse DCF lies in reframing the investment question:

**Traditional DCF asks**: "What is this company worth?"

**Reverse DCF asks**: "What must happen for this stock to be fairly valued today?"

This shift provides critical perspective:

| Scenario | Traditional Response | Reverse DCF Response |
|----------|---------------------|---------------------|
| Stock up 50% | "Still undervalued by my DCF" | "Now implies 20% growth; is that achievable?" |
| Beaten-down stock | "Cheap on P/E" | "Implies permanent margin decline; is that right?" |
| High-flyer | "Too expensive" | "Implies 30% growth for 10 years; what would break that?" |

---

## Practical Application

### Example: High-Growth SaaS Company

Current price implies:
- 35% revenue CAGR for 5 years
- Terminal EBIT margin of 30%
- 10+ years of competitive advantage

Your analysis:
- Competitive intensity increasing, growth likely 25% CAGR
- Margin achievable but not until year 7+
- Moat narrower than assumed

**Conclusion**: Market expectations exceed reasonable forecast. Stock is overvalued on a risk-adjusted basis despite strong fundamentals.

### Example: Turnaround Industrial

Current price implies:
- Revenue decline of 3% annually
- No margin recovery from trough
- Terminal value at 4x EBITDA (distressed)

Your analysis:
- New management executing cost cuts
- Industry stabilizing, flat revenue likely
- Margins can recover 300bps

**Conclusion**: Market embeds permanent impairment. If your turnaround thesis is correct, significant upside exists.

---

## Limitations

| Limitation | Mitigation |
|------------|------------|
| WACC assumption drives results | Sensitivity test WACC +/- 100bps |
| Multiple implied solutions possible | Anchor one variable with high confidence |
| Ignores optionality | Layer in real options value separately |
| Point-in-time analysis | Repeat quarterly as price and data change |

---

## Output Format

Present reverse DCF analysis as:

1. **Implied assumptions table**: Key metrics the market expects
2. **Your forecast comparison**: Side-by-side with implied
3. **Variant perception statement**: Specific disagreement and evidence
4. **Sensitivity**: How implied growth/margin changes with price
5. **Investment conclusion**: Action based on gap between implied and expected
