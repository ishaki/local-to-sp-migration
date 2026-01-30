# Finance Department - Metadata Design Specification

## Purpose
This document defines the recommended metadata schema for Finance department documents in SharePoint Online. Proper metadata enables efficient search, filtering, automated workflows, retention policies, and compliance reporting.

---

## Metadata Design Principles

1. **Consistency** - Use standardized values across all document types
2. **Searchability** - Enable users to find documents quickly
3. **Compliance** - Support retention and audit requirements
4. **Automation** - Enable workflow triggers and automated processing
5. **Simplicity** - Only capture metadata that adds value (avoid over-engineering)

---

## Global Metadata (All Finance Documents)

These columns apply to ALL finance document libraries:

| Column Name | Type | Required | Values/Format | Purpose |
|-------------|------|----------|---------------|---------|
| Document Type | Choice | Yes | [See document types below] | Categorize documents |
| Fiscal Year | Choice | Yes | 2020, 2021, 2022, 2023, 2024, 2025, 2026 | Financial period |
| Confidentiality | Choice | Yes | Public, Internal, Confidential, Highly Confidential | Access control |
| Status | Choice | Yes | Draft, Pending Review, Approved, Final, Archived | Document lifecycle |
| Department/Cost Center | Choice | No | [Company-specific list] | Cost allocation |
| Retention Label | Managed Metadata | Auto | [Based on document type] | Compliance |

---

## Document-Specific Metadata

### 1. Invoices - Accounts Payable (Vendor Invoices)

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Invoice Number | Single line text | Yes | Vendor's invoice number | INV-2024-001234 |
| Vendor Name | Choice/Lookup | Yes | [Vendor master list] | ABC Supplies Sdn Bhd |
| Vendor Code | Single line text | No | ERP vendor code | V00123 |
| Invoice Date | Date | Yes | Date picker | 2024-01-15 |
| Due Date | Date | Yes | Date picker | 2024-02-15 |
| Invoice Amount | Currency | Yes | Number with 2 decimals | 5,250.00 |
| Currency | Choice | Yes | MYR, USD, SGD, EUR, etc. | MYR |
| Tax Amount | Currency | No | Number with 2 decimals | 420.00 |
| PO Number | Single line text | No | Linked PO reference | PO-2024-000456 |
| Payment Status | Choice | Yes | Unpaid, Partially Paid, Paid, On Hold, Disputed | Unpaid |
| Payment Date | Date | No | Date picker | 2024-02-10 |
| Payment Reference | Single line text | No | Cheque/Transfer reference | TRF-20240210-001 |
| Approval Status | Choice | Yes | Pending, Approved, Rejected | Approved |
| Approved By | Person | No | User picker | |
| Approved Date | Date | No | Date picker | |
| GL Account | Single line text | No | General ledger code | 5100-001 |

---

### 2. Invoices - Accounts Receivable (Customer Invoices)

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Invoice Number | Single line text | Yes | Company invoice number | SI-2024-001234 |
| Customer Name | Choice/Lookup | Yes | [Customer master list] | XYZ Corporation |
| Customer Code | Single line text | No | ERP customer code | C00456 |
| Invoice Date | Date | Yes | Date picker | 2024-01-15 |
| Due Date | Date | Yes | Date picker | 2024-02-15 |
| Invoice Amount | Currency | Yes | Number with 2 decimals | 12,500.00 |
| Currency | Choice | Yes | MYR, USD, SGD, EUR, etc. | MYR |
| Tax Amount | Currency | No | Number with 2 decimals | 1,000.00 |
| Collection Status | Choice | Yes | Outstanding, Partial, Collected, Written Off | Outstanding |
| Aging Category | Choice | No | Current, 30 Days, 60 Days, 90 Days, 90+ Days | Current |
| Sales Order Reference | Single line text | No | SO reference | SO-2024-000789 |

---

