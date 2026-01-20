contest = dict()
individual_standing = dict()


while (command := input()) != "no more time":
    tokens = command.split(" -> ")
    name, course, point = tokens[0], tokens[1], int(tokens[2])
    updated_points_only = False
    if course not in contest.keys():
        contest[course] = {}
        contest[course][name] = point
    else:
        name_exists = False
        for username, points in contest[course].items():
            if name == username:
                name_exists = True
                if points < point:
                    contest[course][username] = point
                    updated_points_only = True
                    individual_standing[name] = point
        if not name_exists:
            contest[course][name] = point


    #individual_stansing
    if name not in individual_standing.keys():
        individual_standing[name] = 0
    if not updated_points_only:
        individual_standing[name] += point

individual_standing = dict(sorted(sorted(individual_standing.items(), key=lambda item: item[0]), key=lambda item: item[1], reverse=True))
# contest = dict(sorted(contest.items(), key=lambda item: item[0]))

for crs, val in contest.items():
    print(f"{crs}: {len(val)} participants")
    val = dict(sorted(sorted(val.items(), key=lambda item: item[0]), key=lambda item: item[1], reverse=True))
    num = 0
    for nm, pt in val.items():
        num += 1
        print(f"{num}. {nm} <::> {pt}")

print("Individual standings:")
number = 1
for name01, points01 in individual_standing.items():
    print(f"{number}. {name01} -> {points01}")
    number += 1

# print(contest)
# print(individual_standing)
