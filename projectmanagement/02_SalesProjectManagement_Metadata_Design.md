# Sales & Project Management Department - Metadata Design Specification

## Purpose
This document defines the recommended metadata schema for Sales & Project Management department documents in SharePoint Online. Proper metadata enables efficient search, filtering, order/project tracking, and compliance reporting in a manufacturing environment.

---

## Metadata Design Principles

1. **Simplicity** - Only capture metadata that adds value (avoid over-engineering)
2. **Searchability** - Enable users to find documents quickly by customer, order, project, or type
3. **Consistency** - Use standardized values across all document types
4. **Traceability** - Support audit trails, order history, and project history
5. **Integration** - Link sales and project documents for end-to-end visibility

---

## Metadata Categories

| Category | Description | User Action |
|----------|-------------|-------------|
| **Core** | Essential for identification and search | Must enter at upload |
| **Tracking** | For workflow and status monitoring | Update as status changes |
| **Reference** | Additional context, nice to have | Optional entry |
| **Auto** | System-populated or inherited | No user action needed |

---

# PART A: SALES METADATA

## Global Sales Metadata (All Sales Documents)

These columns apply to ALL sales document libraries:

| Column Name | Type | Required | Category | Values/Format | Purpose |
|-------------|------|----------|----------|---------------|---------|
| Customer Name | Choice/Lookup | Yes | Core | [Customer list] | Link to customer master |
| Customer Code | Text | No | Core | CUST-NNNN | Customer identifier |
| Document Type | Choice | Yes | Core | [See document types below] | Categorize documents |
| Document Date | Date | Yes | Core | Date picker | Primary date on document |
| Document Status | Choice | Yes | Tracking | Draft, Pending, Approved, Final | Document lifecycle |
| Sales Person | Person | No | Core | User picker | Assigned sales rep |
| Region/Territory | Choice | No | Reference | [Region list] | Sales territory |
| Confidentiality | Choice | No | Reference | Internal, Confidential | Access control |
| Created By | Person | Auto | Auto | System | Audit trail |
| Modified Date | Date | Auto | Auto | System | Audit trail |

---

## Sales Stage Values

| Stage Code | Stage Name | Description |
|------------|------------|-------------|
| S1 | Lead/Inquiry | Initial customer inquiry |
| S2 | Qualification | Assessing opportunity |
| S3 | Quotation | Preparing/sent quotation |
| S4 | Negotiation | Price/terms negotiation |
| S5 | Order | Order received/confirmed |
| S6 | Fulfillment | Production/preparation |
| S7 | Delivery | Shipped/delivered |
| S8 | Closed | Completed/invoiced |

---

## Sales Document-Specific Metadata

### S1. Sales Quotations & Proposals

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Quotation Number | Text | Yes | Core | QT-YYYY-NNNN | QT-2024-0001 |
| Quotation Date | Date | Yes | Core | Date picker | 2024-01-15 |
| Quotation Type | Choice | Yes | Core | Standard, Custom, Repeat, Framework | Standard |
| Valid Until | Date | Yes | Core | Date picker | 2024-02-15 |
| Total Value | Currency | Yes | Core | Number | 125,000.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Product Line | Choice | No | Reference | [Product categories] | Industrial Equipment |
| Quotation Status | Choice | Yes | Tracking | Draft, Sent, Under Review, Won, Lost, Expired | Sent |
| Win/Loss Reason | Choice | No | Tracking | Price, Quality, Delivery, Competitor, Other | |
| Competitor | Text | No | Reference | Competitor name if lost | |

**Simplified to 10 fields**

---

### S2. Sales Orders & Contracts

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Sales Order Number | Text | Yes | Core | SO-YYYY-NNNN | SO-2024-0001 |
| Order Date | Date | Yes | Core | Date picker | 2024-01-20 |
| Customer PO Number | Text | Yes | Core | Customer's PO reference | CPO-12345 |
| Customer PO Date | Date | No | Core | Date picker | 2024-01-18 |
| Order Value | Currency | Yes | Core | Number | 125,000.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Delivery Date (Required) | Date | Yes | Core | Date picker | 2024-03-15 |
| Payment Terms | Choice | No | Reference | Net 30, Net 60, Net 90, COD, LC | Net 30 |
| Order Status | Choice | Yes | Tracking | Confirmed, In Production, Ready, Shipped, Delivered, Invoiced, Closed | Confirmed |
| Linked Quotation | Lookup | No | Reference | Link to quotation | QT-2024-0001 |
| Linked Project | Lookup | No | Reference | Link to project | PRJ-2024-001 |

