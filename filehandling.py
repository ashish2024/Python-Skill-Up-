#===============================================

print("\n--- Exception Handling Example ---")

try:

    number = int(input("Enter a number: "))
    result = 100 / number

    print("Result =", result)

except ZeroDivisionError:

    print("Cannot divide by zero.")

except ValueError:

    print("Please enter a valid number.")

finally:

    print("Execution Completed")

# ==================================================
# MULTIPLE EXCEPTIONS
# ==================================================

print("\n--- Multiple Exceptions ---")

try:

    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print(num1 / num2)

except ValueError:

    print("Only numbers are allowed.")

except ZeroDivisionError:

    print("Division by zero is not allowed.")

# ==================================================
# ==================================================

def check_age(age):

    if age < 18:
        raise Exception("Not Eligible")

    print("Eligible")


try:

    age = int(input("\nEnter Age: "))
    check_age(age)

except Exception as e:

    print(e)

# ==================================================

print("\n--- File Write Example ---")

file = open("student.txt", "w")

file.write("Name : Ashish\n")
file.write("Course : Python\n")
file.write("City : Hyderabad\n")

file.close()

print("Data Written Successfully")


print("\n--- Reading File ---")

file = open("student.txt", "r")

content = file.read()

print(content)

file.close()


print("\n--- Append Data ---")

file = open("student.txt", "a")

file.write("Experience : Fresher\n")

file.close()

print("Data Appended")


print("\n--- Line By Line Read ---")

file = open("student.txt", "r")

for line in file:

    print(line.strip())

file.close()


print("\n--- Employee Record System ---")

employee_file = open("employee.txt", "w")

for i in range(1, 4):

    name = input(f"Enter Employee {i} Name : ")

    employee_file.write(name + "\n")

employee_file.close()

print("Employee Data Saved")

# =
print("\nSaved Employees")

employee_file = open("employee.txt", "r")

for employee in employee_file:

    print(employee.strip())

employee_file.close()

