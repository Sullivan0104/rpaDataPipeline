from pathlib import Path
import json

PROCESSED_DIR = Path("data/processed")

def transform_data(data):
    # Example transformation: extract only names and birth years
    people = [
        {"name": person["name"], "birth_year": person["birth_year"]}
        for person in data.get("results", [])
    ]
    output_path = PROCESSED_DIR / "people_cleaned.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(people, f, indent=2)
    return people
