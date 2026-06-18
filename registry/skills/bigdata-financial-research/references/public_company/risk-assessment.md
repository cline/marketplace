# Risk Assessment Workflow

Comprehensive risk analysis covering regulatory/legal exposure, competitive threats, operational vulnerabilities, financial risks, and macro headwinds with likelihood and impact ratings.

## When to Use

- User asks: "Assess risks for [company]"
- User asks: "Risk assessment for [company]"
- User requests risk analysis or risk factors
- User wants to understand key vulnerabilities

**Optional depth:** For **accounting / manipulation** and **forensic** risk, supplement with [../equity-analysis/financial-analysis/red-flags-checklist.md](../equity-analysis/financial-analysis/red-flags-checklist.md).

## Workflow Steps

### Step 1: Identify the Company

Call `find_securities` with the company name to get the RavenPack entity_id.

### Step 2: Analyze Financial Health Baseline

Call `bigdata_company_tearsheet` with the entity_id to analyze:
- **Leverage ratios:** Debt-to-equity, debt-to-assets, debt-to-EBITDA
- **Liquidity metrics:** Current ratio, quick ratio, cash position
- **Cash flow generation:** Operating cash flow, free cash flow trends
- **Debt maturity schedule:** Short-term vs. long-term debt
- **Interest coverage:** Ability to service debt

This establishes financial risk baseline.

### Step 2b: Financial distress quick screen

When **leverage is elevated**, **interest coverage is thin**, **FCF is weak vs debt service**, or **liquidity is tight**, add a quantitative flag:

- **Altman Z-Score (simplified):** compute from tearsheet / latest filing inputs when possible (working capital, retained earnings, EBIT, equity, total liabilities, sales, total assets). If inputs are incomplete, state **data gaps** and give a **qualitative distress read** instead.  
- **Beneish / manipulation context:** if accruals or earnings quality look aggressive, point to [../equity-analysis/financial-analysis/red-flags-checklist.md](../equity-analysis/financial-analysis/red-flags-checklist.md); optional use of `earnings_quality.py` only if the user wants script output—workflows default to tearsheet + judgment.

### Step 2c: Moat and competitive durability

Identify **moat type** (if any) and **erosion** risks using [../equity-analysis/competitive-analysis/moat-taxonomy.md](../equity-analysis/competitive-analysis/moat-taxonomy.md). Consider:

- **Pricing power** trend vs peers  
- **Share** shifts to entrants or substitutes  
- **ROIC** compression vs history and vs cost of capital  

Use `bigdata_search` if needed: "[Company Name] pricing power market share competition ROIC".

### Step 3: Extract Official Risk Disclosures

Use `bigdata_search` to find risk factors from SEC filings:

**Search for 10-K risk factors:**
```
"risk factors material risks regulatory competitive in the last 10-K SEC filing of [Company Name]"
```

This captures the company's official risk disclosures from the most recent annual report.

### Step 4: Search for Material Events in 8-K Filings

Use `bigdata_search` to find recent material events:

**Search for 8-K filings:**
```
"material events changes risks in 8-K SEC filing of [Company Name] in the last 90 days"
```

8-K filings disclose significant corporate events that may present new risks.

### Step 5: Search News for Emerging Risks

Use `bigdata_search` to find recent risk-related news:

**Recommended searches:**
- "[Company Name] regulatory investigation lawsuit controversy in the last 30 days"
- "[Company Name] competitive pressure market share losses"
- "[Company Name] supply chain disruption operational challenges"
- "[Company Name] executive departure management changes"
- "[Company Name] cybersecurity breach data incident"

Conduct 4-6 targeted searches covering different risk categories.

### Step 5b: Management and governance signals

Use `bigdata_search` for governance and incentives (especially for concentrated-holding or founder-led names):

- "[Company Name] CEO chairman combined role board independence"
- "[Company Name] insider selling stock compensation"
- "[Company Name] activist shareholder governance"
- "[Company Name] related party transactions"

Cross-check patterns with [../equity-analysis/management/capital-allocation.md](../equity-analysis/management/capital-allocation.md) (governance and incentive red flags).

### Step 6: Categorize and Rate Risks

Organize findings into **six** risk categories, rating each by:
- **Likelihood:** High / Medium / Low
- **Impact:** High / Medium / Low

Tie **competitive** risks to **moat erosion** where relevant. Connect the **likelihood × impact** view to a **brief scenario bridge** (bull/base/bear **narrative** for value drivers—not full DCF) in the output.

## Risk Categories

### 1. Regulatory/Legal Exposure
- Pending litigation and potential outcomes
- Regulatory investigations or compliance issues
- Antitrust or competition law concerns
- Changes in regulatory framework
- Product liability or recall risks

### 2. Competitive Threats (include moat erosion)

