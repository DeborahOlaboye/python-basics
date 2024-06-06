#Classes in python are used to represent objects with same attribute

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def change_salary(self,amount):
        self.salary += amount

#String Method
   # def _str_(self):
    #    return f"{self.name} has a salary of: {self.salary}"
#Create Employee Instance
employees = [
    Employee("Alice", 50000),
    Employee("Bob", 60000),
    Employee("Charlie", 70000),
    Employee("Avast", 2000)
] 

#Change the Salaries by 10000
for employee in employees:
    if employee.name != "Avast":
        employee.change_salary(10000)

for employee in employees:
    print(f"{employee.name}'s new salary: {employee.salary}")

#String Method
#for employee in employees:
print(employee)