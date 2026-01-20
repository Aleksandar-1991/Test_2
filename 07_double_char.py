while True:
    string=input()
    if string=="End":
        break
    elif string=="SoftUni":
        continue
    else:
        new_string=str()
        for char in string:
            char_to_add=str(char * 2)
            new_string+= char_to_add
        print(new_string)


