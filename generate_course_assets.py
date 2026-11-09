from pathlib import Path
from docx import Document
from docx.shared import Pt, Inches
from pptx import Presentation
from pptx.util import Inches, Pt
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import navy, teal, black, white

root = Path('.')
root.mkdir(exist_ok=True)

# Helpers

def write_md(path, text):
    p = root / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(text.strip() + '\n', encoding='utf-8')

# Module structure with realistic content
module_docs = {
    '01_Fundamentals/01_professional_documentation_guide.md': '''# Module 1: Professional Documentation Fundamentals

## Learning Objective
To understand how to produce clear, structured, and senior-management-ready documents in a government consulting environment.

## Core Principles
1. Purpose-first writing
2. Audience awareness
3. Factual, evidence-based tone
4. Consistent structure and formatting
5. Clean version control and traceability

## Government Documentation Standards
- Use formal, neutral language.
- Separate factual background from recommendations.
- Always include issue, objective, and action required.
- Maintain decision trail and version history.

## Good vs Poor Writing
### Poor
"We need to start the project and hope it works."

### Better
"This initiative is proposed to improve citizen service delivery and streamline workflow automation in the department."

### Excellent
"This concept note is submitted for approval of the project initiation phase, with the objective of improving citizen service delivery, reducing manual processing delays, and enabling transparent monitoring through a digital platform."

## Practical Assignment
Draft a 2-page concept note for a fictional Department of Agriculture and Farmers Empowerment service portal project.
''',
    '02_Government_Correspondence/01_official_letter_sample.md': '''# Official Letter Sample

## Purpose
Used for formal communication between government offices, departments, and agencies.

## Structure
- Header
- Subject
- Date and reference
- Body
- Action requested
- Closing

## Sample
**To**\nThe Principal Secretary\nDepartment of Electronics & IT\nGovernment of Odisha\n\n**Subject:** Request for approval of digital service delivery project\n\nSir,\n\nThis is to respectfully submit the proposal for approval of the Integrated Citizen Service Delivery Platform for the Department of Revenue and Disaster Management. The project intends to streamline public service access, improve service turnaround time, and enhance digital monitoring.\n\nThe preliminary review indicates that the conceptualisation and planning phase can be completed within 45 days and implementation can proceed in a phased manner.\n\nKindly accord approval for the preliminary planning and budgetary sanction as per departmental procedure.\n\nThanking you,\n\n[Name]\n[Designation]\n''',
    '02_Government_Correspondence/02_demi_official_letter_sample.md': '''# D.O. Letter Sample

## Purpose
Used for personal but official communication between officers.

## Structure
- Salutation
- Purpose statement
- Context
- Request or action
- Courtesy closing

## Sample
**D.O. No.:** 17/2026\n\nDear Shri Sahu,\n\nI am writing to request your kind review of the draft concept note on the departmental citizen service delivery initiative. We are in the final stage of internal vetting and would value your guidance on the scope and implementation sequencing.\n\nThe proposal is structured around service mapping, workflow automation, and governance oversight. A detailed discussion may be useful before the next review meeting.\n\nI would be grateful for your suggestions and directions.\n\nWith regards,\n[Name]\n''',
    '03_Project_Documentation/01_project_charter_template.md': '''# Project Charter Template

## Purpose
To formally establish the project and authorize its initiation.

## Sections
- Project title
- Purpose
- Objectives
- Scope
- Stakeholders
- Deliverables
- Timeline
- Budget estimate
- Risks
- Governance structure

## Sample Summary
Project Title: Integrated Citizen Service Delivery Platform\nDepartment: Department of Urban Development\nProject Sponsor: Principal Secretary\nProject Manager: Senior Consultant\nBudget: INR 3.4 crore\nTimeline: 14 months\n\n## Key Points
The project aims to create a digital experience for citizen service requests, integrate department workflows, and reduce manual effort through a unified platform.
''',
    '03_Project_Documentation/02_dpr_outline.md': '''# Detailed Project Report (DPR) Outline

## Purpose
To present the technical, financial, and implementation plan to decision-makers.

## Major Sections
1. Executive Summary
2. Background and Need
3. Existing System Analysis
4. Proposed Solution
5. Technical Architecture
6. Functional Modules
7. Project Governance
8. Budget and Financing
9. Implementation Plan
10. Risk Management
11. Monitoring and Evaluation
12. Annexures

## Example
The proposed project addresses delay in processing public service applications by consolidating request tracking, service status dashboards, and e-payment integration under a single solution.
''',
    '04_Tender_Procurement/01_rfp_framework.md': '''# RFP Framework

## Purpose
To invite bids from vendors for project execution and implementation.

## Typical Sections
- Invitation
- Background
- Scope of Work
- Deliverables
- Technical Eligibility
- Bid Evaluation Criteria
- Financial Proposal
- Contract Terms

## Example Stages
- Pre-bid meeting
- Clarifications
- Bid submission
- Technical evaluation
- Financial evaluation
- Negotiation
- Final award
''',
    '05_PowerPoint_Presentations/01_semt_monthly_review_deck.md': '''# SeMT Monthly Review Meeting Presentation

## Executive Purpose
Provide a concise update on key digital initiatives, risks, budgets, and decisions needed.

## Suggested slide structure
1. Title and objective
2. Executive summary
3. Portfolio overview
4. Key milestones achieved
5. Budget and expenditure status
6. Risks and issues
7. Decision required
8. Next monthly actions

## Speaker notes
Every slide should be concise and action-oriented. Highlight progress, variance, and required decisions.
''',
    '06_Professional_Communication/01_email_etiquette_guide.md': '''# Professional Email Etiquette Guide

## Purpose
To create clear and respectful written communication.

## Good Structure
- Subject line with clarity
- Greeting
- Purpose statement
- Key points
- Action needed
- Polite close

## Example
**Subject:** Request for review of draft DPR for Integrated Citizen Service Delivery Platform\n\nDear Sir,\n\nPlease find attached the draft Detailed Project Report for review and guidance. The report includes project need, scope, implementation plan, financial estimate, and risk assessment.\n\nYour suggestions on governance arrangements and financial phasing would be valuable before submission to the competent authority.\n\nKind regards,\n[Name]\n''',
    '07_Meeting_Management/01_meeting_agenda_template.md': '''# Meeting Agenda Template

## Purpose
To ensure meetings are focused and decisions are traceable.

## Sections
- Meeting title
- Date, time, and venue
- Attendees
- Objectives
- Agenda items
- Action owners
- Decision log

## Example Agenda
1. Review of implementation progress\n2. Risk and dependency review\n3. Budget utilisation update\n4. Vendor performance assessment\n5. Decisions required\n''',
    '08_Excel_Dashboards/01_project_dashboard_template.md': '''# Project Dashboard Template

## Purpose
To present progress, budget, risk, and schedule information in a single view.

## Suggested KPIs
- Schedule variance
- Budget variance
- Milestone attainment
- Defect count
- Risk count
- Vendor performance score

## Example Data Table
| KPI | Target | Actual | Commentary |
|---|---|---|---|
| Milestone completion | 80% | 72% | Delay due to data migration |
| Budget consumption | 60% | 58% | Within acceptable band |
''',
    '09_AI_Tools/01_ai_prompt_library.md': '''# AI Prompt Library for Government Consulting Work

## Prompt 1: Draft a concept note
"Draft a concept note for a digital citizen service platform for a fictional Odisha government department. Include problem statement, objectives, scope, implementation approach, expected outcomes, risks, and approval request. Keep the tone formal, concise, and suitable for senior government review."

## Prompt 2: Summarise a long DPR
"Summarise this DPR into a 6-slide executive brief for a departmental review meeting. Highlight strategic need, scope, budget estimate, risk factors, and decisions required."

## Prompt 3: Prepare executive email
"Write a professional email to a Principal Secretary summarising project progress, key risks, and action required. Keep tone formal and concise."

## Important Guidance
AI-generated material must always be validated for accuracy, logic, and compliance before use in official documentation.
''',
    '10_Odisha_SeMT_Simulation/01_project_case_study.md': '''# Odisha SeMT Simulation: Project Case Study

## Scenario
Implementation of an Integrated Citizen Service Delivery Platform for a fictional Odisha government department.

## Project Narrative
The department currently uses fragmented service applications and manual workflows for citizen requests, leading to delays and inconsistent data handling. The proposed digital platform will centralise service access, improve the citizen experience, and provide dashboards for monitoring performance.

## Lifecycle Stages
1. Initial departmental meeting
2. Requirement capture
3. Concept note preparation
4. DPR development
5. Budget estimation
6. RFP drafting
7. Technical evaluation
8. Vendor selection
9. Implementation
10. Monitoring and reporting
11. UAT and Go-Live
12. Closure and assessment
''',
    '11_Sample_Library/03_sample_library_manifest.md': '''# Sample Library Manifest

## Included categories
- Correspondence
- Project documentation
- Procurement
- Meeting notes
- Presentations
- Dashboards
- Communication examples

## Illustrative sample list
1. Official letter
2. D.O. letter
3. Circular
4. Memorandum
5. Office order
6. Concept note
7. DPR outline
8. BRD summary
9. Risk register
10. RFP framework
11. Evaluation report
12. MoM template
13. Project dashboard
14. Executive summary
15. Stakeholder email
''',
    '12_Assignments_Capstone/01_capstone_assignment.md': '''# Final Capstone Assignment

## Assignment Brief
Prepare a complete consultancy package for a fictional digital service initiative under a department of the Government of Odisha.

## Required outputs
- Concept note
- DPR
- RFP draft
- Project plan
- Risk register
- Three MoMs
- Monthly progress report
- Executive presentation
- Five professional emails
- Final review deck

## Evaluation Criteria
- Clarity and structure
- Formal tone and formatting
- Technical and financial completeness
- Evidence-based recommendations
- Stakeholder and decision fit
''',
}
for rel, content in module_docs.items():
    write_md(rel, content)

