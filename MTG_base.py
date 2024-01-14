class Card:
    def __init__(self, name, cardtype, faction, power, toughness, colourless = 0, coloured = [], flash: bool = False, flying: bool = False):
        self.name = name
        self.colourless = colourless
        self.coloured = coloured
        self.cardtype = cardtype
        self.faction = faction
        self.power = power
        self.toughness = toughness
        self.flash = flash
        self.flying = flying

RestorationAngel = Card(name = "Restoration Angel"
                        , cardtype = "Creature"
                        , colourless = 3
                        , coloured = ["w"]
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flash = True
                        , flying = True
                        )


def main():
    print(vars(RestorationAngel))

if __name__ == "__main__":
    main()