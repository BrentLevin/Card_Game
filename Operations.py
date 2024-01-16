from MTG_base import *
from Cards import *

deck_list = [
    high_sentinels_of_arashin
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    , restoration_angel
    ]

deck_size = len(deck_list)

my_deck = Deck(deck_list, deck_size)


def main():
    # print(vars(restoration_angel))
    # print(str(my_deck.cards()))
    my_deck.shuffle_cards() 
    # for obj in my_deck.cards:
    #     print(obj.name)
    my_deck.draw_starting_hand()
    for obj in my_deck.hand:
        print(obj.name)

if __name__ == "__main__":
    main()