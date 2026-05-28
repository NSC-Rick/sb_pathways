"""
Navigation Context Manager
Centralized navigation state management for the Pathways platform
"""

import streamlit as st
from typing import Optional, Dict, Any


class NavigationContext:
    """
    Manages navigation state, mode detection, and routing context
    Single source of truth for application navigation
    """
    
    # Navigation modes
    MODE_HOME = "home"
    MODE_PATHWAY = "pathway"
    MODE_SUPPLEMENTAL = "supplemental"
    MODE_TOOL = "tool"
    MODE_RESOURCE = "resource"
    MODE_INVALID = "invalid"
    
    def __init__(self):
        """Initialize navigation context from query params and session state"""
        self._initialize_session_state()
        self._sync_from_query_params()
    
    def _initialize_session_state(self):
        """Initialize session state variables if not present"""
        if "nav_context" not in st.session_state:
            st.session_state.nav_context = {
                "mode": self.MODE_HOME,
                "pathway": None,
                "supplemental": None,
                "tool": None,
                "resource": None,
                "sidebar_state": "expanded",
                "show_supplemental": False,
                "manual_sidebar_toggle": False
            }
    
    def _sync_from_query_params(self):
        """
        Sync navigation context from URL query parameters
        Query params take precedence over session state on initial load
        """
        query_params = st.query_params
        
        # Check if we have any navigation query params
        if "pathway" in query_params:
            pathway_key = query_params["pathway"]
            self.navigate_to_pathway(pathway_key, from_deep_link=True)
        
        elif "supplemental" in query_params:
            supplemental_key = query_params["supplemental"]
            self.navigate_to_supplemental(supplemental_key, from_deep_link=True)
        
        elif "tool" in query_params:
            tool_key = query_params["tool"]
            self.navigate_to_tool(tool_key, from_deep_link=True)
        
        elif "resource" in query_params:
            resource_key = query_params["resource"]
            self.navigate_to_resource(resource_key, from_deep_link=True)
        
        # If no query params and session state is home, ensure we're in home mode
        elif st.session_state.nav_context["mode"] == self.MODE_HOME:
            self._clear_query_params()
    
    def _clear_query_params(self):
        """Clear all navigation-related query parameters"""
        # Only clear if there are params to clear
        if len(st.query_params) > 0:
            st.query_params.clear()
    
    def navigate_to_pathway(self, pathway_key: str, from_deep_link: bool = False):
        """
        Navigate to a core pathway
        
        Args:
            pathway_key: The pathway identifier (e.g., "idea_exploration")
            from_deep_link: Whether navigation is from a deep link (affects sidebar state)
        """
        st.session_state.nav_context.update({
            "mode": self.MODE_PATHWAY,
            "pathway": pathway_key,
            "supplemental": None,
            "tool": None,
            "resource": None
        })
        
        # Set sidebar state based on navigation source
        if from_deep_link and not st.session_state.nav_context["manual_sidebar_toggle"]:
            st.session_state.nav_context["sidebar_state"] = "collapsed"
        
        # Update query params to reflect current state
        st.query_params["pathway"] = pathway_key
    
    def navigate_to_supplemental(self, supplemental_key: str, from_deep_link: bool = False):
        """
        Navigate to a supplemental pathway
        
        Args:
            supplemental_key: The supplemental pathway identifier
            from_deep_link: Whether navigation is from a deep link
        """
        st.session_state.nav_context.update({
            "mode": self.MODE_SUPPLEMENTAL,
            "pathway": None,
            "supplemental": supplemental_key,
            "tool": None,
            "resource": None,
            "show_supplemental": True  # Auto-expand supplemental section
        })
        
        if from_deep_link and not st.session_state.nav_context["manual_sidebar_toggle"]:
            st.session_state.nav_context["sidebar_state"] = "collapsed"
        
        st.query_params["supplemental"] = supplemental_key
    
    def navigate_to_tool(self, tool_key: str, from_deep_link: bool = False):
        """Navigate to a tool"""
        st.session_state.nav_context.update({
            "mode": self.MODE_TOOL,
            "pathway": None,
            "supplemental": None,
            "tool": tool_key,
            "resource": None
        })
        
        if from_deep_link and not st.session_state.nav_context["manual_sidebar_toggle"]:
            st.session_state.nav_context["sidebar_state"] = "collapsed"
        
        st.query_params["tool"] = tool_key
    
    def navigate_to_resource(self, resource_key: str, from_deep_link: bool = False):
        """Navigate to a resource"""
        st.session_state.nav_context.update({
            "mode": self.MODE_RESOURCE,
            "pathway": None,
            "supplemental": None,
            "tool": None,
            "resource": resource_key
        })
        
        if from_deep_link and not st.session_state.nav_context["manual_sidebar_toggle"]:
            st.session_state.nav_context["sidebar_state"] = "collapsed"
        
        st.query_params["resource"] = resource_key
    
    def navigate_to_home(self):
        """Navigate to home page"""
        st.session_state.nav_context.update({
            "mode": self.MODE_HOME,
            "pathway": None,
            "supplemental": None,
            "tool": None,
            "resource": None,
            "sidebar_state": "expanded",
            "manual_sidebar_toggle": False
        })
        
        self._clear_query_params()
    
    def toggle_sidebar(self):
        """
        Toggle sidebar state manually
        Sets manual_sidebar_toggle flag to preserve user preference
        """
        current_state = st.session_state.nav_context["sidebar_state"]
        new_state = "collapsed" if current_state == "expanded" else "expanded"
        
        st.session_state.nav_context["sidebar_state"] = new_state
        st.session_state.nav_context["manual_sidebar_toggle"] = True
    
    def toggle_supplemental_section(self):
        """Toggle the supplemental pathways section in sidebar"""
        current = st.session_state.nav_context["show_supplemental"]
        st.session_state.nav_context["show_supplemental"] = not current
    
    @property
    def mode(self) -> str:
        """Get current navigation mode"""
        return st.session_state.nav_context["mode"]
    
    @property
    def current_pathway(self) -> Optional[str]:
        """Get current pathway key"""
        return st.session_state.nav_context["pathway"]
    
    @property
    def current_supplemental(self) -> Optional[str]:
        """Get current supplemental pathway key"""
        return st.session_state.nav_context["supplemental"]
    
    @property
    def current_tool(self) -> Optional[str]:
        """Get current tool key"""
        return st.session_state.nav_context["tool"]
    
    @property
    def current_resource(self) -> Optional[str]:
        """Get current resource key"""
        return st.session_state.nav_context["resource"]
    
    @property
    def sidebar_state(self) -> str:
        """Get current sidebar state"""
        return st.session_state.nav_context["sidebar_state"]
    
    @property
    def show_supplemental(self) -> bool:
        """Get supplemental section visibility"""
        return st.session_state.nav_context["show_supplemental"]
    
    @property
    def active_page_key(self) -> str:
        """
        Get the active page key regardless of mode
        Returns the appropriate key based on current mode
        """
        if self.mode == self.MODE_PATHWAY:
            return self.current_pathway
        elif self.mode == self.MODE_SUPPLEMENTAL:
            return self.current_supplemental
        elif self.mode == self.MODE_TOOL:
            return self.current_tool
        elif self.mode == self.MODE_RESOURCE:
            return self.current_resource
        else:
            return "home"
    
    def is_active(self, page_key: str) -> bool:
        """
        Check if a given page key is currently active
        Used for sidebar highlighting
        """
        return self.active_page_key == page_key
    
    def get_context_dict(self) -> Dict[str, Any]:
        """Get full navigation context as dictionary"""
        return st.session_state.nav_context.copy()


def get_navigation_context() -> NavigationContext:
    """
    Factory function to get or create navigation context
    Use this to access navigation context throughout the app
    """
    return NavigationContext()