### 3. Purchase Orders

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| PO Number | Single line text | Yes | System PO number | PO-2024-000456 |
| Vendor Name | Choice/Lookup | Yes | [Vendor master list] | ABC Supplies Sdn Bhd |
| Vendor Code | Single line text | No | ERP vendor code | V00123 |
| PO Date | Date | Yes | Date picker | 2024-01-10 |
| Required Date | Date | No | Delivery required by | 2024-01-25 |
| Total Amount | Currency | Yes | Number with 2 decimals | 5,000.00 |
| Currency | Choice | Yes | MYR, USD, SGD, EUR, etc. | MYR |
| PO Status | Choice | Yes | Draft, Pending Approval, Approved, Sent, Partially Received, Completed, Cancelled | Approved |
| Requestor | Person | Yes | User picker | |
| Approver | Person | No | User picker | |
| Approval Date | Date | No | Date picker | |
| PR Number | Single line text | No | Purchase Requisition ref | PR-2024-000123 |

---

### 4. Payment Vouchers

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Voucher Number | Single line text | Yes | Payment voucher number | PV-2024-001234 |
| Voucher Date | Date | Yes | Date picker | 2024-02-10 |
| Payee Name | Single line text | Yes | Vendor/Employee name | ABC Supplies Sdn Bhd |
| Payment Amount | Currency | Yes | Number with 2 decimals | 5,250.00 |
| Currency | Choice | Yes | MYR, USD, SGD, EUR, etc. | MYR |
| Payment Method | Choice | Yes | Bank Transfer, Cheque, Cash, Credit Card | Bank Transfer |
| Bank Account | Choice | No | [Company bank accounts] | Maybank-001 |
| Cheque Number | Single line text | No | If payment by cheque | CHQ-000456 |
| Reference Invoices | Multiple lines text | No | Related invoice numbers | INV-001, INV-002 |
| Payment Purpose | Single line text | No | Description | Supplier payment |
| Prepared By | Person | Yes | User picker | |
| Approved By | Person | No | User picker | |

---

### 5. Bank Statements & Reconciliations

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Bank Name | Choice | Yes | [Bank list] | Maybank |
| Account Number | Single line text | Yes | Last 4 digits or masked | ****1234 |
| Account Name | Single line text | No | Account description | Operating Account |
| Statement Period | Choice | Yes | Month/Year | January 2024 |
| Statement Date | Date | Yes | Date picker | 2024-01-31 |
| Opening Balance | Currency | No | Number with 2 decimals | 100,000.00 |
| Closing Balance | Currency | No | Number with 2 decimals | 125,000.00 |
| Reconciliation Status | Choice | Yes | Pending, In Progress, Completed | Completed |
| Reconciled By | Person | No | User picker | |
| Reconciled Date | Date | No | Date picker | |

---

### 6. Financial Reports

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Report Type | Choice | Yes | Profit & Loss, Balance Sheet, Cash Flow, Trial Balance, Budget vs Actual, Management Report, Board Report | Profit & Loss |
| Report Period | Choice | Yes | Monthly, Quarterly, Half-Yearly, Annual | Monthly |
| Period Month | Choice | No | January - December | January |
| Period Quarter | Choice | No | Q1, Q2, Q3, Q4 | Q1 |
| Report Version | Number | No | Version number | 2 |
| Report Status | Choice | Yes | Draft, Under Review, Final | Final |
| Prepared By | Person | Yes | User picker | |
| Reviewed By | Person | No | User picker | |
| Approved By | Person | No | User picker | |
| Approval Date | Date | No | Date picker | |
| Distribution List | Multiple lines text | No | Who receives this report | Board, Management |

---

### 7. Budgets & Forecasts

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Budget Type | Choice | Yes | Annual Budget, Revised Budget, Forecast, Rolling Forecast | Annual Budget |
| Budget Version | Single line text | Yes | Version identifier | V1.0, V2.0 |
| Period Covered | Single line text | Yes | Budget period | FY2024 |
| Total Budget Amount | Currency | No | Number with 2 decimals | 5,000,000.00 |
| Budget Status | Choice | Yes | Draft, Under Review, Approved, Superseded | Approved |
| Prepared By | Person | Yes | User picker | |
| Approved By | Person | No | User picker | |
| Approval Date | Date | No | Date picker | |
| Effective Date | Date | No | When budget takes effect | 2024-01-01 |

---

