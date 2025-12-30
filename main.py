import json
from pathlib import Path

DATA_DIR = Path("data")

def load_json(filename):
    """Load JSON file and return data"""
    try:
        with open(DATA_DIR / filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception as e:
        print(f"Error loading {filename}: {e}")
        return []

def test_data_loading():
    flights = load_json("flights.json")
    hotels = load_json("hotels.json")
    places = load_json("places.json")

    print("Flights Data:", flights)
    print("Hotels Data:", hotels)
    print("Places Data:", places)

if __name__ == "__main__":
    test_data_loading()
