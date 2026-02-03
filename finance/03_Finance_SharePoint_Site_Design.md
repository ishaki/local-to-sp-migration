# Finance Department - SharePoint Site Design

## Purpose
This document outlines the SharePoint Online site architecture for the Finance Department, following Microsoft best practices for document management, security, and collaboration.

---

## Design Principles

1. **Flat Structure** - Minimize folder depth, use metadata for organization
2. **Security by Design** - Separate sensitive content into distinct libraries
3. **Scalability** - Design for growth and future requirements
4. **User Experience** - Easy navigation and document discovery
5. **Compliance Ready** - Support retention policies and audit requirements

---

## Site Architecture Overview

```
Finance Department (Team Site)
│
├── 📚 Document Libraries (10)
│   ├── Accounts Payable
│   ├── Accounts Receivable
│   ├── Banking & Treasury
│   ├── Financial Reporting
│   ├── Budgets & Forecasts
│   ├── Tax & Compliance
│   ├── Audit Files (Restricted)
│   ├── Contracts & Agreements
│   ├── Policies & Procedures
│   └── Fixed Assets
│
├── 📋 Lists (6)
│   ├── Vendor Master
│   ├── Customer Master
│   ├── Bank Master
│   ├── Fixed Asset Register
│   ├── Contract Tracker
│   └── Task Tracker
│
└── 📄 Pages
    ├── Home (Dashboard)
    └── Training Resources
```

---

## Document Libraries - Detailed Design

### 1. Accounts Payable

**Purpose:** Store all vendor-related documents including invoices, purchase orders, and payment vouchers.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/AccountsPayable` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Vendor Invoice | Invoices received from vendors |
| Purchase Order | POs issued to vendors |
| Payment Voucher | Payment documentation |
| Goods Receipt Note | Delivery/receipt confirmation |
| Debit/Credit Note | Adjustments to invoices |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| Pending Payment | Payment Status = Unpaid | AP work queue |
| Pending Approval | Approval Status = Pending | Approval queue |
| By Vendor | Group by Vendor Name | Vendor-based search |
| By Fiscal Year | Group by Fiscal Year | Year-end review |
| This Month | Document Date = This Month | Current month activity |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Contribute |
| External Auditors | Read (during audit period) |

---

### 2. Accounts Receivable

**Purpose:** Customer invoices, billing documents, and collection records.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/AccountsReceivable` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Customer Invoice | Invoices issued to customers |
| Credit Note | Credit adjustments |
| Debit Note | Debit adjustments |
| Statement of Account | Customer account statements |
| Collection Letter | Collection correspondence |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| Outstanding | Collection Status = Outstanding | Collection work queue |
| Overdue | Collection Status = Outstanding AND Due Date < Today | Priority collection |
| By Customer | Group by Customer Name | Customer-based search |
| By Fiscal Year | Group by Fiscal Year | Year-end review |
| Collected This Month | Collection Status = Collected AND Modified = This Month | Monthly tracking |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Contribute |
| External Auditors | Read (during audit period) |

---

### 3. Banking & Treasury

**Purpose:** Bank statements, reconciliations, and cash management documents.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/BankingTreasury` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Bank Statement | Monthly/periodic bank statements |
| Bank Reconciliation | Reconciliation worksheets |
| Cash Position Report | Daily/weekly cash position |
| Fund Transfer Request | Inter-bank transfer documentation |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Bank | Group by Bank Name | Bank-based search |
| By Period | Group by Statement Period | Period-based search |
| Pending Reconciliation | Reconciliation Status = Pending | Work queue |
| Completed | Reconciliation Status = Completed | Completed work |
| Current Year | Fiscal Year = [Current Year] | Current year focus |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Contribute |
| External Auditors | Read (during audit period) |

---

### 4. Financial Reporting

**Purpose:** Monthly, quarterly, and annual financial reports.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/FinancialReporting` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required (for final reports) |
| Content Approval | Yes (for final reports) |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Profit & Loss Statement | Income statement |
| Balance Sheet | Statement of financial position |
| Cash Flow Statement | Cash flow report |
| Trial Balance | Period trial balance |
| Management Report | Internal management reports |
| Board Report | Reports for board meetings |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Reports | None | Default view |
| Monthly Reports | Report Period = Monthly | Monthly reports |
| Quarterly Reports | Report Period = Quarterly | Quarterly reports |
| Annual Reports | Report Period = Annual | Annual reports |
| Draft Reports | Report Status = Draft | Work in progress |
| Final Reports | Report Status = Final | Approved reports |
| By Report Type | Group by Report Type | Type-based search |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Contribute |
| Management | Read (Final reports only) |
| External Auditors | Read (during audit period) |

