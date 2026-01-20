decorations_quantity_needed=int(input())
days_to_christmas=int(input())

money_spent=int()
christmat_spirit=int()

for day in range(1,days_to_christmas+1):
    if day%11==0:
        #print("11th day")
        decorations_quantity_needed += 2
        #print(decorations_quantity_needed)
    if day%2==0:
        money_spent+=2*decorations_quantity_needed
        christmat_spirit+=5
    if day%3==0:
        money_spent += 8*decorations_quantity_needed
        christmat_spirit += 13
    if day%5==0:
        money_spent += 15*decorations_quantity_needed
        christmat_spirit += 17
    if day%3==0 and day%5==0:
        christmat_spirit += 30
        #print("day divisible by 3 and 5")
    if day%10==0:
        money_spent += 23
        christmat_spirit -= 20
        #print("day divisible by 10")
    if day==days_to_christmas and day%10==0:
        christmat_spirit -= 30
        #print("last day divisible by 10")

print(f"Total cost: {money_spent}")
print(f"Total spirit: {christmat_spirit}")