num_list = input().split()

final_list = []

for num in range(len(num_list)):
    final_list.append(abs(float(num_list[num])))

print(final_list)