### 8. Tax Documents

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Tax Type | Choice | Yes | GST/SST, Corporate Tax, Withholding Tax, Stamp Duty, Property Tax, Payroll Tax | GST/SST |
| Tax Period | Single line text | Yes | Tax period covered | Jan-Mar 2024 |
| Tax Year | Choice | Yes | Tax year | 2024 |
| Filing Type | Choice | Yes | Return, Payment, Refund Claim, Assessment, Appeal | Return |
| Filing Status | Choice | Yes | Pending, Filed, Acknowledged, Assessed | Filed |
| Filing Date | Date | No | Date submitted | 2024-04-15 |
| Due Date | Date | Yes | Statutory due date | 2024-04-30 |
| Tax Amount | Currency | No | Amount payable/refundable | 25,000.00 |
| Reference Number | Single line text | No | Tax authority reference | GST-2024-Q1-001 |
| Prepared By | Person | Yes | User picker | |
| Filed By | Person | No | User picker | |

---

### 9. Audit Files

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Audit Type | Choice | Yes | Internal Audit, External Audit, Tax Audit, Special Audit | External Audit |
| Audit Year | Choice | Yes | Year | 2024 |
| Audit Period | Single line text | No | Period covered | FY2023 |
| Auditor Name | Single line text | No | Audit firm/person | Ernst & Young |
| Document Category | Choice | Yes | Engagement Letter, Working Papers, Audit Report, Management Letter, Response | Working Papers |
| Audit Status | Choice | Yes | Planning, Fieldwork, Review, Completed | Completed |
| Issue Date | Date | No | Report issue date | 2024-03-15 |

---

### 10. Contracts & Agreements

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Contract Number | Single line text | Yes | Unique identifier | CNT-2024-001 |
| Contract Title | Single line text | Yes | Description | Office Lease Agreement |
| Contract Type | Choice | Yes | Vendor Agreement, Lease, Loan, Service Agreement, NDA, Employment, License | Lease |
| Counterparty | Single line text | Yes | Other party name | ABC Properties Sdn Bhd |
| Contract Value | Currency | No | Total contract value | 120,000.00 |
| Currency | Choice | No | MYR, USD, SGD, EUR | MYR |
| Start Date | Date | Yes | Contract effective date | 2024-01-01 |
| End Date | Date | Yes | Contract expiry date | 2026-12-31 |
| Renewal Date | Date | No | When to review/renew | 2026-10-01 |
| Auto Renewal | Yes/No | No | Does contract auto-renew? | Yes |
| Notice Period | Single line text | No | Notice required | 3 months |
| Contract Status | Choice | Yes | Draft, Active, Expired, Terminated, Renewed | Active |
| Signed Date | Date | No | Date executed | 2023-12-15 |
| Signed Copy | Yes/No | Yes | Is this the signed version? | Yes |
| Owner | Person | Yes | Contract owner | |

---

### 11. Expense Claims / Reports

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Claim Number | Single line text | Yes | Expense claim reference | EXP-2024-001234 |
| Employee Name | Person | Yes | User picker | |
| Employee ID | Single line text | No | Staff ID | EMP001 |
| Claim Date | Date | Yes | Submission date | 2024-01-20 |
| Expense Period | Single line text | No | Period covered | Jan 2024 |
| Total Amount | Currency | Yes | Total claim amount | 1,250.00 |
| Currency | Choice | Yes | MYR, USD, SGD, EUR | MYR |
| Expense Category | Choice | Yes | Travel, Accommodation, Meals, Transport, Office Supplies, Entertainment, Training, Other | Travel |
| Purpose | Single line text | Yes | Business purpose | Client meeting - Penang |
| Approval Status | Choice | Yes | Pending, Approved, Rejected, Paid | Approved |
| Approved By | Person | No | User picker | |
| Approved Date | Date | No | Date picker | |
| Payment Status | Choice | Yes | Pending, Processed, Paid | Paid |
| Payment Date | Date | No | Date picker | |

---

### 12. Journal Entries / Vouchers

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Journal Number | Single line text | Yes | JV reference | JV-2024-001234 |
| Journal Date | Date | Yes | Transaction date | 2024-01-31 |
| Journal Type | Choice | Yes | Standard, Adjusting, Closing, Reversing, Recurring | Adjusting |
| Description | Single line text | Yes | Journal description | Month-end accruals |
| Total Debit | Currency | No | Total debit amount | 10,000.00 |
| Total Credit | Currency | No | Total credit amount | 10,000.00 |
| Posting Status | Choice | Yes | Draft, Posted, Reversed | Posted |
| Prepared By | Person | Yes | User picker | |
| Approved By | Person | No | User picker | |
| Posted By | Person | No | User picker | |
| Posted Date | Date | No | Date picker | |

