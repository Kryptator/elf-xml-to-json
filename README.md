# ✅ ELF Game Data Conversion – Complete Guide

This guide explains how to convert all ELF game data from XML to JSON, ensuring all JSON files match the exact structure used in the repository.

---

## ✅ What’s Included

This repository package already includes:

- All Python scripts required for:
  - comparing XML and JSON files
  - moving duplicate XMLs
  - converting XML files to JSON
  - renaming newly converted JSONs

- Two cleaned template JSON files:
  - `templates/template1.json`
  - `templates/template2.json`

No additional setup or manual template creation is needed.

---

## ✅ How It Works

### 1. Compare XML and JSON

First, check which games already exist as both XML and JSON, and which exist only as XML.

Run the comparison script:

- It lists all duplicate games.
- It identifies XML files that have not yet been converted.

---

### 2. Move Duplicate XMLs

To avoid duplicate data, move any XML files that already exist as JSON into a separate folder.

Run the move script:

- It places duplicates into a subfolder:

raw_game_data/xml/duplicates


---

### 3. Convert XML to JSON

Run the conversion script:

- It converts all remaining XML files to JSON.
- It ensures all fields are present in the JSON, even if they’re empty.
- It writes all new JSONs into:

raw_game_data/xml/


Note: The converted JSON files are initially stored in the XML folder to keep them separate from the existing JSONs.

---

### 4. Rename New JSONs

The original JSONs in the repo use a specific filename pattern where the **visitor team comes first** in the filename:

{Visitor}{Home}{Season}{Round}.json

Example:
- Game ID: `PWCC2101` → filename: `ccpw2101.json`

However, newly converted JSONs follow a logical convention with **home team first.** To match the repo’s historical naming, you need to rename the new JSONs accordingly.

Run the rename script:

- It scans all new JSONs in:

raw_game_data/xml/

- It renames them into the same visitor-first pattern used by existing JSONs.
- This ensures perfect compatibility with the repo’s existing file names.

---

## ✅ Important Notes

- **Templates are already provided.**  
They ensure all JSONs follow the exact same structure and contain no unwanted default values.

- **File names matter.**  
The templates must be named:
