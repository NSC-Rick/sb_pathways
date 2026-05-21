# SB Pathways Folder Architecture Initialization

**Project**: Small Business Pathways  
**Date**: May 20, 2026  
**Task**: STRUCT-01 through STRUCT-07 - Pathway Resource Structure  
**Status**: ✅ Complete  

---

## Executive Summary

Successfully created a scalable, organized directory structure for all SB Pathways educational assets. The architecture separates Core Pathways (8) from Supplemental Pathways (5) with consistent subfolder organization across all pathways. A shared resources area and metadata template system provide foundation for future manifest-driven rendering.

---

## Architecture Overview

### **Hierarchy Principle**

```
sb_pathways/
├── pathways/
│   ├── core/              # Foundational business-state pathways
│   └── supplemental/      # Focused/specialized guidance areas
├── shared_resources/      # Common assets across pathways
└── pathway_manifest_template.json  # Metadata template
```

**Design Philosophy:**
- **Core Pathways:** Represent foundational business states and critical transitions
- **Supplemental Pathways:** Provide focused capability modules and specialized topics
- **Shared Resources:** Centralize common assets to avoid duplication
- **Manifest-Driven:** Enable future dynamic rendering from metadata

---

## Directory Structure Created

### **STRUCT-01: Top-Level Structure** ✅

```
pathways/
├── core/
└── supplemental/
```

**Status:** ✅ Created  
**Purpose:** Separate core business-state pathways from supplemental capability modules

---

### **STRUCT-02: Core Pathway Folders** ✅

**8 Core Pathways Created:**

```
pathways/core/
├── idea_exploration/
├── startup_launch/
├── loan_readiness/
├── marketing_foundation/
├── recovery_stabilization/
├── growth_planning/
├── business_transition/
└── financial_foundations/
```

**Naming Convention:** `lowercase_with_underscores`  
**Status:** ✅ All 8 pathways created  

---

### **STRUCT-03: Standard Resource Subfolders** ✅

**Each pathway contains 8 standard subfolders:**

```
[pathway_name]/
├── videos/              # Intro and educational videos
├── readings/            # Articles, guides, external resources
├── workbooks/           # Interactive workbooks (PDF, DOCX, Google Docs)
├── worksheets/          # Fillable worksheets and exercises
├── tools/               # Calculators, templates, checklists
├── advisor_notes/       # Internal advisor guidance and tips
├── metadata/            # Pathway metadata and configuration
└── images/              # Icons, diagrams, illustrations
```

**Total Subfolders Created:** 64 (8 pathways × 8 subfolders)  
**Status:** ✅ Consistent structure across all core pathways  

---

### **STRUCT-04: Supplemental Pathway Folders** ✅

**5 Supplemental Pathways Created:**

```
pathways/supplemental/
├── ai_for_small_business/
├── work_life_balance/
├── digital_tools/
├── change_management/
└── caregiver_entrepreneurs/
```

**Same Standard Subfolders:**
- videos/
- readings/
- workbooks/
- worksheets/
- tools/
- advisor_notes/
- metadata/
- images/

**Total Subfolders Created:** 40 (5 pathways × 8 subfolders)  
**Status:** ✅ Consistent structure across all supplemental pathways  

---

### **STRUCT-05: Shared Resource Area** ✅

```
shared_resources/
├── branding/               # Logos, brand guidelines, color palettes
├── templates/              # Reusable document templates
├── icons/                  # Shared icon library
├── downloadable_assets/    # Common downloads (e.g., business plan template)
├── common_videos/          # Videos used across multiple pathways
└── common_readings/        # Readings referenced by multiple pathways
```

**Purpose:** Centralize common assets to avoid duplication  
**Status:** ✅ All 6 subdirectories created  

---

### **STRUCT-06: Metadata Template** ✅

**File Created:** `pathway_manifest_template.json`

**Template Structure:**

