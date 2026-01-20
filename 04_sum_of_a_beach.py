n=input()
input_string=n.lower()
appearance_count=0


sand=["s", "a", "n", "d"]
water=["w", "a", "t", "e", "r"]
fish=["f", "i", "s", "h"]
sun=["s", "u", "n"]
list=[sand, water, fish, sun]

temp_string=input_string

for idx in range(len(list)):
    appearance = False
    letter_count=0
    temp_count=0

    for_counter=0
    for letter in list[idx]:
        for_counter += 1
        if temp_string.count(letter)>0:
            appearance = True
            temp_count=temp_string.count(letter)
            if letter_count==0:
                letter_count=temp_count
            elif letter_count>0:
                if letter_count>temp_count:
                    letter_count=temp_count
        else:
            appearance=False
            break
        if for_counter==len(list[idx]) and appearance==True:
            for letter_remove in list[idx]:
                for rep in range(letter_count):
                    temp_index=temp_string.find(letter_remove)
                    if temp_index!=-1 and temp_index>=0:
                        temp_string=temp_string[:temp_index] + temp_string[temp_index+1:]
                    print(temp_string)


    if appearance == True:
        appearance_count += letter_count


print(appearance_count)
print(input_string)
print(temp_string)

