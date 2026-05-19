"""
Reusable footer component
Displays consistent footer across all pages
"""

import streamlit as st
from pathway_config import APP_FOOTER_TEXT

def render_footer():
    """
    Renders the application footer with consistent styling
    """
    st.markdown('<div style="border-top: 1px solid #E1E8ED; margin-top: 3rem; padding-top: 2rem;"></div>', 
                unsafe_allow_html=True)
    
    st.markdown(f"""
    <div style="text-align: center; color: #7F8C8D; font-size: 0.9rem; padding: 1rem 0;">
        {APP_FOOTER_TEXT}
    </div>
    """, unsafe_allow_html=True)
