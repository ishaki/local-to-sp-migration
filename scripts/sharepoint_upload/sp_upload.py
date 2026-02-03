#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
================================================================================
SharePoint Online Document Upload Tool
================================================================================

Description:
    Uploads files to SharePoint Online document library with metadata mapping.
    Supports flexible metadata columns and large file uploads (chunked upload).

Features:
    - Upload files from Excel manifest to SharePoint Online
    - Flexible metadata mapping (N columns)
    - Interactive column mapping wizard
    - Chunked upload for large files (>250MB)
    - Creates target folders if they don't exist
    - Overwrites existing files (creates new version)
    - Detailed logging and progress tracking
    - Upload report generation

Requirements:
    pip install Office365-REST-Python-Client pandas openpyxl

Usage:
    python sp_upload.py --library "Documents" --source files.xlsx
    python sp_upload.py --library "Finance Documents" --source files.xlsx --config config.json

--------------------------------------------------------------------------------
Author:     Ishak Ahmad (ishak.ahmad@gmail.com)
Created:    2025
Version:    1.0.0
License:    Proprietary - All Rights Reserved

Copyright (c) 2025 Ishak Ahmad. All rights reserved.
================================================================================
"""

import os
import sys
import json
import argparse
import logging
from datetime import datetime
from pathlib import Path

try:
    import pandas as pd
except ImportError:
    print("ERROR: pandas is not installed. Please run: pip install pandas openpyxl")
    sys.exit(1)

try:
    from office365.runtime.auth.client_credential import ClientCredential
    from office365.sharepoint.client_context import ClientContext
    from office365.sharepoint.files.file import File
except ImportError:
    print("ERROR: Office365-REST-Python-Client is not installed.")
    print("Please run: pip install Office365-REST-Python-Client")
    sys.exit(1)


# Constants
CHUNK_SIZE = 10 * 1024 * 1024  # 10MB chunks for large file upload
LARGE_FILE_THRESHOLD = 250 * 1024 * 1024  # 250MB


def setup_logging(output_dir):
    """Setup logging to both console and file."""
    log_file = output_dir / f"upload_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

    logger = logging.getLogger('SPUpload')
    logger.setLevel(logging.DEBUG)

    # Console handler - INFO level
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_format = logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S')
    console_handler.setFormatter(console_format)

    # File handler - DEBUG level
    file_handler = logging.FileHandler(log_file, encoding='utf-8')
    file_handler.setLevel(logging.DEBUG)
    file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_format)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger, log_file


def load_config(config_path):
    """Load configuration from JSON file."""
    if not os.path.exists(config_path):
        print(f"ERROR: Config file not found: {config_path}")
        print("\nPlease create a config.json file with the following structure:")
        print(json.dumps({
            "site_url": "https://yourtenant.sharepoint.com/sites/yoursite",
            "client_id": "your-client-id",
            "client_secret": "your-client-secret"
        }, indent=2))
        sys.exit(1)

    with open(config_path, 'r') as f:
        config = json.load(f)

    required_keys = ['site_url', 'client_id', 'client_secret']
    for key in required_keys:
        if key not in config:
            print(f"ERROR: Missing required config key: {key}")
            sys.exit(1)

    return config


def connect_to_sharepoint(config, logger):
    """Connect to SharePoint Online using client credentials."""
    logger.info(f"Connecting to SharePoint: {config['site_url']}")

    try:
        credentials = ClientCredential(config['client_id'], config['client_secret'])
        ctx = ClientContext(config['site_url']).with_credentials(credentials)

        # Test connection
        web = ctx.web
        ctx.load(web)
        ctx.execute_query()

        logger.info(f"Connected successfully to: {web.properties['Title']}")
        return ctx

    except Exception as e:
        logger.error(f"Failed to connect to SharePoint: {str(e)}")
        sys.exit(1)


def get_library_columns(ctx, library_name, logger):
    """Get available columns from SharePoint document library."""
    logger.info(f"Fetching columns from library: {library_name}")

    try:
        # Get the library
        library = ctx.web.lists.get_by_title(library_name)
        ctx.load(library)
        ctx.execute_query()

        # Get fields
        fields = library.fields
        ctx.load(fields)
        ctx.execute_query()

        # Filter to user-editable fields (exclude system fields)
        system_fields = [
            'ContentType', 'ID', '_UIVersionString', 'Edit', 'LinkTitleNoMenu',
            'LinkTitle', 'DocIcon', 'ItemChildCount', 'FolderChildCount',
            'AppAuthor', 'AppEditor', 'Attachments', 'GUID', 'ProgId',
            'ScopeId', 'File_x0020_Type', 'HTML_x0020_File_x0020_Type',
            'MetaInfo', 'ServerUrl', 'EncodedAbsUrl', 'BaseName', '_Level',
            '_IsCurrentVersion', 'Created_x0020_Date', 'Last_x0020_Modified',
            'FSObjType', 'PermMask', 'FileLeafRef', 'FileDirRef', 'FileRef',
            'File_x0020_Size', 'ComplianceAssetId', 'SMTotalSize',
            'SMLastModifiedDate', 'SMTotalFileStreamSize', 'SMTotalFileCount',
            '_ComplianceFlags', '_ComplianceTag', '_ComplianceTagWrittenTime',
            '_ComplianceTagUserId', '_CommentCount', '_LikeCount', 'BSN',
            '_CheckinComment', 'LinkFilenameNoMenu', 'LinkFilename',
            '_EditMenuTableStart', '_EditMenuTableStart2', '_EditMenuTableEnd',
            '_IsRecord', 'MediaServiceImageTags', 'MediaServiceOCR',
            'MediaServiceGenerationTime', 'MediaServiceEventHashCode',
            'MediaServiceAutoKeyPoints', 'MediaServiceKeyPoints',
            'MediaServiceDateTaken', 'MediaServiceLocation',
            'MediaLengthInSeconds', 'Restricted', 'AccessPolicy',
            'NoExecute', 'ContentVersion', 'A2ODMountCount',
            '_VirusStatus', '_VirusVendorID', '_VirusInfo', '_ShortcutUrl',
            '_ShortcutSiteId', '_ShortcutWebId', '_ShortcutUniqueId',
            '_ExtendedDescription', 'TaxCatchAll', 'TaxCatchAllLabel',
            '_IpLabelId', '_IpLabelAssignmentMethod', '_IsLabelEncryptionApplied',
            '_DisplayName', 'IconOverlay', 'SyncClientId', 'TaxKeywordTaxHTField'
        ]

        editable_columns = []
        for field in fields:
            # Skip system and hidden fields
            if (field.properties.get('Hidden', False) or
                field.properties.get('ReadOnlyField', False) or
                field.properties.get('InternalName') in system_fields or
                    field.properties.get('InternalName', '').startswith('_')):
                continue

            # Get field info
            field_info = {
                'internal_name': field.properties.get('InternalName'),
                'display_name': field.properties.get('Title'),
                'type': field.properties.get('TypeAsString'),
                'required': field.properties.get('Required', False)
            }

            # Include common editable types
            editable_types = ['Text', 'Note', 'Choice', 'MultiChoice', 'Number',
                              'Currency', 'DateTime', 'Boolean', 'URL']

            if field_info['type'] in editable_types:
                editable_columns.append(field_info)

        logger.info(f"Found {len(editable_columns)} editable columns")
        return editable_columns

    except Exception as e:
        logger.error(f"Failed to get library columns: {str(e)}")
        sys.exit(1)


def read_excel_file(excel_path, logger):
    """Read the Excel file with file list and metadata."""
    logger.info(f"Reading Excel file: {excel_path}")

    try:
        df = pd.read_excel(excel_path)
        logger.info(f"Found {len(df)} rows in Excel file")
        logger.info(f"Columns: {list(df.columns)}")
        return df

    except Exception as e:
        logger.error(f"Failed to read Excel file: {str(e)}")
        sys.exit(1)


def get_metadata_columns(df):
    """Identify metadata columns from Excel (excluding FileName, FilePath, TargetFolder)."""
    system_columns = ['FileName', 'FilePath', 'TargetFolder']
    metadata_columns = [col for col in df.columns if col not in system_columns]
    return metadata_columns


def interactive_column_mapping(excel_columns, sp_columns, logger):
    """Interactive wizard to map Excel columns to SharePoint columns."""
    print("\n" + "=" * 60)
    print("COLUMN MAPPING WIZARD")
    print("=" * 60)

    print("\nAvailable SharePoint columns:")
    print("-" * 60)
    for i, col in enumerate(sp_columns, 1):
        req_marker = "*" if col['required'] else " "
        print(f"  {i:2}. [{col['type']:10}] {col['display_name']}{req_marker}")

    print("\n  * = Required field")
    print("-" * 60)

    print("\nExcel metadata columns to map:")
    for col in excel_columns:
        print(f"  - {col}")

    print("\n" + "-" * 60)
    print("For each Excel column, enter the SharePoint column number to map to.")
    print("Enter 0 or press Enter to skip the column.")
    print("-" * 60)

    mapping = {}

    for excel_col in excel_columns:
        while True:
            try:
                user_input = input(f"\nMap '{excel_col}' to SharePoint column [0 to skip]: ").strip()

                if user_input == '' or user_input == '0':
                    print(f"  Skipping '{excel_col}'")
                    break

                col_num = int(user_input)

                if col_num < 1 or col_num > len(sp_columns):
                    print(f"  Invalid number. Please enter 1-{len(sp_columns)} or 0 to skip.")
                    continue

                sp_col = sp_columns[col_num - 1]
                mapping[excel_col] = sp_col['internal_name']
                print(f"  Mapped '{excel_col}' -> '{sp_col['display_name']}' ({sp_col['internal_name']})")
                break

            except ValueError:
                print("  Please enter a valid number.")

    print("\n" + "=" * 60)
    print("COLUMN MAPPING SUMMARY")
    print("=" * 60)

    if mapping:
        for excel_col, sp_col in mapping.items():
            print(f"  {excel_col} -> {sp_col}")
    else:
        print("  No columns mapped (metadata will not be updated)")

    print("=" * 60)

    confirm = input("\nProceed with this mapping? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Mapping cancelled by user.")
        sys.exit(0)

    logger.info(f"Column mapping confirmed: {mapping}")
    return mapping


def ensure_folder_exists(ctx, library_name, folder_path, logger):
    """Ensure target folder exists in SharePoint, create if not."""
    if not folder_path or pd.isna(folder_path):
        return None

    folder_path = str(folder_path).strip().strip('/')

    if not folder_path:
        return None

    logger.debug(f"Ensuring folder exists: {folder_path}")

    try:
        # Build the full server-relative URL
        library = ctx.web.lists.get_by_title(library_name)
        ctx.load(library, ["RootFolder"])
        ctx.execute_query()

        root_folder_url = library.root_folder.serverRelativeUrl
        target_folder_url = f"{root_folder_url}/{folder_path}"

        # Try to get the folder
        try:
            folder = ctx.web.get_folder_by_server_relative_url(target_folder_url)
            ctx.load(folder)
            ctx.execute_query()
            logger.debug(f"Folder exists: {target_folder_url}")
            return target_folder_url

        except Exception:
            # Folder doesn't exist, create it
            logger.info(f"Creating folder: {folder_path}")

            # Create folders recursively
            parts = folder_path.split('/')
            current_path = root_folder_url

            for part in parts:
                current_path = f"{current_path}/{part}"
                try:
                    folder = ctx.web.get_folder_by_server_relative_url(current_path)
                    ctx.load(folder)
                    ctx.execute_query()
                except Exception:
                    # Create this folder level
                    parent_path = '/'.join(current_path.split('/')[:-1])
                    parent_folder = ctx.web.get_folder_by_server_relative_url(parent_path)
                    parent_folder.folders.add(part)
                    ctx.execute_query()
                    logger.debug(f"Created folder: {current_path}")

            return target_folder_url

    except Exception as e:
        logger.error(f"Failed to create folder {folder_path}: {str(e)}")
        raise


def upload_file(ctx, library_name, local_path, target_folder_url, logger):
    """Upload a file to SharePoint (handles large files with chunked upload)."""
    file_size = os.path.getsize(local_path)
    file_name = os.path.basename(local_path)

    logger.debug(f"Uploading: {file_name} ({file_size / 1024 / 1024:.2f} MB)")

    try:
        # Get target folder
        if target_folder_url:
            target_folder = ctx.web.get_folder_by_server_relative_url(target_folder_url)
        else:
            library = ctx.web.lists.get_by_title(library_name)
            ctx.load(library, ["RootFolder"])
            ctx.execute_query()
            target_folder = library.root_folder

        # Upload based on file size
        if file_size > LARGE_FILE_THRESHOLD:
            # Chunked upload for large files
            logger.info(f"Using chunked upload for large file: {file_name}")
            uploaded_file = upload_large_file(ctx, target_folder, local_path, file_name, logger)
        else:
            # Standard upload
            with open(local_path, 'rb') as f:
                file_content = f.read()
            uploaded_file = target_folder.upload_file(file_name, file_content).execute_query()

        logger.debug(f"Upload complete: {file_name}")
        return uploaded_file

    except Exception as e:
        logger.error(f"Failed to upload {file_name}: {str(e)}")
        raise


def upload_large_file(ctx, target_folder, local_path, file_name, logger):
    """Upload large file using chunked upload."""
    file_size = os.path.getsize(local_path)
    chunk_count = (file_size // CHUNK_SIZE) + 1

    logger.debug(f"File size: {file_size / 1024 / 1024:.2f} MB, Chunks: {chunk_count}")

    with open(local_path, 'rb') as f:
        # First chunk - create upload session
        first_chunk = f.read(CHUNK_SIZE)
        upload_result = target_folder.files.create_upload_session(
            file_name, len(first_chunk)
        ).execute_query()

        # Upload remaining chunks
        chunk_num = 1
        while True:
            chunk = f.read(CHUNK_SIZE)
            if not chunk:
                break

            chunk_num += 1
            logger.debug(f"Uploading chunk {chunk_num}/{chunk_count}")

            upload_result = upload_result.continue_upload(chunk).execute_query()

        # Finish upload
        uploaded_file = upload_result.finish_upload().execute_query()

    return uploaded_file


def update_file_metadata(ctx, file_item, metadata, column_mapping, logger):
    """Update file metadata in SharePoint."""
    if not column_mapping or not metadata:
        return

    update_data = {}

    for excel_col, sp_col in column_mapping.items():
        if excel_col in metadata:
            value = metadata[excel_col]

            # Skip NaN/None values
            if pd.isna(value):
                continue

            # Convert value based on type
            if isinstance(value, datetime):
                value = value.isoformat()
            elif isinstance(value, (int, float)):
                if pd.isna(value):
                    continue
                # Keep as-is for Number/Currency
            else:
                value = str(value)

            update_data[sp_col] = value

    if update_data:
        logger.debug(f"Updating metadata: {update_data}")
        try:
            for key, value in update_data.items():
                file_item.set_property(key, value)
            file_item.update()
            ctx.execute_query()
            logger.debug("Metadata updated successfully")
        except Exception as e:
            logger.warning(f"Failed to update metadata: {str(e)}")


def generate_report(results, output_dir, logger):
    """Generate upload report."""
    report_file = output_dir / f"upload_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"

    df = pd.DataFrame(results)

    # Write to Excel with formatting
    with pd.ExcelWriter(report_file, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='Upload Results', index=False)

        # Auto-adjust column widths
        worksheet = writer.sheets['Upload Results']
        for idx, col in enumerate(df.columns):
            max_length = max(
                df[col].astype(str).map(len).max(),
                len(col)
            ) + 2
            worksheet.column_dimensions[chr(65 + idx)].width = min(max_length, 50)

    logger.info(f"Report saved to: {report_file}")
    return report_file


def main():
    # Parse arguments
    parser = argparse.ArgumentParser(
        description='Upload files to SharePoint Online with metadata',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Examples:
    python sp_upload.py --library "Documents" --source files.xlsx
    python sp_upload.py --library "Finance Documents" --source files.xlsx --config config.json
        '''
    )
    parser.add_argument('--library', '-l', required=True,
                        help='Target SharePoint document library name')
    parser.add_argument('--source', '-s', required=True,
                        help='Path to Excel file containing file list')
    parser.add_argument('--config', '-c', default='config.json',
                        help='Path to config file (default: config.json)')
    parser.add_argument('--mapping', '-m',
                        help='Path to saved column mapping JSON file (skip interactive mapping)')

    args = parser.parse_args()

    # Setup paths
    script_dir = Path(__file__).parent.absolute()
    output_dir = script_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Resolve config path
    config_path = Path(args.config)
    if not config_path.is_absolute():
        config_path = script_dir / config_path

    # Setup logging
    logger, log_file = setup_logging(output_dir)

    logger.info("=" * 60)
    logger.info("SHAREPOINT UPLOAD TOOL")
    logger.info("=" * 60)
    logger.info(f"Library: {args.library}")
    logger.info(f"Source: {args.source}")
    logger.info(f"Config: {config_path}")
    logger.info(f"Log file: {log_file}")
    logger.info("=" * 60)

    # Load config
    config = load_config(str(config_path))

    # Connect to SharePoint
    ctx = connect_to_sharepoint(config, logger)

    # Get library columns
    sp_columns = get_library_columns(ctx, args.library, logger)

    # Read Excel file
    df = read_excel_file(args.source, logger)

    # Get metadata columns from Excel
    excel_metadata_cols = get_metadata_columns(df)

    # Column mapping
    if args.mapping and os.path.exists(args.mapping):
        # Load saved mapping
        with open(args.mapping, 'r') as f:
            column_mapping = json.load(f)
        logger.info(f"Loaded column mapping from: {args.mapping}")
    elif excel_metadata_cols:
        # Interactive mapping
        column_mapping = interactive_column_mapping(excel_metadata_cols, sp_columns, logger)

        # Save mapping for future use
        mapping_file = output_dir / "column_mapping.json"
        with open(mapping_file, 'w') as f:
            json.dump(column_mapping, f, indent=2)
        logger.info(f"Column mapping saved to: {mapping_file}")
    else:
        column_mapping = {}
        logger.info("No metadata columns found in Excel file")

    # Process files
    logger.info("-" * 60)
    logger.info("Starting file upload...")
    logger.info("-" * 60)

    results = []
    success_count = 0
    error_count = 0
    total_files = len(df)

    for idx, row in df.iterrows():
        file_name = row.get('FileName', '')
        file_path = row.get('FilePath', '')
        target_folder = row.get('TargetFolder', '')

        # Build full local path
        local_path = os.path.join(file_path, file_name)

        result = {
            'FileName': file_name,
            'FilePath': file_path,
            'TargetFolder': target_folder,
            'Status': '',
            'Message': '',
            'Timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }

        logger.info(f"[{idx + 1}/{total_files}] Processing: {file_name}")

        # Validate file exists
        if not os.path.exists(local_path):
            result['Status'] = 'ERROR'
            result['Message'] = f'File not found: {local_path}'
            logger.error(f"  File not found: {local_path}")
            error_count += 1
            results.append(result)
            continue

        try:
            # Ensure target folder exists
            target_folder_url = ensure_folder_exists(ctx, args.library, target_folder, logger)

            # Upload file
            uploaded_file = upload_file(ctx, args.library, local_path, target_folder_url, logger)

            # Get list item for metadata update
            ctx.load(uploaded_file, ["ListItemAllFields"])
            ctx.execute_query()
            file_item = uploaded_file.listItemAllFields

            # Get metadata from row
            metadata = {col: row.get(col) for col in excel_metadata_cols}

            # Update metadata
            update_file_metadata(ctx, file_item, metadata, column_mapping, logger)

            result['Status'] = 'SUCCESS'
            result['Message'] = 'Uploaded successfully'
            success_count += 1
            logger.info(f"  Uploaded successfully")

        except Exception as e:
            result['Status'] = 'ERROR'
            result['Message'] = str(e)
            error_count += 1
            logger.error(f"  Error: {str(e)}")

        results.append(result)

    # Summary
    logger.info("=" * 60)
    logger.info("UPLOAD COMPLETE")
    logger.info("=" * 60)
    logger.info(f"Total files: {total_files}")
    logger.info(f"Successful: {success_count}")
    logger.info(f"Errors: {error_count}")
    logger.info("=" * 60)

    # Generate report
    report_file = generate_report(results, output_dir, logger)

    print(f"\nUpload complete!")
    print(f"  Success: {success_count}")
    print(f"  Errors: {error_count}")
    print(f"  Report: {report_file}")
    print(f"  Log: {log_file}")


if __name__ == "__main__":
    main()
