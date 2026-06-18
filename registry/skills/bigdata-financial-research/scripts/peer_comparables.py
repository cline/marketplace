#!/usr/bin/env python3
"""
Peer Comparables Analysis

This module builds comprehensive comparable company analysis tables including:
- EV/EBITDA, EV/Revenue, and P/E multiples for each peer
- Statistical analysis (mean, median, percentiles)
- Percentile ranking for the target company
- Implied valuation range based on peer multiples

Author: Equity Analyst Skill
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
import statistics


@dataclass
class PeerData:
    """Financial data for a single peer company."""
    name: str
    ticker: str
    enterprise_value: float    # Enterprise value
    market_cap: float          # Market capitalization
    ebitda: float              # Trailing EBITDA
    revenue: float             # Trailing revenue
    net_income: float          # Trailing net income
    shares_outstanding: float  # Shares outstanding
    growth_rate: Optional[float] = None  # Revenue growth rate (optional)


@dataclass
class TargetMetrics:
    """Financial metrics for the target company."""
    name: str
    ticker: str
    enterprise_value: float
    market_cap: float
    ebitda: float
    revenue: float
    net_income: float
    shares_outstanding: float
    current_price: float
    growth_rate: Optional[float] = None


@dataclass
class ComparableOutput:
    """Output from comparable analysis."""
    peer_table: List[Dict]         # List of peer data with calculated multiples
    target_multiples: Dict         # Target company's multiples
    percentile_rankings: Dict      # Target's percentile ranking for each metric
    implied_valuations: Dict       # Implied valuations based on peer multiples
    summary_stats: Dict            # Summary statistics for peer group


def calculate_multiples(
    ev: float,
    market_cap: float,
    ebitda: float,
    revenue: float,
    net_income: float,
    shares: float
) -> Dict[str, Optional[float]]:
    """
    Calculate valuation multiples for a company.

    Args:
        ev: Enterprise value
        market_cap: Market capitalization
        ebitda: EBITDA
        revenue: Revenue
        net_income: Net income
        shares: Shares outstanding

    Returns:
        Dictionary with calculated multiples
    """
    # EV/EBITDA
    ev_ebitda = ev / ebitda if ebitda > 0 else None

    # EV/Revenue
    ev_revenue = ev / revenue if revenue > 0 else None

    # P/E (using market cap / net income, or price / EPS)
    pe_ratio = market_cap / net_income if net_income > 0 else None

    # Price per share (if shares provided)
    price = market_cap / shares if shares > 0 else None

    # EPS
    eps = net_income / shares if shares > 0 else None

    return {
        'ev_ebitda': ev_ebitda,
        'ev_revenue': ev_revenue,
        'pe_ratio': pe_ratio,
        'price': price,
        'eps': eps
    }


def calculate_percentile(value: float, distribution: List[float]) -> float:
    """
    Calculate the percentile ranking of a value within a distribution.

    Args:
        value: The value to rank
        distribution: List of values to compare against

    Returns:
        Percentile ranking (0-100)
    """
    if not distribution:
        return 50.0

    sorted_dist = sorted(distribution)
    below = sum(1 for v in sorted_dist if v < value)
    equal = sum(1 for v in sorted_dist if v == value)

    percentile = (below + 0.5 * equal) / len(sorted_dist) * 100
    return percentile


def calculate_summary_stats(values: List[float]) -> Dict[str, float]:
    """
    Calculate summary statistics for a list of values.

    Args:
        values: List of numeric values

    Returns:
        Dictionary with mean, median, min, max, 25th/75th percentiles
    """
    if not values:
        return {
            'mean': 0,
            'median': 0,
            'min': 0,
            'max': 0,
            'p25': 0,
            'p75': 0,
            'count': 0
        }

    sorted_values = sorted(values)
    n = len(sorted_values)

    # Calculate percentiles
    p25_idx = int(n * 0.25)
    p75_idx = int(n * 0.75)

    return {
        'mean': statistics.mean(values),
        'median': statistics.median(values),
        'min': min(values),
        'max': max(values),
        'p25': sorted_values[p25_idx] if n > 0 else 0,
        'p75': sorted_values[min(p75_idx, n-1)] if n > 0 else 0,
        'count': n
    }


def build_comp_table(
    target: TargetMetrics,
    peers: List[PeerData]
) -> ComparableOutput:
    """
    Build a comprehensive comparable company analysis.

    Args:
        target: Target company metrics
        peers: List of peer company data

    Returns:
        ComparableOutput with full analysis
    """
    # Calculate multiples for all peers
    peer_table = []
    ev_ebitda_values = []
    ev_revenue_values = []
    pe_values = []

    for peer in peers:
        multiples = calculate_multiples(
            ev=peer.enterprise_value,
            market_cap=peer.market_cap,
            ebitda=peer.ebitda,
            revenue=peer.revenue,
            net_income=peer.net_income,
            shares=peer.shares_outstanding
        )

        peer_entry = {
            'name': peer.name,
            'ticker': peer.ticker,
            'ev': peer.enterprise_value,
            'market_cap': peer.market_cap,
            'ebitda': peer.ebitda,
            'revenue': peer.revenue,
            'net_income': peer.net_income,
            'ev_ebitda': multiples['ev_ebitda'],
            'ev_revenue': multiples['ev_revenue'],
            'pe_ratio': multiples['pe_ratio'],
            'growth_rate': peer.growth_rate
        }
        peer_table.append(peer_entry)

        # Collect valid multiples for statistics
        if multiples['ev_ebitda'] is not None:
            ev_ebitda_values.append(multiples['ev_ebitda'])
        if multiples['ev_revenue'] is not None:
            ev_revenue_values.append(multiples['ev_revenue'])
        if multiples['pe_ratio'] is not None:
            pe_values.append(multiples['pe_ratio'])

    # Calculate target multiples
    target_multiples = calculate_multiples(
        ev=target.enterprise_value,
        market_cap=target.market_cap,
        ebitda=target.ebitda,
        revenue=target.revenue,
        net_income=target.net_income,
        shares=target.shares_outstanding
    )
    target_multiples['name'] = target.name
    target_multiples['ticker'] = target.ticker
    target_multiples['current_price'] = target.current_price

    # Calculate percentile rankings for target
    percentile_rankings = {}
    if target_multiples['ev_ebitda'] is not None and ev_ebitda_values:
        percentile_rankings['ev_ebitda'] = calculate_percentile(
            target_multiples['ev_ebitda'], ev_ebitda_values
        )
    if target_multiples['ev_revenue'] is not None and ev_revenue_values:
        percentile_rankings['ev_revenue'] = calculate_percentile(
            target_multiples['ev_revenue'], ev_revenue_values
        )
    if target_multiples['pe_ratio'] is not None and pe_values:
        percentile_rankings['pe_ratio'] = calculate_percentile(
            target_multiples['pe_ratio'], pe_values
        )

    # Calculate summary statistics
    summary_stats = {
        'ev_ebitda': calculate_summary_stats(ev_ebitda_values),
        'ev_revenue': calculate_summary_stats(ev_revenue_values),
        'pe_ratio': calculate_summary_stats(pe_values)
    }

    # Calculate implied valuations for target
    implied_valuations = calculate_implied_valuations(
        target=target,
        summary_stats=summary_stats
    )

    return ComparableOutput(
        peer_table=peer_table,
        target_multiples=target_multiples,
        percentile_rankings=percentile_rankings,
        implied_valuations=implied_valuations,
        summary_stats=summary_stats
    )


def calculate_implied_valuations(
    target: TargetMetrics,
    summary_stats: Dict
) -> Dict:
    """
    Calculate implied valuations for target based on peer multiples.

    Args:
        target: Target company metrics
        summary_stats: Peer group summary statistics

    Returns:
        Dictionary with implied valuations
    """
    implied = {}

    # EV/EBITDA implied valuation
    if summary_stats['ev_ebitda']['count'] > 0 and target.ebitda > 0:
        ev_ebitda_stats = summary_stats['ev_ebitda']
        implied_ev_low = target.ebitda * ev_ebitda_stats['p25']
        implied_ev_median = target.ebitda * ev_ebitda_stats['median']
        implied_ev_high = target.ebitda * ev_ebitda_stats['p75']

        # Convert to equity value (EV - Net Debt = Equity)
        net_debt = target.enterprise_value - target.market_cap

        implied['ev_ebitda'] = {
            'low': (implied_ev_low - net_debt) / target.shares_outstanding,
            'median': (implied_ev_median - net_debt) / target.shares_outstanding,
            'high': (implied_ev_high - net_debt) / target.shares_outstanding,
            'multiple_low': ev_ebitda_stats['p25'],
            'multiple_median': ev_ebitda_stats['median'],
            'multiple_high': ev_ebitda_stats['p75']
        }

    # EV/Revenue implied valuation
    if summary_stats['ev_revenue']['count'] > 0 and target.revenue > 0:
        ev_rev_stats = summary_stats['ev_revenue']
        implied_ev_low = target.revenue * ev_rev_stats['p25']
        implied_ev_median = target.revenue * ev_rev_stats['median']
        implied_ev_high = target.revenue * ev_rev_stats['p75']

        net_debt = target.enterprise_value - target.market_cap

        implied['ev_revenue'] = {
            'low': (implied_ev_low - net_debt) / target.shares_outstanding,
            'median': (implied_ev_median - net_debt) / target.shares_outstanding,
            'high': (implied_ev_high - net_debt) / target.shares_outstanding,
            'multiple_low': ev_rev_stats['p25'],
            'multiple_median': ev_rev_stats['median'],
            'multiple_high': ev_rev_stats['p75']
        }

    # P/E implied valuation
    if summary_stats['pe_ratio']['count'] > 0 and target.net_income > 0:
        pe_stats = summary_stats['pe_ratio']
        eps = target.net_income / target.shares_outstanding

        implied['pe_ratio'] = {
            'low': eps * pe_stats['p25'],
            'median': eps * pe_stats['median'],
            'high': eps * pe_stats['p75'],
            'multiple_low': pe_stats['p25'],
            'multiple_median': pe_stats['median'],
            'multiple_high': pe_stats['p75']
        }

    return implied


def format_comp_table(output: ComparableOutput) -> str:
    """
    Format the comparable analysis as a readable table.

    Args:
        output: ComparableOutput from build_comp_table

    Returns:
        Formatted string table
    """
    lines = []

    # Header
    lines.append("=" * 100)
    lines.append("COMPARABLE COMPANY ANALYSIS")
    lines.append("=" * 100)

    # Peer table
    lines.append("\n1. PEER MULTIPLES")
    lines.append("-" * 100)

    # Table header
    header = f"{'Company':<20} {'Ticker':<8} {'EV ($M)':<12} {'EV/EBITDA':<12} {'EV/Revenue':<12} {'P/E':<10}"
    lines.append(header)
    lines.append("-" * 100)

    # Peer rows
    for peer in output.peer_table:
        ev_ebitda_str = f"{peer['ev_ebitda']:.1f}x" if peer['ev_ebitda'] else "N/A"
        ev_rev_str = f"{peer['ev_revenue']:.2f}x" if peer['ev_revenue'] else "N/A"
        pe_str = f"{peer['pe_ratio']:.1f}x" if peer['pe_ratio'] else "N/A"

        row = f"{peer['name']:<20} {peer['ticker']:<8} {peer['ev']:>10,.0f} {ev_ebitda_str:>12} {ev_rev_str:>12} {pe_str:>10}"
        lines.append(row)

    lines.append("-" * 100)

    # Summary statistics
    lines.append("\n2. PEER GROUP STATISTICS")
    lines.append("-" * 60)

    for metric, label in [('ev_ebitda', 'EV/EBITDA'), ('ev_revenue', 'EV/Revenue'), ('pe_ratio', 'P/E')]:
        stats = output.summary_stats[metric]
        if stats['count'] > 0:
            lines.append(f"\n{label}:")
            lines.append(f"  Mean:   {stats['mean']:.2f}x    Median: {stats['median']:.2f}x")
            lines.append(f"  Min:    {stats['min']:.2f}x    Max:    {stats['max']:.2f}x")
            lines.append(f"  25th %: {stats['p25']:.2f}x    75th %: {stats['p75']:.2f}x")

    # Target analysis
    lines.append("\n" + "=" * 100)
    lines.append("3. TARGET COMPANY ANALYSIS")
    lines.append("-" * 60)

    tm = output.target_multiples
    lines.append(f"\n{tm['name']} ({tm['ticker']})")
    lines.append(f"Current Price: ${tm['current_price']:.2f}")
    lines.append(f"\nTarget Multiples:")

    if tm['ev_ebitda']:
        pct = output.percentile_rankings.get('ev_ebitda', 'N/A')
        pct_str = f"{pct:.0f}th" if isinstance(pct, float) else pct
        lines.append(f"  EV/EBITDA:  {tm['ev_ebitda']:.1f}x  (Percentile: {pct_str})")

    if tm['ev_revenue']:
        pct = output.percentile_rankings.get('ev_revenue', 'N/A')
        pct_str = f"{pct:.0f}th" if isinstance(pct, float) else pct
        lines.append(f"  EV/Revenue: {tm['ev_revenue']:.2f}x  (Percentile: {pct_str})")

    if tm['pe_ratio']:
        pct = output.percentile_rankings.get('pe_ratio', 'N/A')
        pct_str = f"{pct:.0f}th" if isinstance(pct, float) else pct
        lines.append(f"  P/E Ratio:  {tm['pe_ratio']:.1f}x  (Percentile: {pct_str})")

    # Implied valuations
    lines.append("\n4. IMPLIED VALUATION RANGE")
    lines.append("-" * 60)

    for method, label in [('ev_ebitda', 'EV/EBITDA'), ('ev_revenue', 'EV/Revenue'), ('pe_ratio', 'P/E')]:
        if method in output.implied_valuations:
            iv = output.implied_valuations[method]
            lines.append(f"\nBased on {label}:")
            lines.append(f"  Low (25th %):    ${iv['low']:.2f}  ({iv['multiple_low']:.2f}x)")
            lines.append(f"  Median:          ${iv['median']:.2f}  ({iv['multiple_median']:.2f}x)")
            lines.append(f"  High (75th %):   ${iv['high']:.2f}  ({iv['multiple_high']:.2f}x)")

    # Calculate blended range
    all_lows = []
    all_medians = []
    all_highs = []
    for method in ['ev_ebitda', 'ev_revenue', 'pe_ratio']:
        if method in output.implied_valuations:
            all_lows.append(output.implied_valuations[method]['low'])
            all_medians.append(output.implied_valuations[method]['median'])
            all_highs.append(output.implied_valuations[method]['high'])

    if all_lows:
        lines.append("\n" + "-" * 60)
        lines.append("BLENDED VALUATION RANGE:")
        lines.append(f"  Low:     ${min(all_lows):.2f}")
        lines.append(f"  Median:  ${statistics.median(all_medians):.2f}")
        lines.append(f"  High:    ${max(all_highs):.2f}")
        lines.append(f"\n  Current: ${tm['current_price']:.2f}")

        median_implied = statistics.median(all_medians)
        upside = (median_implied / tm['current_price'] - 1) * 100
        lines.append(f"  Upside to Median: {upside:+.1f}%")

    lines.append("\n" + "=" * 100)
    return "\n".join(lines)


if __name__ == "__main__":
    # Example: SaaS company comparable analysis
    print("=" * 100)
    print("PEER COMPARABLES ANALYSIS - EXAMPLE")
    print("=" * 100)

    # Define target company
    target = TargetMetrics(
        name="Target SaaS Corp",
        ticker="TSAS",
        enterprise_value=5000,      # $5B EV
        market_cap=5500,            # $5.5B market cap (net cash position)
        ebitda=400,                 # $400M EBITDA
        revenue=1200,               # $1.2B revenue
        net_income=250,             # $250M net income
        shares_outstanding=100,     # 100M shares
        current_price=55.00,        # $55 per share
        growth_rate=0.25            # 25% growth
    )

    # Define peer group
    peers = [
        PeerData(
            name="Cloud Leader Inc",
            ticker="CLDI",
            enterprise_value=25000,
            market_cap=28000,
            ebitda=2000,
            revenue=8000,
            net_income=1200,
            shares_outstanding=200,
            growth_rate=0.20
        ),
        PeerData(
            name="Software Giant Co",
            ticker="SFTG",
            enterprise_value=15000,
            market_cap=16000,
            ebitda=1500,
            revenue=5000,
            net_income=900,
            shares_outstanding=150,
            growth_rate=0.15
        ),
        PeerData(
            name="Fast Growth Tech",
            ticker="FGTH",
            enterprise_value=8000,
            market_cap=8500,
            ebitda=500,
            revenue=1800,
            net_income=200,
            shares_outstanding=80,
            growth_rate=0.35
        ),
        PeerData(
            name="Enterprise SaaS Ltd",
            ticker="ESAS",
            enterprise_value=6000,
            market_cap=6200,
            ebitda=550,
            revenue=1500,
            net_income=300,
            shares_outstanding=120,
            growth_rate=0.22
        ),
        PeerData(
            name="Data Platform Corp",
            ticker="DPLT",
            enterprise_value=4500,
            market_cap=4800,
            ebitda=350,
            revenue=1000,
            net_income=180,
            shares_outstanding=90,
            growth_rate=0.28
        ),
        PeerData(
            name="Subscription Software",
            ticker="SUBS",
            enterprise_value=3500,
            market_cap=3700,
            ebitda=300,
            revenue=900,
            net_income=150,
            shares_outstanding=75,
            growth_rate=0.18
        )
    ]

    # Run analysis
    result = build_comp_table(target, peers)

    # Print formatted report
    print(format_comp_table(result))

    # Show raw output
    print("\n" + "=" * 100)
    print("RAW OUTPUT DATA")
    print("-" * 50)

    print("\nTarget Percentile Rankings:")
    for metric, percentile in result.percentile_rankings.items():
        print(f"  {metric}: {percentile:.1f}th percentile")

    print("\nImplied Share Prices:")
    for method, values in result.implied_valuations.items():
        print(f"  {method}:")
        print(f"    Low: ${values['low']:.2f}, Median: ${values['median']:.2f}, High: ${values['high']:.2f}")
