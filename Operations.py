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



def main():
    StartGame(deck_list1, deck_list2)
    StartGame.my_deck

if __name__ == "__main__":
    main()