force_book = dict()

while (command := input()) != "Lumpawaroo":
    if "|" in command:
        force_side, force_user = command.split(" | ")
        if len(force_book)>0:
            user_in_value = False
            for value in force_book.values():
                if force_user in value:
                    user_in_value = True
                    break
            if user_in_value:
                continue
            else:
                if force_side not in force_book.keys():
                    force_book[force_side] = []
                    force_book[force_side].append(force_user)
                else:
                    force_book[force_side].append(force_user)


        else:
            force_book[force_side] = []
            force_book[force_side].append(force_user)
    elif "->" in command:
        force_user, force_side = command.split(" -> ")

        user_in_value = False
        if len(force_book) > 0:
            for value in force_book.values():
                if force_user in value:
                    user_in_value = True


        if user_in_value:
            for side, name in force_book.items():
                if force_user in name:
                    name.remove(force_user)
            if force_side not in force_book.keys():
                force_book[force_side] = []
            force_book[force_side].append(force_user)
        else:
            if force_side not in force_book.keys():
                force_book[force_side] = []
                force_book[force_side].append(force_user)
            else:
                force_book[force_side].append(force_user)
        print(f"{force_user} joins the {force_side} side!")

for side, users in force_book.items():
    if len(users) > 0:
        print(f"Side: {side}, Members: {len(users)}")
        for user in users:
            print(f"! {user}")

