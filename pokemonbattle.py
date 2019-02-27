import sys
import importlib.util
import random

def load_pokemon_from_file(filepath):
    spec = importlib.util.spec_from_file_location("", filepath)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

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


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("usage: python singlepokemonbattle.py pokemon1.py pokemon2.py (numBattles)")
        sys.exit(1)

    print("loading pokemon1 from", sys.argv[1])
    poke_mod_1 = load_pokemon_from_file(sys.argv[1])
    print("loading pokemon2 from", sys.argv[2])
    poke_mod_2 = load_pokemon_from_file(sys.argv[2])

    num_battles = 1 if len(sys.argv) <= 3 else int(sys.argv[3])

    p1_wins = 0
    p2_wins = 0

    for i in range(num_battles):
        p1 = poke_mod_1.Pokemon()
        p2 = poke_mod_2.Pokemon()
        winner = simulate_battle(p1, p2)
        if winner == p1:
            p1_wins += 1
        else:
            p2_wins += 1
        print()

    print(poke_mod_1.Pokemon().get_name(), "won", p1_wins)
    print(poke_mod_2.Pokemon().get_name(), "won", p2_wins)

