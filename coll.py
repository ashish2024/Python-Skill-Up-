# Day 19 - Collections Module

from collections import Counter
from collections import deque

text = ["Python", "Java", "Python", "React"]

counter = Counter(text)

print(counter)

queue = deque()

queue.append("Ashish")
queue.append("Rahul")

print(queue)

queue.popleft()

print(queue)