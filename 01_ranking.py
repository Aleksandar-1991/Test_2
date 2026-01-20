contest_dictionary = dict()
contest_new = dict()


while (contest_command := input()) != "end of contests":
    contest, contest_password = contest_command.split(":")
    contest_dictionary[contest] = contest_password

while (submissions_command := input()) != "end of submissions":
    current_contest, current_password, current_username, current_points = submissions_command.split("=>")
    points = int(current_points)
    if current_contest in contest_dictionary.keys() and contest_dictionary[current_contest] == current_password:
        if current_username not in contest_new.keys():
            contest_new[current_username] = dict()
            contest_new[current_username][current_contest] = points
        else:
            contest_exists = False
            for cont, point in contest_new[current_username].items():
                if current_contest == cont:
                    contest_exists = True
                    if point < int(current_points):
                        point = int(current_points)
            if not contest_exists:
                contest_new[current_username][current_contest] = int(current_points)

# print(contest_new)
total_points = 0
user_total_points = str()
for user, pts in contest_new.items():
    if sum(contest_new[user].values()) > total_points:
        total_points = sum(contest_new[user].values())
        user_total_points = user
print(f"Best candidate is {user_total_points} with total {total_points} points.")


print("Ranking:")
contest_new = dict(sorted(contest_new.items(), key=lambda item: item[0]))

for participant, courses in contest_new.items():
    print(f"{participant}")
    sorted_results = dict(sorted(contest_new[participant].items(), key=lambda item: item[1], reverse=True))
    for crs, pts in sorted_results.items():
        print(f"#  {crs} -> {pts}")




