from Card_Objects import *

restoration_angel = Creature(
    name = "Restoration Angel"
    , cost = {"Colourless": 3, "White" : 1} #maybe a hasmap
    , faction = "Angel"
    , power = 3
    , toughness = 4
    , flash = True
    , flying = True
    # , id = 1
    )

high_sentinels_of_arashin = Creature(
    name = "High Sentinels of Arashin"
    , cost = {"Colourless": 3, "White" : 1}
    , faction = "Angel"
    , power = 3
    , toughness = 4
    , flying = True
    # , id = 1
    )

forest = BasicLand(
    name = "Forest",
    colour = "Green",
    mana_producable = {"Green" : 1} #maybe a hash map
    )

swamp = BasicLand(
    name = "Swamp",
    colour = "Black",
    mana_producable = {"Black" : 1} 
    )

plains = BasicLand(
    name = "Plains",
    colour = "White",
    mana_producable = {"White" : 1}
    )

mountain = BasicLand(
    name = "Mountain",
    colour = "Red",
    mana_producable = {"Red" : 1} 
    )

island = BasicLand(
    name = "Island",
    colour = "Blue",
    mana_producable = {"Blue" : 1}
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
