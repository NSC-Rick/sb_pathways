"""
Reusable video resource list component
Displays educational videos as clean, curated resource items instead of embedded previews
"""

import streamlit as st


def render_video_resource_item(title, duration, description, youtube_url):
    """
    Render a single video resource item with title, duration, description, and link.
    
    Args:
        title (str): Video title
        duration (str): Video duration (e.g., "9 min")
        description (str): One-sentence description
        youtube_url (str): YouTube embed URL (will be converted to watch URL)
    """
    
    # Convert embed URL to watch URL
    if "/embed/" in youtube_url:
        video_id = youtube_url.split("/embed/")[-1].split("?")[0]
        watch_url = f"https://www.youtube.com/watch?v={video_id}"
    else:
        watch_url = youtube_url
    
    # Render resource item
    st.markdown(
        f"""
        <div style="
            background: #F7F9FC;
            border: 1px solid #E1E8ED;
            border-radius: 8px;
            padding: 1rem 1.25rem;
            margin-bottom: 1rem;
        ">
            <div style="display: flex; align-items: baseline; margin-bottom: 0.5rem;">
                <span style="color: #4A90E2; font-size: 1.1rem; margin-right: 0.5rem;">▶</span>
                <strong style="color: #2C3E50; font-size: 1rem;">{title}</strong>
                <span style="color: #7F8C8D; font-size: 0.9rem; margin-left: 0.5rem;">({duration})</span>
            </div>
            <p style="color: #5D6D7E; font-size: 0.95rem; margin: 0.5rem 0 0.75rem 1.6rem; line-height: 1.5;">
                {description}
            </p>
            <div style="margin-left: 1.6rem;">
                <a href="{watch_url}" target="_blank" style="
                    display: inline-block;
                    background-color: #FFFFFF;
                    color: #4A90E2;
                    border: 1px solid #4A90E2;
                    border-radius: 4px;
                    padding: 0.4rem 1rem;
                    font-size: 0.9rem;
                    font-weight: 500;
                    text-decoration: none;
                    transition: all 0.2s ease;
                ">
                    Watch Video →
                </a>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


def render_video_resource_list(videos):
    """
    Render a list of video resources.
    
    Args:
        videos (list): List of video dictionaries with keys:
            - title (str): Video title
            - duration (str): Video duration
            - description (str): One-sentence description
            - url (str): YouTube URL
    """
    
    for video in videos:
        render_video_resource_item(
            title=video.get("title", ""),
            duration=video.get("duration", ""),
            description=video.get("description", ""),
            youtube_url=video.get("url", "")
        )
