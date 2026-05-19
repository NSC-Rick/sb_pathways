import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Client Readiness Pathways",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for calm, professional styling
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
    
    /* Remove extra padding */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
with st.sidebar:
    st.title("🎯 Navigation")
    st.markdown("---")
    
    st.markdown("### Pathways")
    
    if st.button("🏠 Home", use_container_width=True):
        st.switch_page("app.py")
    
    if st.button("💡 Idea Exploration", use_container_width=True):
        st.switch_page("pages/idea_exploration.py")
    
    if st.button("💰 Loan Readiness", use_container_width=True):
        st.switch_page("pages/loan_readiness.py")
    
    if st.button("🛟 Recovery & Stabilization", use_container_width=True):
        st.switch_page("pages/recovery_stabilization.py")
    
    if st.button("🔄 Business Transition", use_container_width=True):
        st.switch_page("pages/business_transition.py")
    
    st.markdown("---")
    st.markdown("### About")
    st.caption("Client Readiness Pathways helps you prepare for meaningful advisory conversations through structured guidance and resources.")

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

# Pathway cards in two columns
col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="pathway-card">
        <h3>💡 Idea Exploration</h3>
        <p>You have a business idea but need help clarifying your concept, validating market fit, 
        and understanding next steps.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Idea Exploration", key="idea", use_container_width=True):
        st.switch_page("pages/idea_exploration.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pathway-card">
        <h3>🛟 Recovery & Stabilization</h3>
        <p>Your business is facing challenges and you need guidance on stabilizing operations, 
        managing cash flow, or pivoting strategy.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Recovery & Stabilization", key="recovery", use_container_width=True):
        st.switch_page("pages/recovery_stabilization.py")

with col2:
    st.markdown("""
    <div class="pathway-card">
        <h3>💰 Loan Readiness</h3>
        <p>You need financing for your business and want to prepare a strong application with 
        clear financials and a compelling case.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Loan Readiness", key="loan", use_container_width=True):
        st.switch_page("pages/loan_readiness.py")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="pathway-card">
        <h3>🔄 Business Transition</h3>
        <p>You're considering selling, transferring ownership, or closing your business and 
        need structured guidance through the process.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("Start Business Transition", key="transition", use_container_width=True):
        st.switch_page("pages/business_transition.py")

st.markdown("---")

# Footer information
st.markdown("""
### How It Works

Each pathway follows a structured approach:

1. **Learn** – Access curated resources and guidance specific to your situation
2. **Work** – Complete a focused workbook to organize your thoughts and data
3. **Submit** – Share your completed work with your advisor before the meeting
4. **Schedule** – Book your advisory session when you're ready

This approach ensures your time with an advisor is focused on strategy, problem-solving, and action planning 
rather than basic information gathering.
""")
