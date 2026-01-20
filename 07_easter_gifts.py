gift_list=input().split()

user_input=str()

while True:
    user_input=input()
    if user_input=="No Money":
        break
    new_list=user_input.split()
    if new_list[0]=="OutOfStock":
        while True:
            if new_list[1] in gift_list:
                idx=gift_list.index(new_list[1])
                gift_list.pop(idx)
                gift_list.insert(idx,"None")
            else:
                break
    elif new_list[0]=="Required":
        if int(new_list[2])<len(gift_list) and int(new_list[2])>=0:
            idx=int(new_list[2])
            gift_list.pop(idx)
            gift_list.insert(idx, new_list[1])
        else:
            continue
    elif new_list[0]=="JustInCase":
        gift_list.pop()
        gift_list.append(new_list[1])

new02_list=[]
for item in gift_list:
    if item!="None":
        new02_list.append(item)

final=(" ".join(new02_list))
print(final)



