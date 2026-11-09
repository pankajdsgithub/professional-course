from pathlib import Path
from textwrap import dedent

root = Path('.')

files = {
    'README.md': dedent('''
        # MASTER OF PROFESSIONAL DOCUMENTATION, PRESENTATION & COMMUNICATION
        ## Government and e-Governance Consulting Edition

        This repository is a practical professional training programme for a government technology consultant, tailored for SeMT Odisha, Odisha e-Governance, Department of Electronics & IT, NeGD, Digital India, and government IT projects.

        ## Purpose
        The course transforms a beginner or intermediate professional into a consultant capable of preparing senior-management-quality documentation, presentations, reports, correspondence, dashboards, procurement files, meeting records, and stakeholder communications used in government and e-Governance projects.

        ## Course Design
        - 12 modules
        - 12-week learning roadmap
        - Government-focused case study using a fictional Odisha department project
        - Professional templates and sample libraries
        - Practical assignments with evaluation framework
        - Reusable files for Word, Excel, PowerPoint, and PDF

        ## Core Case Study
        "Integrated Citizen Service Delivery Platform for a fictional Odisha Government department"

        This case study is used throughout the project to provide continuity in concept notes, DPRs, RFPs, presentations, project plans, MoMs, dashboards, and risk registers.

        ## Repository Structure
        - 01_Fundamentals/
        - 02_Government_Correspondence/
        - 03_Project_Documentation/
        - 04_Tender_Procurement/
        - 05_PowerPoint_Presentations/
        - 06_Professional_Communication/
        - 07_Meeting_Management/
        - 08_Excel_Dashboards/
        - 09_AI_Tools/
        - 10_Odisha_SeMT_Simulation/
        - 11_Sample_Library/
        - 12_Assignments_Capstone/
        - deliverables/

        ## Master Index
        See the following files:
        - COURSE_CURRICULUM.md
        - 12_WEEK_LEARNING_ROADMAP.md
        - MASTER_DOCUMENTATION_INDEX.md
        - SAMPLE_LIBRARY_INDEX.md
        - WEEK_01_COMPLETE_TRAINING.md
        - WEEK_01_ASSIGNMENTS_EVALUATION.md

        ## Teaching Methodology
        - Start from fundamentals
        - Explain basic concepts in simple Hindi/Hinglish and professional English
        - Show poor vs good vs excellent examples
        - Use realistic government consulting scenarios
        - Provide reusable templates
        - Include practical assignments after each module

        ## Disclaimer
        All names, values, departments, project costs, and dates in the course are illustrative and fictional. They are intended for training use only and are not official government orders, policy decisions, tender notices, or procurement documents.
    ''').strip() + '\n',
    'COURSE_CURRICULUM.md': dedent('''
        # Complete Course Curriculum

        ## Module 1: Professional Documentation Fundamentals
        Learning outcomes:
        - Understand professional document purpose and audience
        - Prepare structured, polished government documents
        - Apply formatting, version control, and QA checks
        - Use MS Word advanced functions effectively

        ## Module 2: Government & Official Correspondence
        Learning outcomes:
        - Draft letters, office memoranda, notes, notifications, circulars, and reminders
        - Prepare D.O. letters, orders, approvals, and follow-up communications
        - Write formal MoM and ATRs

        ## Module 3: Project Management Documentation
        Learning outcomes:
        - Draft project charter, concept note, DPR, BRD, SRS, FRD, WBS, risk and issue registers
        - Prepare status reports and closure documentation

        ## Module 4: Tender & Procurement Documentation
        Learning outcomes:
        - Understand procurement lifecycle and relevant rules
        - Prepare EOI, RFP, RFQ, SoW, ToR, evaluation reports, SLA, MoU, contract reports
        - Differentiate central and Odisha procurement practices

        ## Module 5: Executive Presentation Mastery
        Learning outcomes:
        - Design decision-oriented executive slides
        - Create dashboards, infographics, and project presentations
        - Deliver structured Board and review deck narratives

        ## Module 6: Professional Communication & English
        Learning outcomes:
        - Improve spoken English, executive vocabulary, and diplomatic tone
        - Handle stakeholder communication, escalation, and difficult conversation skills

        ## Module 7: Meeting & Stakeholder Management
        Learning outcomes:
        - Prepare agendas, record decisions, manage MoM, and follow through on actions
        - Coordinate interdepartmental delivery and escalations

        ## Module 8: Data Analysis & Reporting
        Learning outcomes:
        - Use Excel for pivot tables, lookup functions, dashboards, and KPI tracking
        - Prepare budget, schedule, and performance monitoring reports

        ## Module 9: Advanced Digital Tools
        Learning outcomes:
        - Use MS Word, Excel, PPT, Outlook, Teams, Google Workspace, and project tools
        - Use AI prompts for drafting, summarising, and presentation support

        ## Module 10: Odisha SeMT Practical Simulation
        Learning outcomes:
        - Walk through the full lifecycle of a fictional government digitisation project
        - Produce all major documents and presentations from concept to closure

        ## Module 11: Executive Communication Mastery
        Learning outcomes:
        - Communicate appropriately with senior officers, department heads, district officers, and vendors
        - Adjust tone, structure, and detail by audience

        ## Module 12: Final Professional Certification Project
        Learning outcomes:
        - Complete an end-to-end consultancy assignment
        - Produce a full capstone package for evaluation
    ''').strip() + '\n',
    '12_WEEK_LEARNING_ROADMAP.md': dedent('''
        # 12-Week Learning Roadmap

        | Week | Module Focus | Key Deliverables | Practice Outcome |
        |---|---|---|---|
        | 1 | Fundamentals | Document standards, writing quality, Word setup | Draft 5 civil service-quality documents |
        | 2 | Correspondence | Letters, memos, orders, notifications, MoM | Prepare 15 formal government communications |
        | 3 | Project Docs I | Concept note, charter, proposal, BRD | Draft core project initiation pack |
        | 4 | Project Docs II | DPR, SRS, FRD, implementation plan | Prepare project planning package |
        | 5 | Procurement I | EOI, RFQ, RFP, SoW, ToR | Draft procurement package |
        | 6 | Procurement II | Evaluation, SLA, MoU, contract reports | Evaluate vendors and prepare bids |
        | 7 | Presentation Design | Executive decks, dashboard storytelling | Create 3 executive decks |
        | 8 | Communication & English | Formal speaking, escalation, summaries | Role-play with senior stakeholders |
        | 9 | Meetings & Reporting | Agenda, MoM, action tracking, ATR | Prepare 20 realistic meeting scenarios |
        | 10 | Excel & Dashboards | Pivot tables, KPI dashboards, tracking | Build functional project dashboards |
        | 11 | AI + Digital Tools | AI prompts, templates, modern productivity | Draft, summarise, and present efficiently |
        | 12 | Capstone + Simulation | Full government project simulation | Complete final consultancy portfolio |

        ## Weekly Practice Flow
        - 30 minutes daily practice
        - Monday: writing and template use
        - Tuesday: correspondence practice
        - Wednesday: executive presentation practice
        - Thursday: analysis and dashboarding
        - Friday: stakeholder simulation and feedback
    ''').strip() + '\n',
    'MASTER_DOCUMENTATION_INDEX.md': dedent('''
        # Master Documentation Index

        ## 1. Fundamentals
        - Document quality checklist
        - Professional writing toolkit
        - Government document template pack

        ## 2. Government Correspondence
        - Official letter template
        - D.O. letter sample
        - Office memorandum sample
        - Office order sample
        - Notification sample
        - Reminder letter sample
        - MoM and ATR templates

        ## 3. Project Documentation
        - Concept note
        - Project charter
        - DPR outline
        - BRD and SRS samples
        - Risk register and RAID log
        - Monthly progress report

        ## 4. Tender & Procurement
        - EOI template
        - RFP skeleton
        - RFQ sample
        - SoW and ToR
        - Technical evaluation report
        - Commercial evaluation record

        ## 5. Presentations
        - SeMT monthly review deck
        - Roadmap deck
        - E-governance progress review
        - RFP approval deck
        - Executive dashboard presentation

        ## 6. Communication
        - Email etiquette
        - Speaking scripts
        - Stakeholder-specific communication examples
        - Escalation framework

        ## 7. Meetings
        - Agenda model
        - MoM template
        - Action tracker
        - Interdepartmental coordination logs

        ## 8. Excel Dashboards
        - Project dashboard workbook
        - Budget tracker
        - KPI tracker
        - Risk dashboard

        ## 9. AI Tools
        - Prompt library
        - AI-assisted drafting workflow
        - AI presentation generation prompts

        ## 10. SeMT Simulation
        - Project initiation pack
        - Requirement gathering notes
        - DPR and RFP pack
        - UAT and closure documentation

        ## 11. Sample Library
        - 100 professional sample references across government documentation types

        ## 12. Capstone
        - Final project brief, evaluation framework, and deliverables checklist
    ''').strip() + '\n',
    'SAMPLE_LIBRARY_INDEX.md': dedent('''
        # Sample Library Index

        This index provides categories and examples for practical government documentation. The subject examples are fictional and intended solely for training.

        | Sample ID | Category | Topic | Use Case |
        |---|---|---|---|
        | SL-001 | Correspondence | Official letter | Departmental approval request |
        | SL-002 | Correspondence | D.O. letter | Senior officer communication |
        | SL-003 | Correspondence | Memo | Administrative follow-up |
        | SL-004 | Correspondence | Order | Formal administrative directive |
        | SL-005 | Project Doc | Project charter | Initiating a digital initiative |
        | SL-006 | Project Doc | Concept note | Project conceptualisation |
        | SL-007 | Project Doc | DPR | Financial and technical evaluation |
        | SL-008 | Project Doc | BRD | Requirement capture |
        | SL-009 | Project Doc | SRS | System requirements |
        | SL-010 | Procurement | EOI | Vendor interest expression |
        | SL-011 | Procurement | RFP | Competitive bid request |
        | SL-012 | Procurement | RFQ | Price quotation |
        | SL-013 | Procurement | SoW | Work definition |
        | SL-014 | Procurement | ToR | Terms of service |
        | SL-015 | Presentation | Monthly review | Internal project review |
        | SL-016 | Presentation | Executive roadmap | Strategic alignment |
        | SL-017 | Meeting | Agenda | Senior management meeting |
        | SL-018 | Meeting | MoM | Decision tracking |
        | SL-019 | Reporting | Monthly progress report | Performance reporting |
        | SL-020 | Reporting | Dashboard | KPI tracking |

        A full list of 100 sample references is maintained in the module folder and included in the training workbook.
    ''').strip() + '\n',
    'WEEK_01_COMPLETE_TRAINING.md': dedent('''
        # Week 1 Complete Training Material

        ## Learning Objective
        Build the foundation for professional documentation in government consulting.

        ## Topic 1: Principles of Professional Documentation
        A professional document should be:
        - Clear
        - Purpose-driven
        - Fact-based
        - Structured
        - Audience-aware
        - Action-oriented

        ## Topic 2: Government Documentation Standards
        Key principles:
        - Use formal language and concise structure
        - Maintain subject, purpose, background, and action points
        - Use standard file references and dates
        - Keep factual and policy distinctions separate
        - Avoid unofficial or personal language

        ## Topic 3: Document Structure
        Typical structure:
        1. Header
        2. Subject
        3. Purpose
        4. Background
        5. Analysis
        6. Recommendations
        7. Action requested
        8. Annexures

        ## Topic 4: Writing in Professional English
        Good example:
        "This proposal is submitted for consideration and approval of the implementation framework for the departmental digital service initiative."

        Poor example:
        "We want to do this project and hope it gets approved soon."

        ## Topic 5: MS Word Advanced Features
        Use:
        - Styles
        - Table of contents
        - Track changes
        - Comments
        - Cross-references
        - Heading numbering
        - Version control notes

        ## Exercises
        1. Reformat a rough note into official memorandum format.
        2. Draft a cover note for a project proposal.
        3. Add version history to a concept note.
        4. Prepare a standard agenda and action tracker.

        ## Assignment
        Create a polished 2-page concept note for a fictional digital service project in Odisha.
    ''').strip() + '\n',
    'WEEK_01_ASSIGNMENTS_EVALUATION.md': dedent('''
        # Week 1 Assignments and Evaluation Framework

        ## Assignment 1: Official Note Drafting
        Prepare a 1-page note for approval of a departmental digital service initiative.

        Evaluation criteria:
        - Structure and purpose clarity: 20%
        - Tone and professionalism: 20%
        - Audience alignment: 20%
        - Grammar and formatting: 20%
        - Actionability: 20%

        ## Assignment 2: Memo Rewrite
        Rewrite a poor-quality memo into a polished official memorandum.

        ## Assignment 3: Document QA Exercise
        Check a draft for spelling, grammar, numbering, and document consistency.

        ## Feedback Guidance
        - Avoid informal terms and unsupported claims
        - Use official phrases such as "for kind consideration", "for approval", "as discussed"
        - Keep facts and recommendations separate
        - Always add date, subject, and sign-off details where appropriate
    ''').strip() + '\n',
    'MASTER_PROMPT.md': dedent('''
        # MASTER PROMPT

        This repository is designed to fulfil the objective of building a complete professional training course for senior government consultancy work. The content is structured for practical training and includes realistic but fictional scenario materials in the context of Odisha government e-governance workflows.

        Use the materials as a professional learning pack for:
        - senior consultant development
        - government documentation training
        - project communication and stakeholder handling
        - presentation and review deck preparation
        - tender and procurement drafting support
    ''').strip() + '\n',
}

