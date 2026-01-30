# SharePoint Online Migration - Discovery Questionnaire

**Purpose:** Gather comprehensive information needed to plan and execute a successful document migration to SharePoint Online.

**Instructions:** Please complete all sections as thoroughly as possible. If you don't know an answer, indicate "Unknown" and we will investigate together.

---

## Section 1: Project Overview & Stakeholders

### 1.1 Project Information

| Question | Answer |
|----------|--------|
| Project Name | |
| Company/Organization Name | |
| Primary Contact Name | |
| Primary Contact Email | |
| Primary Contact Phone | |

### 1.2 Key Stakeholders

| Role | Name | Department | Email | Decision Authority |
|------|------|------------|-------|-------------------|
| Project Sponsor | | | | Yes / No |
| Project Manager | | | | Yes / No |
| IT Lead | | | | Yes / No |
| Compliance/Legal | | | | Yes / No |
| Department Rep 1 | | | | Yes / No |
| Department Rep 2 | | | | Yes / No |

### 1.3 Project Drivers

**Why are you migrating to SharePoint Online?** (Check all that apply)
- [ ] File server end-of-life / hardware refresh
- [ ] Move to cloud / reduce on-premises infrastructure
- [ ] Improve collaboration and remote access
- [ ] Consolidate multiple storage locations
- [ ] Compliance and security requirements
- [ ] Cost reduction
- [ ] Digital transformation initiative
- [ ] Disaster recovery improvement
- [ ] Other: _________________________________

### 1.4 Current Pain Points

**What problems exist with your current document storage?** (Check all that apply)
- [ ] Difficult to find documents
- [ ] Multiple versions of same document
- [ ] No access from outside office
- [ ] Storage capacity issues
- [ ] Backup/recovery concerns
- [ ] Security/permission issues
- [ ] Collaboration difficulties
- [ ] Audit/compliance gaps
- [ ] Other: _________________________________

---

## Section 2: Source Data - File Server

### 2.1 File Server Information

| Question | Answer |
|----------|--------|
| File server name(s) | |
| Operating System | Windows Server ____ / Linux / NAS |
| File server location (on-prem/datacenter) | |
| Network path (e.g., \\\\server\\share) | |
| Current total storage used | _____ GB / TB |
| Total number of files (estimated) | |
| Total number of folders (estimated) | |

### 2.2 Data Volume by Department

| Department | Estimated Size | Estimated File Count | Priority (1-5) |
|------------|----------------|---------------------|----------------|
| | | | |
| | | | |
| | | | |
| | | | |
| | | | |
| **Total** | | | |

### 2.3 Folder Structure

**How would you describe your current folder structure?**
- [ ] Flat (1-2 levels deep, well organized)
- [ ] Moderate (3-4 levels deep, mostly organized)
- [ ] Deep hierarchy (5+ levels deep)
- [ ] Mixed/Inconsistent (varies by department)
- [ ] Chaotic (needs significant cleanup)

**Please provide a sample of your folder structure:**
```
Example:
\\server\share\
├── Department1\
│   ├── Subfolder1\
│   └── Subfolder2\
├── Department2\
└── ...

Your structure:




```

**Do you want to preserve the existing folder structure in SharePoint?**
- [ ] Yes, exactly as-is
- [ ] Yes, but with some modifications (specify below)
- [ ] No, we want to restructure
- [ ] Need guidance on best approach

**If modifications needed, please describe:**
```




```

### 2.4 File Types

**What types of files are stored on the file server?** (Check all that apply)

| Category | File Types | Present? | Estimated % |
|----------|------------|----------|-------------|
| Office Documents | .docx, .xlsx, .pptx | Yes / No | ____% |
| Legacy Office | .doc, .xls, .ppt | Yes / No | ____% |
| PDF | .pdf | Yes / No | ____% |
| Images | .jpg, .png, .gif, .tiff, .bmp | Yes / No | ____% |
| CAD/Engineering | .dwg, .dxf, .stp, .iges | Yes / No | ____% |
| Video | .mp4, .avi, .mov, .wmv | Yes / No | ____% |
| Audio | .mp3, .wav | Yes / No | ____% |
| Archives | .zip, .rar, .7z | Yes / No | ____% |
| Email | .msg, .eml, .pst | Yes / No | ____% |
| Database | .mdb, .accdb, .sql | Yes / No | ____% |
| Executables | .exe, .msi, .dll | Yes / No | ____% |
| Source Code | .py, .js, .java, .cs, etc. | Yes / No | ____% |
| Other | _________________________ | Yes / No | ____% |

