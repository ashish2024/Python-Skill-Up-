
# Inheritance allows one class to acquire
# properties and methods from another class.

# Parent Class

class Person:

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name:", self.name)

# Child Class

class Employee(Person):

    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

    def show_employee(self):
        print("Employee ID:", self.emp_id)

emp = Employee("Ashish", 101)

emp.display()
emp.show_employee()

# Multilevel Inheritance

class GrandParent:
    def family_name(self):
        print("Sonkaria")

class Parent(GrandParent):
    pass

class Child(Parent):
    pass

obj = Child()
obj.family_name()

# Hierarchical Inheritance

class Vehicle:
    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

Car().start()
Bike().start()