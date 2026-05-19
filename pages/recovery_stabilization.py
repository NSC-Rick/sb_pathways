import streamlit as st
from pathway_config import PATHWAYS
from content.video_links import VIDEO_LINKS
from components.pathway_header import render_pathway_header, render_what_to_expect, render_pathway_flow
from components.section_divider import render_section_divider, render_section_header
from components.resource_card import render_resource_card, render_video_placeholder, render_workbook_card
from components.schedule_section import render_schedule_section
from components.business_basics import render_business_basics
from components.footer import render_footer
from components.video_embed import render_video_section

# Page configuration
st.set_page_config(
    page_title="Recovery & Stabilization | Client Readiness Pathways",
    page_icon="🛟",
    layout="wide"
)

# Get pathway configuration
pathway = PATHWAYS["recovery_stabilization"]

# Render pathway header
render_pathway_header(
    pathway["icon"],
    pathway["name"],
    "Navigate challenges, stabilize operations, and build a path forward.",
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

# Special supportive messaging for Recovery pathway
st.markdown("""
<div style="background-color: #E8F4F8; border-left: 4px solid #4A90E2; padding: 1.5rem; 
            margin: 1.5rem 0; border-radius: 4px;">
    <p style="color: #2C3E50; font-size: 1.05rem; margin: 0;">
        <strong>You are not alone.</strong> Many business owners face challenges at some point. 
        Taking time to assess your situation thoughtfully is a sign of strength, not weakness.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
This pathway is designed for business owners facing operational or financial challenges who need help:
- Assessing the current situation objectively
- Stabilizing cash flow and operations
- Identifying viable paths forward
- Making difficult strategic decisions

By completing this pathway, you'll arrive at your advisory meeting with a clear picture of your situation 
and focused options for moving forward.
""")

st.markdown("<br>", unsafe_allow_html=True)

# Introduction Video Section with improved framing
# Future Recovery Intro Video Placeholder
if VIDEO_LINKS["recovery_intro"]:
    render_video_section(
        video_url=VIDEO_LINKS["recovery_intro"],
        section_title="Introduction",
        intro_text="Start with a short introduction to this pathway before moving into the preparation materials.",
        subtitle="Take a few minutes to review this introduction before continuing."
    )
else:
    # Placeholder until video is available
    st.markdown("### Introduction")
    st.caption("Start with a short introduction to this pathway before moving into the preparation materials.")
    st.markdown("<br>", unsafe_allow_html=True)
    render_video_placeholder("Introduction Video", "6 minutes")
    st.markdown("<br>", unsafe_allow_html=True)

# Testimonial placeholder section
st.markdown("""
<div style="background-color: #F7F9FC; border: 1px solid #E1E8ED; padding: 1.5rem; 
            margin: 1.5rem 0; border-radius: 8px; font-style: italic;">
    <p style="color: #7F8C8D; margin: 0;">
        "Working through this pathway helped me see my situation more clearly. I wasn't sure if I should 
        keep going or make changes, but the process helped me think through my options without panic."
    </p>
    <p style="color: #95A5A6; font-size: 0.9rem; margin-top: 0.5rem; margin-bottom: 0;">
        — Business owner, 2025
    </p>
</div>
""", unsafe_allow_html=True)

render_section_divider()

# Section 2: Learn
render_section_header("Learn")

st.markdown("""
Review these resources to understand recovery strategies and stabilization approaches. 
These materials are designed to help you think clearly about your options.
""")

col1, col2 = st.columns(2)

with col1:
    render_resource_card(
        "Essential Reading",
        None,
        "info",
        [
            "Cash Flow Management in Crisis",
            "Assessing Business Viability",
            "Restructuring Options",
            "Communicating with Stakeholders"
        ]
    )

with col2:
    render_resource_card(
        "Video Resources",
        None,
        "video",
        [
            "Stabilization Strategies (9 min)",
            "Making Tough Decisions (7 min)",
            "Pivot vs. Persevere (8 min)"
        ]
    )

render_section_divider()

# Section 3: Work
render_section_header("Work")

st.markdown("""
Complete the Recovery & Stabilization Workbook to assess your situation, identify immediate priorities, 
and explore potential paths forward. This honest assessment will guide your advisory conversation.
""")

st.info("💡 **Remember**: This workbook is confidential. Be honest about your situation — your advisor is here to help, not judge.")

render_workbook_card(
    "Recovery & Stabilization Workbook",
    [
        "Current situation assessment",
        "Cash flow analysis",
        "Critical challenges and constraints",
        "Potential recovery strategies",
        "Decision-making framework"
    ],
    "2-3 hours"
)

st.button("📥 Download Workbook (PDF)", use_container_width=True, disabled=True)
st.caption("Workbook download will be available here")

render_section_divider()

# Section 4: Submit
render_section_header("Submit")

st.markdown("""
Once you've completed your workbook, submit it here. Your advisor will review it confidentially 
before your meeting to provide the most relevant guidance for your situation.
""")

st.markdown("""
<div style="background-color: #FFF9E6; border-left: 4px solid #F39C12; padding: 1rem; 
            margin: 1rem 0; border-radius: 4px;">
    <p style="color: #2C3E50; font-size: 0.95rem; margin: 0;">
        <strong>Time-sensitive situation?</strong> If you're facing an urgent deadline or crisis, 
        please note that in your submission so we can prioritize your meeting.
    </p>
</div>
""", unsafe_allow_html=True)

st.file_uploader("Upload completed workbook", type=['pdf', 'docx'], disabled=True)
st.caption("File upload functionality will be available here")

st.markdown("**Optional:** Share any specific concerns or constraints you're facing.")
st.text_area("Additional notes for your advisor", height=100, disabled=True,
             placeholder="e.g., I need to make a decision about staffing within 30 days...")

render_section_divider()

# Section 5: Schedule
render_section_header("Schedule")

render_schedule_section()

st.markdown("""
<div style="background-color: #E8F4F8; padding: 1.5rem; margin: 1.5rem 0; 
            border-radius: 8px; text-align: center;">
    <p style="color: #2C3E50; font-size: 1rem; margin: 0;">
        <strong>Remember:</strong> Your advisor has helped many business owners navigate similar challenges. 
        You're taking the right step by seeking guidance.
    </p>
</div>
""", unsafe_allow_html=True)

render_section_divider()

# Navigation
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("app.py")

# Footer
render_footer()
