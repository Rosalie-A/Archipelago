from typing import TYPE_CHECKING

from BaseClasses import Location
from rule_builder.rules import Rule
from .logic.regions import all_regions
from .logic import topologies # noqa
from .. import LocationNames

if TYPE_CHECKING:
    from worlds.smrpg import SMRPGWorld


class SMRPGLocation(Location):
    game = "Super Mario RPG"
    rule_builder_rule: Rule["SMRPGWorld"]


class LocationData:
    name: str
    id: int

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

id = 1
all_location_data: list[LocationData] = list()

for region in all_regions:
    for location in region.locations:
        new_location = LocationData(location.name, id)
        all_location_data.append(new_location)
        id += 1

character_locations: list[LocationNames] = [
    LocationNames.MUSHROOM_WAY_CHARACTER_RECRUIT,
    LocationNames.FOREST_MAZE_CHARACTER_RECRUIT,
    LocationNames.MOLEVILLE_MINES_CHARACTER_RECRUIT,
    LocationNames.MARRYMORE_CHARACTER_RECRUIT
]

boss_locations: list[LocationNames] = [
    LocationNames.MUSHROOM_WAY_BOSS_FIGHT,
    LocationNames.BANDITS_WAY_BOSS_FIGHT,
    LocationNames.MUSHROOM_KINGDOM_BOSS_FIGHT,
    LocationNames.MIMIC_CHEST_1_BOSS_FIGHT,
    LocationNames.KERO_SEWERS_BOSS_FIGHT,
    LocationNames.FOREST_MAZE_BOSS_FIGHT,
    LocationNames.MOLEVILLE_MINES_FIRST_BOSS_FIGHT,
    LocationNames.MOLEVILLE_MINES_SECOND_BOSS_FIGHT,
    LocationNames.BOOSTER_TOWER_CURTAIN_ROOM_BOSS_FIGHT,
    LocationNames.BOOSTER_TOWER_BALCONY_BOSS_FIGHT,
    LocationNames.MARRYMORE_BOSS_FIGHT,
    LocationNames.SUNKEN_SHIP_PASSWORD_BOSS_FIGHT,
    LocationNames.MIMIC_CHEST_2_BOSS_FIGHT,
    LocationNames.SUNKEN_SHIP_FINAL_BOSS_FIGHT,
    LocationNames.SEASIDE_TOWN_BOSS_FIGHT,
    LocationNames.LANDS_END_BELOME_TEMPLE_CLOUD_BOSS_FIGHT,
    LocationNames.BELOME_TEMPLE_BOSS_FIGHT,
    LocationNames.MONSTRO_TOWN_DOJO_FIRST_FIGHT,
    LocationNames.MONSTRO_TOWN_DOJO_SECOND_FIGHT,
    LocationNames.MONSTRO_TOWN_DOJO_THIRD_FIGHT,
    LocationNames.MONSTRO_TOWN_DOJO_FOURTH_FIGHT,
    LocationNames.MONSTRO_TOWN_SEALED_DOOR_BOSS_FIGHT,
    LocationNames.MIMIC_CHEST_3_BOSS_FIGHT,
    LocationNames.BEAN_VALLEY_BOSS_FIGHT,
    LocationNames.NIMBUS_CASTLE_STATUE_KEEPER_BOSS_FIGHT,
    LocationNames.NIMBUS_CASTLE_GIANT_EGG_BOSS_FIGHT,
    LocationNames.NIMBUS_LAND_FINAL_BOSS_FIGHT,
    LocationNames.BARREL_VOLCANO_FIRST_BOSS_FIGHT,
    LocationNames.BARREL_VOLCANO_SECOND_BOSS_FIGHT,
    LocationNames.BOWSERS_KEEP_BATTLE_DOOR_BOSS_FIGHT,
    LocationNames.BOWSERS_KEEP_FIRST_BOSS_FIGHT,
    LocationNames.BOWSERS_KEEP_SECOND_BOSS_FIGHT,
    LocationNames.BOWSERS_KEEP_THIRD_BOSS_FIGHT,
    LocationNames.OUTER_FACTORY_FIRST_BOSS_FIGHT,
    LocationNames.OUTER_FACTORY_SECOND_BOSS_FIGHT,
    LocationNames.INNER_FACTORY_FIRST_BOSS_FIGHT,
    LocationNames.INNER_FACTORY_SECOND_BOSS_FIGHT,
    LocationNames.INNER_FACTORY_THIRD_BOSS_FIGHT,
    LocationNames.INNER_FACTORY_FOURTH_BOSS_FIGHT,
    LocationNames.FACTORY_FINAL_BOSS_FIGHT
]

