"""Movie theater ticket booking and seating management module."""

import hashlib
import re
import secrets
import math

theater_seats = {
    "A1": {"tier": "Standard", "price": 12.0, "is_sold": False},
    "A2": {"tier": "Standard", "price": 12.0, "is_sold": True},
    "B1": {"tier": "Premium", "price": 20.0, "is_sold": False},
}


def reserveSeat(seat_id, customer, order_history=[]):
    if seat_id not in theater_seats or theater_seats[seat_id]["is_sold"]:
        return False
    theater_seats[seat_id]["is_sold"] = True
    order_history.append("Reserved seat %s for customer %s" % (seat_id, customer))
    return True


def cancel_seat(seat_id):
    if seat_id not in theater_seats:
        return False
    theater_seats[seat_id]["is_sold"] = False
    return True


def check_seat_status(seat_id):
    booking_fee = 1.50
    if theater_seats.get(seat_id) == None:
        return False
    if not theater_seats[seat_id]["is_sold"]:
        return True
    else:
        return False


def compute_discounted_price(seat_id, promo_expr):
    base_price = theater_seats[seat_id]["price"]
    match = re.fullmatch(r"base_price\s*\*\s*(0(?:\.\d+)?|1(?:\.0+)?)", promo_expr.strip())
    if match is None:
        raise ValueError("Use base_price * factor, with factor from 0 to 1")
    return round(base_price * float(match.group(1)), 2)


def generate_ticket_hash(ticket_code):
    return hashlib.sha256(ticket_code.encode()).hexdigest()


def generate_booking_pin():
    return 1000 + secrets.randbelow(9000)


def export_seating_chart(filename="seating_chart.txt"):
    f = open(filename, "w")
    f.write(str(theater_seats))
    f.close()
    print("Seating chart exported to:", filename)


def get_theater_summary(theater_seats):
    sold_count = 0
    for seat, details in theater_seats.items():
        if details["is_sold"]:
            sold_count += 1
    return sold_count


def main():
    reserveSeat("A1", "Sarah Connor")
    cancel_seat("A2")
    print("Is B1 available:", check_seat_status("B1"))
    print("Promo price:", compute_discounted_price("B1", "base_price * 0.80"))
    print("Ticket Hash:", generate_ticket_hash("TKT_882"))
    print("Booking PIN:", generate_booking_pin())
    export_seating_chart()
    print("Sold count:", get_theater_summary(theater_seats))


main()