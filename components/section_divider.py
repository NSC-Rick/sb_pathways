"""
Reusable section divider component
Creates consistent visual separation between pathway sections
"""

import streamlit as st

def render_section_divider():
    """
    Renders a subtle section divider
    """
    st.markdown('<div style="border-top: 2px solid #E1E8ED; margin: 3rem 0;"></div>', 
                unsafe_allow_html=True)

def render_section_header(title, icon=""):
    """
    Renders a consistent section header
    
    Args:
        title: Section title
        icon: Optional emoji icon
    """
    if icon:
        st.markdown(f'<p style="color: #4A90E2; font-size: 1.8rem; font-weight: 600; margin-bottom: 1rem;">{icon} {title}</p>', 
                    unsafe_allow_html=True)
    else:
        st.markdown(f'<p style="color: #4A90E2; font-size: 1.8rem; font-weight: 600; margin-bottom: 1rem;">{title}</p>', 
                    unsafe_allow_html=True)