---

### 13. Policies & Procedures

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Policy Number | Single line text | Yes | Policy identifier | FIN-POL-001 |
| Policy Title | Single line text | Yes | Policy name | Travel & Expense Policy |
| Policy Category | Choice | Yes | Travel, Expense, Procurement, Cash Management, Accounting, Tax, Compliance, General | Travel |
| Version | Single line text | Yes | Version number | 3.0 |
| Effective Date | Date | Yes | When policy takes effect | 2024-01-01 |
| Review Date | Date | No | Next review date | 2025-01-01 |
| Policy Status | Choice | Yes | Draft, Active, Under Review, Superseded, Retired | Active |
| Approved By | Person | No | User picker | |
| Approval Date | Date | No | Date picker | |
| Supersedes | Single line text | No | Previous version | FIN-POL-001 V2.0 |

---

### 14. Fixed Assets

| Column Name | Type | Required | Values/Format | Example |
|-------------|------|----------|---------------|---------|
| Asset Number | Single line text | Yes | Fixed asset code | FA-2024-001 |
| Asset Description | Single line text | Yes | Asset name | Dell Laptop Latitude 5520 |
| Asset Category | Choice | Yes | Computer Equipment, Office Equipment, Furniture, Vehicles, Machinery, Building, Land, Leasehold | Computer Equipment |
| Serial Number | Single line text | No | Manufacturer serial | SN123456789 |
| Location | Choice | No | Asset location | HQ - Level 5 |
| Acquisition Date | Date | Yes | Purchase date | 2024-01-15 |
| Acquisition Cost | Currency | Yes | Original cost | 5,500.00 |
| Useful Life | Number | No | Years | 5 |
| Depreciation Method | Choice | No | Straight Line, Declining Balance | Straight Line |
| Asset Status | Choice | Yes | Active, Disposed, Written Off, Under Repair | Active |
| Disposal Date | Date | No | Date picker | |
| Disposal Value | Currency | No | Proceeds from disposal | |
| Assigned To | Person | No | User picker | |

---

## Metadata Implementation Checklist

| Task | Status |
|------|--------|
| Create Site Columns for global metadata | ☐ |
| Create Content Types for each document type | ☐ |
| Configure Choice columns with values | ☐ |
| Set up Lookup columns (Vendor, Customer lists) | ☐ |
| Configure default values where applicable | ☐ |
| Set required fields validation | ☐ |
| Apply Content Types to libraries | ☐ |
| Configure column ordering in forms | ☐ |
| Test metadata entry workflow | ☐ |
| Train users on metadata entry | ☐ |

---

## Managed Metadata (Term Store) - Recommended Terms

Consider creating these term sets in the SharePoint Term Store for consistent values:

### Finance Terms
```
Finance
├── Document Types
│   ├── Invoice - AP
│   ├── Invoice - AR
│   ├── Purchase Order
│   ├── Payment Voucher
│   ├── Bank Statement
│   ├── Financial Report
│   ├── Budget
│   ├── Tax Document
│   ├── Audit File
│   ├── Contract
│   ├── Expense Claim
│   ├── Journal Entry
│   ├── Policy
│   └── Fixed Asset
├── Vendors
│   └── [Vendor list]
├── Customers
│   └── [Customer list]
├── Cost Centers
│   └── [Cost center list]
└── GL Accounts
    └── [Chart of accounts]
```

---

## Notes

1. **Required vs Optional**: Mark fields as required only if absolutely necessary to avoid user frustration
2. **Default Values**: Set sensible defaults (e.g., Fiscal Year = current year) to speed up data entry
3. **Validation**: Use column validation for formats (e.g., Invoice Number format)
4. **Views**: Create filtered views based on key metadata (e.g., Unpaid Invoices, Pending Approvals)
5. **Search**: Ensure key metadata columns are included in search schema
