#!/usr/bin/env python3
"""
Reverse DCF Model

This module extracts implied market expectations from current stock prices.
Instead of projecting fundamentals to derive a price, it works backwards
from the market price to determine what growth and margin assumptions
are embedded in the current valuation.

Key outputs:
- Implied revenue growth rate
- Implied terminal margin
- Comparison to analyst estimates

Author: Equity Analyst Skill
"""

from typing import Dict, Optional, Tuple
from dataclasses import dataclass


@dataclass
class ReverseDCFInputs:
    """Input parameters for reverse DCF analysis."""
    current_price: float           # Current stock price
    shares_outstanding: float      # Shares outstanding (in millions)
    net_debt: float               # Net debt (debt minus cash)
    wacc: float                   # Weighted average cost of capital
    terminal_growth: float        # Assumed perpetual growth rate
    base_margin: float            # Starting EBITDA margin
    current_revenue: float        # Current annual revenue
    years: int                    # Number of projection years
    tax_rate: float = 0.21        # Corporate tax rate
    capex_pct: float = 0.05       # CapEx as % of revenue
    nwc_pct: float = 0.10         # NWC as % of revenue
    depreciation_pct: float = 0.03  # D&A as % of revenue


@dataclass
class ReverseDCFOutput:
    """Output results from reverse DCF analysis."""
    implied_revenue_growth: float      # Annual revenue growth rate implied by price
    implied_terminal_revenue: float    # Revenue at end of projection period
    implied_terminal_margin: float     # EBITDA margin at terminal year
    implied_fcff_terminal: float       # Terminal year FCFF
    market_implied_ev: float           # Enterprise value from market price
    iterations: int                    # Number of iterations to converge


def calculate_implied_ev(
    price: float,
    shares: float,
    net_debt: float
) -> float:
    """
    Calculate implied enterprise value from market price.

    EV = Market Cap + Net Debt

    Args:
        price: Current stock price
        shares: Shares outstanding
        net_debt: Net debt (positive = debt, negative = net cash)

    Returns:
        Implied enterprise value
    """
    market_cap = price * shares
    return market_cap + net_debt


def calculate_fcff_from_revenue(
    revenue: float,
    ebitda_margin: float,
    tax_rate: float,
    capex_pct: float,
    nwc_change: float,
    depreciation_pct: float
) -> float:
    """
    Calculate FCFF from revenue and margin assumptions.

    Args:
        revenue: Annual revenue
        ebitda_margin: EBITDA margin as decimal
        tax_rate: Tax rate as decimal
        capex_pct: CapEx as % of revenue
        nwc_change: Change in NWC
        depreciation_pct: D&A as % of revenue

    Returns:
        Free cash flow to firm
    """
    ebitda = revenue * ebitda_margin
    depreciation = revenue * depreciation_pct
    ebit = ebitda - depreciation
    nopat = ebit * (1 - tax_rate)
    capex = revenue * capex_pct
    fcff = nopat + depreciation - capex - nwc_change
    return fcff


