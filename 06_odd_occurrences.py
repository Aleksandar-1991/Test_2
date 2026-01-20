words = input().split(' ')

words_counter = dict()
output_list = list()

for word in words:
    if word.lower() in words_counter:
        words_counter[word.lower()] += 1
    else:
        words_counter[word.lower()] = 1

# for wd in words_counter:
#     if int(words_counter[wd]) % 2 != 0:
#         output_list.append(wd)

for (key, value) in words_counter.items():
    if value % 2 != 0:
        print(key, end=" ")



print(" ".join(output_list))

