import streamlit as st
from pathway_config import PATHWAYS
from components.footer import render_footer

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

# Sidebar navigation with improved structure
with st.sidebar:
    st.title("🎯 Client Pathways")
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    # Home button
    if st.button("🏠 Home", use_container_width=True, key="nav_home"):
        st.switch_page("app.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("**Choose Your Pathway**")
    
    # Pathway buttons using config
    for pathway_key, pathway_data in PATHWAYS.items():
        button_label = f"{pathway_data['icon']} {pathway_data['name']}"
        if st.button(button_label, use_container_width=True, key=f"nav_{pathway_key}"):
            st.switch_page(pathway_data['page_file'])
    
    st.markdown('<div class="sidebar-divider"></div>', unsafe_allow_html=True)
    
    st.markdown("**About**")
    st.caption("These pathways help you prepare for meaningful advisory conversations through structured guidance and reflection.")

# Main content
st.title("Client Readiness Pathways")
st.markdown('<p class="subtitle">Structured preparation before meaningful advising.</p>', unsafe_allow_html=True)

st.markdown("---")

# Introduction
st.markdown("""
Welcome to the Client Readiness Pathways system. This platform helps you prepare for your advisory meeting 
by guiding you through structured learning, reflection, and planning activities.

Each pathway is designed to help you arrive at your meeting with clarity, focus, and actionable questions.
""")

st.markdown("## Choose Your Pathway")

# Pathway cards in two columns using config
col1, col2 = st.columns(2)

pathway_list = list(PATHWAYS.items())

# First column: Idea Exploration and Recovery
with col1:
    for pathway_key in ["idea_exploration", "recovery_stabilization"]:
        pathway = PATHWAYS[pathway_key]
        st.markdown(f"""
        <div class="pathway-card">
            <h3>{pathway['icon']} {pathway['name']}</h3>
            <p>{pathway['short_description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Start {pathway['name']}", key=f"start_{pathway_key}", use_container_width=True):
            st.switch_page(pathway['page_file'])
        
        st.markdown("<br>", unsafe_allow_html=True)

# Second column: Loan Readiness and Business Transition
with col2:
    for pathway_key in ["loan_readiness", "business_transition"]:
        pathway = PATHWAYS[pathway_key]
        st.markdown(f"""
        <div class="pathway-card">
            <h3>{pathway['icon']} {pathway['name']}</h3>
            <p>{pathway['short_description']}</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button(f"Start {pathway['name']}", key=f"start_{pathway_key}", use_container_width=True):
            st.switch_page(pathway['page_file'])
        
        st.markdown("<br>", unsafe_allow_html=True)

st.markdown("---")

# Footer information
st.markdown("""
### How It Works

Each pathway follows a structured approach:

1. **Business Basics** – Review foundational concepts to build shared understanding
2. **Learn** – Access curated resources and guidance specific to your situation
3. **Work** – Complete a focused workbook to organize your thoughts and data
4. **Submit** – Share your completed work with your advisor before the meeting
5. **Schedule** – Book your advisory session when you're ready

This approach ensures your time with an advisor is focused on strategy, problem-solving, and action planning 
rather than basic information gathering.
""")

# Footer
render_footer()
