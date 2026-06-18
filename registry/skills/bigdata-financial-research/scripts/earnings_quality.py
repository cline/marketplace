#!/usr/bin/env python3
"""
Earnings Quality Analysis and Beneish M-Score Calculator

This module provides comprehensive earnings quality assessment including:
- Operating cash flow to net income ratio
- Accrual ratio and quality metrics
- Working capital efficiency (DSO, DIO, DPO, Cash Conversion Cycle)
- Beneish M-Score for earnings manipulation detection
- Red flag identification with explanations

The Beneish M-Score uses 8 financial variables to detect potential
earnings manipulation. An M-Score > -1.78 suggests higher probability
of manipulation.

Author: Equity Analyst Skill
"""

from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass
import math


@dataclass
class FinancialData:
    """
    Financial data required for earnings quality analysis.
    All values should be for the same fiscal period unless noted.
    """
    # Income Statement
    net_income: float
    revenue: float
    gross_profit: float
    operating_income: float
    cogs: float                    # Cost of goods sold
    sga_expense: float             # SG&A expenses
    depreciation: float

    # Balance Sheet - Current Period
    total_assets: float
    current_assets: float
    cash: float
    receivables: float
    inventory: float
    ppe_net: float                 # Property, plant & equipment (net)
    current_liabilities: float
    payables: float
    long_term_debt: float
    total_liabilities: float

    # Balance Sheet - Prior Period
    prior_total_assets: float
    prior_receivables: float
    prior_inventory: float
    prior_ppe_gross: float
    prior_current_assets: float
    prior_current_liabilities: float
    prior_long_term_debt: float

    # Cash Flow Statement
    operating_cash_flow: float

    # Prior Period Income Statement
    prior_revenue: float
    prior_gross_profit: float
    prior_sga_expense: float
    prior_depreciation: float


@dataclass
class QualityMetrics:
    """Container for earnings quality metrics."""
    ocf_ni_ratio: float           # Operating CF / Net Income
    accrual_ratio: float          # (NI - OCF) / Avg Total Assets
    days_sales_outstanding: float
    days_inventory_outstanding: float
    days_payable_outstanding: float
    cash_conversion_cycle: float
    quality_score: str            # High/Medium/Low


@dataclass
class MScoreResult:
    """Container for Beneish M-Score results."""
    dsri: float    # Days Sales in Receivables Index
    gmi: float     # Gross Margin Index
    aqi: float     # Asset Quality Index
    sgi: float     # Sales Growth Index
    depi: float    # Depreciation Index
    sgai: float    # SG&A Index
    lvgi: float    # Leverage Index
    tata: float    # Total Accruals to Total Assets
    m_score: float
    manipulation_probability: str


def calculate_ocf_ni_ratio(
    operating_cash_flow: float,
    net_income: float
) -> Tuple[float, str]:
    """
    Calculate Operating Cash Flow to Net Income ratio.

    A healthy company should generate operating cash flow at least
    equal to its reported net income. Consistently low ratios may
    indicate aggressive revenue recognition or expense capitalization.

    Args:
        operating_cash_flow: Cash from operations
        net_income: Reported net income

    Returns:
        Tuple of (ratio, interpretation)
    """
    if net_income == 0:
        return (float('inf') if operating_cash_flow > 0 else 0, "Net income is zero")

    ratio = operating_cash_flow / net_income

    if ratio >= 1.0:
        interpretation = "Healthy: OCF exceeds or equals net income"
    elif ratio >= 0.8:
        interpretation = "Acceptable: OCF slightly below net income"
    elif ratio >= 0.5:
        interpretation = "Caution: Significant gap between OCF and NI"
    else:
        interpretation = "Warning: OCF much lower than net income"

    return ratio, interpretation


def calculate_accrual_ratio(
    net_income: float,
    operating_cash_flow: float,
    total_assets: float,
    prior_total_assets: float
) -> Tuple[float, str]:
    """
    Calculate the accrual ratio.

    Accrual Ratio = (Net Income - Operating Cash Flow) / Average Total Assets

    High accrual ratios indicate earnings are driven more by accounting
    accruals than cash generation, which may be less sustainable.

    Args:
        net_income: Reported net income
        operating_cash_flow: Cash from operations
        total_assets: Current period total assets
        prior_total_assets: Prior period total assets

    Returns:
        Tuple of (ratio, interpretation)
    """
    avg_assets = (total_assets + prior_total_assets) / 2
    if avg_assets == 0:
        return 0, "Cannot calculate: zero assets"

    accruals = net_income - operating_cash_flow
    ratio = accruals / avg_assets

    if ratio < 0:
        interpretation = "Good: Cash earnings exceed accrual earnings"
    elif ratio < 0.05:
        interpretation = "Acceptable: Low accrual component"
    elif ratio < 0.10:
        interpretation = "Caution: Moderate accrual component"
    else:
        interpretation = "Warning: High accrual component in earnings"

    return ratio, interpretation


