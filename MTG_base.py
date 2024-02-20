import random
import sys
from Cards import object_list
# from utils import create_ids, import_deck

### To do with an individual
class Hand:
    def __init__(self):
        self.hand = [] # if there is errors with this just put the if statement in
        # self.hand_size = len(self.hand) #Better to represent hand as a dictionary?

class Deck(Hand):
    def __init__(self, deck_list):
        print("deck")
        self.deck = deck_list
        self.deck_size = len(deck_list)
        super().__init__()


    def import_deck(player_name):
        formatted_deck_list = []
        num = ["0","1","2","3","4","5","6","7","8","9"]

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
    ##### fix this
    def create_ids(formatted_deck_list): #maybe this goes in the players profile class
        check_list = []
        for card_object in formatted_deck_list:
            temp_id = card_object.name + str(" ") + str(random.randint(1,10000)) ### maybe I can replace spaces with _ here

            while temp_id in check_list:
                temp_id = card_object.name + str(" ") + str(random.randint(1,10000))

                if temp_id not in check_list:
                    check_list.append(temp_id)
            
            card_object.id = temp_id

        return formatted_deck_list


    def shuffle_cards(self):
        random.shuffle(self.deck)

    def draw(self, number = 1):
        for _ in range(number):
            card_to_add = self.active_player.deck.pop()
            self.active_player.hand.append(card_to_add)

            self.deck_size = len(self.active_player.deck) #this might be wrong
            self.hand_size = len(self.active_player.hand)

    def draw_starting_hand(self, starting_size = 7):
        self.draw(starting_size)




### field locations
class Battlefield:
    def __init__(self):
        super().__init__()
        print("battle")
        self.active_creatures = [] ## is there a way we don't need this? or is that too slow?
        self.active_artifacts = []
        self.active_lands = []
        self.active_enchantments = [] 
        self.total_player_battlefield = [] #are these better off as hash maps

class Graveyard:
    def __init__(self):
        self.graveyard_cards = [] #is last 3 from a graveyard ever a feature?

class Exile:
    def __init__(self):
        self.exile = []


class Player(Deck, Battlefield):
    def __init__(self, player_letter, life_total):
        self.deck_list = Deck.create_ids(Deck.import_deck(player_letter)) ### how to do this better, just have the functions in utils? ASK Yossman #when to use func in classes vs not in a class, how to condense create_ids to reference import_deck #oh and is there a better way to do the triple while loop
        self.player_letter = player_letter ### a,b,c,d to work with deck list, but eventually will be actual players name
        self.life_total = life_total
        super().__init__(self.deck_list)


### Gameplay
class turn_interactions:
        
    def upkeep(self):
        #untap everything and draw a card
        #change who's turn it is
        # change summoning sickness to false
        self.draw()
        for i in self.active_player.total_player_battlefield: ### fix
            i.tapped = False

#################################################################
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
        
    def who_is_active(self, whose_turn):
        if whose_turn == True:
            return self.player_a
        elif whose_turn == False:
            return self.player_b

    def start_game(self):
        self.my_deck.shuffle_cards() 
        self.opponents_deck.shuffle_cards()
        self.my_deck.draw_starting_hand()
        self.opponents_deck.draw_starting_hand() # is there a better/cleaner way of coding this



class Game(turn_interactions):
    def __init__(self):
        self.player_a = Player("a", 40)
        self.player_b = Player("b", 40)
        self.active_player = self.who_is_active(self.dice_roll()) # if true its our turn if false its opp turn


    def run_turn(self):
        self.upkeep()
        # self.mainphase1(self.whose_turn)
        self.declare_attackers()
        self.declare_blockers()
        self.damage_resolves()
        self.mainphase2()
        self.endstep(self.whose_turn)

def main():
    play_game = Game()
    # print(play_game.active_player.total_player_battlefield)
    # play_game.run_turn()

if __name__ == "__main__":
    main()
