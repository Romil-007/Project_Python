class TableBookingSystem:
    def __init__(self, tables):
        self.tables = tables
        self.reservations = {}

    def display_tables(self):
        print("Available Tables:")
        for table_number, details in self.tables.items():
            status = "Available" if details["availability"] else "Occupied"
            print(f"Table {table_number}: {status} - Cost: {details['cost']}")

    def display_reservations(self):
        print("Current Reservations:")
        for table_number, reservation in self.reservations.items():
            print(f"Table {table_number}: {reservation}")

    def book_table(self, table_number, date, time):
        if table_number in self.tables and self.tables[table_number]["availability"]:
            reservation_key = f"{date} {time}"
            if reservation_key not in self.reservations:
                self.reservations[reservation_key] = {
                    "table": table_number,
                    "date": date,
                    "time": time,
                    "cost": self.tables[table_number]["cost"]
                }
                self.tables[table_number]["availability"] = False  # Mark table as occupied
                print("Reservation successful!")
            else:
                print("Table already reserved for the given date and time.")
        else:
            print("Table not available for reservation.")