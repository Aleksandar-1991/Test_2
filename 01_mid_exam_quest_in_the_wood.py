days_of_adventure = int(input())
participants = int(input())
total_energy = float(input())
water_per_person_per_day = float(input())
food_per_person_per_day = float(input())

water_needed = days_of_adventure * participants * water_per_person_per_day
food_needed = days_of_adventure * participants * food_per_person_per_day



for day in range(1, days_of_adventure + 1):
    daily_energy_loss = float(input())
    # water_needed -= (water_per_person_per_day * participants)
    # food_needed -= (food_per_person_per_day * participants)
    if total_energy - daily_energy_loss <= 0:
        total_energy -= daily_energy_loss
        break
    else:
        total_energy -= daily_energy_loss
    if day % 2 == 0:
        total_energy += total_energy * 0.05
        water_needed *= 0.7
    if day % 3 == 0:
        total_energy += total_energy * 0.1
        food_needed -= (food_needed/participants)
        # calculate food: reduces their food supplies by the following amount: {currentFood}/{countOfPeople}


if total_energy > 0:
    print(f"You are ready for the quest. You will be left with {total_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {food_needed:.2f} food and {water_needed:.2f} water.")







