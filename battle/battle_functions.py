import importlib.util
import random
# from importlib.machinery import SourceFileLoader

def load_pokemon_from_file(filepath):
    spec = importlib.util.spec_from_file_location("", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    # return SourceFileLoader("", filepath).load_module()
    return module

def pokemon_alive(poke1, poke2):
    return poke1.is_alive() and poke2.is_alive()

def simulate_battle(poke1, poke2):
    # Choose a random pokemon to start
    if random.randint(0, 1) == 1:
        attacking_poke, defending_poke = poke1, poke2
    else:
        attacking_poke, defending_poke = poke2, poke1

    print("Pokemon", attacking_poke.get_name(), "gets to start")

    while pokemon_alive(poke1, poke2):
        move = attacking_poke.choose_move(defending_poke)
        print(attacking_poke.get_name(), "chooses", move.get_name())
        inflicted = defending_poke.inflict(move, attacking_poke)
        print(attacking_poke.get_name(), "inflicts", inflicted, "damage on", defending_poke.get_name())

        attacking_poke, defending_poke = defending_poke, attacking_poke

    if attacking_poke.is_alive():
        winner = attacking_poke
    else:
        winner = defending_poke

    print("The winner is", winner.get_name(), "with", winner.hp, "HP left")
    return winner
