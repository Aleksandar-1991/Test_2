def fill_the_box(box_height, box_length, box_width, *args):
    cubes_passed = list(args)
    cubes =  0
    for cube in cubes_passed:
        if cube == "Finish":
            break
        else:
            cubes += int(cube)
    box_volume = box_height * box_length * box_width
    if box_volume >= cubes:
        free_space = box_volume - cubes
        return f"There is free space in the box. You could put {free_space} more cubes."
    else:
        cubes_left = box_volume - cubes
        return f"No more free space! You have {abs(cubes_left)} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
