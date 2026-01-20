word=input()
list=[]

for idx in range(len(word)):
    if 65<=ord(word[idx])<=90:
        list.append(idx)

print(list)
