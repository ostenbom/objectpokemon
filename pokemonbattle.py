import sys
from battle.battle_functions import load_pokemon_from_file, simulate_battle

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