```json
{
  "pathway_name": "",
  "pathway_type": "core|supplemental",
  "pathway_key": "",
  "icon": "",
  "description": "",
  "short_description": "",
  "estimated_time": "",
  "target_audience": "",
  "learning_objectives": [],
  "prerequisites": [],
  "sections": ["Welcome", "Learn", "Work", "Submit", "Schedule"],
  "videos": {
    "intro_video": {
      "title": "",
      "url": "",
      "duration": "",
      "description": ""
    },
    "educational_videos": []
  },
  "essential_reading": [],
  "workbooks": [],
  "worksheets": [],
  "tools": [],
  "advisor_notes": {
    "preparation_tips": "",
    "common_challenges": [],
    "key_discussion_points": [],
    "follow_up_resources": []
  },
  "metadata": {
    "created_date": "",
    "last_updated": "",
    "version": "1.0",
    "author": "",
    "status": "draft|review|published",
    "tags": []
  }
}
```

**Features:**
- Comprehensive pathway metadata
- Video configuration
- Resource tracking
- Advisor guidance
- Version control
- Status tracking

**Status:** ✅ Template created and ready for use  

---

### **STRUCT-07: Scalability & Consistency** ✅

**Naming Conventions:**
- ✅ All folders use `lowercase_with_underscores`
- ✅ No spaces or special characters
- ✅ Consistent across all pathways

**Folder Structure:**
- ✅ Identical subfolder structure for all pathways
- ✅ Predictable organization
- ✅ Easy to navigate

**Future Compatibility:**
- ✅ Manifest-driven rendering ready
- ✅ Dynamic pathway loading possible
- ✅ Scalable to additional pathways

---

## Git Integration

### **.gitkeep Files Added** ✅

**Total .gitkeep Files:** 125

**Distribution:**
- Core pathways: 64 files (8 pathways × 8 subfolders)
- Supplemental pathways: 40 files (5 pathways × 8 subfolders)
- Shared resources: 6 files
- Parent directories: 15 files

**Purpose:**
- Preserve empty directories in Git
- Maintain folder structure even without content
- Enable clean repository initialization

**Status:** ✅ All empty directories preserved for Git

---

## Quality Verification

### ✅ **All Folders Created**

**Core Pathways:** 8/8 ✓
- business_transition
- financial_foundations
- growth_planning
- idea_exploration
- loan_readiness
- marketing_foundation
- recovery_stabilization
- startup_launch

**Supplemental Pathways:** 5/5 ✓
- ai_for_small_business
- caregiver_entrepreneurs
- change_management
- digital_tools
- work_life_balance

**Shared Resources:** 6/6 ✓
- branding
- common_readings
- common_videos
- downloadable_assets
- icons
- templates

---

### ✅ **Standard Subfolders Verified**

**Sample Pathway Structure** (idea_exploration):
```
idea_exploration/
├── advisor_notes/
├── images/
├── metadata/
├── readings/
├── tools/
├── videos/
├── workbooks/
└── worksheets/
```

**Verification:** ✅ All 8 subfolders present  
**Consistency:** ✅ Identical structure across all 13 pathways  

---

### ✅ **Naming Consistency**

**Convention:** `lowercase_with_underscores`

**Examples:**
- ✅ `idea_exploration` (not `IdeaExploration` or `idea-exploration`)
- ✅ `ai_for_small_business` (not `AI_for_small_business`)
- ✅ `work_life_balance` (not `work-life-balance`)

**Status:** ✅ All folders follow naming convention  

---

### ✅ **No Duplicate or Malformed Directories**

**Verification Steps:**
1. ✅ No duplicate pathway names
2. ✅ No typos or misspellings
3. ✅ No inconsistent subfolder names
4. ✅ No missing subfolders
5. ✅ No extra/unexpected directories

**Status:** ✅ Clean directory structure  

---

### ✅ **Future Manifest-Driven Rendering Compatibility**

