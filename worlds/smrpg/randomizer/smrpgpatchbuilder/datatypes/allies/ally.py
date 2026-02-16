"""Ally/Character data structures for Super Mario RPG."""

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell
    from smrpgpatchbuilder.datatypes.items.classes import Item, Weapon, Armor, Accessory

@dataclass
class LevelUp:
    """Level-up stats for a character at a specific level."""
    level: int
    exp_needed: int
    spell_learned: type['CharacterSpell'] | None
    hp_plus: int
    attack_plus: int
    defense_plus: int
    mg_attack_plus: int
    mg_defense_plus: int
    hp_plus_bonus: int
    attack_plus_bonus: int
    defense_plus_bonus: int
    mg_attack_plus_bonus: int
    mg_defense_plus_bonus: int

@dataclass
class AllyCoordinate:
    """Battle coordinates for an ally character."""
    cursor_x: int
    cursor_y: int
    sprite_abxy_y: int
    cursor_x_scarecrow: int
    cursor_y_scarecrow: int
    sprite_abxy_y_scarecrow: int

@dataclass
class Ally:
    """Represents a playable character (ally) in Super Mario RPG.

    There are 5 allies total: Mario, Mallow, Geno, Bowser, and Toadstool (Peach).
    """
    index: int  # 0-4
    name: str

    # Starting stats
    starting_level: int
    starting_current_hp: int
    starting_max_hp: int
    starting_speed: int
    starting_attack: int
    starting_defense: int
    starting_mg_attack: int
    starting_mg_defense: int
    starting_experience: int
    starting_weapon: type['Weapon'] | None
    starting_armor: type['Armor'] | None
    starting_accessory: type['Accessory'] | None
    starting_magic: list[type['CharacterSpell']]  # List of spells the character starts with

    # Level-up data (levels 2-30, total 29 levels)
    levels: list[LevelUp]

    # Battle coordinates
    coordinates: AllyCoordinate
