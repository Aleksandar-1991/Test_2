list_names = input().split(', ')

sorted_list = sorted(list_names, key=lambda x: (-len(x), x))

print(sorted_list)