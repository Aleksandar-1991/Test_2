import os
from project.pokemon import Pokemon



class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: list[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon not in self.pokemons:
            self.pokemons.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        # for p in self.pokemons:
        #     if p.name == pokemon_name:
        #         self.pokemons.remove(p)
        #         return f"You have released {pokemon_name}"
        # return f"Pokemon is not caught"

        pokemon_to_release = next((p for p in self.pokemons if p.name == pokemon_name), None)
        if pokemon_to_release:
            self.pokemons.remove(pokemon_to_release)
            return f"You have release {pokemon_name}"
        return f"Pokemon is not caught"
    def trainer_data(self) -> str:
        result = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemons)}\n"
        for pok in self.pokemons:
            result += f"- {pok.pokemon_details()}"
        return result



# pokemon = Pokemon("Pikachu", 90)
# print(pokemon.pokemon_details())
# trainer = Trainer("Ash")
# print(trainer.add_pokemon(pokemon))
# second_pokemon = Pokemon("Charizard", 110)
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.add_pokemon(second_pokemon))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())






