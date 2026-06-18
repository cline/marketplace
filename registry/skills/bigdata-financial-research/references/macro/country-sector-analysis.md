# Country-Sector Combined Analysis Workflow

## When to Use
- "Macro analysis of [Sector] investment in [Country]"
- "[Sector] sector outlook in [Country/Region]"
- "Technology investment in the USA"
- "European financials analysis"
- "India consumer sector outlook"
- "China EV/automotive sector analysis"
- Any request combining a **specific sector** with a **specific country/region**

## Workflow Steps

### Step 1: Search Country Economic Context
Use `bigdata_search` to gather macroeconomic backdrop:

```
bigdata_search("[Country] economic outlook GDP growth 2026")
bigdata_search("[Country] inflation interest rates monetary policy")
bigdata_search("[Country] central bank rate decision outlook")
```

Extract: GDP growth, inflation, interest rates, policy environment

### Step 2: Search Country-Specific Sector News
Use `bigdata_search` with **country + sector** queries:
- "[Country] [Sector] sector outlook 2026"
- "[Country] [Sector] industry trends performance"
- "[Country] [Sector] regulatory policy government"
- "[Country] [Sector] investment flows foreign domestic"
- "[Country] [Sector] earnings revenue growth"
- "[Country] [Sector] valuations multiples"
- "[Country] [Sector] headwinds risks challenges"
- "[Country] [Sector] tailwinds opportunities growth drivers"

**Example for "US Technology":**
- "US technology sector outlook 2026"
- "United States technology AI semiconductor investment"
- "US tech regulatory antitrust policy"
- "American technology companies earnings growth"

### Step 3: Identify Country-Domiciled Sector Leaders
Use `find_securities` for 5-10 major companies **headquartered in** or **primarily operating in** that country:

**US Technology Example:**
- Apple, Microsoft, NVIDIA, Alphabet, Amazon, Meta, Broadcom, AMD, Salesforce, Adobe

**India Financials Example:**
- HDFC Bank, ICICI Bank, Axis Bank, State Bank of India, Bajaj Finance

Then call `bigdata_company_tearsheet` for each to get:
- Revenue breakdown by geography (to confirm country exposure)
- Financial metrics and performance
- Analyst estimates and sentiment
- Hiring trends (workforce signals)

### Step 4: Get Country-Specific Sector Events
Use `bigdata_events_calendar` with entity IDs:
- Filter by country's exchange if doing market-wide scan
- Get upcoming earnings for country-domiciled sector leaders

### Step 5: Search Country-Sector Policy & Regulation
Use `bigdata_search`:
- "[Country] [Sector] regulation policy 2026"
- "[Country] government [Sector] subsidies incentives"
- "[Country] [Sector] trade tariffs exports"
- "[Country] [Sector] foreign investment restrictions"

### Step 6: Synthesize Macro-Sector View
Combine:
- Country economic backdrop (from searches)
- Sector-specific trends in that country (from searches)
- Company fundamentals (from tearsheets)
- Policy/regulatory environment
- Valuation relative to global peers

---

## Output Template

