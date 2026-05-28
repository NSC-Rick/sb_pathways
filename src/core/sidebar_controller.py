"""
Sidebar Controller
Manages sidebar rendering, highlighting, and behavior
"""

import streamlit as st
from typing import Optional
from pathway_config import CORE_PATHWAYS, SUPPLEMENTAL_PATHWAYS


class SidebarController:
    """
    Controls sidebar rendering and behavior
    Handles active route highlighting and section expansion
    """
    
    def __init__(self, nav_context):
        """
        Initialize sidebar controller with navigation context
        
        Args:
            nav_context: NavigationContext instance
        """
        self.nav_context = nav_context
    
    def render_sidebar(self):
        """Render the complete sidebar navigation"""
        with st.sidebar:
            self._render_header()
            self._render_home_button()
            self._render_divider()
            self._render_core_pathways()
            self._render_divider()
            self._render_supplemental_section()
            self._render_divider()
            self._render_info_card()
            self._render_divider()
            self._render_footer()
    
    def _render_header(self):
        """Render sidebar header"""
        st.title("🎯 Small Business Pathways")
        st.caption("Prepare. Focus. Move Forward.")
    
    def _render_divider(self):
        """Render section divider"""
        st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    def _render_home_button(self):
        """Render home navigation button"""
        # Highlight if on home page
        button_type = "primary" if self.nav_context.mode == "home" else "secondary"
        
        if st.button("🏠 Home", width="stretch", key="nav_home", type=button_type):
            self.nav_context.navigate_to_home()
            st.rerun()
    
    def _render_core_pathways(self):
        """Render core pathways section"""
        st.markdown("**Core Pathways**")
        st.markdown("<br>", unsafe_allow_html=True)
        
        for pathway_key, pathway_data in CORE_PATHWAYS.items():
            self._render_pathway_button(pathway_key, pathway_data, is_core=True)
    
    def _render_supplemental_section(self):
        """Render collapsible supplemental pathways section"""
        # Toggle button
        toggle_icon = "▼" if self.nav_context.show_supplemental else "▶"
        
        if st.button(
            f"{toggle_icon} Supplemental Pathways",
            width="stretch",
            key="toggle_supplemental"
        ):
            self.nav_context.toggle_supplemental_section()
            st.rerun()
        
        # Show supplemental pathways if expanded
        if self.nav_context.show_supplemental:
            st.markdown("<br>", unsafe_allow_html=True)
            for pathway_key, pathway_data in SUPPLEMENTAL_PATHWAYS.items():
                self._render_pathway_button(pathway_key, pathway_data, is_core=False)
    
    def _render_pathway_button(self, pathway_key: str, pathway_data: dict, is_core: bool):
        """
        Render a pathway navigation button
        
        Args:
            pathway_key: The pathway identifier
            pathway_data: Pathway metadata
            is_core: Whether this is a core pathway
        """
        button_label = f"{pathway_data['icon']} {pathway_data['name']}"
        
        # Highlight if this pathway is active
        is_active = self.nav_context.is_active(pathway_key)
        button_type = "primary" if is_active else "secondary"
        
        if st.button(
            button_label,
            width="stretch",
            key=f"nav_{pathway_key}",
            type=button_type
        ):
            if is_core:
                self.nav_context.navigate_to_pathway(pathway_key)
            else:
                self.nav_context.navigate_to_supplemental(pathway_key)
            st.rerun()
    
    def _render_info_card(self):
        """Render informational card"""
        st.markdown("**What Are Pathways?**")
        st.caption(
            "Pathways guide you through structured steps to help you prepare "
            "for a more productive advisory meeting."
        )
    
    def _render_footer(self):
        """Render sidebar footer"""
        st.caption("Thoughtful preparation before meaningful advising.")
    
    def get_active_pathway_name(self) -> Optional[str]:
        """
        Get the name of the currently active pathway
        
        Returns:
            Pathway name or None
        """
        active_key = self.nav_context.active_page_key
        
        if active_key in CORE_PATHWAYS:
            return CORE_PATHWAYS[active_key]["name"]
        elif active_key in SUPPLEMENTAL_PATHWAYS:
            return SUPPLEMENTAL_PATHWAYS[active_key]["name"]
        
        return None
    
    def should_auto_expand_supplemental(self) -> bool:
        """
        Determine if supplemental section should auto-expand
        
        Returns:
            True if should expand, False otherwise
        """
        # Auto-expand if current page is a supplemental pathway
        return self.nav_context.mode == "supplemental"