---

### 5. Budgets & Forecasts

**Purpose:** Budget planning documents, forecasts, and variance analysis.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/BudgetsForecasts` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Annual Budget | Yearly budget documents |
| Revised Budget | Mid-year budget revisions |
| Forecast | Rolling forecasts |
| Variance Report | Budget vs actual analysis |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| Current Year | Period Covered = [Current FY] | Current budget focus |
| By Budget Type | Group by Budget Type | Type-based search |
| Approved | Budget Status = Approved | Approved budgets |
| Working Drafts | Budget Status = Draft | Work in progress |
| By Version | Group by Version | Version tracking |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Read |
| Budget Preparers | Contribute |
| Management | Read (Approved only) |
| External Auditors | Read (during audit period) |

---

### 6. Tax & Compliance

**Purpose:** Tax filings, returns, and compliance documentation.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/TaxCompliance` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Tax Return | Tax filing documents |
| Tax Payment | Payment receipts/proof |
| Tax Assessment | Assessment notices |
| Tax Correspondence | Communication with tax authority |
| Compliance Certificate | Compliance certifications |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Tax Type | Group by Tax Type | Type-based search |
| By Tax Year | Group by Tax Year | Year-based search |
| Pending Filing | Filing Status = Pending | Filing work queue |
| Filed | Filing Status = Filed | Completed filings |
| Upcoming Due Dates | Due Date = Next 30 Days | Deadline tracking |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Tax Team | Contribute |
| Finance Members | Read |
| External Auditors | Read (during audit period) |

---

### 7. Audit Files (Restricted)

**Purpose:** Internal and external audit working papers and reports.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/AuditFiles` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required |
| Content Approval | No |
| **Unique Permissions** | **Yes - Break inheritance** |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Audit Engagement Letter | Engagement documentation |
| Audit Working Paper | Audit evidence and workings |
| Audit Report | Final audit reports |
| Management Letter | Auditor recommendations |
| Audit Response | Management responses |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Audit Year | Group by Audit Year | Year-based search |
| By Audit Type | Group by Audit Type | Type-based search |
| External Audit | Audit Type = External Audit | External audit files |
| Internal Audit | Audit Type = Internal Audit | Internal audit files |
| Current Year | Audit Year = [Current Year] | Current audit |

**Folders:** None - use metadata for organization

**Permissions (Restricted):**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Senior Finance | Contribute |
| Finance Members | No Access |
| External Auditors | Contribute (during audit period only) |

**Special Settings:**
- Break permission inheritance from site
- Enable audit log tracking
- Disable delete for non-owners
- Require check-out for editing

---

### 8. Contracts & Agreements

**Purpose:** Vendor contracts, leases, service agreements, and other legal documents.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/Contracts` |
| Versioning | Major versions only, keep 100 versions |
| Check-out | Required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Vendor Agreement | Vendor/supplier contracts |
| Service Contract | Service agreements |
| Lease Agreement | Property/equipment leases |
| NDA | Non-disclosure agreements |
| License Agreement | Software/IP licenses |
| Loan Agreement | Financing agreements |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Contracts | None | Default view |
| Active Contracts | Contract Status = Active | Current contracts |
| Expiring Soon | End Date = Next 90 Days | Renewal planning |
| Expired | Contract Status = Expired | Historical |
| By Contract Type | Group by Contract Type | Type-based search |
| By Counterparty | Group by Counterparty | Party-based search |
| High Value | Contract Value > 100,000 | High-value tracking |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Contribute |
| External Auditors | Read (during audit period) |

**Automation (Power Automate):**
- Send email notification 90 days before contract expiry
- Send reminder 30 days before contract expiry

---

### 9. Policies & Procedures

