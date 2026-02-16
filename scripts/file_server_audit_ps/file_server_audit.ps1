<#
================================================================================
File Server Audit Tool (PowerShell)
================================================================================

Description:
    A comprehensive audit tool for Windows file servers designed to support
    migration activities. This script scans directory structures and generates
    CSV reports containing file/folder inventory with NTFS permissions.

    Designed for Windows Server 2012+ (PowerShell 3.0+). No external modules
    required - uses only built-in cmdlets.

Features:
    - Recursive scanning of all folders and subfolders
    - Folder exclusion support with wildcard patterns
    - NTFS permission extraction (inherited vs explicit)
    - File metadata collection (size, extension, last modified date)
    - Owner information retrieval
    - CSV output for easy filtering in Excel
    - Separate error CSV for access-denied scenarios
    - Progress tracking via console and log file

Output:
    - CSV file with file/folder listing and permissions
    - CSV file with errors encountered during scan
    - Log file with detailed scan progress

Usage:
    .\file_server_audit.ps1 -RootPath "D:\Data"
    .\file_server_audit.ps1 -RootPath "D:\Data" -Exclude "D:\Data\Temp"
    .\file_server_audit.ps1 -RootPath "D:\Data" -Exclude "*\Archive","*\Backup"
    .\file_server_audit.ps1 -RootPath "D:\Data" -ExcludeFile "exclusions.txt"
    .\file_server_audit.ps1 -RootPath "D:\Data" -Exclude "*\Temp" -ExcludeFile "exclusions.txt"

Exclusion File Format:
    - One path pattern per line
    - Supports wildcards: * (any characters), ? (single character)
    - Case-insensitive matching
    - Lines starting with # are comments
    - Empty lines are ignored

--------------------------------------------------------------------------------
Author:     Ishak Ahmad (ishak.ahmad@gmail.com)
Created:    2025
Version:    1.0.0
License:    Proprietary - All Rights Reserved

Copyright (c) 2025 Ishak Ahmad. All rights reserved.

This software is proprietary and confidential. Unauthorized copying,
distribution, modification, or use of this software, via any medium,
is strictly prohibited without prior written permission from the author.
================================================================================
#>

[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0, HelpMessage = "Root path to scan (local path or UNC path)")]
    [string]$RootPath,

    [Parameter(Mandatory = $false, HelpMessage = "Folder path patterns to exclude (supports wildcards)")]
    [string[]]$Exclude = @(),

    [Parameter(Mandatory = $false, HelpMessage = "Path to text file containing exclusion patterns")]
    [string]$ExcludeFile
)

Set-StrictMode -Version 2.0
$ErrorActionPreference = "Continue"

# ============================================================================
# Helper Functions
# ============================================================================

function Format-FileSize {
    param([long]$SizeBytes)

    if ($SizeBytes -eq 0) { return "0 B" }

    $units = @("B", "KB", "MB", "GB", "TB")
    $index = 0
    $size = [double]$SizeBytes

    while ($size -ge 1024 -and $index -lt ($units.Length - 1)) {
        $size /= 1024
        $index++
    }

    return "{0:N2} {1}" -f $size, $units[$index]
}

function Write-Log {
    param(
        [string]$Message,
        [string]$Level = "INFO",
        [string]$LogFile
    )

    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logLine = "$timestamp - $Level - $Message"

    # Write to log file
    if ($LogFile) {
        Add-Content -Path $LogFile -Value $logLine -Encoding UTF8
    }

    # Write to console
    switch ($Level) {
        "ERROR"   { Write-Host (Get-Date -Format "HH:mm:ss") "- $Message" -ForegroundColor Red }
        "WARNING" { Write-Host (Get-Date -Format "HH:mm:ss") "- $Message" -ForegroundColor Yellow }
        "INFO"    { Write-Host (Get-Date -Format "HH:mm:ss") "- $Message" }
        "DEBUG"   { Write-Verbose "$timestamp - $Message" }
    }
}

