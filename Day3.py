
# =========================
# DAY 3 - COMBINED PRACTICE
# =========================

print("Welcome to Day 3 Python Practice")

# -------------------------
# Variables and Data Types
# -------------------------

name = "Ashish"
age = 25
salary = 50000.50

print("\n--- Employee Details ---")
print("Name:", name)
print("Age:", age)
print("Salary:", salary)

# -------------------------
# User Input
# -------------------------

user_name = input("\nEnter your name: ")
user_age = int(input("Enter your age: "))

print("Hello", user_name)

# -------------------------
# If Else
# -------------------------

if user_age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# -------------------------
# Even or Odd
# -------------------------

number = int(input("\nEnter a number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")

# -------------------------
# For Loop
# -------------------------

print("\nNumbers from 1 to 5")

for i in range(1, 6):
    print(i)

# -------------------------
# While Loop
# -------------------------

print("\nWhile Loop Example")

count = 1

while count <= 5:
    print("Count =", count)
    count += 1

# -------------------------
# Multiplication Table
# -------------------------

table_num = int(input("\nEnter number for table: "))

print("\nMultiplication Table")

for i in range(1, 11):
    print(f"{table_num} x {i} = {table_num * i}")

# -------------------------
# Sum of First 10 Numbers
# -------------------------

sum_value = 0

for i in range(1, 11):
    sum_value += i

print("\nSum of first 10 numbers =", sum_value)

# -------------------------
# Pattern Program
# -------------------------

print("\nStar Pattern")

for i in range(1, 6):
    print("*" * i)

print("\nDay 3 Practice Completed Successfully")