- **Moat type** the business relies on (network, switching costs, cost advantage, intangibles, efficient scale) and **how it could erode**  
- Market share erosion or intensifying competition  
- New entrants or disruptive technologies  
- Pricing pressure or margin compression (often **first signal of moat damage**)  
- Loss of key customers or contracts  
- Competitive product launches  
- **ROIC vs WACC** compression vs history (tie to long-term structural risk)

### 3. Operational Vulnerabilities
- Supply chain disruptions or dependencies
- Key personnel dependencies or talent retention
- Technology infrastructure risks or cyber threats
- Manufacturing or production constraints
- Quality control or operational execution issues

### 4. Financial/Balance Sheet Risks
- Debt refinancing requirements or covenant concerns  
- Liquidity constraints or working capital issues  
- Currency or interest rate exposure  
- Pension or benefit plan obligations  
- Off-balance sheet liabilities  
- **Distress / bankruptcy remoteness:** incorporate Step 2b findings (Z-Score, cash conversion)

### 5. Macro/Market Headwinds
- Economic cycle sensitivity or recession exposure
- Geopolitical exposure or international risks
- Industry-wide challenges or secular decline
- Commodity price volatility
- Regulatory or policy changes affecting industry

### 6. Management & Governance
- Board independence, **dual CEO/Chair**, classified board, related-party exposure  
- **Compensation** design vs performance; equity grant dilution  
- **Insider buying/selling** patterns (context-aware, not mechanical)  
- Capital allocation credibility (M&A, buybacks, dividends) and **guidance** track record  
- Succession and key-person risk  

## Output Format

Add inline citation with Superscript Numbers [1], [2] immediately after claims and add a hyperlink pointing to the document url.

Structure the report as:

