import random


def run_travel_agent_demo(source, destination, days, budget):
    # Demo datasets
    flights = [
        "IndiGo", "Air India", "Vistara", "SpiceJet"
    ]

    hotels = [
        ("Budget Stay Inn", 1200),
        ("Comfort Suites", 1800),
        ("Grand Palace Hotel", 2500)
    ]

    places = {
        "Goa": ["Baga Beach", "Fort Aguada", "Dudhsagar Falls"],
        "Delhi": ["India Gate", "Red Fort", "Qutub Minar"],
        "Mumbai": ["Gateway of India", "Marine Drive", "Elephanta Caves"],
        "Bangalore": ["Lalbagh", "Cubbon Park", "Bangalore Palace"]
    }

    weather_options = ["Sunny", "Cloudy", "Pleasant", "Warm"]

    selected_flight = random.choice(flights)
    selected_hotel, hotel_price = random.choice(hotels)
    visit_places = places.get(destination, ["Local Sightseeing"])
    weather = random.choice(weather_options)

    estimated_cost = min(budget, (hotel_price * days) + 4500)

    return f"""
================ TRAVEL PLAN ================

✈️ Flight:
{selected_flight} flight from {source} to {destination}
Estimated Cost: ₹4,500

🏨 Hotel:
{selected_hotel}
Price: ₹{hotel_price} per night
Total Stay Cost: ₹{hotel_price * days}

📍 Places to Visit:
{", ".join(visit_places)}

🌤 Weather:
{weather}, around 28–32°C

💰 Estimated Budget:
₹{estimated_cost} for {days} days

========================================================
"""


# Optional: CLI testing (not required for Streamlit)
if __name__ == "__main__":
    print(
        run_travel_agent_demo(
            source="Bangalore",
            destination="Goa",
            days=3,
            budget=20000
        )
    )