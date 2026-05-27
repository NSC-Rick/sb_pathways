"""
Pathway relationships configuration
Maps each pathway to its related/recommended pathways for "Continue Exploring" section
"""

PATHWAY_RELATIONSHIPS = {
    "idea_exploration": [
        {"key": "startup_launch", "name": "Startup Launch", "icon": "🚀"},
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
    ],
    "startup_launch": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "marketing_foundation", "name": "Marketing Foundation", "icon": "📣"},
    ],
    "loan_readiness": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "startup_launch", "name": "Startup Launch", "icon": "🚀"},
        {"key": "growth_planning", "name": "Growth Planning", "icon": "📈"},
    ],
    "marketing_foundation": [
        {"key": "startup_launch", "name": "Startup Launch", "icon": "🚀"},
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
    ],
    "recovery_stabilization": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "owner_sustainability", "name": "Owner Sustainability", "icon": "🌱"},
    ],
    "growth_planning": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "marketing_foundation", "name": "Marketing Foundation", "icon": "📣"},
    ],
    "business_transition": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "owner_sustainability", "name": "Owner Sustainability", "icon": "🌱"},
        {"key": "growth_planning", "name": "Growth Planning", "icon": "📈"},
    ],
    "financial_foundations": [
        {"key": "loan_readiness", "name": "Loan Readiness", "icon": "💰"},
        {"key": "recovery_stabilization", "name": "Recovery & Stabilization", "icon": "🛟"},
        {"key": "startup_launch", "name": "Startup Launch", "icon": "🚀"},
    ],
    "solo_consultant_path": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "marketing_foundation", "name": "Marketing Foundation", "icon": "📣"},
        {"key": "owner_sustainability", "name": "Owner Sustainability", "icon": "🌱"},
    ],
    # Supplemental pathways
    "ai_for_small_business": [
        {"key": "digital_readiness", "name": "Digital Readiness", "icon": "💻"},
        {"key": "time_priority_management", "name": "Time & Priority Management", "icon": "⏰"},
    ],
    "financial_projections": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "cash_flow_basics", "name": "Cash Flow Basics", "icon": "💵"},
        {"key": "business_planning", "name": "Business Planning", "icon": "📝"},
    ],
    "business_planning": [
        {"key": "financial_projections", "name": "Building Financial Projections", "icon": "📐"},
        {"key": "marketing_fundamentals", "name": "Marketing Fundamentals", "icon": "📣"},
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
    ],
    "cash_flow_basics": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "financial_projections", "name": "Building Financial Projections", "icon": "📐"},
        {"key": "pricing_profitability", "name": "Pricing & Profitability", "icon": "📊"},
    ],
    "marketing_fundamentals": [
        {"key": "marketing_foundation", "name": "Marketing Foundation", "icon": "📣"},
        {"key": "digital_readiness", "name": "Digital Readiness", "icon": "💻"},
        {"key": "pricing_profitability", "name": "Pricing & Profitability", "icon": "📊"},
    ],
    "time_priority_management": [
        {"key": "owner_sustainability", "name": "Owner Sustainability", "icon": "🌱"},
        {"key": "growth_planning", "name": "Growth Planning", "icon": "📈"},
    ],
    "owner_sustainability": [
        {"key": "recovery_stabilization", "name": "Recovery & Stabilization", "icon": "🛟"},
        {"key": "growth_planning", "name": "Growth Planning", "icon": "📈"},
        {"key": "time_priority_management", "name": "Time & Priority Management", "icon": "⏰"},
    ],
    "digital_readiness": [
        {"key": "ai_for_small_business", "name": "AI for Small Business", "icon": "🤖"},
        {"key": "marketing_fundamentals", "name": "Marketing Fundamentals", "icon": "📣"},
    ],
    "pricing_profitability": [
        {"key": "financial_foundations", "name": "Financial Foundations", "icon": "📊"},
        {"key": "cash_flow_basics", "name": "Cash Flow Basics", "icon": "💵"},
        {"key": "marketing_fundamentals", "name": "Marketing Fundamentals", "icon": "📣"},
    ],
}
