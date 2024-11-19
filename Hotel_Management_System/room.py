# room.py
class Room:
    def __init__(self, room_id, room_type, rate):
        self.room_id = room_id
        self.room_type = room_type
        self.rate = rate
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Booked"
        return f"Room {self.room_id} ({self.room_type}) - ${self.rate} per night, Status: {status}"
