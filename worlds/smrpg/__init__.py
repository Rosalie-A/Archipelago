import logging
import os
import threading
from copy import deepcopy
from typing import NamedTuple, Union, Dict, Any

import bsdiff4

import Utils
from BaseClasses import Item, Location, Region, Entrance, MultiWorld, ItemClassification, Tutorial
from .Items import item_table
from .Locations import location_table, SMRPGRegions
from .Client import SMRPGClient
from .Options import smrpg_options, build_flag_string
from worlds.AutoWorld import World, WebWorld
from worlds.generic.Rules import add_rule, add_item_rule

from .smrpg_web_randomizer.randomizer.management.commands import make_seed


class SMRPGWeb(WebWorld):
    theme = "ice"
    setup = Tutorial(
        "Multiworld Setup Tutorial",
        "A guide to setting up Super Mario RPG for Archipelago on your computer.",
        "English",
        "multiworld_en.md",
        "multiworld/en",
        ["Rosalie"]
    )

    tutorials = [setup]


class SMRPGWorld(World):
    """
    Croakacola
    """
    option_definitions = smrpg_options
    game = "Super Mario RPG Legend of the Seven Stars"
    topology_present = False
    data_version = 1
    base_id = 85000
    web = SMRPGWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: location.id for name, location in location_table.items()}

    for k, v in item_name_to_id.items():
        item_name_to_id[k] = v + base_id

    for k, v in location_name_to_id.items():
        if v is not None:
            location_name_to_id[k] = v + base_id

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.rom_name = None
        self.generator_in_use = threading.Event()
        self.rom_name_text = ""
        self.rom_name_available_event = threading.Event()
        self.levels = None

    def create_item(self, name: str):
        return SMRPGItem(name, item_table[name].classification, self.item_name_to_id[name], self.player)

    def create_event(self, event: str):
        return SMRPGItem(event, ItemClassification.progression, None, self.player)

    def create_location(self, name, id, parent, event=False):
        return_location = SMRPGLocation(self.player, name, id, parent)
        return_location.event = event
        return return_location

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        overworld = Region("Overworld", self.player, self.multiworld)
        for key, location in location_table.items():
            try:
                region = self.multiworld.get_region(location.region.name, self.player)
            except KeyError:
                region = Region(location.region.name, self.player, self.multiworld)
                new_entrance = Entrance(self.player, location.region.name, overworld)
                new_entrance.connect(region)
                overworld.exits.append(new_entrance)
                self.multiworld.regions.append(region)
            location = self.create_location(location.name, self.location_name_to_id[location.name], region)
            region.locations.append(location)
        begin_game = Entrance(self.player, "Begin Game", menu)
        menu.exits.append(begin_game)
        begin_game.connect(overworld)
        self.multiworld.regions.append(menu)
        self.multiworld.regions.append(overworld)

    def set_rules(self):
        for key, location in location_table.items():
            if location.region is SMRPGRegions.moleville_mines_back:
                add_rule(self.multiworld.get_location(key, self.player),
                         lambda state: state.has("Bambino Bomb", self.player))

            if location.region is SMRPGRegions.nimbus_castle_middle:
                add_rule(self.multiworld.get_location(key, self.player),
                         lambda state: state.has("Castle Key 1", self.player))

            if location.region is SMRPGRegions.nimbus_castle_back:
                add_rule(self.multiworld.get_location(key, self.player),
                         lambda state: state.has("Castle Key 1", self.player)
                                       and state.has("Castle Key 2", self.player))

            if key in Locations.additional_bambino_locks:
                add_rule(self.multiworld.get_location(key, self.player),
                         lambda state: state.has("Bambino Bomb", self.player))

            if location.region is SMRPGRegions.factory:
                add_rule(self.multiworld.get_location(key, self.player),
                         lambda state: state.has("Star Piece", self.player, 7))

            if key in Locations.no_key_locations:
                add_item_rule(self.multiworld.get_location(key, self.player),
                              lambda item: item.name not in Items.key_items)

            if key in Locations.no_coin_locations:
                add_item_rule(self.multiworld.get_location(key, self.player),
                              lambda item: item.name not in Items.coin_rewards)

            if key in Locations.no_reward_locations:
                add_item_rule(self.multiworld.get_location(key, self.player),
                              lambda item: item.name not in Items.chest_rewards)

            if key in Locations.culex_locations \
                    and self.multiworld.IncludeCulex[self.player] == Options.IncludeCulex.option_false:
                add_item_rule(self.multiworld.get_location(key, self.player),
                              lambda item: item.classification != ItemClassification.progression)

            if key in Locations.super_jump_locations \
                    and self.multiworld.SuperJumpsNotRequired[self.player] == Options.SuperJumpsNotRequired.option_true:
                add_item_rule(self.multiworld.get_location(key, self.player),
                              lambda item: item.classification != ItemClassification.progression)

            for index, location in enumerate(Locations.bowsers_keep_doors):
                if index < self.multiworld.BowsersKeepDoors[self.player]:
                    add_item_rule(self.multiworld.get_location(key, self.player),
                                  lambda item: item.classification != ItemClassification.progression)

            add_item_rule(self.multiworld.get_location(key, self.player),
                          lambda item: item.name not in Items.boss_items)

    def generate_basic(self):
        boss_locations = deepcopy(Locations.star_piece_locations)
        star_pieces = self.multiworld.random.sample(boss_locations, 7)
        for location in boss_locations:
            if location in star_pieces:
                self.multiworld.get_location(location, self.player).place_locked_item(
                    self.create_item("Star Piece"))
            else:
                self.multiworld.get_location(location, self.player).place_locked_item(
                    self.create_item("Defeated!"))
        smithy = self.multiworld.get_location("Smithy", self.player)
        smithy.place_locked_item(self.create_item("Star Road Restored!"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Star Road Restored!", self.player)

    def create_items(self):
        for item in Items.singleton_items:
            self.multiworld.itempool.append(self.create_item(item))
        pool_size = len(self.multiworld.get_unfilled_locations(self.player)) \
                    - len(Items.key_items) \
                    - len(Locations.star_piece_locations)
        filler = int(pool_size // 1.5)
        weapons = pool_size // 8
        armors = pool_size // 8
        accessories = pool_size // 8
        misc_pool = pool_size - filler - weapons - armors - accessories
        for i in range(filler):
            self.multiworld.itempool.append(self.create_item(self.multiworld.random.choice(Items.filler)))
        for i in range(weapons):
            self.multiworld.itempool.append(self.create_item(self.multiworld.random.choice(Items.weapons)))
        for i in range(armors):
            self.multiworld.itempool.append(self.create_item(self.multiworld.random.choice(Items.armor)))
        for i in range(accessories):
            self.multiworld.itempool.append(self.create_item(self.multiworld.random.choice(Items.accessories)))
        for i in range(misc_pool):
            self.multiworld.itempool.append(self.create_item(self.multiworld.random.choice(Items.all_mundane_items)))

    def generate_output(self, output_directory: str):
        self.rom_name_text = f'SMRPG{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        self.rom_name_text = self.rom_name_text[:20]
        self.rom_name = bytearray(self.rom_name_text, 'utf-8')
        self.rom_name.extend([0] * (20 - len(self.rom_name)))
        output = dict()
        for key, location in location_table.items():
            item = self.multiworld.get_location(location.name, self.player).item
            rando_name = item_table[item.name].rando_name if item.player == self.player else "ArchipelagoItem"
            output[location.rando_name] = rando_name
        make_seed.Command().handle(
            mode="open",
            flags=build_flag_string(self.options.as_dict(*smrpg_options.keys())),
            seed=self.multiworld.seed % 2 ** 32,
            rom="smrpg.smc",
            output_file="worlds/smrpg/randomized.sfc",
            ap_data=output,
            rom_name=self.rom_name
        )

    def modify_multidata(self, multidata: dict):
        import base64
        rom_name = getattr(self, "rom_name", None)
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]

    def get_filler_item_name(self) -> str:
        filler_items = [item for item in item_table if item_table[item].classification == ItemClassification.filler]
        return self.multiworld.random.choice(filler_items)


class SMRPGItem(Item):
    game = 'Super Mario RPG'


class SMRPGLocation(Location):
    game = 'Super Mario RPG'