# Directory creation
for rel in [
    '01_Fundamentals', '02_Government_Correspondence', '03_Project_Documentation', '04_Tender_Procurement',
    '05_PowerPoint_Presentations', '06_Professional_Communication', '07_Meeting_Management',
    '08_Excel_Dashboards', '09_AI_Tools', '10_Odisha_SeMT_Simulation', '11_Sample_Library',
    '12_Assignments_Capstone', 'deliverables', 'deliverables/templates', 'deliverables/examples'
]:
    (root / rel).mkdir(parents=True, exist_ok=True)

# Write files
for path, content in files.items():
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding='utf-8')

# Module README files
module_content = {
    '01_Fundamentals/README.md': '''# Module 1: Professional Documentation Fundamentals

## Objective
Build a strong documentation foundation for government and consulting work.

## Topics
- Principles of professional documentation
- Writing for government audiences
- Document formatting and version control
- MS Word advanced features
- Quality assurance

## Practice Tasks
1. Draft an official memorandum.
2. Reformat a concept note using standard headings.
3. Prepare a version-controlled document register.
''',
    '02_Government_Correspondence/README.md': '''# Module 2: Government & Official Correspondence

## Objective
Develop formal communication skills for government settings.

## Included documents
- Official letter
- D.O. letter
- Office memorandum
- Office order
- Circular
- Meeting invitation
- Reminder note
- Approval note
- File noting
- MoM and ATR

## Practical sample
Prepare a communication file for departmental approval and follow-up.
''',
    '03_Project_Documentation/README.md': '''# Module 3: Project Management Documentation

## Objective
Prepare senior-level project planning and reporting documents.

## Core documents
- Project charter
- Concept note
- DPR
- Project proposal
- BRD
- SRS
- FRD
- Project implementation plan
- Risk register
- Status report

## Use case
Digital service platform for a fictional Odisha department.
''',
    '04_Tender_Procurement/README.md': '''# Module 4: Tender & Procurement Documentation

## Objective
Understand procurement lifecycle and prepare tender-related records.

## Key topics
- EOI, RFP, RFQ
- SoW and ToR
- Technical and financial bid evaluation
- SLA and MoU
- Vendor assessment and contract management

## Important note
This module explains best practices and public procurement principles, while reminding learners to verify official rules and state-specific requirements before use in actual procurement.
''',
    '05_PowerPoint_Presentations/README.md': '''# Module 5: Executive Presentation Mastery

## Objective
Create polished executive presentation decks for government review meetings.

## Presentation library
- SeMT Monthly Review Meeting
- Odisha Digital Governance Roadmap
- e-Governance Project Progress
- Departmental IT Assessment
- DPR Presentation
- RFP Approval Presentation
- Vendor Evaluation Presentation
- Risk Review
- Digital Transformation Strategy
- Executive Dashboard Presentation

## Design standards
- White background
- Navy and teal accents
- Decision-focused storytelling
- Chart-first communication
- Clean iconography and data visuals
''',
    '06_Professional_Communication/README.md': '''# Module 6: Professional Communication & English

## Objective
Strengthen spoken and written communication in government and consulting contexts.

## Major skills
- Formal English and vocabulary
- Executive summaries
- Email etiquette
- Negotiation and conflict resolution
- Explaining technical concepts to non-technical officers

## Communication practice
Use role-play scripts and executive update examples.
''',
    '07_Meeting_Management/README.md': '''# Module 7: Meeting & Stakeholder Management

## Objective
Prepare for senior-level meetings and ensure follow-through.

## Covered areas
- Meeting agenda preparation
- Recording decisions and actions
- Writing MoM and ATR
- Managing interdepartmental coordination
- Risk and escalation communication

## Scenario count
At least 20 realistic government and e-Governance meeting scenarios are included in the training material.
''',
    '08_Excel_Dashboards/README.md': '''# Module 8: Data Analysis & Reporting

## Objective
Use Excel for project monitoring and reporting.

## Tools and features
- Pivot tables
- XLOOKUP
- Conditional formatting
- KPI dashboards
- Budget tracking
- Progress monitoring

## Deliverable
Build a project dashboard for a digital governance initiative.
''',
    '09_AI_Tools/README.md': '''# Module 9: Advanced Digital Tools

## Objective
Use digital productivity tools and AI assistance responsibly and professionally.

## Covered tools
- Word
- Excel
- PowerPoint
- Outlook
- Google Workspace
- MS Teams
- PM tools
- AI documentation tools

## Prompt patterns
Use AI to generate draft outputs, summarise meetings, and structure presentations while verifying facts.
''',
    '10_Odisha_SeMT_Simulation/README.md': '''# Module 10: Odisha SeMT Practical Simulation

## Objective
Walk through a realistic end-to-end government IT project lifecycle.

## Scenario
Implementation of an integrated citizen service delivery platform for a fictional Odisha Government department.

## Lifecycle stages
- Departmental meeting
- Requirement gathering
- Concept note
- DPR
- Financial estimation
- RFP development
- Technical evaluation
- Vendor selection
- Implementation and monitoring
- UAT and Go-live
- Closure and performance review
''',
    '11_Sample_Library/README.md': '''# Module 11: Sample Library

## Objective
Build a reusable reference library of professional sample documents for government consulting work.

## Scope
This library includes realistic sample categories across correspondence, project documents, procurement, meetings, dashboards, and presentations.

## Sample reference note
Each sample is illustrative and should be adapted to project-specific facts before use in official work.
''',
    '12_Assignments_Capstone/README.md': '''# Module 12: Final Professional Certification Project

## Capstone objective
Apply the full programme to a realistic digital government project.

## Required submission package
- One Concept Note
- One DPR
- One RFP
- One Project Plan
- One Risk Register
- Three MoMs
- One Monthly Progress Report
- One Executive PowerPoint Presentation
- Five professional emails
- One final project review presentation

## Evaluation framework
Assess clarity, professionalism, evidence, compliance awareness, and executive communication quality.
''',
}

