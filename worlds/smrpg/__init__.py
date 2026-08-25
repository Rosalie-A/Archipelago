import json
from typing import Any

import settings
import typing

from BaseClasses import MultiWorld, ItemClassification, Tutorial, Item, Region, Entrance, CollectionState
from Fill import fill_restrictive
from Options import OptionError
from rule_builder.rules import False_, True_, Has, CanReachLocation

from worlds.AutoWorld import World, WebWorld, LogicMixin
from .Options import SMRPGOptions
from .data.ItemNames import ItemNames
from .data.LocationNames import LocationNames
from .data.itempools import get_vanilla_pool

from .data.items import all_item_data, progression_item_names, character_item_data, boss_item_data, \
    remake_boss_item_data, spell_item_data
from .data.logic.Requirement import get_rule_from_requirements, CanDamageWithSpells, CanBeatLocation
from .data.logic.RequirementItems import DamagingSpells, BossFights, boss_fight_names
from .data.locations import all_location_data, SMRPGLocation, character_locations, boss_locations, \
    remake_boss_locations, star_piece_locations, remake_star_piece_locations
from .data.logic.SMRPGLocation import BossFightLocation, StarPieceLocation, CharacterRecruitLocation, ChestLocation
from .data.logic.regions import all_regions, MariosPad
from ..generic.Rules import set_rule, add_item_rule


class SMRPGSettings(settings.Group):
    class RomFile(settings.UserFilePath):
        """File name of the SMRPG ROM"""
        description = "Super Mario RPG USA ROM File"
        copy_to = "Super Mario RPG - Legend of the Seven Stars (USA).sfc "
        md5s = ["d0b68d68d9efc0558242f5476d1c5b81"]

    rom_file: RomFile = RomFile(RomFile.copy_to)
    rom_start: bool = False

class SpellState(LogicMixin):
    can_defeat_with_spells: dict[int, bool]  # per player

    def init_mixin(self, multiworld: MultiWorld) -> None:
        self.can_defeat_with_spells = {
            player: False for player in multiworld.get_game_players("Super Mario RPG")
        }
        pass

    def copy_mixin(self, new_state: CollectionState) -> CollectionState:
        new_state.can_defeat_with_spells = {
            player: can_defeat for player, can_defeat in self.can_defeat_with_spells.items()
        }
        return new_state

class SMRPGWeb(WebWorld):
    theme = "grass"
    setup = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up Final Fantasy Tactics for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Rosalie"]
    )

    tutorials = [setup]

    rich_text_options_doc = True
    #option_groups = fftii_option_groups


