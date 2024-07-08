#Creating a List of Employees in an Organization
Employees = [
    {
        "name": "Deborah Olaboye",
     "details":      {
        "age": 55,
        "position": "Chief Executive Officer",
        "tasks": [
            "Strategic Planning",
            "Corporate Governance",
        ]
    }},
        {
        "name": "Ruth George",
     "details":      {
        "age": 45,
        "position": "Chief Financial Officer",
        "tasks": [
            "Financial Planning",
            "Budget Management",
        ]
    }},
        {
        "name": "Joshua Okeke",
     "details":      {
        "age": 55,
        "position": "Marketing Manager",
        "tasks": [
            "Market Research",
            "Campaign Management",
        ]
    }},
        {
        "name": "Deby Olaboye",
     "details":      {
        "age": 35,
        "position": "Software Developer",
        "tasks": [
            "System Design",
            "Coding",
        ]
    }},
        {
        "name": "Rachael",
     "details":      {
        "age": 47,
        "position": "Human Resources Officer",
        "tasks": [
            "Manage the recruitment process",
            "Address Employee Issues",
        ]
    }},
    ]

#employee4 = (Employees[3]["details"]["tasks"])
#print(employee4)

#print(Employees)

#for employee in Employees:
#    print (employee["name"].upper())


def employees():
    for employee in Employees:
        yield (employee["name"].upper())

employees = ["Deborah", "Ruth", "Joshua", "Deby", "Rachael"]
print(employees(Employees))

# employee_list = [Employees]
# employee_list = iter(employees)
# print(next(iterator))