### 2.5 Large Files

**Do you have files larger than 100MB?**
- [ ] No
- [ ] Yes, a few (< 100 files)
- [ ] Yes, many (100-1000 files)
- [ ] Yes, significant amount (> 1000 files)

**What is your largest file size (approximately)?** _____ MB / GB

**What types of large files do you have?**
- [ ] Video files
- [ ] CAD/Engineering drawings
- [ ] High-resolution images
- [ ] Database backups
- [ ] Archives/ZIP files
- [ ] Other: _________________________________

### 2.6 Data Age and Activity

**What is the age distribution of your files?**
| Age | Estimated % | Still Actively Used? |
|-----|-------------|---------------------|
| Less than 1 year | ____% | Yes / No / Partially |
| 1-3 years | ____% | Yes / No / Partially |
| 3-5 years | ____% | Yes / No / Partially |
| 5-10 years | ____% | Yes / No / Partially |
| More than 10 years | ____% | Yes / No / Partially |

**Should old/inactive files be:**
- [ ] Migrated same as active files
- [ ] Migrated to separate "Archive" library
- [ ] Reviewed before migration (cleanup opportunity)
- [ ] Left on file server / not migrated
- [ ] Need guidance

### 2.7 Duplicate and Cleanup

**Do you suspect there are duplicate files?**
- [ ] No
- [ ] Yes, minimal
- [ ] Yes, significant amount
- [ ] Unknown

**Would you like duplicate detection before migration?**
- [ ] Yes, provide report for review
- [ ] Yes, automatically skip duplicates
- [ ] No, migrate everything

**Are there files/folders that should NOT be migrated?** (Check all that apply)
- [ ] Temporary files (.tmp, ~$*)
- [ ] System files (thumbs.db, desktop.ini)
- [ ] Personal folders (individual user folders)
- [ ] Executables (.exe, .msi)
- [ ] Specific folders: _________________________________
- [ ] Files older than _____ years
- [ ] Other: _________________________________

### 2.8 Current Permissions

**How are permissions currently managed?**
- [ ] Windows Active Directory groups
- [ ] Individual user permissions
- [ ] Mixed (groups and individuals)
- [ ] No specific permissions (everyone has access)
- [ ] Unknown

**Do you have documented permission requirements?**
- [ ] Yes, we have documentation
- [ ] Partially documented
- [ ] No documentation
- [ ] Need to audit current permissions

**Should permissions be migrated/replicated to SharePoint?**
- [ ] Yes, replicate exactly
- [ ] Yes, but simplified
- [ ] No, we will set up new permissions
- [ ] Need guidance

---

## Section 3: Source Data - Hardcopy Documents

### 3.1 Hardcopy Overview

**Do you have physical/hardcopy documents to digitize?**
- [ ] Yes
- [ ] No (skip to Section 4)

| Question | Answer |
|----------|--------|
| Estimated number of documents | |
| Estimated number of pages | |
| Physical location of documents | |
| Document age range | From _____ to _____ |

### 3.2 Document Types (Hardcopy)

**What types of physical documents need to be scanned?** (Check all that apply)
- [ ] Contracts and agreements
- [ ] Invoices and financial records
- [ ] HR/Personnel files
- [ ] Technical drawings/blueprints
- [ ] Correspondence/letters
- [ ] Reports
- [ ] Legal documents
- [ ] Certificates/licenses
- [ ] Photos/images
- [ ] Other: _________________________________

### 3.3 Scanning Vendor

**Do you have a scanning vendor selected?**
- [ ] Yes, vendor name: _________________________________
- [ ] No, need recommendations
- [ ] Will handle in-house

**If vendor selected, what is their delivery format?**
- [ ] PDF (standard)
- [ ] PDF/A (archival)
- [ ] TIFF
- [ ] Other: _________________________________

**Will the vendor provide OCR (searchable text)?**
- [ ] Yes
- [ ] No
- [ ] Unknown

**Will the vendor provide metadata?**
- [ ] Yes, in CSV/Excel format
- [ ] Yes, in XML format
- [ ] No, we need to add metadata ourselves
- [ ] Unknown

### 3.4 Hardcopy Metadata Requirements

