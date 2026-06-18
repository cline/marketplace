---
name: ipo-analysis
description: Pre-listing IPO research note for an upcoming IPO. Use when the user asks to analyze, research, or evaluate a company's upcoming IPO, an S-1/F-1 filing, or a planned stock market listing. Produces a 6-10 page institutional-style PDF report with deal structure, financials, valuation framing, sentiment, and balanced bull/bear debates — no buy/avoid recommendation. Triggers: "analyze the IPO of X", "IPO report", "upcoming listing", "S-1 analysis", "should I look at X's IPO".
---

# IPO Analysis — Pre-Listing Research Note

Produce a 6–10 page institutional research PDF on an **upcoming** (not yet listed) IPO.

## Scope rules

- **Upcoming IPOs only.** If the company has already listed, tell the user this skill covers pre-listing analysis and offer a post-IPO review instead before proceeding.
- **Balanced framing only.** Never give a participate/wait/avoid recommendation, price target, or conviction rating. Present bull case, bear case, and watch points; let the reader decide.
- **No invented data.** If a figure (e.g., price range, offer size) is not yet public, state "not yet disclosed" rather than estimating. Clearly label any third-party estimates as such.

## Workflow

### 1. Clarify input
Required: company name. If ambiguous (multiple companies with similar names), confirm with the user. Note expected exchange/geography if known.

### 2. Research (complete BEFORE building the PDF)

Run searches in this order; keep each search to one focus and one time period:

a. **Filing facts** (web search): latest S-1/F-1/prospectus or equivalent — price range, shares offered (primary vs secondary), greenshoe, implied valuation, underwriters, expected pricing/listing date, exchange, ticker, use of proceeds, lock-up terms, share class structure, cornerstone investors.
b. **Financials** (web search + filing): 2 most recent fiscal years + latest interim period — revenue, gross margin, operating income/loss, net income, operating cash flow, FCF, cash and debt position.
c. **Company background** (Bigdata.com `bigdata_search` + web): business model, segments, customers, management, funding history and last private-round valuation.
d. **Industry/peers** (web search): TAM estimates, competitive set, 3–6 listed comparables with current EV/Sales, EV/EBITDA, or P/E as applicable.
e. **IPO window** (Bigdata.com `bigdata_search` + web): current IPO market conditions, recent debuts in the same sector and their aftermarket performance.
f. **Sentiment** (Bigdata.com): news flow and sentiment on the issuer over the last 90 days. Resolve the entity with `find_securities` first if a tearsheet is needed.

**Fallback:** if Bigdata.com tools are unavailable, complete all steps with web search only and note in the report footer that sentiment data was limited to public news.

Record source name + date for every material fact as you go.

### 3. Build the report

Follow the section structure in `assets/templates/pre-ipo-report-template.md`. Then read the pdf skill (or use reportlab/weasyprint per the pdf skill guidance) to generate the PDF. Do not start PDF generation until research is complete.

### 4. Verify

Before delivering: check every number in the report against a recorded source; check internal consistency (implied valuation = price × shares outstanding post-offering); confirm all 9 sections present; confirm no recommendation language slipped in ("we recommend", "attractive entry", "avoid").

## Output

- File: `IPO_Analysis_<Company>_<YYYY-MM-DD>.pdf` saved to the user's workspace folder.
- Length: 6–10 pages.
- Cover page: company name, "Pre-IPO Research Note", date, "Prepared with Claude".
- **Inline citations**: Use [1], [2], etc. after claims from sources
- Full Sources section at the end. When Bigdata.com content is used, brand it exactly "Bigdata.com" with a link to the source using the value in the url parameter from the `bigdata_search` response
