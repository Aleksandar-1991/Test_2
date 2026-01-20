number_of_students = int(input())
course_lectures = int(input())
additional_bonus = int(input())
students_bonuses = []
max_bonus = float()
max_attendance = int()


for student in range(number_of_students):
    student_attendances = int(input())
    total_bonus = student_attendances/course_lectures*(5 + additional_bonus)
    students_bonuses.append(total_bonus)
    if total_bonus>max_bonus:
        max_bonus=total_bonus
        max_attendance = student_attendances

print(f"Max Bonus: {round(max_bonus)}.")
print(f"The student has attended {max_attendance} lectures.")





