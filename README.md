# Small Business Pathways

A lightweight, unbranded Streamlit prototype designed to help small business owners prepare for meaningful advisory meetings through structured learning, reflection, worksheets, and pathway-specific preparation.

## Overview

Small Business Pathways is a web application that guides entrepreneurs and business owners through structured preparation before meeting with business advisors. The system improves meeting quality by ensuring clients arrive with clarity, organized information, and focused questions.

## Pathway Philosophy

### What This Is
- A guided advisory preparation framework
- A structured learning and reflection tool
- A way to improve advisor meeting quality
- A system to reduce repetitive intake conversations

### What This Is Not
- Not a Learning Management System (LMS)
- Not a Customer Relationship Management (CRM) system
- Not a client portal
- Not an AI-heavy platform

### Core Principles
- **Human-centered**: Supportive, calm, and emotionally intelligent
- **Simplicity over complexity**: Minimal, focused, and clear
- **Structure enables scale**: Reusable architecture for future pathways
- **Preparation improves outcomes**: Better meetings through better preparation

## Available Pathways (V1)

### 💡 Idea Exploration
For entrepreneurs with business concepts who need help clarifying, validating, and planning next steps.

**Ideal for:**
- First-time entrepreneurs
- Concept validation
- Market research guidance
- Business model development

### 💰 Loan Readiness
For business owners seeking financing who need to prepare comprehensive applications with organized financials.

**Ideal for:**
- Growth capital seekers
- SBA loan applicants
- Equipment/real estate financing
- Financial documentation preparation

### 🛟 Recovery & Stabilization
For businesses facing challenges who need objective assessment and strategic guidance.

**Ideal for:**
- Cash flow problems
- Strategic pivots
- Difficult decisions
- Operational restructuring

### 🔄 Business Transition
For owners planning exits, succession, or closure who need structured transition guidance.

**Ideal for:**
- Retirement planning
- Business sale preparation
- Succession planning
- Strategic closure

## Pathway Structure

Each pathway follows a consistent five-step approach:

1. **Welcome** - Introduction and pathway overview with embedded video
2. **Learn** - Curated resources and guidance specific to the pathway
3. **Work** - Focused workbook to organize thoughts and information
4. **Submit** - Share completed work with advisor before meeting
5. **Schedule** - Book advisory session when prepared

## Technology Stack

- **Framework**: Streamlit 1.28.0+
- **Language**: Python 3.8+
- **Deployment**: Render-ready
- **Styling**: Custom CSS for calm, professional appearance

## Project Structure

```
client-pathways/
│
├── app.py                          # Main application and homepage
├── requirements.txt                # Python dependencies
├── README.md                       # This file
│
├── pages/                          # Pathway pages
│   ├── idea_exploration.py
│   ├── loan_readiness.py
│   ├── recovery_stabilization.py
│   └── business_transition.py
│
├── assets/                         # Static assets
│   ├── pdfs/                       # Workbook PDFs
│   ├── images/                     # Images and graphics
│   └── icons/                      # Icon files
│
├── prompts/                        # AI summary prompts (future)
│   ├── idea_snapshot_prompt.md
│   ├── loan_summary_prompt.md
│   ├── recovery_prompt.md
│   └── transition_prompt.md
│
├── content/                        # Content management
│   ├── videos.md                   # Video resource library
│   ├── resource_links.md           # External resource links
│   └── pathway_descriptions.md     # Detailed pathway info
│
├── docs/                           # Documentation
│   ├── architecture/               # Architecture documentation
│   ├── workbooks/                  # Workbook source files
│   └── windsurf_reports/           # Build and deployment reports
│
└── .streamlit/                     # Streamlit configuration
    └── config.toml                 # Theme and server settings
```

## Local Development

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd sbdc-client-pathways
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

4. Open your browser to `http://localhost:8501`

## Deployment to Render

### Prerequisites
- Render account (free tier available)
- GitHub repository with this code

### Deployment Steps

