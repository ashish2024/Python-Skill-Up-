#
# Same method name, different behavior

class Dog:
    def sound(self):
        print("Dog Barks")

class Cat:
    def sound(self):
        print("Cat Meows")

animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()

# Method Overriding

class Employee:

    def work(self):
        print("Employee Works")

class Developer(Employee):

    def work(self):
        print("Developer Writes Code")

dev = Developer()
dev.work()

# Built-in Polymorphism

print(len("Python"))
print(len([1, 2, 3, 4, 5]))