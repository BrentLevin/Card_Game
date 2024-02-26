import random
import sys
from Cards import object_list
from copy import copy
# from utils import create_ids, import_deck

### To do with an individual

class Deck:

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
                formatted_deck_list.append(copy(object_list[card_name])) ## better solution? also how to call copy.copy()

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

    @staticmethod #what does this actually do?
    def shuffle_cards(deck_to_shuffle):
        random.shuffle(deck_to_shuffle)

    def draw(self, number = 1):
        for _ in range(number):
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

    def remove_card_from_list(self, card_to_play, location_of_removal): #this feels slow, but remove is removing the wrong darn thing
        search_length = len(location_of_removal)

        for i in range(search_length):
            if location_of_removal[i] is card_to_play:
                del location_of_removal[i]
                break

    def pass_priority(self):
        if self.active_player_index == len(self.players) - 1:
                self.active_player_index = 0
        else:
            self.active_player_index += 1
            
        self.active_player = self.players[self.active_player_index] 

    def resolve_card_from_stack(self):
        self.active_player.total_player_battlefield.append(self.stack[-1]) #assumig it resolves to battle field sorcery resolves will be to different location
        del self.stack[-1]
        
    def play_card(self, start_player_index): #need constraints to maintain cards being played can actually be played whether it be at instant or sorcery speed
        finality_of_priority = 0

        while True:
            print(len(self.stack))
            card_to_play = None
            print("This is the stack ; ", [i.name for i in self.stack])
            print("Player", self.active_player.player_name, "to play:")

            for card in self.active_player.hand:
                    print(card.id)

            name_of_card_to_play = input("play_card [to skip type in 'pass']:    ")

            if name_of_card_to_play == "exit": ### for debugging
                exit()

            elif name_of_card_to_play == "pass":
                finality_of_priority += 1

                if finality_of_priority == len(self.players):
                    if len(self.stack) > 0:
                        Deck.resolve_card_from_stack(self) #make sure that active player is correct here to match the person who pLYAED IT BIG EJHFDWAJDWJKLADJKLA
                        self.active_player_index = start_player_index
                        self.active_player = self.players[self.active_player_index] #send it back to the person whose turn it is
                        finality_of_priority = 0

                    else:
                        break

                else:
                    Deck.pass_priority(self) # WHY DO I NEED TO PASS SELF IN HERE makes me think self is not functioning properly
             
            elif name_of_card_to_play != None:
                finality_of_priority = 0

                for card in self.active_player.hand: ## okay well can I actually afford to play said card?    # depending on card type go and add to that part of the battlefield tooc
                    if name_of_card_to_play == card.id:
                        card_to_play = card
                        Deck.remove_card_from_list(self, card_to_play, self.active_player.hand)
                        self.stack.append(card_to_play)
                        break

                if card_to_play == None: #print an error only if the for loop cant find anything
                    print("error: " + name_of_card_to_play + " not in hand")
                    
             

    

class Player:
    def __init__(self, player_name, life_total):
        self.deck = []
        self.player_name = player_name ### a,b,c,d to work with deck list, but eventually will be actual players name
        self.life_total = life_total
        self.hand = []

        self.initialise_player_tablespace()

    def initialise_player_tablespace(self): ### is this bad practice?
        self.active_creatures = []
        self.active_artifacts = []
        self.active_lands = []
        self.active_enchantments = [] 
        self.total_player_battlefield = [] 
        self.graveyard_cards = []
        exile = [] #this is shared therefore no self?


### Gameplay
class TurnInteractions:
        
    def upkeep(self):
        #untap everything and draw a card
        #change who's turn it is
        # change summoning sickness to false
        if self.every_turn_counter > 0:
            Deck.pass_priority(self)
        
        self.every_turn_counter += 1
        self.exact_turn_counter = self.every_turn_counter % 4

        Deck.draw(self.active_player)
        for i in self.active_player.total_player_battlefield: ### fix
            i.tapped = False

    def mainphase1(self):
        Deck.play_card(self, self.active_player_index)

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

    def endstep(self):
        pass


    @staticmethod
    def dice_roll(number_of_players):
        roll = random.randint(0, number_of_players - 1)
        return roll

    def start_game(self, number_of_players):
        self.active_player_index = TurnInteractions.dice_roll(number_of_players)
        self.active_player = self.players[self.active_player_index]

        for player in self.players: #order with mulligans?
            Deck.shuffle_cards(player.deck) 
            Deck.draw_starting_hand(player)

    def run_turn(self):
        TurnInteractions.upkeep(self)
        TurnInteractions.mainphase1(self)
        TurnInteractions.declare_attackers(self)
        TurnInteractions.declare_blockers(self)
        TurnInteractions.damage_resolves(self)
        TurnInteractions.mainphase2(self)
        TurnInteractions.endstep(self)


class InitialisingEverything:
    def __init__(self, number_of_players):
        self.players = []
        self.stack = []
        self.initialise_players(number_of_players)
        self.initialise_decks()
        self.active_player = None
        self.active_player_index = None
        self.every_turn_counter = 0
        self.exact_turn_counter = self.every_turn_counter % 4

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


    TurnInteractions.run_turn(play_game)
  

 
    # for i in play_game.active_player.total_player_battlefield:
    #     print(i.id)
    #     print("")
    #     print(len(play_game.active_player.hand))


if __name__ == "__main__":
    main()