```markdown
# Macro Analysis: [Sector] Investment in [Country]
Report Date: [Date]

## Executive Summary
[4-5 sentences: Country economic context + sector positioning + key investment thesis]

---

## Part 1: [Country] Economic Backdrop

### Key Economic Indicators
| Indicator | Current | Trend | Context |
|-----------|---------|-------|---------|
| GDP Growth | X.X% | ↑/↓/→ | [vs peers] |
| Inflation (CPI) | X.X% | ↑/↓/→ | [Context] |
| Policy Rate | X.X% | [Last action] | [Outlook] |
| Unemployment | X.X% | ↑/↓/→ | [Context] |
| Currency (vs USD) | [Level] | YTD: +/-X% | [Outlook] |

### Monetary Policy Outlook
- **Current Stance**: [Restrictive/Neutral/Accommodative]
- **Expected Path**: [X cuts/hikes expected in 2026]
- **Impact on [Sector]**: [How rates affect sector]

### Fiscal Policy Environment
- **Government Spending**: [Relevant programs]
- **Tax Policy**: [Corporate tax, incentives]
- **[Sector]-Specific Policy**: [Subsidies, regulations]

---

## Part 2: [Sector] Sector Analysis in [Country]

### Sector Performance Overview
| Metric | [Country] [Sector] | Global [Sector] | [Country] Broad Market |
|--------|-------------------|-----------------|------------------------|
| YTD Return | +/-X% | +/-X% | +/-X% |
| P/E (Fwd) | X.Xx | X.Xx | X.Xx |
| Revenue Growth | X.X% | X.X% | X.X% |
| Earnings Growth | X.X% | X.X% | X.X% |

### Key Themes & Drivers

#### Tailwinds (Positive for [Country] [Sector])
| Theme | Description | Timeline | Beneficiaries |
|-------|-------------|----------|---------------|
| 1. [Theme] | [Details] | Near/Medium/Long | [Companies] |
| 2. [Theme] | [Details] | Near/Medium/Long | [Companies] |
| 3. [Theme] | [Details] | Near/Medium/Long | [Companies] |

#### Headwinds (Risks for [Country] [Sector])
| Risk | Description | Severity | Most Exposed |
|------|-------------|----------|--------------|
| 1. [Risk] | [Details] | High/Med/Low | [Companies] |
| 2. [Risk] | [Details] | High/Med/Low | [Companies] |

### Regulatory & Policy Environment
- **Current Regulations**: [Key rules affecting sector]
- **Pending Legislation**: [Bills, proposals]
- **Government Support**: [Subsidies, tax breaks, initiatives]
- **Trade Policy Impact**: [Tariffs, export controls]

---

## Part 3: [Country] [Sector] Company Analysis

**Rule:** Render **one analysis block per company**. Do not combine multiple companies in a single subsection (e.g., avoid "Company A & Company B Overview"). Each company selected in Part 2 must have its own dedicated subsection below.

### Sector Leaders Comparison
| Company | Ticker | Mkt Cap | P/E (Fwd) | Rev Growth | Analyst Rating | Price Target |
|---------|--------|---------|-----------|------------|----------------|--------------|
| [Company 1] | [XXX] | $XXB | X.Xx | X.X% | Buy/Hold/Sell | $XXX (+X%) |
| [Company 2] | [XXX] | $XXB | X.Xx | X.X% | Buy/Hold/Sell | $XXX (+X%) |

### [Company 1] ([Ticker])
**Investment View:** [Positive/Neutral/Cautious/Negative] | Price: [Level] | Market Cap: [Size]
[2–4 sentences: key strengths, risks, catalysts, and positioning. Do not merge with another company.]

### [Company 2] ([Ticker])
**Investment View:** [Positive/Neutral/Cautious/Negative] | Price: [Level] | Market Cap: [Size]
[2–4 sentences: key strengths, risks, catalysts, and positioning. Do not merge with another company.]

[Repeat a dedicated ### [Company N] ([Ticker]) block for every company in the comparison table.]

### Sub-Sector Breakdown
| Sub-Sector | [Country] Leaders | Performance | Outlook |
|------------|-------------------|-------------|---------|
| [Sub-sector 1] | [Companies] | +/-X% YTD | Bullish/Neutral/Bearish |
| [Sub-sector 2] | [Companies] | +/-X% YTD | Bullish/Neutral/Bearish |

### Upcoming Earnings Calendar
| Company | Date | EPS Est. | Rev Est. | Key Metrics to Watch |
|---------|------|----------|----------|---------------------|

---

## Part 4: Investment Implications

### Sector Positioning
| Dimension | Assessment | Rationale |
|-----------|------------|-----------|
| **Overall View** | Overweight/Neutral/Underweight | [Brief] |
| **Conviction** | High/Medium/Low | [Brief] |
| **Time Horizon** | Near/Medium/Long-term | [Brief] |

**Rule:** Every company selected in Part 2 must appear in Part 4. Use Top Picks, Areas to Avoid/Underweight, and (if needed) a **Neutral / Hold / Watch** block so that no selected company is omitted.

### Top Picks in [Country] [Sector]
1. **[Company]** ([Ticker]) — [1-2 sentence thesis]
2. **[Company]** ([Ticker]) — [1-2 sentence thesis]

### Areas to Avoid/Underweight
- **[Company/Sub-sector]** — [Reason]

### Neutral / Hold / Watch (if applicable)
Use this subsection when one or more Part 2 companies do not fit clearly as Top Picks or Areas to Avoid. Place each such company here with a brief rationale so **all selected companies are covered**.
- **[Company]** ([Ticker]) — [1-2 sentence rationale for neutral/hold/watch]

### Key Risks to Monitor
| Risk | Probability | Impact | Trigger/Indicator |
|------|-------------|--------|-------------------|

---

## Sources
| # | Source | Date | URL |
|---|--------|------|-----|

---
**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

---

## Common Country-Sector Combinations

### United States (US)
| Sector | Key Companies | Key Themes |
|--------|---------------|------------|
| Technology | Apple, Microsoft, NVIDIA, Alphabet, Amazon | AI, cloud, semiconductors, antitrust |
| Financials | JPMorgan, Bank of America, Goldman Sachs | Rates, regulation, capital markets |
| Healthcare | UnitedHealth, J&J, Pfizer, Eli Lilly | Drug pricing, GLP-1, M&A |
| Energy | ExxonMobil, Chevron, ConocoPhillips | Oil prices, energy transition |
| Consumer | Amazon, Walmart, Home Depot | Consumer spending, e-commerce |

### China (CN)
| Sector | Key Companies | Key Themes |
|--------|---------------|------------|
| Technology | Alibaba, Tencent, Baidu, JD.com | Regulation, AI, e-commerce |
| EV/Auto | BYD, NIO, XPeng, Li Auto | EV adoption, battery, exports |
| Financials | ICBC, CCB, Ping An | Property exposure, rates |
| Consumer | Meituan, PDD, Yum China | Consumption recovery |

### India (IN)
| Sector | Key Companies | Key Themes |
|--------|---------------|------------|
| Financials | HDFC Bank, ICICI Bank, SBI | Credit growth, digital |
| Technology | Infosys, TCS, Wipro, HCL | IT services, AI adoption |
| Consumer | Reliance, Hindustan Unilever | Rising incomes, urbanization |

### Japan (JP)
| Sector | Key Companies | Key Themes |
|--------|---------------|------------|
| Technology | Sony, Tokyo Electron, Keyence | Semiconductors, automation |
| Auto | Toyota, Honda, Nissan | EV transition, yen |
| Financials | Mitsubishi UFJ, Sumitomo | Rate normalization |

### Europe (UK/DE/FR)
| Sector | Key Companies | Key Themes |
|--------|---------------|------------|
| Luxury | LVMH, Hermès, Kering | China demand, aspirational |
| Industrials | Siemens, Schneider, ABB | Automation, green transition |
| Financials | HSBC, BNP Paribas, UBS | Rates, M&A |
| Pharma | Novo Nordisk, Roche, AstraZeneca | GLP-1, oncology |
