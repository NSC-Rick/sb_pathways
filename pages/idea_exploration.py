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
    page_title="Idea Exploration | Client Readiness Pathways",
    page_icon="💡",
    layout="wide"
)

# Get pathway configuration
pathway = PATHWAYS["idea_exploration"]

# Render pathway header
render_pathway_header(
    pathway["icon"],
    pathway["name"],
    "Clarify your concept, validate your market, and prepare for strategic guidance.",
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
This pathway is designed for entrepreneurs who have a business idea but need help:
- Clarifying and refining their concept
- Understanding their target market
- Validating demand and feasibility
- Identifying critical next steps

By completing this pathway, you'll arrive at your advisory meeting with a clear picture of your idea 
and focused questions about execution.
""")

# Video placeholder
render_video_placeholder("Introduction Video", "5 minutes")

render_section_divider()

# Section 2: Learn
render_section_header("Learn")

st.markdown("Review these resources to build foundational knowledge before completing your workbook.")

col1, col2 = st.columns(2)

with col1:
    render_resource_card(
        "Essential Reading",
        None,
        "info",
        [
            "Validating Your Business Idea",
            "Understanding Your Target Customer",
            "Basic Business Model Fundamentals"
        ]
    )

with col2:
    render_resource_card(
        "Video Resources",
        None,
        "video",
        [
            "Market Research Basics (8 min)",
            "Defining Your Value Proposition (6 min)",
            "Common Startup Mistakes (10 min)"
        ]
    )

render_section_divider()

# Section 3: Work
render_section_header("Work")

st.markdown("""
Complete the Idea Exploration Workbook to organize your thoughts, research, and questions. 
This workbook will serve as the foundation for your advisory conversation.
""")

render_workbook_card(
    "Idea Exploration Workbook",
    [
        "Business concept description",
        "Target market analysis",
        "Competitive landscape",
        "Revenue model ideas",
        "Key questions and concerns"
    ],
    "2-3 hours"
)

st.button("📥 Download Workbook (PDF)", use_container_width=True, disabled=True)
st.caption("Workbook download will be available here")

render_section_divider()

# Section 4: Submit
render_section_header("Submit")

st.markdown("""
Once you've completed your workbook, submit it here. Your advisor will review it before your meeting 
to provide more targeted and valuable guidance.
""")

st.file_uploader("Upload completed workbook", type=['pdf', 'docx'], disabled=True)
st.caption("File upload functionality will be available here")

st.markdown("**Optional:** Add any specific questions or areas you'd like to focus on during your meeting.")
st.text_area("Additional notes for your advisor", height=100, disabled=True, 
             placeholder="e.g., I'm particularly uncertain about pricing strategy...")

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
