# Sales & Project Management Department - SharePoint Site Design

## Purpose
This document outlines the SharePoint Online site architecture for the Sales & Project Management Department in a manufacturing environment, following Microsoft best practices for document management, security, and collaboration.

---

## Design Principles

1. **Flat Structure** - Minimize folder depth, use metadata for organization
2. **Customer-Centric** - Easy access to all documents for a specific customer
3. **Order-to-Project Traceability** - Link sales orders to project execution
4. **Phase-Based Views** - Filter by sales stage or project phase
5. **Security by Design** - Separate confidential content with proper permissions
6. **Scalability** - Design for growth and multiple concurrent orders/projects
7. **Compliance Ready** - Support retention policies and audit requirements

---

## Site Architecture Overview

```
Sales & Project Management Department (Team Site)
│
├── SALES LIBRARIES (7)
│   ├── Quotations & Proposals
│   ├── Sales Orders
│   ├── Customer Documents
│   ├── Delivery Documents
│   ├── Customer Complaints
│   ├── Sales Reports
│   └── Price Lists (Restricted)
│
├── PROJECT LIBRARIES (13)
│   ├── Project Initiation
│   ├── Project Planning
│   ├── Status Reports
│   ├── Meeting Documents
│   ├── Risk & Issues
│   ├── Change Requests
│   ├── Technical Documents
│   ├── Test Documents
│   ├── Vendor Documents
│   ├── Project Closure
│   ├── Training & SOPs
│   ├── Templates
│   └── Confidential (Restricted)
│
├── LISTS (9)
│   ├── Customer Master
│   ├── Project Master
│   ├── Sales Pipeline
│   ├── Order Tracker
│   ├── Risk Register
│   ├── Issue Log
│   ├── Action Items
│   ├── Lessons Learned
│   └── Calendar
│
├── Microsoft 365 Integrations
│   ├── Microsoft Planner
│   ├── OneNote Notebook
│   └── Microsoft Teams
│
└── Pages
    ├── Home (Dashboard)
    ├── Sales Dashboard
    ├── Project Portfolio
    └── Resources
```

---

# PART A: SALES DOCUMENT LIBRARIES

## S1. Quotations & Proposals

**Purpose:** Store sales quotations, technical proposals, and tender documents.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/QuotationsProposals` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Sales Quotation | Standard price quotation |
| Technical Proposal | Detailed technical proposal |
| Tender Response | Formal tender submission |
| Framework Agreement | Long-term pricing agreement |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Quotations | None | Default view |
| By Customer | Group by Customer Name | Customer-based search |
| By Sales Person | Group by Sales Person | Rep's quotations |
| Pending | Quotation Status = Sent, Under Review | Active quotations |
| Expiring Soon | Valid Until = Next 14 Days | Follow-up needed |
| Won | Quotation Status = Won | Successful quotes |
| Lost | Quotation Status = Lost | Analysis |
| This Month | Document Date = This Month | Current activity |
| By Value | Sort by Total Value DESC | High-value first |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Sales Team | Contribute |
| Project Managers | Read |
| Management | Read |

---

## S2. Sales Orders

**Purpose:** Store sales orders, customer POs, order acknowledgments, and contracts.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/SalesOrders` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Sales Order | Internal sales order document |
| Customer PO | Received customer purchase order |
| Order Acknowledgment | Confirmation sent to customer |
| Sales Contract | Formal sales agreement |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Orders | None | Default view |
| By Customer | Group by Customer Name | Customer-based search |
| By Status | Group by Order Status | Status-based tracking |
| Active Orders | Order Status != Closed | Current orders |
| Pending Delivery | Order Status = Ready, In Production | Delivery planning |
| This Month | Document Date = This Month | Current activity |
| By Delivery Date | Sort by Delivery Date ASC | Upcoming deliveries |
| By Sales Person | Group by Sales Person | Rep's orders |
| Linked to Projects | Linked Project != Empty | Orders with projects |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Sales Team | Contribute |
| Project Managers | Read |
| Operations | Read |

---

## S3. Customer Documents

