# Object Pokemon
Create pokemon! Battle them against eachother! Achieve victory!

This is an exercise in creating python objects aimed at those with a small amount of python experience but no experience with objects.

### The Rules
- Pokemon have 100 base hp
- Pokemon may spend 100 extra points on HP, attack or defence
- A pokemon with 0 HP is dead
- Defence increases your chance of dodging an attack, up to 50%
- Attack is your base damage inflicted on each move
- Your type of pokemon / attack will decide your *multiplier* according to the following table

| Attack\Defend | Water | Fire | Earth | Normal |
|---------------|-------|------|-------|--------|
| Water         | 1     | 2    | 0.5   | 1      |
| Fire          | 0.5   | 1    | 2     | 1      |
| Earth         | 2     | 0.5  | 1     | 1      |
| Normal        | 0.75  | 0.75 | 0.75  | 1      |

### Make your pokemon

### Usage

```
python3 pokemonbattle.py pokemonfile1.py pokemonfile2.py (num_battles)
```
