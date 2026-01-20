countries = input().split(", ")
capitals = input().split(", ")

# combined_results = {countries[index]:capitals[index] for index in range(len(countries))}
combined_results = dict(zip(countries, capitals))


for country, capital in combined_results.items():
    print(f"{country} -> {capital}")