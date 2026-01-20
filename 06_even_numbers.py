list_numbers = list(map(int, input().split(', ')))

idx_numbers = list(map(lambda x: x if list_numbers[x]%2==0 else 'no', range(len(list_numbers))))
sorted_numbers = list(filter(lambda a: a != 'no', idx_numbers))

print(sorted_numbers)