from Cards import *
# class Land():
#     def __init__(self, name):
#         self.name = name

# Plains = Land("Plains")

# a = {"Plains": Plains} #have a dictionary mapping objects to their string name

# deck = ["Plains"] #have a list of strings from the imported deck so as to create the decklist of objects
# newdeck = [] #decklist of objects

# for i in deck: #for every string in the imported deck list (can we do this straight from the import? no its better to have it in a standardised converted format) find the equivalent object
#     newdeck.append(a[i])

# for i in newdeck:
#     print(i.name)

# print(newdeck)
#####
# list_a = ["bob","bob","bob","bob","bob" ]
# list_b = ["tommy","tommy","tommy","tommy","tommy" ]

# class Deck:
#     def __init__(self, list_of_cards):
#         self.cards = list_of_cards

#     def draw(self):
#         print(self.active_player.cards.pop())

# class Player(Deck):
#     def __init__(self, name, list_of_cards):
#         self.name = name
#         super().__init__(list_of_cards)

# class Game(Player):
#     def __init__(self):
#         self.player_a = Player("a", list_a)
#         self.player_b = Player("b", list_b)
#         self.active_player = self.player_a


# def main():
#     active_game = Game()
#     active_game.draw()

# if __name__ == "__main__":
#     main()
####

# class Creature:
#     def __init__(self, name):
#         self.name = name

# def main():
#     x = Creature("bob")
#     a = x
#     b = x
#     print(a.name)
#     print(b.name)
#     print(x.name)
#     a.name = "taylor"
#     print(a.name)
#     print(b.name)
#     print(x.name)

# if __name__ == "__main__":
#     main()

# class Land:
#     def __init__(self, name = "placeholder"):
#         self.name = name
#         self.height = 50

# def create_card(name):
#     name = card_dict.get(name)
#     name.name = name

# card_dict = {"Plains": Land(),
#             "Swamp" : Land()}


# def main():
#     create_card("Plains")
#     "Plains".name

###

# import random
# import sys
# from Cards import object_list
# # from utils import create_ids, import_deck

# ### To do with an individual
# class Hand:
#     def __init__(self):
#         self.hand = [] # if there is errors with this just put the if statement in
#         # self.hand_size = len(self.hand) #Better to represent hand as a dictionary?

# class Deck(Hand):
#     def __init__(self):
#         pass


#     def import_deck(player_name):
#         formatted_deck_list = []
#         num = ["0","1","2","3","4","5","6","7","8","9"]

#         with open("deck_" + str(player_name) + ".txt") as f:
#             lines = list(map(str.strip, f.readlines()))

#         for line in lines:
#             num_of_cards = 0
#             i = 0

#             while i < len(line) and line[i] in num:
#                 num_of_cards *= 10
#                 num_of_cards += int(line[i])
#                 i += 1
            
#             card_name = line[i+1:]
           
#             for _ in range(num_of_cards):
#                 formatted_deck_list.append(object_list[card_name])

#         return formatted_deck_list
        
#     ### probably want some in built error throwing in this too
#     ### maybe theres a way to read in other deck formats automatically figuring out which is which
#     ### also how to read in multiple decks at once and indetify whose is whos

#     def create_ids(formatted_deck_list): #maybe this goes in the players profile class
#         check_list = []

#         for card_object in formatted_deck_list:
#             card_id = card_object.name + str(" ") + str(random.randint(1,10000)) ### maybe I can replace spaces with _ here

#             while card_id in check_list:
#                 card_id = card_object.name + str(" ") + str(random.randint(1,10000))

#                 if card_id not in check_list:
#                     check_list.append(card_id)
            
#             card_object.id = card_id

#         return formatted_deck_list


#     def shuffle_cards(self):
#         random.shuffle(self.deck)

#     def draw(self, number = 1):
#         for _ in range(number):
#             card_to_add = self.active_player.deck.pop()
#             self.active_player.hand.append(card_to_add)

#             self.deck_size = len(self.active_player.deck) #this might be wrong
#             self.hand_size = len(self.active_player.hand)

#     def draw_starting_hand(self, starting_size = 7):
#         self.draw(starting_size)

#     def discard():
#         pass

#     def mulligan():
#         pass

# class Player:
#     def __init__(self, player_name, life_total, deck_list = []):
#         self.deck_list = deck_list ### how to do this better, just have the functions in utils? ASK Yossman #when to use func in classes vs not in a class, how to condense create_ids to reference import_deck #oh and is there a better way to do the triple while loop
#         self.player_name = player_name ### a,b,c,d to work with deck list, but eventually will be actual players name
#         self.life_total = life_total

# class InitialisingEverything:
#     def __init__(self, number_of_players, players = []):
#         self.players = players
#         self.initialise_players(number_of_players)
#         self.initialise_decks()


#     def initialise_players(self,number_of_players):
#         for i in range(number_of_players):
#             self.players.append(Player(chr(97 + i), 40))

#     def initialise_decks(self):
#         for i in self.players:
#             i.deck_list = Deck.create_ids(Deck.import_deck(i.player_name)) #clean this up, but basically we are adding each players deck to their player object

# def main():
#     play_game = InitialisingEverything(2)
#     for i in play_game.players:
#         for j in i.deck_list:
#             print(j.name)
#         print("")

###

# from dataclasses import dataclass

# @dataclass
# class Bob:
#     name: str
#     age: int = 10

#     @dataclass
#     def method(self):
#         height: int = 120

# def main():
#     x = Bob("bob")
#     print(x.height)

# import random
# def main():
#     print(random.randint(0,4))

import random
import sys
from Cards import object_list

# from utils import create_ids, import_deck

### To do with an individual

class Deck:
    def draw(self, number = 1):
        for _ in range(number):
            print("")
            print(self.player_name)
            print(len(self.hand)) ####why are they sharing a hand???????????????????????????
            print(len(self.deck))
            card_to_add = self.deck.pop()
            self.hand.append(card_to_add)
    
    def draw_starting_hand(self, starting_size: int = 7):
        Deck.draw(self, starting_size)


class Player:
    def __init__(self, player_name, life_total, deck_list = [], hand = []):
        self.deck = deck_list 
        self.life_total = life_total
        self.player_name = player_name ### a,b,c,d to work with deck list, but eventually will be actual players name
        self.hand = hand

class TurnInteractions:
        
    @staticmethod
    def dice_roll(number_of_players):
        roll = random.randint(0, number_of_players - 1)
        return roll
        
    def who_is_active(self, whose_turn):
        return self.players[whose_turn]

    def start_game(self, number_of_players):
        self.active_player = TurnInteractions.who_is_active(self, TurnInteractions.dice_roll(number_of_players))

        for player in self.players: #order with mulligans?
            Deck.draw_starting_hand(player)


class InitialisingEverything:
    def __init__(self, number_of_players, players = []):
        self.players = players
        self.initialise_players(number_of_players)
        self.initialise_decks(deck_list_prac)
        self.active_player = None

    def initialise_players(self,number_of_players):
        for i in range(number_of_players):
            self.players.append(Player(chr(97 + i), 40))

    def initialise_decks(self, deck):
        for i in self.players:
            i.deck = deck

class Game(InitialisingEverything):
    def __init__(self, number_of_players):
        super().__init__(number_of_players)
        TurnInteractions.start_game(self, number_of_players)

deck_list_prac = [plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains, plains]


def main():
    play_game = Game(2)
    Deck.draw(play_game.active_player)
    Deck.draw(play_game.active_player)
    assert play_game.players[0].life_total == play_game.players[1].life_total

if __name__ == "__main__":
    main()