# Day 9, Day 10 and Day 11 Combined Practice
# Topics: Sets, Dictionaries and File Handling

print("Python Combined Practice")

# Sets

fruits = {"Apple", "Banana", "Mango"}

print("Original Set:", fruits)

fruits.add("Orange")
print("After Adding:", fruits)

fruits.remove("Banana")
print("After Removing:", fruits)

for fruit in fruits:
    print(fruit)

# Set Operations

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print("Union:", set1.union(set2))
print("Intersection:", set1.intersection(set2))
print("Difference:", set1.difference(set2))

# Dictionaries

student = {
    "id": 101,
    "name": "Ashish",
    "course": "Python"
}

print("\nStudent Details")
print(student)

print("Name:", student["name"])

student["city"] = "Hyderabad"

print("Updated Dictionary:")
print(student)

for key, value in student.items():
    print(key, ":", value)

# Dictionary of Employees

employees = {
    101: "Ashish",
    102: "Rahul",
    103: "Ankit"
}

print("\nEmployee Records")

for emp_id, emp_name in employees.items():
    print(emp_id, "-", emp_name)

# File Handling

print("\nFile Handling Example")

file = open("sample.txt", "w")

file.write("Welcome to Python File Handling\n")
file.write("Learning Python Step by Step")

file.close()

print("Data Written Successfully")

# Reading File

file = open("sample.txt", "r")

content = file.read()

print("\nFile Content:")
print(content)

file.close()

# Using With Statement

with open("sample.txt", "a") as file:
    file.write("\nThis line is appended to the file")

print("Data Appended Successfully")

# Reading Updated File

with open("sample.txt", "r") as file:
    print("\nUpdated File Content:")
    print(file.read())

print("\nDay 9, Day 10 and Day 11 Practice Completed")
