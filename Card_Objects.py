from dataclasses import dataclass

@dataclass
class Creature:
        name: str
        colourless: int
        coloured: list
        faction: str
        power: int
        toughness: int
        flash: bool = False
        flying: bool = False
        tapped: bool = False
        summoning_sickness: bool = True
        cardtype: str = "Creature"


@dataclass
class BasicLand:
        name: str
        colour: list
        cardtype: str = "BasicLand"

@dataclass
class NonBasicLand:
        name: str
        colourless: int
        coloured: list
        faction: str
        tapped: bool
        cardtype: str = "NonBasicLand"

        # how to deal with dual lands
        # how to deal with land abilities and transformations
