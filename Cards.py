from MTG_base import *

restoration_angel = Creature(name = "Restoration Angel"
                        , colourless = 3
                        , coloured = ["white"] #maybe a hasmap
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flash = True
                        , flying = True
                        )

high_sentinels_of_arashin = Creature(name = "High Sentinels of Arashin"
                        , colourless = 3
                        , coloured = ["white"]
                        , faction = "Angel"
                        , power = 3
                        , toughness = 4
                        , flash = True
                        , flying = True
                        )

Forest = BasicLand(
    name = "Forest",
    colour = "Green"
    )

Swamp = BasicLand(
    name = "Swamp",
    colour = "Black"
)

Plains = BasicLand(
    name = "Plains",
    colour = "White"
)

Mountain = BasicLand(
    name = "Mountain",
    colour = "Red"
)

Island = BasicLand(
    name = "Island",
    colour = "Blue"
)

