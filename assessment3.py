def sort_employees(employees, sort_by):
    sort_indices = ["name", "age", "salary"]
    sort_index = sort_indices.index(sort_by)

    sorted_employees = sorted(employees, key=lambda x: x[sort_index])

    return sorted_employees

employees = [
    ["John", 33, 65000],
    ["sarah", 24, 75000],
    ['Josie', 29, 10000],
    ["jason", 26, 55000],
    ["Connor", 25, 110000]
]
sort_by = "age"
a = sort_employees(employees, sort_by)
print(a)