def calculate_working_capital_metrics(
    receivables: float,
    inventory: float,
    payables: float,
    revenue: float,
    cogs: float
) -> Dict[str, float]:
    """
    Calculate working capital efficiency metrics.

    DSO = (Receivables / Revenue) * 365
    DIO = (Inventory / COGS) * 365
    DPO = (Payables / COGS) * 365
    CCC = DSO + DIO - DPO

    Args:
        receivables: Accounts receivable
        inventory: Inventory balance
        payables: Accounts payable
        revenue: Annual revenue
        cogs: Cost of goods sold

    Returns:
        Dictionary with DSO, DIO, DPO, and CCC
    """
    dso = (receivables / revenue * 365) if revenue > 0 else 0
    dio = (inventory / cogs * 365) if cogs > 0 else 0
    dpo = (payables / cogs * 365) if cogs > 0 else 0
    ccc = dso + dio - dpo

    return {
        'dso': dso,
        'dio': dio,
        'dpo': dpo,
        'ccc': ccc
    }


def calculate_beneish_mscore(data: FinancialData) -> MScoreResult:
    """
    Calculate the Beneish M-Score for earnings manipulation detection.

    The model uses 8 financial ratios to compute a score where:
    - M-Score > -1.78 suggests higher probability of manipulation
    - M-Score < -1.78 suggests lower probability of manipulation

    The 8 variables are:
    1. DSRI - Days Sales in Receivables Index
    2. GMI - Gross Margin Index
    3. AQI - Asset Quality Index
    4. SGI - Sales Growth Index
    5. DEPI - Depreciation Index
    6. SGAI - SG&A Index
    7. LVGI - Leverage Index
    8. TATA - Total Accruals to Total Assets

    Args:
        data: FinancialData with current and prior period data

    Returns:
        MScoreResult with component scores and final M-Score
    """
    # 1. Days Sales in Receivables Index (DSRI)
    # DSRI = (Receivables_t / Sales_t) / (Receivables_t-1 / Sales_t-1)
    dsr_current = data.receivables / data.revenue if data.revenue > 0 else 0
    dsr_prior = data.prior_receivables / data.prior_revenue if data.prior_revenue > 0 else 0
    dsri = dsr_current / dsr_prior if dsr_prior > 0 else 1.0

    # 2. Gross Margin Index (GMI)
    # GMI = Gross_Margin_t-1 / Gross_Margin_t
    gm_current = data.gross_profit / data.revenue if data.revenue > 0 else 0
    gm_prior = data.prior_gross_profit / data.prior_revenue if data.prior_revenue > 0 else 0
    gmi = gm_prior / gm_current if gm_current > 0 else 1.0

    # 3. Asset Quality Index (AQI)
    # AQI = [1 - (CA_t + PPE_t) / TA_t] / [1 - (CA_t-1 + PPE_t-1) / TA_t-1]
    aq_current = 1 - (data.current_assets + data.ppe_net) / data.total_assets if data.total_assets > 0 else 0
    aq_prior = 1 - (data.prior_current_assets + data.prior_ppe_gross) / data.prior_total_assets if data.prior_total_assets > 0 else 0
    aqi = aq_current / aq_prior if aq_prior > 0 else 1.0

    # 4. Sales Growth Index (SGI)
    # SGI = Sales_t / Sales_t-1
    sgi = data.revenue / data.prior_revenue if data.prior_revenue > 0 else 1.0

    # 5. Depreciation Index (DEPI)
    # DEPI = (Dep_t-1 / (Dep_t-1 + PPE_t-1)) / (Dep_t / (Dep_t + PPE_t))
    dep_rate_current = data.depreciation / (data.depreciation + data.ppe_net) if (data.depreciation + data.ppe_net) > 0 else 0
    dep_rate_prior = data.prior_depreciation / (data.prior_depreciation + data.prior_ppe_gross) if (data.prior_depreciation + data.prior_ppe_gross) > 0 else 0
    depi = dep_rate_prior / dep_rate_current if dep_rate_current > 0 else 1.0

    # 6. SG&A Index (SGAI)
    # SGAI = (SGA_t / Sales_t) / (SGA_t-1 / Sales_t-1)
    sga_ratio_current = data.sga_expense / data.revenue if data.revenue > 0 else 0
    sga_ratio_prior = data.prior_sga_expense / data.prior_revenue if data.prior_revenue > 0 else 0
    sgai = sga_ratio_current / sga_ratio_prior if sga_ratio_prior > 0 else 1.0

    # 7. Leverage Index (LVGI)
    # LVGI = [(CL_t + LTD_t) / TA_t] / [(CL_t-1 + LTD_t-1) / TA_t-1]
    lev_current = (data.current_liabilities + data.long_term_debt) / data.total_assets if data.total_assets > 0 else 0
    lev_prior = (data.prior_current_liabilities + data.prior_long_term_debt) / data.prior_total_assets if data.prior_total_assets > 0 else 0
    lvgi = lev_current / lev_prior if lev_prior > 0 else 1.0

    # 8. Total Accruals to Total Assets (TATA)
    # TATA = (NI - CFO) / TA
    tata = (data.net_income - data.operating_cash_flow) / data.total_assets if data.total_assets > 0 else 0

    # Calculate M-Score using Beneish (1999) coefficients
    m_score = (
        -4.84 +
        0.920 * dsri +
        0.528 * gmi +
        0.404 * aqi +
        0.892 * sgi +
        0.115 * depi +
        -0.172 * sgai +
        4.679 * tata +
        -0.327 * lvgi
    )

    # Determine manipulation probability
    if m_score > -1.78:
        probability = "HIGH - Likely manipulator"
    elif m_score > -2.22:
        probability = "MODERATE - Grey zone, needs further analysis"
    else:
        probability = "LOW - Unlikely manipulator"

    return MScoreResult(
        dsri=dsri,
        gmi=gmi,
        aqi=aqi,
        sgi=sgi,
        depi=depi,
        sgai=sgai,
        lvgi=lvgi,
        tata=tata,
        m_score=m_score,
        manipulation_probability=probability
    )


