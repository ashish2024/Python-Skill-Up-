# ========================================
# FUNCTIONS IN PYTHON
# ========================================
#
# A function is a block of code that performs
# a specific task and can be reused multiple times.
#
# Advantages:
# 1. Reduces code duplication
# 2. Improves readability
# 3. Makes code easier to maintain
#
# Syntax:
#
# def function_name():
#     code
#
# ========================================

# Example 1: Simple Function

def greet():
    print("Welcome to Python")

greet()

# ----------------------------------------

# Example 2: Function with Parameters

def greet_user(name):
    print("Hello,", name)

greet_user("Ashish")

# ----------------------------------------

# Example 3: Function with Multiple Parameters

def add_numbers(a, b):
    print("Sum =", a + b)

add_numbers(10, 20)

# ----------------------------------------

# Example 4: Function Returning a Value

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print("Multiplication =", result)

# ----------------------------------------

# Example 5: Function to Find Square

def square(num):
    return num * num

print("Square =", square(6))

# ----------------------------------------

# Example 6: Function to Check Even or Odd

def check_even_odd(number):

    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")

check_even_odd(15)

# ----------------------------------------

# Example 7: Function with Default Parameter

def country(name="India"):
    print("Country:", name)

country()
country("Canada")

# ----------------------------------------

# Example 8: Function to Calculate Area of Rectangle

def area(length, width):
    return length * width

print("Area =", area(10, 5))

# ----------------------------------------

# Example 9: Function to Find Largest Number

def largest(a, b):

    if a > b:
        return a
    else:
        return b

print("Largest Number =", largest(20, 15))

# ----------------------------------------

# Example 10: Function to Calculate Factorial

def factorial(num):

    fact = 1

    for i in range(1, num + 1):
        fact *= i

    return fact

print("Factorial of 5 =", factorial(5))

