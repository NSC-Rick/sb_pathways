"""
Route Resolver
Validates and normalizes pathway/resource/tool routes
"""

from typing import Optional, Tuple
from pathway_config import CORE_PATHWAYS, SUPPLEMENTAL_PATHWAYS


class RouteResolver:
    """
    Validates and resolves route keys to ensure they exist
    Provides graceful fallback for invalid routes
    """
    
    @staticmethod
    def validate_pathway(pathway_key: str) -> Tuple[bool, Optional[str]]:
        """
        Validate a pathway key exists in CORE_PATHWAYS
        
        Args:
            pathway_key: The pathway key to validate
            
        Returns:
            Tuple of (is_valid, normalized_key)
        """
        # Normalize to lowercase with underscores
        normalized_key = pathway_key.lower().replace("-", "_").replace(" ", "_")
        
        if normalized_key in CORE_PATHWAYS:
            return True, normalized_key
        
        return False, None
    
    @staticmethod
    def validate_supplemental(supplemental_key: str) -> Tuple[bool, Optional[str]]:
        """
        Validate a supplemental pathway key exists in SUPPLEMENTAL_PATHWAYS
        
        Args:
            supplemental_key: The supplemental pathway key to validate
            
        Returns:
            Tuple of (is_valid, normalized_key)
        """
        normalized_key = supplemental_key.lower().replace("-", "_").replace(" ", "_")
        
        if normalized_key in SUPPLEMENTAL_PATHWAYS:
            return True, normalized_key
        
        return False, None
    
    @staticmethod
    def validate_tool(tool_key: str) -> Tuple[bool, Optional[str]]:
        """
        Validate a tool key (placeholder for future tools)
        
        Args:
            tool_key: The tool key to validate
            
        Returns:
            Tuple of (is_valid, normalized_key)
        """
        # TODO: Implement when tools are added
        # For now, all tools are invalid
        return False, None
    
    @staticmethod
    def validate_resource(resource_key: str) -> Tuple[bool, Optional[str]]:
        """
        Validate a resource key (placeholder for future resources)
        
        Args:
            resource_key: The resource key to validate
            
        Returns:
            Tuple of (is_valid, normalized_key)
        """
        # TODO: Implement when standalone resources are added
        # For now, all resources are invalid
        return False, None
    
    @staticmethod
    def get_pathway_metadata(pathway_key: str) -> Optional[dict]:
        """
        Get pathway metadata if key is valid
        
        Args:
            pathway_key: The pathway key
            
        Returns:
            Pathway metadata dict or None
        """
        is_valid, normalized_key = RouteResolver.validate_pathway(pathway_key)
        
        if is_valid:
            return CORE_PATHWAYS[normalized_key]
        
        return None
    
    @staticmethod
    def get_supplemental_metadata(supplemental_key: str) -> Optional[dict]:
        """
        Get supplemental pathway metadata if key is valid
        
        Args:
            supplemental_key: The supplemental pathway key
            
        Returns:
            Supplemental pathway metadata dict or None
        """
        is_valid, normalized_key = RouteResolver.validate_supplemental(supplemental_key)
        
        if is_valid:
            return SUPPLEMENTAL_PATHWAYS[normalized_key]
        
        return None
    
    @staticmethod
    def normalize_route_key(route_key: str) -> str:
        """
        Normalize a route key to standard format
        
        Args:
            route_key: Raw route key from URL or user input
            
        Returns:
            Normalized route key (lowercase, underscores)
        """
        return route_key.lower().replace("-", "_").replace(" ", "_")
    
    @staticmethod
    def is_valid_route(route_type: str, route_key: str) -> bool:
        """
        Check if a route is valid for a given type
        
        Args:
            route_type: One of "pathway", "supplemental", "tool", "resource"
            route_key: The route key to validate
            
        Returns:
            True if valid, False otherwise
        """
        if route_type == "pathway":
            is_valid, _ = RouteResolver.validate_pathway(route_key)
            return is_valid
        
        elif route_type == "supplemental":
            is_valid, _ = RouteResolver.validate_supplemental(route_key)
            return is_valid
        
        elif route_type == "tool":
            is_valid, _ = RouteResolver.validate_tool(route_key)
            return is_valid
        
        elif route_type == "resource":
            is_valid, _ = RouteResolver.validate_resource(route_key)
            return is_valid
        
        return False