def identify_red_flags(
    data: FinancialData,
    quality_metrics: QualityMetrics,
    mscore: MScoreResult
) -> List[Dict[str, str]]:
    """
    Identify specific red flags in the financial data.

    Args:
        data: Financial data
        quality_metrics: Calculated quality metrics
        mscore: Beneish M-Score results

    Returns:
        List of red flag dictionaries with 'flag' and 'explanation' keys
    """
    red_flags = []

    # OCF/NI ratio check
    if quality_metrics.ocf_ni_ratio < 0.5:
        red_flags.append({
            'flag': 'Low OCF/NI Ratio',
            'explanation': f'Operating cash flow is only {quality_metrics.ocf_ni_ratio:.1%} of net income. '
                          'This suggests earnings quality issues - income may not be converting to cash.'
        })

    # Negative operating cash flow with positive net income
    if data.operating_cash_flow < 0 and data.net_income > 0:
        red_flags.append({
            'flag': 'Negative OCF with Positive Net Income',
            'explanation': 'Company reports profit but is burning cash from operations. '
                          'This is a significant warning sign.'
        })

    # High accrual ratio
    if quality_metrics.accrual_ratio > 0.10:
        red_flags.append({
            'flag': 'High Accrual Ratio',
            'explanation': f'Accrual ratio of {quality_metrics.accrual_ratio:.1%} indicates earnings '
                          'are heavily driven by accounting accruals rather than cash.'
        })

    # DSO increasing significantly
    if mscore.dsri > 1.3:
        red_flags.append({
            'flag': 'Receivables Growing Faster Than Sales',
            'explanation': f'DSRI of {mscore.dsri:.2f} suggests receivables are growing faster than revenue. '
                          'Could indicate aggressive revenue recognition or collection issues.'
        })

    # Gross margin declining
    if mscore.gmi > 1.2:
        red_flags.append({
            'flag': 'Declining Gross Margins',
            'explanation': f'GMI of {mscore.gmi:.2f} indicates gross margin compression. '
                          'Companies with declining margins may be tempted to manipulate earnings.'
        })

    # Asset quality deteriorating
    if mscore.aqi > 1.3:
        red_flags.append({
            'flag': 'Deteriorating Asset Quality',
            'explanation': f'AQI of {mscore.aqi:.2f} suggests increasing proportion of intangible assets. '
                          'May indicate aggressive capitalization of costs.'
        })

    # Very high sales growth (can incentivize manipulation)
    if mscore.sgi > 1.5:
        red_flags.append({
            'flag': 'Unusually High Sales Growth',
            'explanation': f'SGI of {mscore.sgi:.2f} (>{mscore.sgi*100-100:.0f}% growth). '
                          'Rapid growth can mask underlying issues and create pressure to maintain momentum.'
        })

    # High total accruals
    if mscore.tata > 0.05:
        red_flags.append({
            'flag': 'High Total Accruals',
            'explanation': f'TATA of {mscore.tata:.2%} indicates high accrual component. '
                          'Accruals above 5% of assets warrant scrutiny.'
        })

    # High leverage growth
    if mscore.lvgi > 1.3:
        red_flags.append({
            'flag': 'Rapidly Increasing Leverage',
            'explanation': f'LVGI of {mscore.lvgi:.2f} indicates significant increase in debt. '
                          'Rising leverage combined with other red flags is concerning.'
        })

    # M-Score itself
    if mscore.m_score > -1.78:
        red_flags.append({
            'flag': 'Elevated M-Score',
            'explanation': f'M-Score of {mscore.m_score:.2f} exceeds -1.78 threshold. '
                          'Statistical model suggests higher probability of earnings manipulation.'
        })

    # Cash conversion cycle
    if quality_metrics.cash_conversion_cycle > 120:
        red_flags.append({
            'flag': 'Long Cash Conversion Cycle',
            'explanation': f'CCC of {quality_metrics.cash_conversion_cycle:.0f} days is quite long. '
                          'Company takes extended time to convert investments to cash.'
        })

    return red_flags


