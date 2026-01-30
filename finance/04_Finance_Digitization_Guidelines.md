# Finance Department - Digitization Guidelines
## Hardcopy to Digital Conversion Standards

---

## Purpose
This document provides standards and best practices for converting hardcopy (paper) finance documents to digital format for storage in SharePoint Online. Following these guidelines ensures consistency, searchability, and compliance with audit requirements.

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
| No special characters | Avoid: `\ / : * ? " < > \| # %` | ✗ Invoice#123 → ✓ Invoice-123 |
| No leading/trailing spaces | Trim spaces | ✗ " Invoice.pdf" |
| Use hyphens or underscores | For separation | Invoice-2024-001234.pdf |
| Keep names concise | Max 50-80 characters recommended | |
| Include key identifiers | Document number, date, vendor/customer | |
| Use consistent date format | YYYY-MM-DD or YYYYMMDD | 2024-01-15 or 20240115 |
| Lowercase extensions | .pdf not .PDF | Invoice.pdf |

### Naming Convention by Document Type

#### Invoices - Accounts Payable (Vendor Invoices)
```
Format: INV-AP_[VendorCode]_[InvoiceNumber]_[InvoiceDate].pdf

Examples:
INV-AP_V00123_INV2024001234_2024-01-15.pdf
INV-AP_ABCSUPPLY_A12345_2024-01-15.pdf
```

#### Invoices - Accounts Receivable (Customer Invoices)
```
Format: INV-AR_[CustomerCode]_[InvoiceNumber]_[InvoiceDate].pdf

Examples:
INV-AR_C00456_SI2024001234_2024-01-15.pdf
INV-AR_XYZCORP_SI-2024-0001_2024-01-15.pdf
```

#### Purchase Orders
```
Format: PO_[PONumber]_[VendorCode]_[PODate].pdf

Examples:
PO_PO2024000456_V00123_2024-01-10.pdf
PO_2024-0456_ABCSUPPLY_2024-01-10.pdf
```

#### Payment Vouchers
```
Format: PV_[VoucherNumber]_[PayeeName]_[VoucherDate].pdf

Examples:
PV_PV2024001234_ABCSUPPLY_2024-02-10.pdf
PV_2024-1234_EMPLOYEE-JOHN_2024-02-10.pdf
```

#### Bank Statements
```
Format: BANK_[BankName]_[AccountLast4]_[StatementPeriod].pdf

Examples:
BANK_MAYBANK_1234_2024-01.pdf
BANK_CIMB_5678_2024-Q1.pdf
```

#### Bank Reconciliations
```
Format: RECON_[BankName]_[AccountLast4]_[Period].pdf

Examples:
RECON_MAYBANK_1234_2024-01.pdf
```

#### Financial Reports
```
Format: RPT_[ReportType]_[Period]_[Version].pdf

Examples:
RPT_PL_2024-01_FINAL.pdf
RPT_BS_2024-Q1_DRAFT-V2.pdf
RPT_CASHFLOW_2024-ANNUAL_FINAL.pdf
```

#### Tax Documents
```
Format: TAX_[TaxType]_[TaxPeriod]_[DocumentType].pdf

Examples:
TAX_GST_2024-Q1_RETURN.pdf
TAX_CORPINCOMETAX_2023_ASSESSMENT.pdf
TAX_WHT_2024-01_PAYMENT.pdf
```

#### Audit Files
```
Format: AUDIT_[AuditType]_[AuditYear]_[DocumentType]_[Sequence].pdf

Examples:
AUDIT_EXTERNAL_2023_REPORT_FINAL.pdf
AUDIT_EXTERNAL_2023_WP_001.pdf
AUDIT_INTERNAL_2024-Q1_FINDINGS.pdf
```

#### Contracts
```
Format: CONTRACT_[ContractType]_[Counterparty]_[StartDate].pdf

Examples:
CONTRACT_LEASE_ABCPROPERTIES_2024-01-01.pdf
CONTRACT_SERVICE_ITVENDOR_2024-03-15.pdf
CONTRACT_NDA_XYZCORP_2024-02-01.pdf
```

