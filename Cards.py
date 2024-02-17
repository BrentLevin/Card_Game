from Card_Objects import *

restoration_angel = Creature(name = "Restoration Angel"
                        , colourless = 3
                        , coloured = ["white"] #maybe a hasmap
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flash = True
                        , flying = True
                        # , id = 1
                        )

high_sentinels_of_arashin = Creature(name = "High Sentinels of Arashin"
                        , colourless = 3
                        , coloured = ["white"]
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flying = True
                        # , id = 1
                        )

forest = BasicLand(
    name = "Forest",
    colour = "Green"
    )

swamp = BasicLand(
    name = "Swamp",
    colour = "Black"
)

plains = BasicLand(
    name = "Plains",
    colour = "White"
)

mountain = BasicLand(
    name = "Mountain",
    colour = "Red"
)

island = BasicLand(
    name = "Island",
    colour = "Blue"
)

object_list = {"Restoration Angel": restoration_angel,
               "High Sentinels of Arashin": high_sentinels_of_arashin,
               "Forest": forest,
               "Swamp": swamp,
               "Plains": plains,
               "Mountain": mountain,
               "Island": island}