# Create actual Word docs
word_specs = [
    ('02_Government_Correspondence/official_letter_template.docx', 'Official Letter Template', ['To', 'The Principal Secretary', 'Department of Electronics & IT', 'Subject: Request for approval', 'Sir,', 'This is to submit the proposal...', 'Thanking you,', '[Name]']),
    ('03_Project_Documentation/project_charter_template.docx', 'Project Charter Template', ['Project Title', 'Objective', 'Scope', 'Stakeholders', 'Timeline', 'Budget', 'Governance', 'Risk Summary']),
    ('04_Tender_Procurement/rfp_template.docx', 'RFP Template', ['Invitation to Bid', 'Background', 'Scope of Work', 'Eligibility Criteria', 'Bid Evaluation', 'Commercial Terms', 'Submission Instructions'])
]
for file_path, title, paras in word_specs:
    doc = Document()
    doc.add_heading(title, level=0)
    for p in paras:
        doc.add_paragraph(p)
    doc.save(str(root / file_path))

# Create PowerPoint deck
prs = Presentation()
# slide 1
slide = prs.slides.add_slide(prs.slide_layouts[0])
slide.shapes.title.text = 'SeMT Monthly Review Meeting'
slide.placeholders[1].text = 'Integrated Citizen Service Delivery Platform\nDepartmental digital service initiative\nIllustrative data only'
# slide 2
slide = prs.slides.add_slide(prs.slide_layouts[5])
slide.shapes.title.text = 'Executive Summary'
content = slide.shapes.add_textbox(Inches(0.8), Inches(1.5), Inches(10), Inches(4.5))
text_frame = content.text_frame
for idx, txt in enumerate([
    '• Project status: On-track with 72% milestone completion',
    '• Budget status: 58% utilisation against plan',
    '• Risk watch: Data migration and vendor onboarding',
    '• Decision required: Approval for extension of UAT window',
]):
    para = text_frame.paragraphs[0] if idx == 0 else text_frame.add_paragraph()
    para.text = txt
    para.level = 0
