wealth = list(map(int, input().split(', ')))
mininum_wealth = int(input())

if sum(wealth)//len(wealth) < mininum_wealth:
    print("No equal distribution possible")
else:
    for idx in range(len(wealth)):
        if wealth[idx] < mininum_wealth:
            wealth_needed = mininum_wealth - wealth[idx]
            max_wealth_index = wealth.index(max(wealth))
            if wealth[max_wealth_index] - wealth_needed >= mininum_wealth:
                wealth[idx] += wealth_needed
                wealth[max_wealth_index] -= wealth_needed
    print(wealth)


