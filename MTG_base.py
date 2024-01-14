class Creature():
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
    
class Deck():
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def build_deck(self, card_list):
        for i in card_list:
            self.add_card(i)

    #need something to import a deck list
        

restoration_angel = Creature(name = "Restoration Angel"
                        , cardtype = "Creature"
                        , colourless = 3
                        , coloured = ["w"]
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flash = True
                        , flying = True
                        )

high_sentinels_of_arashin = Creature(name = "High Sentinels of Arashin"
                        , cardtype = "Creature"
                        , colourless = 3
                        , coloured = ["w"]
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flash = True
                        , flying = True
                        )


my_deck = Deck()

deck_list = [high_sentinels_of_arashin,restoration_angel]

my_deck.build_deck(deck_list)

# for i in deck_list:
#     my_deck.add_card(i)

def main():
    # print(vars(RestorationAngel))
    # print(str(my_deck.cards()))
    for obj in my_deck.cards:
        print(obj.name)


if __name__ == "__main__":
    main()

