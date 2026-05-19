"""
Business Basics Foundation Layer
Shared foundational section rendered at the start of each pathway
"""

import streamlit as st
from pathway_config import BUSINESS_BASICS_TOPICS
from components.resource_card import render_expandable_topic
from components.section_divider import render_section_divider, render_section_header

def render_business_basics():
    """
    Renders the Business Basics foundation layer
    This is Step 0 before each pathway begins
    """
    render_section_header("Business Basics", "🎯")
    
    st.markdown("""
    <p style="color: #7F8C8D; font-size: 1.1rem; margin-bottom: 2rem;">
        Before beginning your pathway, review a few foundational business concepts.
    </p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    These topics provide a shared foundation for thinking about your business. 
    They're presented in plain language and designed to be approachable, not academic.
    
    **You don't need to be an expert** — just familiar enough to have productive conversations with your advisor.
    """)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Render expandable topic cards in two columns for better layout
    col1, col2 = st.columns(2)
    
    for i, topic in enumerate(BUSINESS_BASICS_TOPICS):
        with col1 if i % 2 == 0 else col2:
            render_expandable_topic(
                topic["icon"],
                topic["title"],
                topic["description"]
            )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.info("💡 **Tip**: You can return to these topics anytime during your pathway if you need a refresher.")
    
    render_section_divider()
