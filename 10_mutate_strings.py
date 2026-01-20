str01=input()
str02=input()
str_new=str()

for idx in range(len(str01)):
    if str02[idx]==str01[idx]:
        str_new += str01[idx]
    else:
        str_new = str_new[:idx] + str02[idx] + str01[idx+1:]
        print(str_new)