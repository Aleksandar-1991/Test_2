phonebook = dict()

while '-' in (command := input()):
    name, number = command.split("-")
    # if name not in phonebook.keys():
    #     phonebook[name] = ""
    # phonebook[name]= number
    phonebook[name] = number




for i in range(int(command)):
    contact = input()
    if contact in phonebook.keys():
        print(f"{contact} -> {phonebook[contact]}")
    else:
        print(f"Contact {contact} does not exist.")

