import streamlit as st
from pathway_config import PATHWAYS
from components.footer import render_footer

# Import view rendering functions
from views.home import render_home
from views.idea_exploration import render_idea_exploration
from views.loan_readiness import render_loan_readiness
from views.recovery_stabilization import render_recovery_stabilization
from views.business_transition import render_business_transition
from views.pathway_placeholder import render_pathway_placeholder

# Import navigation context layer
from src.core import get_navigation_context, SidebarController, RouteResolver

# Page configuration
st.set_page_config(
    page_title="Small Business Pathways",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for calm, professional styling with mobile responsiveness
st.markdown("""
    <style>
    /* Hide Streamlit default navigation */
    [data-testid="stSidebarNav"] {
        display: none;
    }
    
    /* Main content area */
    .main {
        padding: 2rem;
    }
    
    /* Pathway card styling */
    .pathway-card {
        background-color: #F7F9FC;
        border: 1px solid #E1E8ED;
        border-radius: 12px;
        padding: 2rem;
        margin: 1rem 0;
        transition: all 0.3s ease;
    }
    
    .pathway-card:hover {
        border-color: #4A90E2;
        box-shadow: 0 4px 12px rgba(74, 144, 226, 0.1);
    }
    
    /* Typography */
    h1 {
        color: #2C3E50;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    
    h2 {
        color: #34495E;
        font-weight: 500;
        margin-top: 2rem;
    }
    
    h3 {
        color: #4A90E2;
        font-weight: 500;
        margin-bottom: 0.5rem;
    }
    
    /* Subtitle styling */
    .subtitle {
        color: #7F8C8D;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #4A90E2;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 2rem;
        font-weight: 500;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #357ABD;
        box-shadow: 0 2px 8px rgba(74, 144, 226, 0.3);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #F7F9FC;
    }
    
    /* Sidebar section divider */
    .sidebar-divider {
        border-top: 1px solid #E1E8ED;
        margin: 1rem 0;
    }
    
    /* Remove extra padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    
    /* Mobile responsiveness */
    @media (max-width: 768px) {
        .main {
            padding: 1rem;
        }
        
        .pathway-card {
            padding: 1.5rem;
        }
        
        h1 {
            font-size: 1.8rem;
        }
        
        .subtitle {
            font-size: 1rem;
        }
        
        .block-container {
            padding-top: 2rem;
            padding-bottom: 2rem;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Initialize navigation context (handles query params and session state)
nav_context = get_navigation_context()

# Render sidebar using SidebarController
sidebar_controller = SidebarController(nav_context)
sidebar_controller.render_sidebar()

# Route to appropriate view based on navigation context
if nav_context.mode == "home":
    render_home()

elif nav_context.mode == "pathway":
    pathway_key = nav_context.current_pathway
    
    # Validate pathway exists
    is_valid, normalized_key = RouteResolver.validate_pathway(pathway_key)
    
    if not is_valid:
        # Invalid pathway - show error and redirect to home
        st.error(f"⚠️ Pathway '{pathway_key}' not found.")
        st.info("Redirecting to home page...")
        if st.button("← Return to Home", width="stretch"):
            nav_context.navigate_to_home()
            st.rerun()
    else:
        # Render appropriate pathway view
        if normalized_key == "idea_exploration":
            render_idea_exploration()
        elif normalized_key == "loan_readiness":
            render_loan_readiness()
        elif normalized_key == "recovery_stabilization":
            render_recovery_stabilization()
        elif normalized_key == "business_transition":
            render_business_transition()
        else:
            # Placeholder view for pathways not yet fully built
            pathway = PATHWAYS[normalized_key]
            render_pathway_placeholder(
                pathway["name"],
                pathway["icon"],
                pathway["short_description"],
                pathway["estimated_time"]
            )

elif nav_context.mode == "supplemental":
    supplemental_key = nav_context.current_supplemental
    
    # Validate supplemental pathway exists
    is_valid, normalized_key = RouteResolver.validate_supplemental(supplemental_key)
    
    if not is_valid:
        # Invalid supplemental pathway
        st.error(f"⚠️ Supplemental pathway '{supplemental_key}' not found.")
        st.info("Redirecting to home page...")
        if st.button("← Return to Home", width="stretch"):
            nav_context.navigate_to_home()
            st.rerun()
    else:
        # Render supplemental pathway (all use placeholder for now)
        pathway = PATHWAYS[normalized_key]
        render_pathway_placeholder(
            pathway["name"],
            pathway["icon"],
            pathway["short_description"],
            pathway["estimated_time"]
        )

elif nav_context.mode == "tool":
    # Tools not yet implemented
    st.error("⚠️ Tools are not yet available.")
    st.info("This feature is coming soon!")
    if st.button("← Return to Home", width="stretch"):
        nav_context.navigate_to_home()
        st.rerun()

elif nav_context.mode == "resource":
    # Resources not yet implemented
    st.error("⚠️ Resources are not yet available.")
    st.info("This feature is coming soon!")
    if st.button("← Return to Home", width="stretch"):
        nav_context.navigate_to_home()
        st.rerun()

else:
    # Fallback to home for any unknown mode
    render_home()
