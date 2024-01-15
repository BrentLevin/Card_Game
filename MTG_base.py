from random import shuffle

class Creature:
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

class Deck:
    def __init__(self, deck_list):
        self.cards = deck_list

    def shuffle(self):
        self.cards = random.shuffle(self.cards)


class Hand(Deck):
    def __init__(self, hand_size = 0, hand = []):
        self.hand_size = hand_size
        self.hand = hand

    def draw_starting_hand(self):
        self.hand = self.hand.append(Deck.pop())

    def draw(self):
        hand.append(self.cards.pop())



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



deck_list = [
    high_sentinels_of_arashin
    , restoration_angel
    ]

my_deck = Deck(deck_list)


def main():
    # print(vars(RestorationAngel))
    # print(str(my_deck.cards()))
    print(random.shuffle([1,2,3,4,5]))
    for obj in my_deck.cards:
        print(shuffle(obj.name))


if __name__ == "__main__":
    main()
