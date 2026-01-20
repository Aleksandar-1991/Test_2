user_input=input()
list=user_input.split(", ")

wolf_idx=-1
sheep_idx=-1

for idx in range(len(list)):
    if list[idx]=="wolf" and idx==len(list)-1:
        print("Please go away and stop eating my sheep")
        break
    elif list[idx]=="wolf":
        wolf_idx=idx
        sheep_idx=len(list) - (idx+1)
        print(f"Oi! Sheep number {sheep_idx}! You are about to be eaten by a wolf!")


#print(len(list))