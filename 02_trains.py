wagons = int(input())

my_list = [0] * wagons

while True:
    operation = input()
    if operation == "End":
        break
    elif operation.split()[0] == 'add':
        my_list[-1] += int(operation.split()[1])
    elif operation.split()[0] == "insert":
        current_wagon = int(operation.split()[1])
        current_people = int(operation.split()[2])
        my_list[current_wagon] += current_people
    elif operation.split()[0] == "leave":
        leaving_wagon = int(operation.split()[1])
        leaving_people = int(operation.split()[2])
        my_list[leaving_wagon] -= leaving_people

print(my_list)
