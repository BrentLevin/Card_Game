import random
import sys
from Cards import object_list, plains
# from utils import create_ids, import_deck

### To do with an individual
class Hand:
    def __init__(self):
        self.hand = {}

class Deck(Hand):
    def __init__(self, deck_list):
        self.deck = deck_list
        super().__init__()


    def import_deck(player_name):
        formatted_deck_list = {}
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
            
            if num_of_cards != 0:
                formatted_deck_list[line[i+1:]] = num_of_cards

        return formatted_deck_list
        

    def create_ids(formatted_deck_list): #maybe this goes in the players profile class
        ided_deck = {}
        for name, quantity in formatted_deck_list.items():
            while quantity > 0:
                key = name + str(" ") + str(random.randint(1,10000)) ### maybe I can replace spaces with _ here

                while key in ided_deck.keys():
                    key = name + str(" ") + str(random.randint(1,10000))

                value = object_list[name] #the value is the object pair in the dictionary based on the name being passed in # Land("Plains") ### fix
                ided_deck[key] = value

                quantity -= 1

        return ided_deck

    def draw(self):
        print(self.active_player.deck.pop())

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
        
list_a = [plains,plains,plains,plains,plains,plains ]

class Player(Deck):
    def __init__(self, player_letter, life_total):
        # self.deck_list = list_a
        self.deck_list = Deck.create_ids(Deck.import_deck(player_letter))
        self.player_letter = player_letter 
        self.life_total = life_total
        super().__init__(self.deck_list)

class turn_interactions:
        
    def upkeep(self):
        self.draw()

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


class Game(Deck, turn_interactions):
    def __init__(self):
        self.player_a = Player("a", 40)
        self.player_b = Player("b", 40)
        self.active_player = self.who_is_active(self.dice_roll()) 


def main():
    play_game = Game()
    print(play_game.active_player.deck)

if __name__ == "__main__":
    main()
