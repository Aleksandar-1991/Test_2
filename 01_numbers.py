first_set = set( input().split())
second_set = set(input().split())


n = int(input())

for i in range(n):
    user_input = input().split()
    command = user_input[0] + " " + user_input[1]
    numbers = [x for x in user_input[2:]]
    if command == 'Add First':
        first_set = first_set.union(numbers)
    elif command == 'Add Second':
        second_set = second_set.union(numbers)
    elif command == 'Remove First':
        first_set = {n for n in first_set if n not in numbers}
    elif command == 'Remove Second':
        second_set = { n for n in second_set if n not in numbers}
    elif command == 'Check Subset':
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print(True)
        else:
            print(False)

first = list(map(int, first_set))
second = list(map(int, second_set))
print(*sorted(first), sep=', ')
print(*sorted(second), sep=', ')


