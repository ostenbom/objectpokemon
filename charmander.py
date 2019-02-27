from basepokemon import BasePokemon, BaseAttack, Type

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(50)
        self.spend_attack(25)
        self.spend_defence(25)
        self.set_attack(Burn())

        self.set_type(Type.FIRE)

    def get_name(self):
        return "Charmander"

    def choose_attack(self, enemy):
        return self.get_attack_by_name("Burn")

class Burn(BaseAttack):
    def __init__(self):
        BaseAttack.__init__(self)
        self.choose_uses(5)
        self.set_type(Type.FIRE)

    def get_name(self):
        return "Burn"
