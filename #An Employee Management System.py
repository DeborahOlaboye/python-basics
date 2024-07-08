#An Employee Management System
class Employee:
    def __init__(self, name:str, age: int, position: str, salary: float, ID_number):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self.ID_number = ID_number

    def __str__(self):
        return f"Employee Name: {self.name}\nAge: {self.age}\nPosition: {self.position}\nSalary: {self.salary}"
    
    def update_position(self, new_position: str):
        self.position = new_position

    def update_salary(self, new_salary: float):
        self.salary = new_salary

class Company:
    def __init__(self):
        self.employees = []

    def __add_employee__(self, employee: Employee):
        self.employees.append(employee)

    def __remove_employee__(self, name: str):
        self.employees = [emp for emp in self.employees if emp.name != name]

    def __update_employee__(self, name: str, new_position: str = None, new_salary: float = None):
        employee = self.find_employee(name)
        if employee:
            if new_position:
                employee.update_position(new_position)
            if new_salary:
                employee.update_salary(new_salary)

    def __view_all_employees(self):
        for emp in self.employees:
            print(emp)

    def find_employee(self, name: str):
        for emp in self.employees:
            if emp.name == name:
                return emp
        return None
    
    def find_employee_by_ID(self, ID_number):
        for emp in self.employees:
            if emp.ID_number == ID_number:
                return emp
        return None

    def display():
    company = Company()

    while True:
        print("Employee Management System")
        print("1. Add new employee")
        print("2. Remove an employee")
        print("3. Update employee's details")
        print("4. View all employees")
        print("5. Find an employee by name")
            
        choice = input("select")

        if choice == "1":
            name = input("Enter Employee name")
            age = input(int("Enter Employee age"))
            position = input("Enter employee position")
            salary = input(float("Enter employee salary"))
            new_employee = Employee(name, age, position, salary)
            company.add_employee(new_employee)
            print("Employee has been added successfully")

        elif choice == "2":
            name = input("Enter employee name to be removed")
            company.remove_employee(name)
            print("Employee has been removed successfully")

        elif choice == "3":
            name = input("Enter employee name to be updated")
            new_position = input("Enter the new position")
            increased_salary = input(float("Enter current employee salary"))
            new_salary = float(increased_salary)
            company.update_employee(name, new_position, new_salary)
            print("Employee details has been updated successfully")
            
        elif choice == "4":
            print("Employee List")
            company.view_all_employees()
            
        elif choice == "5":
            name = input("Enter Employee name")
            employee = company.find_employee(name)
            if employee:
                print(employee)
            else:
                print("Invalid")

        else:
            print("Invalid choice")

display()