**Purpose:** Finance policies, standard operating procedures, and guidelines.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/Policies` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Required |
| Content Approval | Yes |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Policy | Official policy documents |
| SOP | Standard operating procedures |
| Guideline | Best practice guidelines |
| Form Template | Standard form templates |
| Process Flowchart | Visual process documentation |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Policies | None | Default view |
| Active Policies | Policy Status = Active | Current policies |
| By Category | Group by Policy Category | Category-based search |
| Recently Updated | Modified = Last 30 Days | Recent changes |
| Under Review | Policy Status = Under Review | Review queue |
| Superseded | Policy Status = Superseded | Historical versions |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Policy Owners | Contribute |
| Finance Members | Read |
| All Employees | Read (selected policies) |

---

### 10. Fixed Assets

**Purpose:** Asset documentation, depreciation schedules, and disposal records.

| Setting | Value |
|---------|-------|
| URL | `/sites/finance/FixedAssets` |
| Versioning | Major versions only, keep 50 versions |
| Check-out | Not required |
| Content Approval | No |

**Content Types:**
| Content Type | Description |
|--------------|-------------|
| Asset Documentation | Supporting documents for assets |
| Depreciation Schedule | Depreciation calculations |
| Asset Disposal Form | Disposal documentation |
| Asset Photo | Photos of physical assets |
| Asset Transfer Form | Inter-department transfers |

**Views:**
| View Name | Filter/Group | Purpose |
|-----------|--------------|---------|
| All Documents | None | Default view |
| By Asset Category | Group by Asset Category | Category-based search |
| By Location | Group by Location | Location-based search |
| Active Assets | Asset Status = Active | Current assets |
| Disposed Assets | Asset Status = Disposed | Disposed records |
| By Acquisition Year | Group by Fiscal Year | Year-based search |

**Folders:** None - use metadata for organization

**Permissions:**
| Group | Permission Level |
|-------|------------------|
| Finance Owners | Full Control |
| Finance Members | Contribute |
| External Auditors | Read (during audit period) |

---

## SharePoint Lists - Detailed Design

### 1. Vendor Master

**Purpose:** Centralized list of approved vendors for lookup in document metadata.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Vendor Code | Text | Yes | Unique vendor identifier |
| Vendor Name | Text | Yes | Official vendor name |
| Contact Person | Text | No | Primary contact |
| Email | Text | No | Contact email |
| Phone | Text | No | Contact phone |
| Address | Multiple lines | No | Business address |
| Payment Terms | Choice | No | Net 30, Net 60, etc. |
| Status | Choice | Yes | Active, Inactive |

**Views:** All Vendors, Active Vendors, By Status

---

### 2. Customer Master

**Purpose:** Centralized list of customers for lookup in document metadata.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Customer Code | Text | Yes | Unique customer identifier |
| Customer Name | Text | Yes | Official customer name |
| Contact Person | Text | No | Primary contact |
| Email | Text | No | Contact email |
| Phone | Text | No | Contact phone |
| Address | Multiple lines | No | Business address |
| Credit Terms | Choice | No | Net 30, Net 60, etc. |
| Credit Limit | Currency | No | Approved credit limit |
| Status | Choice | Yes | Active, Inactive |

**Views:** All Customers, Active Customers, By Status

---

### 3. Bank Master

**Purpose:** Centralized list of company bank accounts for lookup in payment vouchers.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Bank Name | Text | Yes | Name of the bank |
| Account Number | Text | Yes | Full account number (restricted view) |
| Account Number (Masked) | Calculated | Auto | Last 4 digits only |
| Account Name | Text | Yes | Account holder name |
| Account Type | Choice | Yes | Current, Savings, Fixed Deposit |
| Currency | Choice | Yes | MYR, USD, SGD, EUR |
| Branch | Text | No | Branch name |
| Swift Code | Text | No | International transfers |
| Status | Choice | Yes | Active, Inactive, Closed |

**Views:** All Accounts, Active Accounts, By Bank, By Currency

**Permissions:** Restricted to Finance Owners and Senior Finance only

---

### 4. Fixed Asset Register

**Purpose:** Master list of all company fixed assets with key details.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Asset Number | Text | Yes | Unique asset identifier |
| Asset Description | Text | Yes | Asset name/description |
| Asset Category | Choice | Yes | Computer, Furniture, Vehicle, etc. |
| Serial Number | Text | No | Manufacturer serial number |
| Location | Choice | Yes | Physical location |
| Department | Choice | No | Assigned department |
| Acquisition Date | Date | Yes | Purchase date |
| Acquisition Cost | Currency | Yes | Original cost |
| Supplier | Lookup | No | Link to Vendor Master |
| Warranty Expiry | Date | No | Warranty end date |
| Asset Status | Choice | Yes | Active, Disposed, Written Off, Under Repair |
| Assigned To | Person | No | Current custodian |
| Disposal Date | Date | No | Date disposed |
| Disposal Value | Currency | No | Sale/disposal proceeds |
| Remarks | Multiple lines | No | Additional notes |

**Views:** All Assets, Active Assets, By Category, By Location, By Department, Disposed Assets

---

### 5. Contract Tracker

**Purpose:** Track contract milestones, renewals, and key dates.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Contract | Lookup | Yes | Link to Contracts library |
| Milestone Type | Choice | Yes | Start, Renewal, Review, Expiry |
| Due Date | Date | Yes | Milestone date |
| Responsible Person | Person | Yes | Owner of the action |
| Status | Choice | Yes | Pending, Completed, Overdue |
| Notes | Multiple lines | No | Action notes |
| Reminder Sent | Yes/No | Auto | Email reminder sent |

**Views:** All Items, Upcoming (Next 30 Days), Overdue, By Contract, My Items

**Automation:**
- Power Automate to send reminders 7 days before due date
- Auto-update status to Overdue when past due date

---

### 6. Task Tracker

**Purpose:** Track finance department tasks and action items.

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| Task Title | Text | Yes | Task description |
| Task Category | Choice | Yes | Month-End, Year-End, Audit, Tax, General |
| Priority | Choice | Yes | High, Medium, Low |
| Assigned To | Person | Yes | Task owner |
| Due Date | Date | Yes | Deadline |
| Status | Choice | Yes | Not Started, In Progress, Completed, On Hold |
| Related Library | Choice | No | AP, AR, Tax, etc. |
| Notes | Multiple lines | No | Additional details |
| Completed Date | Date | No | Actual completion date |

**Views:** All Tasks, My Tasks, By Category, By Status, Overdue, This Week

---

## Permission Structure

### Security Groups

| Group Name | Members | Description |
|------------|---------|-------------|
| Finance Owners | Finance Manager, Finance Director | Full control of entire site |
| Finance Members | All Finance Staff | Standard access to most libraries |
| Senior Finance | Senior accountants, supervisors | Access to restricted content |
| Tax Team | Tax specialists | Full access to Tax library |
| Budget Preparers | Budget coordinators | Edit access to Budgets |
| Policy Owners | Designated policy managers | Edit access to Policies |
| External Auditors | External audit firm staff | Time-limited read/contribute access |

### Permission Matrix by Library

| Library | Finance Owners | Finance Members | Senior Finance | External Auditors |
|---------|----------------|-----------------|----------------|-------------------|
| Accounts Payable | Full Control | Contribute | Contribute | Read |
| Accounts Receivable | Full Control | Contribute | Contribute | Read |
| Banking & Treasury | Full Control | Contribute | Contribute | Read |
| Financial Reporting | Full Control | Contribute | Contribute | Read |
| Budgets & Forecasts | Full Control | Read | Contribute | Read |
| Tax & Compliance | Full Control | Read | Contribute | Read |
| **Audit Files** | Full Control | **No Access** | Contribute | **Contribute** |
| Contracts | Full Control | Contribute | Contribute | Read |
| Policies | Full Control | Read | Read | Read |
| Fixed Assets | Full Control | Contribute | Contribute | Read |

### External Auditor Access

**Access Period:** During annual audit (typically 2-3 months)

**Setup Process:**
1. Create Microsoft 365 guest accounts for auditors
2. Add to "External Auditors" group
3. Grant access at start of audit
4. Remove access at audit completion
5. Document access dates for compliance

**Accessible Content:**
- All document libraries (Read access)
- Audit Files library (Contribute access)
- SharePoint Lists (Read access)

---

## Navigation Design

### Left Navigation (Quick Launch)

```
🏠 Home
─────────────────────────────
DOCUMENTS
─────────────────────────────
📁 Accounts Payable
📁 Accounts Receivable
📁 Banking & Treasury
📁 Financial Reporting
📁 Budgets & Forecasts
📁 Tax & Compliance
📁 Audit Files
📁 Contracts
📁 Policies
📁 Fixed Assets
─────────────────────────────
LISTS
─────────────────────────────
📋 Vendor Master
📋 Customer Master
📋 Bank Master
📋 Fixed Asset Register
📋 Contract Tracker
📋 Task Tracker
─────────────────────────────
RESOURCES
─────────────────────────────
📄 Training Resources
```

### Home Page Layout

```
┌─────────────────────────────────────────────────────────────────────────┐
│  FINANCE DEPARTMENT                                          [🔍 Search]│
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐           │
│  │ 📁 QUICK ACCESS │ │ ⏰ PENDING      │ │ 📅 EXPIRING     │           │
│  │                 │ │    TASKS        │ │    CONTRACTS    │           │
│  │ • AP Invoices   │ │                 │ │                 │           │
│  │ • AR Invoices   │ │ [Task list      │ │ [Contract list  │           │
│  │ • Bank Recon    │ │  web part]      │ │  web part]      │           │
│  │ • Tax Documents │ │                 │ │                 │           │
│  │ • Policies      │ │                 │ │                 │           │
│  └─────────────────┘ └─────────────────┘ └─────────────────┘           │
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐│
│  │ 📢 ANNOUNCEMENTS                                                    ││
│  │ ─────────────────────────────────────────────────────────────────── ││
│  │ • Month-end closing deadline: [Date]                                ││
│  │ • Tax filing deadline: [Date]                                       ││
│  │ • New policy effective: [Date]                                      ││
│  └─────────────────────────────────────────────────────────────────────┘│
│                                                                         │
│  ┌──────────────────────────────┐ ┌────────────────────────────────────┐│
│  │ 📄 RECENT DOCUMENTS          │ │ 📊 KEY DEADLINES                   ││
│  │                              │ │                                    ││
│  │ [Document library web part   │ │ • Month-end close: 5th            ││
│  │  showing recent files]       │ │ • GST filing: [Date]              ││
│  │                              │ │ • Audit preparation: [Date]       ││
│  │                              │ │ • Budget submission: [Date]       ││
│  └──────────────────────────────┘ └────────────────────────────────────┘│
│                                                                         │
│  ┌─────────────────────────────────────────────────────────────────────┐│
│  │ 📚 RESOURCES                                                        ││
│  │                                                                     ││
│  │ [Finance Policies]  [Training Materials]  [Forms & Templates]       ││
│  └─────────────────────────────────────────────────────────────────────┘│
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

