"""
Route Helpers
Utilities for generating deep links and navigation URLs
"""

from typing import Optional


def create_pathway_link(pathway_key: str, base_url: str = "") -> str:
    """
    Create a deep link to a pathway
    
    Args:
        pathway_key: The pathway identifier
        base_url: Optional base URL (for absolute links)
        
    Returns:
        Deep link URL string
        
    Example:
        create_pathway_link("idea_exploration")
        Returns: "?pathway=idea_exploration"
    """
    return f"{base_url}?pathway={pathway_key}"


def create_supplemental_link(supplemental_key: str, base_url: str = "") -> str:
    """
    Create a deep link to a supplemental pathway
    
    Args:
        supplemental_key: The supplemental pathway identifier
        base_url: Optional base URL
        
    Returns:
        Deep link URL string
    """
    return f"{base_url}?supplemental={supplemental_key}"


def create_tool_link(tool_key: str, base_url: str = "") -> str:
    """
    Create a deep link to a tool
    
    Args:
        tool_key: The tool identifier
        base_url: Optional base URL
        
    Returns:
        Deep link URL string
    """
    return f"{base_url}?tool={tool_key}"


def create_resource_link(resource_key: str, base_url: str = "") -> str:
    """
    Create a deep link to a resource
    
    Args:
        resource_key: The resource identifier
        base_url: Optional base URL
        
    Returns:
        Deep link URL string
    """
    return f"{base_url}?resource={resource_key}"


def create_home_link(base_url: str = "") -> str:
    """
    Create a link to the home page
    
    Args:
        base_url: Optional base URL
        
    Returns:
        Home page URL string
    """
    return base_url if base_url else "/"


def get_shareable_link(route_type: str, route_key: str, base_url: str = "") -> str:
    """
    Get a shareable deep link for any route type
    
    Args:
        route_type: One of "pathway", "supplemental", "tool", "resource", "home"
        route_key: The route identifier (ignored for home)
        base_url: Optional base URL for absolute links
        
    Returns:
        Shareable deep link URL
    """
    if route_type == "pathway":
        return create_pathway_link(route_key, base_url)
    elif route_type == "supplemental":
        return create_supplemental_link(route_key, base_url)
    elif route_type == "tool":
        return create_tool_link(route_key, base_url)
    elif route_type == "resource":
        return create_resource_link(route_key, base_url)
    else:
        return create_home_link(base_url)


def format_pathway_url_slug(pathway_name: str) -> str:
    """
    Convert a pathway name to a URL-friendly slug
    
    Args:
        pathway_name: Human-readable pathway name
        
    Returns:
        URL-friendly slug
        
    Example:
        format_pathway_url_slug("Idea Exploration")
        Returns: "idea_exploration"
    """
    return pathway_name.lower().replace(" ", "_").replace("-", "_").replace("&", "and")


def parse_query_param(param_value: Optional[str]) -> Optional[str]:
    """
    Parse and normalize a query parameter value
    
    Args:
        param_value: Raw query parameter value
        
    Returns:
        Normalized value or None
    """
    if not param_value:
        return None
    
    # Normalize to lowercase with underscores
    return param_value.lower().replace("-", "_").replace(" ", "_")
