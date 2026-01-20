exam_results = dict()
submissions = dict()

while (command := input()) != "exam finished":
    tokens = command.split("-")
    name = tokens[0]
    if tokens[1] == 'banned':
        del exam_results[name]
    else:
        course, points = tokens[1], int(tokens[2])
        if name not in exam_results.keys():
            exam_results[name] = 0
        if points > exam_results[name]:
            exam_results[name] = points
        if course not in submissions.keys():
            submissions[course] = 0
        submissions[course] += 1

print("Results:")
for name, pt in exam_results.items():
    print(f"{name} | {pt}")

print("Submissions:")
for crs, scr in submissions.items():
    print(f"{crs} - {scr}")



