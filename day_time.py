
from datetime import datetime
from datetime import timedelta

now = datetime.now()

print("Current Date & Time:", now)

print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)

future = now + timedelta(days=10)

print("After 10 Days:", future)