MAX_POKE_SPEND = 100
MAX_ATTACK_SPEND = 150

class BasePokemon:
    def __init__(self):
        self.__spendpoints = MAX_POKE_SPEND
        self.__hp = 0
        self.__attack = 0
        self.__defence = 0
        self.__attacks = {}

    def get_name(self):
        return "anonymous pokemon"

    def get_hp(self):
        return self.__hp

    def get_attack_points(self):
        return self.__attack

    def get_defence_points(self):
        return self.__defence

    def is_alive(self):
        return self.__hp > 0

    def set_attack(self, attack):
        self.__attacks[attack.get_name()] = attack

    def get_attack(self, name):
        return self.__attacks[name]

    def spend_hp(self, hp):
        if self.__spendpoints - hp < 0:
            print("cannot allocate hp, over budget")
            return

        self.__spendpoints -= hp
        self.__hp += hp

    def spend_attack(self, attack):
        if self.__spendpoints - attack < 0:
            print("cannot allocate attack, over budget")
            return

        self.__spendpoints -= attack
        self.__attack += attack

    def spend_defence(self, defence):
        if self.__spendpoints - defence < 0:
            print("cannot allocate defence, over budget")
            return

        self.__spendpoints -= defence
        self.__defence += defence

    def inflict(self, attack, enemy_attack_points):
        attack_damage = attack.use()
        damage = attack_damage + enemy_attack_points - self.__defence
        inflict_points = damage if damage > 0 else 0
        self.__hp -= inflict_points

        return inflict_points


class BaseAttack:
    def __init__(self):
        self.__max_uses = 0
        self.__uses = 0
        self.__attack = 0

    def get_name(self):
        return "no_name_attack"

    def choose_uses(self, uses):
        if uses > MAX_ATTACK_SPEND:
            print("cannot allocate attack strength, uses exceeds attack")
            return

        self.__max_uses = uses
        self.__attack = MAX_ATTACK_SPEND / uses

    def use(self):
        if self.__uses >= self.__max_uses:
            print("out of uses")
            return

        self.__uses += 1
        return self.__attack
