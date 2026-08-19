# Day 12 - Encapsulation

class BankAccount:

    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)

account.deposit(2000)

print("Balance:", account.get_balance())

# Student Example

class Student:

    def __init__(self):
        self.__marks = 0

    def set_marks(self, marks):
        self.__marks = marks

    def get_marks(self):
        return self.__marks

student = Student()

student.set_marks(95)

print(student.get_marks())