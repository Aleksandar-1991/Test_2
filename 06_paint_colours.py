from collections import deque

substrings = deque(input().split())

main_colours = ["yellow", "blue", "red"]
secondary_colours = ["orange", "purple", "green"]

collected_colours = list()


while substrings:
    if len(substrings) == 1:
        temp_string01 = substrings[0]
    else:
        temp_string01 = substrings[0] + substrings[-1]
        temp_string02 = substrings[-1] + substrings[0]
    colour_found = ""
    for col in main_colours:
        if col == temp_string01 or col == temp_string02:
            colour_found = col
            break
    for col in secondary_colours:
        if col == temp_string01 or col == temp_string02:
            colour_found = col
            break
    if colour_found:
        collected_colours.append(colour_found)
        if len(substrings) == 1:
            del substrings[0]
            break
        substrings.popleft()
        substrings.pop()
    else:
        if len(substrings) == 1:
            substrings.pop()
            break
        first = substrings.popleft()[:-1]
        second = substrings.pop()[:-1]
        mid = len(substrings) // 2
        if not first and not second:
            continue
        elif not first:
            substrings.insert(mid, second)
        elif not second:
            substrings.insert(mid, first)
        else:
            substrings.insert(mid, first)
            substrings.insert(mid + 1, second)

if 'orange' in collected_colours:
    if 'red' not in collected_colours or 'yellow' not in collected_colours:
        collected_colours.remove('orange')
if 'purple' in collected_colours:
    if 'red' not in collected_colours or 'blue' not in collected_colours:
        collected_colours.remove('orange')
if 'green' in collected_colours:
    if 'yellow' not in collected_colours or 'blue' not in collected_colours:
        collected_colours.remove('orange')

print(collected_colours)




