word=input()

list01=word.split()
new_list=[]
for i in list01:
    new_list.append(int(i)*(-1))

print(new_list)