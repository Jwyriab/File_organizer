#!/usr/bin/env python3
"""
File Organizer - by Jaweria Batool
Automatically sorts files in a folder by their type into subfolders.
Usage: python3 file_organizer.py -d /path/to/folder
       python3 file_organizer.py -d /path/to/folder --dry-run
"""

import os
import shutil
import argparse
from datetime import datetime

# File type categories
CATEGORIES = {
    "Images":     [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".ico"],
    "Videos":     [".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm"],
    "Audio":      [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Documents":  [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf", ".md"],
    "Spreadsheets": [".xls", ".xlsx", ".csv", ".ods"],
    "Slides":     [".ppt", ".pptx", ".odp"],
    "Archives":   [".zip", ".rar", ".tar", ".gz", ".7z", ".bz2"],
    "Code":       [".py", ".js", ".html", ".css", ".java", ".c", ".cpp",
                   ".sh", ".json", ".xml", ".php", ".ts"],
    "Executables":[".exe", ".msi", ".deb", ".appimage"],
    "Fonts":      [".ttf", ".otf", ".woff", ".woff2"],
}


def get_category(extension):
    """Return the category folder for a given file extension."""
    ext = extension.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"


def organize(folder, dry_run=False):
    """Organize files in the given folder."""
    if not os.path.isdir(folder):
        print(f"[-] Folder not found: {folder}")
        return

    files = [f for f in os.listdir(folder)
             if os.path.isfile(os.path.join(folder, f))]

    if not files:
        print("[~] No files found in folder.")
        return

    moved = 0
    skipped = 0
    summary = {}

    print("=" * 55)
    print("         FILE ORGANIZER")
    print("         by Jaweria Batool")
    print("=" * 55)
    print(f"[*] Folder   : {folder}")
    print(f"[*] Files    : {len(files)} found")
    print(f"[*] Mode     : {'DRY RUN (no changes made)' if dry_run else 'LIVE'}")
    print(f"[*] Started  : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55 + "\n")

    for filename in files:
        # Skip the script itself
        if filename == os.path.basename(__file__):
            continue

        _, ext = os.path.splitext(filename)
        if not ext:
            category = "Other"
        else:
            category = get_category(ext)

        src = os.path.join(folder, filename)
        dest_folder = os.path.join(folder, category)
        dest = os.path.join(dest_folder, filename)

        # Handle duplicate filenames
        if os.path.exists(dest):
            name, extension = os.path.splitext(filename)
            dest = os.path.join(dest_folder, f"{name}_duplicate{extension}")

        if dry_run:
            print(f"  [PREVIEW] {filename} → {category}/")
        else:
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(src, dest)
            print(f"  [MOVED]   {filename} → {category}/")

        summary[category] = summary.get(category, 0) + 1
        moved += 1

    print("\n" + "=" * 55)
    print(f"[*] {'Would move' if dry_run else 'Moved'} {moved} file(s)\n")
    print("  Summary:")
    for cat, count in sorted(summary.items()):
        print(f"    {cat:<20} {count} file(s)")
    print("=" * 55)

    if dry_run:
        print("\n[~] This was a dry run. No files were moved.")
        print("[~] Run without --dry-run to apply changes.")


def main():
    parser = argparse.ArgumentParser(
        description="File Organizer — Sort files into folders by type"
    )
    parser.add_argument(
        "-d", "--directory",
        required=True,
        help="Path to the folder you want to organize"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview what would happen without moving any files"
    )
    args = parser.parse_args()
    organize(args.directory, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
