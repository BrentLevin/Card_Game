class Creature:
    def __init__(self, name, faction, power, toughness, cardtype = "Creature", colourless = 0, coloured = [], flash: bool = False, flying: bool = False, tapped = False, summoning_sickness = True):
        self.name = name
        self.colourless = colourless
        self.coloured = coloured
        self.cardtype = cardtype
        self.faction = faction
        self.power = power
        self.toughness = toughness
        self.flash = flash
        self.flying = flying
        self.tapped = tapped
        self.summoning_sickness = summoning_sickness


class BasicLand:
    def __init__(self, name, colour, cardtype = "BasicLand"):
        self.name = name
        self.colour = colour
        self.cardtype = cardtype

class NonBasicLand:
    def __init__(self, name, faction, cardtype = "NonBasicLand", colourless = 0, coloured = [], tapped = False):
        self.name = name
        self.colourless = colourless
        self.coloured = coloured
        self.cardtype = cardtype
        self.faction = faction
        self.tapped = tapped
        # self.id = id
        # how to deal with dual lands
        # how to deal with land abilities and transformations
