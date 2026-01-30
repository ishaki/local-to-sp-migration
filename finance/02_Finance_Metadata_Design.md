# Finance Department - Metadata Design Specification

## Purpose
This document defines the recommended metadata schema for Finance department documents in SharePoint Online. Proper metadata enables efficient search, filtering, automated workflows, retention policies, and compliance reporting.

---

## Metadata Design Principles

1. **Simplicity** - Only capture metadata that adds value (avoid over-engineering)
2. **Searchability** - Enable users to find documents quickly
3. **Consistency** - Use standardized values across all document types
4. **Compliance** - Support retention and audit requirements

---

## Metadata Categories

| Category | Description | User Action |
|----------|-------------|-------------|
| **Core** | Essential for identification and search | Must enter at upload |
| **Tracking** | For workflow and status monitoring | Update as status changes |
| **Reference** | Additional context, nice to have | Optional entry |
| **Auto** | System-populated or inherited | No user action needed |

---

## Global Metadata (All Finance Documents)

These columns apply to ALL finance document libraries:

| Column Name | Type | Required | Category | Values/Format | Purpose |
|-------------|------|----------|----------|---------------|---------|
| Document Type | Choice | Yes | Core | [See document types below] | Categorize documents |
| Fiscal Year | Choice | Yes | Core | 2020-2026 | Financial period |
| Document Date | Date | Yes | Core | Date picker | Primary date on document |
| Status | Choice | Yes | Tracking | Draft, Pending, Approved, Final | Document lifecycle |
| Confidentiality | Choice | No | Reference | Internal, Confidential, Highly Confidential | Access control |
| Created By | Person | Auto | Auto | System | Audit trail |
| Modified Date | Date | Auto | Auto | System | Audit trail |

---

## Document-Specific Metadata

### 1. Invoices - Accounts Payable (Vendor Invoices)

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Invoice Number | Text | Yes | Core | Vendor's invoice number | INV-2024-001234 |
| Vendor Name | Choice | Yes | Core | [Vendor list] | ABC Supplies Sdn Bhd |
| Invoice Amount | Currency | Yes | Core | Number with decimals | 5,250.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Due Date | Date | Yes | Core | Date picker | 2024-02-15 |
| PO Number | Text | No | Reference | Linked PO reference | PO-2024-000456 |
| Payment Status | Choice | Yes | Tracking | Unpaid, Paid, On Hold | Unpaid |
| Approval Status | Choice | Yes | Tracking | Pending, Approved, Rejected | Pending |

**Simplified from 15 → 8 fields** (Removed: Vendor Code, Tax Amount, Payment Date, Payment Reference, Approved By, Approved Date, GL Account)

---

### 2. Invoices - Accounts Receivable (Customer Invoices)

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Invoice Number | Text | Yes | Core | Company invoice number | SI-2024-001234 |
| Customer Name | Choice | Yes | Core | [Customer list] | XYZ Corporation |
| Invoice Amount | Currency | Yes | Core | Number with decimals | 12,500.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Due Date | Date | Yes | Core | Date picker | 2024-02-15 |
| Collection Status | Choice | Yes | Tracking | Outstanding, Partial, Collected, Written Off | Outstanding |

**Simplified from 11 → 6 fields** (Removed: Customer Code, Tax Amount, Aging Category, Sales Order Reference)

---

### 3. Purchase Orders

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| PO Number | Text | Yes | Core | System PO number | PO-2024-000456 |
| Vendor Name | Choice | Yes | Core | [Vendor list] | ABC Supplies Sdn Bhd |
| Total Amount | Currency | Yes | Core | Number with decimals | 5,000.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| PO Status | Choice | Yes | Tracking | Draft, Approved, Sent, Completed, Cancelled | Approved |
| Requestor | Person | No | Reference | User picker | |

**Simplified from 12 → 6 fields** (Removed: Vendor Code, PO Date, Required Date, Approver, Approval Date, PR Number)

---

### 4. Payment Vouchers

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Voucher Number | Text | Yes | Core | Payment voucher number | PV-2024-001234 |
| Payee Name | Text | Yes | Core | Vendor/Employee name | ABC Supplies Sdn Bhd |
| Payment Amount | Currency | Yes | Core | Number with decimals | 5,250.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Payment Method | Choice | Yes | Core | Bank Transfer, Cheque, Cash | Bank Transfer |
| Reference Invoices | Text | No | Reference | Related invoice numbers | INV-001, INV-002 |