**Purpose:** Store customer-provided documents including specifications, drawings, agreements, and correspondence.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/CustomerDocuments` |
| Versioning | Major versions only, keep 30 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Customer Specification | Technical requirements |
| Customer Drawing | Engineering drawings |
| Customer Agreement | NDAs, quality agreements |
| Customer Correspondence | Emails, letters, memos |
| Visit Report | Customer visit documentation |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Customer | Group by Customer Name | Customer-based search |
| By Category | Group by Document Category | Type-based search |
| Specifications | Document Category = Specification | Specs only |
| Drawings | Document Category = Drawing | Drawings only |
| Recent | Modified = Last 30 Days | Recent documents |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Sales Team | Contribute |
| Project Managers | Contribute |
| Engineers | Read |

---

## S4. Delivery Documents

**Purpose:** Store delivery orders, packing lists, shipping documents, and proof of delivery.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/DeliveryDocuments` |
| Versioning | Major versions only, keep 30 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Delivery Order | DO issued for shipment |
| Packing List | Detailed packing list |
| Bill of Lading | Shipping document |
| Proof of Delivery | Signed delivery confirmation |
| Shipping Invoice | Commercial invoice |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Customer | Group by Customer Name | Customer-based search |
| By Status | Group by Delivery Status | Status tracking |
| Pending Shipment | Delivery Status = Pending | To be shipped |
| In Transit | Delivery Status = In Transit | Tracking |
| Delivered | Delivery Status = Delivered | Completed |
| This Month | Delivery Date = This Month | Current activity |
| Missing POD | Delivery Status = Delivered AND Proof of Delivery = Empty | Follow-up needed |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Sales Team | Contribute |
| Logistics | Contribute |
| Operations | Read |

---

## S5. Customer Complaints

**Purpose:** Store customer complaints, returns, RMAs, and resolution documentation.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/CustomerComplaints` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Complaint Report | Initial complaint documentation |
| Investigation Report | Root cause analysis |
| Corrective Action | CAPA documentation |
| RMA Document | Return authorization |
| Credit Note | Credit adjustment |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Complaints | None | Default view |
| By Customer | Group by Customer Name | Customer-based search |
| By Status | Group by Complaint Status | Status tracking |
| Open | Complaint Status = Open, Investigating | Active complaints |
| Critical/Major | Severity = Critical, Major | Priority issues |
| By Type | Group by Complaint Type | Category analysis |
| This Month | Complaint Date = This Month | Current activity |
| By Sales Order | Group by Sales Order Number | Order-linked issues |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Sales Team | Contribute |
| Quality Team | Contribute |
| Project Managers | Read |

---

## S6. Sales Reports

**Purpose:** Store sales reports, forecasts, pipeline reports, and performance analysis.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/SalesReports` |
| Versioning | Major versions only, keep 30 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Pipeline Report | Sales pipeline status |
| Forecast Report | Sales forecast |
| Performance Report | Sales performance analysis |
| Win/Loss Report | Quote conversion analysis |
| Territory Report | Regional sales report |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Reports | None | Default view |
| By Type | Group by Report Type | Type-based search |
| By Period | Group by Report Period | Period-based search |
| Monthly | Report Frequency = Monthly | Monthly reports |
| Quarterly | Report Frequency = Quarterly | Quarterly reports |
| This Year | Report Period contains current year | Current year |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Sales Team | Contribute |
| Management | Read |

---

## S7. Price Lists (Restricted)

**Purpose:** Store price lists, discount structures, cost sheets, and margin analysis. **Restricted access.**

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/PriceLists` |
| Versioning | Major versions only, keep 20 versions |
| Check-out | Required |
| Content Approval | Yes |
| **Unique Permissions** | **Yes - Break inheritance** |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Price List | Standard price list |
| Discount Matrix | Discount structures |
| Cost Sheet | Product costing |
| Margin Analysis | Profitability analysis |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| Active | Price List Status = Active | Current price lists |
| By Product Line | Group by Product Line | Product-based search |
| By Currency | Group by Currency | Currency-based search |
| Expiring | Expiry Date = Next 30 Days | Review needed |

**Permissions (Restricted):**
| Group | Permission Level |
|-------|------------------|
| Sales Managers | Full Control |
| Senior Sales | Read |
| Sales Team | **No Access** |
| Management | Read |

---

# PART B: PROJECT DOCUMENT LIBRARIES

## P1. Project Initiation

**Purpose:** Store project charters, proposals, business cases, and feasibility studies.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/ProjectInitiation` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Project Charter | Project authorization document |
| Business Case | Justification and ROI analysis |
| Project Proposal | Initial project request |
| Feasibility Study | Technical/financial feasibility |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Customer | Group by Customer Name | Customer projects |
| By Category | Group by Project Category | Category-based search |
| Pending Approval | Approval Status = Pending | Approval queue |
| Approved | Approval Status = Approved | Approved charters |
| Linked to Sales Order | Linked Sales Order != Empty | Customer projects |
| By Project Phase | Group by Project Phase | Phase-based view |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Sales Managers | Read |
| Team Members | Read |

