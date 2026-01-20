n = int(input())
students = dict()

for i in range(n):
    line = input().split()
    name, grade = line[0], float(line[1])
    if name not in students.keys():
        students[name] = list()
    students[name].append(grade)

for key, value in students.items():
    average = sum(students[key]) / len(students[key])
    grades_as_string = [f"{el:.2f}" for el in value]
    print(f"{key} -> {' '.join(grades_as_string)} (avg: {average:.2f})")


