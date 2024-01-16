import random

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
        # how to deal with dual lands
        # how to deal with land abilities and transformations

class Hand:
    def __init__(self, hand_size = 0, hand = []):
        self.hand_size = hand_size
        self.hand = hand

class Deck(Hand):
    def __init__(self, deck_list, deck_size):
        self.cards = deck_list
        self.deck_size = deck_size
        super().__init__()

    def shuffle_cards(self):
        random.shuffle(self.cards)

    def draw(self, number):
        for i in range(number):
            self.hand.append(self.cards.pop())
        self.hand_size = len(self.hand)

    def draw_starting_hand(self, starting_size = 7):
        self.draw(starting_size)

  

class turn_interactions:
    def upkeep(self):
        #untap everything and draw a card
        #change who's turn it is
        # change summoning sickness to false
        self.draw(1)

    def mainphase1(self):
        #play cards
        pass 

    def declare_attackers(self):
        #choose attackes and their opponents
        pass

    def declare_blockers(self):
        #opponent chooses blockers
        pass
    
    def declare_blockers(self):
        #opponent chooses blockers
        pass

    def mainphase2(self):
        pass

    def endstep(self):
        pass
    
class turn(turn_interactions):
    #maybe i could put whose turn it is in here
    def run_turn(self):
        self.upkeep()
        self.mainphase1()
        self.declare_attackers()
        self.mainphase2()
        self.endstep()

    #need something to import a deck list

def main():
    pass

if __name__ == "__main__":
    main()