---

## P2. Project Planning

**Purpose:** Store project plans, schedules, WBS, resource plans, and planning documents.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/ProjectPlanning` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Master Project Plan | Overall project plan/schedule |
| Detailed Schedule | Detailed work breakdown |
| Resource Plan | Resource allocation |
| Communication Plan | Stakeholder communication |
| Risk Management Plan | Risk management approach |
| Quality Plan | Quality management approach |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Plan Type | Group by Plan Type | Type-based search |
| Latest Versions | Document Status = Final | Current approved plans |
| Working Drafts | Document Status = Draft | Work in progress |
| By Project Phase | Group by Project Phase | Phase-based view |
| Excel Schedules | File Type = .xlsx | Schedule files only |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Team Members | Read |

---

## P3. Status Reports

**Purpose:** Store project status reports, progress reports, and dashboard snapshots.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/StatusReports` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Weekly Status Report | Weekly progress update |
| Monthly Status Report | Monthly summary report |
| Executive Summary | Management-level summary |
| Customer Status Report | Report for customer |
| Dashboard Snapshot | Point-in-time metrics |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Reports | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Customer | Group by Customer Name | Customer projects |
| Weekly Reports | Report Type = Weekly | Weekly updates |
| Monthly Reports | Report Type = Monthly | Monthly summaries |
| Customer Reports | Report Type = Customer Status Report | Customer-facing |
| Red/Yellow Status | Overall Status = Red OR Yellow | At-risk projects |
| This Month | Document Date = This Month | Current month |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Sales Managers | Read |
| Team Members | Read |

---

## P4. Meeting Documents

**Purpose:** Store meeting minutes, agendas, and presentation materials.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/MeetingDocuments` |
| Versioning | Major versions only, keep 30 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Meeting Minutes | Minutes of meeting |
| Meeting Agenda | Pre-meeting agenda |
| Presentation | Meeting presentations |
| Customer Meeting Notes | Customer meeting documentation |
| Workshop Materials | Workshop/training materials |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Customer | Group by Customer Name | Customer meetings |
| By Meeting Type | Group by Meeting Type | Type-based search |
| Customer Meetings | Meeting Type = Customer Meeting | Customer meetings |
| Gate Reviews | Meeting Type = Gate Review | Gate review meetings |
| Recent (30 days) | Meeting Date >= Today-30 | Recent meetings |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Sales Team | Contribute |
| Team Members | Contribute |

---

## P5. Risk & Issues

**Purpose:** Store risk assessments, risk registers, and issue documentation.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/RiskIssues` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Risk Register | Project risk register |
| Risk Assessment | Detailed risk analysis |
| Issue Log | Project issue log |
| Issue Report | Detailed issue analysis |
| Mitigation Plan | Risk/issue mitigation actions |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| High Risks | Risk Level = High | Priority risks |
| Customer-Related | Risk/Issue Category = Customer | Customer issues |
| Open Items | Document Status != Closed | Active items |
| By Category | Group by Risk/Issue Category | Category-based view |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Team Members | Contribute |

---

## P6. Change Requests

**Purpose:** Store change requests, change orders, and impact assessments.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/ChangeRequests` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Change Request | Formal change request |
| Customer Change Request | Customer-initiated change |
| Change Impact Assessment | Impact analysis |
| Engineering Change Order | Technical change order |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| Pending Approval | Approval Status = Pending | Approval queue |
| Customer Changes | Change Type = Customer Request | Customer-initiated |
| Approved Changes | Approval Status = Approved | Approved changes |
| High Priority | Change Priority = Critical, High | Priority changes |
| Requires Customer Approval | Customer Approval Required = Yes | Customer sign-off needed |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Sales Managers | Read |
| Change Control Board | Contribute |

---

## P7. Technical Documents

**Purpose:** Store technical specifications, requirements, design documents, and engineering files.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/TechnicalDocuments` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Requirements Document | Functional/technical requirements |
| Technical Specification | Detailed specifications |
| Design Document | Engineering/system design |
| Equipment Specification | Equipment requirements |
| Customer Specification | Customer-provided specs |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Specification Type | Group by Specification Type | Type-based search |
| Customer Approved | Customer Approved = Yes | Customer-signed specs |
| Approved/Released | Review Status = Released | Released documents |
| Under Review | Review Status = Under Review | Review queue |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Engineers | Contribute |
| Team Members | Read |

---

## P8. Test Documents

