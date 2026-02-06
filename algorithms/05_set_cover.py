def set_cover(universe, sets):
    universe_set = set(universe)
    chosen_sets = []
    remaining_sets = sets.copy()

    while universe_set and remaining_sets:
        best_set = set()
        num_match = 0
        for s in remaining_sets:
            if universe_set.intersection(s) and len(universe_set.intersection(s)) > num_match:
                num_match = len(s)
                best_set = s
        if best_set:
            universe_set = universe_set.difference(best_set)
            remaining_sets.remove(best_set)
            chosen_sets.append(best_set)
        else:
            return f"No solution exists"
    if not remaining_sets and universe_set:
        return f"No solution exists"
    result = f"Sets to take ({len(chosen_sets)}):\n"
    for s in chosen_sets:
        result += "{ " + f'{", ".join(map(str, s))}'+" }\n"
    return result

numbers = [int(x) for x in input().split(", ")]
n = int(input())
sets = []
for i in range(n):
    line = [int(x) for x in input().split(", ")]
    sets.append(line)


print(set_cover(numbers, sets))
