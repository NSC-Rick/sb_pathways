"""
Idea Exploration pathway view
Renders the Idea Exploration pathway content
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
from components.video_resource_list import render_video_resource_list


def render_idea_exploration():
    """Render the Idea Exploration pathway"""
    
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
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Introduction Video Section with improved framing
    if VIDEO_LINKS["idea_intro"]:
        render_video_section(
            video_url=VIDEO_LINKS["idea_intro"],
            section_title="Introduction",
            intro_text="Start with a short introduction to this pathway before moving into the preparation materials.",
            subtitle="Take a few minutes to review this introduction before continuing."
        )
    else:
        # Fallback to placeholder if video not available
        st.markdown("### Introduction")
        st.caption("Start with a short introduction to this pathway before moving into the preparation materials.")
        st.markdown("<br>", unsafe_allow_html=True)
        render_video_placeholder("Introduction Video", "5 minutes")
        st.markdown("<br>", unsafe_allow_html=True)
    
    render_section_divider()
    
    # Section 2: Learn
    render_section_header("Learn")
    
    st.markdown("Review these curated resources to build foundational knowledge before completing your workbook.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Essential Reading Section
    st.markdown("### 📚 Essential Reading")
    st.caption("Advisor-recommended materials to guide your exploration process.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Reading resource cards
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="pathway-card">
            <h4>📄 Validating Your Business Idea</h4>
            <p>Learn practical approaches to testing and validating your business concept before making larger commitments.</p>
        </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "📥 Download PDF",
            data=open("pathways/core/idea_exploration/readings/SB_Pathways_Validating_Your_Business_Idea_FINAL.pdf", "rb"),
            file_name="Validating_Your_Business_Idea.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="pathway-card">
            <h4>📄 Understanding Your Target Customer</h4>
            <p>Develop clarity on who your customers are, what they need, and how to reach them effectively.</p>
        </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "📥 Download PDF",
            data=open("pathways/core/idea_exploration/readings/SB_Pathways_Understanding_Your_Target_Customer_FINAL.pdf", "rb"),
            file_name="Understanding_Your_Target_Customer.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="pathway-card">
            <h4>📄 Basic Business Model Fundamentals</h4>
            <p>Understand the core components of a business model and how they work together to create value.</p>
        </div>
        """, unsafe_allow_html=True)
        st.download_button(
            "📥 Download PDF",
            data=open("pathways/core/idea_exploration/readings/SB_Pathways_Basic_Business_Model_Fundamentals_FINAL.pdf", "rb"),
            file_name="Basic_Business_Model_Fundamentals.pdf",
            mime="application/pdf",
            use_container_width=True
        )
        st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Video Resources Section
    st.markdown("### Video Resources")
    st.caption("These additional resources provide practical perspectives and foundational guidance related to this pathway.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Educational video resource list
    educational_videos = [
        {
            "title": "How to Validate a Business Idea",
            "duration": "8 min",
            "description": "A practical introduction to testing and validating early-stage business concepts.",
            "url": VIDEO_LINKS["idea_validate"]
        },
        {
            "title": "Finding Product Market Fit",
            "duration": "7 min",
            "description": "Understanding customer fit, demand, and market alignment for new ideas.",
            "url": VIDEO_LINKS["idea_product_fit"]
        },
        {
            "title": "Start Small and Test Your Business Idea",
            "duration": "6 min",
            "description": "Exploring practical ways to test ideas thoughtfully before scaling.",
            "url": VIDEO_LINKS["idea_test_small"]
        }
    ]
    
    render_video_resource_list(educational_videos)
    
    render_section_divider()
    
    # Section 3: Work
    render_section_header("Work")
    
    st.markdown("""
    Complete the Idea Exploration Workbook to organize your thoughts, research, and questions. 
    This workbook will serve as the foundation for your advisory conversation.
    """)
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Guided Workbook Section
    st.markdown("### 📝 Guided Workbook")
    st.caption("A guided workbook designed to help you thoughtfully explore, test, and refine your business idea before making larger commitments.")
    st.markdown("<br>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
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
    
    with col2:
        st.markdown("<br>", unsafe_allow_html=True)
        st.download_button(
            "📥 Download Workbook",
            data=open("pathways/core/idea_exploration/workbooks/SB_Pathways_Idea_Exploration_Workbook_FINAL.pdf", "rb"),
            file_name="Idea_Exploration_Workbook.pdf",
            mime="application/pdf",
            use_container_width=True,
            type="primary"
        )
        st.markdown("<br>", unsafe_allow_html=True)
        st.caption("💡 **Tip:** Print this workbook or complete it digitally before your advisory meeting.")
    
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
            st.session_state.current_page = "home"
            st.rerun()
    
    # Footer
    render_footer()
