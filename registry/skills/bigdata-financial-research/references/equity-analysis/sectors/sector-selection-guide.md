# Sector Selection Guide

## Table of Contents
1. [GICS Classification Overview](#gics-classification-overview)
2. [Sector File Selection Decision Tree](#sector-file-selection-decision-tree)
3. [Cross-Sector Considerations](#cross-sector-considerations)
4. [Sector-Specific Valuation Methodology Summary](#sector-specific-valuation-methodology-summary)
5. [Quick Reference: When Sector Files Apply](#quick-reference-when-sector-files-apply)

## GICS Classification Overview

The Global Industry Classification Standard (GICS) organizes companies into a four-tier hierarchy: 11 sectors, 25 industry groups, 74 industries, and 163 sub-industries. This framework provides standardized categorization for equity analysis.

| GICS Sector | Key Characteristics |
|-------------|---------------------|
| Energy | Oil, gas, consumable fuels, energy equipment |
| Materials | Chemicals, metals, mining, paper, containers |
| Industrials | Capital goods, transportation, commercial services |
| Consumer Discretionary | Retail, autos, durables, apparel, leisure |
| Consumer Staples | Food, beverages, tobacco, household products |
| Health Care | Pharma, biotech, equipment, services, managed care |
| Financials | Banks, insurance, capital markets, REITs |
| Information Technology | Software, hardware, semiconductors, IT services |
| Communication Services | Telecom, media, entertainment, interactive media |
| Utilities | Electric, gas, water utilities, IPPs |
| Real Estate | REITs, real estate development and services |

## Sector File Selection Decision Tree

### Step 1: Identify Primary Revenue Source

Determine where the majority of revenue originates:

1. **Manufacturing capital goods, equipment, or providing B2B services** - Load `industrials.md`
2. **Selling products directly to consumers** - Load `consumer-retail.md`
3. **Extracting, processing, transporting, or generating energy** - Load `energy.md`

### Step 2: Validate Subsector Alignment

Confirm the company's business model matches the selected sector file:

**Industrials** covers:
- Aerospace and defense contractors
- Machinery and equipment manufacturers
- Electrical equipment and components
- Building products and construction materials
- Transportation and logistics providers
- Commercial and professional services

**Consumer/Retail** covers:
- Specialty and broadline retailers
- E-commerce platforms
- Restaurants and food service
- Consumer durables manufacturers
- Apparel and footwear brands
- Direct-to-consumer businesses

**Energy** covers:
- Exploration and production companies
- Midstream pipeline and infrastructure operators
- Refiners and fuel marketers
- Oilfield services providers
- Integrated oil companies
- Renewable energy developers

### Step 3: Handle Edge Cases

Some companies require judgment in sector assignment:

| Company Type | Recommended Approach |
|--------------|---------------------|
| Industrial distributors | Industrials (capital goods focus) or Consumer (if retail format) |
| Auto manufacturers | Consumer Discretionary GICS, but load Industrials for manufacturing KPIs |
| Food manufacturers | Consumer Staples, but load Consumer-Retail for channel analysis |
| Utility equipment makers | Industrials (not Energy) |
| Energy equipment makers | Energy (oilfield services) or Industrials (general equipment) |

## Cross-Sector Considerations

### Conglomerates and Diversified Companies

For companies operating across multiple sectors:

1. **Identify dominant segment** - Load the sector file representing the largest revenue or EBIT contribution
2. **Load secondary sector files** - If a secondary segment exceeds 25% of revenue or EBIT, load its sector file for segment-specific KPIs
3. **Sum-of-parts valuation** - Apply appropriate sector multiples to each segment

### Vertical Integration

Vertically integrated companies may span multiple sector files:

| Business Model | Files to Load |
|----------------|---------------|
| Integrated oil company | Energy (all subsections apply) |
| Vertically integrated retailer with manufacturing | Consumer-Retail + relevant manufacturing KPIs |
| Aerospace OEM with aftermarket services | Industrials (comprehensive coverage) |

### When to Load Multiple Sector Files

Load multiple files when:
- Company has distinct business segments exceeding 25% of revenue
- Valuation requires segment-level multiple application
- Competitive analysis spans different industry verticals
- M&A analysis involves cross-sector combinations

## Sector-Specific Valuation Methodology Summary

| Sector | Primary Valuation | Key Adjustments |
|--------|-------------------|-----------------|
| Industrials | EV/EBITDA (4.5-12x) | Cycle normalization, backlog premium, aftermarket mix |
| Consumer/Retail | EV/EBITDA (4-25x) | Same-store momentum, inventory adjustment, DTC margin validation |
| Energy (E&P) | NAV (PV-10), EV/EBITDAX | Commodity price sensitivity, reserve quality |
| Energy (Midstream) | DCF yield, EV/EBITDA | Contract structure, leverage, volume risk |
| Energy (Refining) | Mid-cycle EV/EBITDA | Crack spread normalization, complexity |
| Energy (OFS) | Through-cycle EV/EBITDA | Activity normalization, utilization |
| Energy (Renewables) | DCF on contracted | PPA quality, development pipeline risk |

## Quick Reference: When Sector Files Apply

| If analyzing... | Load... |
|-----------------|---------|
| Boeing, Caterpillar, Honeywell | `industrials.md` |
| Walmart, Nike, Amazon | `consumer-retail.md` |
| ExxonMobil, Kinder Morgan, Schlumberger | `energy.md` |
| General Electric (diversified) | `industrials.md` + segment-specific files |
| Tesla | `consumer-retail.md` (auto sales) + `industrials.md` (manufacturing) |
