
import csv
import os
tables = [
    {'number': 1, 'seats': 3},
    {'number': 2, 'seats': 6},
    {'number': 3, 'seats': 9},
    {'number': 4, 'seats': 12},
    {'number': 5, 'seats': 15}
]

reservations_file = 'reservations_file.csv'
#Function for make reservations
def make_reservation(tables, reservations_file):
    name = input("Enter your name: ")
    while True:
        try:
            contact = int(input("Enter your phone number: "))
            break
        except ValueError:
            print("Invalid input")
    while True:
        try:
            party_size = int(input("Enter number of people: "))
            break
        except ValueError:
            print("Invalid input")
    date = input("Enter the date of resservation: ")
    start_time = input("Enter reservation start time (HH:MM): ")
    end_time = input("Enter reservation end time (HH:MM): ")

    available_tables = [table for table in tables if table['seats'] >= party_size]

    if not available_tables:
        print("No available tables for your party size")
        return
    print("Available tables")
    for table in available_tables:
        print(f"Table {table['number']} - Seats: {table['seats']}")

 
    table_number  = int(input("Enter table number to reserve: "))
    if table_number not in [table['number'] for table in available_tables]:
        print("Invalid Table Number")
        return
    new_row = [table_number, name, party_size, date, start_time, end_time]
    
    try:
        with open(reservations_file, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(new_row)
        print(f"Table {table_number} reserved successfully for {name}.")
    except Exception as e:
        print(f"Error making reservation: {e}")
        pass

#Function to view reservations
def view_reservations(reservations_file):
    try:
        with open(reservations_file, 'r') as file:
            reader = csv.reader(file)
            reservations = list(reader)
            print(reservations)
            if reservations:
                for reservation in reservations:
                    print(reservation)
            else:
                print("No reservations found.")
            pass
    except Exception as e:
        print(f"Error reading reservations: {e}")
        pass
#Function to view daily summary
def daily_summary(reservations_file):
    date = input("Enter date of reservation: ")
    try:
        with open(reservations_file, "r") as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
            current_reservations = [row for row in reservations if row[header.index("date")] == date]
            if current_reservations:
                for i in current_reservations:
                    print(i)
                else:
                    print("No reservation found")
    except Exception as e:
        print('Invalid date')
        pass



def modify_reservations(reservations_file):
    date = input("Enter the date of the reservation to modify (format: YYYY-MM-DD): ")
    name = input("Enter the name of the reservation to modify: ")
    table_number = int(input("Enter the table number of the reservation to modify: "))

    try:
        # Read all reservations
        with open(reservations_file, "r", newline='') as file:
            reader = csv.reader(file)
            header = next(reader)
            reservations = list(reader)
        
        # Find and modify the reservation
        reservation_found = False
        for row in reservations:
            if row[header.index("Date")] == date and row[header.index("Name")] == name and row[header.index("Table Number")] == table_number:
                reservation_found = True
                print("Current reservation details:", row)
                
                # Update Details
                new_name = input(f"Enter new name (leave blank to keep current value '{row[header.index('name')]}'): ")
                if new_name:
                    row[header.index('name')] = new_name

                new_table_number = input(f"Enter new table number (leave blank to keep current value '{row[header.index('table_number')]}'): ")
                if new_table_number:
                    row[header.index('table_number')] = new_table_number

                new_date = input(f"Enter new date (leave blank to keep current value '{row[header.index('date')]}'): ")
                if new_date:
                    row[header.index('date')] = new_date
                break

            if reservation_found:    
                # Write the updated reservations back to the CSV file
                with open(reservations_file, "w", newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow(header)
                    writer.writerows(reservations)

                print("Reservation updated successfully.")
            else:
                print("No reservation found for the given details.")
            return

        # If no reservation was found
            
    
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        
def display():
    Reservations = reservations_file

    while True:
        print("Reservation System")
        print("1. Make reservation")
        print("2. View reservation")
        print("3. Modify reservation")
        print("4. View daily summary")
        print("5. Exit")
                
        choice = input("select: ")

        if choice == "1":
            make_reservation(tables, reservations_file)
        elif choice == "2":
            view_reservations(reservations_file)
        elif choice == "3":
            modify_reservations(reservations_file)
        elif choice == "4":
            daily_summary(reservations_file)
        elif choice == "5":
            break 
        else:
            print("Invalid choice")

display()