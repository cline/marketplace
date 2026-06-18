#!/usr/bin/env python3
"""
Discounted Cash Flow (DCF) Valuation Model

This module provides a comprehensive DCF valuation framework with support for:
- Multi-year free cash flow to firm (FCFF) projections
- Gordon Growth terminal value calculation
- Three-scenario analysis (bull/base/bear cases)
- Sensitivity analysis (terminal growth vs WACC)

Author: Equity Analyst Skill
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass


@dataclass
class DCFInputs:
    """Input parameters for DCF valuation."""
    revenue_projections: List[float]  # Projected revenues for each year
    ebitda_margins: List[float]       # EBITDA margin for each year (as decimals, e.g., 0.20)
    tax_rate: float                    # Corporate tax rate (as decimal)
    capex_pct: float                   # CapEx as % of revenue (as decimal)
    nwc_pct: float                     # Net working capital as % of revenue (as decimal)
    wacc: float                        # Weighted average cost of capital (as decimal)
    terminal_growth: float             # Perpetual growth rate (as decimal)
    shares_outstanding: float          # Number of shares outstanding (in millions)
    net_debt: float                    # Net debt (debt minus cash)
    depreciation_pct: float = 0.03    # D&A as % of revenue (as decimal)


@dataclass
class DCFOutput:
    """Output results from DCF valuation."""
    fcff_by_year: List[float]         # Free cash flow to firm for each projected year
    terminal_value: float              # Terminal value (undiscounted)
    pv_fcff: List[float]              # Present value of each year's FCFF
    pv_terminal_value: float          # Present value of terminal value
    enterprise_value: float           # Total enterprise value
    equity_value: float               # Equity value (EV minus net debt)
    equity_value_per_share: float     # Per share intrinsic value


def calculate_fcff(
    revenue: float,
    ebitda_margin: float,
    tax_rate: float,
    capex_pct: float,
    nwc_change: float,
    depreciation_pct: float
) -> float:
    """
    Calculate Free Cash Flow to Firm (FCFF) for a single period.

    FCFF = EBIT * (1 - Tax Rate) + D&A - CapEx - Change in NWC

    Args:
        revenue: Revenue for the period
        ebitda_margin: EBITDA margin as decimal
        tax_rate: Tax rate as decimal
        capex_pct: CapEx as percentage of revenue
        nwc_change: Change in net working capital
        depreciation_pct: Depreciation as percentage of revenue

    Returns:
        Free cash flow to firm for the period
    """
    ebitda = revenue * ebitda_margin
    depreciation = revenue * depreciation_pct
    ebit = ebitda - depreciation
    nopat = ebit * (1 - tax_rate)
    capex = revenue * capex_pct
    fcff = nopat + depreciation - capex - nwc_change
    return fcff


def calculate_terminal_value(
    final_fcff: float,
    terminal_growth: float,
    wacc: float
) -> float:
    """
    Calculate terminal value using Gordon Growth Model.

    TV = FCFF * (1 + g) / (WACC - g)

    Args:
        final_fcff: Free cash flow in final projection year
        terminal_growth: Perpetual growth rate
        wacc: Weighted average cost of capital

    Returns:
        Terminal value (undiscounted)

    Raises:
        ValueError: If WACC <= terminal growth rate
    """
    if wacc <= terminal_growth:
        raise ValueError(
            f"WACC ({wacc:.2%}) must be greater than terminal growth rate ({terminal_growth:.2%})"
        )
    return final_fcff * (1 + terminal_growth) / (wacc - terminal_growth)


def discount_to_present(
    cash_flows: List[float],
    discount_rate: float,
    terminal_value: Optional[float] = None
) -> Tuple[List[float], Optional[float]]:
    """
    Discount cash flows to present value.

    Args:
        cash_flows: List of future cash flows
        discount_rate: Discount rate (WACC)
        terminal_value: Optional terminal value to discount

    Returns:
        Tuple of (discounted cash flows, discounted terminal value)
    """
    pv_cash_flows = []
    for year, cf in enumerate(cash_flows, start=1):
        pv = cf / ((1 + discount_rate) ** year)
        pv_cash_flows.append(pv)

    pv_terminal = None
    if terminal_value is not None:
        final_year = len(cash_flows)
        pv_terminal = terminal_value / ((1 + discount_rate) ** final_year)

    return pv_cash_flows, pv_terminal


def run_dcf_valuation(inputs: DCFInputs) -> DCFOutput:
    """
    Execute a complete DCF valuation.

    Args:
        inputs: DCFInputs dataclass with all required parameters

    Returns:
        DCFOutput dataclass with valuation results
    """
    # Calculate FCFF for each projected year
    fcff_by_year = []
    prev_nwc = 0

    for i, revenue in enumerate(inputs.revenue_projections):
        current_nwc = revenue * inputs.nwc_pct
        nwc_change = current_nwc - prev_nwc
        prev_nwc = current_nwc

        fcff = calculate_fcff(
            revenue=revenue,
            ebitda_margin=inputs.ebitda_margins[i],
            tax_rate=inputs.tax_rate,
            capex_pct=inputs.capex_pct,
            nwc_change=nwc_change,
            depreciation_pct=inputs.depreciation_pct
        )
        fcff_by_year.append(fcff)

    # Calculate terminal value
    terminal_value = calculate_terminal_value(
        final_fcff=fcff_by_year[-1],
        terminal_growth=inputs.terminal_growth,
        wacc=inputs.wacc
    )

    # Discount to present value
    pv_fcff, pv_terminal_value = discount_to_present(
        cash_flows=fcff_by_year,
        discount_rate=inputs.wacc,
        terminal_value=terminal_value
    )

    # Calculate enterprise and equity value
    enterprise_value = sum(pv_fcff) + pv_terminal_value
    equity_value = enterprise_value - inputs.net_debt
    equity_value_per_share = equity_value / inputs.shares_outstanding

    return DCFOutput(
        fcff_by_year=fcff_by_year,
        terminal_value=terminal_value,
        pv_fcff=pv_fcff,
        pv_terminal_value=pv_terminal_value,
        enterprise_value=enterprise_value,
        equity_value=equity_value,
        equity_value_per_share=equity_value_per_share
    )


def run_scenario_analysis(
    base_inputs: DCFInputs,
    bull_adjustments: Dict[str, float],
    bear_adjustments: Dict[str, float]
) -> Dict[str, DCFOutput]:
    """
    Run three-scenario DCF analysis (bull/base/bear cases).

    Args:
        base_inputs: Base case DCF inputs
        bull_adjustments: Dict of adjustments for bull case
            Supported keys: 'revenue_growth', 'margin_add', 'wacc_subtract', 'terminal_growth_add'
        bear_adjustments: Dict of adjustments for bear case
            Same supported keys as bull_adjustments

    Returns:
        Dict with 'bull', 'base', 'bear' keys mapping to DCFOutput objects
    """
    results = {}

    # Base case
    results['base'] = run_dcf_valuation(base_inputs)

    # Bull case
    bull_inputs = DCFInputs(
        revenue_projections=[
            r * (1 + bull_adjustments.get('revenue_growth', 0))
            for r in base_inputs.revenue_projections
        ],
        ebitda_margins=[
            m + bull_adjustments.get('margin_add', 0)
            for m in base_inputs.ebitda_margins
        ],
        tax_rate=base_inputs.tax_rate,
        capex_pct=base_inputs.capex_pct,
        nwc_pct=base_inputs.nwc_pct,
        wacc=base_inputs.wacc - bull_adjustments.get('wacc_subtract', 0),
        terminal_growth=base_inputs.terminal_growth + bull_adjustments.get('terminal_growth_add', 0),
        shares_outstanding=base_inputs.shares_outstanding,
        net_debt=base_inputs.net_debt,
        depreciation_pct=base_inputs.depreciation_pct
    )
    results['bull'] = run_dcf_valuation(bull_inputs)

    # Bear case
    bear_inputs = DCFInputs(
        revenue_projections=[
            r * (1 - bear_adjustments.get('revenue_decline', 0))
            for r in base_inputs.revenue_projections
        ],
        ebitda_margins=[
            m - bear_adjustments.get('margin_subtract', 0)
            for m in base_inputs.ebitda_margins
        ],
        tax_rate=base_inputs.tax_rate,
        capex_pct=base_inputs.capex_pct,
        nwc_pct=base_inputs.nwc_pct,
        wacc=base_inputs.wacc + bear_adjustments.get('wacc_add', 0),
        terminal_growth=base_inputs.terminal_growth - bear_adjustments.get('terminal_growth_subtract', 0),
        shares_outstanding=base_inputs.shares_outstanding,
        net_debt=base_inputs.net_debt,
        depreciation_pct=base_inputs.depreciation_pct
    )
    results['bear'] = run_dcf_valuation(bear_inputs)

    return results


def generate_sensitivity_table(
    base_inputs: DCFInputs,
    growth_range: List[float],
    wacc_range: List[float]
) -> List[List[float]]:
    """
    Generate sensitivity table showing equity value per share
    for different combinations of terminal growth and WACC.

    Args:
        base_inputs: Base case DCF inputs
        growth_range: List of terminal growth rates to test
        wacc_range: List of WACC values to test

    Returns:
        2D list where rows are growth rates and columns are WACC values
        First row contains WACC headers, first column contains growth headers
    """
    table = []

    # Header row with WACC values
    header = ['Growth \\ WACC'] + [f"{w:.1%}" for w in wacc_range]
    table.append(header)

    for growth in growth_range:
        row = [f"{growth:.1%}"]
        for wacc in wacc_range:
            try:
                test_inputs = DCFInputs(
                    revenue_projections=base_inputs.revenue_projections,
                    ebitda_margins=base_inputs.ebitda_margins,
                    tax_rate=base_inputs.tax_rate,
                    capex_pct=base_inputs.capex_pct,
                    nwc_pct=base_inputs.nwc_pct,
                    wacc=wacc,
                    terminal_growth=growth,
                    shares_outstanding=base_inputs.shares_outstanding,
                    net_debt=base_inputs.net_debt,
                    depreciation_pct=base_inputs.depreciation_pct
                )
                result = run_dcf_valuation(test_inputs)
                row.append(f"${result.equity_value_per_share:.2f}")
            except ValueError:
                row.append("N/A")
        table.append(row)

    return table


def format_sensitivity_table(table: List[List[str]]) -> str:
    """Format sensitivity table for display."""
    if not table:
        return ""

    # Calculate column widths
    col_widths = []
    for col_idx in range(len(table[0])):
        max_width = max(len(str(row[col_idx])) for row in table)
        col_widths.append(max_width + 2)

    # Build formatted output
    lines = []
    for row_idx, row in enumerate(table):
        formatted_row = ""
        for col_idx, cell in enumerate(row):
            formatted_row += str(cell).center(col_widths[col_idx])
        lines.append(formatted_row)
        if row_idx == 0:
            lines.append("-" * sum(col_widths))

    return "\n".join(lines)


if __name__ == "__main__":
    # Example: Tech company DCF valuation
    print("=" * 70)
    print("DCF VALUATION MODEL - EXAMPLE")
    print("=" * 70)

    # Define base case inputs (values in millions USD)
    base_inputs = DCFInputs(
        revenue_projections=[1000, 1150, 1322, 1520, 1748],  # 5-year projections
        ebitda_margins=[0.25, 0.26, 0.27, 0.28, 0.28],       # Margin expansion
        tax_rate=0.21,
        capex_pct=0.05,
        nwc_pct=0.10,
        wacc=0.10,
        terminal_growth=0.03,
        shares_outstanding=100,  # 100 million shares
        net_debt=200,            # $200M net debt
        depreciation_pct=0.03
    )

    # Run base case valuation
    print("\n1. BASE CASE VALUATION")
    print("-" * 40)
    result = run_dcf_valuation(base_inputs)

    print("\nProjected FCFF by Year:")
    for i, fcff in enumerate(result.fcff_by_year, 1):
        print(f"  Year {i}: ${fcff:,.0f}M")

    print(f"\nTerminal Value: ${result.terminal_value:,.0f}M")
    print(f"PV of Terminal Value: ${result.pv_terminal_value:,.0f}M")
    print(f"\nEnterprise Value: ${result.enterprise_value:,.0f}M")
    print(f"Less: Net Debt: ${base_inputs.net_debt:,.0f}M")
    print(f"Equity Value: ${result.equity_value:,.0f}M")
    print(f"\nEquity Value Per Share: ${result.equity_value_per_share:.2f}")

    # Run scenario analysis
    print("\n" + "=" * 70)
    print("2. SCENARIO ANALYSIS")
    print("-" * 40)

    bull_adj = {
        'revenue_growth': 0.10,      # 10% higher revenues
        'margin_add': 0.02,          # 2% higher margins
        'wacc_subtract': 0.01,       # 1% lower WACC
        'terminal_growth_add': 0.005 # 0.5% higher terminal growth
    }

    bear_adj = {
        'revenue_decline': 0.10,       # 10% lower revenues
        'margin_subtract': 0.03,       # 3% lower margins
        'wacc_add': 0.02,              # 2% higher WACC
        'terminal_growth_subtract': 0.01  # 1% lower terminal growth
    }

    scenarios = run_scenario_analysis(base_inputs, bull_adj, bear_adj)

    print("\nScenario Results (Equity Value Per Share):")
    print(f"  Bull Case:  ${scenarios['bull'].equity_value_per_share:.2f}")
    print(f"  Base Case:  ${scenarios['base'].equity_value_per_share:.2f}")
    print(f"  Bear Case:  ${scenarios['bear'].equity_value_per_share:.2f}")

    # Generate sensitivity table
    print("\n" + "=" * 70)
    print("3. SENSITIVITY ANALYSIS")
    print("-" * 40)
    print("\nEquity Value Per Share by Terminal Growth vs WACC:")

    growth_range = [0.01, 0.02, 0.03, 0.04, 0.05]
    wacc_range = [0.08, 0.09, 0.10, 0.11, 0.12]

    sensitivity = generate_sensitivity_table(base_inputs, growth_range, wacc_range)
    print(format_sensitivity_table(sensitivity))

    print("\n" + "=" * 70)