#### Expense Claims
```
Format: EXP_[EmployeeID]_[ClaimNumber]_[ClaimDate].pdf

Examples:
EXP_EMP001_EXP2024001234_2024-01-20.pdf
EXP_JOHN-DOE_2024-0045_2024-01-20.pdf
```

#### Journal Entries
```
Format: JV_[JournalNumber]_[JournalDate].pdf

Examples:
JV_JV2024001234_2024-01-31.pdf
JV_2024-ADJ-001_2024-01-31.pdf
```

#### Policies & Procedures
```
Format: POL_[PolicyNumber]_[PolicyTitle]_V[Version].pdf

Examples:
POL_FIN-001_TRAVEL-EXPENSE-POLICY_V3.0.pdf
POL_FIN-002_PROCUREMENT-POLICY_V1.0.pdf
```

#### Fixed Assets
```
Format: FA_[AssetNumber]_[DocumentType].pdf

Examples:
FA_FA2024001_INVOICE.pdf
FA_FA2024001_PHOTO.jpg
FA_FA2024001_DISPOSAL-FORM.pdf
```

### Multi-Page Documents
For documents scanned in multiple parts:
```
Format: [StandardName]_PART[Number].pdf

Examples:
CONTRACT_LEASE_ABCPROP_2024-01-01_PART1.pdf
CONTRACT_LEASE_ABCPROP_2024-01-01_PART2.pdf

Better: Combine into single PDF when possible
```

### Supporting Documents / Attachments
```
Format: [ParentDocumentName]_ATT[Number]_[Description].pdf

Examples:
INV-AP_V00123_INV2024001234_2024-01-15_ATT1_DELIVERY-ORDER.pdf
INV-AP_V00123_INV2024001234_2024-01-15_ATT2_RECEIPT.pdf
EXP_EMP001_2024-0045_ATT1_HOTEL-RECEIPT.pdf
EXP_EMP001_2024-0045_ATT2_TAXI-RECEIPT.pdf
```

---

## 2. Scanning Standards

### Resolution Guidelines

| Document Type | Minimum Resolution | Recommended | Notes |
|---------------|-------------------|-------------|-------|
| Standard documents (invoices, letters) | 200 DPI | 300 DPI | Black & white or grayscale |
| Documents with fine print | 300 DPI | 400 DPI | Grayscale |
| Contracts with signatures | 300 DPI | 300 DPI | Grayscale or color |
| Color documents (charts, logos) | 300 DPI | 300 DPI | Color |
| Photos (assets, receipts) | 300 DPI | 300 DPI | Color |
| Archival/Legal documents | 300 DPI | 400 DPI | As per original |

### Color Mode

| Document Type | Recommended Mode |
|---------------|------------------|
| Text-only documents | Black & White (1-bit) or Grayscale |
| Documents with stamps/signatures | Grayscale (8-bit) |
| Documents with color content | Color (24-bit) |
| Receipts (thermal paper) | Grayscale - scan promptly before fading |

### File Format

| Format | Use Case | Pros | Cons |
|--------|----------|------|------|
| **PDF/A** (Recommended) | Archival documents | ISO standard, long-term preservation | Slightly larger file size |
| **PDF** | General documents | Universal compatibility | |
| **TIFF** | High-quality archival | Lossless | Large file size |
| **JPEG** | Photos only | Small file size | Lossy compression |

**Recommendation:** Use **PDF/A** for all finance documents for compliance and long-term preservation.

### File Size Guidelines

| Size Range | Action |
|------------|--------|
| < 10 MB | Optimal for SharePoint |
| 10-50 MB | Acceptable, consider compression |
| 50-100 MB | Compress or split if possible |
| > 100 MB | Split into multiple files |

**Compression Tips:**
- Use PDF optimization tools
- Reduce resolution for non-critical documents
- Convert color to grayscale where appropriate
- Remove blank pages

### OCR (Optical Character Recognition)

**Enable OCR for all scanned documents** to make text searchable.

| Setting | Recommendation |
|---------|----------------|
| OCR Language | Set to document language (English, Malay, etc.) |
| OCR Mode | Searchable Image (preserves original appearance) |
| Text Layer | Embedded in PDF |

