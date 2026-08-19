# 
import re

text = "Ashish 123 Python 456"

numbers = re.findall(r'\d+', text)

print(numbers)

name = re.search("Python", text)

print(name)

sentence = "Python,Java,React"

print(re.split(",", sentence))

new_text = re.sub("Python", "Java", sentence)

print(new_text)