**Simplified to 11 fields**

---

### S3. Customer Purchase Orders (Received)

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Customer PO Number | Text | Yes | Core | Customer's PO number | CPO-12345 |
| PO Date | Date | Yes | Core | Date picker | 2024-01-18 |
| PO Value | Currency | Yes | Core | Number | 125,000.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Delivery Date (Requested) | Date | Yes | Core | Date picker | 2024-03-15 |
| PO Status | Choice | Yes | Tracking | Received, Acknowledged, Processing, Completed | Received |
| Linked Sales Order | Text/Lookup | No | Reference | Our SO reference | SO-2024-0001 |

**Simplified to 7 fields**

---

### S4. Delivery Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Delivery Order Number | Text | Yes | Core | DO-YYYY-NNNN | DO-2024-0001 |
| Delivery Date | Date | Yes | Core | Date picker | 2024-03-15 |
| Sales Order Number | Text/Lookup | Yes | Core | Link to SO | SO-2024-0001 |
| Shipping Method | Choice | No | Reference | Ex-Works, FOB, CIF, DDP, Courier | FOB |
| Carrier | Text | No | Reference | Shipping company | DHL |
| Tracking Number | Text | No | Reference | Shipment tracking | 123456789 |
| Delivery Status | Choice | Yes | Tracking | Pending, Shipped, In Transit, Delivered, Returned | Shipped |
| Received By | Text | No | Tracking | Receiver name | |
| Received Date | Date | No | Tracking | Actual receipt date | |

**Simplified to 9 fields**

---

### S5. Customer Complaints & Returns

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Complaint Number | Text | Yes | Core | CMP-YYYY-NNNN | CMP-2024-0001 |
| Complaint Date | Date | Yes | Core | Date picker | 2024-03-20 |
| Complaint Type | Choice | Yes | Core | Quality, Delivery, Documentation, Pricing, Service | Quality |
| Sales Order Number | Text/Lookup | No | Core | Related SO | SO-2024-0001 |
| Severity | Choice | Yes | Core | Critical, Major, Minor | Major |
| Description | Note | Yes | Core | Complaint details | |
| Root Cause | Choice | No | Tracking | Manufacturing, Shipping, Documentation, Other | |
| Resolution | Note | No | Tracking | Resolution details | |
| Complaint Status | Choice | Yes | Tracking | Open, Investigating, Resolved, Closed | Open |
| RMA Number | Text | No | Reference | Return authorization | RMA-2024-0001 |

**Simplified to 10 fields**

---

### S6. Customer Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Document Category | Choice | Yes | Core | Specification, Drawing, Certificate, Agreement, Correspondence | Specification |
| Document Title | Text | Yes | Core | Document name | Product Requirements |
| Received Date | Date | Yes | Core | Date received | 2024-01-10 |
| Version | Text | No | Core | Version number | V1.0 |
| Valid Until | Date | No | Tracking | Expiry date if applicable | |
| Supersedes | Text | No | Reference | Previous version reference | |

**Simplified to 6 fields**

---

### S7. Sales Reports

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Report Type | Choice | Yes | Core | Pipeline, Forecast, Performance, Win/Loss, Territory | Pipeline |
| Report Period | Text | Yes | Core | Period covered | Q1 2024 |
| Report Frequency | Choice | Yes | Core | Weekly, Monthly, Quarterly, Annual | Monthly |
| Report Status | Choice | No | Tracking | Draft, Final | Final |

**Simplified to 4 fields**

---

### S8. Price Lists & Catalogs

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Price List Name | Text | Yes | Core | List identifier | Standard Price List 2024 |
| Effective Date | Date | Yes | Core | Date picker | 2024-01-01 |
| Expiry Date | Date | No | Core | Date picker | 2024-12-31 |
| Product Line | Choice | No | Reference | Product category | All Products |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Version | Text | Yes | Core | V1.0, V1.1 | V1.0 |
| Price List Status | Choice | Yes | Tracking | Draft, Active, Superseded | Active |

**Simplified to 7 fields**

---

