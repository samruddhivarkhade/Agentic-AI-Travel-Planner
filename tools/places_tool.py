import json
from pathlib import Path
from typing import Dict, List

DATA_DIR = Path("data")

def load_places() -> List[Dict]:
    """Load places data from JSON file"""
    with open(DATA_DIR / "places.json", "r", encoding="utf-8") as file:
        return json.load(file)

def discover_places(
    city: str,
    interest_type: str = None,
    top_n: int = 5
) -> List[Dict]:
    """
    Discover top-rated places based on city and interest type
    """
    places = load_places()

    filtered_places = [
        place for place in places
        if place["city"].lower() == city.lower()
    ]

    if interest_type:
        filtered_places = [
            place for place in filtered_places
            if place["type"].lower() == interest_type.lower()
        ]

    # Sort by rating (highest first)
    filtered_places.sort(key=lambda x: x["rating"], reverse=True)

    return filtered_places[:top_n]

# Testing the tool directly
if __name__ == "__main__":
    results = discover_places("Goa", interest_type="fort", top_n=3)
    if results:
        print("Top Places:")
        for place in results:
            print(place)
    else:
        print("No places found.")