**Purpose:** Store test plans, test cases, test results, and validation records.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/TestDocuments` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Test Plan | Testing approach and scope |
| Test Cases | Detailed test cases |
| Test Report | Test execution results |
| FAT Report | Factory Acceptance Test |
| SAT Report | Site Acceptance Test |
| Customer Witness Report | Customer-witnessed tests |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Test Type | Group by Test Type | Type-based search |
| Customer Witnessed | Customer Witnessed = Yes | Customer-witnessed |
| Test Plans | Document Type = Test Plan | Test plans only |
| Failed Tests | Test Result = Fail | Failed tests |
| FAT/SAT | Test Type = FAT, SAT | Acceptance tests |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| QA Team | Contribute |
| Team Members | Read |

---

## P9. Vendor Documents

**Purpose:** Store vendor quotations, contracts, purchase orders, and vendor correspondence.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/VendorDocuments` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Vendor Quotation | Price quotations |
| Vendor Contract | Vendor agreements |
| Purchase Order | PO documents |
| Vendor Evaluation | Vendor assessment |
| Technical Submittal | Vendor technical documents |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Vendor | Group by Vendor Name | Vendor-based search |
| Active Quotations | Valid Until >= Today | Valid quotations |
| Contracts | Document Category = Contract | Contracts only |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Procurement | Contribute |
| Team Members | Read |

---

## P10. Project Closure

**Purpose:** Store closure reports, lessons learned, handover documents, and post-implementation reviews.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/ProjectClosure` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Project Closure Report | Final closure documentation |
| Lessons Learned | Project learnings |
| Handover Document | Operational handover |
| Customer Sign-off | Customer acceptance |
| Post-Implementation Review | PIR assessment |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Customer | Group by Customer Name | Customer projects |
| Lessons Learned | Document Type = Lessons Learned | Knowledge base |
| Pending Sign-off | Sign-off Status = Pending | Awaiting closure |
| Customer Sign-offs | Document Type = Customer Sign-off | Customer acceptances |
| Successful Projects | Overall Assessment = Successful | Best practices |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Sales Managers | Read |
| Team Members | Read |

---

## P11. Training & SOPs

**Purpose:** Store training materials, user manuals, SOPs, and process documentation.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/TrainingSOPs` |
| Versioning | Major versions only, keep 30 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Training Material | Training presentations/guides |
| User Manual | End-user documentation |
| SOP | Standard operating procedure |
| Work Instruction | Step-by-step instructions |
| Customer Training | Customer training materials |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Project | Group by Project Name | Project-based search |
| By Category | Group by Document Category | Type-based search |
| Customer Training | Document Category = Customer Training | Customer materials |
| Current Version | Document Status = Final | Active documents |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| PMO Owners | Full Control |
| Project Managers | Contribute |
| Team Members | Read |

---

## P12. Templates

