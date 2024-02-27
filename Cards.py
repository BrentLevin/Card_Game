from Card_Objects import *

restoration_angel = Creature(
    name = "Restoration Angel"
    , colourless_cost = 3
    , coloured_cost = ["white"] #maybe a hasmap
    , faction = "Angel"
    , power = 3
    , toughness = 4
    , flash = True
    , flying = True
    # , id = 1
    )

high_sentinels_of_arashin = Creature(
    name = "High Sentinels of Arashin"
    , colourless_cost = 3
    , coloured_cost = ["white"]
    , faction = "Angel"
    , power = 3
    , toughness = 4
    , flying = True
    # , id = 1
    )

forest = BasicLand(
    name = "Forest",
    colour = "Green",
    coloured = ["G"] #maybe a hash map
    )

swamp = BasicLand(
    name = "Swamp",
    colour = "Black",
    coloured = ["Bla"] 
    )

plains = BasicLand(
    name = "Plains",
    colour = "White",
    coloured = ["W"] 
    )

mountain = BasicLand(
    name = "Mountain",
    colour = "Red",
    coloured = ["R"] 
    )

island = BasicLand(
    name = "Island",
    colour = "Blue",
    coloured = ["Blu"] 
    )

object_list = {
    "Restoration Angel": restoration_angel,
    "High Sentinels of Arashin": high_sentinels_of_arashin,
    "Forest": forest,
    "Swamp": swamp,
    "Plains": plains,
    "Mountain": mountain,
    "Island": island
    }
