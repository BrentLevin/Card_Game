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
    def __init__(self):
        self.hand = {} # if there is errors with this just put the if statement in
        # self.hand_size = len(self.hand) #Better to represent hand as a dictionary?

class Deck(Hand):
    def __init__(self, deck_list):
        self.deck = deck_list
        self.deck_size = len(deck_list)
        super().__init__()

    def shuffle_cards(self):
        random.shuffle(self.deck)

    def draw(self, number):
        for _ in range(number):
            if self.deck[-1] in self.hand.keys():
                self.hand[self.deck.pop()] += 1
            else:
                self.hand[self.deck.pop()] = 1
            self.deck_size = len(self.deck) #this might be wrong
        # self.hand_size = len(self.hand)

    def draw_starting_hand(self, starting_size = 7):
        self.draw(starting_size)

class BattleField:
    pass

class Graveyard:
    pass

class Exile:
    pass

class turn_interactions:
        
    def upkeep(self, turn):
        #untap everything and draw a card
        #change who's turn it is
        # change summoning sickness to false
        if turn == True:
            self.my_deck.draw(1)
            #untap
        elif turn == False:
            self.opponents_deck.draw(1)

    def mainphase1(self):
        #play cards
        pass 

    def declare_attackers(self):
        #choose attackes and their opponents
        pass

    def declare_blockers(self):
        #opponent chooses blockers
        pass
    
    def damage_resolves(self):
        pass

    def mainphase2(self):
        pass

    def endstep(self, turn):
        if turn == True:
            self.whose_turn = False
        if turn == False:
            self.whose_turn = True

    
    def dice_roll(self):
        roll = random.randint(1, 2)
        if roll == 1:
            return True
        else:
            return False

    def start_game(self):
        self.my_deck.shuffle_cards() 
        self.opponents_deck.shuffle_cards()
        self.my_deck.draw_starting_hand()
        self.opponents_deck.draw_starting_hand() # is there a better/cleaner way of coding this



class Game(Deck, turn_interactions):
    def __init__(self, our_decklist, opponents_decklist):
        self.my_deck = Deck(our_decklist)
        self.opponents_deck = Deck(opponents_decklist)
        self.whose_turn = self.dice_roll() # if true its our turn if false its opp turn

    def run_turn(self):
        self.upkeep(self.whose_turn)
        self.mainphase1()
        self.declare_attackers()
        self.declare_blockers()
        self.damage_resolves()
        self.mainphase2()
        self.endstep(self.whose_turn)

def main():
    pass

if __name__ == "__main__":
    main()
