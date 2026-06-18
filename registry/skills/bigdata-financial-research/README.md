# Financial Research Analyst

Part of the **Bigdata.com**

An AI-powered financial research capability that transforms your agent
platform into a professional-grade Financial Research Analyst.

Powered by **Bigdata.com MCP**, this module automates
institutional-quality research workflows and produces structured,
decision-ready deliverables.

---

## Overview

The Financial Research Analyst module enables structured financial
analysis directly inside Claude and other supported agent platforms.

It combines:

- Bigdata.com financial data
- News and filings
- Analyst estimates
- Structured research frameworks

To generate consistent, professional outputs suitable for internal
investment teams or client-facing materials.

---

## What It Enables

### Research & Analysis

- **Company Briefs**\
  30-day development summaries with categorized news, key events, and
  investment implications.

- **Earnings Previews**\
  Pre-earnings analysis including bull/bear scenarios and key metrics
  to monitor.

- **Earnings Digests**\
  Post-earnings breakdowns covering surprises, guidance updates, and
  analyst reactions.

- **Risk Assessments**\
  Structured risk profiles with likelihood/impact ratings based on SEC
  filings, news, and company disclosures.

---

### Documents & Deliverables

- **Investment Memos**\
  Structured buy/sell/hold recommendations with supporting thesis and
  data.

- **Pitch Deck Content**\
  Key slide content for investment committee discussions.

- **Quick Updates**\
  Morning briefs or client-ready summaries.

---

## Usage (Within the Plugin)

Once the **Bigdata.com** plugin is installed, financial
research capabilities are accessible via namespaced commands such as:

    /bigdata:financial-research

Example:

    /bigdata:financial-research NVIDIA earnings preview

---

## Customization (Advanced / Dev-Only)

If you are customizing this module inside your own fork of the plugin
repository, you may adjust:

- Report templates and formatting
- Section structure and analytical depth
- Output formatting (Markdown, Word-ready content, etc.)
- Risk frameworks and scoring models
- Default research scope

All implementation files are located under:

    skills/financial-research-analyst/

---

## Requirements

This module requires an active **Bigdata.com MCP** connection configured
in your agent platform.

It relies on MCP for:

- Financial statements
- News
- Regulatory filings
- Analyst estimates
- Market data

Refer to the official Bigdata.com documentation portal for detailed
setup instructions for your platform.

---

## License

See the root `LICENSE` file of the plugin repository for details.
