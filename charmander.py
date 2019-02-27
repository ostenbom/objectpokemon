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
