budget=float(input())
flour_kg_price=float(input())
pack_of_eggs_price=(flour_kg_price/4)*3
milk_litre_price=flour_kg_price + (flour_kg_price/4)

bread_made=int()
eggs_received=int()

total_price_one_bread=flour_kg_price + pack_of_eggs_price + (milk_litre_price/4)

while budget>total_price_one_bread:
    budget-=total_price_one_bread
    bread_made+=1
    eggs_received+=3
    if bread_made%3==0:
        eggs_received-=(bread_made-2)

print(f"You made {bread_made} loaves of Easter bread! Now you have {eggs_received} eggs and {budget:.2f}BGN left.")


# quantity_milk=float()
# quantity_flour=int()
# quantity_pack_of_eggs=int()
#
# while budget>0:
#     if quantity_milk<0.25 and budget<(milk_litre_price+pack_of_eggs_price+flour_kg_price):
#         break
#     elif quantity_milk>=0.25 and budget<(pack_of_eggs_price+flour_kg_price):
#         break
#
#     if quantity_milk<0.25:
#         budget-=(milk_litre_price+pack_of_eggs_price+flour_kg_price)
#         quantity_milk += 1
#         quantity_flour += 1
#         quantity_pack_of_eggs += 1
#     elif quantity_milk>=0.25:
#         budget -= (pack_of_eggs_price + flour_kg_price)
#         quantity_flour += 1
#         quantity_pack_of_eggs += 1
#
#     quantity_milk -= 0.25
#     quantity_flour -= 1
#     quantity_pack_of_eggs -= 1
#     bread_made+=1
#     eggs_received+=3
#     if bread_made%3==0:
#         eggs_received-=(bread_made-2)
#     if quantity_milk>0:
#         budget+=(milk_litre_price*quantity_milk)
#         quantity_milk=0
#
# print(f"You made {bread_made} loaves of Easter bread! Now you have {eggs_received} eggs and {budget:.2f}BGN left.")




