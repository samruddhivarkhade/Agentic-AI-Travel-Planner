""" 
from langchain.tools import tool

from tools.flight_tool import search_cheapest_flight
from tools.hotel_tool import recommend_hotel
from tools.places_tool import discover_places
from tools.weather_tool import get_weather
from tools.budget_tool import estimate_budget


@tool("Flight Search Tool")
def flight_search_tool(source: str, destination: str):
   
    return search_cheapest_flight(source=source, destination=destination)


@tool("Hotel Recommendation Tool")
def hotel_recommendation_tool(city: str, min_stars: int, max_price: int):
    
    return recommend_hotel(
        city=city,
        min_stars=min_stars,
        max_price=max_price
    )


@tool("Places Discovery Tool")
def places_discovery_tool(city: str, interest_type: str, top_n: int):
    
    return discover_places(
        city=city,
        interest_type=interest_type,
        top_n=top_n
    )


@tool("Weather Lookup Tool")
def weather_lookup_tool(city: str, days: int):
   
    return get_weather(city=city, days=days)


@tool("Budget Estimation Tool")
def budget_estimation_tool(flight: dict, hotel: dict, days: int):
    
    return estimate_budget(flight=flight, hotel=hotel, days=days)


TOOLS = [
    flight_search_tool,
    hotel_recommendation_tool,
    places_discovery_tool,
    weather_lookup_tool,
    budget_estimation_tool
]

"""
""" 
# Define your travel tools
TOOLS = [
    {
        "name": "search_flights",
        "func": lambda query: f"Searching flights for: {query}",
        "description": "Search for flights between cities."
    },
    {
        "name": "search_hotels",
        "func": lambda query: f"Searching hotels for: {query}",
        "description": "Search for hotels in a city with budget info."
    },
    {
        "name": "suggest_places",
        "func": lambda query: f"Suggesting places to visit for: {query}",
        "description": "Suggest tourist attractions in a city."
    }
]
"""

from langchain.tools import tool


@tool
def get_flight_info(source: str, destination: str) -> str:
    """Returns cheapest flight information between two cities."""
    return f"Cheapest flight from {source} to {destination} costs ₹4,500."


@tool
def get_hotel_info(city: str) -> str:
    """Returns budget hotel options in the city."""
    return f"Budget hotel in {city}: ₹1,200 per night."


@tool
def get_places_to_visit(city: str) -> str:
    """Returns top tourist places in the city."""
    return f"Top places in {city}: Baga Beach, Fort Aguada, Dudhsagar Falls."


@tool
def get_weather(city: str) -> str:
    """Returns current weather info of the city."""
    return f"Weather in {city}: Sunny, 30°C."


@tool
def estimate_budget(days: int) -> str:
    """Returns estimated total budget."""
    return f"Estimated budget for {days} days: ₹18,000."


TOOLS = [
    get_flight_info,
    get_hotel_info,
    get_places_to_visit,
    get_weather,
    estimate_budget
]
