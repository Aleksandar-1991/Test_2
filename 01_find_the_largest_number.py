n=input()
temp_number=n
new_number=str()
temp_max_num=-1
idx_max_number=int()

for i in range(len(n)):
    for char in range(len(temp_number)):
        if int(temp_number[char])>temp_max_num:
            temp_max_num=int(temp_number[char])
            idx_max_number=char
    new_number+=str(temp_max_num)
    temp_number=temp_number[:idx_max_number] + temp_number[idx_max_number+1:]
    temp_max_num=-1

print(new_number)
