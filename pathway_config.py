"""
Centralized pathway configuration
Maintains all pathway metadata in one location for easy maintenance
"""

PATHWAYS = {
    "idea_exploration": {
        "name": "Idea Exploration",
        "icon": "💡",
        "short_description": "You have a business idea but need help clarifying your concept, validating market fit, and understanding next steps.",
        "estimated_time": "30–45 minutes",
        "page_file": "pages/idea_exploration.py",
        "workbook_placeholder": "Idea Exploration Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "loan_readiness": {
        "name": "Loan Readiness",
        "icon": "💰",
        "short_description": "You need financing for your business and want to prepare a strong application with clear financials and a compelling case.",
        "estimated_time": "45–60 minutes",
        "page_file": "pages/loan_readiness.py",
        "workbook_placeholder": "Loan Readiness Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "recovery_stabilization": {
        "name": "Recovery & Stabilization",
        "icon": "🛟",
        "short_description": "Your business is facing challenges and you need guidance on stabilizing operations, managing cash flow, or pivoting strategy.",
        "estimated_time": "30–45 minutes",
        "page_file": "pages/recovery_stabilization.py",
        "workbook_placeholder": "Recovery & Stabilization Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    },
    "business_transition": {
        "name": "Business Transition",
        "icon": "🔄",
        "short_description": "You're considering selling, transferring ownership, or closing your business and need structured guidance through the process.",
        "estimated_time": "45–60 minutes",
        "page_file": "pages/business_transition.py",
        "workbook_placeholder": "Business Transition Workbook",
        "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"]
    }
}

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