# PART B: PROJECT METADATA

## Global Project Metadata (All Project Documents)

These columns apply to ALL project document libraries:

| Column Name | Type | Required | Category | Values/Format | Purpose |
|-------------|------|----------|----------|---------------|---------|
| Project Code | Text | Yes | Core | PRJ-YYYY-NNN | Unique project identifier |
| Project Name | Choice/Lookup | Yes | Core | [Project list] | Link to project master |
| Project Phase | Choice | Yes | Core | [See phases below] | Current project phase |
| Document Type | Choice | Yes | Core | [See document types below] | Categorize documents |
| Document Date | Date | Yes | Core | Date picker | Primary date on document |
| Document Status | Choice | Yes | Tracking | Draft, In Review, Approved, Final, Superseded | Document lifecycle |
| Linked Sales Order | Lookup | No | Reference | Link to originating SO | Sales order traceability |
| Confidentiality | Choice | No | Reference | Internal, Confidential, Highly Confidential | Access control |
| Created By | Person | Auto | Auto | System | Audit trail |
| Modified Date | Date | Auto | Auto | System | Audit trail |

---

## Project Phase Values

| Phase Code | Phase Name | Description |
|------------|------------|-------------|
| P1 | Initiation | Project concept and charter |
| P2 | Planning | Detailed planning and scheduling |
| P3 | Design | Technical/engineering design |
| P4 | Procurement | Vendor selection and purchasing |
| P5 | Execution | Implementation and construction |
| P6 | Testing | Validation and commissioning |
| P7 | Go-Live | Handover and deployment |
| P8 | Closure | Project close-out and review |

---

## Project Document-Specific Metadata

### P1. Project Charters & Proposals

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Charter Number | Text | Yes | Core | CHR-YYYY-NNN | CHR-2024-001 |
| Project Sponsor | Person | Yes | Core | User picker | |
| Project Manager | Person | Yes | Core | User picker | |
| Project Category | Choice | Yes | Core | Customer Project, NPD, Process Improvement, Equipment, Facility, IT, Quality, Cost Reduction | Customer Project |
| Estimated Budget | Currency | No | Reference | Number | 500,000.00 |
| Currency | Choice | No | Reference | MYR, USD, SGD, EUR | MYR |
| Target Start Date | Date | Yes | Core | Date picker | 2024-03-01 |
| Target End Date | Date | Yes | Core | Date picker | 2024-12-31 |
| Approval Status | Choice | Yes | Tracking | Pending, Approved, Rejected, On Hold | Approved |
| Linked Sales Order | Lookup | No | Reference | Originating SO | SO-2024-0001 |

**Simplified to 10 fields**

---

### P2. Project Plans & Schedules

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Plan Type | Choice | Yes | Core | Master Plan, Detailed Plan, Resource Plan, Communication Plan, Risk Plan | Master Plan |
| Plan Version | Text | Yes | Core | V1.0, V1.1, V2.0 | V1.0 |
| Baseline Date | Date | No | Tracking | Date picker | 2024-02-15 |
| Revision Number | Number | No | Tracking | Integer | 3 |
| Source System | Choice | No | Reference | Excel, Planner, Smartsheet, Other | Excel |

**Simplified to 5 fields**

---

### P3. Status Reports

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Report Type | Choice | Yes | Core | Weekly, Bi-Weekly, Monthly, Quarterly, Ad-hoc | Weekly |
| Report Period | Text | Yes | Core | Period covered | Week 5, Jan 2024 |
| Overall Status | Choice | Yes | Core | Green, Yellow, Red, Completed, On Hold | Green |
| Schedule Status | Choice | No | Tracking | On Track, At Risk, Delayed | On Track |
| Budget Status | Choice | No | Tracking | On Track, At Risk, Over Budget | On Track |
| % Complete | Number | No | Tracking | Percentage | 65 |
| Key Highlights | Note | No | Reference | Multi-line text | |
| Key Issues | Note | No | Reference | Multi-line text | |

**Simplified to 8 fields**

---

### P4. Meeting Minutes

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Meeting Type | Choice | Yes | Core | Kickoff, Status Review, Customer Meeting, Steering Committee, Technical Review, Gate Review | Status Review |
| Meeting Date | Date | Yes | Core | Date picker | 2024-01-15 |
| Meeting Location | Text | No | Reference | Location/Room | Conference Room A |
| Attendees | Person | No | Reference | Multi-user picker | |
| Action Items Count | Number | No | Tracking | Integer | 5 |

