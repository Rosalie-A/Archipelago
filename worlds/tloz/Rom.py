import hashlib
import json
import zlib
import os
from pkgutil import get_data

import bsdiff4

import Utils
from BaseClasses import ItemClassification
from worlds.Files import APDeltaPatch, APProcedurePatch, APTokenMixin, APPatchExtension

NA10CHECKSUM = '337bd6f1a1163df31bf2633665589ab0'
rom_name_location = 0x00
rom_name_length = 0x20
header_length = 0x10
player_name_location = 0x20
player_name_length = 0x40
major_offsets_location = 0x60
deathlink_options = 0x80
bit_positions = [0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80]
candle_shop = bit_positions[4]
arrow_shop = bit_positions[3]
potion_shop = bit_positions[2]
shield_shop = bit_positions[5]
ring_shop = bit_positions[6]
take_any = bit_positions[1]
left_shop_slots = 0x0628
middle_shop_slots = 0x0629
right_shop_slots = 0x062A
take_any_caves_checked = 0x0678
first_quest_dungeon_items_early = 0x18910
first_quest_dungeon_items_late = 0x18C10
game_mode = 0x12
fill_hearts = 0x63
death_mode_counter = 0xE5
items_obtained_low = 0x0677
items_obtained_high = 0x067B
sword = 0x0657
bombs = 0x0658
max_bombs = 0x067C
arrow = 0x0659
bow = 0x065A
candle = 0x065B
recorder = 0x065C
food = 0x065D
potion = 0x065E
magical_rod = 0x065F
raft = 0x0660
book_of_magic = 0x0661
ring = 0x0662
stepladder = 0x0663
magical_key = 0x0664
power_bracelet = 0x0665
letter = 0x0666
clock = 0x066C
keys = 0x066E
heart_containers = 0x066F
partial_hearts = 0x0670
triforce_fragments = 0x0671
triforce_count = 0x0679
boomerang = 0x0674
magical_boomerang = 0x0675
magical_shield = 0x0676
rupees_to_add = 0x067D

item_to_lift = 0x0505
item_lift_timer = 0x0506
sound_effect_queue = 0x0602


overworld_status_block = 0x067F
underworld_early_status_block = 0x06FF
underworld_late_status_block = 0x077F

cave_type_flags = {
    "Starting Sword Cave": 0b01000000,
    "Take Any Item": 0b01000100,
    "Door Repair": 0b01011100,
    "Potion Shop": 0b01101000,
    "Level 9": 0b00100100,
    "White Sword Pond": 0b01001000,
    "Level 5": 0b00010100,
    "Candle Shop": 0b01111000,
    "Letter Cave": 0b01100000,
    "Secret Money Large": 0b10001000,
    "Money Making Game": 0b01011000,
    "Shield Shop": 0b01111100,
    "Secret Money Medium": 0b10000100,
    "Go Up The Mountain Hint": 0b01101100,
    "Secret Is In Tree Hint": 0b01010100,
    "Warp Cave": 0b01010000,
    "Magical Sword Grave": 0b01001100,
    "Level 6": 0b00011000,
    "Arrow Shop": 0b01110100,
    "Blue Ring Shop": 0b10000000,
    "Level 2": 0b00001000,
    "Level 7": 0b00011100,
    "Level 4": 0b00010000,
    "Secret Money Small": 0b10001100,
    "Level 8": 0b00100000,
    "Lost Woods Hint": 0b01110000,
    "Level 3": 0b00001100,
    "Old Man Grave Hint": 0b01100100,
    "Level 1": 0b00000100
}

warp_cave_offset = 0x19344
starting_sword_cave_location_byte = 0x70
white_sword_pond_location_byte = 0x71
magical_sword_grave_location_byte = 0x72
letter_cave_location_byte = 0x73

shop_correspondance = {
    "Arrow Shop": arrow_shop,
    "Candle Shop": candle_shop,
    "Blue Ring Shop": ring_shop,
    "Shield Shop": shield_shop,
    "Potion Shop": potion_shop
}

item_frame_table_offset = 0x71A7
item_palette_table_offset = 0x6BD7
map_item_slot = 0x11
item_tiles_offset = 0x808F
compass_tile_offset = 0x6A0     # Offset from start of item tile sprites, not the rom!
archipelago_sprite = [ 0x03, 0x07, 0x3f, 0x7f, 0xff, 0xff, 0xc6, 0x00, 0x00, 0x00, 0x38, 0x7c, 0xfe, 0xfe, 0xfe, 0x7c, 0x00, 0x03, 0x07, 0x0f, 0x0f, 0x0f, 0x07, 0x03, 0xfe, 0xfc, 0xf8, 0x70, 0x30, 0x00, 0x00, 0x00 ]

