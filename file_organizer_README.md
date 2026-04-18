# 🗂️ File Organizer

A Python script that automatically sorts files in any folder into categorized subfolders.  
Part of my Python scripting portfolio — developed while applying to Howest University of Applied Sciences, Belgium.

---

## 📌 What It Does

- Scans a folder and sorts files by type automatically
- Creates subfolders: **Images, Videos, Audio, Documents, Code, Archives** and more
- Includes a **dry run mode** — preview changes before moving anything
- Handles **duplicate filenames** safely
- Works on **Linux, Windows, and macOS**

---

## 📂 Categories

| Folder | File Types |
|---|---|
| Images | .jpg .png .gif .svg .webp |
| Videos | .mp4 .mkv .avi .mov |
| Audio | .mp3 .wav .flac .aac |
| Documents | .pdf .docx .txt .md |
| Spreadsheets | .xlsx .csv |
| Slides | .pptx .odp |
| Archives | .zip .rar .tar .gz |
| Code | .py .js .html .css .java |
| Executables | .exe .deb .appimage |
| Other | anything else |

---

## 🚀 Usage

```bash
# Preview first (recommended — no files moved)
python3 file_organizer.py -d /path/to/folder --dry-run

# Actually organize the folder
python3 file_organizer.py -d /path/to/folder
```

### Arguments

| Argument | Description |
|---|---|
| `-d` | Path to the folder to organize |
| `--dry-run` | Preview only, no files moved |

---

## 📋 Example Output

```
=======================================================
         FILE ORGANIZER
         by Jaweria Batool
=======================================================
[*] Folder   : /home/user/Downloads
[*] Files    : 4 found
[*] Mode     : DRY RUN (no changes made)

  [PREVIEW] photo.jpg → Images/
  [PREVIEW] notes.txt → Documents/
  [PREVIEW] script.py → Code/
  [PREVIEW] music.mp3 → Audio/

=======================================================
  Summary:
    Audio                1 file(s)
    Code                 1 file(s)
    Documents            1 file(s)
    Images               1 file(s)
=======================================================
```

---

## 🛠️ Requirements

- Python 3.x
- No external libraries — standard library only

---

## 👩‍💻 About

Built by **Jaweria Batool** — self-taught Python on Ubuntu Linux.  
Cybersecurity enthusiast applying to Howest University, Belgium 🇧🇪
