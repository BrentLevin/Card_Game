from MTG_base import *
from Cards import *

my_deck_list = [
    high_sentinels_of_arashin
    , Plains_1
    , Plains_2
    , Plains_3
    , Plains_4
    , Plains_5
    , Plains_6
    , Plains_7
    , Plains_8
    , Plains_9
    , Plains_10
    , Plains_11
]

opp_deck_list = [
    restoration_angel
    , Plains_1
    , Plains_2
    , Plains_3
    , Plains_4
    , Plains_5
    , Plains_6
    , Plains_7
    , Plains_8
    , Plains_9
    , Plains_10
    , Plains_11
]



def main():
    round = Game(my_deck_list, opp_deck_list)
    round.start_game()
    print(round.whose_turn)
    # print(len(round.my_deck.hand))
    # print(len(round.opponents_deck.hand))
    round.run_turn()
    print(round.whose_turn)


    round.run_turn()
    print(round.my_deck.hand)
    print(round.opponents_deck.hand)
    print(round.whose_turn)

    # for obj, value in round.opponents_deck.hand.items():
    #     print(obj.name, value)

if __name__ == "__main__":
    main()