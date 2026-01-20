lines = int(input())
student_book = dict()

for line in range(lines):
    student_name = input()
    grade = float(input())
    if student_name not in student_book.keys():
        student_book[student_name] = []
    student_book[student_name].append(grade)

for name, grades in student_book.items():
    average_grade = sum(grades)/len(grades)
    if average_grade >= 4.50:
        print(f"{name} -> {average_grade:.2f}")

