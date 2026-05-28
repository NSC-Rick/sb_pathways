"""
Business Transition pathway view
Renders the Business Transition pathway content
"""

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
from src.core import get_navigation_context
from components.video_resource_list import render_video_resource_list


def render_business_transition():
    """Render the Business Transition pathway"""
    
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
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Introduction Video Section with improved framing
    # Future Business Transition Intro Video Placeholder
    if VIDEO_LINKS["transition_intro"]:
        render_video_section(
            video_url=VIDEO_LINKS["transition_intro"],
            section_title="Introduction",
            intro_text="Start with a short introduction to this pathway before moving into the preparation materials.",
            subtitle="Take a few minutes to review this introduction before continuing."
        )
    else:
        # Placeholder until video is available
        st.markdown("### Introduction")
        st.caption("Start with a short introduction to this pathway before moving into the preparation materials.")
        st.markdown("<br>", unsafe_allow_html=True)
        render_video_placeholder("Introduction Video", "8 minutes")
        st.markdown("<br>", unsafe_allow_html=True)
    
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
                "Exit Planning Strategies (12 min)",
                "Valuation Methods (9 min)",
                "Succession vs. Sale (7 min)"
            ]
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Video Resources Section
    st.markdown("### Video Resources")
    st.caption("These additional resources provide practical perspectives and foundational guidance related to this pathway.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Educational video resource list
    educational_videos = [
        {
            "title": "Preparing a Business for Sale",
            "duration": "9 min",
            "description": "Key concepts involved in preparing a business for transition or sale.",
            "url": VIDEO_LINKS["transition_sale"]
        },
        {
            "title": "Small Business Succession Planning",
            "duration": "8 min",
            "description": "An overview of succession planning strategies for small businesses.",
            "url": VIDEO_LINKS["transition_succession"]
        },
        {
            "title": "How to Increase Business Transferability",
            "duration": "7 min",
            "description": "Understanding how to improve business transferability and continuity.",
            "url": VIDEO_LINKS["transition_transferability"]
        }
    ]
    
    render_video_resource_list(educational_videos)
    
    render_section_divider()
    
    # Section 3: Work
    render_section_header("Work")
    
    st.markdown("""
    Complete the Business Transition Workbook to clarify your goals, assess your business readiness, 
    and develop a preliminary transition plan. This will guide your advisory conversation.
    """)
    
    render_workbook_card(
        "Business Transition Workbook",
        [
            "Transition goals and timeline",
            "Business assessment and valuation",
            "Transition options analysis",
            "Stakeholder considerations",
            "Next steps and questions"
        ],
        "3-4 hours"
    )
    
    st.button("📥 Download Workbook (PDF)", width="stretch", disabled=True)
    st.caption("Workbook download will be available here")
    
    render_section_divider()
    
    # Section 4: Submit
    render_section_header("Submit")
    
    st.markdown("""
    Once you've completed your workbook, submit it here. Your advisor will review it before your meeting 
    to provide guidance tailored to your transition goals.
    """)
    
    st.file_uploader("Upload completed workbook", type=['pdf', 'docx'], disabled=True)
    st.caption("File upload functionality will be available here")
    
    st.markdown("**Optional:** Share any specific concerns or questions about your transition.")
    st.text_area("Additional notes for your advisor", height=100, disabled=True,
                 placeholder="e.g., I'm unsure about the best timing for my transition...")
    
    render_section_divider()
    
    # Section 5: Schedule
    render_section_header("Schedule")
    
    render_schedule_section()
    
    render_section_divider()
    
    # Continue Exploring section
    from components.continue_exploring import render_continue_exploring
    render_continue_exploring("business_transition")
    
    render_section_divider()
    
    # Navigation
    nav_context = get_navigation_context()
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        if st.button("← Back to Home", width="stretch"):
            nav_context.navigate_to_home()
            st.rerun()
    
    # Footer
    render_footer()
