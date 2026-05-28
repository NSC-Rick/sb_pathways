"""
Generic placeholder view for pathways under development
Provides a clean "coming soon" experience with pathway metadata
"""

import streamlit as st
from components.footer import render_footer
from src.core import get_navigation_context


def render_pathway_placeholder(pathway_name, pathway_icon, pathway_description, estimated_time):
    """
    Render a placeholder page for pathways under development
    
    Args:
        pathway_name: Name of the pathway
        pathway_icon: Emoji icon for the pathway
        pathway_description: Short description of the pathway
        estimated_time: Estimated completion time
    """
    
    # Header
    st.title(f"{pathway_icon} {pathway_name}")
    st.markdown('<p class="subtitle">Coming Soon</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Placeholder content
    st.markdown(f"""
    ### This Pathway Is Under Development
    
    {pathway_description}
    
    **Estimated Time**: {estimated_time}
    
    ---
    
    ### What to Expect
    
    When this pathway launches, you'll be able to:
    
    - **Learn** – Access curated resources and guidance specific to this topic
    - **Work** – Complete a focused workbook to organize your thoughts and information
    - **Submit** – Share your completed work with your advisor before the meeting
    - **Schedule** – Book your advisory session when you're ready
    
    ---
    
    ### Need Help Now?
    
    While this pathway is being developed, you can:
    
    - Explore other available pathways that may address related needs
    - Schedule a general advisory meeting to discuss your situation
    - Contact your advisor directly for immediate support
    
    """)
    
    # Back to home button
    nav_context = get_navigation_context()
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("← Back to Home", width="stretch"):
            nav_context.navigate_to_home()
            st.rerun()
    
    # Footer
    render_footer()
