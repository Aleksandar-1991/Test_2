import math
from math import floor

emp01 = int(input())
emp02 = int(input())
emp03 = int(input())
students = int(input())

total_students_per_hour = emp01 + emp02 + emp03

time_needed = students/total_students_per_hour
if time_needed//3 > 0:
    time_needed += time_needed//3
# if time_needed % 3 == 1:
#     time_needed -= 1

# time_needed_including_breaks = 0
# for hour in range(1, time_needed +1):
#     time_needed_including_breaks += 1
#     if hour % 4 == 0:
#         time_needed_including_breaks += 1

print(f"Time needed: {math.ceil(time_needed)}h.")