class SMRPGWorld(World):
    """
    An open world mod for Final Fantasy Tactics for Archipelago.
    Find all the Zodiac Stones and make your way to Murond Death City to confront Altima!
    """
    settings: typing.ClassVar[SMRPGSettings]
    game = "Super Mario RPG"
    options_dataclass = SMRPGOptions
    options: SMRPGOptions

    web = SMRPGWeb()

    item_name_to_id = {item.name.value: item.game_id for item in all_item_data}
    location_name_to_id = {location.name: location.id for location in all_location_data}
    character_spells: dict[str, list[str]] = {}
    damaging_spells = [member.name.value for member in DamagingSpells.members]
    placed_characters: set = set()

    item_name_groups = {
        "Boss Fights": [
            *[boss.name.value for boss in boss_item_data],
            *[boss.name.value for boss in remake_boss_item_data]
        ]
    }

    filler_items = None

    version = "1.0.0"
    debug = False
    topology_present = debug

    def __init__(self, multiworld: MultiWorld, player: int):
        super().__init__(multiworld, player)
        self.character_spells = {
            "Mario": [],
            "Mallow": [],
            "Geno": [],
            "Bowser": [],
            "Toadstool": [],
        }
        self.filler_items = None

    def create_item(self, name: str) -> "SMRPGItem":
        if name in progression_item_names:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler
        return SMRPGItem(name, classification, self.item_name_to_id[name], self.player)

    def create_event(self, name: str) -> "SMRPGItem":
        return SMRPGItem(name, ItemClassification.progression, None, self.player)

    def create_regions(self):
        for region_data in all_regions:
            region = Region(region_data.name, self.player, self.multiworld)
            self.multiworld.regions.append(region)

        self.origin_region_name = MariosPad.name

        # Define connections
        for origin_region_data in all_regions:
            origin_region = self.get_region(origin_region_data.name)
            for connection in origin_region_data.connections:
                if self.debug:
                    print(f"Connection: {origin_region.name} to {connection.destination.name}")
                rule = get_rule_from_requirements(connection.requirements, self.options)
                connecting_region = self.get_region(connection.destination.name)
                connection_name = f"{origin_region.name} to {connecting_region.name}"
                self.create_entrance(origin_region, connecting_region, rule, connection_name, True)
            for location in origin_region_data.locations:
                if location.check_enabled(self.options):
                    new_location = SMRPGLocation(
                        self.player,
                        location.name,
                        self.location_name_to_id[location.name],
                        origin_region)
                    origin_region.locations.append(new_location)
                    rule2 = get_rule_from_requirements(location.requirements, self.options)
                    self.set_rule(new_location, rule2)
                    if issubclass(location.__class__, BossFightLocation):
                        add_item_rule(new_location, lambda item: item.name in boss_fight_names)
                    elif issubclass(location.__class__, StarPieceLocation):
                        add_item_rule(new_location, lambda item: item.name in [ItemNames.STAR_PIECE, ItemNames.NO_STAR])
                    elif issubclass(location.__class__, CharacterRecruitLocation):
                        add_item_rule(new_location, lambda item: item.name in [*[character.name for character in character_item_data], ItemNames.NO_CHARACTER])
                    elif issubclass(location.__class__, ChestLocation):
                        add_item_rule(new_location,
                                      lambda item: item.name not in [
                                          *boss_fight_names,
                                          ItemNames.STAR_PIECE,
                                          ItemNames.NO_CHARACTER,
                                          ItemNames.NO_STAR,
                                          *[character.name for character in character_item_data]
                                      ])
                    else:
                        add_item_rule(new_location,
                                      lambda item: item.name not in [
                                          *boss_fight_names,
                                          ItemNames.STAR_PIECE,
                                          ItemNames.NO_CHARACTER,
                                          ItemNames.NO_STAR,
                                          ItemNames.FIRST_MIMIC_LAUNCHER,
                                          ItemNames.SECOND_MIMIC_LAUNCHER,
                                          ItemNames.THIRD_MIMIC_LAUNCHER,
                                          ItemNames.EXP_STAR,
                                          *[character.name for character in character_item_data]
                                      ])

                    new_location.rule_builder_rule = rule2

        if self.debug:
            from Utils import visualize_regions
            visualize_regions(self.get_region(self.origin_region_name), f"smrpgdiagram{self.player}.puml", show_entrance_rules=True)

    def place_characters(self):
        character_list = [character.name for character in character_item_data]
        lead_character = character_list[self.options.lead_character]
        starting_characters = set()
        starting_characters.add(lead_character)
        if self.options.mario_placement == self.options.mario_placement.option_starting:
            starting_characters.add(ItemNames.MARIO)
        if self.options.mallow_placement == self.options.mallow_placement.option_starting:
            starting_characters.add(ItemNames.MALLOW)
        if self.options.geno_placement == self.options.geno_placement.option_starting:
            starting_characters.add(ItemNames.GENO)
        if self.options.bowser_placement == self.options.bowser_placement.option_starting:
            starting_characters.add(ItemNames.BOWSER)
        if self.options.toadstool_placement == self.options.toadstool_placement.option_starting:
            starting_characters.add(ItemNames.TOADSTOOL)
        self.get_location(LocationNames.STARTER_CHARACTER_1).place_locked_item(self.create_item(lead_character))
        starting_characters.remove(lead_character)
        self.placed_characters.add(lead_character)
        starting_characters = sorted(list(starting_characters))
        while len(starting_characters) < 4:
            starting_characters.append(ItemNames.NO_CHARACTER)
        remaining_slots = [
            self.get_location(LocationNames.STARTER_CHARACTER_2),
            self.get_location(LocationNames.STARTER_CHARACTER_3),
            self.get_location(LocationNames.STARTER_CHARACTER_4),
            self.get_location(LocationNames.STARTER_CHARACTER_5),
        ]
        for character, location in zip(starting_characters, remaining_slots):
            location.place_locked_item(self.create_item(character))
        available_characters = set()
        if self.options.mario_placement == self.options.mario_placement.option_available:
            available_characters.add(ItemNames.MARIO)
        if self.options.mallow_placement == self.options.mallow_placement.option_available:
            available_characters.add(ItemNames.MALLOW)
        if self.options.geno_placement == self.options.geno_placement.option_available:
            available_characters.add(ItemNames.GENO)
        if self.options.bowser_placement == self.options.bowser_placement.option_available:
            available_characters.add(ItemNames.BOWSER)
        if self.options.toadstool_placement == self.options.toadstool_placement.option_available:
            available_characters.add(ItemNames.TOADSTOOL)
        available_characters.remove(lead_character)
        available_characters = sorted(list(available_characters))
        remaining_slots = [
            self.get_location(LocationNames.MUSHROOM_WAY_CHARACTER_RECRUIT),
            self.get_location(LocationNames.FOREST_MAZE_CHARACTER_RECRUIT),
            self.get_location(LocationNames.MOLEVILLE_MINES_CHARACTER_RECRUIT),
            self.get_location(LocationNames.MARRYMORE_CHARACTER_RECRUIT),
        ]
        while len(available_characters) < 4:
            available_characters.append(ItemNames.NO_CHARACTER)
        available_characters = [self.create_item(character) for character in available_characters]
        self.random.shuffle(available_characters)
        star_pieces = [self.create_item(ItemNames.STAR_PIECE) for i in range(self.options.total_star_pieces.value)]
        star_locations = star_piece_locations.copy()
        if self.options.enable_remake_content:
            star_locations.extend(remake_star_piece_locations)
        star_locations = [self.get_location(location) for location in star_locations]
        while len(star_pieces) < len(star_locations):
            star_pieces.append(self.create_item(ItemNames.NO_STAR))
        self.random.shuffle(star_pieces)
        self.random.shuffle(star_locations)
        boss_list = [self.create_item(boss.name) for boss in boss_item_data]
        boss_location_list = [self.get_location(boss) for boss in boss_locations]
        if self.options.enable_remake_content:
            boss_list.extend([self.create_item(boss.name) for boss in remake_boss_item_data])
            boss_location_list.extend([self.get_location(boss) for boss in remake_boss_locations])
        self.random.shuffle(boss_list)
        self.random.shuffle(boss_location_list)
        all_pre_locations = [*remaining_slots, *star_locations, *boss_location_list]
        all_pre_items = [*available_characters, *star_pieces, *boss_list]
        fill_restrictive(
            self.multiworld,
            self.multiworld.get_all_state(),
            all_pre_locations,
            all_pre_items,
            True,
            True,
            False,
            lambda loc: print(f"placing {loc.item.name} at {loc.name}.") if self.debug else None,
            allow_partial=False,
            name=f"SMRPG Player {self.player} Pre Fill Step")



    def place_spells(self):
        all_spells = [spell.name for spell in spell_item_data]
        while len(all_spells) < 36:
            all_spells.append(ItemNames.NOTHING)
        self.random.shuffle(all_spells)
        for character, spell_list in self.character_spells.items():
            for i in range(6):
                spell_list.append(all_spells.pop())
            spell_list.sort(key=lambda x: x == ItemNames.NOTHING)
        character_list = ["Mario", "Mallow", "Geno", "Bowser", "Toadstool"]
        for i, origin_character in enumerate(character_list):
            if self.options.lead_character == i:
                if not [spell for spell in self.character_spells[origin_character] if spell in self.damaging_spells]:
                    spell_1 = self.character_spells[origin_character][0]
                    done = False
                    for destination_character, spell_list in self.character_spells.items():
                        if done or destination_character == origin_character:
                            continue
                        new_spell_list = spell_list.copy()
                        for spell in spell_list:
                            if spell in self.damaging_spells:
                                spell_2 = spell
                                new_spell_list.remove(spell)
                                new_spell_list.append(spell_1)
                                self.character_spells[origin_character][0] = spell_2
                                done = True
                        self.character_spells[destination_character] = new_spell_list
        if self.options.mario_placement == self.options.mario_placement.option_absent:
            if self.options.lead_character != self.options.lead_character.option_mario:
                self.character_spells["Mario"] = []
        if self.options.mallow_placement == self.options.mallow_placement.option_absent:
            if self.options.lead_character != self.options.lead_character.option_mallow:
                self.character_spells["Mallow"] = []
        if self.options.geno_placement == self.options.geno_placement.option_absent:
            if self.options.lead_character != self.options.lead_character.option_geno:
                self.character_spells["Geno"] = []
        if self.options.bowser_placement == self.options.bowser_placement.option_absent:
            if self.options.lead_character != self.options.lead_character.option_bowser:
                self.character_spells["Bowser"] = []
        if self.options.toadstool_placement == self.options.toadstool_placement.option_absent:
            if self.options.lead_character != self.options.lead_character.option_toadstool:
                self.character_spells["Toadstool"] = []

    def pre_fill(self) -> None:
        self.place_characters()
        self.place_spells()

    def get_pre_fill_items2(self) -> list["Item"]:
        prefill_list = [self.create_item(boss.name) for boss in boss_item_data]
        if self.options.enable_remake_content:
            prefill_list.extend([self.create_item(boss.name) for boss in remake_boss_item_data])
        prefill_list.extend([self.create_item(character.name) for character in character_item_data])
        prefill_list.extend([self.create_item(spell.name) for spell in spell_item_data])
        for i in range(self.options.total_star_pieces.value):
            prefill_list.append(self.create_item("Star Piece"))
        return prefill_list

    def create_items(self):
        itempool = []
        vanilla_pool = get_vanilla_pool(self.options)
        for item in all_item_data:
            if item.name in vanilla_pool.keys():
                for i in range(vanilla_pool[item.name]):
                    itempool.append(item.name)
        for item in map(self.create_item, itempool):
            self.multiworld.itempool.append(item)

    def collect(self, state: CollectionState, item: Item) -> bool:
        change = super().collect(state, item)
        if change and not self.options.spells_anywhere:
            for character in self.character_spells.keys():
                if state.has(character, self.player):
                    state.can_defeat_with_spells[self.player] = True
                    break
        if change and not state.can_defeat_with_spells[self.player] and item.name in self.damaging_spells:
            for character in self.character_spells.keys():
                if state.has(character, self.player) and item.name in self.character_spells[character]:
                    state.can_defeat_with_spells[self.player] = True
                    break
        return change

    def remove(self, state: CollectionState, item: Item) -> bool:
        change = super().remove(state, item)
        if change and state.can_defeat_with_spells[self.player] and item.name in self.damaging_spells:
            state.can_defeat_with_spells[self.player] = False
            for character in self.character_spells.keys():
                if state.has(character, self.player):
                    for spell_name in self.character_spells[character]:
                        if spell_name in self.damaging_spells and state.has(spell_name):
                            state.can_defeat_with_spells[self.player] = True
                            break
                    if state.can_defeat_with_spells[self.player]:
                        break
        return change

    def set_rules(self):
        if self.options.win_condition == self.options.win_condition.option_factory:
            victory_condition_rule = CanBeatLocation(ItemNames.FACTORY)
        elif self.options.win_condition == self.options.win_condition.option_smithy:
            victory_condition_rule = Has(ItemNames.SMITHY)
        elif self.options.win_condition == self.options.win_condition.option_sealed_door:
            victory_condition_rule = CanBeatLocation(ItemNames.SEALED_DOOR)
        else: # self.options.win_condition == self.options.win_condition.option_stars:
            victory_condition_rule = Has(ItemNames.STAR_PIECE, self.options.star_pieces_required.value)
        self.set_completion_rule(victory_condition_rule)

    def generate_basic(self):
        pass

    def create_location_dict(self):
        locations = self.get_locations()
        location_dict = dict()
        for location in locations:
            ap_location = self.get_location(location.name)
            item = ap_location.item
            player = item.player
            location_dict[ap_location] = item.name
        return location_dict

    def generate_output(self, output_directory: str) -> None:
        patch_dict: dict[str, Any] = dict()
        # Hash of the MW seed to associate with save file
        patch_dict["Seed"] = self.multiworld.seed + self.player
        patch_dict["LocationDict"] = self.create_location_dict()

    def get_filler_item_name(self) -> str:
        if self.filler_items is None:
            self.filler_items = ["Mushroom"]
        return self.random.choice(self.filler_items)


class SMRPGItem(Item):
    game = "Super Mario RPG"
