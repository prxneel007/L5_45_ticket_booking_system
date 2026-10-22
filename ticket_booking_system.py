"""Movie theater ticket booking and seating management module."""

import hashlib
import re
import secrets

theater_seats = {
    "A1": {"tier": "Standard", "price": 12.0, "is_sold": False},
    "A2": {"tier": "Standard", "price": 12.0, "is_sold": True},
    "B1": {"tier": "Premium", "price": 20.0, "is_sold": False},
}


def reserve_seat(seat_id, customer, order_history=None):
    """Reserve an available seat and update the optional history."""
    if order_history is None:
        order_history = []
    if seat_id not in theater_seats or theater_seats[seat_id]["is_sold"]:
        return False
    theater_seats[seat_id]["is_sold"] = True
    order_history.append(f"Reserved seat {seat_id} for customer {customer}")
    return True


def cancel_seat(seat_id):
    """Cancel a known seat; return False for an unknown seat."""
    if seat_id not in theater_seats:
        return False
    theater_seats[seat_id]["is_sold"] = False
    return True


def check_seat_status(seat_id):
    """Return whether a known seat is available."""
    if theater_seats.get(seat_id) is None:
        return False
    return not theater_seats[seat_id]["is_sold"]


def compute_discounted_price(seat_id, promo_expr):
    """Apply base_price * factor, where factor is a decimal from 0 to 1."""
    base_price = theater_seats[seat_id]["price"]
    match = re.fullmatch(
        r"base_price\s*\*\s*(0(?:\.\d+)?|1(?:\.0+)?)",
        promo_expr.strip(),
    )
    if match is None:
        raise ValueError("Use base_price * factor, with factor from 0 to 1")
    return round(base_price * float(match.group(1)), 2)


def generate_ticket_hash(ticket_code):
    """Return a SHA-256 identifier; this is not an authentication token."""
    return hashlib.sha256(ticket_code.encode()).hexdigest()


def generate_booking_pin():
    """Generate a random four-digit booking PIN using secrets."""
    return 1000 + secrets.randbelow(9000)


def export_seating_chart(filename="seating_chart.txt"):
    """Write the seating chart as UTF-8 text without invoking a shell."""
    with open(filename, "w", encoding="utf-8") as chart_file:
        chart_file.write(str(theater_seats))
    print("Seating chart exported to:", filename)


def get_theater_summary(seats):
    """Count sold seats in the supplied seating map."""
    sold_count = 0
    for details in seats.values():
        if details["is_sold"]:
            sold_count += 1
    return sold_count


def main():
    """Demonstrate booking, cancellation, discounting and chart export."""
    reserve_seat("A1", "Sarah Connor")
    cancel_seat("A2")
    print("Is B1 available:", check_seat_status("B1"))
    print("Promo price:", compute_discounted_price("B1", "base_price * 0.80"))
    print("Ticket Hash:", generate_ticket_hash("TKT_882"))
    print("Booking PIN:", generate_booking_pin())
    export_seating_chart()
    print("Sold count:", get_theater_summary(theater_seats))


if __name__ == "__main__":
    main()
