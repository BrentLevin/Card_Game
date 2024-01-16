from MTG_base import *
from Cards import *

deck_list1 = [
    high_sentinels_of_arashin
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
]

deck_list2 = [
    restoration_angel
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , restoration_angel
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
]

my_deck = Deck(deck_list1)
opponents_deck = Deck(deck_list2)

def main():
    my_deck.shuffle_cards() 
    opponents_deck.shuffle_cards()

    # print(opponents_deck.hand_size)
    # print(opponents_deck.hand)

    my_deck.draw_starting_hand()
    print(my_deck.hand_size)
    print(my_deck.hand)

    # opponents_deck.draw_starting_hand()
    # print(opponents_deck.hand_size)
    # print(opponents_deck.hand)

    opponents_deck.draw_starting_hand()
    print(my_deck.hand_size)
    print(my_deck.hand)

if __name__ == "__main__":
    main()