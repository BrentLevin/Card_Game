from MTG_base import *
from Cards import *
# pass a list of players? 
# pass a format

def main():
    round = Game()
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