# slides 3-5 more
for title, bullets in [
    ('Key Highlights', ['• 12 modules delivered', '• 3 interdepartmental reviews completed', '• Citizen service backlog reduced by 18%']),
    ('Budget and Timeline', ['• Budget: INR 3.4 crore', '• Variance: +4% against plan', '• Timeline: 14 months, 3 months remaining']),
    ('Risks and Mitigation', ['• Data migration risk', '• Vendor coordination risk', '• Cybersecurity readiness risk'])
]:
    slide = prs.slides.add_slide(prs.slide_layouts[5])
    slide.shapes.title.text = title
    content = slide.shapes.add_textbox(Inches(0.8), Inches(1.6), Inches(10), Inches(4.4))
    tf = content.text_frame
    for i, txt in enumerate(bullets):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.text = txt
prs.save(str(root / '05_PowerPoint_Presentations/SeMT_Monthly_Review_Deck.pptx'))

# Create workbook
wb = Workbook()
ws = wb.active
ws.title = 'Dashboard'
rows = [
    ['KPI', 'Target', 'Actual', 'Variance', 'Status'],
    ['Milestone Completion (%)', 80, 72, -8, 'Monitor'],
    ['Budget Utilisation (%)', 60, 58, -2, 'On track'],
    ['Vendor Performance Score', 90, 85, -5, 'Needs review'],
    ['Citizen Service Response Time', 48, 54, 6, 'Action needed'],
    ['UAT Completion (%)', 85, 80, -5, 'Monitor'],
]
for r in rows:
    ws.append(r)