**Purpose:** Central repository for reusable document templates.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/Templates` |
| Versioning | Major versions only, keep 20 versions |
| Check-out | Required |
| Content Approval | Yes |

**Template Categories:**
| Category | Templates Included |
|----------|-------------------|
| Sales | Quotation, Proposal, Order Acknowledgment, Visit Report |
| Project Initiation | Project Charter, Business Case, Project Proposal |
| Project Planning | Project Plan, WBS, Resource Plan, Communication Plan |
| Execution | Status Report, Meeting Agenda, Meeting Minutes |
| Monitoring | Change Request, Risk Register, Issue Log, Action Tracker |
| Closure | Closure Report, Lessons Learned, Handover Checklist |
| General | Presentation Template, Email Template |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Templates | None | Default view |
| By Category | Group by Template Category | Category-based search |
| Sales Templates | Template Category = Sales | Sales templates |
| Project Templates | Template Category != Sales | Project templates |
| Recently Updated | Modified = Last 30 Days | Recent changes |

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Site Owners | Full Control |
| Template Owners | Contribute |
| All Users | Read |

---

## P13. Confidential (Restricted)

**Purpose:** Store highly confidential project documents including strategic projects, pricing-sensitive information.

| Setting | Value |
|---------|-------|
| URL | `/sites/salespm/Confidential` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required |
| **Unique Permissions** | **Yes - Break inheritance** |

**Permissions (Restricted):**
| Group | Permission Level |
|-------|------------------|
| Site Owners | Full Control |
| Sales Managers | Contribute |
| PMO Owners | Contribute |
| Executive Team | Read |
| All Others | **No Access** |

---

# PART C: SHAREPOINT LISTS

## L1. Customer Master

**Purpose:** Central registry of customers for lookup and customer management.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Customer Code | Text | Yes | Unique identifier (CUST-NNNN) |
| Customer Name | Text | Yes | Official company name |
| Customer Type | Choice | Yes | OEM, Distributor, End User, Government |
| Industry | Choice | No | Manufacturing, Oil & Gas, Electronics, etc. |
| Region/Territory | Choice | No | Sales territory |
| Sales Person | Person | No | Assigned sales rep |
| Contact Person | Text | No | Primary contact name |
| Contact Email | Text | No | Primary contact email |
| Contact Phone | Text | No | Primary contact phone |
| Address | Multiple lines | No | Business address |
| Payment Terms | Choice | No | Net 30, Net 60, etc. |
| Credit Limit | Currency | No | Approved credit limit |
| Customer Status | Choice | Yes | Active, Inactive, Prospect |

**Views:** All Customers, Active Customers, By Region, By Sales Person, By Industry, My Customers

---

## L2. Project Master

**Purpose:** Central registry of all projects for lookup and portfolio tracking.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Project Code | Text | Yes | Unique identifier (PRJ-YYYY-NNN) |
| Project Name | Text | Yes | Full project name |
| Project Category | Choice | Yes | Customer Project, NPD, Process Improvement, etc. |
| Customer | Lookup | No | Link to Customer Master |
| Sales Order | Text | No | Originating sales order number |
| Project Sponsor | Person | Yes | Executive sponsor |
| Project Manager | Person | Yes | Assigned PM |
| Plant/Location | Choice | No | Manufacturing plant |
| Start Date | Date | Yes | Planned start |
| End Date | Date | Yes | Planned end |
| Budget | Currency | No | Approved budget |
| Project Status | Choice | Yes | Active, On Hold, Completed, Cancelled |
| Current Phase | Choice | Yes | P1-P8 phases |
| Priority | Choice | No | High, Medium, Low |
| Overall Health | Choice | No | Green, Yellow, Red |

**Views:** All Projects, Active Projects, By Customer, By Category, By Manager, By Status, My Projects, Customer Projects

---

## L3. Sales Pipeline

**Purpose:** Track sales opportunities from lead to order.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Opportunity ID | Text | Yes | OPP-YYYY-NNNN |
| Opportunity Name | Text | Yes | Description |
| Customer | Lookup | Yes | Link to Customer Master |
| Sales Stage | Choice | Yes | Lead, Qualification, Quotation, Negotiation, Won, Lost |
| Estimated Value | Currency | Yes | Potential order value |
| Currency | Choice | Yes | MYR, USD, SGD, EUR |
| Probability | Number | No | Win probability % |
| Expected Close | Date | Yes | Target close date |
| Sales Person | Person | Yes | Assigned sales rep |
| Product Line | Choice | No | Product category |
| Competitor | Text | No | Main competitor |
| Next Action | Text | No | Next step required |
| Notes | Multiple lines | No | Additional notes |

**Views:** All Opportunities, By Stage, By Sales Person, By Customer, Hot Leads, Closing This Month, Won, Lost

---

## L4. Order Tracker

**Purpose:** Track sales orders from confirmation to delivery.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Sales Order | Text | Yes | SO-YYYY-NNNN |
| Customer | Lookup | Yes | Link to Customer Master |
| Order Date | Date | Yes | Order confirmation date |
| Order Value | Currency | Yes | Order value |
| Delivery Date (Required) | Date | Yes | Customer required date |
| Delivery Date (Promised) | Date | No | Committed delivery date |
| Order Status | Choice | Yes | Confirmed, In Production, Ready, Shipped, Delivered, Invoiced |
| Linked Project | Lookup | No | Link to Project Master |
| Sales Person | Person | Yes | Sales rep |
| Notes | Multiple lines | No | Order notes |

**Views:** All Orders, Active Orders, By Customer, By Status, Pending Delivery, This Week, Overdue, By Sales Person

---

## L5. Risk Register

**Purpose:** Track and manage project risks across all projects.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Risk ID | Text | Yes | RISK-PRJ-NNN |
| Project | Lookup | Yes | Link to Project Master |
| Risk Title | Text | Yes | Brief description |
| Risk Description | Multiple lines | Yes | Detailed description |
| Risk Category | Choice | Yes | Technical, Schedule, Cost, Resource, Quality, Customer, External, Safety |
| Probability | Choice | Yes | High, Medium, Low |
| Impact | Choice | Yes | High, Medium, Low |
| Risk Score | Calculated | Auto | Probability x Impact |
| Risk Response | Choice | Yes | Avoid, Mitigate, Transfer, Accept |
| Mitigation Action | Multiple lines | No | Mitigation plan |
| Risk Owner | Person | Yes | Responsible person |
| Status | Choice | Yes | Open, Mitigating, Closed |
| Due Date | Date | No | Target resolution date |

**Views:** All Risks, Open Risks, High Risks, By Project, By Category, By Owner, Customer-Related

---

## L6. Issue Log

**Purpose:** Track and manage project issues across all projects.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Issue ID | Text | Yes | ISS-PRJ-NNN |
| Project | Lookup | Yes | Link to Project Master |
| Issue Title | Text | Yes | Brief description |
| Issue Description | Multiple lines | Yes | Detailed description |
| Issue Category | Choice | Yes | Technical, Resource, Vendor, Customer, Quality, Schedule, Scope |
| Priority | Choice | Yes | Critical, High, Medium, Low |
| Impact | Choice | Yes | High, Medium, Low |
| Resolution Plan | Multiple lines | No | How to resolve |
| Issue Owner | Person | Yes | Responsible person |
| Status | Choice | Yes | Open, In Progress, Resolved, Closed |
| Raised Date | Date | Yes | When raised |
| Target Resolution | Date | No | Target date |

**Views:** All Issues, Open Issues, Critical Issues, By Project, By Category, Customer Issues, Overdue

---

## L7. Action Items

**Purpose:** Track action items from meetings and reviews.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Action ID | Text | Yes | ACT-NNN |
| Source | Choice | Yes | Project, Sales, Meeting, Risk, Issue, Customer |
| Project | Lookup | No | Link to Project Master |
| Customer | Lookup | No | Link to Customer Master |
| Action Description | Text | Yes | What needs to be done |
| Assigned To | Person | Yes | Who is responsible |
| Priority | Choice | Yes | High, Medium, Low |
| Due Date | Date | Yes | Target completion |
| Status | Choice | Yes | Open, In Progress, Completed |
| Notes | Multiple lines | No | Additional notes |

**Views:** All Actions, My Actions, Open Actions, Overdue, By Project, By Customer, Due This Week

---

## L8. Lessons Learned

**Purpose:** Capture and share project learnings for continuous improvement.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Lesson ID | Text | Yes | LL-YYYY-NNN |
| Project | Lookup | Yes | Link to Project Master |
| Customer | Lookup | No | Link to Customer Master |
| Lesson Title | Text | Yes | Brief description |
| Category | Choice | Yes | What Went Well, What Could Improve, Recommendation |
| Area | Choice | Yes | Sales, Planning, Execution, Communication, Technical, Vendor, Customer |
| Description | Multiple lines | Yes | Detailed lesson |
| Recommendation | Multiple lines | No | Suggested action |
| Submitted By | Person | Yes | Who submitted |
| Submitted Date | Date | Yes | When submitted |

**Views:** All Lessons, By Project, By Customer, By Category, By Area, What Went Well, Recommendations

---

## L9. Calendar

**Purpose:** Track project milestones, customer events, and important dates.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Event Title | Text | Yes | Name of event |
| Event Type | Choice | Yes | Milestone, Deadline, Customer Meeting, Review, Delivery, Gate |
| Project | Lookup | No | Link to Project Master |
| Customer | Lookup | No | Link to Customer Master |
| Start Date | Date/Time | Yes | Event start |
| End Date | Date/Time | No | Event end |
| Location | Text | No | Location |
| Description | Multiple lines | No | Event details |
| Status | Choice | No | Scheduled, Completed, Cancelled |

**Views:** Calendar View, All Events, By Project, By Customer, Upcoming, Milestones, Customer Meetings

---

# PART D: PERMISSIONS & SECURITY

## Security Groups

| Group Name | Members | Description |
|------------|---------|-------------|
| Site Owners | Department Head, IT Admin | Full control of entire site |
| Sales Managers | Sales Manager, Senior Sales | Full control of sales content |
| Sales Team | All Sales Staff | Standard sales access |
| PMO Owners | PMO Director, Senior PM | Full control of project content |
| Project Managers | All Project Managers | Manage project documents |
| Team Members | Project team staff | Standard project access |
| Engineers | Engineering staff | Technical document access |
| QA Team | Quality assurance staff | Test document access |
| Procurement | Procurement staff | Vendor document access |
| Logistics | Logistics/shipping staff | Delivery document access |
| Management | Directors, VPs | Read access to most content |
| External Customers | Customer contacts | Limited, time-bound access |

---

## Permission Matrix - Sales Libraries

| Library | Sales Managers | Sales Team | Project Managers | Management |
|---------|----------------|------------|------------------|------------|
| Quotations & Proposals | Full Control | Contribute | Read | Read |
| Sales Orders | Full Control | Contribute | Read | Read |
| Customer Documents | Full Control | Contribute | Contribute | Read |
| Delivery Documents | Full Control | Contribute | Read | Read |
| Customer Complaints | Full Control | Contribute | Read | Read |
| Sales Reports | Full Control | Contribute | Read | Read |
| **Price Lists** | Full Control | **No Access** | **No Access** | Read |

---

## Permission Matrix - Project Libraries

| Library | PMO Owners | Project Managers | Sales Managers | Team Members |
|---------|------------|------------------|----------------|--------------|
| Project Initiation | Full Control | Contribute | Read | Read |
| Project Planning | Full Control | Contribute | Read | Read |
| Status Reports | Full Control | Contribute | Read | Read |
| Meeting Documents | Full Control | Contribute | Read | Contribute |
| Risk & Issues | Full Control | Contribute | Read | Contribute |
| Change Requests | Full Control | Contribute | Read | Read |
| Technical Documents | Full Control | Contribute | Read | Read |
| Test Documents | Full Control | Contribute | Read | Read |
| Vendor Documents | Full Control | Contribute | Read | Read |
| Project Closure | Full Control | Contribute | Read | Read |
| Training & SOPs | Full Control | Contribute | Read | Read |
| Templates | Full Control | Read | Read | Read |
| **Confidential** | Full Control | **Per Project** | Contribute | **No Access** |

---

# PART E: NAVIGATION & HOME PAGE

## Left Navigation

```
🏠 HOME
─────────────────────────────
📊 SALES
─────────────────────────────
   Quotations & Proposals
   Sales Orders
   Customer Documents
   Delivery Documents
   Customer Complaints
   Sales Reports
   Price Lists (if access)
