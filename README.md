Hotel Booking Management System
Description
The Hotel Booking Management System is a console-based Python application designed to manage room bookings for a hotel. It provides functionality for hotel owners to manage rooms and bookings and for customers to view and book available rooms.

The system is powered by SQLite for database management and implements priority queues to optimize room allocation based on rates.

Features
Owner Features:
Add rooms to the hotel database.
Update the availability status of rooms.
View all bookings.
Customer Features:
View all available rooms.
Book the cheapest available room.
Input booking details like name, contact, start, and end dates.


Project Structure
Files:
main.py: Entry point for the application, handles menus and workflow.
room.py: Defines the Room class for managing room details.
room_manager.py: Implements the RoomManager class for managing room allocation using a priority queue.
customer.py: Defines the Customer class for managing customer details.
booking.py: Defines the Booking class for managing booking records.
Database Tables:
Rooms: Stores room details.
Customers: Stores customer information.
Bookings: Stores booking information.


Installation and Setup
Clone the repository:
git clone https://github.com/your-username/hotel-booking-management-system.git
cd hotel-booking-management-system

Install dependencies:
pip install -r requirements.txt
Initialize the database: Run the following command to create necessary tables in database.db:



Add sample rooms: The program automatically initializes the database with three sample rooms. You can add more rooms using the owner menu.

Usage
Run the Application:
Execute the following command to start the system:
python -m HotelManagementSystem.main

Main Menu:
Owner Login: Access owner features.
Customer Login: Access customer features.
Exit: Exit the application.


Code Highlights
Room Manager with Priority Queue:
Rooms are managed using a heap-based priority queue to ensure the cheapest available room is always booked first:

import heapq

class RoomManager:
    def __init__(self):
        self.available_rooms = []

    def add_room(self, room):
        if room.is_available:
            heapq.heappush(self.available_rooms, (room.rate, room))

    def get_cheapest_room(self):
        return heapq.heappop(self.available_rooms)[1] if self.available_rooms else None

Database Integration:
SQLite is used to persist room, customer, and booking data:

def setup_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Rooms (
                        room_id INTEGER PRIMARY KEY, 
                        room_type TEXT, 
                        rate REAL, 
                        is_available BOOLEAN)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Customers (
                        customer_id INTEGER PRIMARY KEY, 
                        name TEXT, 
                        contact TEXT)''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS Bookings (
                        booking_id INTEGER PRIMARY KEY, 
                        customer_id INTEGER, 
                        room_id INTEGER, 
                        start_date TEXT, 
                        end_date TEXT)''')
    conn.commit()
    conn.close()


Future Enhancements
Add authentication for owners and customers.
Implement cancellation and modification of bookings.
Integrate live room availability updates with a web interface.
Add support for generating detailed booking reports.


Contributing
Contributions are welcome! Please fork this repository and submit a pull request.

Author
AJAYKUMAR J S
Feel free to reach out for any questions or suggestions!









