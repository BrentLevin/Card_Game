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

def main():
    list_test = []
    for i in range(5):
        list_test.append("bob")
    print(list_test)

if __name__ == "__main__":
    main()