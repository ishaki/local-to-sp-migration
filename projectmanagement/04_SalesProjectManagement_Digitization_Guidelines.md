# Sales & Project Management Department - Digitization Guidelines
## Hardcopy to Digital Conversion Standards

---

## Purpose
This document provides standards and best practices for converting hardcopy (paper) sales and project management documents to digital format for storage in SharePoint Online. Following these guidelines ensures consistency, searchability, and compliance with audit requirements in a manufacturing environment.

---

## Table of Contents
1. [File Naming Conventions](#1-file-naming-conventions)
2. [Scanning Standards](#2-scanning-standards)
3. [Document-Specific Guidelines](#3-document-specific-guidelines)
4. [Metadata Requirements](#4-metadata-requirements)
5. [Quality Control Checklist](#5-quality-control-checklist)
6. [Original Document Handling](#6-original-document-handling)
7. [Workflow Process](#7-workflow-process)

---

## 1. File Naming Conventions

### General Rules

| Rule | Description | Example |
|------|-------------|---------|
| No special characters | Avoid: `\ / : * ? " < > \| # %` | QT-2024-0001 (not QT#2024/0001) |
| No leading/trailing spaces | Trim spaces | |
| Use hyphens or underscores | For separation | SO-2024-0001_Customer-PO.pdf |
| Keep names concise | Max 50-80 characters recommended | |
| Include key identifier | Customer, order, or project reference | |
| Use consistent date format | YYYY-MM-DD or YYYYMMDD | 2024-01-15 |
| Lowercase extensions | .pdf not .PDF | Quotation.pdf |

---

# PART A: SALES DOCUMENT NAMING

### Sales Quotations & Proposals
```
Format: QT_[QuotationNumber]_[CustomerCode]_[Date].pdf
        PROP_[CustomerCode]_[Description]_[Date].pdf

Examples:
QT_QT-2024-0001_CUST001_2024-01-15.pdf
QT_QT-2024-0001_ACME-CORP_2024-01-15.pdf
PROP_CUST001_ASSEMBLY-LINE-UPGRADE_2024-01-15.pdf
```

### Sales Orders
```
Format: SO_[SalesOrderNumber]_[CustomerCode]_[Date].pdf

Examples:
SO_SO-2024-0001_CUST001_2024-01-20.pdf
SO_SO-2024-0001_ACME-CORP_2024-01-20.pdf
```

### Customer Purchase Orders (Received)
```
Format: CPO_[CustomerPONumber]_[CustomerCode]_[Date].pdf

Examples:
CPO_PO12345_CUST001_2024-01-18.pdf
CPO_ACME-PO-2024-001_ACME-CORP_2024-01-18.pdf
```

### Order Acknowledgments
```
Format: OA_[SalesOrderNumber]_[CustomerCode]_[Date].pdf

Examples:
OA_SO-2024-0001_CUST001_2024-01-22.pdf
```

### Delivery Documents
```
Format: DO_[DeliveryOrderNumber]_[CustomerCode]_[Date].pdf
        PL_[DeliveryOrderNumber]_[CustomerCode]_[Date].pdf (Packing List)
        POD_[DeliveryOrderNumber]_[CustomerCode]_[Date].pdf (Proof of Delivery)

Examples:
DO_DO-2024-0001_CUST001_2024-03-15.pdf
PL_DO-2024-0001_CUST001_2024-03-15.pdf
POD_DO-2024-0001_CUST001_2024-03-18.pdf
```

### Customer Complaints & Returns
```
Format: CMP_[ComplaintNumber]_[CustomerCode]_[Date].pdf
        RMA_[RMANumber]_[CustomerCode]_[Date].pdf

Examples:
CMP_CMP-2024-0001_CUST001_2024-03-20.pdf
RMA_RMA-2024-0001_CUST001_2024-03-22.pdf
```

### Customer Documents (Received)
```
Format: CUSTDOC_[CustomerCode]_[DocType]_[Description]_[Date].pdf

Examples:
CUSTDOC_CUST001_SPEC_PRODUCT-REQUIREMENTS_2024-01-10.pdf
CUSTDOC_CUST001_DWG_ASSEMBLY-DRAWING_2024-01-10.pdf
CUSTDOC_CUST001_NDA_CONFIDENTIALITY-AGREEMENT_2024-01-05.pdf
```

### Customer Visit Reports
```
Format: VISIT_[CustomerCode]_[Date]_[Description].pdf

Examples:
VISIT_CUST001_2024-01-15_QUARTERLY-REVIEW.pdf
VISIT_ACME-CORP_2024-02-10_SITE-SURVEY.pdf
```

### Price Lists & Catalogs
```
Format: PRICELIST_[Name]_[Currency]_[EffectiveDate].pdf
        CATALOG_[ProductLine]_[Version]_[Year].pdf

Examples:
PRICELIST_STANDARD-2024_MYR_2024-01-01.pdf
PRICELIST_OEM-DISCOUNT_USD_2024-01-01.pdf
CATALOG_INDUSTRIAL-EQUIPMENT_V2_2024.pdf
```

### Sales Reports
```
Format: SALES-RPT_[ReportType]_[Period].pdf

Examples:
SALES-RPT_PIPELINE_2024-01.pdf
SALES-RPT_FORECAST_2024-Q1.pdf
SALES-RPT_PERFORMANCE_2024-ANNUAL.pdf
```

---

# PART B: PROJECT DOCUMENT NAMING

### Project Charters & Proposals
```
Format: [ProjectCode]_CHARTER_[Version].pdf
        [ProjectCode]_PROPOSAL_[Date].pdf
        [ProjectCode]_BUSINESSCASE_[Version].pdf

Examples:
PRJ-2024-001_CHARTER_V1.0.pdf
PRJ-2024-001_PROPOSAL_2024-01-15.pdf
PRJ-2024-001_BUSINESSCASE_V1.0.pdf
```

### Project Plans & Schedules
```
Format: [ProjectCode]_PLAN_[PlanType]_[Version].pdf
        [ProjectCode]_SCHEDULE_[Version].xlsx

Examples:
PRJ-2024-001_PLAN_MASTER_V1.0.pdf
PRJ-2024-001_PLAN_RESOURCE_V1.0.pdf
PRJ-2024-001_SCHEDULE_V2.1.xlsx
PRJ-2024-001_PLAN_COMMUNICATION_V1.0.pdf
```

### Status Reports
```
Format: [ProjectCode]_STATUS_[Period]_[Date].pdf
        [ProjectCode]_STATUS_CUSTOMER_[Date].pdf (for customer-facing reports)

Examples:
PRJ-2024-001_STATUS_WEEKLY_2024-01-15.pdf
PRJ-2024-001_STATUS_MONTHLY_2024-01.pdf
PRJ-2024-001_STATUS_CUSTOMER_2024-01-20.pdf
```

### Meeting Minutes
```
Format: [ProjectCode]_MOM_[MeetingType]_[Date].pdf

Examples:
PRJ-2024-001_MOM_KICKOFF_2024-01-10.pdf
PRJ-2024-001_MOM_CUSTOMER_2024-01-20.pdf
PRJ-2024-001_MOM_REVIEW_2024-02-05.pdf
PRJ-2024-001_MOM_GATE-3_2024-03-15.pdf
```

### Risk & Issue Documents
```
Format: [ProjectCode]_RISK-REGISTER_[Date].pdf
        [ProjectCode]_ISSUE-LOG_[Date].pdf

Examples:
PRJ-2024-001_RISK-REGISTER_2024-01-31.pdf
PRJ-2024-001_ISSUE-LOG_2024-01-31.pdf
```

### Change Requests
```
Format: [ProjectCode]_CR_[CRNumber]_[Description].pdf

Examples:
PRJ-2024-001_CR_CR-001_SCOPE-CHANGE.pdf
PRJ-2024-001_CR_CR-002_CUSTOMER-REQUEST.pdf
```

### Technical Specifications
```
Format: [ProjectCode]_SPEC_[SpecType]_[Number]_[Version].pdf

Examples:
PRJ-2024-001_SPEC_FUNCTIONAL_FS-001_V1.0.pdf
PRJ-2024-001_SPEC_TECHNICAL_TS-001_V2.0.pdf
PRJ-2024-001_SPEC_CUSTOMER_CS-001_V1.0.pdf
```

### Test Documents
```
Format: [ProjectCode]_TEST_[TestType]_[Number/Date].pdf

Examples:
PRJ-2024-001_TEST_PLAN_TP-001_V1.0.pdf
PRJ-2024-001_TEST_FAT_REPORT_2024-03-15.pdf
PRJ-2024-001_TEST_SAT_REPORT_2024-04-01.pdf
PRJ-2024-001_TEST_CUSTOMER-WITNESS_2024-04-01.pdf
```

### Vendor Documents
```
Format: [ProjectCode]_VENDOR_[VendorCode]_[DocType]_[Date].pdf

Examples:
PRJ-2024-001_VENDOR_ABC-EQUIP_QUOTATION_2024-01-10.pdf
PRJ-2024-001_VENDOR_ABC-EQUIP_CONTRACT_2024-02-01.pdf
PRJ-2024-001_VENDOR_ABC-EQUIP_PO_PO2024-001.pdf
```

### Project Closure Documents
```
Format: [ProjectCode]_CLOSURE_[DocType]_[Date].pdf

Examples:
PRJ-2024-001_CLOSURE_REPORT_2024-12-15.pdf
PRJ-2024-001_CLOSURE_LESSONS-LEARNED_2024-12-15.pdf
PRJ-2024-001_CLOSURE_CUSTOMER-SIGNOFF_2024-12-10.pdf
PRJ-2024-001_CLOSURE_HANDOVER_2024-12-10.pdf
```

### Training Documents
```
Format: [ProjectCode]_TRAINING_[Topic]_[Version].pdf
        [ProjectCode]_SOP_[Number]_[Title]_[Version].pdf
        [ProjectCode]_MANUAL_[Title]_[Version].pdf

Examples:
PRJ-2024-001_TRAINING_OPERATOR_V1.0.pdf
PRJ-2024-001_TRAINING_CUSTOMER_V1.0.pdf
PRJ-2024-001_SOP_001_MACHINE-OPERATION_V1.0.pdf
PRJ-2024-001_MANUAL_USER_V1.0.pdf
```

---

## Attachments & Supporting Documents
```
Format: [ParentDocumentName]_ATT[Number]_[Description].pdf

Examples:
QT_QT-2024-0001_CUST001_ATT1_TECHNICAL-SPECS.pdf
QT_QT-2024-0001_CUST001_ATT2_DRAWINGS.pdf
SO_SO-2024-0001_CUST001_ATT1_CUSTOMER-PO.pdf
PRJ-2024-001_CR_CR-001_ATT1_IMPACT-ANALYSIS.pdf
```

---

## 2. Scanning Standards

### Resolution Guidelines

| Document Type | Minimum Resolution | Recommended | Notes |
|---------------|-------------------|-------------|-------|
| Standard documents (letters, reports) | 200 DPI | 300 DPI | Grayscale |
| Customer POs / Orders | 300 DPI | 300 DPI | Grayscale |
| Contracts with signatures | 300 DPI | 300 DPI | Grayscale or color |
| Technical drawings | 300 DPI | 400 DPI | Grayscale or color |
| Delivery PODs with signatures | 300 DPI | 300 DPI | Grayscale |
| Photos (products, site) | 300 DPI | 300 DPI | Color |

### Color Mode

| Document Type | Recommended Mode |
|---------------|------------------|
| Text-only documents | Black & White (1-bit) or Grayscale |
| Documents with stamps/signatures | Grayscale (8-bit) |
| Customer documents (preserve original) | As received |
| Technical drawings with color coding | Color (24-bit) |
| Marketing materials | Color (24-bit) |

### File Format

| Format | Use Case |
|--------|----------|
| **PDF/A** (Recommended) | All archival documents |
| **PDF** | General documents |
| **TIFF** | Technical drawings (high quality) |
| **JPEG** | Photos only |

### File Size Guidelines

| Size Range | Action |
|------------|--------|
| < 10 MB | Optimal for SharePoint |
| 10-50 MB | Acceptable, consider compression |
| 50-100 MB | Compress or split if possible |
| > 100 MB | Split into multiple files |

### OCR Requirements

**Enable OCR for all scanned documents** to make text searchable.

| Setting | Recommendation |
|---------|----------------|
| OCR Language | English, Malay (as appropriate) |
| OCR Mode | Searchable Image |
| Text Layer | Embedded in PDF |

---

## 3. Document-Specific Guidelines

### Sales Quotations

**What to Capture:**
- Complete quotation (all pages)
- Technical specifications/attachments
- Terms and conditions
- Any handwritten notes/modifications

**Scanning Tips:**
- Ensure quotation number is clearly visible
- Include all pages including T&Cs
- Scan attachments separately with clear naming

---

### Customer Purchase Orders

**What to Capture:**
- Complete PO (all pages)
- All terms and conditions
- Delivery instructions
- Any amendments

**Scanning Tips:**
- **Critical document** - ensure high quality
- Capture PO number clearly
- Include all pages even if partially blank
- Scan both sides if double-sided

---

### Contracts & Agreements

**What to Capture:**
- Complete contract (all pages including schedules)
- Signature pages
- Any amendments/addendums
- Supporting documents

**Scanning Tips:**
- Use color scanning for signed pages
- Ensure signatures and stamps are clear
- Include all schedules and attachments
- Scan as single PDF if possible

**Example Package:**
```
SO_SO-2024-0001_CUST001_2024-01-20.pdf           (Main order)
SO_SO-2024-0001_CUST001_ATT1_CUSTOMER-PO.pdf     (Customer PO)
SO_SO-2024-0001_CUST001_ATT2_TERMS.pdf           (Terms if separate)
```

---

### Delivery Documents & PODs

**What to Capture:**
- Delivery order
- Packing list
- Bill of lading / shipping documents
- **Signed proof of delivery** (critical)

**Scanning Tips:**
- POD signatures must be clearly visible
- Include date and receiver name
- Scan immediately after receiving signed copy
- Keep original PODs in secure storage

---

### Customer Complaints

**What to Capture:**
- Complaint form/notification
- Supporting evidence (photos, test results)
- Investigation report
- Corrective action documentation
- Customer correspondence

**Scanning Tips:**
- Include all evidence photos
- Capture date stamps clearly
- Document chain of custody

---

### Project Technical Documents

**What to Capture:**
- Complete specification (all pages)
- All appendices and annexes
- Revision history
- Customer approval signatures (if applicable)

**Scanning Tips:**
- Ensure revision/version number is visible
- Capture customer approval stamps
- Technical drawings may need larger format scanning

---

### Test Reports / FAT / SAT

**What to Capture:**
- Test plan
- Test results/data
- Pass/fail status clearly visible
- **Customer witness signatures** (critical for FAT/SAT)
- Defect/punch lists

**Scanning Tips:**
- Customer signatures must be clear
- Include all test data sheets
- Photos of test setup if relevant

---

## 4. Metadata Requirements

After scanning, the following metadata MUST be entered in SharePoint:

### Sales Documents - Required Metadata

| Document Type | Key Metadata to Enter |
|---------------|----------------------|
| Quotation | Quotation Number, Customer, Date, Value, Status |
| Sales Order | SO Number, Customer, Customer PO, Date, Value, Status |
| Customer PO | Customer PO Number, Customer, Date, Value |
| Delivery | DO Number, Customer, SO Number, Date, Status |
| Complaint | Complaint Number, Customer, Date, Type, Severity, Status |
| Customer Document | Customer, Document Category, Date, Description |

### Project Documents - Required Metadata

| Document Type | Key Metadata to Enter |
|---------------|----------------------|
| Project Charter | Project Code, Project Name, Category, Dates, Status |
| Project Plan | Project Code, Plan Type, Version |
| Status Report | Project Code, Report Type, Period, Overall Status |
| Meeting Minutes | Project Code, Meeting Type, Date |
| Change Request | Project Code, CR Number, Type, Priority, Status |
| Technical Spec | Project Code, Spec Number, Type, Version, Status |
| Test Document | Project Code, Test Type, Date, Result |
| Closure Document | Project Code, Document Type, Date, Assessment |

---

## 5. Quality Control Checklist

### Pre-Scan Checklist
- [ ] Document is complete (all pages present)
- [ ] Document is flat and unwrinkled
- [ ] Staples/clips removed (if needed)
- [ ] Document orientation correct
- [ ] Key identifiers visible (PO number, order number, etc.)

### Post-Scan Checklist
- [ ] All pages scanned (count matches original)
- [ ] Image is clear and readable
- [ ] No cut-off text or images
- [ ] Correct orientation
- [ ] OCR completed (text is searchable)
- [ ] File size is reasonable
- [ ] File name follows naming convention
- [ ] Signatures/stamps are clearly visible

### Upload Checklist
- [ ] File uploaded to correct library
- [ ] All required metadata entered
- [ ] Customer/Project correctly linked
- [ ] Document status set correctly
- [ ] Attachments linked properly

---

## 6. Original Document Handling

### Retention of Originals

| Document Type | Keep Original? | Retention Period | Notes |
|---------------|----------------|------------------|-------|
| Signed contracts | Yes | Contract + 7 years | Legal requirement |
| Customer POs | Yes | 7 years | Audit requirement |
| Signed quotations | Yes | 7 years | Commercial records |
| Delivery PODs | Yes | 7 years | Proof of delivery |
| Complaint evidence | Yes | 10 years | Quality/legal |
| Test witness reports | Yes | Product lifecycle | Regulatory |
| Customer specifications | Yes | Product lifecycle | Technical reference |
| General correspondence | No | After scanning | Can dispose |
| Internal memos | No | After scanning | Can dispose |
| Draft documents | No | After scanning | Can dispose |

### Storage of Physical Originals

For documents requiring physical retention:

1. **Label the storage box:**
   ```
   SALES & PM - [Category]
   Customer/Project: [Reference]
   Documents: [Types]
   Date Range: [Start - End]
   Box #: [Number]
   Retention Until: [Date]
   ```

2. **Create a box inventory list**

3. **Store in secure, climate-controlled location**

4. **Log location in tracking system**

---

## 7. Workflow Process

### Digitization Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  1. Receive │────▶│  2. Prepare │────▶│  3. Scan    │
│  Document   │     │  Document   │     │             │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  6. Store   │◀────│  5. Upload  │◀────│  4. Quality │
│  Original   │     │  & Metadata │     │  Check      │
└─────────────┘     └─────────────┘     └─────────────┘
```

### Step-by-Step Process

#### Step 1: Receive Document
- Log receipt in tracking sheet
- Identify document type (Sales or Project)
- Identify customer/project code
- Prioritize based on urgency

#### Step 2: Prepare Document
- Remove staples/clips if using sheet feeder
- Flatten creases
- Arrange pages in order
- Check completeness
- Verify key identifiers are visible

#### Step 3: Scan Document
- Select appropriate scan settings
- Preview first page
- Scan all pages
- Save with correct file name
- Enable OCR

#### Step 4: Quality Check
- Review scanned image
- Verify all pages captured
- Check readability
- Verify signatures are visible
- Confirm OCR completed
- Verify file name follows convention

#### Step 5: Upload & Enter Metadata
- Upload to correct SharePoint library
- Select correct Customer/Project
- Enter all required metadata
- Link supporting documents
- Verify upload successful

#### Step 6: Store/Dispose Original
- If retention required: file in labeled storage
- If no retention: secure disposal
- Update tracking log

---

## Appendix A: File Naming Quick Reference Card

```
╔══════════════════════════════════════════════════════════════════╗
║       SALES & PROJECT MANAGEMENT NAMING QUICK REFERENCE          ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  SALES DOCUMENTS                                                 ║
║  ───────────────────────────────────────────────────────────     ║
║  Quotation:     QT_[Number]_[Customer]_[Date].pdf               ║
║  Sales Order:   SO_[Number]_[Customer]_[Date].pdf               ║
║  Customer PO:   CPO_[PONumber]_[Customer]_[Date].pdf            ║
║  Delivery:      DO_[Number]_[Customer]_[Date].pdf               ║
║  POD:           POD_[DONumber]_[Customer]_[Date].pdf            ║
║  Complaint:     CMP_[Number]_[Customer]_[Date].pdf              ║
║  Customer Doc:  CUSTDOC_[Customer]_[Type]_[Desc]_[Date].pdf     ║
║  Visit Report:  VISIT_[Customer]_[Date]_[Description].pdf       ║
║                                                                  ║
║  PROJECT DOCUMENTS                                               ║
║  ───────────────────────────────────────────────────────────     ║
║  Charter:       [PRJ]_CHARTER_[Version].pdf                     ║
║  Plan:          [PRJ]_PLAN_[Type]_[Version].pdf                 ║
║  Status:        [PRJ]_STATUS_[Period]_[Date].pdf                ║
║  Minutes:       [PRJ]_MOM_[MeetingType]_[Date].pdf              ║
║  Change Req:    [PRJ]_CR_[Number]_[Description].pdf             ║
║  Spec:          [PRJ]_SPEC_[Type]_[Number]_[Version].pdf        ║
║  Test:          [PRJ]_TEST_[Type]_[Number/Date].pdf             ║
║  Closure:       [PRJ]_CLOSURE_[DocType]_[Date].pdf              ║
║                                                                  ║
║  ───────────────────────────────────────────────────────────     ║
║  RULES:                                                          ║
║  • Date format: YYYY-MM-DD                                       ║
║  • No special characters: \ / : * ? " < > | # %                  ║
║  • Use hyphens (-) or underscores (_)                            ║
║  • Attachments: Add _ATT[N]_[Description]                        ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Appendix B: Scanner Settings Quick Reference

```
╔══════════════════════════════════════════════════════════════════╗
║                    SCANNER SETTINGS REFERENCE                    ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  STANDARD DOCUMENTS (Reports, Letters, Memos)                    ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Grayscale                                              ║
║  • Format: PDF/A                                                 ║
║  • OCR: Enabled                                                  ║
║                                                                  ║
║  CUSTOMER POs / CONTRACTS / SIGNED DOCUMENTS                     ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Grayscale or Color (for stamps)                        ║
║  • Format: PDF/A                                                 ║
║  • OCR: Enabled                                                  ║
║  • Note: Signatures must be clearly visible!                     ║
║                                                                  ║
║  PROOF OF DELIVERY (POD)                                         ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Grayscale                                              ║
║  • Format: PDF/A                                                 ║
║  • OCR: Enabled                                                  ║
║  • Note: CRITICAL - Receiver signature must be clear!            ║
║                                                                  ║
║  TECHNICAL DRAWINGS                                              ║
║  • Resolution: 400 DPI                                           ║
║  • Color: As per original                                        ║
║  • Format: PDF/A or TIFF                                         ║
║                                                                  ║
║  PHOTOS (Products, Site, Evidence)                               ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Full Color                                             ║
║  • Format: JPEG or PDF                                           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Appendix C: Code Formats

### Customer Code
```
CUST-NNNN (e.g., CUST-0001)
or
Short customer name (e.g., ACME-CORP)
```

### Project Code
```
PRJ-YYYY-NNN (e.g., PRJ-2024-001)
```

### Document Numbers
```
Quotation:      QT-YYYY-NNNN    (e.g., QT-2024-0001)
Sales Order:    SO-YYYY-NNNN    (e.g., SO-2024-0001)
Delivery Order: DO-YYYY-NNNN    (e.g., DO-2024-0001)
Complaint:      CMP-YYYY-NNNN   (e.g., CMP-2024-0001)
Change Request: CR-YYYY-NNN     (e.g., CR-2024-001)
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-02-06 | Migration Team | Initial version - Sales & Project Management combined |
