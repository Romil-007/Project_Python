import datetime
from Project.dine_in_Class import *

def dine_in_menu():
    # Predefined tables with details
    tables_info = {
        1: {"availability": True, "cost": 50},
        2: {"availability": True, "cost": 40},
        3: {"availability": True, "cost": 60},
        4: {"availability": True, "cost": 55}
    }

    booking_system = TableBookingSystem(tables_info)

    while True:
        print("\n===== Hotel Table Booking System =====")
        print("1. Display Available Tables")
        print("2. Display Current Reservations")
        print("3. Book a Table")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            booking_system.display_tables()
        elif choice == "2":
            booking_system.display_reservations()
        elif choice == "3":
            table_number = int(input("Enter the table number you want to book: "))
            date = input("Enter the date (YYYY-MM-DD): ")
            time = input("Enter the time (HH:MM AM/PM): ")
            booking_system.book_table(table_number, date, time)
        elif choice == "4":
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

