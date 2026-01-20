usernames = input().split(", ")
not_allowed = ['']
for user in usernames:
    if len(user) not in range(3, 16 +1):
        continue
    if any(char in not_allowed for char in user):
        continue
    if all(char.isalnum() or char in ('-', '_') for char in user):
        print(user)