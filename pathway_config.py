"""
Centralized pathway configuration
Maintains all pathway metadata in one location for easy maintenance
"""

CORE_PATHWAYS = {
    "idea_exploration": {
        "name": "Idea Exploration",
        "icon": "💡",
        "short_description": "You have a business idea but need help clarifying your concept, validating market fit, and understanding next steps.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Idea Exploration Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "startup_launch": {
        "name": "Startup Launch",
        "icon": "🚀",
        "short_description": "You're ready to launch your business and need guidance on first steps, legal setup, and early operations.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Startup Launch Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "loan_readiness": {
        "name": "Loan Readiness",
        "icon": "💰",
        "short_description": "You are preparing for a loan or funding request and want to strengthen your financial position and documentation.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Loan Readiness Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "marketing_foundation": {
        "name": "Marketing Foundation",
        "icon": "📣",
        "short_description": "You need to build or strengthen your marketing approach to reach and retain customers effectively.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Marketing Foundation Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "recovery_stabilization": {
        "name": "Recovery & Stabilization",
        "icon": "🛟",
        "short_description": "Your business is facing challenges and you need support to stabilize operations and regain control.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Recovery & Stabilization Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "growth_planning": {
        "name": "Growth Planning",
        "icon": "📈",
        "short_description": "Your business is stable and you're ready to plan strategic growth and expansion.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Growth Planning Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "business_transition": {
        "name": "Business Transition",
        "icon": "🔄",
        "short_description": "You are planning to buy, sell, or transition your business and want guidance through the process.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Business Transition Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "financial_foundations": {
        "name": "Financial Foundations",
        "icon": "📊",
        "short_description": "You need to strengthen your financial management, recordkeeping, and reporting systems.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Financial Foundations Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "solo_consultant_path": {
        "name": "Solo Consultant Path",
        "icon": "👤",
        "short_description": "You're building or running a solo consulting or professional services practice.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Solo Consultant Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    }
}

SUPPLEMENTAL_PATHWAYS = {
    "ai_for_small_business": {
        "name": "AI for Small Business",
        "icon": "🤖",
        "short_description": "Learn practical ways to use AI tools to improve efficiency and decision-making in your business.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "AI for Small Business Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "financial_projections": {
        "name": "Building Financial Projections",
        "icon": "📐",
        "short_description": "Create realistic financial forecasts and projections for planning and funding purposes.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Financial Projections Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "business_planning": {
        "name": "Business Planning",
        "icon": "📝",
        "short_description": "Develop a clear, actionable business plan for your venture.",
        "estimated_time": "60+ minutes",
        "workbook_placeholder": "Business Planning Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "cash_flow_basics": {
        "name": "Cash Flow Basics",
        "icon": "💵",
        "short_description": "Master the fundamentals of cash flow management and forecasting.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Cash Flow Basics Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "marketing_fundamentals": {
        "name": "Marketing Fundamentals",
        "icon": "📣",
        "short_description": "Learn core marketing concepts and strategies for small businesses.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Marketing Fundamentals Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "time_priority_management": {
        "name": "Time & Priority Management",
        "icon": "⏰",
        "short_description": "Improve how you manage time, priorities, and energy as a business owner.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Time & Priority Management Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "owner_sustainability": {
        "name": "Owner Sustainability",
        "icon": "🌱",
        "short_description": "Build sustainable practices to avoid burnout and maintain long-term business ownership.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Owner Sustainability Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "digital_readiness": {
        "name": "Digital Readiness",
        "icon": "💻",
        "short_description": "Assess and improve your business's digital capabilities and online presence.",
        "estimated_time": "30–45 minutes",
        "workbook_placeholder": "Digital Readiness Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "pricing_profitability": {
        "name": "Pricing & Profitability",
        "icon": "📊",
        "short_description": "Develop pricing strategies that support profitability and business sustainability.",
        "estimated_time": "45–60 minutes",
        "workbook_placeholder": "Pricing & Profitability Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    }
}

# Combined pathways for backward compatibility
PATHWAYS = {**CORE_PATHWAYS, **SUPPLEMENTAL_PATHWAYS}

BUSINESS_BASICS_TOPICS = [
    {
        "icon": "💵",
        "title": "Understanding Cash Flow",
        "description": "Learn why cash flow is different from profit and why it matters for your business survival."
    },
    {
        "icon": "📊",
        "title": "Revenue vs Profit",
        "description": "Understand the difference between money coming in and money you actually keep."
    },
    {
        "icon": "⚖️",
        "title": "Fixed vs Variable Costs",
        "description": "Learn how different types of expenses affect your business decisions and flexibility."
    },
    {
        "icon": "👥",
        "title": "Understanding Customers",
        "description": "Discover why knowing your customer deeply is more important than having lots of customers."
    },
    {
        "icon": "🔍",
        "title": "Why Businesses Struggle",
        "description": "Common patterns that lead to business challenges and how to recognize them early."
    },
    {
        "icon": "🧩",
        "title": "Organizing Business Thinking",
        "description": "Simple frameworks for thinking through business decisions and priorities."
    }
]

WHAT_TO_EXPECT = [
    "Watch a few short videos",
    "Complete a simple workbook",
    "Organize your thoughts",
    "Meet with your advisor"
]

APP_FOOTER_TEXT = "These pathways are designed to support thoughtful preparation before meaningful advising conversations."
