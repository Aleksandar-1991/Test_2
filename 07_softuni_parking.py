parking = dict()
n = int(input())

for line in range(n):
    tokens = input().split(" ")
    command = tokens[0]
    if command == "register":
        name, reg = tokens[1], tokens[2]
        if name in parking.keys():
            print(f"ERROR: already registered with plate number {parking[name]}")
        else:
            parking[name] = reg
            print(f"{name} registered {reg} successfully")
    elif command == "unregister":
        name = tokens[1]
        if name not in parking.keys():
            print(f"ERROR: user {name} not found")
        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")


for (name, reg) in parking.items():
    print(f"{name} => {reg}")