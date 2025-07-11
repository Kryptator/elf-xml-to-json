# ✅ ELF Game Data Conversion – Complete Guide

This guide explains how to convert all ELF game data from XML to JSON, ensuring all JSON files match the exact structure used in the /european-league-of-football-data-repository/ repository.

https://github.com/armstjc/european-league-of-football-data-repository

---

## ✅ What’s Included

This repository package already includes:

- All Python scripts required for:
  - comparing XML and JSON files
  - moving duplicate XMLs
  - converting XML files to JSON and rename them


- Two cleaned template JSON files:
  - `templates/template1.json`
  - `templates/template2.json`

No additional setup or manual template creation is needed.

---

## ✅ How It Works

### 1. Compare XML and JSON

      python compare_xml_json.py

First, check which games already exist as both XML and JSON, and which exist only as XML.

Run the comparison script:

- It lists all duplicate games.
- It identifies XML files that have not yet been converted.

---

### 2. Move Duplicate XMLs

      python move_duplicates.py

To avoid duplicate data, move any XML files that already exist as JSON into a separate folder.

Run the move script:

- It places duplicates into a subfolder:

raw_game_data/xml/duplicates


---

### 3. Convert XML to JSON

      python xmltojsonconverter_with_rename.py

Run the conversion script:

- It converts all remaining XML files to JSON.
- It ensures all fields are present in the JSON, even if they’re empty.
- It writes all new JSONs into:

raw_game_data/xml/


Note: The converted JSON files are initially stored in the XML folder to keep them separate from the existing JSONs.

---

### 4. Copy

Copy all newly generated files to raw_game_data/json

## ✅ Important Notes

- **Templates are already provided.**  
They ensure all JSONs follow the exact same structure and contain no unwanted default values.

- **File names matter.**  
The templates must be named:

template1.json

template2.json

and placed in the `templates` folder, as already included in the provided package.

- **No manual edits are required.**  
The scripts handle everything automatically.

---

## ✅ Done!

After following these steps:

✅ All ELF XML files will exist as JSON.  
✅ All JSONs will match the repo’s original data model perfectly.  
✅ No dummy stats or unexpected data remain.  
✅ All file names follow a unified naming convention matching the repo.

---

**Short summary:**  
Run the scripts in order – compare, move duplicates, convert, rename – and your XML data will become perfect JSON files ready for the repo.

