company_users = dict()

while (command := input()) != 'End':
    company_name, user = command.split(" -> ")
    if company_name not in company_users:
        company_users[company_name] = []
    if user not in company_users[company_name]:
        company_users[company_name].append(user)

for company, users in company_users.items():
    print(f"{company}")
    for use in users:
        print(f"-- {use}")