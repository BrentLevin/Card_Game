import random
from Cards import object_list

def import_deck():
    formatted_deck_list = {}
    num = ["0","1","2","3","4","5","6","7","8","9"]

    with open("MTG\\deck.txt") as f:
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
    
### maybe theres a way to read in other deck formats automatically figuring out which is which
### also how to read in multiple decks at once and indetify whose is whose

def create_ids(formatted_deck_list): #maybe this goes in the players profile class
    ided_deck = {}
    for name in formatted_deck_list:
        key = name + str(" ") + str(random.randint(1,10000)) ### maybe I can replace spaces with _ here

        while key in ided_deck.keys():
            key = name + str(" ") + str(random.randint(1,10000))

        value = object_list[name] #the value is the object pair in the dictionary based on the name being passed in # Land("Plains") ### fix
        ided_deck[key] = value

    return ided_deck


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

###

def main():
    # print(import_deck())
    formatted_deck_list = import_deck()
    x = create_ids(formatted_deck_list)
    for name in x:
        print(name)
        
if __name__ == "__main__":
    main()
