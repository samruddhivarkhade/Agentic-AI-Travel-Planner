from typing import Dict

# Approximate daily expense (food + local transport)
DAILY_EXPENSE = 800

def estimate_budget(
    flight: Dict,
    hotel: Dict,
    days: int
) -> Dict:
    """
    Estimate total trip budget
    """
    flight_cost = flight.get("price", 0)
    hotel_cost = hotel.get("price_per_night", 0) * days
    local_expense = DAILY_EXPENSE * days

    total_cost = flight_cost + hotel_cost + local_expense

    return {
        "flight_cost": flight_cost,
        "hotel_cost": hotel_cost,
        "local_expense": local_expense,
        "total_cost": total_cost
    }

# Testing the tool directly
if __name__ == "__main__":
    sample_flight = {"price": 4800}
    sample_hotel = {"price_per_night": 3200}
    days = 3

    budget = estimate_budget(sample_flight, sample_hotel, days)
    print("Budget Breakdown:")
    print(budget)
