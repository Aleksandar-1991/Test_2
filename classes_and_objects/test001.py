# x = 5
#
# print(f"{x:02d}")
# print(f"{x:.2f}")


ingredients = {"cheese": 2, "olives": 3}
# print(", ".join(ingredients.items()))



result = []
for key, value in ingredients.items():
    result.append(f"{key}: {value}")

print(", ".join(result))

