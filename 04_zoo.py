class Zoo:
    __animals = 0

    def __init__(self, name: str):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species: str, name: str):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species: str):
        names = str()
        total_animals = len(self.mammals) + len(self.fishes) + len(self.birds)
        capitalized = species.capitalize()
        if species == "mammal":
            names = ", ".join(self.mammals)
            return f"{capitalized}s in {self.name}: {names}\nTotal animals: {total_animals}"
        elif species == "fish":
            names = ", ".join(self.fishes)
            return f"{capitalized}es in {self.name}: {names}\nTotal animals: {total_animals}"
        elif species == "bird":
            names = ", ".join(self.birds)
            return f"{capitalized}s in {self.name}: {names}\nTotal animals: {total_animals}"



zoo_name = input()

zoo = Zoo(zoo_name)
n = int(input())
for i in range(n):
    line = input()
    tokens = line.split(" ")
    species = tokens[0]
    name = tokens[1]
    zoo.add_animal(species, name)

required_species = input()

print(zoo.get_info(required_species))