**Benefits of OCR:**
- Full-text search in SharePoint
- Copy/paste text when needed
- Accessibility compliance
- Data extraction for automation

---

## 3. Document-Specific Guidelines

### Invoices (AP/AR)

**What to Capture:**
- Full invoice (all pages)
- Supporting delivery orders/goods receipts
- Any attached credit/debit notes

**Scanning Tips:**
- Ensure invoice number is clearly visible
- Include any handwritten approvals/stamps
- Scan attachments separately with clear naming

**Example Package:**
```
INV-AP_V00123_INV2024001234_2024-01-15.pdf          (Main invoice)
INV-AP_V00123_INV2024001234_2024-01-15_ATT1_DO.pdf  (Delivery order)
INV-AP_V00123_INV2024001234_2024-01-15_ATT2_GRN.pdf (Goods receipt)
```

---

### Purchase Orders

**What to Capture:**
- Complete PO with all line items
- Approval signatures
- Any amendments/change orders

**Scanning Tips:**
- Ensure PO number is clearly legible
- Capture all pages including terms & conditions
- Scan signed version (not draft)

---

### Contracts & Agreements

**What to Capture:**
- Complete contract (all pages including schedules/annexes)
- Signature pages
- Any amendments/addendums
- Supporting documents (board resolutions, etc.)

**Scanning Tips:**
- Use color scanning for signed pages
- Ensure signatures and stamps are clear
- Include all schedules and attachments
- Scan as single PDF if possible

**Example Package:**
```
CONTRACT_LEASE_ABCPROP_2024-01-01.pdf           (Main contract)
CONTRACT_LEASE_ABCPROP_2024-01-01_SCH-A.pdf     (Schedule A)
CONTRACT_LEASE_ABCPROP_2024-01-01_AMENDMENT-1.pdf (Amendment)
```

---

### Bank Statements

**What to Capture:**
- All pages of the statement
- Any attached advices or notifications

**Scanning Tips:**
- Ensure account number and period are visible
- Keep in chronological order
- Scan front and back if double-sided

---

### Tax Documents

**What to Capture:**
- Tax returns/filings
- Acknowledgment receipts
- Assessments from tax authority
- Supporting computations

**Scanning Tips:**
- Include submission acknowledgment/receipt
- Capture any stamps or official marks
- Keep computation workings as separate files

---

### Expense Claims

**What to Capture:**
- Expense claim form
- All supporting receipts
- Approval documentation

**Scanning Tips:**
- Scan faded thermal receipts promptly
- Group all receipts for one claim together
- Ensure amounts are clearly readable

**Example Package:**
```
EXP_EMP001_2024-0045_CLAIM-FORM.pdf
EXP_EMP001_2024-0045_RECEIPTS.pdf (all receipts in one PDF)
  OR
EXP_EMP001_2024-0045_ATT1_HOTEL.pdf
EXP_EMP001_2024-0045_ATT2_MEALS.pdf
EXP_EMP001_2024-0045_ATT3_TRANSPORT.pdf
```

---

### Cheques / Payment Instruments

**What to Capture:**
- Cheque image (front)
- Cheque image (back - if returned/cancelled)
- Cheque register/log

**Scanning Tips:**
- Scan at higher resolution for security features
- Include MICR line clearly
- For cancelled cheques, ensure "VOID" stamp is visible

---

## 4. Metadata Requirements

After scanning, the following metadata MUST be entered in SharePoint:

### Mandatory Metadata (All Documents)

| Field | Description | Example |
|-------|-------------|---------|
| Document Type | Select from list | Vendor Invoice |
| Fiscal Year | Financial year | 2024 |
| Document Date | Date on the document | 2024-01-15 |
| Confidentiality | Security classification | Internal |

### Document-Specific Metadata

Refer to [02_Finance_Metadata_Design.md](02_Finance_Metadata_Design.md) for complete metadata requirements by document type.

### Quick Reference

