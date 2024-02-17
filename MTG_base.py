import random
import sys
from Cards import object_list
from utils import create_ids, import_deck

### To do with an individual
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
            self.card_to_add = self.deck.pop()
            print(self.card_to_add)
            if self.card_to_add.name in self.hand.keys():
                self.hand[self.card_to_add.name].append(self.card_to_add)
            else:
                self.hand[self.card_to_add.name] = [self.card_to_add]
            self.deck_size = len(self.deck) #this might be wrong
            self.hand_size = len(self.hand)

    def draw_starting_hand(self, starting_size = 7):
        self.draw(starting_size)

class Player(Deck):
    def __init__(self, player_letter, life_total):
        self.formatted_deck_list = import_deck(player_letter)
        self.deck_list = create_ids(self.formatted_deck_list)
        self.player_letter = player_letter ### a,b,c,d to work with deck list, but eventually will be actual players name
        self.life_total = life_total
        super.__init__(self.deck_list)


### field locations
class BattleField:
    def __init__(self):
        self.active_creatures = {} ## is there a way we don't need this? or is that too slow?
        self.active_artifacts = {}
        self.active_lands = {}
        self.active_enchantments = {} 
        self.total_battlefield = {} #are these better off as hash maps

class Graveyard:
    def __init__(self):
        self.graveyard_cards = {} #is last 3 from a graveyard ever a feature?

class Exile:
    def __init__(self):
        self.exile = {}


### Gameplay
class turn_interactions:
        
    def upkeep(self, turn):
        #untap everything and draw a card
        #change who's turn it is
        # change summoning sickness to false
        if turn == True:
            self.my_deck.draw(1)
            for i in self.my_battlefield.total_battlefield: ### fix
                i.tapped = False
        elif turn == False:
            self.opponents_deck.draw(1)
            for i in self.opp_battlefield.total_battlefield:
                i.tapped = False

    def mainphase1(self, turn):
        #play cards
        if turn == True:
            for key, value in self.my_deck.hand.items():
                print(key, value)
            print(">>>>", self.my_deck.hand)
            self.play_card = input("play_card: ")  #could do a while loop, then end and pass # THIS DOESN'T WORK BECAUSE THE DICT IS holding OBJECTS NOT NAMES is there a way that i can have names in the dict represent objects?
            if self.my_deck.hand[self.play_card]:
                self.my_deck.hand[self.play_card] -= 1
                self.my_battlefield.total_battlefield[self.play_card] += 1 # depending on card type go and add to that part of the battlefield too
                
            else:
                print("error: " + self.play_card + " not in hand")
                exit() # probably instead of exiting i want to go back to the input.
        else: 
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
        self.player_a = Player("a")
        self.player_a_battlefield = BattleField()
        self.player_b = Deck("b")
        self.opp_battlefield = BattleField()
        self.whose_turn = self.dice_roll() # if true its our turn if false its opp turn


    def run_turn(self):
        self.upkeep(self.whose_turn)
        # self.mainphase1(self.whose_turn)
        self.declare_attackers()
        self.declare_blockers()
        self.damage_resolves()
        self.mainphase2()
        self.endstep(self.whose_turn)

def main():
    pass

if __name__ == "__main__":
    main()
