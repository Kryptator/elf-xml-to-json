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

By default, the newly converted JSONs follow the correct naming pattern where the home team comes first:

{Home}{Visitor}{Season}{Round}.json

Example:
- Game ID: `PWCC2101` → filename: `pwcc2101.json`

This matches the naming convention already used in the original JSON files in the repo.

**Therefore, no reordering of home/visitor codes is required when naming new JSONs.**

If you want to ensure all filenames strictly follow the naming pattern, you can run the rename script. It reads the game ID inside each JSON file and renames the file accordingly to:

{Home}{Visitor}{Season}{Round}.json


This guarantees that all JSON filenames remain consistent.

---

## ✅ Important Notes

- **Templates are already provided.**  
They ensure all JSONs follow the exact same structure and contain no unwanted default values.

- **File names matter.**  
The templates must be named:
