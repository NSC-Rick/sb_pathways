"""
Reusable resource card components
Creates consistent cards for videos, worksheets, downloads, and articles
"""

import streamlit as st

def render_resource_card(title, description, card_type="info", items=None):
    """
    Renders a resource card with consistent styling
    
    Args:
        title: Card title
        description: Optional description text
        card_type: Type of card (info, video, download, article)
        items: Optional list of items to display
    """
    # Icon based on card type
    icons = {
        "info": "📚",
        "video": "🎥",
        "download": "📥",
        "article": "📄"
    }
    
    icon = icons.get(card_type, "📚")
    
    card_html = f"""
    <div style="background-color: #F7F9FC; border-left: 4px solid #4A90E2; 
                padding: 1.5rem; margin: 1rem 0; border-radius: 4px;">
        <h4 style="margin-top: 0; color: #2C3E50;">{icon} {title}</h4>
    """
    
    if description:
        card_html += f'<p style="color: #7F8C8D; margin-bottom: 0.5rem;">{description}</p>'
    
    if items:
        card_html += '<ul style="margin-top: 0.5rem;">'
        for item in items:
            card_html += f'<li>{item}</li>'
        card_html += '</ul>'
    
    card_html += '<p style="margin-top: 1rem; margin-bottom: 0;"><em>Placeholder for resource links</em></p>'
    card_html += '</div>'
    
    st.markdown(card_html, unsafe_allow_html=True)

def render_video_placeholder(title, duration="5 minutes"):
    """
    Renders a video placeholder with consistent styling
    
    Args:
        title: Video title
        duration: Video duration
    """
    st.markdown(f"""
    <div style="background-color: #F7F9FC; border: 2px dashed #4A90E2; 
                border-radius: 8px; padding: 3rem; text-align: center; 
                color: #7F8C8D; margin: 1rem 0;">
        <h3 style="color: #4A90E2;">📹 {title}</h3>
        <p>Video content will be embedded here</p>
        <p style="font-size: 0.9rem; margin-top: 1rem;">Duration: ~{duration}</p>
    </div>
    """, unsafe_allow_html=True)

def render_workbook_card(workbook_name, sections, estimated_time):
    """
    Renders a workbook card with consistent styling
    
    Args:
        workbook_name: Name of the workbook
        sections: List of workbook sections
        estimated_time: Estimated completion time
    """
    st.markdown(f"""
    <div style="background-color: #E8F4F8; border: 1px solid #4A90E2; 
                border-radius: 8px; padding: 2rem; margin: 1rem 0;">
        <h3 style="color: #2C3E50; margin-top: 0;">📋 {workbook_name}</h3>
        <p style="color: #7F8C8D;">This workbook includes sections on:</p>
        <ul style="color: #2C3E50;">
    """, unsafe_allow_html=True)
    
    for section in sections:
        st.markdown(f"<li>{section}</li>", unsafe_allow_html=True)
    
    st.markdown(f"""
        </ul>
        <p style="margin-top: 1.5rem; color: #7F8C8D;">
            <strong>Estimated time:</strong> {estimated_time}
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_expandable_topic(icon, title, description):
    """
    Renders an expandable topic card (for Business Basics)
    
    Args:
        icon: Emoji icon
        title: Topic title
        description: Topic description
    """
    with st.expander(f"{icon} {title}"):
        st.markdown(description)
        st.markdown("---")
        st.caption("📹 Video resource placeholder")
        st.caption("📄 Article resource placeholder")