| Document Type | Key Metadata to Enter |
|---------------|----------------------|
| Vendor Invoice | Invoice Number, Vendor, Amount, Due Date, PO Number |
| Customer Invoice | Invoice Number, Customer, Amount, Due Date |
| Purchase Order | PO Number, Vendor, Amount, Requestor |
| Payment Voucher | Voucher Number, Payee, Amount, Payment Method |
| Bank Statement | Bank, Account, Period |
| Contract | Contract Number, Counterparty, Start/End Dates, Value |
| Tax Document | Tax Type, Tax Period, Filing Status |
| Expense Claim | Claim Number, Employee, Amount |

---

## 5. Quality Control Checklist

### Pre-Scan Checklist
- [ ] Document is complete (all pages present)
- [ ] Document is flat and unwrinkled
- [ ] Staples/clips removed (if needed for flatbed scan)
- [ ] Document orientation correct
- [ ] No missing or torn sections

### Post-Scan Checklist
- [ ] All pages scanned (count matches original)
- [ ] Image is clear and readable
- [ ] No cut-off text or images
- [ ] Correct orientation (not upside down/sideways)
- [ ] OCR completed successfully (text is searchable)
- [ ] File size is reasonable (< 10MB preferred)
- [ ] File name follows naming convention
- [ ] No blank pages included (unless intentional)

### Upload Checklist
- [ ] File uploaded to correct library
- [ ] All required metadata entered
- [ ] Metadata values are accurate
- [ ] Supporting documents linked/attached
- [ ] Document opens correctly in SharePoint

### Quality Issues - What to Re-scan

| Issue | Action |
|-------|--------|
| Blurry/unreadable text | Re-scan at higher resolution |
| Dark/light image | Adjust brightness/contrast |
| Skewed image | Re-scan with proper alignment |
| Missing pages | Scan missing pages, combine |
| Cut-off edges | Re-position document, re-scan |
| File too large | Optimize/compress PDF |

---

## 6. Original Document Handling

### Retention of Originals

| Document Type | Keep Original? | Retention Period | Notes |
|---------------|----------------|------------------|-------|
| Signed contracts | Yes | Duration + 7 years | Legal requirement |
| Original invoices | Check local law | Per retention policy | Some jurisdictions require originals |
| Tax documents | Yes | 7-10 years | Statutory requirement |
| Audit evidence | Yes | Per audit policy | External auditor may require |
| Cheques (cancelled) | Yes | 7 years | Banking records |
| General correspondence | No | After scanning | Can dispose |
| Internal memos | No | After scanning | Can dispose |
| Receipts | No | After scanning + verification | Can dispose |

### Storage of Physical Originals

For documents requiring physical retention:

1. **Label the storage box:**
   ```
   FINANCE - [Document Type]
   Period: [Date Range]
   Box #: [Sequential Number]
   Contents: [Brief Description]
   Retention Until: [Date]
   ```

2. **Create a box inventory list**

3. **Store in secure, climate-controlled location**

4. **Log location in tracking system**

### Disposal Process

1. Verify retention period has elapsed
2. Obtain approval from Finance Manager
3. Use secure shredding for confidential documents
4. Log disposal date and method
5. Update tracking system

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
- Sort by document type
- Prioritize urgent documents

#### Step 2: Prepare Document
- Remove staples/clips if using sheet feeder
- Flatten creases
- Repair tears with tape (back side)
- Arrange pages in order
- Check completeness

#### Step 3: Scan Document
- Select appropriate scan settings
- Preview first page
- Scan all pages
- Save with correct file name

#### Step 4: Quality Check
- Review scanned image
- Verify all pages captured
- Check readability
- Confirm OCR completed
- Verify file name

#### Step 5: Upload & Enter Metadata
- Upload to correct SharePoint library
- Enter all required metadata
- Link supporting documents
- Verify upload successful

#### Step 6: Store/Dispose Original
- If retention required: file in labeled storage
- If no retention: secure disposal
- Update tracking log

### Batch Processing Tips

For high-volume scanning:

1. **Sort first:** Group similar documents together
2. **Batch scan:** Use document feeder for multiple pages
3. **Batch rename:** Use bulk rename tools if needed
4. **Batch upload:** Upload multiple files at once
5. **Bulk metadata:** Use datasheet view for faster entry

