#
square = lambda x: x * x

print(square(5))

numbers = [1, 2, 3, 4, 5]

result = list(map(lambda x: x * 2, numbers))

print(result)

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)
