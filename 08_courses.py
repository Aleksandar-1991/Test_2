courses = dict()

while (command := input()) != 'end':
    course_name, student_name = command.split(" : ")
    if course_name not in courses.keys():
        courses[course_name] = []
    courses[course_name].append(student_name)

for name, students in courses.items():
    print(f"{name}: {len(students)}")
    for student in students:
        print(f"-- {student}")