"""Django management command to disassemble enemies from ROM and generate Python implementations."""

from django.core.management.base import BaseCommand
from pathlib import Path
import importlib

class Command(BaseCommand):
    help = "Disassemble enemies from ROM and generate Python enemy definitions"

    def add_arguments(self, parser):
        parser.add_argument(
            "-r",
            "--rom",
            dest="rom",
            required=True,
            help="Path to a Mario RPG ROM file",
        )
        parser.add_argument(
            "-o",
            "--output",
            dest="output",
            default="src/disassembler_output/enemies/enemies.py",
            help="Output file path",
        )

    def handle(self, *args, **options):
        rom_path = options["rom"]
        output_path = options["output"]

        # read rom
        with open(rom_path, "rb") as f:
            rom = bytearray(f.read())

        # load item collection to get item id to class name mappings
        item_id_to_class = self._load_item_mapping()

        # constants from enemies/classes.py
        ENEMY_POINTER_TABLE_ADDRESS = 0x390026
        BASE_ENEMY_BANK = 0x390000  # bank for enemy data pointers
        REWARD_POINTER_TABLE_ADDRESS = 0x39142A
        REWARD_DATA_BANK = 0x390000  # bank for reward data pointers
        FLOWER_BONUS_BASE_ADDRESS = 0x39BB44
        ENEMY_NAME_BASE_ADDRESS = 0x3992D1
        PSYCHOPATH_POINTER_ADDRESS = 0x399FD1
        PSYCHOPATH_DATA_POINTER_OFFSET = 0x390000
        NUM_ENEMIES = 256

        # read the enemy pointer table (256 * 2-byte pointers)
        enemy_pointers = []
        for i in range(NUM_ENEMIES):
            ptr_offset = ENEMY_POINTER_TABLE_ADDRESS + (i * 2)
            pointer_value = rom[ptr_offset] | (rom[ptr_offset + 1] << 8)
            # convert to full address (add bank)
            full_address = BASE_ENEMY_BANK | pointer_value
            enemy_pointers.append(full_address)

        # read the reward pointer table (256 * 2-byte pointers)
        reward_pointers = []
        for i in range(NUM_ENEMIES):
            ptr_offset = REWARD_POINTER_TABLE_ADDRESS + (i * 2)
            pointer_value = rom[ptr_offset] | (rom[ptr_offset + 1] << 8)
            # convert to full address (add bank)
            full_address = REWARD_DATA_BANK | pointer_value
            reward_pointers.append(full_address)

        # read psychopath messages from rom
        psychopath_messages = self._read_psychopath_messages(
            rom,
            PSYCHOPATH_POINTER_ADDRESS,
            PSYCHOPATH_DATA_POINTER_OFFSET,
            NUM_ENEMIES
        )

        # process each enemy
        used_class_names = {}
        class_names = []  # store class names for enemycollection
        used_item_classes: set[str] = set()  # track which item classes are used

        enemy_definitions = []
        for enemy_id in range(NUM_ENEMIES):
            enemy_data = self._parse_enemy(
                rom,
                enemy_id,
                enemy_pointers[enemy_id],  # use pointer from table
                reward_pointers[enemy_id],  # use pointer from table
                FLOWER_BONUS_BASE_ADDRESS,
                ENEMY_NAME_BASE_ADDRESS
            )

            # add psychopath message to enemy data
            enemy_data["psychopath_message"] = psychopath_messages[enemy_id]

            # generate unique class name
            class_name = self._generate_class_name(enemy_data["name"], used_class_names)
            class_names.append(class_name)

            class_def = self._generate_class_definition(
                enemy_id, enemy_data, class_name, item_id_to_class, used_item_classes
            )
            enemy_definitions.append(class_def)

        # generate output with imports
        output_lines = []
        output_lines.append("from smrpgpatchbuilder.datatypes.enemies.classes import (")
        output_lines.append("    Enemy,")
        output_lines.append("    EnemyCollection,")
        output_lines.append(")")
        output_lines.append("from smrpgpatchbuilder.datatypes.enemies.enums import (")
        output_lines.append("    ApproachSound,")
        output_lines.append("    HitSound,")
        output_lines.append("    FlowerBonusType,")
        output_lines.append("    CoinSprite,")
        output_lines.append("    EntranceStyle,")
        output_lines.append(")")
        output_lines.append("from smrpgpatchbuilder.datatypes.spells.enums import Element, Status")
        output_lines.append("from smrpgpatchbuilder.datatypes.items.classes import RegularItem")
        output_lines.append("from ..items import *")    

        output_lines.append("")
        output_lines.append("")

        # add enemy definitions
        for class_def in enemy_definitions:
            output_lines.extend(class_def)
            output_lines.append("")
            output_lines.append("")

        # generate enemycollection
        output_lines.append("")
        output_lines.append("# Enemy collection containing all enemies")
        output_lines.append("ALL_ENEMIES = EnemyCollection([")
        for class_name in class_names:
            output_lines.append(f"    {class_name}(),")
        output_lines.append("])")
        output_lines.append("")

        # write output file
        output_file = Path(output_path)
        output_file.parent.mkdir(parents=True, exist_ok=True)
        output_file.write_text("\n".join(output_lines))

        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated {NUM_ENEMIES} enemy definitions to {output_path}")
        )

    def _load_item_mapping(self) -> dict[int, str]:
        """load all_items and build item id to class name mapping.

        returns:
            dict mapping item ids to class names
        """
        # import all_items from the disassembler output
        module_path = "disassembler_output.items.items"

        try:
            module = importlib.import_module(module_path)
        except ImportError as e:
            raise ValueError(f"Could not load items from {module_path}: {e}")

        # get all_items
        all_items = getattr(module, "ALL_ITEMS", None)
        if all_items is None:
            raise ValueError("Could not find ALL_ITEMS in items.py")

        # build the mapping (item_id -> class name)
        item_id_to_class = {}
        for item in all_items.items:
            item_id = item.item_id
            class_name = item.__class__.__name__
            item_id_to_class[item_id] = class_name

        return item_id_to_class

    def _parse_enemy(self, rom, enemy_id, enemy_addr, reward_data_addr, flower_bonus_addr,
                     name_addr):
        """parse enemy data from rom.

        args:
            rom: rom data
            enemy_id: enemy index (0-255)
            enemy_addr: full rom address where enemy data is stored
            reward_data_addr: full rom address where reward data is stored
            flower_bonus_addr: base address for flower bonus data
            name_addr: base address for enemy names
        """
        # read enemy name
        name_offset = name_addr + (enemy_id * 13)
        name = self._parse_enemy_name(rom, name_offset)

        # main stats (16 bytes at enemy_addr)
        data = rom[enemy_addr : enemy_addr + 16]

        # bytes 0-1: hp (little-endian)
        hp = data[0] | (data[1] << 8)

        # byte 2: speed
        speed = data[2]

        # byte 3: attack
        attack = data[3]

        # byte 4: defense
        defense = data[4]

        # byte 5: magic attack
        magic_attack = data[5]

        # byte 6: magic defense
        magic_defense = data[6]

        # byte 7: fp
        fp = data[7]

        # byte 8: evade
        evade = data[8]

        # byte 9: magic evade
        magic_evade = data[9]

        # byte 10: flags (disable_auto_death and share_palette)
        byte10 = data[10]
        disable_auto_death = bool(byte10 & 0x01)
        share_palette = bool(byte10 & 0x02)

        # bytes 11-14: special properties
        # byte 11: hit/special defense and sound on hit (top half)
        byte11 = data[11]
        invincible = bool(byte11 & 0x01)
        ohko_immune = bool(byte11 & 0x02)
        morph_chance_bits = (byte11 & 0x0C) >> 2
        morph_chance_map = {0: 0, 1: 25, 2: 75, 3: 100}
        morph_chance = morph_chance_map[morph_chance_bits]
        sound_on_hit_value = (byte11 >> 4) & 0x0F

        # byte 12: elemental resistances
        elemental_resistances = self._parse_bitfield_to_elements(data[12])

        # byte 13: elemental weaknesses (top half) and sound on approach (bottom half)
        byte13 = data[13]
        sound_on_approach_value = byte13 & 0x0F
        weaknesses = []
        for bit_pos in [4, 5, 6, 7]:
            if byte13 & (1 << bit_pos):
                weaknesses.append(bit_pos)

        # byte 14: status immunities
        status_immunities = self._parse_bitfield_to_statuses(data[14])

        # byte 15: entrance style (lower 4 bits), elevate (bits 4-5), coin sprite (bits 6-7)
        byte15 = data[15]
        entrance_style_value = byte15 & 0x0F
        elevate = (byte15 >> 4) & 0x03
        coin_sprite_value = (byte15 >> 6) & 0x03

        # read reward data (6 bytes at reward_data_addr)
        reward_data = rom[reward_data_addr : reward_data_addr + 6]

        # bytes 0-1: xp (little-endian)
        xp = reward_data[0] | (reward_data[1] << 8)

        # byte 2: coins
        coins = reward_data[2]

        # byte 3: yoshi cookie item
        yoshi_cookie_item_id = reward_data[3]

        # byte 4: common item drop
        common_item_drop = reward_data[4] if reward_data[4] != 0xFF else None

        # byte 5: rare item drop
        rare_item_drop = reward_data[5] if reward_data[5] != 0xFF else None

        # read flower bonus
        bonus_offset = flower_bonus_addr + enemy_id
        bonus_byte = rom[bonus_offset]
        flower_bonus_chance = ((bonus_byte >> 4) & 0x0F) * 10
        flower_bonus_type_value = bonus_byte & 0x0F

        # read cursor position (1 byte: cursorX in upper 4 bits, cursorY in lower 4 bits)
        cursor_offset = 0x39B944 + enemy_id
        cursor_byte = rom[cursor_offset]
        cursor_x = (cursor_byte >> 4) & 0x0F
        cursor_y = cursor_byte & 0x0F

        return {
            "name": name,
            "hp": hp,
            "fp": fp,
            "speed": speed,
            "attack": attack,
            "defense": defense,
            "magic_attack": magic_attack,
            "magic_defense": magic_defense,
            "evade": evade,
            "magic_evade": magic_evade,
            "disable_auto_death": disable_auto_death,
            "share_palette": share_palette,
            "invincible": invincible,
            "ohko_immune": ohko_immune,
            "morph_chance": morph_chance,
            "sound_on_hit": sound_on_hit_value,
            "elemental_resistances": elemental_resistances,
            "weaknesses": weaknesses,
            "sound_on_approach": sound_on_approach_value,
            "status_immunities": status_immunities,
            "entrance_style": entrance_style_value,
            "elevate": elevate,
            "coin_sprite": coin_sprite_value,
            "xp": xp,
            "coins": coins,
            "yoshi_cookie_item_id": yoshi_cookie_item_id,
            "common_item_drop": common_item_drop,
            "rare_item_drop": rare_item_drop,
            "flower_bonus_chance": flower_bonus_chance,
            "flower_bonus_type": flower_bonus_type_value,
            "cursor_x": cursor_x,
            "cursor_y": cursor_y,
        }

    def _read_psychopath_messages(self, rom, pointer_addr, pointer_offset, num_enemies):
        """read all psychopath messages from rom using the pointer table.

        args:
            rom: rom bytearray
            pointer_addr: address of the pointer table
            pointer_offset: offset to add to pointers to get actual address
            num_enemies: number of enemies to read

        returns:
            list of psychopath message strings
        """
        from smrpgpatchbuilder.datatypes.dialogs.utils import decompress, COMPRESSION_TABLE

        # use compression table from entry with byte 0x22 onward (index 17)
        # convert bytes to bytearray for decompress function
        psychopath_compression_table = [("\n", bytearray(b"\x01")), ("[await]", bytearray(b"\x02"))] + [
            (key, bytearray(value)) for key, value in COMPRESSION_TABLE[17:]
        ]

        messages = []

        for enemy_id in range(num_enemies):
            # read pointer (little-endian 2 bytes)
            ptr_offset = pointer_addr + (enemy_id * 2)
            pointer_value = rom[ptr_offset] | (rom[ptr_offset + 1] << 8)

            # calculate actual address (add bank offset 0x390000)
            message_addr = pointer_offset + pointer_value

            # read message (null-terminated)
            message_bytes = []
            idx = message_addr
            while idx < len(rom):
                byte = rom[idx]
                if byte == 0x00:  # null terminator
                    break
                message_bytes.append(byte)
                idx += 1

            # decode message using compression table
            if message_bytes:
                message = decompress(bytes(message_bytes), psychopath_compression_table)
            else:
                message = ""

            messages.append(message)

        return messages

    def _parse_enemy_name(self, rom, offset):
        """parse enemy name from rom (13 bytes, strip trailing 0x20).

        returns name string
        """
        name_bytes = rom[offset : offset + 13]

        # extract the name and strip trailing spaces (0x20)
        name_chars = list(name_bytes)
        while name_chars and name_chars[-1] == 0x20:
            name_chars.pop()

        # build the name with special character replacements
        name_parts = []
        for b in name_chars:
            if b == 0x7D:
                name_parts.append('-')  # standard hyphen
            elif b == 0x7E:
                name_parts.append('\u2019')  # closing quote (u+2019: ')
            else:
                try:
                    name_parts.append(chr(b))
                except:
                    name_parts.append('?')

        name = ''.join(name_parts)

        return name if name else "UnnamedEnemy"

    def _generate_class_name(self, enemy_name, used_names):
        """Generate a valid Python class name from enemy name, handling duplicates."""
        # clean up the name for use as a class name
        base_name = enemy_name.replace(" ", "").replace("-", "").replace("'", "").replace(".", "")
        # remove any non-alphanumeric characters
        base_name = ''.join(c for c in base_name if c.isalnum())

        # ensure it starts with a letter
        if not base_name or not base_name[0].isalpha():
            base_name = "Unnamed"

        # track occurrence for duplicates
        if base_name not in used_names:
            used_names[base_name] = 0

        used_names[base_name] += 1
        occurrence = used_names[base_name]

        # generate class name with "Enemy" suffix
        if occurrence > 1:
            class_name = f"{base_name}Enemy{occurrence}"
        else:
            class_name = f"{base_name}Enemy"

        return class_name

    def _parse_bitfield_to_elements(self, bitfield):
        """Parse bitfield to Element enum list."""
        elements = []
        element_map = {
            4: "Element.ICE",
            5: "Element.THUNDER",
            6: "Element.FIRE",
            7: "Element.JUMP",
        }
        for bit_pos, element in element_map.items():
            if bitfield & (1 << bit_pos):
                elements.append(element)
        return elements

    def _parse_bitfield_to_statuses(self, bitfield):
        """Parse bitfield to Status enum list."""
        statuses = []
        status_map = {
            0: "Status.MUTE",
            1: "Status.SLEEP",
            2: "Status.POISON",
            3: "Status.FEAR",
            4: "Status.BERSERK",
            5: "Status.MUSHROOM",
            6: "Status.SCARECROW",
            7: "Status.INVINCIBLE",
        }
        for bit_pos, status in status_map.items():
            if bitfield & (1 << bit_pos):
                statuses.append(status)
        return statuses

    def _generate_class_definition(self, enemy_id, data, class_name, item_id_to_class, used_item_classes):
        """Generate Python class definition for an enemy."""
        # import enums to build mappings dynamically
        from smrpgpatchbuilder.datatypes.enemies.enums import (
            HitSound, FlowerBonusType, ApproachSound, CoinSprite, EntranceStyle
        )

        # build enum mappings dynamically
        hit_sound_map = {member.value: f"HitSound.{member.name}" for member in HitSound}
        flower_bonus_map = {member.value: f"FlowerBonusType.{member.name}" for member in FlowerBonusType}
        approach_sound_map = {member.value: f"ApproachSound.{member.name}" for member in ApproachSound}
        coin_sprite_map = {member.value: f"CoinSprite.{member.name}" for member in CoinSprite}
        entrance_style_map = {member.value: f"EntranceStyle.{member.name}" for member in EntranceStyle}

        lines = []

        lines.append(f"class {class_name}(Enemy):")
        lines.append(f'    """{data["name"]} enemy class"""')
        lines.append(f"    _monster_id: int = {enemy_id}")
        lines.append(f'    _name: str = "{data["name"]}"')
        lines.append("")

        # stats
        lines.append(f"    _hp: int = {data['hp']}")
        lines.append(f"    _fp: int = {data['fp']}")
        lines.append(f"    _attack: int = {data['attack']}")
        lines.append(f"    _defense: int = {data['defense']}")
        lines.append(f"    _magic_attack: int = {data['magic_attack']}")
        lines.append(f"    _magic_defense: int = {data['magic_defense']}")
        lines.append(f"    _speed: int = {data['speed']}")
        lines.append(f"    _evade: int = {data['evade']}")
        lines.append(f"    _magic_evade: int = {data['magic_evade']}")

        # status immunities
        if data["status_immunities"]:
            immunities_str = ", ".join(data["status_immunities"])
            lines.append(f"    _status_immunities: list[Status] = [{immunities_str}]")

        # weaknesses (convert bit positions to elements)
        if data["weaknesses"]:
            weakness_map = {4: "Element.ICE", 5: "Element.THUNDER", 6: "Element.FIRE", 7: "Element.JUMP"}
            weaknesses_list = [weakness_map[w] for w in data["weaknesses"] if w in weakness_map]
            if weaknesses_list:
                weaknesses_str = ", ".join(weaknesses_list)
                lines.append(f"    _weaknesses: list[Element] = [{weaknesses_str}]")

        # resistances
        if data["elemental_resistances"]:
            resistances_str = ", ".join(data["elemental_resistances"])
            lines.append(f"    _resistances: list[Element] = [{resistances_str}]")

        # rewards
        lines.append(f"    _xp: int = {data['xp']}")
        lines.append(f"    _coins: int = {data['coins']}")

        # yoshi cookie item (always present)
        yoshi_cookie_item_class = item_id_to_class.get(data["yoshi_cookie_item_id"])
        if yoshi_cookie_item_class:
            used_item_classes.add(yoshi_cookie_item_class)
            lines.append(f"    _yoshi_cookie_item = {yoshi_cookie_item_class}")

        if data["rare_item_drop"] is not None:
            rare_item_class = item_id_to_class.get(data["rare_item_drop"])
            if rare_item_class:
                used_item_classes.add(rare_item_class)
                lines.append(f"    _rare_item_drop = {rare_item_class}")

        if data["common_item_drop"] is not None:
            common_item_class = item_id_to_class.get(data["common_item_drop"])
            if common_item_class:
                used_item_classes.add(common_item_class)
                lines.append(f"    _common_item_drop = {common_item_class}")

        # flower bonus
        if data["flower_bonus_type"] in flower_bonus_map:
            lines.append(f"    _flower_bonus_type: FlowerBonusType = {flower_bonus_map[data['flower_bonus_type']]}")
        elif data["flower_bonus_type"] != 0:
            lines.append(f"    # WARNING: Unknown flower_bonus_type value: {data['flower_bonus_type']}")

        if data["flower_bonus_chance"] > 0:
            lines.append(f"    _flower_bonus_chance: int = {data['flower_bonus_chance']}")

        # other properties
        if data["morph_chance"] > 0:
            lines.append(f"    _morph_chance: float = {data['morph_chance']}")

        # sound on hit enum
        if data["sound_on_hit"] in hit_sound_map:
            lines.append(f"    _sound_on_hit: HitSound = {hit_sound_map[data['sound_on_hit']]}")
        elif data["sound_on_hit"] != 0:  # only warn if non-default
            lines.append(f"    # WARNING: Unknown sound_on_hit value: {data['sound_on_hit']}")

        # sound on approach enum
        if data["sound_on_approach"] in approach_sound_map:
            lines.append(f"    _sound_on_approach: ApproachSound = {approach_sound_map[data['sound_on_approach']]}")
        elif data["sound_on_approach"] != 0:
            lines.append(f"    # WARNING: Unknown sound_on_approach value: {data['sound_on_approach']}")

        # coin sprite enum
        if data["coin_sprite"] in coin_sprite_map:
            lines.append(f"    _coin_sprite: CoinSprite = {coin_sprite_map[data['coin_sprite']]}")
        elif data["coin_sprite"] != 0:
            lines.append(f"    # WARNING: Unknown coin_sprite value: {data['coin_sprite']}")

        # entrance style enum
        if data["entrance_style"] in entrance_style_map:
            lines.append(f"    _entrance_style: EntranceStyle = {entrance_style_map[data['entrance_style']]}")
        elif data["entrance_style"] != 0:
            lines.append(f"    # WARNING: Unknown entrance_style value: {data['entrance_style']}")

        # elevation
        if data["elevate"] > 0:
            lines.append(f"    _elevate: int = {data['elevate']}")

        # cursor position
        if data["cursor_x"] > 0:
            lines.append(f"    _cursor_x: int = {data['cursor_x']}")
        if data["cursor_y"] > 0:
            lines.append(f"    _cursor_y: int = {data['cursor_y']}")

        # flags
        if data["invincible"]:
            lines.append("    _invincible: bool = True")
        if data["ohko_immune"]:
            lines.append("    _ohko_immune: bool = True")
        if data["disable_auto_death"]:
            lines.append("    _disable_auto_death: bool = True")
        if data["share_palette"]:
            lines.append("    _share_palette: bool = True")

        # psychopath message (escape backslashes, newlines, and quotes)
        psychopath = data.get("psychopath_message", "")
        psychopath_escaped = psychopath.replace("\\", "\\\\").replace('\n', '\\n').replace('"', '\\"')
        lines.append(f'    _psychopath_message: str = "{psychopath_escaped}"')

        return lines
