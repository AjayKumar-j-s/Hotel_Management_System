# main.py
from .room import Room
from .booking import Booking
from .room_manager import RoomManager
from .customer import *
import sqlite3
from datetime import datetime

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

def add_sample_rooms(room_manager):
    rooms = [Room(1, "Single", 100), Room(2, "Double", 150), Room(3, "Suite", 300)]
    for room in rooms:
        room_manager.add_room(room)

def owner_menu(room_manager):
    while True:
        print("\nOwner Menu")
        print("1. Add Room")
        print("2. Update Room Availability")
        print("3. View All Bookings")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            room_id = int(input("Enter room ID: "))
            room_type = input("Enter room type: ")
            rate = float(input("Enter room rate: "))
            room = Room(room_id, room_type, rate)
            room_manager.add_room(room)
            print(f"Room {room_id} added successfully.")
        
        elif choice == '2':
            room_id = int(input("Enter room ID to update: "))
            room = next((r for rate, r in room_manager.available_rooms if r.room_id == room_id), None)
            if room:
                room.is_available = not room.is_available
                status = "available" if room.is_available else "booked"
                print(f"Room {room_id} status updated to {status}.")
            else:
                print("Room not found.")
        
        elif choice == '3':
            print("\nAll Bookings:")
            # Fetch and display bookings from the database (assuming database holds booking data)
            conn = sqlite3.connect('database.db')
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Bookings")
            for row in cursor.fetchall():
                print(row)
            conn.close()
        
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def customer_menu(room_manager):
    while True:
        print("\nCustomer Menu")
        print("1. View Available Rooms")
        print("2. Book a Room")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nAvailable Rooms:")
            for rate, room in room_manager.available_rooms:
                if room.is_available:
                    print(room)

        elif choice == '2':
            name = input("Enter your name: ")
            contact = input("Enter your contact: ")
            customer = Customer(None, name, contact)
            room = room_manager.get_cheapest_room()
            if room:
                room.is_available = False  # Mark room as booked
                start_date = input("Enter start date (YYYY-MM-DD): ")
                end_date = input("Enter end date (YYYY-MM-DD): ")
                booking = Booking(1, customer, room, start_date, end_date)
                print("\nBooking Confirmed:")
                print(booking)
                # Save booking to database
                conn = sqlite3.connect('database.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO Customers (name, contact) VALUES (?, ?)", (customer.name, customer.contact))
                cursor.execute("INSERT INTO Bookings (customer_id, room_id, start_date, end_date) VALUES (?, ?, ?, ?)", 
                               (1, room.room_id, start_date, end_date))
                conn.commit()
                conn.close()
                room_manager.refresh_rooms([room for rate, room in room_manager.available_rooms])  # Refresh room list after booking
            else:
                print("No rooms available.")

        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def main():
    setup_database()
    room_manager = RoomManager()
    add_sample_rooms(room_manager)

    while True:
        print("\nWelcome to the Hotel Booking System")
        print("1. Owner Login")
        print("2. Customer Login")
        print("3. Exit")
        user_type = input("Enter your choice: ")

        if user_type == '1':
            owner_menu(room_manager)
        elif user_type == '2':
            customer_menu(room_manager)
        elif user_type == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
