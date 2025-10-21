import requests
import json
from pathlib import Path

RAW_DATA_DIR = Path("data/raw")

def fetch_data(endpoint="people"):
    url = f"https://swapi.dev/api/{endpoint}/"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    
    output_path = RAW_DATA_DIR / f"{endpoint}.json"
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w") as f:
        json.dump(data, f, indent=2)
    return data