**Simplified to 5 fields**

---

### P5. Risk Registers & Risk Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Risk ID | Text | No | Core | RISK-NNN | RISK-001 |
| Risk Category | Choice | Yes | Core | Technical, Schedule, Cost, Resource, Quality, Customer, External, Safety | Technical |
| Risk Level | Choice | Yes | Core | High, Medium, Low | High |
| Total Risks | Number | No | Tracking | Integer | 12 |
| Open Risks | Number | No | Tracking | Integer | 5 |
| Review Date | Date | No | Tracking | Date picker | 2024-01-31 |

**Simplified to 6 fields**

---

### P6. Issue Logs & Issue Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Issue ID | Text | No | Core | ISS-NNN | ISS-001 |
| Issue Category | Choice | Yes | Core | Technical, Resource, Vendor, Customer, Quality, Schedule, Scope | Technical |
| Issue Priority | Choice | Yes | Core | Critical, High, Medium, Low | High |
| Total Issues | Number | No | Tracking | Integer | 8 |
| Open Issues | Number | No | Tracking | Integer | 3 |
| Review Date | Date | No | Tracking | Date picker | 2024-01-31 |

**Simplified to 6 fields**

---

### P7. Change Requests

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Change Request Number | Text | Yes | Core | CR-YYYY-NNN | CR-2024-001 |
| Change Type | Choice | Yes | Core | Scope, Schedule, Budget, Technical, Resource, Customer Request | Scope |
| Change Priority | Choice | Yes | Core | Critical, High, Medium, Low | High |
| Impact Area | Choice | Yes | Core | Cost, Schedule, Quality, Scope, Resource | Cost |
| Estimated Impact | Currency | No | Reference | Number | 25,000.00 |
| Requested By | Person | Yes | Core | User picker | |
| Request Date | Date | Yes | Core | Date picker | 2024-01-20 |
| Approval Status | Choice | Yes | Tracking | Pending, Approved, Rejected, Deferred | Pending |
| Customer Approval Required | Yes/No | No | Tracking | Yes/No | Yes |
| Customer Approved | Yes/No | No | Tracking | Yes/No | |

**Simplified to 10 fields**

---

### P8. Technical Specifications & Requirements

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Specification Number | Text | Yes | Core | SPEC-YYYY-NNN | SPEC-2024-001 |
| Specification Type | Choice | Yes | Core | Functional, Technical, Equipment, Process, Interface, Customer | Technical |
| Version | Text | Yes | Core | V1.0, V1.1 | V1.0 |
| Review Status | Choice | Yes | Tracking | Draft, Under Review, Approved, Released | Released |
| Customer Approved | Yes/No | No | Tracking | Yes/No | Yes |
| Review Date | Date | No | Tracking | Date picker | |

**Simplified to 6 fields**

---

### P9. Test Plans & Test Reports

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Test Document Number | Text | Yes | Core | TST-YYYY-NNN | TST-2024-001 |
| Test Type | Choice | Yes | Core | Unit Test, Integration Test, System Test, UAT, FAT, SAT, Validation | UAT |
| Test Phase | Choice | Yes | Core | Planning, Execution, Completed | Completed |
| Test Result | Choice | No | Tracking | Pass, Fail, Partial, Pending | Pass |
| Test Date | Date | No | Core | Date picker | 2024-02-15 |
| Tester | Person | No | Reference | User picker | |
| Customer Witnessed | Yes/No | No | Tracking | Yes/No | Yes |

**Simplified to 7 fields**

---

### P10. Vendor & Procurement Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Vendor Name | Choice/Text | Yes | Core | [Vendor list] | ABC Equipment Sdn Bhd |
| Document Category | Choice | Yes | Core | Quotation, Contract, PO, Evaluation, Performance Review | Quotation |
| Quotation/Contract Number | Text | No | Core | Reference number | QT-2024-001 |
| Value | Currency | No | Reference | Number | 150,000.00 |
| Currency | Choice | No | Reference | MYR, USD, SGD, EUR | MYR |
| Valid Until | Date | No | Tracking | Date picker | 2024-03-31 |

**Simplified to 6 fields**

---