for cell in ws['A1:E1'][0]:
    cell.font = Font(bold=True, color='FFFFFF')
    cell.fill = PatternFill('solid', fgColor='1F4E78')
for rows_range in ws.iter_rows(min_row=2, max_row=6, min_col=1, max_col=5):
    for c in rows_range:
        c.alignment = Alignment(horizontal='center')
ws.column_dimensions['A'].width = 28
ws.column_dimensions['B'].width = 14
ws.column_dimensions['C'].width = 14
ws.column_dimensions['D'].width = 14
ws.column_dimensions['E'].width = 16
wb.save(str(root / '08_Excel_Dashboards/project_dashboard.xlsx'))

# Create PDF reference manual
pdf_path = root / 'deliverables/course_reference_manual.pdf'
canvas_obj = canvas.Canvas(str(pdf_path), pagesize=A4)
canvas_obj.setTitle('Professional Documentation Reference Manual')
canvas_obj.setFillColor(navy)
c_canvas = canvas_obj
c_canvas.setFont('Helvetica-Bold', 18)
c_canvas.drawString(60, 800, 'Professional Documentation Reference Manual')
c_canvas.setFillColor(black)
c_canvas.setFont('Helvetica', 11)
line_y = 760
for text in [
    '1. Structure documents by purpose, audience, and action required.',
    '2. Keep facts, recommendations, and approvals clearly separated.',
    '3. Use formal language and a consistent government document style.',
    '4. Track version history and approval trail for all critical files.',
    '5. Prepare concise executive summaries and decision-ready presentations.',
    '6. Validate figures, assumptions, and procurement references before final submission.',
    '7. Align communication with the authority level of the recipient.',
    '8. Use professional templates and maintain continuity across the project lifecycle.'
]:
    c_canvas.drawString(70, line_y, text)
    line_y -= 28
