from MTG_base import *
from Cards import *

my_deck_list = [
    high_sentinels_of_arashin
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
    , Plains
]

opp_deck_list = [
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



def main():
    round = Game(my_deck_list, opp_deck_list)
    round.start_game()
    print(round.whose_turn)
    print(len(round.my_deck.hand))
    print(len(round.opponents_deck.hand))
    round.run_turn()
    print(round.whose_turn)


    round.run_turn()
    print(round.my_deck.deck)
    print(round.opponents_deck.deck)
    print(round.whose_turn)

    for obj, value in round.opponents_deck.hand.items():
        print(obj.name, value)

if __name__ == "__main__":
    main()