def project_dcf_value(
    current_revenue: float,
    growth_rate: float,
    margin: float,
    years: int,
    wacc: float,
    terminal_growth: float,
    tax_rate: float,
    capex_pct: float,
    nwc_pct: float,
    depreciation_pct: float
) -> Tuple[float, float]:
    """
    Project DCF value given growth and margin assumptions.

    Args:
        current_revenue: Starting revenue
        growth_rate: Annual revenue growth rate
        margin: EBITDA margin (assumed constant for simplicity)
        years: Projection years
        wacc: Discount rate
        terminal_growth: Perpetual growth rate
        tax_rate: Corporate tax rate
        capex_pct: CapEx as % of revenue
        nwc_pct: NWC as % of revenue
        depreciation_pct: D&A as % of revenue

    Returns:
        Tuple of (enterprise value, terminal year FCFF)
    """
    pv_fcff_sum = 0
    prev_nwc = current_revenue * nwc_pct
    revenue = current_revenue
    terminal_fcff = 0

    for year in range(1, years + 1):
        revenue = revenue * (1 + growth_rate)
        current_nwc = revenue * nwc_pct
        nwc_change = current_nwc - prev_nwc
        prev_nwc = current_nwc

        fcff = calculate_fcff_from_revenue(
            revenue=revenue,
            ebitda_margin=margin,
            tax_rate=tax_rate,
            capex_pct=capex_pct,
            nwc_change=nwc_change,
            depreciation_pct=depreciation_pct
        )

        pv_fcff = fcff / ((1 + wacc) ** year)
        pv_fcff_sum += pv_fcff
        terminal_fcff = fcff

    # Terminal value
    if wacc > terminal_growth:
        terminal_value = terminal_fcff * (1 + terminal_growth) / (wacc - terminal_growth)
        pv_terminal = terminal_value / ((1 + wacc) ** years)
    else:
        pv_terminal = 0

    enterprise_value = pv_fcff_sum + pv_terminal
    return enterprise_value, terminal_fcff


def solve_implied_growth(
    inputs: ReverseDCFInputs,
    tolerance: float = 0.001,
    max_iterations: int = 100
) -> ReverseDCFOutput:
    """
    Solve for implied revenue growth rate using binary search.

    This function iteratively finds the growth rate that, when used
    in a standard DCF model, produces an enterprise value equal to
    the market-implied enterprise value.

    Args:
        inputs: ReverseDCFInputs with market data and assumptions
        tolerance: Convergence tolerance (as % of target EV)
        max_iterations: Maximum iterations before giving up

    Returns:
        ReverseDCFOutput with implied growth and metrics
    """
    target_ev = calculate_implied_ev(
        inputs.current_price,
        inputs.shares_outstanding,
        inputs.net_debt
    )

    # Binary search bounds
    low_growth = -0.20  # -20% annual decline
    high_growth = 0.50  # 50% annual growth

    iterations = 0
    implied_growth = 0
    terminal_fcff = 0

    while iterations < max_iterations:
        iterations += 1
        mid_growth = (low_growth + high_growth) / 2

        ev, terminal_fcff = project_dcf_value(
            current_revenue=inputs.current_revenue,
            growth_rate=mid_growth,
            margin=inputs.base_margin,
            years=inputs.years,
            wacc=inputs.wacc,
            terminal_growth=inputs.terminal_growth,
            tax_rate=inputs.tax_rate,
            capex_pct=inputs.capex_pct,
            nwc_pct=inputs.nwc_pct,
            depreciation_pct=inputs.depreciation_pct
        )

        error_pct = abs(ev - target_ev) / target_ev

        if error_pct < tolerance:
            implied_growth = mid_growth
            break

        if ev < target_ev:
            low_growth = mid_growth
        else:
            high_growth = mid_growth

        implied_growth = mid_growth

    # Calculate terminal revenue
    terminal_revenue = inputs.current_revenue * ((1 + implied_growth) ** inputs.years)

    return ReverseDCFOutput(
        implied_revenue_growth=implied_growth,
        implied_terminal_revenue=terminal_revenue,
        implied_terminal_margin=inputs.base_margin,
        implied_fcff_terminal=terminal_fcff,
        market_implied_ev=target_ev,
        iterations=iterations
    )


