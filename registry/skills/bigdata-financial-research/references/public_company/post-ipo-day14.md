---
name: post-ipo-day14
description: Day-14 post-IPO note on potential NASDAQ-100 fast-track index inclusion. Use ~2 weeks after a major IPO to assess the stock's status and the potential impact of fast-track inclusion in the NASDAQ-100 (effective around day 15 of trading). Estimates passive-flow demand and the index effect; balanced, no buy/avoid call. Triggers: "NASDAQ-100 fast track for X", "index inclusion impact X", "post-IPO day 14", "will X be added to the Nasdaq-100".
---

# Post-IPO Day 14 — NASDAQ-100 Fast-Track Inclusion

A major IPO can qualify for **fast-track inclusion** in the NASDAQ-100 after a short minimum trading period (the user's premise: eligibility assessed after ~15 trading days). Run this note around **day 14** to capture the stock's status and the potential impact **before** inclusion takes effect.

Read [post-ipo-common.md](./post-ipo-common.md) first for scope rules, the data foundation, and the verify checklist.

> **Verify the rule, don't assume it.** NASDAQ-100 fast-entry eligibility (minimum trading days, the market-cap-rank threshold — historically top ~25% of the index) and the effective date are set by Nasdaq's published index methodology and can change. Confirm the current criteria and the specific effective date via web search before drawing conclusions; state them as cited facts, not assumptions.

## What this note answers

- Does the stock plausibly meet the fast-track eligibility criteria (market-cap rank, liquidity, seasoning)?
- If included, how large is the likely index weight and the mechanical passive demand?
- How does that demand compare to average daily volume (the "index effect" run-up / reversal risk)?
- How is the stock trading two weeks in, and what's already priced in?

## Workflow

### 1. Two-week trading status
Price vs offer and vs day-1 close, trend and volatility, average daily volume (ADV), and current free float. Summarize whether the deal is working or fading.

### 2. Eligibility check (cite the methodology)
From Nasdaq's current index methodology: minimum trading period, market-cap threshold, and liquidity/float requirements. Compare the company's market cap to the smallest current NASDAQ-100 constituents to gauge where it would rank. State eligibility as **likely / borderline / unlikely**, with the source.

### 3. Passive-demand estimate (show the math, label as estimate)
- Estimate the **float-adjusted index weight** = company float-adjusted market cap / total NASDAQ-100 float-adjusted market cap.
- **Implied passive buying** ≈ index weight × AUM tracking the NASDAQ-100 (QQQ + other trackers; cite the AUM figure) / price = shares passive funds must buy.
- **Days-to-cover** = implied passive buying / ADV. This is the core "index effect" magnitude.

### 4. The index effect
Historical pattern: additions often drift up into the effective date as funds and front-runners accumulate, sometimes partially reversing afterward. Cite recent NASDAQ-100 fast-track additions as analogs and how they traded around the event.

### 5. Sentiment and risks
Bigdata.com sentiment and positioning. Risks both ways: inclusion not granted or delayed; the move already priced in; post-event reversal; high float/ADV diluting the effect.

### 6. Watch points
Effective inclusion/rebalance date, rebalance mechanics, lock-up expiries (180- and 366-day), first earnings.

## Output

Follow [../../assets/templates/post-ipo-day14-report-template.md](../../assets/templates/post-ipo-day14-report-template.md). Present the inclusion scenario and its mechanics — no recommendation or price target. File: `Post_IPO_Day14_IndexInclusion_<Company>_<YYYY-MM-DD>.pdf` (or .docx/markdown per the user's requested format).
