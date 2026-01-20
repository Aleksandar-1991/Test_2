from collections import deque

given_strings = deque(input().split())

main_colours = ['red', 'yellow', 'blue']
secondary_colours = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'}
}

collected_colours = list()

while given_strings:
    first = given_strings.popleft()
    second = given_strings.pop() if given_strings else ""
    for colour in (first + second, second + first):
        if colour in main_colours or colour in secondary_colours:
            collected_colours.append(colour)
            break
    else:
        if len(first) > 1:
            given_strings.insert(len(given_strings) // 2, first[:-1])
        if len(second) > 1:
            given_strings.insert(len(given_strings) // 2, second[:-1])

for colour in collected_colours:
    if colour in secondary_colours.keys() and not secondary_colours[colour].issubset(collected_colours):
        collected_colours.remove(colour)

print(collected_colours)
