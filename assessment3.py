def sort_employees(employees):
    return employees[1]


employees = [
    ["john", 10, 20000], 
    ["doe", 19, 100000]
]
employees.sort(key=sort_employees)
print(employees)