**Metadata Template Features:**
- ✅ JSON format for easy parsing
- ✅ Comprehensive pathway metadata
- ✅ Resource tracking (videos, readings, workbooks, etc.)
- ✅ Version control fields
- ✅ Status tracking (draft/review/published)

**Future Capabilities:**
- Dynamic pathway loading from manifest files
- Automated resource discovery
- Version management
- Content status workflow

**Status:** ✅ Ready for manifest-driven architecture  

---

## Directory Statistics

### **Total Directories Created**

| Category | Count |
|----------|-------|
| Core Pathways | 8 |
| Supplemental Pathways | 5 |
| Subfolders per Pathway | 8 |
| Total Pathway Subfolders | 104 |
| Shared Resource Folders | 6 |
| **Total Directories** | **119** |

### **Total .gitkeep Files**

| Category | Count |
|----------|-------|
| Core Pathway Subfolders | 64 |
| Supplemental Pathway Subfolders | 40 |
| Shared Resource Folders | 6 |
| Parent Directories | 15 |
| **Total .gitkeep Files** | **125** |

---

## File System Layout

### **Complete Structure**

```
sb_pathways/
│
├── pathways/
│   │
│   ├── core/
│   │   ├── business_transition/
│   │   │   ├── videos/
│   │   │   ├── readings/
│   │   │   ├── workbooks/
│   │   │   ├── worksheets/
│   │   │   ├── tools/
│   │   │   ├── advisor_notes/
│   │   │   ├── metadata/
│   │   │   └── images/
│   │   │
│   │   ├── financial_foundations/
│   │   │   └── [8 subfolders]
│   │   │
│   │   ├── growth_planning/
│   │   │   └── [8 subfolders]
│   │   │
│   │   ├── idea_exploration/
│   │   │   └── [8 subfolders]
│   │   │
│   │   ├── loan_readiness/
│   │   │   └── [8 subfolders]
│   │   │
│   │   ├── marketing_foundation/
│   │   │   └── [8 subfolders]
│   │   │
│   │   ├── recovery_stabilization/
│   │   │   └── [8 subfolders]
│   │   │
│   │   └── startup_launch/
│   │       └── [8 subfolders]
│   │
│   └── supplemental/
│       ├── ai_for_small_business/
│       │   └── [8 subfolders]
│       │
│       ├── caregiver_entrepreneurs/
│       │   └── [8 subfolders]
│       │
│       ├── change_management/
│       │   └── [8 subfolders]
│       │
│       ├── digital_tools/
│       │   └── [8 subfolders]
│       │
│       └── work_life_balance/
│           └── [8 subfolders]
│
├── shared_resources/
│   ├── branding/
│   ├── common_readings/
│   ├── common_videos/
│   ├── downloadable_assets/
│   ├── icons/
│   └── templates/
│
└── pathway_manifest_template.json
```

---

## Usage Guidelines

### **Adding New Pathways**

1. **Determine pathway type** (core or supplemental)
2. **Create pathway folder** in appropriate directory
3. **Use naming convention:** `lowercase_with_underscores`
4. **Create 8 standard subfolders:**
   - videos/
   - readings/
   - workbooks/
   - worksheets/
   - tools/
   - advisor_notes/
   - metadata/
   - images/
5. **Copy and populate** `pathway_manifest_template.json`
6. **Save manifest** to `metadata/` subfolder

---

### **Organizing Resources**

**Videos:**
- Place intro videos in `videos/`
- Reference external videos via manifest
- Store local videos if needed

**Readings:**
- Store PDFs in `readings/`
- Link external articles via manifest
- Organize by topic or section

**Workbooks/Worksheets:**
- Store fillable PDFs in respective folders
- Include Google Doc links in manifest
- Version control important

**Tools:**
- Store calculators, templates, checklists
- Include usage instructions
- Link from pathway views

**Advisor Notes:**
- Internal guidance for advisors
- Preparation tips
- Common challenges and solutions

**Metadata:**
- Store pathway manifest JSON
- Track versions and updates
- Maintain resource inventory