def run_quality_analysis(data: FinancialData) -> Dict:
    """
    Run comprehensive earnings quality analysis.

    Args:
        data: FinancialData with all required inputs

    Returns:
        Dictionary with quality_metrics, m_score_result, and red_flags
    """
    # Calculate OCF/NI ratio
    ocf_ni, ocf_interpretation = calculate_ocf_ni_ratio(
        data.operating_cash_flow,
        data.net_income
    )

    # Calculate accrual ratio
    accrual, accrual_interpretation = calculate_accrual_ratio(
        data.net_income,
        data.operating_cash_flow,
        data.total_assets,
        data.prior_total_assets
    )

    # Calculate working capital metrics
    wc_metrics = calculate_working_capital_metrics(
        data.receivables,
        data.inventory,
        data.payables,
        data.revenue,
        data.cogs
    )

    # Determine overall quality score
    if ocf_ni >= 0.9 and accrual < 0.05:
        quality_score = "HIGH"
    elif ocf_ni >= 0.7 and accrual < 0.10:
        quality_score = "MEDIUM"
    else:
        quality_score = "LOW"

    quality_metrics = QualityMetrics(
        ocf_ni_ratio=ocf_ni,
        accrual_ratio=accrual,
        days_sales_outstanding=wc_metrics['dso'],
        days_inventory_outstanding=wc_metrics['dio'],
        days_payable_outstanding=wc_metrics['dpo'],
        cash_conversion_cycle=wc_metrics['ccc'],
        quality_score=quality_score
    )

    # Calculate M-Score
    mscore_result = calculate_beneish_mscore(data)

    # Identify red flags
    red_flags = identify_red_flags(data, quality_metrics, mscore_result)

    return {
        'quality_metrics': quality_metrics,
        'm_score_result': mscore_result,
        'red_flags': red_flags,
        'ocf_interpretation': ocf_interpretation,
        'accrual_interpretation': accrual_interpretation
    }