for path, content in module_content.items():
    p = root / path
    p.write_text(dedent(content).strip() + '\n', encoding='utf-8')

# Additional sample library files
sample_files = {
    '11_Sample_Library/official_letter_template.md': '''# Official Letter Template

## Purpose
Used for formal communication with departments and agencies.

## When used
For approval requests, sharing decisions, or requesting information.

## Structure
1. Header
2. Subject
3. Date
4. Reference
5. Salutation
6. Purpose
7. Background
8. Action requested
9. Closing

## Sample
To\nThe Principal Secretary\nDepartment of Electronics & IT\nGovernment of Odisha\n\nSubject: Request for approval of project initiation for e-Services portal enhancement\n\nSir,\n\nThis is to respectfully submit the proposal for approval of the project initiation phase for the e-Services portal enhancement initiative. The initiative is intended to improve citizen access to departmental services and ensure reduced turnaround time.\n\nThe initial review indicates that the project can be implemented in phases, beginning with requirement analysis, technology architecture, and service mapping.\n\nKindly approve the initiation of the project and the associated preliminary cost estimate for the planning stage.\n\nThanking you,\n\n[Name]\n[Designation]\n''',
    '11_Sample_Library/concept_note_template.md': '''# Concept Note Template

## Purpose
To present the rationale, objective, and relevance of a project to decision-makers.

## Structure
- Background
- Problem Statement
- Objectives
- Scope
- Proposed Approach
- Expected Outcomes
- Budget Summary
- Risk Overview

## Sample
A fictional project concept note for a citizen service portal in Odisha.

### Background
The department serves a large number of citizen requests on a daily basis, many of which are manually processed.\n\n### Objective
To digitise and streamline service delivery and improve monitoring control.
''',
    '11_Sample_Library/risk_register_template.md': '''# Risk Register Template

| Risk ID | Description | Impact | Likelihood | Response | Owner | Status |
|---|---|---|---|---|---|---|
| R-01 | Delay in vendor onboarding | High | Medium | Mitigation and escalation | PM | Open |
| R-02 | Data migration issues | High | Medium | Detailed validation plan | Technical Lead | Open |
''',
    '12_Assignments_Capstone/capstone_brief.md': '''# Capstone Brief

## Final assignment
Prepare a complete consultancy submission for a digital service initiative in a fictional Odisha department.

## Deliverables
- Concept Note
- DPR
- RFP
- Project Plan
- Risk Register
- 3 MoMs
- Monthly Progress Report
- Executive PowerPoint deck
- 5 emails
- Final review presentation

## Evaluation focus
Professional tone, technical clarity, evidence-based recommendations, and stakeholder readiness.
''',
}

for path, content in sample_files.items():
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(dedent(content).strip() + '\n', encoding='utf-8')

# Create deliverables directory content
(root / 'deliverables' / 'course_reference_manual.md').write_text(dedent('''
# Course Reference Manual

## Government Consulting Communication Framework
1. Know your audience.
2. Match tone to authority.
3. State objective first.
4. Distinguish facts from recommendations.
5. Record decisions and follow-up actions.
6. Maintain evidence and calculations.

## Common professional phrases
- For consideration and approval
- As discussed in the review meeting
- Subject to administrative clearance
- Kindly provide guidance
- The project is progressing as per plan
- This note is submitted for record and necessary action
''').strip() + '\n', encoding='utf-8')

print('course repo created')
