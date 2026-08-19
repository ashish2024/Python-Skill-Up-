# Day 6, Day 7 and Day 8 Combined Practice
# Topics: Strings, Classes, Objects, Constructors, Inheritance,
# Polymorphism and Encapsulation

print("Python Combined Practice")

# String Operations

name = "Ashish Sonkaria"

print("Original String:", name)
print("Upper Case:", name.upper())
print("Lower Case:", name.lower())
print("Length:", len(name))
print("Replace:", name.replace("Ashish", "Aman"))
print("Contains Ashish:", "Ashish" in name)

words = "Python Java SpringBoot React"

print(words.split())

for char in "Python":
    print(char)

# Classes and Objects

class Student:
    def display(self):
        print("Student method called")

student1 = Student()
student1.display()

# Employee Example

class Employee:
    def employee_info(self, emp_id, name):
        print("Employee ID:", emp_id)
        print("Employee Name:", name)

emp1 = Employee()
emp1.employee_info(101, "Ashish")

# Constructor Example

class EmployeeDetails:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("Employee Details")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Salary:", self.salary)

employee = EmployeeDetails(101, "Ashish", 60000)
employee.display()

# Inheritance Example

class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print("Name:", self.name)

class Developer(Person):

    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

    def show_skill(self):
        print("Skill:", self.skill)

dev = Developer("Ashish", "Python")

dev.show_name()
dev.show_skill()

# Polymorphism Example

class Dog:
    def sound(self):
        print("Dog says Bark")

class Cat:
    def sound(self):
        print("Cat says Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

# Encapsulation Example

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

account.deposit(2000)

print("Current Balance:", account.get_balance())

# Mini Project - Employee Management

class EmployeeManagement:

    def __init__(self, emp_id, name, department):
        self.emp_id = emp_id
        self.name = name
        self.department = department

    def display(self):
        print("Employee Record")
        print("ID:", self.emp_id)
        print("Name:", self.name)
        print("Department:", self.department)

employee1 = EmployeeManagement(
    1001,
    "Ashish",
    "Development"
)

employee1.display()

# Loop with Objects

employee_names = [
    "Ashish",
    "Rahul",
    "Ankit",
    "Rohit"
]

for employee in employee_names:
    print(employee)

