n = int(input())
max_inter = {
    'max_len': 0,
    'start': 0,
    'end': 0
             }

for i in range(n):
    first, second = input().split("-")
    first_start, first_end = map(int, first.split(","))
    second_start, second_end = map(int, second.split(","))
    inter_start = int()
    inter_end = int()

    if first_start < second_start:
        inter_start = second_start
    else:
        inter_start = first_start

    if first_end > second_end:
        inter_end = second_end
    else:
        inter_end = first_end

    inter_len = inter_end - inter_start
    if max_inter['max_len'] <= inter_len:
        max_inter['max_len'] = inter_len
        max_inter['start'] = inter_start
        max_inter['end'] = inter_end

list_max = list()
for i in range(max_inter['start'], max_inter['end'] +1):
    list_max.append(i)
print(f"Longest intersection is {list_max} with length {max_inter['max_len'] +1}")





