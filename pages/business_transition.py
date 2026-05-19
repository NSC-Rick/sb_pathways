import streamlit as st
from pathway_config import PATHWAYS
from components.pathway_header import render_pathway_header, render_what_to_expect, render_pathway_flow
from components.section_divider import render_section_divider, render_section_header
from components.resource_card import render_resource_card, render_video_placeholder, render_workbook_card
from components.schedule_section import render_schedule_section
from components.business_basics import render_business_basics
from components.footer import render_footer

# Page configuration
st.set_page_config(
    page_title="Business Transition | Client Readiness Pathways",
    page_icon="🔄",
    layout="wide"
)

# Get pathway configuration
pathway = PATHWAYS["business_transition"]

# Render pathway header
render_pathway_header(
    pathway["icon"],
    pathway["name"],
    "Plan your exit, succession, or closure with clarity and confidence.",
    pathway["estimated_time"]
)

# Render what to expect
render_what_to_expect()

# Render pathway flow
render_pathway_flow("Welcome")

render_section_divider()

# Business Basics Foundation Layer
render_business_basics()

# Section 1: Welcome
render_section_header("Welcome")

st.markdown("""
This pathway is designed for business owners considering a transition who need help:
- Understanding transition options (sale, succession, closure)
- Preparing the business for transition
- Valuing the business appropriately
- Planning the transition timeline and process

By completing this pathway, you'll arrive at your advisory meeting with a clear understanding of your 
goals and the steps needed to achieve a successful transition.
""")

# Video placeholder
render_video_placeholder("Introduction Video", "8 minutes")

render_section_divider()

# Section 2: Learn
render_section_header("Learn")

st.markdown("Review these resources to understand transition options and planning considerations.")

col1, col2 = st.columns(2)

with col1:
    render_resource_card(
        "Essential Reading",
        None,
        "info",
        [
            "Business Transition Options Overview",
            "Preparing Your Business for Sale",
            "Succession Planning Fundamentals",
            "Business Valuation Basics"
        ]
    )

with col2:
    render_resource_card(
        "Video Resources",
        None,
        "video",
        [
            "Exit Strategy Planning (10 min)",
            "Maximizing Business Value (9 min)",
            "Transition Timeline (7 min)"
        ]
    )

render_section_divider()

# Section 3: Work
render_section_header("Work")

st.markdown("""
Complete the Business Transition Workbook to clarify your goals, assess your business readiness, 
and identify key considerations for your transition. This will form the basis of your transition strategy.
""")

render_workbook_card(
    "Business Transition Workbook",
    [
        "Transition goals and timeline",
        "Business readiness assessment",
        "Financial preparation",
        "Stakeholder considerations",
        "Next steps and action items"
    ],
    "3-4 hours"
)

st.button("📥 Download Workbook (PDF)", use_container_width=True, disabled=True)
st.caption("Workbook download will be available here")

render_section_divider()

# Section 4: Submit
render_section_header("Submit")

st.markdown("""
Once you've completed your workbook, submit it here. Your advisor will review it confidentially 
before your meeting to provide tailored guidance for your transition.
""")

st.file_uploader("Upload completed workbook", type=['pdf', 'docx'], disabled=True)
st.caption("File upload functionality will be available here")

st.markdown("**Optional:** Share any specific concerns or priorities for your transition.")
st.text_area("Additional notes for your advisor", height=100, disabled=True,
             placeholder="e.g., I want to ensure my employees are taken care of during the transition...")

render_section_divider()

# Section 5: Schedule
render_section_header("Schedule")

render_schedule_section()

render_section_divider()

# Navigation
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Footer
render_footer()
