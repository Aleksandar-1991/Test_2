cups_of_coffee=int()
while True:
    string=input()
    if string=="END":
        break
    elif (string=="coding" or string=="cat" or string=="dog" or string=="movie"):
        cups_of_coffee+= 1
    elif (string=="CODING" or string=="CAT" or string=="DOG" or string=="MOVIE"):
        cups_of_coffee+= 2
    else:
        continue

if cups_of_coffee>5:
    print("You need extra sleep")
else:
    print(cups_of_coffee)