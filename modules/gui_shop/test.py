numbers = [int(x) for x in input().split(", ")]
n = int(input())
sets = []
for i in range(n):
    line = [int(x) for x in input().split(", ")]
    sets.append(line)

universe_set = set(numbers)
chosen_sets = []
remaining_sets = sets.copy()

while universe_set and remaining_sets:
    best_set = max(remaining_sets, key=lambda s: len(universe_set.intersection(s)))
    print(best_set)