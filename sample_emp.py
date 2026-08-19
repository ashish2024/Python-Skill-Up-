# Day 20 - Employee Management System

employees = {}

while True:

    print("\n1. Add Employee")
    print("2. View Employees")
    print("3. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        emp_id = input("Enter Employee ID: ")
        name = input("Enter Employee Name: ")

        employees[emp_id] = name

        print("Employee Added Successfully")

    elif choice == "2":

        for emp_id, name in employees.items():
            print(emp_id, "-", name)

    elif choice == "3":
        break

    else:
        print("Invalid Choice")