"""
Reusable pathway header component
Displays pathway title, estimated time, and what to expect
"""

import streamlit as st
from pathway_config import WHAT_TO_EXPECT

def render_pathway_header(pathway_icon, pathway_name, pathway_description, estimated_time):
    """
    Renders a consistent header for all pathway pages
    
    Args:
        pathway_icon: Emoji icon for the pathway
        pathway_name: Name of the pathway
        pathway_description: Brief description
        estimated_time: Estimated completion time
    """
    st.title(f"{pathway_icon} {pathway_name}")
    st.markdown(f"**{pathway_description}**")
    
    # Estimated time indicator
    st.markdown(f"""
    <div style="background-color: #F7F9FC; border-left: 3px solid #4A90E2; padding: 1rem; 
                margin: 1.5rem 0; border-radius: 4px;">
        <span style="color: #7F8C8D; font-size: 0.9rem;">⏱️ Estimated time: <strong>{estimated_time}</strong></span>
    </div>
    """, unsafe_allow_html=True)

def render_what_to_expect():
    """
    Renders the 'What to Expect' section
    """
    st.markdown("### What to Expect")
    
    for item in WHAT_TO_EXPECT:
        st.markdown(f"• {item}")
    
    st.markdown("<br>", unsafe_allow_html=True)

def render_pathway_flow(current_section="Welcome"):
    """
    Renders a subtle progress flow indicator
    
    Args:
        current_section: The current section being viewed
    """
    sections = ["Business Basics", "Welcome", "Learn", "Work", "Submit", "Schedule"]
    
    flow_html = '<div style="display: flex; align-items: center; justify-content: center; margin: 2rem 0; flex-wrap: wrap;">'
    
    for i, section in enumerate(sections):
        # Determine if this is the current section
        is_current = section == current_section
        
        # Style for current vs other sections
        if is_current:
            style = 'color: #4A90E2; font-weight: 600; font-size: 0.95rem;'
        else:
            style = 'color: #BDC3C7; font-size: 0.9rem;'
        
        flow_html += f'<span style="{style}">{section}</span>'
        
        # Add arrow between sections (except after last one)
        if i < len(sections) - 1:
            flow_html += '<span style="color: #E1E8ED; margin: 0 0.5rem;">→</span>'
    
    flow_html += '</div>'
    
    st.markdown(flow_html, unsafe_allow_html=True)