### Recommended Tools

| Purpose | Tool Options |
|---------|--------------|
| Scanning software | Scanner manufacturer software, Adobe Acrobat, NAPS2 (free) |
| PDF editing/combining | Adobe Acrobat, Foxit, PDF-XChange |
| Bulk rename | Bulk Rename Utility (Windows), PowerRename (PowerToys) |
| OCR | Adobe Acrobat, ABBYY FineReader, Tesseract (free) |
| PDF compression | Adobe Acrobat, iLovePDF, SmallPDF |

---

## Appendix A: File Naming Quick Reference Card

```
╔══════════════════════════════════════════════════════════════════╗
║              FINANCE DOCUMENT NAMING QUICK REFERENCE             ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  VENDOR INVOICE                                                  ║
║  INV-AP_[VendorCode]_[InvoiceNo]_[Date].pdf                     ║
║  Example: INV-AP_V00123_INV2024001_2024-01-15.pdf               ║
║                                                                  ║
║  CUSTOMER INVOICE                                                ║
║  INV-AR_[CustomerCode]_[InvoiceNo]_[Date].pdf                   ║
║  Example: INV-AR_C00456_SI2024001_2024-01-15.pdf                ║
║                                                                  ║
║  PURCHASE ORDER                                                  ║
║  PO_[PONumber]_[VendorCode]_[Date].pdf                          ║
║  Example: PO_PO2024000456_V00123_2024-01-10.pdf                 ║
║                                                                  ║
║  PAYMENT VOUCHER                                                 ║
║  PV_[VoucherNo]_[Payee]_[Date].pdf                              ║
║  Example: PV_PV2024001234_ABCSUPPLY_2024-02-10.pdf              ║
║                                                                  ║
║  BANK STATEMENT                                                  ║
║  BANK_[BankName]_[Last4Digits]_[Period].pdf                     ║
║  Example: BANK_MAYBANK_1234_2024-01.pdf                         ║
║                                                                  ║
║  CONTRACT                                                        ║
║  CONTRACT_[Type]_[Counterparty]_[StartDate].pdf                 ║
║  Example: CONTRACT_LEASE_ABCPROP_2024-01-01.pdf                 ║
║                                                                  ║
║  TAX DOCUMENT                                                    ║
║  TAX_[TaxType]_[Period]_[DocType].pdf                           ║
║  Example: TAX_GST_2024-Q1_RETURN.pdf                            ║
║                                                                  ║
║  EXPENSE CLAIM                                                   ║
║  EXP_[EmployeeID]_[ClaimNo]_[Date].pdf                          ║
║  Example: EXP_EMP001_2024-0045_2024-01-20.pdf                   ║
║                                                                  ║
║  ─────────────────────────────────────────────────────────────  ║
║  RULES:                                                          ║
║  • Date format: YYYY-MM-DD                                       ║
║  • No special characters: \ / : * ? " < > | # %                  ║
║  • Use hyphens (-) or underscores (_)                            ║
║  • Attachments: Add _ATT1_[Description]                          ║
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
║  STANDARD DOCUMENTS (Invoices, Letters, POs)                     ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Grayscale                                              ║
║  • Format: PDF/A                                                 ║
║  • OCR: Enabled                                                  ║
║                                                                  ║
║  CONTRACTS / SIGNED DOCUMENTS                                    ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Grayscale or Color (for stamps)                        ║
║  • Format: PDF/A                                                 ║
║  • OCR: Enabled                                                  ║
║                                                                  ║
║  RECEIPTS (Thermal Paper)                                        ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Grayscale                                              ║
║  • Format: PDF/A                                                 ║
║  • OCR: Enabled                                                  ║
║  • Note: SCAN IMMEDIATELY - thermal paper fades!                 ║
║                                                                  ║
║  PHOTOS / COLOR DOCUMENTS                                        ║
║  • Resolution: 300 DPI                                           ║
║  • Color: Full Color                                             ║
║  • Format: PDF or JPEG                                           ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## Document History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-30 | Finance Migration Team | Initial version |
