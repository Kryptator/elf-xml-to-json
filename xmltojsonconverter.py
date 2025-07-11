import os
import json
import xml.etree.ElementTree as ET
import copy

repo_root = os.path.dirname(os.path.abspath(__file__))
xml_folder = os.path.join(repo_root, "raw_game_data", "xml")
json_folder = xml_folder   # JSONs landen im gleichen Ordner

template_folder = os.path.join(repo_root, "templates")
template_file1 = os.path.join(template_folder, "template1.json")
template_file2 = os.path.join(template_folder, "template2.json")

# Load JSON templates
def load_json(filepath):
    with open(filepath, encoding="utf-8") as f:
        return json.load(f)

template1 = load_json(template_file1)
template2 = load_json(template_file2)

def xml_attributes(elem):
    """
    Converts XML element attributes into a dictionary.
    """
    return elem.attrib

def parse_team(team_elem):
    """
    Parses a <team> element into a dict.
    """
    team_dict = {
        "_attributes": team_elem.attrib
    }

    # Find <player> elements under this team
    players = []
    for player_elem in team_elem.findall("player"):
        player_dict = {
            "_attributes": player_elem.attrib
        }
        # Look for child elements under <player> (e.g. rcv, rush, etc.)
        for child in list(player_elem):
            player_dict[child.tag] = {
                "_attributes": child.attrib
            }
        players.append(player_dict)

    if players:
        team_dict["player"] = players

    return team_dict

for filename in os.listdir(xml_folder):
    if not filename.endswith(".xml"):
        continue

    xml_path = os.path.join(xml_folder, filename)
    json_filename = filename.replace(".xml", ".json")
    json_path = os.path.join(json_folder, json_filename)

    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()

        fbgame_elem = root
        venue_elem = fbgame_elem.find("venue")
        team_elems = fbgame_elem.findall("team")

        # Parse venue attributes
        venue_attrs = xml_attributes(venue_elem)

        # ------- MAPPING TO OLD FIELD NAMES -------
        if "visitorid" in venue_attrs:
            venue_attrs["visid"] = venue_attrs.pop("visitorid")
        if "visitor" in venue_attrs:
            venue_attrs["visname"] = venue_attrs.pop("visitor")
        if "home" in venue_attrs:
            venue_attrs["homename"] = venue_attrs.pop("home")

        venue_dict = {
            "_attributes": venue_attrs
        }

        # Parse all teams
        teams = []
        for team_elem in team_elems:
            team_dict = parse_team(team_elem)
            teams.append(team_dict)

        # Build JSON object from template
        json_data = copy.deepcopy(template1)
        json_data["fbgame"]["venue"] = venue_dict
        json_data["fbgame"]["team"] = teams

        # Fill any missing keys from template2
        def fill_missing(template_obj, data_obj):
            if isinstance(template_obj, dict):
                for key in template_obj:
                    if key not in data_obj:
                        data_obj[key] = template_obj[key]
                    else:
                        fill_missing(template_obj[key], data_obj[key])
            elif isinstance(template_obj, list):
                # Skip lists for simplicity
                pass

        fill_missing(template2["fbgame"], json_data["fbgame"])

        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)

        print(f"✅ Converted {filename} → {json_filename}")

    except Exception as e:
        print(f"❌ Error converting {filename}: {e}")

print("🎉 Conversion complete.")