**What information can be extracted from the physical documents?**
| Field | Visible on Document? | Vendor Will Capture? |
|-------|---------------------|---------------------|
| Document date | Yes / No / Sometimes | Yes / No |
| Document title | Yes / No / Sometimes | Yes / No |
| Author/creator | Yes / No / Sometimes | Yes / No |
| Department | Yes / No / Sometimes | Yes / No |
| Document type | Yes / No / Sometimes | Yes / No |
| Reference numbers | Yes / No / Sometimes | Yes / No |
| Other: __________ | Yes / No / Sometimes | Yes / No |

---

## Section 4: SharePoint Online Target

### 4.1 Current SharePoint Status

**Do you currently have Microsoft 365 / SharePoint Online?**
- [ ] Yes, actively using
- [ ] Yes, but not actively using
- [ ] Yes, in trial/pilot
- [ ] No, need to set up
- [ ] Unknown

**If yes, what is your SharePoint URL?**
`https://____________.sharepoint.com`

**What Microsoft 365 license do you have?**
- [ ] Microsoft 365 Business Basic
- [ ] Microsoft 365 Business Standard
- [ ] Microsoft 365 Business Premium
- [ ] Microsoft 365 E3
- [ ] Microsoft 365 E5
- [ ] Office 365 E1/E3/E5
- [ ] Other: _________________________________
- [ ] Unknown

### 4.2 SharePoint Structure Preference

**How would you like SharePoint organized?**
- [ ] One site per department (Recommended for large orgs)
- [ ] Single site with multiple document libraries
- [ ] Hub site with connected department sites
- [ ] Need guidance on best approach

**Site Type Preference:**
- [ ] Team Sites (collaboration-focused)
- [ ] Communication Sites (publishing-focused)
- [ ] Mix based on department needs
- [ ] Need guidance

### 4.3 Departments/Sites to Create

| Department | Site Needed? | Approx. Users | Special Requirements |
|------------|--------------|---------------|---------------------|
| | Yes / No | | |
| | Yes / No | | |
| | Yes / No | | |
| | Yes / No | | |
| | Yes / No | | |

### 4.4 Document Libraries

**How many document libraries per site?**
- [ ] One main library
- [ ] Separate libraries by document type
- [ ] Separate libraries for active vs archived
- [ ] Need guidance

**Standard libraries to create:** (Check all that apply)
- [ ] Active Documents
- [ ] Archived Documents
- [ ] Scanned Documents (from hardcopy)
- [ ] Templates
- [ ] Policies & Procedures
- [ ] Other: _________________________________

---

## Section 5: Metadata Requirements

### 5.1 Metadata Importance

**How important is document metadata/classification?**
- [ ] Critical - need detailed metadata for compliance
- [ ] Important - want good searchability
- [ ] Moderate - basic metadata is sufficient
- [ ] Low - just need the files accessible

### 5.2 Required Metadata Fields

**Which metadata fields do you need?** (Check all that apply)

| Field | Required? | Source | Notes |
|-------|-----------|--------|-------|
| Document Title | Yes / No | Auto / Manual | |
| Document Type | Yes / No | Auto / Manual | |
| Department | Yes / No | Auto / Manual | |
| Author | Yes / No | Auto / Manual | |
| Created Date | Yes / No | Auto / Manual | |
| Modified Date | Yes / No | Auto / Manual | |
| Keywords/Tags | Yes / No | Auto / Manual | |
| Project Name | Yes / No | Auto / Manual | |
| Client/Customer | Yes / No | Auto / Manual | |
| Contract Number | Yes / No | Auto / Manual | |
| Classification | Yes / No | Auto / Manual | |
| Retention Category | Yes / No | Auto / Manual | |
| Original Location | Yes / No | Auto / Manual | For audit trail |
| Custom: _________ | Yes / No | Auto / Manual | |
| Custom: _________ | Yes / No | Auto / Manual | |

### 5.3 Document Types

**List the document types/categories for your organization:**
```
Examples: Contract, Invoice, Report, Drawing, Policy, Memo, etc.

1.
2.
3.
4.
5.
6.
7.
8.
9.
10.
```

### 5.4 Classification Levels

**Do you need document classification (sensitivity levels)?**
- [ ] Yes
- [ ] No
- [ ] Need guidance

**If yes, what classification levels?**
- [ ] Public
- [ ] Internal
- [ ] Confidential
- [ ] Restricted / Highly Confidential
- [ ] Other: _________________________________

---

## Section 6: Compliance & Security

### 6.1 Industry & Regulations

**What industry are you in?**
- [ ] Manufacturing
- [ ] Healthcare
- [ ] Financial Services
- [ ] Government
- [ ] Education
- [ ] Retail
- [ ] Technology
- [ ] Legal
- [ ] Other: _________________________________