### P11. Project Closure Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Closure Document Type | Choice | Yes | Core | Closure Report, Lessons Learned, Handover, Post-Implementation Review | Closure Report |
| Actual End Date | Date | Yes | Core | Date picker | 2024-12-15 |
| Final Budget | Currency | No | Reference | Number | 485,000.00 |
| Budget Variance | Currency | No | Reference | Number | -15,000.00 |
| Schedule Variance | Number | No | Reference | Days (+ or -) | +5 |
| Overall Assessment | Choice | No | Tracking | Successful, Partially Successful, Challenged, Failed | Successful |
| Sign-off Status | Choice | Yes | Tracking | Pending, Signed Off | Signed Off |
| Customer Sign-off | Yes/No | No | Tracking | Yes/No | Yes |

**Simplified to 8 fields**

---

### P12. Training & Documentation

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Document Category | Choice | Yes | Core | Training Material, User Manual, SOP, Process Document, Work Instruction | Training Material |
| Target Audience | Choice | No | Reference | Operators, Engineers, Management, Customer, All Staff | Operators |
| Version | Text | Yes | Core | V1.0, V1.1 | V1.0 |
| Effective Date | Date | No | Tracking | Date picker | 2024-03-01 |
| Review Cycle | Choice | No | Reference | Annual, Bi-Annual, As Needed | Annual |

**Simplified to 5 fields**

---

# PART C: MASTER LISTS

## Customer Master List Fields

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
| Customer Status | Choice | Yes | Active, Inactive, Prospect, Blacklisted |

---

## Project Master List Fields

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Project Code | Text | Yes | Unique identifier (PRJ-YYYY-NNN) |
| Project Name | Text | Yes | Full project name |
| Project Category | Choice | Yes | Customer Project, NPD, Process Improvement, etc. |
| Customer | Lookup | No | Link to Customer Master (for customer projects) |
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

---

## Summary: Field Count

### Sales Documents
| Document Type | Field Count |
|---------------|-------------|
| Quotations & Proposals | 10 |
| Sales Orders & Contracts | 11 |
| Customer Purchase Orders | 7 |
| Delivery Documents | 9 |
| Customer Complaints | 10 |
| Customer Documents | 6 |
| Sales Reports | 4 |
| Price Lists | 7 |
| **Sales Subtotal** | **64** |

### Project Documents
| Document Type | Field Count |
|---------------|-------------|
| Project Charters | 10 |
| Project Plans | 5 |
| Status Reports | 8 |
| Meeting Minutes | 5 |
| Risk Documents | 6 |
| Issue Documents | 6 |
| Change Requests | 10 |
| Technical Specs | 6 |
| Test Documents | 7 |
| Vendor Documents | 6 |
| Closure Documents | 8 |
| Training Docs | 5 |
| **Project Subtotal** | **82** |

### **Grand Total: 146 fields**

---

## Managed Metadata (Term Store)

Consider Term Store for frequently used lists:

```
Sales & Project Management
├── Customers (managed list)
├── Sales Stages (8 stages)
├── Project Categories (8 types)
├── Project Phases (8 phases)
├── Document Types (20+ types)
├── Vendors (managed list)
├── Product Lines (managed list)
├── Regions/Territories (managed list)
└── Risk Categories (8 types)
```

---

## Key Linkages

| From | To | Link Field | Purpose |
|------|-----|------------|---------|
| Sales Order | Customer | Customer Name | Customer lookup |
| Sales Order | Quotation | Linked Quotation | Quote-to-order tracking |
| Project | Sales Order | Linked Sales Order | Sales-to-project traceability |
| Project | Customer | Customer | Customer project tracking |
| Delivery | Sales Order | Sales Order Number | Fulfillment tracking |
| Complaint | Sales Order | Sales Order Number | Issue tracking |
| Change Request | Project | Project Code | Project change management |

---

## Notes

- Fields can be added back for specific document types if detailed tracking is required
- Consider using Power Automate to auto-populate fields from linked records
- Project Code format: PRJ-YYYY-NNN (e.g., PRJ-2024-001)
- Sales Order format: SO-YYYY-NNNN (e.g., SO-2024-0001)
- Customer Code format: CUST-NNNN (e.g., CUST-0001)
- Quotation format: QT-YYYY-NNNN (e.g., QT-2024-0001)