1. **Push code to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <your-repo-url>
git push -u origin main
```

2. **Create New Web Service on Render**
   - Log in to [Render](https://render.com)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure Service**
   - **Name**: `client-pathways`
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
   - **Instance Type**: Free (or paid for production)

4. **Environment Variables** (if needed)
   - Add any required environment variables in Render dashboard

5. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy
   - Your app will be available at `https://client-pathways.onrender.com`

### Render Configuration Notes
- Free tier apps sleep after 15 minutes of inactivity
- First request after sleep takes ~30 seconds to wake up
- For production, use paid tier for always-on service
- Custom domains can be configured in Render settings

## Design Philosophy

### Visual Design
- **Whitespace**: Generous spacing for calm, uncluttered feel
- **Typography**: Clean, readable fonts with clear hierarchy
- **Colors**: Soft, professional palette (blues, grays)
- **Icons**: Simple, supportive visual cues
- **Layout**: Mobile-friendly, responsive design

### Tone & Voice
- Calm and reassuring
- Professional but approachable
- Supportive without being patronizing
- Structured without being rigid

### What to Avoid
- Busy, cluttered layouts
- Harsh or aggressive colors
- Dense text blocks
- Gamification elements
- Dashboard overload
- Corporate jargon

## Future Roadmap

The current V1 implementation establishes the foundation. Future enhancements may include:

### Phase 2: Enhanced Functionality
- [ ] File upload and storage system
- [ ] Workbook PDF generation and downloads
- [ ] Scheduling system integration (Calendly, etc.)
- [ ] Email notifications

### Phase 3: Intelligence Layer
- [ ] AI-generated workbook summaries for advisors
- [ ] Automated pathway recommendations
- [ ] Smart form validation and guidance
- [ ] Adaptive questioning based on responses

### Phase 4: Integration & Analytics
- [ ] CRM integration (Salesforce, HubSpot)
- [ ] Pathway completion analytics
- [ ] Advisor dashboard
- [ ] Client progress tracking
- [ ] Outcome measurement

### Phase 5: Expansion
- [ ] Additional specialized pathways
- [ ] Multi-language support
- [ ] Accessibility enhancements (WCAG 2.1 AA)
- [ ] Mobile app version

## Architecture Decisions

### Why Streamlit?
- Rapid prototyping and iteration
- Python-based (familiar to data/analytics teams)
- Built-in components for forms and file handling
- Easy deployment to multiple platforms
- Good for MVP validation

### Why No Database Yet?
- V1 focuses on structure and user experience
- Reduces complexity for initial validation
- Easier to iterate on pathway design
- Database layer can be added when needed

### Why No Authentication Yet?
- Simplifies initial deployment
- Reduces barrier to entry for testing
- Can be added when moving to production
- Focus on core pathway experience first

### Extension Points
The architecture supports future additions:
- **Database layer**: SQLite → PostgreSQL migration path
- **Authentication**: Streamlit auth or OAuth integration
- **File storage**: Local → S3/Azure Blob migration
- **AI integration**: OpenAI API ready prompts
- **Analytics**: Event tracking hooks in place

## Contributing

### Code Style
- Follow PEP 8 Python style guide
- Use meaningful variable and function names
- Comment complex logic
- Keep functions focused and modular

### Adding New Pathways
1. Create new page in `pages/` directory
2. Follow existing pathway template structure
3. Add navigation button in `app.py` sidebar
4. Create corresponding prompt in `prompts/` directory
5. Update this README

### Content Updates
- Video resources: Update `content/videos.md`
- External links: Update `content/resource_links.md`
- Pathway descriptions: Update `content/pathway_descriptions.md`

## Support & Contact

For questions, issues, or suggestions:
- Create an issue in the GitHub repository
- Contact the technical team
- Email: [contact email]

## License

[Specify license - e.g., MIT, Apache 2.0, or proprietary]

## Acknowledgments

Built to improve client preparation and advisory meeting quality.

---

**Version**: 3.0.0  
**Last Updated**: May 2026  
**Status**: V3 Unbranded Navigation Complete
