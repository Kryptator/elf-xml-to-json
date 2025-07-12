import os
import json

repo_root = os.path.dirname(os.path.abspath(__file__))
xml_folder = os.path.join(repo_root, "raw_game_data", "xml")

files = [f for f in os.listdir(xml_folder) if f.endswith(".json")]

rename_count = 0

for filename in files:
    old_path = os.path.join(xml_folder, filename)

    try:
        with open(old_path, encoding="utf-8") as f:
            data = json.load(f)

        fbgame = data.get("fbgame", {})
        venue = fbgame.get("venue", {})
        attrs = venue.get("_attributes", {})
        gameid = attrs.get("gameid", "").upper()

        if not gameid or len(gameid) < 8:
            print(f"⚠️ Skipping {filename}: Missing or invalid gameid.")
            continue

        visitor = gameid[0:2].lower()
        home = gameid[2:4].lower()
        season = gameid[4:6]
        round_or_week = gameid[6:].lower()

        # Overwrite naming to match OLD JSONs (Visitor first!)
        new_filename = f"{visitor}{home}{season}{round_or_week}.json"

        if new_filename != filename:
            new_path = os.path.join(xml_folder, new_filename)

            if os.path.exists(new_path):
                print(f"⚠️ Skipping rename for {filename}: target {new_filename} already exists!")
                continue

            os.rename(old_path, new_path)
            print(f"✅ Renamed {filename} → {new_filename}")
            rename_count += 1

    except Exception as e:
        print(f"❌ Error processing {filename}: {e}")

print(f"\nTotal files renamed in xml-folder: {rename_count}")