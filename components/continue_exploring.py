"""
Continue Exploring component
Displays related pathway recommendations at the bottom of pathway pages
"""

import streamlit as st
from pathway_relationships import PATHWAY_RELATIONSHIPS
from src.core import get_navigation_context
from pathway_config import CORE_PATHWAYS, SUPPLEMENTAL_PATHWAYS


def render_continue_exploring(current_pathway_key):
    """
    Render the "Continue Exploring" section with related pathway recommendations
    
    Args:
        current_pathway_key: The key of the current pathway (e.g., "idea_exploration")
    """
    nav_context = get_navigation_context()
    
    # Get related pathways for current pathway
    related_pathways = PATHWAY_RELATIONSHIPS.get(current_pathway_key, [])
    
    # Only render if there are related pathways
    if not related_pathways:
        return
    
    # Section header
    st.markdown("### Continue Exploring")
    st.markdown("Businesses exploring this pathway also often explore:")
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display related pathways in columns (3 per row)
    num_pathways = len(related_pathways)
    
    if num_pathways == 1:
        cols = st.columns(1)
    elif num_pathways == 2:
        cols = st.columns(2)
    else:
        cols = st.columns(3)
    
    for idx, pathway in enumerate(related_pathways):
        col_idx = idx % len(cols)
        
        with cols[col_idx]:
            # Create clickable pathway card
            pathway_label = f"{pathway['icon']} {pathway['name']}"
            
            if st.button(
                pathway_label,
                key=f"continue_exploring_{current_pathway_key}_{pathway['key']}",
                width="stretch"
            ):
                # Navigate to the related pathway
                # Determine if it's core or supplemental
                if pathway['key'] in CORE_PATHWAYS:
                    nav_context.navigate_to_pathway(pathway['key'])
                elif pathway['key'] in SUPPLEMENTAL_PATHWAYS:
                    nav_context.navigate_to_supplemental(pathway['key'])
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
