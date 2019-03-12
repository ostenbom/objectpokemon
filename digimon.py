from basepokemon import BasePokemon, BaseMove

class Pokemon(BasePokemon):
    def __init__(self):
        BasePokemon.__init__(self)
        # Has to sum to 100
        self.spend_hp(1)
        self.spend_attack(0)
        self.spend_defence(99)
        self.add_move(Burn())
        self.add_move(LargeSMile())
        self.add_move(ToTAL_CARNAGE())
        self.add_move(Chunk())
        self.move = 0
        self.moves = ['Burn', "LargeSMile ;) <:^)~", "Chew me!", "get CHUNKED!"]


    def get_name(self):
        return "Digimon!"

    def choose_move(self, enemy):
        mov = self.moves[self.move]
        self.move = self.move + 1 if self.move < len(self.moves) - 1 else 0
        return self.get_move_by_name(mov)

class Burn(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "Burn"

class LargeSMile(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "LargeSMile ;) <:^)~"


class ToTAL_CARNAGE(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "Chew me!"


class Chunk(BaseMove):
    def __init__(self):
        BaseMove.__init__(self)
        self.choose_uses(1)

    def get_name(self):
        return "get CHUNKED!"


