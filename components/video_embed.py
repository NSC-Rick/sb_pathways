"""
Shared video embed component with improved framing and responsive design
Provides consistent, calm, and intentional video presentation across all pathways
"""

import streamlit as st


def render_video_embed(video_url, title=None, subtitle=None, max_width=750):
    """
    Render an embedded video with improved framing and responsive design.
    
    Args:
        video_url (str): URL of the video to embed
        title (str, optional): Title to display above the video
        subtitle (str, optional): Supportive text to display below the video
        max_width (int, optional): Maximum width of the video container in pixels (default: 750)
    """
    
    if not video_url:
        return
    
    # Title section (if provided)
    if title:
        st.markdown(f"### {title}")
    
    # Responsive video container with improved framing
    # Uses centered layout with max-width constraint and soft styling
    video_html = f"""
    <style>
        .video-container {{
            max-width: {max_width}px;
            margin: 1.5rem auto;
            padding: 0;
        }}
        
        .video-wrapper {{
            background: #FFFFFF;
            border: 1px solid #E1E8ED;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}
        
        .video-frame {{
            position: relative;
            width: 100%;
            padding-bottom: 56.25%; /* 16:9 aspect ratio fallback */
            height: 0;
            overflow: hidden;
            border-radius: 8px;
            background: #F7F9FC;
        }}
        
        .video-frame iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
        
        .video-subtitle {{
            text-align: center;
            color: #7F8C8D;
            font-size: 0.9rem;
            margin-top: 1rem;
            font-style: italic;
        }}
        
        /* Mobile responsiveness */
        @media (max-width: 768px) {{
            .video-container {{
                max-width: 100%;
                margin: 1rem auto;
            }}
            
            .video-wrapper {{
                padding: 0.75rem;
            }}
        }}
    </style>
    
    <div class="video-container">
        <div class="video-wrapper">
            <div class="video-frame">
                <iframe 
                    src="{video_url}"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    loading="lazy">
                </iframe>
            </div>
        </div>
    </div>
    """
    
    # Render the video
    st.components.v1.html(video_html, height=500)
    
    # Subtitle section (if provided)
    if subtitle:
        st.markdown(f'<p class="video-subtitle">{subtitle}</p>', unsafe_allow_html=True)


def render_video_section(video_url, section_title="Introduction", 
                         intro_text=None, subtitle=None, max_width=750):
    """
    Render a complete video section with title, intro text, video, and subtitle.
    
    Args:
        video_url (str): URL of the video to embed
        section_title (str): Section header (default: "Introduction")
        intro_text (str, optional): Supportive text before the video
        subtitle (str, optional): Supportive text after the video
        max_width (int): Maximum width of the video container in pixels
    """
    
    # Section header
    st.markdown(f"### {section_title}")
    
    # Intro text
    if intro_text:
        st.caption(intro_text)
    else:
        st.caption("Start with a short introduction to this pathway before moving into the preparation materials.")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Embedded video
    render_video_embed(
        video_url=video_url,
        title=None,  # Title already shown above
        subtitle=subtitle,
        max_width=max_width
    )
    
    st.markdown("<br>", unsafe_allow_html=True)


def render_adaptive_video(video_url, aspect_ratio="16:9", max_width=750):
    """
    Render a video with adaptive aspect ratio handling.
    
    Args:
        video_url (str): URL of the video to embed
        aspect_ratio (str): Aspect ratio as "width:height" (e.g., "16:9", "4:3", "1:1")
        max_width (int): Maximum width of the video container in pixels
    """
    
    if not video_url:
        return
    
    # Calculate padding-bottom percentage based on aspect ratio
    try:
        width, height = map(int, aspect_ratio.split(':'))
        padding_bottom = (height / width) * 100
    except:
        padding_bottom = 56.25  # Default to 16:9
    
    video_html = f"""
    <style>
        .adaptive-video-container {{
            max-width: {max_width}px;
            margin: 1.5rem auto;
            padding: 0;
        }}
        
        .adaptive-video-wrapper {{
            background: #FFFFFF;
            border: 1px solid #E1E8ED;
            border-radius: 12px;
            padding: 1rem;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
        }}
        
        .adaptive-video-frame {{
            position: relative;
            width: 100%;
            padding-bottom: {padding_bottom}%;
            height: 0;
            overflow: hidden;
            border-radius: 8px;
            background: #F7F9FC;
        }}
        
        .adaptive-video-frame iframe {{
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            border: none;
        }}
        
        @media (max-width: 768px) {{
            .adaptive-video-container {{
                max-width: 100%;
                margin: 1rem auto;
            }}
            
            .adaptive-video-wrapper {{
                padding: 0.75rem;
            }}
        }}
    </style>
    
    <div class="adaptive-video-container">
        <div class="adaptive-video-wrapper">
            <div class="adaptive-video-frame">
                <iframe 
                    src="{video_url}"
                    frameborder="0"
                    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                    allowfullscreen
                    loading="lazy">
                </iframe>
            </div>
        </div>
    </div>
    """
    
    st.components.v1.html(video_html, height=int((max_width * padding_bottom / 100) + 50))
