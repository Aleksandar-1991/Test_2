food_available=int(input())
food_available*=1000
food_eaten=str()

while True:
    food_eaten=input()
    if food_eaten=="Adopted":
        break
    food_available-=int(food_eaten)


if food_available<0:
    print(f"Food is not enough. You need {(food_available)*(-1)} grams more." )
else:
    print(f"Food is enough! Leftovers: {food_available} grams." )