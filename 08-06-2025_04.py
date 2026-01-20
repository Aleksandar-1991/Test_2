cats=int(input())
group1=int()
group2=int()
group3=int()
total_food=int()
total_food_price=float()

for i in range(cats):
    food_needed=int(input())
    if 100<=food_needed<200:
        total_food+=food_needed
        group1+=1
    elif 200<=food_needed<300:
        total_food+=food_needed
        group2+=1
    elif 300<=food_needed<400:
        total_food+=food_needed
        group3+=1

total_food_price=(total_food/1000)*12.45

print(f"Group 1: {group1} cats.")
print(f"Group 2: {group2} cats.")
print(f"Group 3: {group3} cats.")
print(f"Price for food per day: {total_food_price:.2f} lv.")