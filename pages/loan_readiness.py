import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Loan Readiness | Client Readiness Pathways",
    page_icon="💰",
    layout="wide"
)

# Apply consistent styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    
    .section-divider {
        border-top: 2px solid #E1E8ED;
        margin: 3rem 0;
    }
    
    .section-header {
        color: #4A90E2;
        font-size: 1.8rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    
    .video-placeholder {
        background-color: #F7F9FC;
        border: 2px dashed #4A90E2;
        border-radius: 8px;
        padding: 3rem;
        text-align: center;
        color: #7F8C8D;
        margin: 1rem 0;
    }
    
    .resource-box {
        background-color: #F7F9FC;
        border-left: 4px solid #4A90E2;
        padding: 1.5rem;
        margin: 1rem 0;
        border-radius: 4px;
    }
    
    .workbook-box {
        background-color: #E8F4F8;
        border: 1px solid #4A90E2;
        border-radius: 8px;
        padding: 2rem;
        margin: 1rem 0;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.title("💰 Loan Readiness Pathway")
st.markdown("**Prepare a compelling loan application with organized financials and clear business case.**")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Section 1: Welcome
st.markdown('<p class="section-header">Welcome</p>', unsafe_allow_html=True)

st.markdown("""
This pathway is designed for business owners who need financing and want to:
- Understand what lenders look for
- Organize financial documentation
- Build a strong business case
- Prepare for the application process

By completing this pathway, you'll arrive at your advisory meeting with organized materials 
and a clear understanding of your financing needs.
""")

# Video placeholder
st.markdown("""
<div class="video-placeholder">
    <h3>📹 Introduction Video</h3>
    <p>Video content will be embedded here</p>
    <p style="font-size: 0.9rem; margin-top: 1rem;">Duration: ~7 minutes</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Section 2: Learn
st.markdown('<p class="section-header">Learn</p>', unsafe_allow_html=True)

st.markdown("Review these resources to understand the loan application process and lender expectations.")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="resource-box">
        <h4>📚 Essential Reading</h4>
        <ul>
            <li>Understanding Loan Types and Terms</li>
            <li>What Lenders Look For</li>
            <li>Preparing Financial Statements</li>
            <li>Building Your Business Case</li>
        </ul>
        <p><em>Placeholder for resource links</em></p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="resource-box">
        <h4>🎥 Video Resources</h4>
        <ul>
            <li>Loan Application Overview (10 min)</li>
            <li>Financial Documentation Checklist (8 min)</li>
            <li>Common Application Mistakes (6 min)</li>
        </ul>
        <p><em>Placeholder for video links</em></p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Section 3: Work
st.markdown('<p class="section-header">Work</p>', unsafe_allow_html=True)

st.markdown("""
Complete the Loan Readiness Workbook to organize your financial information, clarify your needs, 
and prepare your business case. This workbook will help you identify any gaps before applying.
""")

st.markdown("""
<div class="workbook-box">
    <h3>📋 Loan Readiness Workbook</h3>
    <p>This workbook includes sections on:</p>
    <ul>
        <li>Loan amount and use of funds</li>
        <li>Financial history and projections</li>
        <li>Collateral and personal guarantees</li>
        <li>Business plan summary</li>
        <li>Document checklist</li>
    </ul>
    <p style="margin-top: 1.5rem;"><strong>Estimated time:</strong> 3-4 hours</p>
</div>
""", unsafe_allow_html=True)

st.button("📥 Download Workbook (PDF)", use_container_width=True, disabled=True)
st.caption("Workbook download will be available here")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Section 4: Submit
st.markdown('<p class="section-header">Submit</p>', unsafe_allow_html=True)

st.markdown("""
Once you've completed your workbook, submit it here along with any supporting financial documents. 
Your advisor will review everything before your meeting to provide targeted guidance.
""")

st.file_uploader("Upload completed workbook", type=['pdf', 'docx'], disabled=True)
st.caption("File upload functionality will be available here")

st.markdown("**Optional:** Upload supporting documents (financial statements, tax returns, etc.)")
st.file_uploader("Additional documents", type=['pdf', 'xlsx', 'docx'], accept_multiple_files=True, disabled=True)

st.text_area("Additional notes for your advisor", height=100, disabled=True,
             placeholder="e.g., I'm unsure about how to value my equipment for collateral...")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Section 5: Schedule
st.markdown('<p class="section-header">Schedule</p>', unsafe_allow_html=True)

st.markdown("""
Ready to meet with an advisor? Schedule your session below. We recommend completing all previous steps 
before scheduling to maximize the value of your meeting.
""")

st.info("✅ **Preparation Checklist:**\n- Reviewed learning resources\n- Completed workbook\n- Gathered financial documents\n- Submitted materials to advisor")

st.button("📅 Schedule Advisory Session", use_container_width=True, disabled=True)
st.caption("Scheduling integration will be available here")

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

# Navigation
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("← Back to Home", use_container_width=True):
        st.switch_page("app.py")