### Home Page Web Parts

| Section | Web Part Type | Data Source |
|---------|---------------|-------------|
| Quick Access | Quick Links | Manual links to libraries |
| Pending Tasks | List | Task Tracker (Status ≠ Completed) |
| Expiring Contracts | Document Library | Contracts (End Date = Next 90 Days) |
| Announcements | News | Site News posts |
| Recent Documents | Document Library | Site-wide recent documents |
| Key Deadlines | Text | Manual entry or Events list |
| Resources | Quick Links | Links to Policies, Training |

---

## Retention Policies

### Retention Schedule

| Library | Retention Period | Action | Legal Basis |
|---------|------------------|--------|-------------|
| Accounts Payable | 7 years | Archive → Delete | Tax/Audit requirements |
| Accounts Receivable | 7 years | Archive → Delete | Tax/Audit requirements |
| Banking & Treasury | 7 years | Archive → Delete | Banking regulations |
| Financial Reporting | Permanent | Archive only | Statutory requirement |
| Budgets & Forecasts | 7 years | Archive → Delete | Internal policy |
| Tax & Compliance | 10 years | Archive → Delete | Tax authority requirements |
| Audit Files | 10 years | Archive → Delete | Audit standards |
| Contracts | 7 years after expiry | Archive → Delete | Legal requirements |
| Policies | Permanent (current) | Archive old versions | Compliance |
| Fixed Assets | 7 years after disposal | Archive → Delete | Tax requirements |

