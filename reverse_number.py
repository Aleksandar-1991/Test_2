arr01=input().split(',')
arr02=[]

for i in arr01:
    if i in arr02:
        continue
    else:
        arr02.append(i)


print(','.join(arr02))






#
#     if arr01[i]==last:
#         seq+=1
#         if seq>max_seq:
#             max_seq=seq
#             max_char=arr01[i]
#     else:
#         seq=0
#     last=arr01[i]
#
# print(max_char)




