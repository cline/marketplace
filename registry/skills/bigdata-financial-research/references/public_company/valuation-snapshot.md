# Valuation snapshot workflow

Lightweight answer path when the user asks **what a company is worth**, **whether it’s cheap/expensive**, or for a **valuation snapshot**—without requiring a full investment memo or standalone model build.

## When to use

- "What is [company] worth?"
- "Is [ticker] expensive vs peers?"
- "Valuation snapshot for [company]"
- "What’s priced in for [company]?"

## Workflow steps

### Step 1: Identify the company

`find_securities` → entity id.

### Step 2: Pull valuation inputs

`bigdata_company_tearsheet` → current and historical multiples, estimates, margins, FCF where shown, segment context.

### Step 3: Peer and history context

- Use tearsheet peer set or `bigdata_search`: "[Company] valuation vs peers EV EBITDA PE comparison"  
- Note **current** vs **~5-year range** or **trailing average** when tearsheet or search allows (approximate if only spot data).

### Step 4: Implied expectations (reverse DCF mindset)

Without building a full model, articulate **what has to go right** at the current price: growth, margins, reinvestment, and risk premium. Methodology depth: [../equity-analysis/valuation/reverse-dcf.md](../equity-analysis/valuation/reverse-dcf.md).

### Step 5: Synthesize

Combine **multiples cross-check** + **implied expectations** + **2–3 value drivers** (see [analytical-frameworks.md](./analytical-frameworks.md)).

## Output template

```markdown
# Valuation snapshot: [Company] ([Ticker])

## Executive summary
[2–3 sentences: cheap/fair/rich vs history and peers; what the price implies]

## Multiple cross-check

| Metric | Now | ~5Y avg / prior range (if known) | vs peer median | Read |
|--------|-----|-----------------------------------|----------------|------|
| EV/EBITDA | | | | |
| P/E (NTM or TTM) | | | | |
| FCF yield | | | | |
| [Sector KPI if obvious] | | | | |

## What’s priced in
- **Revenue growth:** consensus vs what multiple implies  
- **Margins:** embedded vs recent trend  
- **Risk:** de-rating or re-rating vs fundamentals  

## Key drivers to monitor
1. [Driver — what would change fair value]
2. [Driver]
3. [Driver]

## Caveats
- [Data gaps, one-time items, accounting quirks]

**Closing (structured):** Net assessment: [Cheap/Fair/Rich vs setup] because [specific]; key risk: [X]; next catalyst: [Y].

## Sources
[Numbered sources with URLs]

---
**Powered by Bigdata.com** - https://bigdata.com

## Disclaimer

This output is for informational and research-assistance purposes only. It does **not** constitute investment, legal, tax, accounting, or other professional advice, and it is **not** a recommendation to buy, sell, or hold any security or instrument or to pursue any strategy. Information may be incomplete, estimated, delayed, or inaccurate. Past performance does not guarantee future results. Verify material facts independently and consult qualified advisors before making decisions.
```

## Practices

- Prefer **tearsheet + search**; do not require Python or spreadsheet models unless the user asks.  
- For full DCF mechanics and sum-of-parts, see [../equity-analysis/valuation/](../equity-analysis/valuation/).
