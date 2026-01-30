# SharePoint Online as Document Management System
## Best Practices & Recommendations

**Version:** 1.0
**Created:** 2026-01-28

---

## Table of Contents

1. [Introduction: File Server vs SharePoint Mindset](#1-introduction-file-server-vs-sharepoint-mindset)
2. [The Great Folder Debate](#2-the-great-folder-debate)
3. [Metadata-Driven Document Management](#3-metadata-driven-document-management)
4. [Recommended Document Library Structure](#4-recommended-document-library-structure)
5. [Naming Conventions](#5-naming-conventions)
6. [Version Control](#6-version-control)
7. [Search Optimization](#7-search-optimization)
8. [Permission Management](#8-permission-management)
9. [Compliance & Governance](#9-compliance--governance)
10. [Common Mistakes to Avoid](#10-common-mistakes-to-avoid)
11. [Migration Strategy: Folders to Metadata](#11-migration-strategy-folders-to-metadata)
12. [Quick Reference Cheat Sheet](#12-quick-reference-cheat-sheet)

---

## 1. Introduction: File Server vs SharePoint Mindset

### The Old Way (File Server)
```
\\FileServer\Departments\Finance\2024\Invoices\Vendor_ABC\January\INV-001.pdf
```
- Location = Organization
- Find files by navigating folders
- One file can only exist in one location
- Security by folder

### The New Way (SharePoint)
```
https://company.sharepoint.com/sites/Finance/Invoices/INV-001.pdf
Metadata: Year=2024, Vendor=ABC, Month=January, Type=Invoice
```
- Metadata = Organization
- Find files by searching and filtering
- One file can appear in multiple views
- Security by permission groups

### Key Mindset Shifts

| File Server Thinking | SharePoint Thinking |
|---------------------|---------------------|
| "Where should I save this?" | "How should I tag this?" |
| Navigate to find | Search to find |
| Folder = Category | Metadata = Category |
| One location per file | Multiple views per file |
| Copy file for different needs | Create view for different needs |
| Folder permissions | Item/library permissions |

---

## 2. The Great Folder Debate

### Why Users Want Nested Folders

Users coming from file servers often want to recreate deep folder structures:
```
Documents/
├── 2024/
│   ├── Q1/
│   │   ├── January/
│   │   │   ├── Projects/
│   │   │   │   ├── Project_Alpha/
│   │   │   │   │   ├── Contracts/
│   │   │   │   │   │   └── Contract_v1.docx    ← 7 levels deep!
```

**Their reasoning:**
- "This is how we've always done it"
- "It's organized and I know where things are"
- "I can see the structure at a glance"

### Why Deep Folders Are Problematic in SharePoint

#### Problem 1: URL/Path Length Limits
```
SharePoint URL limit: 400 characters total

https://company.sharepoint.com/sites/Finance/Shared%20Documents/
2024/Q1/January/Projects/Project_Alpha/Phase1/Deliverables/
Reports/Final/Approved/Contract_Agreement_With_Vendor_ABC_Final_v3.docx

= 200+ characters just for path!
```

**Impact:** Files deep in folders may:
- Fail to sync with OneDrive
- Fail to open in desktop apps
- Cause migration failures
- Break when file is renamed

#### Problem 2: Navigation Nightmare
```
To reach a file 6 levels deep:
Click → Click → Click → Click → Click → Click → Find file

Time: 30-60 seconds per file access
```

**With metadata + search:**
```
Search "Project Alpha Contract" or Filter by Project = Alpha
Time: 5-10 seconds
```

#### Problem 3: Single Classification
A file can only exist in ONE folder location.

**Example:** A contract document that is:
- For Project Alpha
- From 2024
- With Vendor ABC
- Related to Finance

**Folder approach:** Pick ONE location
```
Where does it go?
├── By Project/Project_Alpha/
├── By Year/2024/
├── By Vendor/ABC/
└── By Department/Finance/
```

**Metadata approach:** Tag with ALL attributes
```
File: Contract.pdf
- Project: Alpha
- Year: 2024
- Vendor: ABC
- Department: Finance

→ Appears in ALL relevant views!
```

#### Problem 4: Permissions Complexity
```
Nested folder permissions inheritance:

Documents/           ← Finance Team: Edit
├── Confidential/    ← Finance Managers: Edit (break inheritance)
│   ├── Salaries/    ← HR Only: Edit (break inheritance again)
│   │   └── file.xlsx

Result: Permission spaghetti, hard to audit, easy to make mistakes
```

#### Problem 5: Sync Issues
OneDrive sync works best with:
- Flat or shallow structures
- Shorter paths
- Fewer than 100,000 files per library

Deep folders = sync failures, conflicts, and user frustration

#### Problem 6: Mobile Experience
```
Mobile device folder navigation:
Tap → Wait → Tap → Wait → Tap → Wait → Tap → Wait...

Users give up after 3-4 levels
```

### When Folders ARE Appropriate

Folders aren't evil - they have valid uses:

| Use Case | Why Folders Work |
|----------|------------------|
| Project workspaces | Logical grouping, temporary, clear boundary |
| Year/Month archives | Simple, universal understanding |
| Document sets | Related docs that travel together |
| 1-2 levels max | Quick navigation still efficient |
| Permission boundaries | When group of files needs different access |

**Good folder usage:**
```
Documents/
├── 2024/
│   ├── Project_Alpha/
│   │   ├── contract.pdf
│   │   ├── proposal.docx
│   │   └── budget.xlsx
│   └── Project_Beta/
└── 2025/
```
*2 levels, clear purpose, manageable*

**Bad folder usage:**
```
Documents/
├── Departments/
│   ├── Finance/
│   │   ├── Accounts Payable/
│   │   │   ├── Invoices/
│   │   │   │   ├── 2024/
│   │   │   │   │   ├── Paid/
│   │   │   │   │   │   ├── Vendor_ABC/
│   │   │   │   │   │   │   ├── January/    ← 8 levels!
```

### The Hybrid Approach (Recommended)

**Best Practice: Folders for WHAT, Metadata for EVERYTHING ELSE**

```
Document Library: Finance Documents

Folders (1-2 levels max):
├── Invoices/
├── Contracts/
├── Reports/
└── Policies/

Metadata columns:
- Year (choice): 2023, 2024, 2025
- Vendor (lookup): ABC Corp, XYZ Inc, ...
- Status (choice): Draft, Pending, Approved, Paid
- Project (lookup): Alpha, Beta, Gamma
- Department (choice): Finance, HR, Operations

Views:
- All Documents
- By Year (grouped)
- Pending Approval
- By Vendor
- My Documents
```

**Result:**
- Simple navigation (4 top-level folders)
- Rich filtering (5 metadata columns)
- Multiple perspectives (5+ views)
- No deep drilling required

---

## 3. Metadata-Driven Document Management

### What is Metadata?

Metadata = "Data about data" = Properties/attributes of a document

**Built-in metadata (automatic):**
- Created date
- Modified date
- Created by
- Modified by
- File size
- File type

**Custom metadata (you define):**
- Document type
- Department
- Project
- Status
- Vendor
- Expiration date
- Classification
- etc.

### Types of Metadata Columns

| Column Type | Use For | Example |
|-------------|---------|---------|
| Single line of text | Free-form short text | Reference number |
| Multiple lines | Long descriptions | Notes, comments |
| Choice | Predefined options | Status: Draft/Final |
| Number | Numeric values | Invoice amount |
| Currency | Money values | Contract value |
| Date | Dates | Due date, expiry |
| Yes/No | Boolean flags | Approved: Yes/No |
| Lookup | Pull from another list | Vendor (from Vendors list) |
| Person | User selection | Document owner |
| Managed Metadata | Enterprise taxonomy | Department hierarchy |
| Calculated | Auto-computed | Days until expiry |

### Metadata Design Principles

#### Principle 1: Start Simple
```
Start with:        NOT:
- Document Type    - Document Type
- Department       - Department
- Year             - Year
- Status           - Quarter
                   - Month
                   - Sub-department
                   - Cost Center
                   - Region
                   - Sub-region
                   - Project Code
                   - Sub-project
                   - ... (15 more fields)
```

**Rule:** 5-7 metadata columns maximum per library

#### Principle 2: Required Fields = Minimal
```
Required: Only fields ABSOLUTELY needed
- Document Type ✓ (critical for organization)
- Department ✓ (critical for permissions/filtering)

Optional: Everything else
- Project (nice to have)
- Keywords (nice to have)
- Vendor (context-dependent)
```

**Why?** Too many required fields = users hate the system

#### Principle 3: Use Choice Fields Over Text
```
Bad:  Department [________________] (free text)
      Results: "Finance", "finance", "FINANCE", "Fin", "Fin.", "Financ"

Good: Department [▼ Select...    ]
      - Finance
      - HR
      - Operations
      - Marketing
```

#### Principle 4: Consistent Taxonomy
Define standard values across the organization:

```
Document Types (organization-wide):
├── Contract
├── Invoice
├── Report
├── Policy
├── Procedure
├── Memo
├── Presentation
├── Spreadsheet
└── Drawing

NOT department-specific variations:
├── Finance: "Invoice", "Bill", "Payment Request"
├── HR: "Invoice", "Vendor Invoice", "Supplier Bill"
└── Ops: "Invoice", "PO Invoice", "Purchase Invoice"
```

### Creating Effective Views

Views = Saved filters and sorts that users can switch between

**Default views to create:**

| View Name | Configuration | Purpose |
|-----------|---------------|---------|
| All Documents | No filter, sorted by modified date | Default view |
| My Documents | Filter: Created By = [Me] | Personal files |
| Recent | Modified in last 30 days | Active work |
| By Type | Grouped by Document Type | Category browse |
| By Year | Grouped by Year column | Historical |
| Pending Review | Filter: Status = Pending | Workflow |
| Expiring Soon | Filter: Expiry Date < Today+30 | Compliance |

**View example - "Contracts by Vendor":**
```
Columns shown: Name, Vendor, Contract Value, Expiry Date, Status
Grouped by: Vendor
Sorted by: Expiry Date (ascending)
Filter: Document Type = Contract
```

### Metadata Best Practices Summary

| Do | Don't |
|----|-------|
| Use choice columns | Use free text for categories |
| Start with 5-7 columns | Start with 15+ columns |
| Make most fields optional | Make everything required |
| Create multiple views | Expect users to filter manually |
| Use consistent values | Let each department define their own |
| Train users on metadata | Assume users understand |
| Review and refine | Set and forget |

---

## 4. Recommended Document Library Structure

### Option A: Single Library with Metadata (Best for < 50,000 docs)

```
Site: Finance
└── Document Library: Finance Documents
    ├── Metadata columns:
    │   - Document Type (Contract, Invoice, Report, Policy)
    │   - Year
    │   - Vendor
    │   - Status
    │   - Project
    └── Views:
        - All Documents
        - Contracts
        - Invoices
        - By Year
        - Pending Approval
```

**Pros:** Simple, unified search, easy management
**Cons:** Can get slow with very large file counts

### Option B: Multiple Libraries by Document Type (Best for > 50,000 docs)

```
Site: Finance
├── Document Library: Contracts
│   ├── Metadata: Vendor, Value, Start Date, End Date, Status
│   └── Views: Active, Expiring, By Vendor
├── Document Library: Invoices
│   ├── Metadata: Vendor, Amount, Invoice Date, Due Date, Status
│   └── Views: Pending, Paid, By Vendor, By Month
├── Document Library: Reports
│   ├── Metadata: Report Type, Period, Author
│   └── Views: By Type, By Period
└── Document Library: Policies
    ├── Metadata: Policy Area, Version, Effective Date, Owner
    └── Views: Current, Archived, By Area
```

**Pros:** Better performance, specific metadata per type, clearer navigation
**Cons:** Multiple places to search, more libraries to manage

### Option C: Hybrid (Recommended for Most Organizations)

```
Site: Finance
├── Document Library: Active Documents
│   ├── Folders (max 2 levels):
│   │   ├── Contracts/
│   │   ├── Invoices/
│   │   └── Reports/
│   ├── Metadata: Document Type, Year, Vendor, Status, Project
│   └── Views: Multiple views per document type
├── Document Library: Archive
│   └── Older documents moved here after X years
├── Document Library: Scanned Documents
│   └── Documents from hardcopy digitization
└── Document Library: Templates
    └── Standard templates for the department
```

### Library Limits to Consider

| Item | Limit | Recommendation |
|------|-------|----------------|
| Items per library | 30 million | Keep under 100,000 for performance |
| Items per view | 5,000 (threshold) | Use indexed columns for filtering |
| Indexed columns | 20 per library | Index columns used in filters |
| File size | 250 GB | No action needed usually |
| Path length | 400 characters | Avoid deep folders + long names |
| Sync (OneDrive) | 300,000 files | Split large libraries |

---

## 5. Naming Conventions

### File Naming Best Practices

**General rules:**
- Be descriptive but concise
- Use consistent format
- Avoid special characters
- Include key identifiers
- Don't rely on names alone (use metadata)

**Avoid these characters:**
```
# % & * { } \ : < > ? / + | " '
```

**Recommended format:**
```
[Type]_[Identifier]_[Description]_[Date].[ext]

Examples:
CONTRACT_ABC-Corp_Service-Agreement_2024-01.pdf
INVOICE_INV-2024-00123_ABC-Corp.pdf
REPORT_Monthly-Sales_2024-03.xlsx
POLICY_Travel-Expense_v2.1.docx
```

### What NOT to Do

```
Bad naming examples:

Document1.docx              ← No description
Final_Final_FINAL_v3.docx   ← Version chaos
John's file (1).xlsx        ← Special chars, copy indicator
Meeting notes.docx          ← Too generic
Contract.pdf                ← No identifier
asdfjkl.pdf                 ← Meaningless
```

### Naming Convention by Document Type

| Document Type | Format | Example |
|---------------|--------|---------|
| Contract | CONTRACT_[Vendor]_[Type]_[Date] | CONTRACT_ABC_Service_2024-01 |
| Invoice | INV_[Number]_[Vendor] | INV_2024-00123_ABC |
| Report | RPT_[Type]_[Period] | RPT_Sales_2024-Q1 |
| Policy | POL_[Area]_[Name]_v[Version] | POL_HR_Leave_v2.0 |
| Meeting | MTG_[Group]_[Date] | MTG_Finance-Team_2024-03-15 |
| Proposal | PROP_[Client]_[Project] | PROP_XYZ_Website-Redesign |

### When to Use Dates in Filenames

**Use dates when:**
- Document is version-specific (monthly reports)
- Date is key identifier (meeting notes)
- Multiple similar documents exist

**Don't use dates when:**
- Using version history instead
- Date is captured in metadata
- Only one version will ever exist

**Date format (always):**
```
YYYY-MM-DD or YYYY-MM

Good: 2024-03-15, 2024-03
Bad:  03-15-24, March 15, 15/03/2024
```

---

## 6. Version Control

### SharePoint Version History

SharePoint automatically tracks versions - no need for:
```
Contract_v1.docx
Contract_v2.docx
Contract_v2_final.docx
Contract_v2_final_FINAL.docx     ← Never again!
```

### Version Settings

| Setting | Recommendation | Why |
|---------|----------------|-----|
| Versioning | Enabled | Track all changes |
| Major versions | Yes | For published documents |
| Minor versions | Optional | For draft workflows |
| Version limit | 50-100 | Balance history vs storage |
| Require checkout | No (usually) | Causes confusion |

### How Version History Works

```
Contract.docx
├── Version 3.0 (current) - Modified by Sarah, 2024-03-15
├── Version 2.0 - Modified by John, 2024-03-10
├── Version 1.0 - Created by Mike, 2024-03-01
```

**Users can:**
- View any previous version
- Restore previous version
- Compare versions
- See who changed what and when

### When to Use Major vs Minor Versions

```
Major versions (1.0, 2.0, 3.0):
- Published, approved documents
- Available to all users with read access

Minor versions (1.1, 1.2, 1.3):
- Drafts in progress
- Only visible to editors
- Becomes major when "Published"

Workflow:
1.1 (draft) → 1.2 (draft) → 1.3 (draft) → 2.0 (published)
```

---

## 7. Search Optimization

### How SharePoint Search Works

```
User searches "Project Alpha Contract"

SharePoint searches:
├── File name
├── File content (full text)
├── Metadata values
├── Folder names
└── Previous versions (optional)
```

### Making Documents Findable

**1. Good file names**
```
Good: CONTRACT_Alpha-Project_Service-Agreement.pdf
Bad:  Document1.pdf
```

**2. Rich metadata**
```
Good: Project=Alpha, Type=Contract, Vendor=ABC, Year=2024
Bad:  No metadata
```

**3. Document content**
```
Good: Searchable text (native Office docs, OCR'd PDFs)
Bad:  Scanned image PDFs without OCR
```

### Search Tips for Users

| To Find | Search Syntax |
|---------|---------------|
| Exact phrase | "project alpha contract" |
| File type | filetype:pdf |
| Author | author:"John Smith" |
| Modified date | modified>2024-01-01 |
| In specific site | site:finance |
| File name only | filename:contract |

### Managed Properties (Advanced)

Map metadata to search properties for better filtering:

```
Metadata column: Document Type
↓
Managed property: RefinableString00
↓
Search refiners: Filter by Document Type in search results
```

---

## 8. Permission Management

### Permission Best Practices

**Principle: Simple, Group-Based, Inherited**

```
Good permission model:
Site: Finance
├── Owners: Finance-Admins (3 people)
├── Members: Finance-Team (50 people)
├── Visitors: All-Employees (read-only)
└── All libraries inherit from site

Bad permission model:
Library: Documents
├── Folder1: John, Sarah, Mike (edit)
├── Folder2: Sarah, Lisa (edit), John (read)
├── Folder3: Finance-Team minus John
├── File1.docx: Only CEO
└── ... (unique permissions everywhere)
```

### Permission Levels

| Level | Can Do | Use For |
|-------|--------|---------|
| Full Control | Everything | Site admins only |
| Design | Create lists, pages | Power users |
| Edit | Add, edit, delete items | Regular contributors |
| Contribute | Add, edit own items | Limited contributors |
| Read | View only | General audience |

### When to Break Inheritance

**Do break inheritance for:**
- Confidential document libraries
- HR/Personnel files
- Executive materials
- External-shared content

**Don't break inheritance for:**
- Individual files (hard to manage)
- Temporary needs (use separate library)
- Every folder (creates chaos)

### Permission Anti-Patterns

| Pattern | Problem | Solution |
|---------|---------|----------|
| Individual permissions | Unmanageable | Use groups |
| Permission per file | Audit nightmare | Use libraries |
| Deep folder permissions | Confusion | Flatten + groups |
| Everyone has Full Control | Security risk | Least privilege |
| No one owns permissions | Drift over time | Assign ownership |

---

## 9. Compliance & Governance

### Document Lifecycle

```
┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
│ Create  │───▶│ Active  │───▶│ Review  │───▶│ Archive │───▶│ Dispose │
│         │    │   Use   │    │         │    │         │    │         │
└─────────┘    └─────────┘    └─────────┘    └─────────┘    └─────────┘
                                   │
                              Retain if
                              still needed
```

### Retention Policies

**Configure in Microsoft Purview (Compliance Center)**

| Document Type | Retain For | After Retention |
|---------------|------------|-----------------|
| Financial Records | 7 years | Delete |
| Contracts | Contract end + 10 years | Review |
| HR Records | Employment end + 7 years | Delete |
| Correspondence | 3 years | Delete |
| Policies | Superseded + 3 years | Delete |
| Technical Drawings | Permanent | N/A |

### Sensitivity Labels

**Classification levels:**
```
┌────────────────┐
│   Restricted   │  ← Highest: Board materials, M&A
├────────────────┤
│  Confidential  │  ← High: Financial data, HR records
├────────────────┤
│    Internal    │  ← Medium: Internal communications
├────────────────┤
│     Public     │  ← Low: Marketing materials
└────────────────┘
```

**What labels can do:**
- Add watermarks
- Encrypt content
- Restrict sharing
- Block printing
- Auto-expire access

### Audit Requirements

**Enable unified audit logging:**
- Who accessed what documents
- Who modified what
- Who shared what externally
- Who deleted what

**Retention of audit logs:** 90 days (standard) or 1 year (E5)

---

## 10. Common Mistakes to Avoid

### Mistake 1: Replicating File Server Structure
```
Bad: Copy exact folder structure from file server
     \\Server\Dept\Year\Month\Type\Subtype\Project\file.docx
     ↓
     SharePoint/Dept/Year/Month/Type/Subtype/Project/file.docx

Good: Redesign for SharePoint
     SharePoint/DeptDocuments/file.docx
     + Metadata: Year, Month, Type, Project
```

### Mistake 2: Too Many Sites/Libraries
```
Bad:
- 50 SharePoint sites for 100-person company
- Separate library for every project
- Users don't know where to look

Good:
- Site per department (5-10 sites)
- Libraries by document type
- Clear governance
```

### Mistake 3: No Governance
```
Bad:
- Anyone can create sites
- No naming standards
- No ownership assigned
- No cleanup process

Good:
- Site creation approval process
- Documented standards
- Clear ownership
- Regular reviews
```

### Mistake 4: Ignoring User Training
```
Bad:
- Deploy SharePoint
- Send email: "Your files are now in SharePoint"
- Wonder why adoption is low

Good:
- Training sessions
- Quick reference guides
- Champions in each department
- Ongoing support
```

### Mistake 5: Over-Engineering Metadata
```
Bad:
- 20 metadata columns
- 10 required fields
- Complex calculated fields
- Users avoid adding documents

Good:
- 5-7 columns
- 2-3 required
- Simple choices
- Users actually use it
```

### Mistake 6: Forgetting Mobile Users
```
Bad:
- 7-level folder structure
- Files with 100-character names
- No mobile-friendly views

Good:
- Flat/shallow structure
- Concise names
- Views optimized for mobile
```

### Mistake 7: No Search Strategy
```
Bad:
- Rely only on navigation
- No metadata
- Non-searchable PDFs

Good:
- Rich metadata
- OCR all scanned documents
- Train users on search
```

---

## 11. Migration Strategy: Folders to Metadata

### Approach: Convert Folder Path to Metadata

**Source file server:**
```
\\Server\Finance\Invoices\2024\Vendor_ABC\Paid\INV-001.pdf
         ↓        ↓       ↓      ↓        ↓
       Dept     Type    Year  Vendor   Status
```

**Target SharePoint:**
```
File: INV-001.pdf
Location: Finance Site / Invoices Library
Metadata:
  - Department: Finance (from site)
  - Document Type: Invoice (from library)
  - Year: 2024 (extracted from path)
  - Vendor: ABC (extracted from path)
  - Status: Paid (extracted from path)
```

### Path-to-Metadata Mapping Table

Create mapping for your migration:

| Path Segment | Maps To | Column Type |
|--------------|---------|-------------|
| Department name | Site | N/A (structural) |
| Document type | Library or metadata | Choice |
| Year | Year column | Choice |
| Vendor name | Vendor column | Lookup |
| Status folder | Status column | Choice |
| Project name | Project column | Lookup or Choice |

### Migration Script Logic

```python
# Pseudocode for path-to-metadata extraction

source_path = "\\Server\Finance\Invoices\2024\Vendor_ABC\Paid\INV-001.pdf"

# Parse path segments
segments = source_path.split("\\")
# ['Server', 'Finance', 'Invoices', '2024', 'Vendor_ABC', 'Paid', 'INV-001.pdf']

# Map to metadata based on position and patterns
metadata = {
    "Department": segments[1],           # Finance
    "DocumentType": segments[2],         # Invoices
    "Year": extract_year(segments),      # 2024
    "Vendor": extract_vendor(segments),  # ABC
    "Status": extract_status(segments),  # Paid
}

# Upload to SharePoint with metadata
upload_to_sharepoint(file, target_library, metadata)
```

### Handling Inconsistent Folder Structures

**Problem:** Different departments use different structures

```
Finance: \Finance\Invoices\2024\Vendor\file.pdf
HR:      \HR\2024\Documents\Personnel\file.pdf
Ops:     \Operations\Projects\Alpha\Documents\file.pdf
```

**Solution:** Department-specific mapping rules

```json
{
  "Finance": {
    "pattern": "{dept}/{type}/{year}/{vendor}/{file}",
    "mappings": {"2": "DocumentType", "3": "Year", "4": "Vendor"}
  },
  "HR": {
    "pattern": "{dept}/{year}/{type}/{subtype}/{file}",
    "mappings": {"2": "Year", "3": "DocumentType"}
  }
}
```

---

## 12. Quick Reference Cheat Sheet

### Folder Guidelines

| Guideline | Rule |
|-----------|------|
| Maximum depth | 2 levels |
| Folder purpose | Major categories only |
| When to use | Project groupings, document types |
| When NOT to use | Year/month, status, vendor |

### Metadata Guidelines

| Guideline | Rule |
|-----------|------|
| Maximum columns | 5-7 per library |
| Required fields | 2-3 maximum |
| Column types | Prefer Choice over Text |
| Consistency | Use organization-wide taxonomy |

### Naming Guidelines

| Element | Rule |
|---------|------|
| Format | TYPE_Identifier_Description_Date |
| Characters | Avoid # % & * : < > ? / \ |
| Length | Under 50 characters (name only) |
| Dates | YYYY-MM-DD format |

### Permission Guidelines

| Principle | Implementation |
|-----------|----------------|
| Use groups | Never individual permissions |
| Inherit | Break inheritance sparingly |
| Least privilege | Start with Read, add as needed |
| Audit | Review quarterly |

### Search Guidelines

| Element | Optimize By |
|---------|-------------|
| File names | Descriptive, include keywords |
| Metadata | Fill out all relevant fields |
| Content | Use searchable formats, OCR |
| Views | Create for common filters |

---

## Summary: The Golden Rules

### 1. Think Metadata, Not Folders
Replace deep folder structures with rich metadata columns

### 2. Keep It Simple
Start with 5-7 metadata columns, expand only if needed

### 3. Design for Search
Users will search, not browse - make content findable

### 4. Use Groups for Permissions
Never assign permissions to individuals

### 5. Plan for Growth
Design structure that scales with your organization

### 6. Train Your Users
Technology is only as good as user adoption

### 7. Govern Continuously
Regular reviews, cleanup, and improvement

---

## Appendix: Folder to Metadata Decision Matrix

**Should this be a folder or metadata?**

| Attribute | Folder | Metadata | Reasoning |
|-----------|--------|----------|-----------|
| Year | Maybe | Yes | Multiple years = multiple views |
| Month | No | Yes | 12 folders vs 1 dropdown |
| Document Type | Yes | Yes | Can be either, major category |
| Project | Yes | Yes | Logical grouping, temporary |
| Vendor/Client | No | Yes | Too many = too many folders |
| Status | No | Yes | Changes over time |
| Author | No | Yes | Auto-populated |
| Department | Site | Maybe | Site-level separation |
| Region | No | Yes | Cross-cutting attribute |
| Confidentiality | No | Yes | Use sensitivity labels |

---

*Document Version: 1.0*
*Created: 2026-01-28*
*Review Date: Quarterly*
