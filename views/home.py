"""
Home view for Client Readiness Pathways
Renders the main landing page with pathway selection
"""

import streamlit as st
from pathway_config import PATHWAYS
from components.footer import render_footer


def render_home():
    """Render the home page with pathway selection"""
    
    # Main content
    st.title("Client Readiness Pathways")
    st.markdown('<p class="subtitle">Structured preparation before meaningful advising.</p>', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    Welcome to the Client Readiness Pathways system. This resource helps you prepare for your advisory meeting 
    so you can make the most of your time together.
    
    Each pathway is designed to help you arrive with clarity, focus, and actionable questions.
    """)
    
    st.markdown("## Choose Your Pathway")
    
    # Pathway cards in two columns using config
    col1, col2 = st.columns(2)
    
    # First column: Idea Exploration and Recovery
    with col1:
        for pathway_key in ["idea_exploration", "recovery_stabilization"]:
            pathway = PATHWAYS[pathway_key]
            st.markdown(f"""
            <div class="pathway-card">
                <h3>{pathway['icon']} {pathway['name']}</h3>
                <p>{pathway['short_description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Start {pathway['name']}", key=f"start_{pathway_key}", use_container_width=True):
                st.session_state.current_page = pathway_key
                st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)
    
    # Second column: Loan Readiness and Business Transition
    with col2:
        for pathway_key in ["loan_readiness", "business_transition"]:
            pathway = PATHWAYS[pathway_key]
            st.markdown(f"""
            <div class="pathway-card">
                <h3>{pathway['icon']} {pathway['name']}</h3>
                <p>{pathway['short_description']}</p>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button(f"Start {pathway['name']}", key=f"start_{pathway_key}", use_container_width=True):
                st.session_state.current_page = pathway_key
                st.rerun()
            
            st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Footer information
    st.markdown("""
    ### How It Works
    
    Each pathway follows a structured approach:
    
    1. **Business Basics** – Review foundational concepts to build shared understanding
    2. **Learn** – Access curated resources and guidance specific to your situation
    3. **Work** – Complete a focused workbook to organize your thoughts and data
    4. **Submit** – Share your completed work with your advisor before the meeting
    5. **Schedule** – Book your advisory session when you're ready
    
    This approach ensures your time with an advisor is focused on strategy, problem-solving, and action planning 
    rather than basic information gathering.
    """)
    
    # Footer
    render_footer()