remake_boss_locations: list[LocationNames] = [
    LocationNames.MOLEVILLE_MINES_POSTGAME_BOSS_FIGHT,
    LocationNames.BOOSTER_TOWER_POSTGAME_BOSS_FIGHT,
    LocationNames.MARRYMORE_POSTGAME_BOSS_FIGHT,
    LocationNames.SUNKEN_SHIP_POSTGAME_BOSS_FIGHT,
    LocationNames.BELOME_TEMPLE_POSTGAME_BOSS_FIGHT,
    LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_FIGHT,
    LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_BOSS_FIGHT
]

star_piece_locations: list[LocationNames] = [
    LocationNames.MUSHROOM_WAY_BOSS_STAR_PIECE,
    LocationNames.BANDITS_WAY_BOSS_STAR_PIECE,
    LocationNames.MUSHROOM_KINGDOM_INVASION_BOSS_STAR_PIECE,
    LocationNames.MIMIC_CHEST_1_STAR_PIECE,
    LocationNames.KERO_SEWERS_BOSS_STAR_PIECE,
    LocationNames.FOREST_MAZE_BOSS_STAR_PIECE,
    LocationNames.MOLEVILLE_MINES_FIRST_BOSS_STAR_PIECE,
    LocationNames.MOLEVILLE_MINES_SECOND_BOSS_STAR_PIECE,
    LocationNames.BOOSTER_TOWER_CURTAIN_ROOM_BOSS_STAR_PIECE,
    LocationNames.BOOSTER_TOWER_BALCONY_BOSS_STAR_PIECE,
    LocationNames.MARRYMORE_BOSS_STAR_PIECE,
    LocationNames.STAR_HILL_FREESTANDING_STAR_PIECE,
    LocationNames.SUNKEN_SHIP_PASSWORD_BOSS_STAR_PIECE,
    LocationNames.MIMIC_CHEST_2_STAR_PIECE,
    LocationNames.SUNKEN_SHIP_FINAL_BOSS_STAR_PIECE,
    LocationNames.SEASIDE_TOWN_BOSS_STAR_PIECE,
    LocationNames.LANDS_END_BELOME_TEMPLE_CLOUD_STAR_PIECE,
    LocationNames.BELOME_TEMPLE_BOSS_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_DOJO_FIRST_FIGHT_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_DOJO_SECOND_FIGHT_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_DOJO_THIRD_FIGHT_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_DOJO_FOURTH_FIGHT_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_SEALED_DOOR_STAR_PIECE,
    LocationNames.MIMIC_CHEST_3_STAR_PIECE,
    LocationNames.BEAN_VALLEY_BOSS_STAR_PIECE,
    LocationNames.NIMBUS_CASTLE_STATUE_KEEPER_BOSS_STAR_PIECE,
    LocationNames.NIMBUS_CASTLE_GIANT_EGG_BOSS_STAR_PIECE,
    LocationNames.NIMBUS_LAND_FINAL_BOSS_STAR_PIECE,
    LocationNames.BARREL_VOLCANO_FIRST_BOSS_STAR_PIECE,
    LocationNames.BARREL_VOLCANO_SECOND_BOSS_STAR_PIECE,
    LocationNames.BOWSERS_KEEP_BATTLE_DOOR_STAR_PIECE,
    LocationNames.BOWSERS_KEEP_FIRST_BOSS_STAR_PIECE,
    LocationNames.BOWSERS_KEEP_SECOND_BOSS_STAR_PIECE,
    LocationNames.BOWSERS_KEEP_THIRD_BOSS_STAR_PIECE,
    LocationNames.OUTER_FACTORY_FIRST_BOSS_STAR_PIECE,
    LocationNames.OUTER_FACTORY_SECOND_BOSS_STAR_PIECE,
    LocationNames.INNER_FACTORY_FIRST_BOSS_STAR_PIECE,
    LocationNames.INNER_FACTORY_SECOND_BOSS_STAR_PIECE,
    LocationNames.INNER_FACTORY_THIRD_BOSS_STAR_PIECE,
    LocationNames.INNER_FACTORY_FOURTH_BOSS_STAR_PIECE,
    LocationNames.FACTORY_FINAL_BOSS_STAR_PIECE
]

remake_star_piece_locations: list[LocationNames] = [
    LocationNames.MOLEVILLE_MINES_POSTGAME_BOSS_STAR_PIECE,
    LocationNames.BOOSTER_TOWER_POSTGAME_BOSS_STAR_PIECE,
    LocationNames.MARRYMORE_POSTGAME_BOSS_STAR_PIECE,
    LocationNames.SUNKEN_SHIP_POSTGAME_BOSS_STAR_PIECE,
    LocationNames.BELOME_TEMPLE_POSTGAME_BOSS_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_DOJO_POSTGAME_STAR_PIECE,
    LocationNames.MONSTRO_TOWN_POSTGAME_SEALED_DOOR_STAR_PIECE
]