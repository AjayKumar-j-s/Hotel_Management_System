# booking.py
class Booking:
    def __init__(self, booking_id, customer, room, start_date, end_date):
        self.booking_id = booking_id
        self.customer = customer
        self.room = room
        self.start_date = start_date
        self.end_date = end_date

    def __str__(self):
        return f"Booking #{self.booking_id} for {self.customer.name} in Room {self.room.room_id} from {self.start_date} to {self.end_date}"