compass_map_treasure_string_offset = 0x9471
remaining_red_blue_string_offset = 0x93A8
redundant_red_blue_string_offset = 0x93D1
triforce_string_offset = 0x9485
redundant_red_blue_table_offset = 0x94E1
triforce_table_offset = 0x94F5
archipelago_treasure_string = [6, 15, 18, 21, 21, 14, 27, 36, 36, 36, 36, 36, 25, 27, 24, 16, 27, 14, 28, 28, 18, 24, 23, 0xFF]

# The ROM is chopped up into banks that are loaded into memory at 0x8000, translate between them!
def rom_addr_to_memory_addr(address):
    if address < 0x10: return None 
    elif address < 0x1C010:
        address -= 0x10
        address %= 0x4000
        return address + 0x8000
    else:
        return address - 0x1C010 + 0xC000

def get_base_rom_bytes(file_name: str = "") -> bytes:
    base_rom_bytes = getattr(get_base_rom_bytes, "base_rom_bytes", None)
    if not base_rom_bytes:
        file_name = get_base_rom_path(file_name)
        base_rom_bytes = bytes(Utils.read_snes_rom(open(file_name, "rb")))

        basemd5 = hashlib.md5()
        basemd5.update(base_rom_bytes)
        if NA10CHECKSUM != basemd5.hexdigest():
            raise Exception('Supplied Base Rom does not match known MD5 for NA (1.0) release. '
                            'Get the correct game and version, then dump it')
        get_base_rom_bytes.base_rom_bytes = base_rom_bytes
    return base_rom_bytes


def get_base_rom_path(file_name: str = "") -> str:
    from worlds.tloz import TLoZWorld
    return TLoZWorld.settings.rom_file