**Simplified from 11 → 6 fields** (Removed: Voucher Date, Bank Account, Cheque Number, Payment Purpose, Prepared By, Approved By)

---

### 5. Bank Statements & Reconciliations

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Bank Name | Choice | Yes | Core | [Bank list] | Maybank |
| Account Number | Text | Yes | Core | Last 4 digits | ****1234 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Statement Period | Text | Yes | Core | Month/Year | January 2024 |
| Reconciliation Status | Choice | Yes | Tracking | Pending, In Progress, Completed | Completed |

**Simplified from 9 → 5 fields** (Removed: Account Name, Statement Date, Reconciled By, Reconciled Date)

---

### 6. Financial Reports

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Report Type | Choice | Yes | Core | P&L, Balance Sheet, Cash Flow, Management Report, Board Report | Profit & Loss |
| Report Period | Choice | Yes | Core | Monthly, Quarterly, Annual | Monthly |
| Report Status | Choice | Yes | Tracking | Draft, Under Review, Final | Final |
| Version | Number | No | Tracking | Version number | 2 |

**Simplified from 11 → 4 fields** (Removed: Period Month, Period Quarter, Prepared By, Reviewed By, Approved By, Approval Date, Distribution List)

---

### 7. Budgets & Forecasts

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Budget Type | Choice | Yes | Core | Annual Budget, Revised Budget, Forecast | Annual Budget |
| Period Covered | Text | Yes | Core | Budget period | FY2024 |
| Budget Status | Choice | Yes | Tracking | Draft, Under Review, Approved | Approved |
| Version | Text | No | Tracking | Version identifier | V1.0 |

**Simplified from 9 → 4 fields** (Removed: Total Budget Amount, Prepared By, Approved By, Approval Date, Effective Date)

---

### 8. Tax Documents

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Tax Type | Choice | Yes | Core | GST/SST, Corporate Tax, Withholding Tax | GST/SST |
| Tax Year | Choice | Yes | Core | Year | 2024 |
| Tax Period | Text | Yes | Core | Period covered | Q1 2024 |
| Filing Type | Choice | Yes | Core | Return, Payment, Assessment | Return |
| Filing Status | Choice | Yes | Tracking | Pending, Filed, Assessed | Filed |
| Due Date | Date | No | Reference | Statutory due date | 2024-04-30 |

**Simplified from 11 → 6 fields** (Removed: Filing Date, Tax Amount, Reference Number, Prepared By, Filed By)

---

### 9. Audit Files

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Audit Type | Choice | Yes | Core | Internal Audit, External Audit, Tax Audit | External Audit |
| Audit Year | Choice | Yes | Core | Year | 2024 |
| Document Category | Choice | Yes | Core | Working Papers, Audit Report, Management Letter | Working Papers |
| Audit Status | Choice | Yes | Tracking | Planning, Fieldwork, Completed | Completed |

**Simplified from 7 → 4 fields** (Removed: Audit Period, Auditor Name, Issue Date)

---

### 10. Contracts & Agreements

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Contract Number | Text | Yes | Core | Unique identifier | CNT-2024-001 |
| Contract Title | Text | Yes | Core | Description | Office Lease Agreement |
| Contract Type | Choice | Yes | Core | Vendor, Lease, Service, NDA, License | Lease |
| Counterparty | Text | Yes | Core | Other party name | ABC Properties Sdn Bhd |
| Start Date | Date | Yes | Core | Contract start | 2024-01-01 |
| End Date | Date | Yes | Core | Contract expiry | 2026-12-31 |
| Contract Value | Currency | No | Reference | Total value | 120,000.00 |
| Currency | Choice | No | Reference | MYR, USD, SGD, EUR | MYR |
| Contract Status | Choice | Yes | Tracking | Draft, Active, Expired, Terminated | Active |

**Simplified from 15 → 9 fields** (Removed: Renewal Date, Auto Renewal, Notice Period, Signed Date, Signed Copy, Owner)

---

### 11. Expense Claims

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Claim Number | Text | Yes | Core | Expense claim reference | EXP-2024-001234 |
| Employee Name | Person | Yes | Core | User picker | |
| Total Amount | Currency | Yes | Core | Total claim amount | 1,250.00 |
| Currency | Choice | Yes | Core | MYR, USD, SGD, EUR | MYR |
| Expense Category | Choice | Yes | Core | Travel, Meals, Transport, Training, Other | Travel |
| Purpose | Text | Yes | Core | Business purpose | Client meeting |
| Approval Status | Choice | Yes | Tracking | Pending, Approved, Rejected, Paid | Approved |

