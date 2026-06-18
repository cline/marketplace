---
name: post-ipo-common
description: Shared scope rules, data foundation, and verification checklist for all post-IPO event-driven workflows (day-1 reaction, day-14 index inclusion, day-179 lock-up, day-365 founder lock-up). Read this before any individual post-IPO workflow.
---

# Post-IPO Analysis — Shared Conventions

The post-IPO workflows are **event-driven research notes** on a company that has **already listed**. Each one is anchored to a specific point on the post-IPO timeline and the catalyst that falls just after it:

| Workflow | Run on (trading day) | Catalyst analyzed |
|----------|----------------------|-------------------|
| [post-ipo-day1.md](./post-ipo-day1.md) | Day 1 close | First-day price discovery and aftermarket setup |
| [post-ipo-day14.md](./post-ipo-day14.md) | Day 14 | NASDAQ-100 fast-track inclusion (effective ~day 15) |
| [post-ipo-day179.md](./post-ipo-day179.md) | Day 179 | 180-day lock-up expiry |
| [post-ipo-day365.md](./post-ipo-day365.md) | Day 365 | 366-day founder/major-investor lock-up expiry; float expansion |

## Scope rules (apply to every post-IPO workflow)

- **Already-listed companies only.** If the company has not yet priced, route to the pre-IPO workflow: [../private_company/pre-ipo-analysis.md](../private_company/pre-ipo-analysis.md). Confirm the listing date and compute the trading-day count before choosing the workflow.
- **Balanced framing only.** Never give a buy/sell/hold, participate/avoid, price target, or conviction rating. Present the setup, the mechanics, bull and bear reads, and dated watch points; let the reader decide.
- **No invented data.** If a figure (offer price, float %, lock-up share count, index AUM, eligibility threshold) is not in a source, state "not disclosed" or "to be confirmed" rather than estimating. Label every third-party estimate and every back-of-envelope calculation as such, and show the arithmetic.
- **Verify the rules, don't assume them.** Index-inclusion eligibility and lock-up terms change and are issuer-specific. Confirm them against the prospectus (S-1/F-1/424B), the exchange's current index methodology, and recent filings — do not rely on rules of thumb in this skill.
- **Quiet period awareness.** Underwriter-affiliated analysts are typically restricted from publishing ratings for a period after the IPO. Note where sell-side coverage does not yet exist rather than implying consensus that isn't there.

## Data foundation (complete BEFORE building the report)

Establish the factual base with Bigdata.com MCP tools first, then fill gaps with web search:

1. `find_securities` → RavenPack `entity_id` and confirm the listed ticker/exchange.
2. `bigdata_company_tearsheet` → price, market cap, shares outstanding, free float, financials, sentiment baseline.
3. `bigdata_search` → IPO terms and lock-up language from the prospectus, news flow, secondary-offering filings, insider intentions, analyst commentary. One focus and one time period per call; natural-language queries; preserve user wording on dates.
4. `bigdata_events_calendar` → next earnings date and other scheduled events (when `entity_id` is available).
5. **Web search** → daily price/volume since listing, exchange index methodology and eligibility thresholds, passive AUM tracking the relevant index, and historical analogs for the catalyst.

**Reference math used across these workflows** (always show the inputs and label estimates):
- **First-day return** = (first-day close − offer price) / offer price.
- **Free float** = shares outstanding − locked/insider/strategic shares. Track it as a % of shares outstanding.
- **Days-to-trade / overhang** = newly tradable shares / average daily volume (ADV). Higher = heavier supply digestion.
- **Implied passive demand** from index inclusion ≈ estimated index weight × tracking AUM / price = shares passive funds must buy; compare to ADV for a days-to-cover read.

**Fallback:** if Bigdata.com tools are unavailable, complete every step with web search only and note in the footer that sentiment/entity data was limited to public sources.

Record source name + date for every material fact as you collect it.

## Build and output (every post-IPO workflow)

- Follow the matching template in `../../assets/templates/` (named per workflow). Do not start report/PDF generation until research is complete.
- Length: 4–7 pages (lighter than the pre-IPO note — these are single-catalyst).
- Cover line: company name, the workflow title (e.g. "Post-IPO — 180-Day Lock-Up Expiry"), date, "Prepared with Claude".
- **Inline citations** [1], [2], … after every claim from a source, hyperlinked to the document URL. Bigdata.com content branded exactly "Bigdata.com" and linked to the `url` from the `bigdata_search` response.
- End with a full **Sources** section, then the standard footer per [../../assets/templates/report-footer.md](../../assets/templates/report-footer.md) (verbatim).

## Verify before delivering

- Every number traces to a recorded source or a labeled, shown calculation.
- Internal consistency: float % + locked % reconcile to shares outstanding; market cap = price × shares outstanding.
- The trading-day count matches the listing date and the catalyst date is correct.
- No recommendation/price-target language slipped in ("we recommend", "attractive entry", "avoid", "buy the dip").
- Eligibility/lock-up rules are cited to a source, not asserted from memory.
