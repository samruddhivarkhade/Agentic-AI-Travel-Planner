import json
from pathlib import Path
from typing import Dict, List, Optional

DATA_DIR = Path("data")

def load_flights() -> List[Dict]:
    """Load flights data from JSON file"""
    with open(DATA_DIR / "flights.json", "r", encoding="utf-8") as file:
        return json.load(file)

def search_cheapest_flight(source: str, destination: str) -> Optional[Dict]:
    """
    Search for the cheapest flight between source and destination
    """
    flights = load_flights()

    matching_flights = [
        flight for flight in flights
        if flight["from"].lower() == source.lower()
        and flight["to"].lower() == destination.lower()
    ]

    if not matching_flights:
        return None

    cheapest_flight = min(matching_flights, key=lambda x: x["price"])
    return cheapest_flight

# Testing the tool directly
if __name__ == "__main__":
    result = search_cheapest_flight("Goa", "Bangalore")
    if result:
        print("Cheapest Flight Found:")
        print(result)
    else:
        print("No flights found.")