def solve_implied_margin(
    inputs: ReverseDCFInputs,
    assumed_growth: float,
    tolerance: float = 0.001,
    max_iterations: int = 100
) -> float:
    """
    Solve for implied terminal margin given a fixed growth rate.

    Args:
        inputs: ReverseDCFInputs with market data
        assumed_growth: Assumed revenue growth rate
        tolerance: Convergence tolerance
        max_iterations: Maximum iterations

    Returns:
        Implied EBITDA margin
    """
    target_ev = calculate_implied_ev(
        inputs.current_price,
        inputs.shares_outstanding,
        inputs.net_debt
    )

    low_margin = 0.01
    high_margin = 0.60

    for _ in range(max_iterations):
        mid_margin = (low_margin + high_margin) / 2

        ev, _ = project_dcf_value(
            current_revenue=inputs.current_revenue,
            growth_rate=assumed_growth,
            margin=mid_margin,
            years=inputs.years,
            wacc=inputs.wacc,
            terminal_growth=inputs.terminal_growth,
            tax_rate=inputs.tax_rate,
            capex_pct=inputs.capex_pct,
            nwc_pct=inputs.nwc_pct,
            depreciation_pct=inputs.depreciation_pct
        )

        error_pct = abs(ev - target_ev) / target_ev

        if error_pct < tolerance:
            return mid_margin

        if ev < target_ev:
            low_margin = mid_margin
        else:
            high_margin = mid_margin

    return (low_margin + high_margin) / 2


def compare_to_estimates(
    implied_growth: float,
    implied_margin: float,
    analyst_growth: float,
    analyst_margin: float
) -> Dict[str, any]:
    """
    Compare implied expectations to analyst estimates.

    Args:
        implied_growth: Market-implied growth rate
        implied_margin: Market-implied margin
        analyst_growth: Analyst consensus growth estimate
        analyst_margin: Analyst margin estimate

    Returns:
        Dictionary with comparison metrics
    """
    growth_gap = implied_growth - analyst_growth
    margin_gap = implied_margin - analyst_margin

    # Determine if market is more optimistic or pessimistic
    if growth_gap > 0.02:
        growth_view = "Market expects HIGHER growth than analysts"
    elif growth_gap < -0.02:
        growth_view = "Market expects LOWER growth than analysts"
    else:
        growth_view = "Market roughly aligned with analyst growth estimates"

    if margin_gap > 0.02:
        margin_view = "Market expects HIGHER margins than analysts"
    elif margin_gap < -0.02:
        margin_view = "Market expects LOWER margins than analysts"
    else:
        margin_view = "Market roughly aligned with analyst margin estimates"

    return {
        'implied_growth': implied_growth,
        'analyst_growth': analyst_growth,
        'growth_gap': growth_gap,
        'growth_interpretation': growth_view,
        'implied_margin': implied_margin,
        'analyst_margin': analyst_margin,
        'margin_gap': margin_gap,
        'margin_interpretation': margin_view
    }


def format_reverse_dcf_report(
    output: ReverseDCFOutput,
    inputs: ReverseDCFInputs,
    comparison: Optional[Dict] = None
) -> str:
    """
    Format reverse DCF results as a readable report.

    Args:
        output: ReverseDCFOutput results
        inputs: Original inputs
        comparison: Optional comparison dict from compare_to_estimates

    Returns:
        Formatted string report
    """
    lines = []
    lines.append("=" * 60)
    lines.append("REVERSE DCF ANALYSIS")
    lines.append("=" * 60)

    lines.append("\nMARKET DATA:")
    lines.append(f"  Current Price: ${inputs.current_price:.2f}")
    lines.append(f"  Shares Outstanding: {inputs.shares_outstanding:.1f}M")
    lines.append(f"  Market Cap: ${inputs.current_price * inputs.shares_outstanding:,.0f}M")
    lines.append(f"  Net Debt: ${inputs.net_debt:,.0f}M")
    lines.append(f"  Market-Implied EV: ${output.market_implied_ev:,.0f}M")

    lines.append("\nASSUMPTIONS:")
    lines.append(f"  WACC: {inputs.wacc:.1%}")
    lines.append(f"  Terminal Growth: {inputs.terminal_growth:.1%}")
    lines.append(f"  Projection Years: {inputs.years}")
    lines.append(f"  Base EBITDA Margin: {inputs.base_margin:.1%}")

    lines.append("\nIMPLIED EXPECTATIONS:")
    lines.append(f"  Implied Revenue Growth: {output.implied_revenue_growth:.1%} per year")
    lines.append(f"  Current Revenue: ${inputs.current_revenue:,.0f}M")
    lines.append(f"  Implied Terminal Revenue: ${output.implied_terminal_revenue:,.0f}M")
    lines.append(f"  Revenue Multiple: {output.implied_terminal_revenue / inputs.current_revenue:.1f}x")

    if comparison:
        lines.append("\nCOMPARISON TO ESTIMATES:")
        lines.append(f"  Analyst Growth Estimate: {comparison['analyst_growth']:.1%}")
        lines.append(f"  Growth Gap: {comparison['growth_gap']:+.1%}")
        lines.append(f"  --> {comparison['growth_interpretation']}")
        lines.append(f"  Analyst Margin Estimate: {comparison['analyst_margin']:.1%}")
        lines.append(f"  Margin Gap: {comparison['margin_gap']:+.1%}")
        lines.append(f"  --> {comparison['margin_interpretation']}")

    lines.append("\n" + "=" * 60)
    return "\n".join(lines)


