from enum import Enum

MAX_POKE_SPEND = 100
MAX_ATTACK_SPEND = 150


class Type(Enum):
    WATER = 1
    FIRE = 2
    EARTH = 3
    NORMAL = 4


class BasePokemon:
    def __init__(self):
        self.__spendpoints = MAX_POKE_SPEND
        self.hp = 0
        self.attack_points = 0
        self.defence_points = 0
        self.__attacks = {}
        self.type = Type.NORMAL

    def get_name(self):
        return "anonymous pokemon"

    def is_alive(self):
        return self.hp > 0

    def set_type(self, poke_type):
        check = Type[poke_type.name]
        self.type = check

    def set_attack(self, attack):
        self.__attacks[attack.get_name()] = attack

    def get_attack(self, name):
        return self.__attacks[name]

    def spend_hp(self, hp):
        if self.__spendpoints - hp < 0:
            print("cannot allocate hp, over budget")
            return

        self.__spendpoints -= hp
        self.hp += hp

    def spend_attack(self, attack):
        if self.__spendpoints - attack < 0:
            print("cannot allocate attack, over budget")
            return

        self.__spendpoints -= attack
        self.attack_points += attack

    def spend_defence(self, defence):
        if self.__spendpoints - defence < 0:
            print("cannot allocate defence, over budget")
            return

        self.__spendpoints -= defence
        self.defence_points += defence

    def inflict(self, attack, enemy):
        attack_damage = attack.use()
        pokemon_type_multiplier = self.__get_multiplier(enemy.type, self.type)
        attack_multiplier = self.__get_multiplier(attack.type, self.type)
        damage = (attack_multiplier * attack_damage) + (pokemon_type_multiplier * enemy.attack_points) - self.defence_points
        inflict_points = damage if damage > 0 else 0
        self.hp -= inflict_points

        return inflict_points

    def __get_multiplier(self, attacking_type, defending_type):
        return multiplier_table[attacking_type][defending_type]


class BaseAttack:
    def __init__(self):
        self.max_uses = 0
        self.uses = 0
        self.attack = 0
        self.type = Type.NORMAL

    def get_name(self):
        return "no_name_attack"

    def choose_uses(self, uses):
        if uses > MAX_ATTACK_SPEND:
            print("cannot allocate attack strength, uses exceeds attack")
            return

        self.max_uses = uses
        self.attack = MAX_ATTACK_SPEND / uses

    def set_type(self, poke_type):
        check = Type[poke_type.name]
        self.type = check

    def use(self):
        if self.uses >= self.max_uses:
            print("out of uses")
            return

        self.uses += 1
        return self.attack


multiplier_table = {
            Type.WATER: {
                    Type.WATER: 1,
                    Type.FIRE: 2,
                    Type.EARTH: 0.5,
                    Type.NORMAL: 1
                },
            Type.FIRE: {
                    Type.WATER: 0.5,
                    Type.FIRE: 1,
                    Type.EARTH: 2,
                    Type.NORMAL: 1
                },
            Type.EARTH: {
                    Type.WATER: 2,
                    Type.FIRE: 0.5,
                    Type.EARTH: 1,
                    Type.NORMAL: 1
                },
            Type.NORMAL: {
                    Type.WATER: 1,
                    Type.FIRE: 1,
                    Type.EARTH: 1,
                    Type.NORMAL: 1
                },
        }