c_canvas.setFillColor(teal)
c_canvas.setFont('Helvetica-Bold', 12)
c_canvas.drawString(60, 145, 'Illustrative government consulting guidance only')
canvas_obj.save()

# Create a readable repo index
write_md('00_MASTER_INDEX.md', '''# Master Index

## Repository Overview
This repository contains a structured 12-module government consulting and documentation course tailored to SeMT Odisha, e-Governance, and digital project environments.

## Module Directory Map
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

## Primary Files
- [README.md](README.md)
- [COURSE_CURRICULUM.md](COURSE_CURRICULUM.md)
- [12_WEEK_LEARNING_ROADMAP.md](12_WEEK_LEARNING_ROADMAP.md)
- [MASTER_DOCUMENTATION_INDEX.md](MASTER_DOCUMENTATION_INDEX.md)
- [SAMPLE_LIBRARY_INDEX.md](SAMPLE_LIBRARY_INDEX.md)
- [WEEK_01_COMPLETE_TRAINING.md](WEEK_01_COMPLETE_TRAINING.md)
- [WEEK_01_ASSIGNMENTS_EVALUATION.md](WEEK_01_ASSIGNMENTS_EVALUATION.md)

## Deliverables
- Document templates and sample files are available in the module folders.
- The PowerPoint deck and Excel dashboard are generated as editable files.
- PDF and reference manuals are stored in the deliverables folder.
''')

# update root README with stronger project framing
root_readme = root / 'README.md'
root_readme.write_text('''# MASTER OF PROFESSIONAL DOCUMENTATION, PRESENTATION & COMMUNICATION

## Government and e-Governance Consulting Edition

This repository is a professional training course framework for government technology consultants working in the Odisha e-Governance context, SeMT, NeGD, and digital government environments.

## Included materials
- 12-week learning roadmap
- 12 modules for documentation, correspondence, project work, procurement, presentations, communication, meetings, and reporting
- Realistic, fictional project case study for an Odisha department
- Sample library, templates, and assignment pack
- Executive presentation, dashboard, and reference PDF

## Repository structure
- [00_MASTER_INDEX.md](00_MASTER_INDEX.md)
- [COURSE_CURRICULUM.md](COURSE_CURRICULUM.md)
- [12_WEEK_LEARNING_ROADMAP.md](12_WEEK_LEARNING_ROADMAP.md)
- [MASTER_DOCUMENTATION_INDEX.md](MASTER_DOCUMENTATION_INDEX.md)
- [SAMPLE_LIBRARY_INDEX.md](SAMPLE_LIBRARY_INDEX.md)
- [WEEK_01_COMPLETE_TRAINING.md](WEEK_01_COMPLETE_TRAINING.md)
- [WEEK_01_ASSIGNMENTS_EVALUATION.md](WEEK_01_ASSIGNMENTS_EVALUATION.md)
- [01_Fundamentals](01_Fundamentals)
- [02_Government_Correspondence](02_Government_Correspondence)
- [03_Project_Documentation](03_Project_Documentation)
- [04_Tender_Procurement](04_Tender_Procurement)
- [05_PowerPoint_Presentations](05_PowerPoint_Presentations)
- [06_Professional_Communication](06_Professional_Communication)
- [07_Meeting_Management](07_Meeting_Management)
- [08_Excel_Dashboards](08_Excel_Dashboards)
- [09_AI_Tools](09_AI_Tools)
- [10_Odisha_SeMT_Simulation](10_Odisha_SeMT_Simulation)
- [11_Sample_Library](11_Sample_Library)
- [12_Assignments_Capstone](12_Assignments_Capstone)
- [deliverables](deliverables)

## Important note
All names, department references, budgets, dates, and project scenarios in this repository are fictional and illustrative, intended for training and learning, and are not official government orders, policy references, or tender notices.
''', encoding='utf-8')

print('Generated course assets successfully.')
