import json
from pathlib import Path
from typing import Dict, List, Optional

DATA_DIR = Path("data")

def load_hotels() -> List[Dict]:
    """Load hotels data from JSON file"""
    with open(DATA_DIR / "hotels.json", "r", encoding="utf-8") as file:
        return json.load(file)

def recommend_hotel(
    city: str,
    min_stars: int = 3,
    max_price: int = 5000
) -> Optional[Dict]:
    """
    Recommend the best hotel based on city, stars and price
    """
    hotels = load_hotels()

    filtered_hotels = [
        hotel for hotel in hotels
        if hotel["city"].lower() == city.lower()
        and hotel["stars"] >= min_stars
        and hotel["price_per_night"] <= max_price
    ]

    if not filtered_hotels:
        return None

    # Sort: highest stars first, then lowest price
    filtered_hotels.sort(
        key=lambda x: (-x["stars"], x["price_per_night"])
    )

    return filtered_hotels[0]

# Testing the tool directly
if __name__ == "__main__":
    result = recommend_hotel("Goa", min_stars=3, max_price=3000)
    if result:
        print("Recommended Hotel:")
        print(result)
    else:
        print("No suitable hotel found.")