### Retention Implementation

1. **Apply retention labels** in Microsoft Purview Compliance Center
2. **Auto-apply labels** based on document type metadata
3. **Review disposition** before deletion for sensitive content
4. **Document exceptions** for legal holds

---

## Implementation Checklist

### Phase 1: Site Creation & Setup
| Task | Owner | Status |
|------|-------|--------|
| Create Finance Team Site | IT Admin | ☐ |
| Configure site settings (regional, time zone) | IT Admin | ☐ |
| Set site logo and branding | IT Admin | ☐ |
| Configure site permissions | IT Admin | ☐ |
| Create security groups | IT Admin | ☐ |

### Phase 2: Document Libraries
| Task | Owner | Status |
|------|-------|--------|
| Create all 10 document libraries | IT Admin | ☐ |
| Configure versioning settings | IT Admin | ☐ |
| Configure check-out requirements | IT Admin | ☐ |
| Create site columns (metadata) | IT Admin | ☐ |
| Create content types | IT Admin | ☐ |
| Apply content types to libraries | IT Admin | ☐ |
| Set library permissions | IT Admin | ☐ |
| Break inheritance for Audit Files | IT Admin | ☐ |

### Phase 3: SharePoint Lists
| Task | Owner | Status |
|------|-------|--------|
| Create Vendor Master list | Finance | ☐ |
| Create Customer Master list | Finance | ☐ |
| Create Bank Master list | Finance | ☐ |
| Create Fixed Asset Register list | Finance | ☐ |
| Create Contract Tracker list | Finance | ☐ |
| Create Task Tracker list | Finance | ☐ |
| Import existing data to lists | Finance | ☐ |