**Simplified from 14 → 7 fields** (Removed: Employee ID, Claim Date, Expense Period, Approved By, Approved Date, Payment Status, Payment Date)

---

### 12. Journal Entries

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Journal Number | Text | Yes | Core | JV reference | JV-2024-001234 |
| Journal Type | Choice | Yes | Core | Standard, Adjusting, Closing, Reversing | Adjusting |
| Description | Text | Yes | Core | Journal description | Month-end accruals |
| Posting Status | Choice | Yes | Tracking | Draft, Posted, Reversed | Posted |

**Simplified from 11 → 4 fields** (Removed: Journal Date, Total Debit, Total Credit, Prepared By, Approved By, Posted By, Posted Date)

---

### 13. Policies & Procedures

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Policy Number | Text | Yes | Core | Policy identifier | FIN-POL-001 |
| Policy Title | Text | Yes | Core | Policy name | Travel & Expense Policy |
| Policy Category | Choice | Yes | Core | Travel, Expense, Procurement, Accounting | Travel |
| Version | Text | Yes | Core | Version number | 3.0 |
| Effective Date | Date | Yes | Core | When policy takes effect | 2024-01-01 |
| Policy Status | Choice | Yes | Tracking | Draft, Active, Superseded, Retired | Active |

**Simplified from 10 → 6 fields** (Removed: Review Date, Approved By, Approval Date, Supersedes)

---

### 14. Fixed Assets

| Column Name | Type | Required | Category | Values/Format | Example |
|-------------|------|----------|----------|---------------|---------|
| Asset Number | Text | Yes | Core | Fixed asset code | FA-2024-001 |
| Asset Description | Text | Yes | Core | Asset name | Dell Laptop Latitude 5520 |
| Asset Category | Choice | Yes | Core | Computer, Office Equipment, Furniture, Vehicle | Computer |
| Acquisition Date | Date | Yes | Core | Purchase date | 2024-01-15 |
| Acquisition Cost | Currency | Yes | Core | Original cost | 5,500.00 |
| Asset Status | Choice | Yes | Tracking | Active, Disposed, Written Off | Active |
| Location | Choice | No | Reference | Asset location | HQ - Level 5 |

**Simplified from 12 → 7 fields** (Removed: Serial Number, Useful Life, Depreciation Method, Disposal Date, Disposal Value, Assigned To)

---

## Summary: Field Count Comparison

| Document Type | Original | Simplified | Reduction |
|---------------|----------|------------|-----------|
| Vendor Invoices (AP) | 15 | 8 | -47% |
| Customer Invoices (AR) | 11 | 6 | -45% |
| Purchase Orders | 12 | 6 | -50% |
| Payment Vouchers | 11 | 6 | -45% |
| Bank Statements | 9 | 5 | -44% |
| Financial Reports | 11 | 4 | -64% |
| Budgets & Forecasts | 9 | 4 | -56% |
| Tax Documents | 11 | 6 | -45% |
| Audit Files | 7 | 4 | -43% |
| Contracts | 15 | 9 | -40% |
| Expense Claims | 14 | 7 | -50% |
| Journal Entries | 11 | 4 | -64% |
| Policies | 10 | 6 | -40% |
| Fixed Assets | 12 | 7 | -42% |
| **TOTAL** | **158** | **82** | **-48%** |

---

## Category Distribution

| Category | Count | % of Total | User Effort |
|----------|-------|------------|-------------|
| Core | 58 | 71% | Enter at upload |
| Tracking | 18 | 22% | Update when status changes |
| Reference | 6 | 7% | Optional |
| Auto | - | - | System handles |

---

## Implementation Notes

1. **Start Simple**: Begin with Core fields only; add Reference fields later if needed
2. **Default Values**: Set Fiscal Year to current year, Status to "Draft"
3. **Choice Lists**: Keep options to 5-7 items where possible
4. **Views**: Create views filtered by Status for workflow tracking
5. **Training**: Focus training on Core fields only

---

## Managed Metadata (Term Store)

Consider Term Store for frequently used lists:

```
Finance
├── Document Types (14 types)
├── Vendors (managed list)
├── Customers (managed list)
├── Banks (managed list)
└── Cost Centers (optional)
```

---

## Notes

- Fields removed are typically: workflow participants (Prepared By, Approved By), detailed dates, codes that duplicate names, and calculated/derived values
- If detailed tracking is required, fields can be added back for specific document types
- Consider using Power Automate to auto-populate some removed fields if needed later