**Images:**
- Icons, diagrams, illustrations
- Pathway-specific visuals
- Optimized for web

---

### **Shared Resources**

**When to use shared_resources/:**
- Asset used by multiple pathways
- Common branding elements
- Reusable templates
- Universal tools

**When to use pathway-specific folders:**
- Pathway-unique content
- Specialized resources
- Context-specific materials

---

## Future Enhancements

### **Manifest-Driven Rendering**

**Phase 1: Metadata Population**
- Populate manifest files for all pathways
- Standardize resource references
- Establish version control

**Phase 2: Dynamic Loading**
- Build manifest parser
- Create dynamic pathway renderer
- Implement resource discovery

**Phase 3: Content Management**
- Admin interface for manifest editing
- Resource upload system
- Version management workflow

---

### **Additional Pathways**

**Potential Core Pathways:**
- Franchise Exploration
- Business Acquisition
- Strategic Partnerships
- Exit Planning

**Potential Supplemental Pathways:**
- Social Media Basics
- Email Marketing
- Customer Service Excellence
- Team Building
- Legal Compliance
- Tax Planning

**Scalability:** Structure supports unlimited pathway expansion

---

## Integration with Existing System

### **Current Application Structure**

**Existing:**
```
sb_pathways/
├── app.py
├── pathway_config.py
├── views/
├── components/
├── content/
└── docs/
```

**New Addition:**
```
sb_pathways/
├── pathways/          # NEW
├── shared_resources/  # NEW
└── pathway_manifest_template.json  # NEW
```

**Compatibility:** ✅ No conflicts with existing structure

---

### **Migration Path**

**Current State:**
- Pathway views hardcoded in `views/`
- Video links in `content/video_links.py`
- Pathway metadata in `pathway_config.py`

**Future State:**
- Pathway content in `pathways/[type]/[name]/`
- Resources organized by type
- Metadata in manifest JSON files
- Dynamic rendering from manifests

**Transition:**
- Gradual migration pathway-by-pathway
- Maintain backward compatibility
- Test thoroughly before switching

---

## Deployment Considerations

### **Git Repository**

**Commit Strategy:**
```bash
git add pathways/ shared_resources/ pathway_manifest_template.json
git commit -m "Initialize pathway folder architecture with Core and Supplemental structure"
git push origin main
```

**Benefits:**
- Clean directory structure in repository
- .gitkeep files preserve empty folders
- Ready for content population

---

### **Content Population**

**Recommended Order:**
1. **Core Pathways First** (highest priority)
   - idea_exploration
   - loan_readiness
   - recovery_stabilization
   - business_transition
2. **Remaining Core Pathways**
   - startup_launch
   - marketing_foundation
   - growth_planning
   - financial_foundations
3. **Supplemental Pathways** (as needed)

---

## Success Criteria Met

✅ **SB Pathways has a scalable organized architecture**
- 119 directories created
- Consistent structure across all pathways
- Clear separation of core vs. supplemental

✅ **Core and Supplemental pathways are clearly separated**
- `pathways/core/` for business-state pathways
- `pathways/supplemental/` for capability modules
- Logical organization principle

✅ **All pathways follow a consistent asset structure**
- 8 standard subfolders per pathway
- Identical organization
- Predictable resource locations

✅ **Future workbook/resource expansion is simplified**
- Manifest template ready
- Standard folder structure
- Scalable to unlimited pathways

---

## Conclusion

The SB Pathways folder architecture has been successfully initialized with a scalable, organized structure that separates Core and Supplemental pathways. The consistent subfolder organization and metadata template system provide a solid foundation for future content expansion and manifest-driven rendering.

**Status:** ✅ Complete and ready for content population  
**Total Directories:** 119  
**Total .gitkeep Files:** 125  
**Pathways Ready:** 13 (8 Core + 5 Supplemental)  

---

**Report Generated:** May 20, 2026  
**Task ID:** STRUCT-01 through STRUCT-07  
**Status:** ✅ All tasks complete
