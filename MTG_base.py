import random
import sys
from Cards import object_list

# from utils import create_ids, import_deck

### To do with an individual

class Deck:
    def __init__(self):
        pass

    def import_deck(player_name):
        formatted_deck_list = []
        num = [str(i) for i in range(0,10)]

        with open("deck_" + str(player_name) + ".txt") as f:
            lines = list(map(str.strip, f.readlines()))

        for line in lines:
            num_of_cards = 0
            i = 0

            while i < len(line) and line[i] in num:
                num_of_cards *= 10
                num_of_cards += int(line[i])
                i += 1
            
            card_name = line[i+1:]
           
            for _ in range(num_of_cards):
                formatted_deck_list.append(object_list[card_name])

        return formatted_deck_list
        
    ### probably want some in built error throwing in this too
    ### maybe theres a way to read in other deck formats automatically figuring out which is which
    ### also how to read in multiple decks at once and indetify whose is whos

    def create_ids(formatted_deck_list): #maybe this goes in the players profile class
        check_list = []

        for card_object in formatted_deck_list:
            card_id = card_object.name + str(" ") + str(random.randint(1,10000)) ### maybe I can replace spaces with _ here

            while card_id in check_list:
                card_id = card_object.name + str(" ") + str(random.randint(1,10000))

                if card_id not in check_list:
                    check_list.append(card_id)
            
            card_object.id = card_id

        return formatted_deck_list

    @staticmethod
    def shuffle_cards(deck_to_shuffle):
        random.shuffle(deck_to_shuffle)

    def draw(self, number = 1):
        for _ in range(number):
            print(self.deck)
            card_to_add = self.deck.pop()
            self.hand.append(card_to_add)

            self.deck_size = len(self.deck) #this might be wrong
            self.hand_size = len(self.hand)

    
    def draw_starting_hand(self, starting_size = 7):
        Deck.draw(self, starting_size)

    def discard():
        pass

    def mulligan():
        pass


class Player:
    def __init__(self, player_name, life_total, deck_list = [], hand = []):
        self.deck = deck_list 
        self.player_name = player_name ### a,b,c,d to work with deck list, but eventually will be actual players name
        self.life_total = life_total
        self.hand = hand
        self.initialise_player_tablespace()

    def initialise_player_tablespace(self): ### is this bad practice?
        self.active_creatures = []
        self.active_artifacts = []
        self.active_lands = []
        self.active_enchantments = [] 
        self.total_player_battlefield = [] 
        self.graveyard_cards = []
        exile = [] #this is sharedm therefore no self?



### Gameplay
class TurnInteractions:
        
    def upkeep(self):
        #untap everything and draw a card
        #change who's turn it is
        # change summoning sickness to false
        Deck.draw(self)
        for i in self.active_player.total_player_battlefield: ### fix
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

    @staticmethod
    def dice_roll(number_of_players):
        roll = random.randint(0, number_of_players - 1)
        return roll
        
    def who_is_active(self, whose_turn):
        return self.players[whose_turn]

    def start_game(self, number_of_players):
        self.acitve_player = TurnInteractions.who_is_active(self, TurnInteractions.dice_roll(number_of_players))

        for player in self.players: #order with mulligans?
            Deck.shuffle_cards(player.deck) 
            Deck.draw_starting_hand(player)

    def run_turn(self):
        self.upkeep()
        # self.mainphase1(self.whose_turn)
        self.declare_attackers()
        self.declare_blockers()
        self.damage_resolves()
        self.mainphase2()
        self.endstep(self.whose_turn)



class InitialisingEverything:
    def __init__(self, number_of_players, players = []):
        self.players = players
        self.initialise_players(number_of_players)
        self.initialise_decks()
        self.active_player = None

    def initialise_players(self,number_of_players):
        for i in range(number_of_players):
            self.players.append(Player(chr(97 + i), 40))

    def initialise_decks(self):
        for i in self.players:
            i.deck = Deck.create_ids(Deck.import_deck(i.player_name)) #clean this up, but basically we are adding each players deck to their player object


class Game(InitialisingEverything):
    def __init__(self, number_of_players):
        super().__init__(number_of_players)
        TurnInteractions.start_game(self, number_of_players)



def main():
    play_game = Game(2)
    for player in play_game.players:
        print("")
        print(player.player_name)
        for card in player.hand:
            print(card.name)
    # print(play_game.active_player.total_player_battlefield)
    # play_game.run_turn()

if __name__ == "__main__":
    main()
