# view table
# make reservation
# view reservations
import csv
import os
tables = [
    {'number': 1, 'seats': 3},
    {'number': 2, 'seats': 6},
    {'number': 3, 'seats': 9},
    {'number': 4, 'seats': 12},
    {'number': 5, 'seats': 15}
]

def view_tables(tables, reservations, date=None, start_time=None, end_time=None):
    for table in tables:
        print(table)

# view_tables(tables)

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

#Function for cancelling reservations
def cancel_reservation(reservations_file):
    name = input("Enter your name: ")
    reserved_date = input("Enter the date of reservation: ")

    try:
        with open(reservations_file, 'r') as file:
            reader = csv.reader(file)
            reservations = list(reader)

        current_reservations = [row for row in reservations if not (row[1] == name and row[4] == reserved_date)]
        with open(reservations_file, 'w', newline='') as file:
             writer = csv.writer(file)
             writer.writerows(current_reservations)
        if len(current_reservations) == len(reservations):
            print("No matching reservation found.")
        else:
            print(f"Reservation for {name} on {reserved_date} has been cancelled.")
            pass
    except Exception as e:
        print(f"Error canceling reservation: {e}")
        pass
#Function to view reservations
def view_reservations(reservations_file):
    try:
        with open(reservations_file, 'r') as file:
            reader = csv.reader(file)
            reservations = list(reader)
            print(reservations)
            # reservations = []
            if reservations:
                reserved_tables = [reservation for reservation in reservations if reservation[reservations]]
                print(reserved_tables)
            if not reservations:
                print("No reservations found.")
            pass
            # for reservation in reservations:
                
    except Exception as e:
        print(f"Error reading reservations: {e}")
        pass

def modify_reservations(reservation):
    table_number = int(input("Enter table number to modify resrvations: "))
    name = input("Enter current reservation name: ")
    date = input("Enter current reservation date (YYY-MM-DD)")

    with open(reservations_file, mode = 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        reservations = list(reader)
    for res in reservations:
        if res[headers.index('Table Number')] == table_number and res[headers.index('Name')] == name and res[headers.index('Date')] == date:
            print(res)
            # print("Reservation Found")
        
            new_name = input("Enter new name: ")
            while True:
                try:
                    new_contact = int(input("Enter new phone number: "))
                    break
                except ValueError:
                    print("Invalid input")
            while True:
                try:
                    new_party_size = int(input("Enter number of people: "))
                    break
                except ValueError:
                    print("Invalid input")
            new_date = input("Enter the new date of resservation: ")
            new_start_time = input("Enter new reservation start time (HH:MM): ")
            new_end_time = input("Enter new reservation end time (HH:MM): ")
            # if res[headers.index('New Name')] == new_name
        # print(headers)

        
def display():
    Reservations = reservations_file

    while True:
        print("Reservation System")
        print("1. Make reservation")
        print("2. View reservation")
        print("3. Cancel reservation")
        print("4. Modify reservation")
        print("5. Exit")
                
        choice = input("select: ")

        if choice == "1":
            make_reservation(tables, reservations_file)

        elif choice == "2":
            view_reservations(reservations_file)

        elif choice == "3":
            cancel_reservation(reservations_file)
        elif choice == "4":
            break 
        else:
            print("Invalid choice")


# modify_reservations(reservations_file)
# display()
make_reservation(tables, reservations_file)