### Phase 4: Views & Navigation
| Task | Owner | Status |
|------|-------|--------|
| Create views for each library | Finance | ☐ |
| Configure left navigation | IT Admin | ☐ |
| Design home page | IT Admin | ☐ |
| Add web parts to home page | IT Admin | ☐ |
| Test navigation flow | Finance | ☐ |

### Phase 5: Automation
| Task | Owner | Status |
|------|-------|--------|
| Create contract expiry notification flow | IT Admin | ☐ |
| Create task reminder flow | IT Admin | ☐ |
| Test all automation flows | IT Admin | ☐ |

### Phase 6: Security & Compliance
| Task | Owner | Status |
|------|-------|--------|
| Verify all permission settings | IT Admin | ☐ |
| Test access with each user role | Finance | ☐ |
| Configure retention labels | IT Admin | ☐ |
| Apply retention labels to libraries | IT Admin | ☐ |
| Document external auditor access process | Finance | ☐ |

### Phase 7: Data Migration
| Task | Owner | Status |
|------|-------|--------|
| Run file server audit | IT Admin | ☐ |
| Clean up unnecessary files | Finance | ☐ |
| Create migration mapping | Finance | ☐ |
| Migrate documents | IT Admin | ☐ |
| Verify migration completeness | Finance | ☐ |
| Apply metadata to migrated documents | Finance | ☐ |

### Phase 8: Training & Go-Live
| Task | Owner | Status |
|------|-------|--------|
| Prepare training materials | Finance | ☐ |
| Conduct training sessions | Finance | ☐ |
| Create quick reference guides | Finance | ☐ |
| Pilot with select users | Finance | ☐ |
| Gather feedback and adjust | Finance | ☐ |
| Full team go-live | Finance | ☐ |
| Post-go-live support | IT Admin | ☐ |

---

## Best Practices

### Document Management
1. **No deep folders** - Maximum 2 levels; use metadata instead
2. **Consistent naming** - Follow file naming conventions
3. **Version control** - Don't save as "v2", "final", etc.; use SharePoint versions
4. **Regular cleanup** - Archive old documents per retention policy

### Search & Discovery
1. **Use metadata** - Fill in all required fields for searchability
2. **Meaningful titles** - Use descriptive document names
3. **Tags** - Use managed metadata where configured

### Collaboration
1. **Co-authoring** - Use for simultaneous editing (Word, Excel)
2. **Comments** - Use document comments instead of email
3. **Alerts** - Set up alerts for important libraries

### Security
1. **Don't share externally** - Unless approved; use external auditor process
2. **Report issues** - Notify Finance Manager of any security concerns
3. **Clean up access** - Remove users who leave the team

---

## Appendix: Standard Views Reference

### Views for All Libraries

| View Name | Filter | Group By | Columns |
|-----------|--------|----------|---------|
| All Documents | None | None | Name, Document Type, Modified, Modified By |
| By Fiscal Year | None | Fiscal Year | Name, Document Type, Status, Modified |
| My Documents | Created By = [Me] | None | Name, Document Type, Modified |
| Recent (7 days) | Modified ≥ [Today-7] | None | Name, Document Type, Modified, Modified By |
| Draft | Status = Draft | None | Name, Document Type, Created, Modified |
| This Month | Document Date ≥ First Day of Month | None | Name, Document Type, Modified |

### Status-Based Views

| View Name | Filter | Purpose |
|-----------|--------|---------|
| Pending Approval | Approval Status = Pending | Approval queue |
| Pending Payment | Payment Status = Unpaid | Payment queue |
| Outstanding | Collection Status = Outstanding | Collection queue |
| Pending Reconciliation | Reconciliation Status = Pending | Recon queue |

---

## Document Control

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2025-01-31 | Finance Migration Team | Initial version |
