# Local File Server to SharePoint Online Migration

A collection of tools and documentation to support migrating Windows file server data to SharePoint Online.

## Overview

This project provides resources for organizations planning to migrate their on-premises file server content to SharePoint Online, including:

- **Pre-migration audit tools** - Scan and inventory file servers before migration
- **Planning documents** - Templates and guides for migration planning
- **Best practices** - SharePoint document management recommendations

## Tools

### File Server Audit Tool

Python script to scan Windows file servers and generate Excel reports with:

- Complete folder/file inventory
- NTFS permissions (inherited vs explicit)
- File metadata (size, extension, last modified)
- Owner information

**Location:** `scripts/file_server_audit/`

**Requirements:**
```bash
pip install openpyxl pywin32
```

**Usage:**
```powershell
# Basic scan
python file_server_audit.py "D:\Data"

# With folder exclusions (CLI)
python file_server_audit.py "D:\Data" -x "*\Temp" -x "*\Archive"

# With exclusion file
python file_server_audit.py "D:\Data" --exclude-file exclusions.txt

# Combined
python file_server_audit.py "\\fileserver\share" -x "*\Temp" -e exclusions.txt
```

**Output:**
- Excel file with file/folder listing and permissions
- Log file with scan progress and errors

## Documents

| Document | Description |
|----------|-------------|
| `SharePoint_Migration_Project_Plan.md` | Comprehensive migration project plan template |
| `Migration_Discovery_Questionnaire.md` | Questions to gather requirements from stakeholders |
| `Questionnaire_Guide_for_Admin.md` | Guide for IT admins completing the questionnaire |
| `Migration_Status_Tracker.md` | Template to track migration progress |
| `SharePoint_DMS_Best_Practices.md` | Document management best practices for SharePoint |
| `SharePoint_DMS_Presentation.md` | Presentation material for stakeholders |
| `Stakeholder_Handout_OnePage.md` | One-page summary for executives |

## Migration Workflow

```
1. Discovery & Planning
   └── Run audit tool on file servers
   └── Complete discovery questionnaire
   └── Review permissions report

2. Preparation
   └── Clean up unnecessary files
   └── Resolve permission issues
   └── Design SharePoint site structure

3. Migration
   └── Configure SharePoint sites/libraries
   └── Execute migration (SharePoint Migration Tool / 3rd party)
   └── Validate migrated content

4. Post-Migration
   └── User training
   └── Decommission file server
```

## Author

**Ishak Ahmad** - ishak.ahmad@gmail.com

## License

Proprietary - All Rights Reserved
