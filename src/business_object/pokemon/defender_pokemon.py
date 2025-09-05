from src.business_object.pokemon.abstract_pokemon import AbstracPokemon


class DefenderPokemon(AbstracPokemon):
    def get_pokemon_attack_coef(self) -> float:
        multiplier = 1+(self.defense_current + self.attack_current)/200
        return multiplier
