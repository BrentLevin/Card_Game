from dataclasses import dataclass

@dataclass
class Creature:
        name: str
        cost: dict
        faction: str
        power: int
        toughness: int
        flash: bool = False
        flying: bool = False
        tapped: bool = False
        summoning_sickness: bool = True
        card_type: str = "Creature"
        mana_source = False

### something for artifact and for equipment and for planeswwalker
        
@dataclass
class BasicLand:
        name: str
        mana_producable: dict
        colour: str #idk if we need this
        card_type: str = "BasicLand"
        mana_source: bool = True
        tapped: bool = False

@dataclass
class NonBasicLand:
        name: str
        mana_producable: dict
        faction: str
        tapped: bool
        card_type: str = "NonBasicLand"
        mana_source = True
        tapped: bool = False

        # how to deal with dual lands
        # how to deal with land abilities and transformations