class TLOZPatchExtension(APPatchExtension):
    game = "The Legend of Zelda"

    @staticmethod
    def apply_base_patch(rom):
        # The base patch source is on a different repo, so here's the summary of changes:
        # Remove Triforce check for recorder, so you can always warp.
        # Remove level check for Triforce Fragments (and maps and compasses, but this won't matter)
        # Replace some code with a jump to free space
        # Check if we're picking up a Triforce Fragment. If so, increment the local count
        # In either case, we do the instructions we overwrote with the jump and then return to normal flow
        # Remove map/compass check so they're always on
        # Removing a bit from the boss roars flags, so we can have more dungeon items. This allows us to
        # go past 0x1F items for dungeon items.
        base_patch = get_data(__name__, "z1_base_patch.bsdiff4")
        rom_data = bsdiff4.patch(rom.read(), base_patch)
        rom_data = bytearray(rom_data)
        # Set every item to the new nothing value, but keep room flags. Type 2 boss roars should
        # become type 1 boss roars, so we at least keep the sound of roaring where it should be.
        for i in range(0, 0x7F):
            item = rom_data[first_quest_dungeon_items_early + i]
            if item & 0b00100000:
                item = item & 0b11011111
                item = item | 0b01000000
                rom_data[first_quest_dungeon_items_early + i] = item
            if item & 0b00011111 == 0b00000011:  # Change all Item 03s to Item 3F, the proper "nothing"
                rom_data[first_quest_dungeon_items_early + i] = item | 0b00111111

            item = rom_data[first_quest_dungeon_items_late + i]
            if item & 0b00100000:
                item = item & 0b11011111
                item = item | 0b01000000
                rom_data[first_quest_dungeon_items_late + i] = item
            if item & 0b00011111 == 0b00000011:
                rom_data[first_quest_dungeon_items_late + i] = item | 0b00111111

        # Make the map item use the same sprite as the compass 
        rom_data[item_frame_table_offset + map_item_slot] = 0x18 
        # Change the palette to blue for non-progression items
        rom_data[item_palette_table_offset + map_item_slot] = 0x01
        for i in range(len(archipelago_sprite)):
            rom_data[item_tiles_offset + compass_tile_offset + i] = archipelago_sprite[i]

        # Move the string triforce to a redundant string block to give our message more room
        for i in range(10):
            rom_data[redundant_red_blue_string_offset + i] = rom_data[triforce_string_offset + i]
        memory_string_offset = rom_addr_to_memory_addr(redundant_red_blue_string_offset)
        rom_data[triforce_table_offset] = memory_string_offset & 0xFF
        rom_data[triforce_table_offset + 1] = (memory_string_offset >> 8) & 0xFF
        # Update a pointer from a redundant string to the remaining string
        memory_string_offset = rom_addr_to_memory_addr(remaining_red_blue_string_offset)
        rom_data[redundant_red_blue_table_offset] = memory_string_offset & 0xFF
        rom_data[redundant_red_blue_table_offset + 1] = (memory_string_offset >> 8) & 0xFF
        # Overwrite the compass and map string in the Treasures list with our new item descriptions
        for i in range(len(archipelago_treasure_string)):
            rom_data[compass_map_treasure_string_offset + i] = archipelago_treasure_string[i]

        return rom_data

    @staticmethod
    def write_entrances(rom_data, entrance_randomizer_set):
        from worlds.tloz import cave_data_location_start
        warp_caves = []
        for entrance, data in entrance_randomizer_set.items():
            entrance_offset = int(entrance[7:], 16)
            entrance_name = data
            entrance_flag = cave_type_flags[entrance_name]
            original_data = rom_data[cave_data_location_start + entrance_offset]
            original_data = original_data & 0b00000011
            new_data = entrance_flag | original_data
            rom_data[cave_data_location_start + entrance_offset] = new_data
            if entrance_name == "Warp Cave":
                warp_caves.append(entrance_offset)
            if entrance_name == "Starting Sword Cave":
                rom_data[starting_sword_cave_location_byte] = entrance_offset
            if entrance_name == "White Sword Pond":
                rom_data[white_sword_pond_location_byte] = entrance_offset
            if entrance_name == "Magical Sword Grave":
                rom_data[magical_sword_grave_location_byte] = entrance_offset
            if entrance_name == "Letter Cave":
                rom_data[letter_cave_location_byte] = entrance_offset
        for i, cave in enumerate(warp_caves):
            rom_data[warp_cave_offset + i] = cave
            print(hex(cave))
        return rom_data

    @staticmethod
    def apply_randomizer(caller, rom, placement_file):
        from worlds.tloz import (shop_price_location_ids, shop_locations, item_game_ids, location_ids,
                                 item_prices, secret_money_ids)
        placements: dict[str, any] = json.loads(caller.get_file(placement_file))
        with open(get_base_rom_path(), 'rb') as rom:
            rom_data = TLOZPatchExtension.apply_base_patch(rom)
            rom_data = TLOZPatchExtension.write_entrances(rom_data, placements["entrance_randomizer_set"])
        rom_name = bytearray(placements["meta"]["rom_name"][:rom_name_length], "utf8")[:rom_name_length]
        rom_name.extend([0] * (rom_name_length - len(rom_name)))
        rom_data[rom_name_location + header_length:rom_name_location + header_length + rom_name_length] = rom_name
        player_name = bytearray(placements["meta"]["player_name"], 'utf8')[:player_name_length]
        player_name.extend([0] * (player_name_length - len(player_name)))
        rom_data[player_name_location + header_length:player_name_location + header_length + player_name_length] = player_name
        rom_data[deathlink_options + header_length] = placements["meta"]["death_link"]

        # Write each location's new data in
        for location, item in placements.items():
            # Zelda and Ganon aren't real locations. Neither is the metadata.
            if location == "Ganon" or location == "Zelda" or location == "entrance_randomizer_set" or location == "meta":
                continue

            if "Secret Money" in location:
                rom_data[secret_money_ids[location]] = item
                continue

            if "Classification" in location:
                continue

            # Neither are boss defeat events
            if "Status" in location:
                continue
            item_id = item_game_ids[item]
            location_id = location_ids[location]

            # Shop prices need to be set
            if location in shop_locations:
                if location[-5:] == "Right":
                    # Final item in stores has bit 6 and 7 set. It's what marks the cave a shop.
                    item_id = item_id | 0b11000000
                price_location = shop_price_location_ids[location]
                rom_data[price_location] = item_prices[item]
            if location == "Take Any Item Right":
                # Same story as above: bit 6 is what makes this a Take Any cave
                item_id = item_id | 0b01000000
            rom_data[location_id] = item_id
        return rom_data


class TLOZProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "The Legend of Zelda"
    hash = NA10CHECKSUM
    patch_file_ending = ".aptloz"
    result_file_ending = ".nes"

    procedure = [
        ("apply_randomizer", ["placement_file.json"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        return get_base_rom_bytes()
