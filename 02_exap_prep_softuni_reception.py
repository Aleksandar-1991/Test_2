first_employee_capacity = int(input())
second_employee_capacity = int(input())
third_employee_capacity = int(input())
total_capacity_per_hour = first_employee_capacity + second_employee_capacity + third_employee_capacity

number_of_students = int(input())
time_needed = 0

while number_of_students > 0:
    time_needed += 1
    if time_needed % 4 == 0:
        continue
    number_of_students -= total_capacity_per_hour

print(f"Time needed: {time_needed}h.")