**Which regulations/standards apply to your documents?** (Check all that apply)
- [ ] None specific
- [ ] SOX (Sarbanes-Oxley)
- [ ] HIPAA
- [ ] GDPR
- [ ] ISO 9001
- [ ] ISO 27001
- [ ] Industry-specific: _________________________________
- [ ] Internal policies only
- [ ] Unknown

### 6.2 Retention Requirements

**Do you have document retention policies?**
- [ ] Yes, documented and enforced
- [ ] Yes, but not consistently applied
- [ ] No formal policy
- [ ] Need to create
- [ ] Unknown

**If yes, please list retention periods:**
| Document Type | Retention Period | After Retention |
|---------------|------------------|-----------------|
| Financial records | _____ years | Archive / Delete |
| HR records | _____ years | Archive / Delete |
| Contracts | _____ years | Archive / Delete |
| General documents | _____ years | Archive / Delete |
| Technical documents | _____ years | Archive / Delete |
| ______________ | _____ years | Archive / Delete |

### 6.3 Legal Hold

**Do you need legal hold capability?**
- [ ] Yes, critical requirement
- [ ] Yes, nice to have
- [ ] No
- [ ] Unknown

**Are any documents currently under legal hold?**
- [ ] Yes
- [ ] No
- [ ] Unknown

### 6.4 Audit Requirements

**Do you need audit trails for document access?**
- [ ] Yes, full audit logging
- [ ] Yes, basic logging
- [ ] No
- [ ] Need guidance

**What audit events need to be tracked?**
- [ ] Document views/reads
- [ ] Document edits
- [ ] Document downloads
- [ ] Document deletions
- [ ] Permission changes
- [ ] All of the above

### 6.5 Data Sensitivity

**Do any documents contain sensitive data?** (Check all that apply)
- [ ] Personal Identifiable Information (PII)
- [ ] Financial data (bank accounts, credit cards)
- [ ] Health information
- [ ] Trade secrets / IP
- [ ] Employee records
- [ ] Customer data
- [ ] None of the above

**Do you need Data Loss Prevention (DLP) policies?**
- [ ] Yes
- [ ] No
- [ ] Need guidance

---

## Section 7: Access & Permissions

### 7.1 User Access

**How many users will access SharePoint?**
| User Type | Count |
|-----------|-------|
| Full-time employees | |
| Contractors | |
| External partners | |
| **Total** | |

**Do external users (outside your organization) need access?**
- [ ] Yes
- [ ] No
- [ ] Maybe in the future

### 7.2 Permission Model

**How should permissions be structured?**
- [ ] Department-based (users access their department only)
- [ ] Role-based (based on job function)
- [ ] Project-based (cross-department projects)
- [ ] Mixed
- [ ] Need guidance

**Permission levels needed:**
| Level | Description | Who Gets This? |
|-------|-------------|----------------|
| Full Control | Manage site and permissions | Site admins |
| Edit | Add, edit, delete documents | ______________ |
| Contribute | Add documents only | ______________ |
| Read | View only | ______________ |

### 7.3 Authentication

**How do users currently authenticate?**
- [ ] Active Directory (on-premises)
- [ ] Azure AD
- [ ] Azure AD with MFA
- [ ] Other: _________________________________

**Is Azure AD Connect configured (AD sync)?**
- [ ] Yes
- [ ] No
- [ ] Unknown

---

## Section 8: Technical Environment

### 8.1 Network & Connectivity

**What is your internet bandwidth?**
- [ ] < 100 Mbps
- [ ] 100-500 Mbps
- [ ] 500 Mbps - 1 Gbps
- [ ] > 1 Gbps
- [ ] Unknown

**Are there any network restrictions for cloud uploads?**
- [ ] No restrictions
- [ ] Firewall/proxy restrictions
- [ ] Bandwidth limitations
- [ ] Upload size limits
- [ ] Unknown

### 8.2 Migration Machine

**What machine will run the migration scripts?**
- [ ] Dedicated server
- [ ] Admin workstation
- [ ] Virtual machine
- [ ] Cloud VM (Azure/AWS)
- [ ] Need guidance

**Operating system:**
- [ ] Windows 10/11
- [ ] Windows Server
- [ ] Linux
- [ ] Other: _________________________________

### 8.3 Scripting Preference