─────────────────────────────
📁 PROJECTS
─────────────────────────────
   Project Initiation
   Project Planning
   Status Reports
   Meeting Documents
   Risk & Issues
   Change Requests
   Technical Documents
   Test Documents
   Vendor Documents
   Project Closure
   Training & SOPs
   Templates
   Confidential (if access)
─────────────────────────────
📋 LISTS
─────────────────────────────
   Customer Master
   Project Master
   Sales Pipeline
   Order Tracker
   Risk Register
   Issue Log
   Action Items
   Lessons Learned
   Calendar
─────────────────────────────
🔗 MICROSOFT 365
─────────────────────────────
   Planner Board
   Team Notebook
   Teams Channel
─────────────────────────────
📚 RESOURCES
─────────────────────────────
   Templates
   Guidelines
   Help & Support
```

---

## Home Page Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  SALES & PROJECT MANAGEMENT                                  [🔍 SEARCH]│
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐│
│  │ 📢 NEWS & ANNOUNCEMENTS                                             ││
│  └─────────────────────────────────────────────────────────────────────┘│
│                                                                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐           │
│  │ 💰 SALES        │ │ 📊 PROJECTS     │ │ ✅ MY ACTIONS   │           │
│  │ PIPELINE        │ │ OVERVIEW        │ │                 │           │
│  │                 │ │                 │ │ [Action items   │           │
│  │ Open Quotes: 12 │ │ Active: 8       │ │  assigned to    │           │
│  │ Value: RM 2.5M  │ │ 🔴 Red: 1       │ │  current user]  │           │
│  │ Closing: 3      │ │ 🟡 Yellow: 2    │ │                 │           │
│  │                 │ │ 🟢 Green: 5     │ │ Due Today: 3    │           │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘           │
│                                                                         │
│  ┌──────────────────────────────────────┐ ┌────────────────────────────┐│
│  │ 📋 ACTIVE ORDERS                     │ │ 📅 UPCOMING EVENTS         ││
│  │                                      │ │                            ││
│  │ [Order Tracker - Active orders]      │ │ [Calendar - Next 14 days]  ││
│  │                                      │ │                            ││
│  └──────────────────────────────────────┘ └────────────────────────────┘│
│                                                                         │
│  ┌──────────────────────────────────────┐ ┌────────────────────────────┐│
│  │ 📄 RECENT DOCUMENTS                  │ │ ⚠️ ATTENTION NEEDED        ││
│  │                                      │ │                            ││
│  │ [Recently modified documents]        │ │ Expiring Quotes: 5         ││
│  │                                      │ │ Open Complaints: 3         ││
│  │                                      │ │ High Risks: 2              ││
│  │                                      │ │ Overdue Actions: 4         ││
│  └──────────────────────────────────────┘ └────────────────────────────┘│
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐│
│  │ 🔗 QUICK LINKS                                                      ││
│  │                                                                     ││
│  │ [New Quote] [New Order] [New Project] [Templates] [Pipeline Report] ││
│  └─────────────────────────────────────────────────────────────────────┘│
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

# PART F: RETENTION POLICIES

## Sales Documents

| Library | Retention Period | Action | Basis |
|---------|------------------|--------|-------|
| Quotations & Proposals | 7 years | Archive → Delete | Commercial records |
| Sales Orders | 7 years after order close | Archive → Delete | Tax/Audit |
| Customer Documents | 10 years | Archive only | Customer relationship |
| Delivery Documents | 7 years | Archive → Delete | Tax/Audit |
| Customer Complaints | 10 years | Archive only | Quality/Legal |
| Sales Reports | 7 years | Archive → Delete | Internal policy |
| Price Lists | Current + 3 years | Archive → Delete | Commercial |

## Project Documents

| Library | Retention Period | Action | Basis |
|---------|------------------|--------|-------|
| Project Initiation | 10 years after project close | Archive → Delete | Audit |
| Project Planning | 7 years after project close | Archive → Delete | Internal |
| Status Reports | 5 years after project close | Archive → Delete | Internal |
| Meeting Documents | 5 years after project close | Archive → Delete | Internal |
| Risk & Issues | 7 years after project close | Archive → Delete | Internal |
| Change Requests | 10 years after project close | Archive → Delete | Audit |
| Technical Documents | 10 years or product lifecycle | Archive only | Regulatory |
| Test Documents | 10 years or product lifecycle | Archive only | Regulatory |
| Vendor Documents | 7 years after contract expiry | Archive → Delete | Legal |
| Project Closure | 10 years after project close | Archive → Delete | Audit |
| Training & SOPs | Current + 5 years | Archive → Delete | Internal |
| Templates | Permanent | Archive only | Governance |
| Confidential | Extended hold | Archive only | Legal |

---

# PART G: IMPLEMENTATION CHECKLIST

## Phase 1: Site Creation
| Task | Owner | Status |
|------|-------|--------|
| Create Team Site | IT Admin | |
| Configure site settings | IT Admin | |
| Set site branding | IT Admin | |
| Create security groups | IT Admin | |

## Phase 2: Sales Libraries
| Task | Owner | Status |
|------|-------|--------|
| Create 7 sales libraries | IT Admin | |
| Configure metadata columns | IT Admin | |
| Create content types | IT Admin | |
| Set permissions | IT Admin | |
| Create views | Sales Manager | |

## Phase 3: Project Libraries
| Task | Owner | Status |
|------|-------|--------|
| Create 13 project libraries | IT Admin | |
| Configure metadata columns | IT Admin | |
| Create content types | IT Admin | |
| Set permissions | IT Admin | |
| Create views | PMO | |

## Phase 4: Lists
| Task | Owner | Status |
|------|-------|--------|
| Create Customer Master | Sales Manager | |
| Create Project Master | PMO | |
| Create Sales Pipeline | Sales Manager | |
| Create Order Tracker | Sales Manager | |
| Create Risk Register | PMO | |
| Create Issue Log | PMO | |
| Create Action Items | PMO | |
| Create Lessons Learned | PMO | |
| Create Calendar | PMO | |
| Import existing data | Both | |

## Phase 5: Integration
| Task | Owner | Status |
|------|-------|--------|
| Set up Planner | IT Admin | |
| Create OneNote notebook | IT Admin | |
| Create Teams team/channels | IT Admin | |
| Configure Power Automate flows | IT Admin | |

## Phase 6: Migration
| Task | Owner | Status |
|------|-------|--------|
| Audit existing files | Both | |
| Clean up unnecessary files | Both | |
| Migrate sales documents | Sales | |
| Migrate project documents | PMO | |
| Apply metadata | Both | |
| Verify completeness | Both | |

## Phase 7: Training & Go-Live
| Task | Owner | Status |
|------|-------|--------|
| Prepare training materials | Both | |
| Conduct training sessions | Both | |
| Pilot with select team | Both | |
| Go-live | Both | |
| Post-go-live support | IT Admin | |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-02-06 | Migration Team | Initial version - Sales & Project Management combined |
