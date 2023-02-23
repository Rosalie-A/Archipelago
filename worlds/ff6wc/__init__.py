import importlib
import json
import os
import random
import shutil
import string
import subprocess
import threading
from typing import NamedTuple, Union
import logging

from BaseClasses import Item, Location, Region, Entrance, MultiWorld, ItemClassification
from . import Logic
from .Rom import FF6WCDeltaPatch
from .Client import FF6WCClient
from ..generic.Rules import add_rule, set_rule, forbid_item, add_item_rule
from ..AutoWorld import World, LogicMixin, WebWorld
from NetUtils import SlotType
from .Locations import location_table
from .Items import item_table
from .Options import ff6wc_options, generate_flagstring
import Utils

from worlds.ff6wc.WorldsCollide.wc import WC


class FF6WCWeb(WebWorld):
    theme = "dirt"

class FF6WCWorld(World):
    option_definitions = ff6wc_options
    game = "Final Fantasy 6 Worlds Collide"
    topology_present = False
    data_version = 1
    base_id = 6000
    web = FF6WCWeb()
    wc_ready = threading.Lock()

    item_name_to_id = {name: index for index, name in enumerate(item_table)}
    location_name_to_id = {name: index for index, name in enumerate(location_table)}

    all_characters = [
            'Terra', 'Locke', 'Cyan', 'Shadow', 'Edgar',
            'Sabin', 'Celes', 'Strago', 'Relm', 'Setzer',
            'Mog', 'Gau', 'Gogo', 'Umaro'
        ]

    all_espers = [
            "Ramuh", "Ifrit", "Shiva", "Siren", "Terrato", "Shoat", "Maduin",
            "Bismark", "Stray", "Palidor", "Tritoch", "Odin", "Raiden", "Bahamut",
            "Alexandr", "Crusader", "Ragnarok Esper", "Kirin", "ZoneSeek", "Carbunkl",
            "Phantom", "Sraphim", "Golem", "Unicorn", "Fenrir", "Starlet", "Phoenix",
        ]

    all_dragon_clears = [
            "Removed!", "Stomped!",
            "Blasted!", "Ditched!",
            "Wiped!", "Incinerated!",
            "Skunked!", "Gone!"
        ]

    item_name_groups = {
        'characters': all_characters,
        'espers': all_espers,
        "dragons": all_dragon_clears
    }

    for k, v in item_name_to_id.items():
        item_name_to_id[k] = v + base_id

    for k, v in location_name_to_id.items():
        if v is not None:
            location_name_to_id[k] = v + base_id

    def __init__(self, world: MultiWorld, player: int):
        super().__init__(world, player)
        self.starting_characters = None
        self.generator_in_use = threading.Event()
        self.wc = None
        self.rom_name_available_event = threading.Event()

    def create_item(self, name: str):
        return FF6WCItem(name, ItemClassification.progression, self.item_name_to_id[name], self.player)

    def create_good_filler_item(self, name: str):
        return FF6WCItem(name, ItemClassification.useful, self.item_name_to_id[name], self.player)

    def create_filler_item(self, name: str):
        return FF6WCItem(name, ItemClassification.filler, self.item_name_to_id[name], self.player)

    def create_event(self, event: str):
        return FF6WCItem(event, ItemClassification.progression, None, self.player)

    def create_location(self, name, id, parent, event=False):
        return_location = FF6WCLocation(self.player, name, id, parent)
        return_location.event = event
        return return_location

    def generate_early(self):
        if self.multiworld.EnableFlagstring[self.player].value == "true":

            self.starting_characters = []
            character_list = []
            flags = self.multiworld.Flagstring[self.player].value
            # Determining Starting Characters
            flags_list = flags.split(" ")
            sc1_index = flags_list.index("-sc1") + 1
            character_list.append(flags_list[sc1_index])
            if "-sc2" in flags_list:
                sc2_index = flags_list.index("-sc2") + 1
                character_list.append(flags_list[sc2_index])
            if "-sc3" in flags_list:
                sc3_index = flags_list.index("-sc3") + 1
                character_list.append(flags_list[sc3_index])
            if "-sc4" in flags_list:
                sc4_index = flags_list.index("-sc4") + 1
                character_list.append(flags_list[sc4_index])

            for character in range(len(character_list)):
                if character_list[character] == "randomgu":
                    compare_character_list = character_list.copy()
                    character_list[character] = random.choice(Rom.characters[:12]).lower()
                    while character_list[character] in compare_character_list:
                        character_list[character] = random.choice(Rom.characters[:12]).lower()
                elif character_list[character] == "random":
                    compare_character_list = character_list.copy()
                    character_list[character] = random.choice(Rom.characters[:14]).lower()
                    while character_list[character] in compare_character_list:
                        character_list[character] = random.choice(Rom.characters[:14]).lower()
                elif character_list[character] not in character_list:
                    character_list[character] = character_list[character]

            for x in range(len(character_list)):
                if x == 0:
                    flags_list[sc1_index] = character_list[x]
                if x == 1:
                    flags_list[sc2_index] = character_list[x]
                if x == 2:
                    flags_list[sc3_index] = character_list[x]
                if x == 3:
                    flags_list[sc4_index] = character_list[x]


            self.multiworld.StartingCharacterCount[self.player].value = len(character_list)

            starting_character_options = list(self.multiworld.StartingCharacter1[self.player].name_lookup.values())
            self.multiworld.StartingCharacter1[self.player].value = starting_character_options.index(character_list[0])
            self.multiworld.StartingCharacter2[self.player].value = 14
            self.multiworld.StartingCharacter3[self.player].value = 14
            self.multiworld.StartingCharacter4[self.player].value = 14
            if len(character_list) > 1:
                self.multiworld.StartingCharacter2[self.player].value = starting_character_options.index(character_list[1])
            if len(character_list) > 2:
                self.multiworld.StartingCharacter3[self.player].value = starting_character_options.index(character_list[2])
            if len(character_list) > 3:
                self.multiworld.StartingCharacter4[self.player].value = starting_character_options.index(character_list[3])

            proper_names = " ".join(character_list)
            proper_names = proper_names.title()
            character_list = proper_names.split(" ")
            self.starting_characters = character_list

            # Determining character, esper, and dragon requirements
            # Finding KT Objective in flagstring (starts with 2)
            character_count = 0
            esper_count = 0
            dragon_count = 0
            boss_count = 0

            alphabet = string.ascii_lowercase
            for letter in range(len(alphabet)):
                objective_list = ["-o", alphabet[letter]]
                objective = "".join(objective_list)
                if objective in flags_list:
                    objective_code = flags_list[flags_list.index(objective) + 1]
                    objective_code_list = objective_code.split(".")
                    if objective_code_list[0] == "2":
                        kt_obj_code = objective_code
                        kt_obj_list = objective_code_list
                        kt_obj_code_index = flags_list.index(objective) + 1
                        break
            # Determining Esper and Dragon Counts
            for index in range(len(kt_obj_list)):
                if index%3 == 0 and index > 0:
                    count_low = int(kt_obj_list[index + 1])
                    count_high = int(kt_obj_list[index + 2])
                    if kt_obj_list[index] == "2":
                        character_count = random.randint(count_low, count_high)
                        kt_obj_list[index + 1] = str(character_count)
                        kt_obj_list[index + 2] = str(character_count)
                    elif kt_obj_list[index] == "4":
                        esper_count = random.randint(count_low, count_high)
                        kt_obj_list[index + 1] = str(esper_count)
                        kt_obj_list[index + 2] = str(esper_count)
                    elif kt_obj_list[index] == "6":
                        dragon_count = random.randint(count_low, count_high)
                        kt_obj_list[index + 1] = str(dragon_count)
                        kt_obj_list[index + 2] = str(dragon_count)
                    elif kt_obj_list[index] == "8":
                        boss_count = random.randint(count_low, count_high)
                        kt_obj_list[index + 1] = str(boss_count)
                        kt_obj_list[index + 2] = str(boss_count)
            kt_obj_list_string = ".".join(kt_obj_list)
            flags_list[kt_obj_code_index] = kt_obj_list_string

            self.multiworld.Flagstring[self.player].value = " ".join(flags_list)
            self.multiworld.CharacterCount[self.player].value = character_count
            self.multiworld.EsperCount[self.player].value = esper_count
            self.multiworld.DragonCount[self.player].value = dragon_count
            # self.multiworld.BossCount[self.player].value = boss_count

        else:
            starting_characters = [
                (self.multiworld.StartingCharacter1[self.player].current_key).capitalize(),
                (self.multiworld.StartingCharacter2[self.player].current_key).capitalize(),
                (self.multiworld.StartingCharacter3[self.player].current_key).capitalize(),
                (self.multiworld.StartingCharacter4[self.player].current_key).capitalize()
            ]
            starting_characters = starting_characters[0:self.multiworld.StartingCharacterCount[self.player]]
            starting_characters.sort(key=lambda character: character == "Random_with_no_gogo_or_umaro")

            filtered_starting_characters = []
            for character in starting_characters:
                if character == "Random_with_no_gogo_or_umaro":
                    character = random.choice(Rom.characters[:12])
                    while character in filtered_starting_characters:
                        character = random.choice(Rom.characters[:12])
                if character not in filtered_starting_characters:
                    filtered_starting_characters.append(character)

            self.starting_characters = filtered_starting_characters

    def create_regions(self):
        menu = Region("Menu", self.player, self.multiworld)
        world_map = Region("World Map", self.player, self.multiworld)
        final_dungeon = Region("Kefka's Tower", self.player, self.multiworld)

        for name, id in self.location_name_to_id.items():
            if self.multiworld.Treasuresanity[self.player] == 0:
                if name in Locations.all_minor_checks:
                    continue
            if name in Locations.dragon_events:
                id = None
            if name in Locations.kefka_checks:
                final_dungeon.locations.append(self.create_location(name, id, final_dungeon))
            elif name in Locations.accomplishment_data:
                final_dungeon.locations.append(self.create_location(name, None, final_dungeon, True))
            else:
                world_map.locations.append(self.create_location(name, id, world_map))

        airship = Entrance(self.player, "Airship", menu)
        final_dungeon_entrance = Entrance(self.player, "Kefka's Tower Landing", world_map)
        # airship.connect(menu)
        airship.connect(world_map)
        menu.exits.append(airship)
        world_map.exits.append(airship)
        self.multiworld.regions.append(menu)
        final_dungeon_entrance.connect(world_map)
        final_dungeon_entrance.connect(final_dungeon)
        world_map.exits.append(final_dungeon_entrance)
        final_dungeon.exits.append(final_dungeon_entrance)
        self.multiworld.regions.append(world_map)
        self.multiworld.regions.append(final_dungeon)

    def create_items(self):
        for item in map(self.create_item, self.item_name_to_id):
            if item.name in self.starting_characters:
                self.multiworld.push_precollected(item)
            elif item.name in Rom.characters or item.name in Rom.espers:
                self.multiworld.itempool.append(item)

    def set_rules(self):
        check_list = {
            "Terra": (Locations.major_terra_checks, Locations.minor_terra_checks, Locations.minor_terra_ext_checks),
            "Locke": (Locations.major_locke_checks, Locations.minor_locke_checks, Locations.minor_locke_ext_checks),
            "Cyan": (Locations.major_cyan_checks, Locations.minor_cyan_checks, Locations.minor_cyan_ext_checks),
            "Shadow": (Locations.major_shadow_checks, Locations.minor_shadow_checks, Locations.minor_shadow_ext_checks),
            "Edgar": (Locations.major_edgar_checks, Locations.minor_edgar_checks, Locations.minor_edgar_ext_checks),
            "Sabin": (Locations.major_sabin_checks, Locations.minor_sabin_checks, Locations.minor_sabin_ext_checks),
            "Celes": (Locations.major_celes_checks, Locations.minor_celes_checks, Locations.minor_celes_ext_checks),
            "Strago": (Locations.major_strago_checks, Locations.minor_strago_checks, Locations.minor_strago_ext_checks),
            "Relm": (Locations.major_relm_checks, Locations.minor_relm_checks, Locations.minor_relm_ext_checks),
            "Setzer": (Locations.major_setzer_checks, Locations.minor_setzer_checks, Locations.minor_setzer_ext_checks),
            "Mog": (Locations.major_mog_checks, Locations.minor_mog_checks, Locations.minor_mog_ext_checks),
            "Gau": (Locations.major_gau_checks, Locations.minor_gau_checks, Locations.minor_gau_ext_checks),
            "Gogo": (Locations.major_gogo_checks, Locations.minor_gogo_checks, Locations.minor_gogo_ext_checks),
            "Umaro": (Locations.major_umaro_checks, Locations.minor_umaro_checks, Locations.minor_umaro_ext_checks),
        }
        # Set every character locked check to require that character.
        for check_name, checks in check_list.items():
            # Major checks. These are always on.
            for check in checks[0]:
                set_rule(self.multiworld.get_location(check, self.player),
                         lambda state, character=check_name: state.has(character, self.player))
            # Minor checks. These are only on if Treasuresanity is on.
            if self.multiworld.Treasuresanity[self.player] != 0:
                for check in checks[1]:
                    set_rule(self.multiworld.get_location(check, self.player),
                             lambda state, character=check_name: state.has(character, self.player))
            # Minor extended gating checks. These are on if Treasuresanity are on, but can be character gated.
            if self.multiworld.Treasuresanity[self.player] == 2:
                for check in checks[2]:
                    set_rule(self.multiworld.get_location(check, self.player),
                             lambda state, character=check_name: state.has(character, self.player))

        # Lock (ha!) these behind Terra as well as Locke, since whatever isn't chosen is put behind Whelk
        for check_name in ["Narshe Weapon Shop 1", "Narshe Weapon Shop 2",]:
            add_rule(self.multiworld.get_location(check_name, self.player),
                     lambda state: state.has("Terra", self.player))

        for check in Locations.major_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name not in Items.okay_items)

        for check in Locations.item_only_checks:
            if self.multiworld.Treasuresanity[self.player] != 0 or (check not in Locations.minor_checks and check not in Locations.minor_ext_checks):
                add_item_rule(self.multiworld.get_location(check, self.player),
                              lambda item: item.name not in self.item_name_groups["characters"]
                                       and item.name not in self.item_name_groups['espers']
                                       or item.player != self.player)

        for check in Locations.no_character_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name not in self.item_name_groups["characters"]
                                       or item.player != self.player)

        for check in Locations.no_item_checks:
            add_item_rule(self.multiworld.get_location(check, self.player),
                          lambda item: item.name in self.item_name_groups["characters"]
                                       or item.name in self.item_name_groups['espers']
                                       or item.player != self.player)

        for dragon in Locations.dragons:
            dragon_event = Locations.dragon_events_link[dragon]
            add_item_rule(self.multiworld.get_location(dragon_event, self.player),
                          lambda state: state.can_reach(str(dragon), 'Location', self.player))

        for location in Locations.fanatics_tower_checks:
            if self.multiworld.Treasuresanity[self.player] != 0 or location not in Locations.all_minor_checks:
                add_rule(self.multiworld.get_location(location, self.player),
                         lambda state: state.has_group("espers", self.player, 4))

        set_rule(self.multiworld.get_entrance("Kefka's Tower Landing", self.player),
                 lambda state: state._ff6wc_has_enough_characters(self.multiworld, self.player)
                               and state._ff6wc_has_enough_espers(self.multiworld, self.player))
        set_rule(self.multiworld.get_location("Beat Final Kefka", self.player),
                 lambda state: state.can_reach("Kefka's Tower", 'Location', self.player)
                               and state._ff6wc_has_enough_dragons(self.multiworld, self.player))
    def pre_fill(self):
        pass

    def generate_basic(self):
        self.multiworld.get_location("Kefka's Tower", self.player).place_locked_item(
            self.create_event("Kefka's Tower Access"))
        self.multiworld.get_location("Beat Final Kefka", self.player).place_locked_item(self.create_event("Victory"))
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

        for index, dragon in enumerate(Locations.dragons):
            dragon_event = Locations.dragon_events_link[dragon]
            self.multiworld.get_location(dragon_event, self.player).place_locked_item(
                self.create_event(self.all_dragon_clears[index]))

        for location in Locations.no_item_checks:
            possibilities = [item for item in self.multiworld.itempool if item.player == self.player]
            possibilities = [item for item in possibilities if
                             item.name in Items.characters or item.name in Items.espers]
            location = self.multiworld.get_location(location, self.player)
            item = self.multiworld.random.choice(possibilities)
            location.place_locked_item(item)
            self.multiworld.itempool.remove(item)
        unfilled_locations = self.multiworld.get_unfilled_locations(self.player)
        item_pool_size = len([item for item in self.multiworld.itempool if item.player == self.player])
        filler_count = len(unfilled_locations) - item_pool_size
        filler_pool = []
        good_filler_pool = []
        for item in Items.items:
            if item != "ArchplgoItem":
                filler_pool.append(item)
            if item in Items.good_items:
                good_filler_pool.append(item)
        unfilled_major_locations = [
            location for location in unfilled_locations
            if location.player == self.player and location.name in Locations.major_checks
        ]
        self.multiworld.itempool += [
            self.create_good_filler_item(self.multiworld.random.choice(good_filler_pool))
            for _ in range(0, len(unfilled_major_locations))
        ]
        filler_count -= len(unfilled_major_locations)
        self.multiworld.itempool += [
            self.create_filler_item(self.multiworld.random.choice(filler_pool))
            for _ in range(0, filler_count)
        ]

    def post_fill(self) -> None:
        spheres = list(self.multiworld.get_spheres())
        sphere_count = len(spheres)
        upgrade_base = sphere_count * 2
        for current_sphere_count, sphere in enumerate(spheres):
            for location in sphere:
                if location.item.player == self.player:
                    if self.multiworld.random.randint(0, upgrade_base) < current_sphere_count:
                        self.upgrade_item(location.item)
        return

    def upgrade_item(self, item: Item):
        if item.name in Items.okay_items:
            new_item = self.multiworld.random.choice(Items.good_items)
            new_item_id = self.item_name_to_id[new_item]
            item.name = new_item
            item.code = new_item_id
            item.classification = ItemClassification.useful
        return

    def generate_output(self, output_directory: str):
        locations = dict()
        # get all locations
        for region in self.multiworld.regions:
            if region.player == self.player:
                for location in region.locations:
                    if location.name in Locations.minor_checks:
                        location_name = Rom.treasure_chest_data[location.name][2]
                    elif location.name in Locations.minor_ext_checks:
                        location_name = Rom.treasure_chest_data[location.name][2]
                    else:
                        location_name = location.name
                    locations[location_name] = "Archipelago Item"
                    if location.item.player == self.player:
                        if location_name in Locations.major_checks or location.item.name in Items.items:
                            locations[location_name] = location.item.name
        self.rom_name_text = f'6WC{Utils.__version__.replace(".", "")[0:3]}_{self.player}_{self.multiworld.seed:11}'
        self.rom_name_text = self.rom_name_text[:20]
        self.romName = bytearray(self.rom_name_text, 'utf-8')
        self.romName.extend([0] * (20 - len(self.romName)))
        self.rom_name = self.romName
        locations["RomName"] = self.rom_name_text
        placement_file = os.path.join(output_directory,
                                      f'{self.multiworld.get_out_file_name_base(self.player)}' + '.applacements')
        with open(placement_file, "w") as file:
            json.dump(locations, file, indent=2)
        output_file = os.path.join(output_directory,f"{self.multiworld.get_out_file_name_base(self.player)}.sfc")
        wc_args = ["-i", "Final Fantasy III (USA).sfc", "-o", f"{output_file}", "-ap", placement_file]
        wc_args.extend(generate_flagstring(self.multiworld, self.player, self.starting_characters))
        print(wc_args)
        with FF6WCWorld.wc_ready:
            import sys
            from copy import deepcopy
            module_keys = deepcopy(list(sys.modules.keys()))
            for module in module_keys:
                if str(module).startswith("worlds.ff6wc.WorldsCollide"):
                    del sys.modules[module]
            wc = WC()
            wc.main(wc_args)
            patch = FF6WCDeltaPatch(
                os.path.splitext(output_file)[0] + FF6WCDeltaPatch.patch_file_ending,
                player=self.player,
                player_name=self.multiworld.player_name[self.player],
                patched_path=output_file)
            patch.write()
            os.remove(output_file)
            os.remove(placement_file)
            self.rom_name_available_event.set()


    def modify_multidata(self, multidata: dict):
        import base64
        # wait for self.rom_name to be available.
        self.rom_name_available_event.wait()
        rom_name = getattr(self, "rom_name", None)
        # we skip in case of error, so that the original error in the output thread is the one that gets raised
        if rom_name:
            new_name = base64.b64encode(bytes(self.rom_name)).decode()
            multidata["connect_names"][new_name] = multidata["connect_names"][self.multiworld.player_name[self.player]]


class FF6WCItem(Item):
    game = 'Final Fantasy 6 Worlds Collide'


class FF6WCLocation(Location):
    game = 'Final Fantasy 6 Worlds Collide'