if __name__ == "__main__":
    # Example: Analyze a growth stock's implied expectations
    print("=" * 70)
    print("REVERSE DCF ANALYSIS - EXAMPLE")
    print("=" * 70)

    # Example company trading at $150/share
    inputs = ReverseDCFInputs(
        current_price=150.00,
        shares_outstanding=500,      # 500M shares
        net_debt=-2000,              # $2B net cash (negative debt)
        wacc=0.10,                   # 10% WACC
        terminal_growth=0.03,        # 3% perpetual growth
        base_margin=0.30,            # 30% EBITDA margin
        current_revenue=30000,       # $30B current revenue
        years=10,                    # 10-year DCF
        tax_rate=0.21,
        capex_pct=0.04,
        nwc_pct=0.08
    )

    # Solve for implied growth
    print("\n1. SOLVING FOR IMPLIED GROWTH RATE")
    print("-" * 40)
    result = solve_implied_growth(inputs)

    print(f"\nMarket-Implied Enterprise Value: ${result.market_implied_ev:,.0f}M")
    print(f"Implied Annual Revenue Growth: {result.implied_revenue_growth:.1%}")
    print(f"Terminal Revenue (Year {inputs.years}): ${result.implied_terminal_revenue:,.0f}M")
    print(f"Iterations to converge: {result.iterations}")

    # Now solve for implied margin at different growth assumptions
    print("\n" + "=" * 70)
    print("2. IMPLIED MARGIN AT DIFFERENT GROWTH RATES")
    print("-" * 40)

    growth_scenarios = [0.05, 0.10, 0.15, 0.20]
    for growth in growth_scenarios:
        implied_margin = solve_implied_margin(inputs, assumed_growth=growth)
        print(f"  At {growth:.0%} growth --> Implied margin: {implied_margin:.1%}")

    # Compare to analyst estimates
    print("\n" + "=" * 70)
    print("3. COMPARISON TO ANALYST ESTIMATES")
    print("-" * 40)

    # Hypothetical analyst estimates
    analyst_growth = 0.12  # 12% consensus growth
    analyst_margin = 0.32  # 32% margin target

    comparison = compare_to_estimates(
        implied_growth=result.implied_revenue_growth,
        implied_margin=inputs.base_margin,
        analyst_growth=analyst_growth,
        analyst_margin=analyst_margin
    )

    print(f"\nImplied Growth: {comparison['implied_growth']:.1%}")
    print(f"Analyst Growth: {comparison['analyst_growth']:.1%}")
    print(f"Gap: {comparison['growth_gap']:+.1%}")
    print(f"--> {comparison['growth_interpretation']}")

    # Full formatted report
    print("\n" + "=" * 70)
    print("4. FULL REPORT")
    print("-" * 40)
    print(format_reverse_dcf_report(result, inputs, comparison))
