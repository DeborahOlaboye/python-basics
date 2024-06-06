from datetime import datetime
Current_year = datetime.now().year
FN = input("What is your First Name?")
LN = input("What is your Last Name?")
year_of_birth = abs(int(input("In what year were you born?")))
age = Current_year - year_of_birth
print(f"Hello, {FN} {LN}, you are {age} years old")