**Preferred scripting language:**
- [ ] Python (cross-platform, rich libraries)
- [ ] PowerShell (native Windows/Microsoft integration)
- [ ] No preference
- [ ] Need guidance

### 8.4 Azure AD App Registration

**Do you have access to Azure AD to create app registrations?**
- [ ] Yes, I am Global Admin
- [ ] Yes, I have Application Administrator role
- [ ] No, need to request from IT
- [ ] Unknown

**Is there an existing app registration for SharePoint API access?**
- [ ] Yes
- [ ] No
- [ ] Unknown

---

## Section 9: Timeline & Resources

### 9.1 Timeline

**When do you want to start the migration?**
- [ ] Immediately
- [ ] Within 1 month
- [ ] Within 3 months
- [ ] Flexible

**When must the migration be completed?**
- [ ] Hard deadline: _______________ (date)
- [ ] Soft target: _______________ (date)
- [ ] No specific deadline

**Are there any blackout periods (no migration)?**
- [ ] Month-end/Quarter-end periods
- [ ] Specific dates: _______________
- [ ] Holiday periods
- [ ] None

### 9.2 Migration Approach

**Preferred migration approach:**
- [ ] Big bang (migrate everything at once)
- [ ] Phased by department (Recommended)
- [ ] Phased by data type
- [ ] Gradual/continuous
- [ ] Need guidance

**Preferred order of departments:**
```
1. _________________ (Pilot)
2. _________________
3. _________________
4. _________________
5. _________________
```

### 9.3 Cut-over Strategy

**During migration, should source files be:**
- [ ] Read-only (no new files during migration)
- [ ] Still writable (sync new/changed files after)
- [ ] Phased cut-over by department
- [ ] Need guidance

### 9.4 Resources

**Who will be involved in the migration?**
| Role | Name | Availability |
|------|------|--------------|
| Migration lead | | Full-time / Part-time |
| Technical resource | | Full-time / Part-time |
| Department coordinators | | As needed |
| Testing/validation | | As needed |

**Is training needed for end users?**
- [ ] Yes, comprehensive training
- [ ] Yes, basic training
- [ ] No, users are familiar with SharePoint
- [ ] Need guidance

---

## Section 10: Post-Migration

### 10.1 Source Data Handling

**What should happen to source files after migration?**
- [ ] Keep read-only for ___ months, then delete
- [ ] Keep read-only indefinitely
- [ ] Archive to cold storage
- [ ] Delete immediately after validation
- [ ] Need guidance

### 10.2 Ongoing Management

**Who will manage SharePoint after migration?**
| Role | Name | Department |
|------|------|------------|
| SharePoint Admin | | |
| Site Collection Admin | | |
| Department Site Owners | | |

### 10.3 Success Criteria

**How will you measure migration success?**
- [ ] All files accessible in SharePoint
- [ ] No data loss
- [ ] User satisfaction
- [ ] Search functionality working
- [ ] Compliance requirements met
- [ ] Performance acceptable
- [ ] Other: _________________________________

---

## Section 11: Budget & Constraints

### 11.1 Budget

**Is there a defined budget for this migration?**
- [ ] Yes: $_______________
- [ ] No specific budget
- [ ] Need to determine

**Budget includes:** (Check all that apply)
- [ ] Internal staff time
- [ ] External consultants
- [ ] Software/tools
- [ ] Scanning vendor (hardcopy)
- [ ] Training
- [ ] Additional storage

### 11.2 Constraints

**Are there any constraints we should know about?**
- [ ] Limited IT resources
- [ ] Limited budget
- [ ] Regulatory deadlines
- [ ] Organizational changes pending
- [ ] Other systems dependent on file server
- [ ] Other: _________________________________

---

## Section 12: Additional Information

### 12.1 Previous Migration Experience

**Have you done a similar migration before?**
- [ ] Yes, successfully
- [ ] Yes, with challenges
- [ ] No, first time

**If yes, what lessons learned?**
```




```

### 12.2 Known Issues or Concerns

**Any specific concerns about this migration?**
```




```

### 12.3 Special Requirements

**Any special requirements not covered above?**
```




```

### 12.4 Questions for Migration Team

**What questions do you have?**
```




```

---

## Summary Section (To be completed by Migration Team)

### Key Findings
```




```

### Recommended Approach
```




```

### Risk Areas
```




```

### Next Steps
```




```

---

**Questionnaire Completed By:** _______________________
**Date:** _______________________
**Reviewed By:** _______________________
**Date:** _______________________

---

*Document Version: 1.0 | Created: 2026-01-28*
