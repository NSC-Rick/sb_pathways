"""
Reusable schedule section component
Displays consistent scheduling section across all pathways
"""

import streamlit as st

def render_schedule_section():
    """
    Renders the scheduling section with preparation checklist and Microsoft Bookings link
    """
    st.markdown("""
    When you're ready, schedule your advisory session to review your pathway materials and next steps.
    """)
    
    st.info("""
    ✅ **Preparation Checklist:**
    - Reviewed learning resources
    - Completed workbook
    - Submitted materials to advisor
    - Identified key questions
    """)
    
    # Microsoft Bookings scheduling link
    booking_url = "https://outlook.office.com/book/ScheduleameetingwithRick@livevsc.onmicrosoft.com/"
    
    st.markdown(
        f'<a href="{booking_url}" target="_blank" style="text-decoration: none;">'
        f'<button style="'
        f'background-color: #4A90E2; '
        f'color: white; '
        f'border: none; '
        f'border-radius: 6px; '
        f'padding: 0.5rem 2rem; '
        f'font-weight: 500; '
        f'font-size: 1rem; '
        f'width: 100%; '
        f'cursor: pointer; '
        f'transition: all 0.3s ease; '
        f'">'
        f'📅 Schedule Your Advisory Meeting'
        f'</button></a>',
        unsafe_allow_html=True
    )
    
    st.markdown("<br>", unsafe_allow_html=True)
