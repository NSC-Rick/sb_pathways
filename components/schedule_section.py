"""
Reusable schedule section component
Displays consistent scheduling section across all pathways
"""

import streamlit as st

def render_schedule_section():
    """
    Renders the scheduling section with preparation checklist
    """
    st.markdown("""
    Ready to meet with an advisor? Schedule your session below. We recommend completing all previous steps 
    before scheduling to maximize the value of your meeting.
    """)
    
    st.info("""
    ✅ **Preparation Checklist:**
    - Reviewed learning resources
    - Completed workbook
    - Submitted materials to advisor
    - Identified key questions
    """)
    
    st.button("📅 Schedule Advisory Session", use_container_width=True, disabled=True)
    st.caption("Scheduling integration will be available here")
