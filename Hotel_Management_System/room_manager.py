# room_manager.py
import heapq

class RoomManager:
    def __init__(self):
        self.available_rooms = []

    def add_room(self, room):
        if room.is_available:
            heapq.heappush(self.available_rooms, (room.rate, room))

    def get_cheapest_room(self):
        return heapq.heappop(self.available_rooms)[1] if self.available_rooms else None

    def refresh_rooms(self, room_list):
        self.available_rooms = [(room.rate, room) for room in room_list if room.is_available]
        heapq.heapify(self.available_rooms)
