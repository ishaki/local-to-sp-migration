# SharePoint Online Upload Tool

Upload files to SharePoint Online document library with metadata mapping.

## Features

- Upload files from Excel manifest to SharePoint Online
- Flexible metadata mapping (N columns)
- Interactive column mapping wizard
- Chunked upload for large files (>250MB)
- Creates target folders automatically
- Overwrites existing files (creates new version)
- Detailed logging and progress tracking
- Upload report generation

## Prerequisites

### 1. Python Requirements

```bash
pip install -r requirements.txt
```

### 2. Azure AD App Registration

You need an Azure AD App Registration with the following:

1. **Create App Registration:**
   - Go to Azure Portal > Azure Active Directory > App registrations
   - Click "New registration"
   - Name: `SP-Upload-Tool` (or your preferred name)
   - Supported account types: "Accounts in this organizational directory only"
   - Click "Register"

2. **Configure API Permissions:**
   - Go to "API permissions"
   - Click "Add a permission"
   - Select "SharePoint"
   - Select "Application permissions"
   - Add: `Sites.ReadWrite.All`
   - Click "Grant admin consent"

3. **Create Client Secret:**
   - Go to "Certificates & secrets"
   - Click "New client secret"
   - Description: `SP Upload Tool`
   - Expiry: Choose appropriate period
   - Copy the secret value (you won't see it again!)

4. **Note the following:**
   - Client ID (Application ID)
   - Client Secret (from step 3)
   - Tenant ID

## Configuration

1. Copy `config.template.json` to `config.json`:

```bash
cp config.template.json config.json
```

2. Edit `config.json` with your values:

```json
{
    "site_url": "https://yourtenant.sharepoint.com/sites/yoursite",
    "client_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
    "client_secret": "your-client-secret-value"
}
```

**Important:** Never commit `config.json` to source control!

## Excel File Format

The source Excel file should have the following columns:

| Column | Required | Description |
|--------|----------|-------------|
| FileName | Yes | Name of the file to upload |
| FilePath | Yes | Local folder path where the file is located |
| TargetFolder | No | Target folder in SharePoint (leave empty for root) |
| [Metadata columns] | No | Any additional columns for metadata |

### Example:

| FileName | FilePath | TargetFolder | InvoiceNumber | VendorName | Amount |
|----------|----------|--------------|---------------|------------|--------|
| INV001.pdf | D:\Invoices | 2024/January | INV-2024-001 | ABC Corp | 5000 |
| INV002.pdf | D:\Invoices | 2024/January | INV-2024-002 | XYZ Ltd | 3500 |
| INV003.pdf | D:\Invoices | 2024/February | INV-2024-003 | ABC Corp | 7500 |

## Usage

### Basic Usage

```bash
python sp_upload.py --library "Documents" --source files.xlsx
```

### With Custom Config Path

```bash
python sp_upload.py --library "Finance Documents" --source files.xlsx --config myconfig.json
```

### With Saved Column Mapping

```bash
python sp_upload.py --library "Documents" --source files.xlsx --mapping column_mapping.json
```

## Column Mapping

When you run the script for the first time, it will:

1. Connect to SharePoint
2. List available columns from the document library
3. Prompt you to map each Excel metadata column to a SharePoint column
4. Save the mapping to `output/column_mapping.json` for future use

### Example Mapping Session:

```
============================================================
COLUMN MAPPING WIZARD
============================================================

Available SharePoint columns:
------------------------------------------------------------
   1. [Text      ] Invoice Number
   2. [Text      ] Vendor Name
   3. [Currency  ] Amount*
   4. [DateTime  ] Invoice Date
   5. [Choice    ] Status
   ...

Excel metadata columns to map:
  - InvoiceNumber
  - VendorName
  - Amount

------------------------------------------------------------
For each Excel column, enter the SharePoint column number to map to.
Enter 0 or press Enter to skip the column.
------------------------------------------------------------

Map 'InvoiceNumber' to SharePoint column [0 to skip]: 1
  Mapped 'InvoiceNumber' -> 'Invoice Number' (InvoiceNumber)

Map 'VendorName' to SharePoint column [0 to skip]: 2
  Mapped 'VendorName' -> 'Vendor Name' (VendorName)

Map 'Amount' to SharePoint column [0 to skip]: 3
  Mapped 'Amount' -> 'Amount' (Amount)
```

## Output

The script generates the following output in the `output` folder:

| File | Description |
|------|-------------|
| `upload_log_YYYYMMDD_HHMMSS.log` | Detailed log of the upload process |
| `upload_report_YYYYMMDD_HHMMSS.xlsx` | Excel report with upload results |
| `column_mapping.json` | Saved column mapping for reuse |

## Troubleshooting

### "Access denied" error

- Verify the App Registration has `Sites.ReadWrite.All` permission
- Ensure admin consent has been granted
- Check that the site URL is correct

### "Library not found" error

- Verify the library name is spelled correctly (case-sensitive)
- Ensure the library exists in the site

### Large file upload fails

- Files over 250MB use chunked upload automatically
- If timeout occurs, check network stability
- Maximum file size is 250GB (SharePoint limit)

### Metadata update fails

- Verify the SharePoint column type matches the data
- Check for required fields that are empty
- Ensure Choice column values match exactly

## Security Notes

1. **Never commit `config.json`** - It contains sensitive credentials
2. **Rotate client secrets** regularly
3. **Use least privilege** - Only grant necessary permissions
4. **Audit access** - Monitor who uses the tool

## License

Proprietary - All Rights Reserved
