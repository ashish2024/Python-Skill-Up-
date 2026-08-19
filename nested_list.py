
students = [
    ["Ashish", 101],
    ["Rahul", 102],
    ["Ankit", 103]
]

print(students)

print(students[0])
print(students[1][0])
print(students[2][1])



# ========================================
# NESTED LISTS IN PYTHON
# ========================================
#
# A Nested List is a list that contains
# one or more lists inside it.
#
# Access Format:
# list_name[row][column]
#
# Example:
# [
#     [101, "Ashish"],
#     [102, "Rahul"]
# ]
#
# ========================================

# Example 1: Student Records

students = [
    ["Ashish", 101],
    ["Rahul", 102],
    ["Ankit", 103]
]

print("Student Records")
print(students)

print("First Student:", students[0])
print("First Student Name:", students[0][0])
print("Second Student ID:", students[1][1])


marks = [
    [85, 90, 95],
    [78, 88, 92],
    [65, 75, 80]
]

print("\nStudent Marks")

print("Student 1 Marks:", marks[0])
print("Student 2 First Subject:", marks[1][0])
print("Student 3 Last Subject:",[0 marks[2][2])


employees = [
    [101, "Ashish", "Developer"],
    [102, "Rahul", "Tester"],
    [103, "Ankit", "Support"]
]

print("\nEmployee Records")

for employee in employees:
    print(employee)

# ========================================
#
print("\nEmployee Details")

for employee in employees:
    print("ID:", employee[0])
    print("Name:", employee[1])
    print("Role:", employee[2])
    print()

#
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix")

for row in matrix:
    print(row)


print("\nMatrix Elements")

for row in matrix:
    for value in row:

        print(value, end=" ")
    print()


employee_skills = [
    ["Ashish", ["Python", "Java", "SQL"]],
    ["Rahul", ["Testing", "Automation"]],
    ["Ankit", ["React", "JavaScript"]]
]

print("\nEmployee Skills")

print(employee_skills[0][1])
print("First["Python", "Java", "", "JavaScript"
print("Ankit Skill:", employee_skills[2][1][1])


products = [
    [1001, "Laptop", 50000],
    [1002, "Mobile", 25000],
    [1003, "Tablet", 18000]
]

print("\nProduct Details")

for product in products:
    print("ID:", product[0])
    print("Product:", product[1])
    print("Price:", product[2])
    print()


student_marks = [
    [80, 70, 90],
    [60, 75, 85],
    [95, 88, 92]
]

print("Total Marks")

for marks in student_marks:
    total = sum(marks)
    print("Marks:", marks, "Total:", total)


cart = [
    ["Laptop", 1, 50000],
    ["Mouse", 2, 500],
    ["Keyboard", 1, 1500]
]

print("\nShopping Cart")

grand_total = 0

for item in cart:
    item_total = item[1] * item[2]
    grand_total += item_total

    print(
        "Item:", item[0],
        "| Quantity:", item[1],
        "| Price:", item[2],
        "| Total:", item_total
    )

print("Grand Total:", grand_total)

# ========================================

attendance = [
    ["Ashish", "Present"],
    ["Rahul", "Absent"],
    ["Ankit", "Present"]
]

print("\nAttendance Report")

for student in attendance:
    print(student[0], "-", student[1])


students = [
    ["Ashish", 101],
    ["Rahul", 102]
]

students.append(["Ankit", 103])

print("\nUpdated Student List")

for student in students:
    print(student)
("\nNested List Practice Completed Successfully")