def format_quality_report(analysis: Dict, company_name: str = "Company") -> str:
    """
    Format the quality analysis as a readable report.

    Args:
        analysis: Output from run_quality_analysis
        company_name: Name of the company for the report header

    Returns:
        Formatted string report
    """
    qm = analysis['quality_metrics']
    ms = analysis['m_score_result']

    lines = []
    lines.append("=" * 70)
    lines.append(f"EARNINGS QUALITY ANALYSIS: {company_name}")
    lines.append("=" * 70)

    lines.append("\n1. CASH FLOW QUALITY")
    lines.append("-" * 40)
    lines.append(f"   OCF/Net Income Ratio: {qm.ocf_ni_ratio:.2f}x")
    lines.append(f"   --> {analysis['ocf_interpretation']}")
    lines.append(f"   Accrual Ratio: {qm.accrual_ratio:.2%}")
    lines.append(f"   --> {analysis['accrual_interpretation']}")
    lines.append(f"   Overall Quality Score: {qm.quality_score}")

    lines.append("\n2. WORKING CAPITAL EFFICIENCY")
    lines.append("-" * 40)
    lines.append(f"   Days Sales Outstanding (DSO): {qm.days_sales_outstanding:.0f} days")
    lines.append(f"   Days Inventory Outstanding (DIO): {qm.days_inventory_outstanding:.0f} days")
    lines.append(f"   Days Payable Outstanding (DPO): {qm.days_payable_outstanding:.0f} days")
    lines.append(f"   Cash Conversion Cycle: {qm.cash_conversion_cycle:.0f} days")

    lines.append("\n3. BENEISH M-SCORE ANALYSIS")
    lines.append("-" * 40)
    lines.append("   Component Scores:")
    lines.append(f"     DSRI (Receivables Index): {ms.dsri:.3f}")
    lines.append(f"     GMI (Gross Margin Index): {ms.gmi:.3f}")
    lines.append(f"     AQI (Asset Quality Index): {ms.aqi:.3f}")
    lines.append(f"     SGI (Sales Growth Index): {ms.sgi:.3f}")
    lines.append(f"     DEPI (Depreciation Index): {ms.depi:.3f}")
    lines.append(f"     SGAI (SG&A Index): {ms.sgai:.3f}")
    lines.append(f"     LVGI (Leverage Index): {ms.lvgi:.3f}")
    lines.append(f"     TATA (Total Accruals/Assets): {ms.tata:.3f}")
    lines.append(f"\n   M-SCORE: {ms.m_score:.2f}")
    lines.append(f"   Threshold: -1.78 (higher = more likely manipulation)")
    lines.append(f"   Assessment: {ms.manipulation_probability}")

    lines.append("\n4. RED FLAGS IDENTIFIED")
    lines.append("-" * 40)
    if analysis['red_flags']:
        for i, flag in enumerate(analysis['red_flags'], 1):
            lines.append(f"\n   [{i}] {flag['flag']}")
            lines.append(f"       {flag['explanation']}")
    else:
        lines.append("   No significant red flags identified.")

    lines.append("\n" + "=" * 70)
    return "\n".join(lines)


if __name__ == "__main__":
    # Example: Analyze a hypothetical company's earnings quality
    print("=" * 70)
    print("EARNINGS QUALITY ANALYSIS - EXAMPLE")
    print("=" * 70)

    # Create sample financial data
    sample_data = FinancialData(
        # Current period income statement
        net_income=500,
        revenue=10000,
        gross_profit=4000,
        operating_income=800,
        cogs=6000,
        sga_expense=3000,
        depreciation=200,

        # Current period balance sheet
        total_assets=15000,
        current_assets=5000,
        cash=1000,
        receivables=1500,
        inventory=2000,
        ppe_net=8000,
        current_liabilities=3000,
        payables=1200,
        long_term_debt=4000,
        total_liabilities=7000,

        # Prior period balance sheet
        prior_total_assets=13500,
        prior_receivables=1200,
        prior_inventory=1800,
        prior_ppe_gross=7500,
        prior_current_assets=4500,
        prior_current_liabilities=2700,
        prior_long_term_debt=3500,

        # Cash flow
        operating_cash_flow=400,  # OCF lower than NI - potential issue

        # Prior period income statement
        prior_revenue=9000,
        prior_gross_profit=3800,
        prior_sga_expense=2700,
        prior_depreciation=180
    )

    # Run analysis
    analysis = run_quality_analysis(sample_data)

    # Print formatted report
    report = format_quality_report(analysis, "Sample Corp")
    print(report)

    # Also show raw metrics
    print("\n" + "=" * 70)
    print("RAW METRICS OUTPUT")
    print("-" * 40)
    qm = analysis['quality_metrics']
    print(f"Quality Metrics Dict:")
    print(f"  ocf_ni_ratio: {qm.ocf_ni_ratio:.3f}")
    print(f"  accrual_ratio: {qm.accrual_ratio:.3f}")
    print(f"  dso: {qm.days_sales_outstanding:.1f}")
    print(f"  dio: {qm.days_inventory_outstanding:.1f}")
    print(f"  dpo: {qm.days_payable_outstanding:.1f}")
    print(f"  ccc: {qm.cash_conversion_cycle:.1f}")
    print(f"  quality_score: {qm.quality_score}")

    ms = analysis['m_score_result']
    print(f"\nM-Score: {ms.m_score:.2f}")
    print(f"Red Flags Count: {len(analysis['red_flags'])}")
