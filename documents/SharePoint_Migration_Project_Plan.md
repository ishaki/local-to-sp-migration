# SharePoint Online Migration Project Plan
## Taiyo Document Migration - Hardcopy & File Server to SharePoint Online

**Version:** 1.0
**Created:** 2026-01-28
**Timeline:** 3-6 Months (Phased by Department)

---

## Executive Summary

This plan covers the migration of documents from two sources:
1. **Hardcopy Documents** → Digitized by 3rd party vendor → SharePoint Online
2. **Local File Server** → Script-based migration (Python/PowerShell) → SharePoint Online

Migration will be executed in phases by department: Production, HR, Finance, Marketing, etc.

---

## Table of Contents

1. [Phase 1: Discovery & Planning](#phase-1-discovery--planning)
2. [Phase 2: Infrastructure Setup](#phase-2-infrastructure-setup)
3. [Phase 3: Development & Testing](#phase-3-development--testing)
4. [Phase 4: Pilot Migration](#phase-4-pilot-migration)
5. [Phase 5: Production Migration](#phase-5-production-migration)
6. [Phase 6: Validation & Finalization](#phase-6-validation--finalization)
7. [Technical Architecture](#technical-architecture)
8. [Risk Management](#risk-management)
9. [Department Migration Schedule](#department-migration-schedule)

---

## Phase 1: Discovery & Planning
**Duration:** 2-3 Weeks

### 1.1 File Server Analysis

| Task | Description | Deliverable |
|------|-------------|-------------|
| Inventory Scan | Run discovery script to catalog all files | `file_inventory_report.csv` |
| Size Analysis | Calculate total size per department/folder | Size breakdown report |
| File Type Analysis | Identify all file extensions and formats | File type matrix |
| Duplicate Detection | Identify duplicate files for cleanup | Duplicate report |
| Permission Mapping | Document existing NTFS permissions | Permission mapping document |
| Path Length Check | Identify paths exceeding 400 characters | Path issues report |
| Special Files | Identify CAD, large media, legacy formats | Special handling list |

**Discovery Script Requirements:**
```
- Total file count and sizes per folder
- File type distribution
- Files > 250MB (SharePoint single file limit warning)
- Files > 15GB (cannot be uploaded)
- Path lengths exceeding limits
- Last modified dates (for retention decisions)
- Files with special characters in names
```

### 1.2 Hardcopy Document Planning

| Task | Description | Deliverable |
|------|-------------|-------------|
| Vendor Coordination | Align on output format and metadata schema | Vendor specification document |
| Metadata Template | Define metadata fields vendor must provide | Metadata template (Excel/CSV) |
| Naming Convention | Establish file naming standards | Naming convention guide |
| Quality Standards | Define scan quality requirements (DPI, format) | Quality specification |
| Delivery Schedule | Coordinate batch delivery schedule | Delivery calendar |

**Required Metadata from 3rd Party Vendor:**
```
- Document ID (unique identifier)
- Document Title
- Document Type/Category
- Department
- Original Date (if visible on document)
- Scan Date
- Keywords/Tags
- Retention Category
- Classification Level (Public/Internal/Confidential/Restricted)
- Box/Batch Reference (for audit trail)
```

### 1.3 SharePoint Structure Design

| Site | URL Pattern | Purpose |
|------|-------------|---------|
| Production | `/sites/Production` | Production department documents |
| HR | `/sites/HR` | Human Resources documents |
| Finance | `/sites/Finance` | Financial documents |
| Marketing | `/sites/Marketing` | Marketing materials |
| [Additional] | `/sites/[DeptName]` | Other departments as needed |

**Document Library Structure per Site:**
```
Site: [Department]
├── Document Library: Active Documents
│   ├── Folder structure migrated from file server
│   └── Metadata columns applied
├── Document Library: Archived Documents
│   └── Historical/legacy documents
├── Document Library: Scanned Documents
│   └── Documents from hardcopy digitization
└── Document Library: Templates
    └── Department templates
```

### 1.4 Metadata Schema Definition

**Core Metadata Columns:**

| Column Name | Type | Required | Description |
|-------------|------|----------|-------------|
| DocumentID | Text | Yes | Unique identifier |
| DocumentType | Choice | Yes | Contract, Report, Drawing, Correspondence, etc. |
| Department | Choice | Yes | Source department |
| Classification | Choice | Yes | Public, Internal, Confidential, Restricted |
| RetentionCategory | Choice | Yes | Links to retention policy |
| OriginalPath | Text | No | Original file server path (audit trail) |
| MigrationDate | DateTime | Auto | When document was migrated |
| MigrationBatch | Text | Auto | Batch identifier for tracking |
| SourceType | Choice | Auto | FileServer, Hardcopy |
| Author | Person | No | Document author if known |
| Keywords | Multi-text | No | Searchable keywords |
| ExpirationDate | DateTime | No | Auto-calculated from retention |

### 1.5 Compliance & Retention Planning

| Retention Category | Retention Period | Action After | Applies To |
|-------------------|------------------|--------------|------------|
| Financial Records | 7 years | Archive then Delete | Finance |
| HR Personnel Files | Employment + 7 years | Archive | HR |
| Contracts | Contract End + 10 years | Legal Review | All |
| Technical Drawings | Permanent | None | Production |
| General Correspondence | 3 years | Delete | All |
| Legal/Compliance | Permanent | None | All |

**Compliance Requirements:**
- [ ] Audit logging enabled for all document libraries
- [ ] Legal hold capability configured
- [ ] Sensitivity labels configured (Microsoft Purview)
- [ ] DLP policies for confidential content
- [ ] Version history enabled (major versions)

---

## Phase 2: Infrastructure Setup
**Duration:** 2 Weeks

### 2.1 Azure AD App Registration

| Configuration | Value |
|--------------|-------|
| App Name | `Taiyo-SP-Migration` |
| Authentication | Client ID + Client Secret |
| Secret Expiry | Set appropriate expiry (recommend: 6 months minimum) |

**Required API Permissions:**

| API | Permission | Type |
|-----|------------|------|
| Microsoft Graph | Sites.ReadWrite.All | Application |
| Microsoft Graph | Files.ReadWrite.All | Application |
| SharePoint | Sites.FullControl.All | Application |

**Setup Checklist:**
- [ ] Register application in Azure AD
- [ ] Generate client secret (store securely in Key Vault)
- [ ] Grant admin consent for permissions
- [ ] Test authentication
- [ ] Document App ID and Tenant ID

### 2.2 SharePoint Sites Creation

**Per Department Site Setup:**
- [ ] Create SharePoint site (Team Site or Communication Site)
- [ ] Configure site permissions (Owners, Members, Visitors)
- [ ] Create document libraries per structure design
- [ ] Add custom metadata columns to libraries
- [ ] Configure retention labels
- [ ] Enable versioning settings
- [ ] Configure audit logging
- [ ] Set storage quotas if needed

### 2.3 Development Environment Setup

```
Required Tools:
├── Python 3.10+ OR PowerShell 7+
├── VS Code or preferred IDE
├── Git for version control
├── Microsoft Graph SDK / PnP PowerShell
└── Testing SharePoint site (non-production)
```

**Python Libraries:**
```
- msal (Microsoft Authentication Library)
- office365-rest-python-client OR
- msgraph-sdk
- pandas (for data processing)
- openpyxl (Excel handling)
- python-magic (file type detection)
- tqdm (progress bars)
```

**PowerShell Modules:**
```
- PnP.PowerShell
- Microsoft.Graph
- ImportExcel
```

---

## Phase 3: Development & Testing
**Duration:** 3-4 Weeks

### 3.1 Migration Scripts Development

**Script 1: File Server Scanner** (`scan_files.py` / `Scan-Files.ps1`)
```
Purpose: Inventory file server and generate migration manifest

Features:
- Recursive folder scanning
- File metadata extraction (size, dates, type)
- Path validation (length, special characters)
- Duplicate detection (hash-based)
- Large file flagging
- Export to CSV/Excel manifest
- Error logging
```

**Script 2: Metadata Processor** (`process_metadata.py` / `Process-Metadata.ps1`)
```
Purpose: Process and validate metadata from manifest and vendor files

Features:
- Read vendor metadata CSV
- Map to SharePoint columns
- Validate required fields
- Auto-classify based on rules
- Generate upload manifest
- Flag issues for review
```

**Script 3: Migration Uploader** (`upload_files.py` / `Upload-Files.ps1`)
```
Purpose: Upload files to SharePoint with metadata

Features:
- Batch processing with resume capability
- Chunked upload for large files (>4MB)
- Metadata application
- Folder structure creation
- Progress tracking
- Error handling and retry logic
- Detailed logging
- Checksum verification (optional)
```

**Script 4: Validation Script** (`validate_migration.py` / `Validate-Migration.ps1`)
```
Purpose: Post-migration validation

Features:
- File count comparison (source vs destination)
- File size verification
- Metadata completeness check
- Random sample download and compare
- Generate validation report
```

### 3.2 Script Architecture

```
project/
├── config/
│   ├── settings.json          # Configuration (sites, libraries, paths)
│   ├── metadata_mapping.json  # Field mapping rules
│   └── classification_rules.json  # Auto-classification rules
├── scripts/
│   ├── scan_files.py
│   ├── process_metadata.py
│   ├── upload_files.py
│   └── validate_migration.py
├── logs/
│   ├── scan_[timestamp].log
│   ├── upload_[timestamp].log
│   └── errors_[timestamp].log
├── manifests/
│   ├── file_inventory.csv
│   ├── upload_manifest.csv
│   └── validation_report.csv
├── vendor_input/
│   └── [vendor metadata files]
└── README.md
```

### 3.3 Testing Plan

| Test Type | Description | Environment |
|-----------|-------------|-------------|
| Unit Testing | Test individual functions | Local |
| Integration Testing | Test full workflow with small dataset | Test SP Site |
| Performance Testing | Test with 1000+ files | Test SP Site |
| Large File Testing | Test files >100MB, >250MB | Test SP Site |
| Error Recovery | Test resume after failure | Test SP Site |
| Metadata Validation | Verify all columns populated | Test SP Site |

**Test Dataset Requirements:**
- Minimum 1000 files
- Include files >100MB
- Include various file types (Office, PDF, CAD, images)
- Include deep folder paths
- Include files with special characters
- Include duplicate files

---

## Phase 4: Pilot Migration
**Duration:** 2 Weeks

### 4.1 Pilot Department Selection

**Recommended Pilot:** Marketing or smaller department
- Moderate data volume
- Variety of file types
- Engaged stakeholders
- Lower risk if issues occur

### 4.2 Pilot Execution Steps

| Step | Task | Checkpoint |
|------|------|------------|
| 1 | Run scanner on pilot department folder | Manifest generated |
| 2 | Review manifest with department | Exclusions identified |
| 3 | Process metadata | Upload manifest ready |
| 4 | Execute migration (batch 1 - 10%) | Verify success |
| 5 | User acceptance testing | Feedback collected |
| 6 | Execute remaining batches | Full migration complete |
| 7 | Run validation script | Report generated |
| 8 | Sign-off from department | Approval documented |

### 4.3 Pilot Success Criteria

- [ ] 100% files uploaded (minus exclusions)
- [ ] All metadata columns populated correctly
- [ ] Folder structure preserved as designed
- [ ] Files accessible and openable
- [ ] Search working on migrated content
- [ ] Permissions correct
- [ ] No data loss or corruption
- [ ] Performance acceptable (<X hours for X GB)
- [ ] User acceptance received

### 4.4 Pilot Lessons Learned

Document and address:
- Script issues encountered
- Performance bottlenecks
- Metadata mapping problems
- User feedback
- Process improvements needed

---

## Phase 5: Production Migration
**Duration:** 6-10 Weeks (varies by department size)

### 5.1 Migration Waves

| Wave | Department | Est. Size | Duration | Target Date |
|------|------------|-----------|----------|-------------|
| 1 | Marketing (Pilot) | 50 GB | 1 week | Week 6-7 |
| 2 | HR | 100 GB | 1.5 weeks | Week 8-9 |
| 3 | Finance | 200 GB | 2 weeks | Week 10-12 |
| 4 | Production | 500 GB+ | 3 weeks | Week 13-16 |
| 5 | Hardcopy Documents | Ongoing | Parallel | Throughout |

### 5.2 Pre-Migration Checklist (Per Department)

- [ ] Department stakeholder briefing completed
- [ ] Source folder path confirmed
- [ ] Destination site/library confirmed
- [ ] Scanner run and manifest reviewed
- [ ] Exclusions documented
- [ ] Metadata mapping validated
- [ ] Cut-over plan communicated (if needed)
- [ ] Rollback plan documented
- [ ] Support contacts identified

### 5.3 Migration Execution Process

```
Day -7: Communication to department users
Day -3: Final scan and manifest generation
Day -1: Disable write access to source (optional, for cut-over)
Day 0:  Execute migration script
        Monitor progress and logs
        Address errors in real-time
Day +1: Run validation script
        Generate completion report
Day +2: User acceptance testing
        Address immediate issues
Day +3: Sign-off and move to next department
```

### 5.4 Hardcopy Document Migration

**Parallel Track with Vendor:**

| Step | Description | Responsibility |
|------|-------------|----------------|
| 1 | Vendor receives physical documents | Vendor |
| 2 | Scanning and OCR | Vendor |
| 3 | Metadata entry per template | Vendor |
| 4 | Batch delivery (files + metadata CSV) | Vendor |
| 5 | Quality check (random sample) | Internal Team |
| 6 | Process metadata through script | Internal Team |
| 7 | Upload to SharePoint (Scanned Documents library) | Internal Team |
| 8 | Validation | Internal Team |
| 9 | Confirmation to vendor | Internal Team |

### 5.5 Error Handling Procedures

| Error Type | Action |
|------------|--------|
| File too large (>15GB) | Log, skip, manual handling |
| Path too long | Rename or restructure |
| Special characters | Auto-rename with mapping log |
| Upload timeout | Auto-retry (3 attempts) |
| Auth failure | Refresh token, alert team |
| Metadata invalid | Log, upload file, flag for review |
| Checksum mismatch | Re-upload, if persists flag |

---

## Phase 6: Validation & Finalization
**Duration:** 2 Weeks

### 6.1 Validation Checklist

**Quantitative Validation:**
- [ ] File count matches (source vs destination)
- [ ] Total size within expected range
- [ ] All folders created
- [ ] All metadata fields populated
- [ ] No orphaned files

**Qualitative Validation:**
- [ ] Random sample files open correctly
- [ ] Search returns expected results
- [ ] Permissions working as expected
- [ ] Large files (CAD, media) accessible
- [ ] Version history intact (if applicable)

### 6.2 Final Reports

| Report | Purpose | Audience |
|--------|---------|----------|
| Migration Summary | Overall statistics | Management |
| Validation Report | Technical verification | IT Team |
| Exception Report | Files requiring attention | IT Team |
| Audit Trail | Compliance evidence | Compliance |
| Lessons Learned | Process improvement | Project Team |

### 6.3 Post-Migration Tasks

- [ ] Archive migration logs
- [ ] Document final folder/site structure
- [ ] Update IT documentation
- [ ] User training on SharePoint access
- [ ] Configure ongoing backup/DR
- [ ] Plan source data decommission (after retention period)
- [ ] Close project with stakeholder sign-off

### 6.4 Source Data Handling

**Recommended Approach:**
1. Keep source read-only for 30-60 days post-migration
2. After validation sign-off, archive source to cold storage
3. Set deletion date per retention policy
4. Document decommission in change management

---

## Technical Architecture

### Authentication Flow

```
┌──────────────────┐      ┌───────────────────┐      ┌─────────────────┐
│  Migration       │      │   Azure AD        │      │  SharePoint     │
│  Script          │──────│   (OAuth 2.0)     │──────│  Online         │
│                  │      │                   │      │                 │
│  - Client ID     │      │  - Token Issue    │      │  - Graph API    │
│  - Client Secret │      │  - Validation     │      │  - REST API     │
└──────────────────┘      └───────────────────┘      └─────────────────┘
```

### Upload Flow (Large Files)

```
┌─────────────┐     ┌──────────────┐     ┌────────────────┐     ┌─────────────┐
│  Read File  │────▶│  Create      │────▶│  Upload Chunks │────▶│  Apply      │
│  from Disk  │     │  Upload      │     │  (4MB each)    │     │  Metadata   │
│             │     │  Session     │     │                │     │             │
└─────────────┘     └──────────────┘     └────────────────┘     └─────────────┘
                                                │
                                                ▼
                                         ┌────────────────┐
                                         │  Log Success   │
                                         │  Update        │
                                         │  Manifest      │
                                         └────────────────┘
```

### Data Flow Overview

```
┌─────────────────────────────────────────────────────────────────────────┐
│                           SOURCE DATA                                    │
├─────────────────────────────────┬───────────────────────────────────────┤
│      File Server                │         Hardcopy Documents             │
│      (500GB - 2TB)              │         (3rd Party Vendor)             │
└───────────────┬─────────────────┴───────────────────┬───────────────────┘
                │                                     │
                ▼                                     ▼
┌───────────────────────────────┐   ┌─────────────────────────────────────┐
│  Scanner Script               │   │  Vendor Delivery                    │
│  - Inventory                  │   │  - Scanned PDFs                     │
│  - Metadata Extract           │   │  - Metadata CSV                     │
└───────────────┬───────────────┘   └───────────────────┬─────────────────┘
                │                                       │
                ▼                                       ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      Metadata Processor Script                           │
│  - Validate & Map Metadata                                              │
│  - Generate Upload Manifest                                             │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      Uploader Script                                     │
│  - Batch Upload with Resume                                             │
│  - Apply Metadata                                                       │
│  - Log Everything                                                       │
└───────────────────────────────────┬─────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      SharePoint Online                                   │
├─────────────────┬─────────────────┬─────────────────┬───────────────────┤
│  /sites/HR      │ /sites/Finance  │ /sites/Prod     │  /sites/Marketing │
└─────────────────┴─────────────────┴─────────────────┴───────────────────┘
```

---

## Risk Management

### Risk Register

| # | Risk | Probability | Impact | Mitigation |
|---|------|-------------|--------|------------|
| 1 | Large files fail to upload | Medium | Medium | Chunked upload, retry logic, manual fallback |
| 2 | API throttling by Microsoft | High | Medium | Rate limiting, exponential backoff, batch scheduling |
| 3 | Metadata mapping errors | Medium | High | Thorough testing, validation scripts, review process |
| 4 | Path length issues | Medium | Low | Pre-scan detection, auto-rename with logging |
| 5 | Authentication token expiry | Low | Medium | Token refresh logic, alerting |
| 6 | Vendor delay (hardcopy) | Medium | Medium | Buffer time, parallel processing |
| 7 | Data loss during migration | Low | Critical | Checksums, validation, source retained |
| 8 | User adoption issues | Medium | Medium | Training, communication, support |
| 9 | Compliance gaps | Low | Critical | Pre-migration compliance review, audit trail |
| 10 | Budget overrun | Medium | Medium | Phase-based approach, regular monitoring |

### Rollback Plan

**If critical issues during migration:**
1. Stop migration scripts immediately
2. Document issue and files affected
3. Files already in SharePoint: Keep or delete based on issue
4. Source data intact (read-only, not deleted)
5. Fix issue in test environment
6. Resume or restart batch as appropriate

---

## Department Migration Schedule

### Gantt Chart Overview (18-Week Plan)

```
Week:  1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
       ├──┴──┴──┼──┴──┼──┴──┴──┴──┼──┴──┼──┴──┴──┴──┴──┼──┴──┤
Phase 1 ████████                                              Discovery
Phase 2          █████                                        Infrastructure
Phase 3               ████████████                            Development
Phase 4                            █████                      Pilot
Phase 5                                  ██████████████       Production
Phase 6                                               █████   Finalization

Hardcopy  ─────────────────────────████████████████████────   Parallel Track
```

### Weekly Milestones

| Week | Milestone |
|------|-----------|
| 2 | Discovery complete, inventory reports |
| 4 | SharePoint sites created, app registered |
| 8 | All scripts developed and tested |
| 10 | Pilot migration complete |
| 12 | HR migration complete |
| 14 | Finance migration complete |
| 17 | Production migration complete |
| 18 | Project close-out |

---

## Appendices

### A. Vendor Metadata Template

| Column | Description | Required | Example |
|--------|-------------|----------|---------|
| DocumentID | Unique ID | Yes | DOC-2026-00001 |
| FileName | Output filename | Yes | Contract_ABC_2026.pdf |
| DocumentTitle | Descriptive title | Yes | ABC Supplier Contract |
| DocumentType | Type category | Yes | Contract |
| Department | Target department | Yes | Finance |
| OriginalDate | Date on document | No | 2025-06-15 |
| ScanDate | When scanned | Yes | 2026-01-20 |
| Keywords | Search terms | No | supplier, contract, ABC |
| Classification | Security level | Yes | Confidential |
| RetentionCategory | Retention rule | Yes | Contracts |
| BoxReference | Physical box ID | Yes | BOX-FIN-2025-042 |
| PageCount | Number of pages | Yes | 12 |
| Notes | Special notes | No | Contains signature page |

### B. File Type Handling Matrix

| File Type | Extension | Max Size | Special Handling |
|-----------|-----------|----------|------------------|
| Office Docs | .docx, .xlsx, .pptx | 250GB | Standard |
| Legacy Office | .doc, .xls, .ppt | 250GB | Consider conversion |
| PDF | .pdf | 250GB | Standard |
| Images | .jpg, .png, .tiff | 250GB | Standard |
| CAD Files | .dwg, .dxf | 250GB | Verify preview support |
| Video | .mp4, .avi, .mov | 250GB | Large file handling |
| Archives | .zip, .7z | 250GB | Standard, no extraction |
| Executables | .exe, .msi | N/A | **Exclude from migration** |
| Database | .mdb, .accdb | N/A | **Exclude, special handling** |

### C. Configuration Template

```json
{
  "tenant_id": "your-tenant-id",
  "client_id": "your-client-id",
  "client_secret": "**stored-in-keyvault**",
  "sharepoint_host": "yourtenant.sharepoint.com",
  "sites": {
    "HR": "/sites/HR",
    "Finance": "/sites/Finance",
    "Production": "/sites/Production",
    "Marketing": "/sites/Marketing"
  },
  "batch_size": 100,
  "chunk_size_mb": 4,
  "max_retries": 3,
  "log_level": "INFO",
  "exclude_extensions": [".exe", ".msi", ".dll", ".tmp"],
  "exclude_folders": ["$RECYCLE.BIN", "System Volume Information"]
}
```

---

## Change Log

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-01-28 | [Your Name] | Initial plan creation |

---

## Sign-Off

| Role | Name | Signature | Date |
|------|------|-----------|------|
| Project Manager | | | |
| IT Lead | | | |
| Compliance | | | |
| Business Stakeholder | | | |
