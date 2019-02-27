# Object Pokemon
Create pokemon! Battle them against eachother! Achieve victory!

This is an exercise in creating python objects aimed at those with a small amount of python experience but no experience with objects.

### The Rules
- Pokemon have 100 base hp
- Pokemon may spend 100 extra points on HP, attack or defence
- A pokemon with 0 HP is dead
- Defence increases your chance of dodging an attack, up to 50%
- Attack is your base damage inflicted on each move
- No more than 4 move types allowed
- Your type of pokemon / attack will decide your *multiplier* according to the following table

| Attack\Defend | Water | Fire | Earth | Normal |
|---------------|-------|------|-------|--------|
| Water         | 1     | 2    | 0.5   | 1      |
| Fire          | 0.5   | 1    | 2     | 1      |
| Earth         | 2     | 0.5  | 1     | 1      |
| Normal        | 0.75  | 0.75 | 0.75  | 1      |

### Make your pokemon
- Extend the `BasePokemon` and `BaseMove` classes and implement your Pokemon

```
from basepokemon import BasePokemon, BaseMove, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(50)
        self.spend_attack(25)
        self.spend_defence(25)
        self.add_move(Burn())

        self.set_type(Type.FIRE)

    def get_name(self):
        return "Charmander"

    def choose_move(self, enemy):
        return self.get_move_by_name("Burn")

class Burn(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Burn"
```

### Usage

```
python3 pokemonbattle.py pokemonfile1.py pokemonfile2.py (num_battles)
```
