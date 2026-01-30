# Migration Questionnaire - Admin Guide

**Purpose:** This guide explains why each section of the questionnaire matters and what to look out for during discovery.

---

## Quick Reference: Why Each Section Matters

| Section | Why It's Critical | Red Flags to Watch |
|---------|-------------------|-------------------|
| 1. Project Overview | Identifies decision makers, avoids delays | No clear sponsor, conflicting stakeholders |
| 2. File Server | Determines migration complexity and duration | Inconsistent structure, huge volume, many large files |
| 3. Hardcopy | Coordinates vendor timeline | No vendor selected, unclear metadata requirements |
| 4. SharePoint Target | Designs destination architecture | No M365 license, unclear structure preference |
| 5. Metadata | Defines searchability and organization | Too many fields, unrealistic manual entry expectations |
| 6. Compliance | Ensures legal/regulatory adherence | Unknown regulations, no retention policy |
| 7. Access & Permissions | Security model design | Complex permissions, external users |
| 8. Technical | Infrastructure readiness | Slow network, no admin access |
| 9. Timeline | Realistic planning | Unrealistic deadlines, no resources |
| 10. Post-Migration | Ensures sustainability | No SharePoint admin identified |
| 11. Budget | Resource allocation | No budget for tools or training |
| 12. Additional | Catches edge cases | Undisclosed requirements |

---

## Section-by-Section Deep Dive

### Section 1: Project Overview & Stakeholders

**Why it matters:**
- Identifies who can make decisions (avoids project delays)
- Understands the business drivers (helps prioritize)
- Identifies pain points to address

**Key questions to probe:**
- "Who has final sign-off authority?"
- "What happens if we don't complete by deadline?"
- "What's the biggest problem you're trying to solve?"

**Watch out for:**
- Multiple stakeholders with conflicting priorities
- No clear executive sponsor
- Vague or undefined success criteria

---

### Section 2: Source Data - File Server

**Why it matters:**
- Data volume directly impacts migration duration
- Folder structure affects SharePoint design
- File types determine special handling needs

**Key questions to probe:**
- "Are there any files you know shouldn't be migrated?"
- "Who currently manages the file server?"
- "How often do files change?"

**Technical checks you should run:**
```powershell
# Get total size
Get-ChildItem "\\server\share" -Recurse | Measure-Object -Property Length -Sum

# Count files by extension
Get-ChildItem "\\server\share" -Recurse -File |
    Group-Object Extension |
    Sort-Object Count -Descending |
    Select-Object Name, Count

# Find large files
Get-ChildItem "\\server\share" -Recurse -File |
    Where-Object {$_.Length -gt 100MB} |
    Select-Object FullName, @{N='SizeMB';E={[math]::Round($_.Length/1MB,2)}}
```

**Watch out for:**
- Files > 250GB (SharePoint limit)
- Path lengths > 400 characters
- Special characters in file names: `# % * : < > ? / \ |`
- Files with no extension
- Database files (.mdb, .accdb) - need special handling
- PST files - consider migrating to Exchange Online instead

**SharePoint Online Limits to Know:**
| Limit | Value |
|-------|-------|
| Max file size | 250 GB |
| Max path length | 400 characters |
| Max files per library | 30 million |
| Blocked file types | .exe, .dll, .msi, etc. |
| Storage per tenant | Based on license |

---

### Section 3: Hardcopy Documents

**Why it matters:**
- Vendor coordination affects overall timeline
- Metadata quality from vendor determines search capability
- OCR quality affects document usability

**Key questions to probe:**
- "What's the vendor's delivery schedule?"
- "Have you seen sample scans from the vendor?"
- "Who will validate the metadata from vendor?"

**Vendor specification checklist:**
- [ ] Output format (PDF/A recommended for archival)
- [ ] Resolution (300 DPI minimum for text)
- [ ] OCR included and accuracy level
- [ ] Metadata fields to capture
- [ ] File naming convention
- [ ] Delivery method (secure file transfer)
- [ ] Quality acceptance criteria
- [ ] Timeline and batch sizes

