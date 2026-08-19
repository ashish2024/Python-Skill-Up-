# Day 18 - Iterators and Generators

numbers = [10, 20, 30]

iterator = iter(numbers)

print(next(iterator))
print(next(iterator))
print(next(iterator))

# Generator

def generate_numbers():

    for i in range(1, 6):
        yield i

for num in generate_numbers():
    print(num)