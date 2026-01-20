def plant_garden(garden_space: float, *allowed_plant_types: tuple, **planting_requests: dict):
    free_space = garden_space
    sorted_planting_requests = sorted(planting_requests.items(), key= lambda kvp: kvp[0])
    planted_types = dict()

    min_area = float()

    can_be_planted = dict()
    plants_area = dict()
    for name, quantity in planting_requests.items():
        for allowed_plant_name, allowed_plant_area in allowed_plant_types:
            if name == allowed_plant_name:
                can_be_planted[name] = quantity
                plants_area[name] = allowed_plant_area
                if min_area > allowed_plant_area:
                    min_area = allowed_plant_area
    sorted_can_be_planted = sorted(can_be_planted.items(), key= lambda kvp: kvp[0])
    not_planted_types = dict(sorted_can_be_planted)


    for name, quantity in sorted_can_be_planted:
        if not not_planted_types or free_space < min_area:
            break
        quantity_for_planting = free_space // plants_area[name]
        if quantity_for_planting <= 0:
            continue
        if quantity_for_planting > quantity:
            quantity_for_planting = quantity
        free_space -= quantity_for_planting * plants_area[name]
        planted_types[name] = quantity_for_planting
        not_planted_types[name] = quantity - quantity_for_planting
        if not_planted_types[name] == 0:
            del not_planted_types[name]


    result = ""
    if not not_planted_types:
        result += f"All plants were planted! Available garden space: {free_space:.1f} sq meters.\n"
    else:
        result += f"Not enough space to plant all requested plants!\n"

    result += "Planted plants:\n"
    for key, value in planted_types.items():
        result += f"{key}: {int(value)}\n"

    return result


print(plant_garden(50.0, ("rose", 2.5), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20))
print(plant_garden(20.0, ("rose", 2.0), ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, sunflower=5))
print(plant_garden(2.0, ("rose", 2.5), ("tulip", 1.2), ("daisy", 0.2), rose=4, tulip=15, sunflower=3, daisy=4))
print(plant_garden(50.0, ("tulip", 1.2), ("sunflower", 3.0), rose=10, tulip=20, daisy=1))