**Watch out for:**
- Vendor unable to provide metadata
- No quality assurance process
- Unclear delivery schedule
- No OCR (documents won't be searchable)

---

### Section 4: SharePoint Online Target

**Why it matters:**
- License type determines available features
- Site structure affects governance and permissions
- Wrong design now = expensive restructuring later

**License feature comparison:**
| Feature | Business Basic | E3 | E5 |
|---------|---------------|----|----|
| SharePoint storage | 1 TB + 10GB/user | Same | Same |
| Compliance Center | Basic | Yes | Advanced |
| DLP | No | Yes | Advanced |
| eDiscovery | No | Yes | Advanced |
| Sensitivity Labels | No | Basic | Full |

**Site structure recommendations:**
| Scenario | Recommended Structure |
|----------|----------------------|
| < 100 users, simple needs | Single site, multiple libraries |
| 100-500 users, departmental | One site per department |
| > 500 users, enterprise | Hub site architecture |
| Heavy collaboration | Team sites |
| Publishing/communication | Communication sites |

**Watch out for:**
- No M365 license (migration blocked)
- License doesn't support compliance features needed
- Stakeholders disagree on structure
- No SharePoint admin experience

---

### Section 5: Metadata Requirements

**Why it matters:**
- Metadata = findability (without it, documents get lost)
- Over-complicated metadata = user frustration
- Compliance often requires specific metadata

**Metadata design principles:**
1. **Start simple** - 5-7 fields maximum initially
2. **Make required fields minimal** - only truly mandatory
3. **Use choice fields** - better than free text for consistency
4. **Plan for automation** - what can be auto-populated?

**Recommended core metadata:**
| Field | Type | Auto/Manual | Notes |
|-------|------|-------------|-------|
| Document Type | Choice | Manual | Required |
| Department | Choice | Auto (from site) | Required |
| Year | Choice/Calculated | Auto | From date |
| Classification | Choice | Manual | If compliance needed |

**Watch out for:**
- Too many required fields (user resistance)
- Expecting manual entry for hundreds of thousands of files
- No standard document type taxonomy
- Conflicting metadata requirements between departments

---

### Section 6: Compliance & Security

**Why it matters:**
- Legal exposure if regulations not met
- Audit failures can be costly
- Data breaches have serious consequences

**Key compliance questions:**
- "Has Legal/Compliance reviewed this migration?"
- "Are any documents under litigation hold?"
- "What happens to documents after retention expires?"

**Compliance feature mapping:**
| Requirement | SharePoint Feature |
|-------------|-------------------|
| Retention | Retention policies/labels |
| Legal hold | In-place hold |
| Audit trail | Unified audit log |
| Classification | Sensitivity labels |
| Data protection | DLP policies |
| eDiscovery | Compliance Center |

**Watch out for:**
- Unknown regulatory requirements
- No documented retention policy
- Documents under legal hold (don't modify!)
- PII/sensitive data without protection plan

---

### Section 7: Access & Permissions

**Why it matters:**
- Wrong permissions = security risk or user frustration
- External sharing needs special consideration
- Permission complexity increases support burden

**Permission model options:**
| Model | Pros | Cons | Best For |
|-------|------|------|----------|
| Department-based | Simple, clear | Rigid | Traditional orgs |
| Role-based | Flexible | More complex | Matrix orgs |
| Site-based | Easy to manage | May duplicate content | Departmental |
| Item-level | Granular | High maintenance | Small scale only |

**Best practices:**
- Use groups, never individual permissions
- Inherit permissions where possible
- Break inheritance sparingly
- Document permission model

**Watch out for:**
- Individual permissions everywhere
- No documentation of current permissions
- External user requirements without governance
- No permission audit plan

---

### Section 8: Technical Environment

**Why it matters:**
- Network speed = migration duration
- Script platform affects tool selection
- Admin access required for setup

**Network bandwidth estimates:**
| Bandwidth | ~Transfer Rate | Time for 1 TB |
|-----------|----------------|---------------|
| 100 Mbps | ~10 MB/s | ~28 hours |
| 500 Mbps | ~50 MB/s | ~6 hours |
| 1 Gbps | ~100 MB/s | ~3 hours |

*Note: Real-world speeds are typically 50-70% of theoretical due to overhead*

**Migration machine requirements:**
- Windows 10/11 or Server 2019+
- 8 GB RAM minimum (16 GB recommended)
- SSD for temp files
- Network access to file server AND internet
- Admin access to Azure AD

**Watch out for:**
- Slow internet connection (< 100 Mbps)
- Firewall blocking Microsoft 365 endpoints
- No Azure AD admin access
- Machine cannot reach file server

---

### Section 9: Timeline & Resources

**Why it matters:**
- Unrealistic timeline = failed project
- Insufficient resources = delays and errors
- Business cycles affect migration windows

**Rough timeline estimates:**
| Phase | Duration | Dependencies |
|-------|----------|--------------|
| Discovery | 2-3 weeks | Stakeholder availability |
| Setup | 1-2 weeks | Azure AD access |
| Development | 2-4 weeks | Technical resources |
| Pilot | 1-2 weeks | Pilot department identified |
| Migration | 4-8 weeks | Data volume |
| Validation | 1-2 weeks | Testing resources |

**Migration speed estimates (per batch):**
| Data Size | Estimated Duration |
|-----------|-------------------|
| 50 GB | 4-8 hours |
| 100 GB | 8-16 hours |
| 500 GB | 2-4 days |
| 1 TB | 4-7 days |

**Watch out for:**
- "We need this done in 2 weeks" for large datasets
- No dedicated migration resource
- Critical blackout periods not communicated
- Change freeze during planned migration

---

### Section 10: Post-Migration

**Why it matters:**
- No owner = SharePoint becomes new file server chaos
- Source decommission needs planning
- Users need to know how to use new system

**Post-migration checklist:**
- [ ] SharePoint administrators trained
- [ ] Site owners identified per department
- [ ] User training completed
- [ ] Support process defined
- [ ] Source data retention policy set
- [ ] Backup/DR verified
- [ ] Governance documentation complete

**Watch out for:**
- No identified SharePoint admin
- No user training planned
- Expectation to delete source immediately
- No ongoing governance plan

---

## Discovery Meeting Tips

### Before the Meeting
- [ ] Send questionnaire in advance
- [ ] Request access to file server for assessment
- [ ] Identify technical contact for follow-up
- [ ] Review any existing documentation

### During the Meeting
- Use questionnaire as guide, not rigid script
- Ask "why" to understand requirements
- Note concerns and objections
- Identify decision makers present
- Schedule follow-up for unanswered items

### After the Meeting
- Document all findings
- Identify gaps requiring investigation
- Create initial risk assessment
- Develop preliminary timeline
- Schedule technical assessment

### Questions to Ask When Answers Are Vague

| Vague Answer | Follow-up Question |
|--------------|-------------------|
| "A lot of files" | "Can we access the server to run a scan?" |
| "Users need access" | "Which users? Can you list the groups?" |
| "It's important" | "What happens if we don't have this?" |
| "Soon" | "Is there a specific date or event driving this?" |
| "We'll figure it out" | "Who will make that decision and when?" |

---

## Common Migration Gotchas

1. **OneNote notebooks** - Need special handling, not regular files
2. **Linked files** - Excel files linked to other files break when moved
3. **Access databases** - Consider migrating to SharePoint lists or Power Apps
4. **PST files** - Should go to Exchange Online, not SharePoint
5. **Files with macros** - May have security implications
6. **Versioned files** - Decide if version history migrates
7. **Checked-out files** - Need to be checked in before migration
8. **Long file names** - May hit path limits when nested in SharePoint
9. **Special characters** - `# % & * { } \ : < > ? / + | "` cause issues
10. **Hidden files/folders** - Decide if they should migrate

---

*Guide Version: 1.0 | Created: 2026-01-28*
