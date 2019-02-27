from basepokemon import BasePokemon, BaseAttack

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(50)
        self.spend_attack(25)
        self.spend_defence(25)
        self.set_attack(Burn())

    def get_name(self):
        return "Charmander"

    def choose_attack(self):
        return self.get_attack("Burn")

class Burn(BaseAttack):
    def __init__(self):
        BaseAttack.__init__(self)
        self.choose_uses(5)

    def get_name(self):
        return "Burn"
