import streamlit as st
from pathway_config import PATHWAYS
from components.footer import render_footer

# Import view rendering functions
from views.home import render_home
from views.idea_exploration import render_idea_exploration
from views.loan_readiness import render_loan_readiness
from views.recovery_stabilization import render_recovery_stabilization
from views.business_transition import render_business_transition

# Page configuration
st.set_page_config(
    page_title="Client Readiness Pathways",
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

# Initialize session state for navigation
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Sidebar navigation with clean unbranded structure
with st.sidebar:
    # Header
    st.title("🎯 Client Pathways")
    st.caption("Prepare. Focus. Move Forward.")
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    # Home button
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        st.session_state.current_page = "home"
        st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Pathway buttons using config
    for pathway_key, pathway_data in PATHWAYS.items():
        button_label = f"{pathway_data['icon']} {pathway_data['name']}"
        if st.button(button_label, use_container_width=True, key=f"nav_{pathway_key}"):
            st.session_state.current_page = pathway_key
            st.rerun()
    
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    # Support card
    st.markdown("**What Are Pathways?**")
    st.caption("Pathways guide you through structured steps to help you prepare for a more productive advisory meeting.")
    
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    # Footer note
    st.caption("Thoughtful preparation before meaningful advising.")

# Route to appropriate view based on session state
if st.session_state.current_page == "home":
    render_home()
elif st.session_state.current_page == "idea_exploration":
    render_idea_exploration()
elif st.session_state.current_page == "loan_readiness":
    render_loan_readiness()
elif st.session_state.current_page == "recovery_stabilization":
    render_recovery_stabilization()
elif st.session_state.current_page == "business_transition":
    render_business_transition()
else:
    # Fallback to home if unknown page
    st.session_state.current_page = "home"
    render_home()
