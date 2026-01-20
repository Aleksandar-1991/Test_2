list01 = input().split(', ')
list02 = input().split(', ')
final_list = []

# for sub in list01:
#     for word in list02:
#         if sub in word:
#             final_list.append(sub)
#             break
#
# print(final_list)

final_list = [sub for sub in list01 if any(sub in i for i in list02)]


print(final_list)