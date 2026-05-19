import streamlit as st
from pathway_config import PATHWAYS
from content.video_links import VIDEO_LINKS, VIDEO_HEIGHT
from components.pathway_header import render_pathway_header, render_what_to_expect, render_pathway_flow
from components.section_divider import render_section_divider, render_section_header
from components.resource_card import render_resource_card, render_video_placeholder, render_workbook_card
from components.schedule_section import render_schedule_section
from components.business_basics import render_business_basics
from components.footer import render_footer

# Page configuration
st.set_page_config(
    page_title="Loan Readiness | Client Readiness Pathways",
    page_icon="💰",
    layout="wide"
)

# Get pathway configuration
pathway = PATHWAYS["loan_readiness"]

# Render pathway header
render_pathway_header(
    pathway["icon"],
    pathway["name"],
    "Prepare a compelling loan application with organized financials and clear business case.",
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
This pathway is designed for business owners who need financing and want to:
- Understand what lenders look for
- Organize financial documentation
- Build a strong business case
- Prepare for the application process

By completing this pathway, you'll arrive at your advisory meeting with organized materials 
and a clear understanding of your financing needs.
""")

st.markdown("<br>", unsafe_allow_html=True)

# Introduction Video Section
st.markdown("### Introduction")
st.caption("Start with a short introduction to this pathway before moving into the preparation materials.")

st.markdown("<br>", unsafe_allow_html=True)

# Embedded intro video
if VIDEO_LINKS["loan_intro"]:
    st.components.v1.iframe(
        VIDEO_LINKS["loan_intro"],
        height=VIDEO_HEIGHT,
        scrolling=False
    )
else:
    # Fallback to placeholder if video not available
    render_video_placeholder("Introduction Video", "7 minutes")

st.markdown("<br>", unsafe_allow_html=True)

render_section_divider()

# Section 2: Learn
render_section_header("Learn")

st.markdown("Review these resources to understand the loan application process and lender expectations.")

col1, col2 = st.columns(2)

with col1:
    render_resource_card(
        "Essential Reading",
        None,
        "info",
        [
            "Understanding Loan Types and Terms",
            "What Lenders Look For",
            "Preparing Financial Statements",
            "Building Your Business Case"
        ]
    )

with col2:
    render_resource_card(
        "Video Resources",
        None,
        "video",
        [
            "Loan Application Overview (10 min)",
            "Financial Documentation Checklist (8 min)",
            "Common Application Mistakes (6 min)"
        ]
    )

render_section_divider()

# Section 3: Work
render_section_header("Work")

st.markdown("""
Complete the Loan Readiness Workbook to organize your financial information, clarify your needs, 
and prepare your business case. This workbook will help you identify any gaps before applying.
""")

render_workbook_card(
    "Loan Readiness Workbook",
    [
        "Loan amount and use of funds",
        "Financial history and projections",
        "Collateral and personal guarantees",
        "Business plan summary",
        "Document checklist"
    ],
    "3-4 hours"
)

st.button("📥 Download Workbook (PDF)", use_container_width=True, disabled=True)
st.caption("Workbook download will be available here")

render_section_divider()

# Section 4: Submit
render_section_header("Submit")

st.markdown("""
Once you've completed your workbook, submit it here along with any supporting financial documents. 
Your advisor will review everything before your meeting to provide targeted guidance.
""")

st.file_uploader("Upload completed workbook", type=['pdf', 'docx'], disabled=True)
st.caption("File upload functionality will be available here")

st.markdown("**Optional:** Upload supporting documents (financial statements, tax returns, etc.)")
st.file_uploader("Additional documents", type=['pdf', 'xlsx', 'docx'], accept_multiple_files=True, disabled=True)

st.text_area("Additional notes for your advisor", height=100, disabled=True,
             placeholder="e.g., I'm unsure about how to value my equipment for collateral...")

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