```
# Risk Assessment: [Company Name]
Assessment Date: [Date]

## Executive Summary
[2-3 sentences: **top risks that matter** for value—apply ./analytical-frameworks.md]

## Financial Health Baseline

### Leverage and Liquidity
| Metric | Current | Industry Avg | Assessment |
|--------|---------|--------------|------------|
| Debt-to-Equity | X.Xx | X.Xx | [High/Normal/Low] |
| Current Ratio | X.Xx | X.Xx | [Strong/Adequate/Weak] |
| Interest Coverage | X.Xx | X.Xx | [Strong/Adequate/Weak] |
| Cash Position | $X.XB | - | [Strong/Adequate/Weak] |

### Key Financial Observations
- [Observation 1]
- [Observation 2]

### Financial distress screen (if leverage or coverage is weak)
| Signal | Value / read | Note |
|--------|----------------|------|
| Altman Z (if computable) | | [Zone: safe / grey / distress] |
| Cash conversion vs earnings | | |
| Covenant / maturity (if known) | | |

## Moat and competitive durability
- **Primary moat type(s):** [per moat taxonomy]  
- **Erosion warning signs:** [pricing, share, ROIC vs WACC, other]  
- **Narrative:** [1 short paragraph]

## Risk Category Analysis

### 1. Regulatory/Legal Exposure

**Identified Risks:**
1. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

2. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

**Category Risk Score:** [High/Medium/Low based on aggregate likelihood × impact]

---

### 2. Competitive Threats

**Moat link:** Each major competitive risk should state **how it could damage the moat or ROIC spread** (not only “more competition”).

**Identified Risks:**
1. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

2. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

**Category Risk Score:** [High/Medium/Low based on aggregate likelihood × impact]

---

### 3. Operational Vulnerabilities

**Identified Risks:**
1. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

2. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

**Category Risk Score:** [High/Medium/Low based on aggregate likelihood × impact]

---

### 4. Financial/Balance Sheet Risks

**Identified Risks:**
1. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [Tearsheet / 10-K / 8-K with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

2. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [Tearsheet / 10-K / 8-K with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

**Category Risk Score:** [High/Medium/Low based on aggregate likelihood × impact]

---

### 5. Macro/Market Headwinds

**Identified Risks:**
1. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

2. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [10-K / 8-K / News with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

**Category Risk Score:** [High/Medium/Low based on aggregate likelihood × impact]

---

### 6. Management & Governance

**Identified Risks:**
1. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [Filing / News / Tearsheet with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

2. **[Risk Name]**
   - Description: [Detailed explanation]
   - Source: [Filing / News / Tearsheet with date]
   - Likelihood: **[High/Medium/Low]**
   - Impact: **[High/Medium/Low]**
   - Mitigation Status: [Known mitigations if disclosed]

**Category Risk Score:** [High/Medium/Low based on aggregate likelihood × impact]

---

## Top 5 Priority Risks
(Ranked by Likelihood × Impact)

1. **[Risk Category]: [Risk Name]**
   - Combined Score: [Likelihood] × [Impact]
   - Why This Matters: [Brief explanation]

2. **[Risk Category]: [Risk Name]**
   - Combined Score: [Likelihood] × [Impact]
   - Why This Matters: [Brief explanation]

3. **[Risk Category]: [Risk Name]**
   - Combined Score: [Likelihood] × [Impact]
   - Why This Matters: [Brief explanation]

4. **[Risk Category]: [Risk Name]**
   - Combined Score: [Likelihood] × [Impact]
   - Why This Matters: [Brief explanation]

5. **[Risk Category]: [Risk Name]**
   - Combined Score: [Likelihood] × [Impact]
   - Why This Matters: [Brief explanation]

## Risk Mitigation Overview

### Disclosed Mitigations from 10-K
- [Mitigation 1]: [How company addresses this risk]
- [Mitigation 2]: [How company addresses this risk]
- [Mitigation 3]: [How company addresses this risk]

### Gap Analysis
- [Areas where mitigation appears inadequate or unclear]

## Scenario bridge (valuation / outcomes)

Connect risks to **forward outcomes** (narrative + rough probabilities—**not** a full model unless the user asks):

| Scenario | Probability (indicative) | Key drivers | Implication for multiples / earnings power |
|----------|-------------------------|-------------|-------------------------------------------|
| Bull | | | |
| Base | | | |
| Bear | | | |

For methodology depth: [../equity-analysis/variant-perception/thesis-construction.md](../equity-analysis/variant-perception/thesis-construction.md).

## Investment Implications

### Overall Risk Profile
[High Risk / Moderate Risk / Low Risk with explanation]

### Risk-Adjusted Investment Thesis
[How identified risks affect investment attractiveness]

### Key Monitoring Points
[What investors should watch to track risk evolution]
- [Monitoring point 1]
- [Monitoring point 2]
- [Monitoring point 3]

### Valuation Considerations
[How risk profile should affect valuation multiples or required return]

**Closing (structured):** Net assessment: [Positive/Negative/Neutral] on risk-adjusted attractiveness because [specific]; key risk: [X]; next catalyst: [Y].

## Sources
  ALWAYS include a "Sources" section at the end listing ALL documents referenced with:
   - Reference number matching the inline Superscript Numbers
   - Source name and Publication date (MMM DD, YYYY format) with a hyperlink to the URL
  
   **Example:**
   [1] (NVIDIA Q3 2026 Earnings Call - Nov 19, 2025)[https://www.benzinga.com/node/...]
   [2] (Benzinga - Nov 20, 2025)[https://www.benzinga.com/node/...]
   [3] (Yahoo! Finance - Jan 18, 2026)[https://finance.yahoo.com/news/...]


---

**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

## Best Practices

- Apply [analytical-frameworks.md](./analytical-frameworks.md): **prioritize** what moves the name  
- **Start with official disclosures** (10-K risk factors) as authoritative baseline  
- **Validate with recent filings** (8-K) to catch emerging risks  
- **Supplement with news** for real-time developments not yet in SEC filings  
- **Moat and governance** are first-order—use Steps 2c and 5b  
- **Distress screen** when leverage/coverage is weak (Step 2b)  
- **Be objective in rating** likelihood and impact—evidence-based  
- **Distinguish materiality**—focus on risks that could significantly impact business/valuation  
- **Note mitigation status**—what the company is doing to address risks  
- **Scenario bridge** makes the assessment actionable vs descriptive  
- **Update quarterly**—risk profile changes with new 10-Q/10-K filings  

## Likelihood and Impact Rating Guide

### Likelihood Scale
- **High:** >50% probability of occurring within 12 months or already materializing
- **Medium:** 20-50% probability within 12-24 months
- **Low:** <20% probability or >24 months out

### Impact Scale
- **High:** Could affect >10% of revenue/earnings or represent existential threat
- **Medium:** Could affect 3-10% of revenue/earnings or significantly impair operations
- **Low:** <3% revenue/earnings impact or manageable operational disruption

### Combined Priority
- High × High = Critical Priority (Immediate attention required)
- High × Medium or Medium × High = High Priority (Close monitoring needed)
- Medium × Medium = Medium Priority (Monitor and assess)
- All others = Lower Priority (Awareness sufficient)

## Key Differences from Other Workflows

- **vs. Company Brief:** Risk Assessment is comprehensive risk-focused; Brief covers all recent developments
- **vs. Earnings Preview/Digest:** Risk Assessment is long-term risk profile; Earnings focuses on quarterly performance
- **Focus:** This workflow specifically targets risk identification, quantification, and prioritization

## Example Queries to User

If 10-K not found:
- "I couldn't locate the most recent 10-K filing. Should I proceed with 8-K filings and news-based risk analysis?"

If minimal risks identified:
- "Risk profile appears relatively low based on available information. Would you like me to expand the search parameters or focus on industry-specific risks?"
