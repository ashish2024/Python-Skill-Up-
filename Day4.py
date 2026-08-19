# ==========================================
# DAY 4 : FUNCTIONS + LOOPS + CONDITIONS
# ==========================================

print("================================")
print(" Welcome to Day 4 Practice ")
print("================================")


# ------------------------------------------
# 1. Simple Function
# ------------------------------------------

def greet():
    print("\nHello Ashish!")
    print("Welcome to Python Functions.")

greet()


# ------------------------------------------
# 2. Function with Parameters
# ------------------------------------------

def student_details(name, age):
    print("\nStudent Details")
    print("Name :", name)
    print("Age  :", age)

student_details("Ashish", 25)


# ------------------------------------------
# 3. Function with Return Value
# ------------------------------------------

def add_numbers(a, b):
    return a + b

result = add_numbers(20, 30)

print("\nAddition Result =", result)


# ------------------------------------------
# 4. Even or Odd Checker
# ------------------------------------------

def check_even_odd(number):

    if number % 2 == 0:
        return "Even Number"

    return "Odd Number"


num = int(input("\nEnter any number: "))

print(check_even_odd(num))


# ------------------------------------------
# 5. Multiplication Table using Function
# ------------------------------------------

def multiplication_table(number):

    print(f"\nTable of {number}")

    for i in range(1, 11):

        print(f"{number} x {i} = {number*i}")

multiplication_table(5)


# ------------------------------------------
# 6. Sum of Numbers using Loop
# ------------------------------------------

def calculate_sum(n):

    total = 0

    for i in range(1, n + 1):

        total += i

    return total


print("\nSum of 1 to 10 =", calculate_sum(10))


# ------------------------------------------
# 7. Factorial Program
# ------------------------------------------

def factorial(number):

    fact = 1

    for i in range(1, number + 1):

        fact = fact * i

    return fact


user_num = int(input("\nEnter number for factorial: "))

print("Factorial =", factorial(user_num))


# ------------------------------------------
# 8. Find Largest Number
# ------------------------------------------

def find_largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= c:
        return b

    else:
        return c


largest = find_largest(55, 78, 45)

print("\nLargest Number =", largest)


# ------------------------------------------
# 9. Count Even Numbers in Loop
# ------------------------------------------

def count_even_numbers(limit):

    count = 0

    for i in range(1, limit + 1):

        if i % 2 == 0:
            count += 1

    return count


print("Even Numbers Count =", count_even_numbers(20))


# ------------------------------------------
# 10. Grade Calculator
# ------------------------------------------

def calculate_grade(marks):

    if marks >= 90:
        return "A Grade"

    elif marks >= 75:
        return "B Grade"

    elif marks >= 60:
        return "C Grade"

    else:
        return "Fail"


marks = int(input("\nEnter Marks: "))

print("Result :", calculate_grade(marks))


# ------------------------------------------
# 11. Star Pattern using Function
# ------------------------------------------

def print_pattern(rows):

    print("\nStar Pattern")

    for i in range(1, rows + 1):

        print("*" * i)


print_pattern(5)


# ------------------------------------------
# 12. Employee Bonus Calculator
# ------------------------------------------

def calculate_bonus(salary):

    if salary >= 50000:
        return salary * 0.10

    else:
        return salary * 0.05


salary = float(input("\nEnter Salary: "))

bonus = calculate_bonus(salary)

print("Bonus =", bonus)


# ------------------------------------------
# 13. Simple Login Verification
# ------------------------------------------

def login(username, password):

    if username == "ashish" and password == "1234":
        return "Login Successful"

    return "Invalid Username or Password"


user = input("\nEnter Username: ")
pwd = input("Enter Password: ")

print(login(user, pwd))


# ------------------------------------------
# 14. Lambda Function
# ------------------------------------------

square = lambda x: x * x

print("\nSquare of 7 =", square(7))


# ------------------------------------------