function Load-ExclusionPatterns {
    param(
        [string]$FilePath,
        [string]$LogFile
    )

    $patterns = @()

    if (-not $FilePath) { return $patterns }

    if (-not (Test-Path $FilePath)) {
        Write-Log -Message "Exclusion file not found: $FilePath" -Level "WARNING" -LogFile $LogFile
        return $patterns
    }

    try {
        $lines = Get-Content -Path $FilePath -Encoding UTF8
        foreach ($line in $lines) {
            $line = $line.Trim()

            # Skip empty lines and comments
            if (-not $line -or $line.StartsWith("#")) { continue }

            # Normalize path separators and convert to lowercase
            $pattern = $line.Replace("/", "\").ToLower()
            $patterns += $pattern
            Write-Log -Message "Loaded exclusion pattern: $pattern" -Level "DEBUG" -LogFile $LogFile
        }

        Write-Log -Message "Loaded $($patterns.Count) exclusion pattern(s) from $FilePath" -Level "INFO" -LogFile $LogFile
    }
    catch {
        Write-Log -Message "Error reading exclusion file: $($_.Exception.Message)" -Level "ERROR" -LogFile $LogFile
    }

    return $patterns
}

function Test-PathExcluded {
    param(
        [string]$Path,
        [string[]]$ExclusionPatterns
    )

    if (-not $ExclusionPatterns -or $ExclusionPatterns.Count -eq 0) { return $false }

    # Normalize path for comparison
    $normalizedPath = $Path.Replace("/", "\").ToLower()

    foreach ($pattern in $ExclusionPatterns) {
        # Check wildcard match
        if ($normalizedPath -like $pattern) { return $true }

        # Check prefix match (for exact directory paths)
        $patternTrimmed = $pattern.TrimEnd("\")
        if ($normalizedPath -eq $patternTrimmed -or $normalizedPath.StartsWith("$patternTrimmed\")) {
            return $true
        }
    }

    return $false
}

function Get-NtfsPermissions {
    param(
        [string]$Path,
        [string]$LogFile
    )

    $owner = ""
    $permissionEntries = @()

    try {
        $acl = Get-Acl -LiteralPath $Path -ErrorAction Stop

        # Get owner
        $owner = $acl.Owner
        if (-not $owner) { $owner = "" }

        # Get access rules
        foreach ($ace in $acl.Access) {
            $inheritance = if ($ace.IsInherited) { "Inherited" } else { "Explicit" }

            $entry = "{0}:{1}:{2}({3})" -f $ace.IdentityReference, $ace.AccessControlType, $ace.FileSystemRights, $inheritance
            $permissionEntries += $entry
        }
    }
    catch {
        Write-Log -Message "Error getting permissions for ${Path}: $($_.Exception.Message)" -Level "DEBUG" -LogFile $LogFile
        throw
    }

    $permissionsString = $permissionEntries -join "; "
    return @{ Owner = $owner; Permissions = $permissionsString }
}

# ============================================================================
# Main Script
# ============================================================================

# Validate root path
if (-not (Test-Path -LiteralPath $RootPath)) {
    Write-Host "ERROR: Path does not exist: $RootPath" -ForegroundColor Red
    exit 1
}

if (-not (Test-Path -LiteralPath $RootPath -PathType Container)) {
    Write-Host "ERROR: Path is not a directory: $RootPath" -ForegroundColor Red
    exit 1
}

# Setup output directory
$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$outputDir = Join-Path $scriptDir "output"
if (-not (Test-Path $outputDir)) {
    New-Item -Path $outputDir -ItemType Directory -Force | Out-Null
}

# Setup log file
$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$logFile = Join-Path $outputDir "audit_log_$timestamp.log"

# Banner
Write-Log -Message ("=" * 60) -LogFile $logFile
Write-Log -Message "FILE SERVER AUDIT TOOL (PowerShell)" -LogFile $logFile
Write-Log -Message ("=" * 60) -LogFile $logFile
Write-Log -Message "Root Path: $RootPath" -LogFile $logFile
Write-Log -Message "Output Directory: $outputDir" -LogFile $logFile
Write-Log -Message "PowerShell Version: $($PSVersionTable.PSVersion)" -LogFile $logFile

if ($Exclude.Count -gt 0) {
    Write-Log -Message "CLI Exclusion Patterns: $($Exclude.Count)" -LogFile $logFile
}
if ($ExcludeFile) {
    Write-Log -Message "Exclusion File: $ExcludeFile" -LogFile $logFile
}

Write-Log -Message "Start Time: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')" -LogFile $logFile
Write-Log -Message ("=" * 60) -LogFile $logFile

# Load exclusion patterns from file
$exclusionPatterns = @(Load-ExclusionPatterns -FilePath $ExcludeFile -LogFile $logFile)

# Add CLI exclusion patterns
foreach ($pattern in $Exclude) {
    $normalized = $pattern.Replace("/", "\").ToLower()
    $exclusionPatterns += $normalized
    Write-Log -Message "Added CLI exclusion pattern: $normalized" -Level "DEBUG" -LogFile $logFile
}

if ($exclusionPatterns.Count -gt 0) {
    Write-Log -Message "Total exclusion patterns: $($exclusionPatterns.Count)" -LogFile $logFile
}

# Generate output filenames
$safePathName = $RootPath.Replace("\", "_").Replace(":", "").Replace("/", "_")
if ($safePathName.Length -gt 50) { $safePathName = $safePathName.Substring(0, 50) }

$outputFileData = Join-Path $outputDir "FileAudit_${safePathName}_${timestamp}.csv"
$outputFileErrors = Join-Path $outputDir "FileAudit_${safePathName}_${timestamp}_errors.csv"

# Initialize CSV files with headers using StreamWriter for performance
$dataWriter = New-Object System.IO.StreamWriter($outputFileData, $false, [System.Text.Encoding]::UTF8)
$errorWriter = New-Object System.IO.StreamWriter($outputFileErrors, $false, [System.Text.Encoding]::UTF8)

# Write CSV headers
$dataWriter.WriteLine('"Folder Path","Name","Type","Extension","Size (Bytes)","Size (Formatted)","Last Modified","Owner","Permissions"')
$errorWriter.WriteLine('"Path","Error Type","Error Message","Timestamp"')

# Counters
$folderCount = 0
$fileCount = 0
$errorCount = 0
$excludedCount = 0

# Helper to escape CSV field
function Escape-CsvField {
    param([string]$Value)
    if (-not $Value) { return '""' }
    $escaped = $Value.Replace('"', '""')
    return "`"$escaped`""
}

function Write-DataRow {
    param(
        [string]$FolderPath,
        [string]$Name,
        [string]$Type,
        [string]$Extension,
        [long]$SizeBytes,
        [string]$SizeFormatted,
        [string]$LastModified,
        [string]$Owner,
        [string]$Permissions
    )

    $line = "{0},{1},{2},{3},{4},{5},{6},{7},{8}" -f `
        (Escape-CsvField $FolderPath),
        (Escape-CsvField $Name),
        (Escape-CsvField $Type),
        (Escape-CsvField $Extension),
        $SizeBytes,
        (Escape-CsvField $SizeFormatted),
        (Escape-CsvField $LastModified),
        (Escape-CsvField $Owner),
        (Escape-CsvField $Permissions)

    $dataWriter.WriteLine($line)
}

function Write-ErrorRow {
    param(
        [string]$Path,
        [string]$ErrorType,
        [string]$ErrorMessage
    )

    $line = "{0},{1},{2},{3}" -f `
        (Escape-CsvField $Path),
        (Escape-CsvField $ErrorType),
        (Escape-CsvField $ErrorMessage),
        (Escape-CsvField (Get-Date -Format 'yyyy-MM-dd HH:mm:ss'))

    $errorWriter.WriteLine($line)
}

$startTime = Get-Date

Write-Log -Message "Starting scan of: $RootPath" -LogFile $logFile
if ($exclusionPatterns.Count -gt 0) {
    Write-Log -Message "Exclusion patterns loaded: $($exclusionPatterns.Count)" -LogFile $logFile
}
Write-Log -Message ("-" * 60) -LogFile $logFile

# Process the root folder itself
try {
    $permInfo = Get-NtfsPermissions -Path $RootPath -LogFile $logFile
    $rootItem = Get-Item -LiteralPath $RootPath -Force
    $rootParent = Split-Path -Parent $RootPath
    if (-not $rootParent) { $rootParent = $RootPath }
    $rootName = Split-Path -Leaf $RootPath
    if (-not $rootName) { $rootName = $RootPath }

    Write-DataRow -FolderPath $rootParent -Name $rootName -Type "Folder" `
        -Extension "" -SizeBytes 0 -SizeFormatted "" `
        -LastModified ($rootItem.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")) `
        -Owner $permInfo.Owner -Permissions $permInfo.Permissions

    $folderCount++
}
catch {
    Write-ErrorRow -Path $RootPath -ErrorType $_.Exception.GetType().Name -ErrorMessage $_.Exception.Message
    $errorCount++
    Write-Log -Message "Error accessing root path: $($_.Exception.Message)" -Level "WARNING" -LogFile $logFile
}

# Walk through directory tree
# Use a stack-based approach for better control over exclusions (compatible with PS 3.0)
$dirStack = New-Object System.Collections.Stack
$dirStack.Push($RootPath)

while ($dirStack.Count -gt 0) {
    $currentDir = $dirStack.Pop()

    # Get subdirectories
    try {
        $subdirs = @(Get-ChildItem -LiteralPath $currentDir -Directory -Force -ErrorAction Stop)
    }
    catch {
        Write-ErrorRow -Path $currentDir -ErrorType $_.Exception.GetType().Name -ErrorMessage "Cannot list subdirectories: $($_.Exception.Message)"
        $errorCount++
        Write-Log -Message "Error listing subdirectories of ${currentDir}: $($_.Exception.Message)" -Level "DEBUG" -LogFile $logFile
        $subdirs = @()
    }

    # Process subdirectories (reverse order so stack processes them in original order)
    $nonExcluded = @()
    foreach ($subdir in $subdirs) {
        $folderPath = $subdir.FullName

        if (Test-PathExcluded -Path $folderPath -ExclusionPatterns $exclusionPatterns) {
            $excludedCount++
            Write-Log -Message "Excluded folder: $folderPath" -Level "INFO" -LogFile $logFile
            continue
        }

        $nonExcluded += $subdir
        $folderCount++

        if ($folderCount % 100 -eq 0) {
            Write-Log -Message "Progress: $folderCount folders, $fileCount files scanned, $excludedCount excluded..." -LogFile $logFile
        }

        try {
            $permInfo = Get-NtfsPermissions -Path $folderPath -LogFile $logFile

            Write-DataRow -FolderPath $currentDir -Name $subdir.Name -Type "Folder" `
                -Extension "" -SizeBytes 0 -SizeFormatted "" `
                -LastModified ($subdir.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")) `
                -Owner $permInfo.Owner -Permissions $permInfo.Permissions
        }
        catch {
            Write-ErrorRow -Path $folderPath -ErrorType $_.Exception.GetType().Name -ErrorMessage $_.Exception.Message
            $errorCount++
            Write-Log -Message "Error on folder ${folderPath}: $($_.Exception.Message)" -Level "DEBUG" -LogFile $logFile
        }
    }

    # Push non-excluded subdirectories onto stack (reverse for correct order)
    for ($i = $nonExcluded.Count - 1; $i -ge 0; $i--) {
        $dirStack.Push($nonExcluded[$i].FullName)
    }

    # Process files in current directory
    try {
        $files = @(Get-ChildItem -LiteralPath $currentDir -File -Force -ErrorAction Stop)
    }
    catch {
        Write-ErrorRow -Path $currentDir -ErrorType $_.Exception.GetType().Name -ErrorMessage "Cannot list files: $($_.Exception.Message)"
        $errorCount++
        $files = @()
    }

    foreach ($file in $files) {
        $fileCount++

        if ($fileCount % 500 -eq 0) {
            Write-Log -Message "Progress: $folderCount folders, $fileCount files scanned, $excludedCount excluded..." -LogFile $logFile
        }

        try {
            $permInfo = Get-NtfsPermissions -Path $file.FullName -LogFile $logFile

            Write-DataRow -FolderPath $currentDir -Name $file.Name -Type "File" `
                -Extension $file.Extension.ToLower() -SizeBytes $file.Length `
                -SizeFormatted (Format-FileSize $file.Length) `
                -LastModified ($file.LastWriteTime.ToString("yyyy-MM-dd HH:mm:ss")) `
                -Owner $permInfo.Owner -Permissions $permInfo.Permissions
        }
        catch {
            Write-ErrorRow -Path $file.FullName -ErrorType $_.Exception.GetType().Name -ErrorMessage $_.Exception.Message
            $errorCount++
            Write-Log -Message "Error on file $($file.FullName): $($_.Exception.Message)" -Level "DEBUG" -LogFile $logFile
        }
    }
}

# Close writers
$dataWriter.Flush()
$dataWriter.Close()
$errorWriter.Flush()
$errorWriter.Close()

$endTime = Get-Date
$duration = $endTime - $startTime

# Summary
Write-Log -Message ("-" * 60) -LogFile $logFile
Write-Log -Message ("=" * 60) -LogFile $logFile
Write-Log -Message "SCAN COMPLETE" -LogFile $logFile
Write-Log -Message ("=" * 60) -LogFile $logFile
Write-Log -Message "Folders Scanned: $($folderCount.ToString('N0'))" -LogFile $logFile
Write-Log -Message "Files Scanned: $($fileCount.ToString('N0'))" -LogFile $logFile
Write-Log -Message "Total Items: $(($folderCount + $fileCount).ToString('N0'))" -LogFile $logFile
Write-Log -Message "Folders Excluded: $($excludedCount.ToString('N0'))" -LogFile $logFile
Write-Log -Message "Errors: $($errorCount.ToString('N0'))" -LogFile $logFile
Write-Log -Message "Duration: $duration" -LogFile $logFile
Write-Log -Message "Data File: $outputFileData" -LogFile $logFile
Write-Log -Message "Error File: $outputFileErrors" -LogFile $logFile
Write-Log -Message ("=" * 60) -LogFile $logFile

Write-Host ""
Write-Host "Output saved to: $outputFileData" -ForegroundColor Green
if ($errorCount -gt 0) {
    Write-Host "Errors saved to: $outputFileErrors" -ForegroundColor Yellow
}
