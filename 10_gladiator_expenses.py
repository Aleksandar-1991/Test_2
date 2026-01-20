lost_fights=int(input())
helmet_price=float(input())
sword_price=float(input())
shield_price=float(input())
armor_price=float(input())

total_sum=0
broken_shield=int()

for fight in range(1,lost_fights+1):
    if fight%2==0:
        total_sum += helmet_price
    if fight%3==0:
        total_sum += sword_price
    if fight%2==0 and fight%3==0:
        total_sum += shield_price
        broken_shield += 1
    if broken_shield%2==0 and broken_shield>0:
        total_sum += armor_price
        broken_shield=0

print(f"Gladiator expenses: {total_sum:.2f} aureus")
