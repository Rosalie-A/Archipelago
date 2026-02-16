"""Django management command to disassemble ally/character data from a ROM."""

from django.core.management.base import BaseCommand
from smrpgpatchbuilder.datatypes.allies.ally import Ally, LevelUp, AllyCoordinate
from smrpgpatchbuilder.datatypes.spells.classes import SpellCollection
from smrpgpatchbuilder.utils.disassembler_common import writeline
import os
import importlib

class Command(BaseCommand):
    help = "Disassemble ally/character data from a ROM"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", required=True, help="Path to a Mario RPG ROM file")
        parser.add_argument(
            "-o",
            "--output",
            dest="output",
            default="src/disassembler_output/allies/allies.py",
            help="Output file path",
        )

    def handle(self, *args, **options):
        rom_path = options["rom"]
        output_path = options["output"]

        # Load ROM
        #self.stdout.write(f"Loading ROM from {rom_path}...")
        with open(rom_path, "rb") as f:
            rom = f.read()

        # Load spell classes
        #self.stdout.write("Loading character spells...")
        spell_index_to_class = self._load_spell_classes()

        # Load item classes
        #self.stdout.write("Loading items...")
        item_index_to_class = self._load_item_classes()

        # Disassemble all 5 allies
        allies = []
        ally_names = ["Mario", "Mallow", "Geno", "Bowser", "Toadstool"]

        for ally_index in range(5):
            #self.stdout.write(f"Disassembling {ally_names[ally_index]}...")
            ally = self._disassemble_ally(rom, ally_index, spell_index_to_class, item_index_to_class)
            allies.append(ally)

        # Write output file
        #self.stdout.write(f"Writing to {output_path}...")
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        with open(output_path, "w", encoding="utf-8") as f:
            self._write_allies_file(f, allies)

        self.stdout.write(self.style.SUCCESS(f"Successfully disassembled allies to {output_path}"))

    def _load_spell_classes(self):
        """Load character spell classes from disassembler output.

        Returns:
            Dictionary mapping spell index to spell class
        """
        try:
            # Import the spells module
            spells_module = importlib.import_module("disassembler_output.spells.spells")

            # Build index to class mapping
            spell_index_to_class = {}

            # Get the spell collection (it's called ALL_SPELLS in the output)
            if hasattr(spells_module, "ALL_SPELLS"):
                spell_collection: SpellCollection = spells_module.ALL_SPELLS
                for spell in spell_collection.spells:
                    if spell.index <= 26:
                        spell_index_to_class[spell.index] = type(spell)
            
            return spell_index_to_class
        except ImportError as e:
            #self.stdout.write(self.style.WARNING(f"Could not load spells: {e}"))
            return {}

    def _load_item_classes(self):
        """Load item classes from disassembler output.

        Returns:
            Dictionary mapping item index to item class
        """
        try:
            # Import the items module
            items_module = importlib.import_module("disassembler_output.items.items")

            # Build index to class mapping
            item_index_to_class = {}

            # Get the item collection (it's called ALL_ITEMS in the output)
            if hasattr(items_module, "ALL_ITEMS"):
                from smrpgpatchbuilder.datatypes.items.classes import ItemCollection
                item_collection: ItemCollection = items_module.ALL_ITEMS
                for item in item_collection.items:
                    item_index_to_class[item.index] = type(item)
            
            return item_index_to_class
        except ImportError as e:
            #self.stdout.write(self.style.WARNING(f"Could not load items: {e}"))
            return {}

    def _disassemble_ally(self, rom: bytes, index: int, spell_index_to_class: dict, item_index_to_class: dict) -> Ally:
        """Disassemble a single ally from ROM data.

        Based on Character.cs lines 78-120.
        """
        # Starting stats - 20 bytes per character at 0x3A002C
        offset = (index * 20) + 0x3A002C
        starting_level = rom[offset]
        offset += 1
        starting_current_hp = rom[offset] | (rom[offset + 1] << 8)
        offset += 2
        starting_max_hp = rom[offset] | (rom[offset + 1] << 8)
        offset += 2
        starting_speed = rom[offset]
        offset += 1
        starting_attack = rom[offset]
        offset += 1
        starting_defense = rom[offset]
        offset += 1
        starting_mg_attack = rom[offset]
        offset += 1
        starting_mg_defense = rom[offset]
        offset += 1
        starting_experience = rom[offset] | (rom[offset + 1] << 8)
        offset += 2
        starting_weapon_byte = rom[offset]
        offset += 1
        starting_armor_byte = rom[offset]
        offset += 1
        starting_accessory_byte = rom[offset]
        offset += 2  # Skip one byte

        # Map equipment bytes to item classes (0xFF = None/no item)
        starting_weapon = None if starting_weapon_byte == 0xFF else item_index_to_class.get(starting_weapon_byte, None)
        starting_armor = None if starting_armor_byte == 0xFF else item_index_to_class.get(starting_armor_byte, None)
        starting_accessory = None if starting_accessory_byte == 0xFF else item_index_to_class.get(starting_accessory_byte, None)

        # Starting magic - 32 bits (4 bytes)
        # Convert to list of spell classes the character starts with
        starting_magic_bits = []
        for byte_idx in range(4):
            byte_val = rom[offset + byte_idx]
            for bit_idx in range(8):
                starting_magic_bits.append((byte_val >> bit_idx) & 1 == 1)

        # Build list of spell classes from bit array
        starting_magic = []
        for spell_index, has_spell in enumerate(starting_magic_bits):
            if has_spell and spell_index in spell_index_to_class:
                starting_magic.append(spell_index_to_class[spell_index])

        # Character name - 10 characters at 0x3A134D
        name_offset = (index * 10) + 0x3A134D
        name_bytes = rom[name_offset:name_offset + 10]
        name = "".join(chr(b) if b >= 0x20 else " " for b in name_bytes).rstrip()

        # Level-ups (levels 2-30, total 29 levels)
        levels = []
        for level in range(2, 31):
            level_up = self._disassemble_level_up(rom, level, index, spell_index_to_class)
            levels.append(level_up)

        # Coordinates
        coordinates = self._disassemble_coordinates(rom, index)

        return Ally(
            index=index,
            name=name,
            starting_level=starting_level,
            starting_current_hp=starting_current_hp,
            starting_max_hp=starting_max_hp,
            starting_speed=starting_speed,
            starting_attack=starting_attack,
            starting_defense=starting_defense,
            starting_mg_attack=starting_mg_attack,
            starting_mg_defense=starting_mg_defense,
            starting_experience=starting_experience,
            starting_weapon=starting_weapon,
            starting_armor=starting_armor,
            starting_accessory=starting_accessory,
            starting_magic=starting_magic,
            levels=levels,
            coordinates=coordinates,
        )

    def _disassemble_level_up(self, rom: bytes, level: int, owner: int, spell_index_to_class: dict) -> LevelUp:
        """Disassemble level-up data for a specific level.

        Based on LevelUp.Disassemble() lines 208-231.
        """
        # Experience needed (shared across all characters)
        exp_offset = 0x3A1AFF + ((level - 2) * 2)
        exp_needed = rom[exp_offset] | (rom[exp_offset + 1] << 8)

        # Stat increases - 3 bytes per character, 15 bytes per level
        stat_offset = (owner * 3) + ((level - 2) * 15) + 0x3A1B39
        hp_plus = rom[stat_offset]
        stat_offset += 1

        temp = rom[stat_offset]
        attack_plus = (temp & 0xF0) >> 4
        defense_plus = temp & 0x0F
        stat_offset += 1

        temp = rom[stat_offset]
        mg_attack_plus = (temp & 0xF0) >> 4
        mg_defense_plus = temp & 0x0F

        # Bonus stat increases - same structure
        bonus_offset = (owner * 3) + ((level - 2) * 15) + 0x3A1CEC
        hp_plus_bonus = rom[bonus_offset]
        bonus_offset += 1

        temp = rom[bonus_offset]
        attack_plus_bonus = (temp & 0xF0) >> 4
        defense_plus_bonus = temp & 0x0F
        bonus_offset += 1

        temp = rom[bonus_offset]
        mg_attack_plus_bonus = (temp & 0xF0) >> 4
        mg_defense_plus_bonus = temp & 0x0F

        # Spell learned
        spell_offset = owner + ((level - 2) * 5) + 0x3A42F5
        spell_learned_byte = rom[spell_offset]

        # Map byte to spell class
        if spell_learned_byte > 0x1F:
            spell_learned = None  # No spell
        else:
            spell_learned = spell_index_to_class.get(spell_learned_byte, None)
            
        return LevelUp(
            level=level,
            exp_needed=exp_needed,
            spell_learned=spell_learned,
            hp_plus=hp_plus,
            attack_plus=attack_plus,
            defense_plus=defense_plus,
            mg_attack_plus=mg_attack_plus,
            mg_defense_plus=mg_defense_plus,
            hp_plus_bonus=hp_plus_bonus,
            attack_plus_bonus=attack_plus_bonus,
            defense_plus_bonus=defense_plus_bonus,
            mg_attack_plus_bonus=mg_attack_plus_bonus,
            mg_defense_plus_bonus=mg_defense_plus_bonus,
        )

    def _disassemble_coordinates(self, rom: bytes, index: int) -> AllyCoordinate:
        """Disassemble ally battle coordinates.

        Based on AllyCoordinate.Disassemble() lines 297-312.
        """
        # Regular coordinates
        temp = rom[0x029752 + index]
        cursor_x = (temp & 0xF0) >> 4
        cursor_y = temp & 0x0F

        sprite_abxy_y = rom[0x023685 + (index * 2)]

        # Scarecrow coordinates (shared)
        temp = rom[0x029757]
        cursor_x_scarecrow = (temp & 0xF0) >> 4
        cursor_y_scarecrow = temp & 0x0F

        sprite_abxy_y_scarecrow = rom[0x02346E]

        return AllyCoordinate(
            cursor_x=cursor_x,
            cursor_y=cursor_y,
            sprite_abxy_y=sprite_abxy_y,
            cursor_x_scarecrow=cursor_x_scarecrow,
            cursor_y_scarecrow=cursor_y_scarecrow,
            sprite_abxy_y_scarecrow=sprite_abxy_y_scarecrow,
        )

    def _write_allies_file(self, file, allies: list):
        """Write all allies to a Python file."""
        writeline(file, "\"\"\"Ally/Character data disassembled from ROM.\"\"\"")
        writeline(file, "")
        writeline(file, "from smrpgpatchbuilder.datatypes.allies.ally import Ally, LevelUp, AllyCoordinate")
        writeline(file, "from smrpgpatchbuilder.datatypes.allies.ally_collection import AllyCollection")
        writeline(file, "from disassembler_output.spells.spells import *")
        writeline(file, "from disassembler_output.items.items import *")
        writeline(file, "")

        for ally in allies:
            self._write_ally(file, ally)
            writeline(file, "")

        # Write AllyCollection
        writeline(file, "ally_collection = AllyCollection(")
        writeline(file, "    allies=[")
        for ally in allies:
            var_name = ally.name.upper() + "_Ally"
            writeline(file, f"        {var_name},")
        writeline(file, "    ]")
        writeline(file, ")")

    def _write_ally(self, file, ally: Ally):
        """Write a single ally to the file."""
        var_name = ally.name.upper() + "_Ally"
        writeline(file, f"{var_name} = Ally(")
        writeline(file, f"    index={ally.index},")
        writeline(file, f"    name=\"{ally.name}\",")
        writeline(file, f"    starting_level={ally.starting_level},")
        writeline(file, f"    starting_current_hp={ally.starting_current_hp},")
        writeline(file, f"    starting_max_hp={ally.starting_max_hp},")
        writeline(file, f"    starting_speed={ally.starting_speed},")
        writeline(file, f"    starting_attack={ally.starting_attack},")
        writeline(file, f"    starting_defense={ally.starting_defense},")
        writeline(file, f"    starting_mg_attack={ally.starting_mg_attack},")
        writeline(file, f"    starting_mg_defense={ally.starting_mg_defense},")
        writeline(file, f"    starting_experience={ally.starting_experience},")

        # Write equipment as item class names
        weapon_name = ally.starting_weapon.__name__ if ally.starting_weapon else "None"
        armor_name = ally.starting_armor.__name__ if ally.starting_armor else "None"
        accessory_name = ally.starting_accessory.__name__ if ally.starting_accessory else "None"

        writeline(file, f"    starting_weapon={weapon_name},")
        writeline(file, f"    starting_armor={armor_name},")
        writeline(file, f"    starting_accessory={accessory_name},")

        # Starting magic (list of spell classes)
        if ally.starting_magic:
            writeline(file, f"    starting_magic=[")
            for spell_class in ally.starting_magic:
                writeline(file, f"        {spell_class.__name__},")
            writeline(file, f"    ],")
        else:
            writeline(file, f"    starting_magic=[],")

        # Levels
        writeline(file, f"    levels=[")
        for level_up in ally.levels:
            self._write_level_up(file, level_up)
        writeline(file, f"    ],")

        # Coordinates
        writeline(file, f"    coordinates=AllyCoordinate(")
        writeline(file, f"        cursor_x={ally.coordinates.cursor_x},")
        writeline(file, f"        cursor_y={ally.coordinates.cursor_y},")
        writeline(file, f"        sprite_abxy_y={ally.coordinates.sprite_abxy_y},")
        writeline(file, f"        cursor_x_scarecrow={ally.coordinates.cursor_x_scarecrow},")
        writeline(file, f"        cursor_y_scarecrow={ally.coordinates.cursor_y_scarecrow},")
        writeline(file, f"        sprite_abxy_y_scarecrow={ally.coordinates.sprite_abxy_y_scarecrow},")
        writeline(file, f"    ),")
        writeline(file, f")")

    def _write_level_up(self, file, level_up: LevelUp):
        """Write a single level-up entry."""
        writeline(file, f"        LevelUp(")
        writeline(file, f"            level={level_up.level},")
        writeline(file, f"            exp_needed={level_up.exp_needed},")

        # Write spell_learned as class name or None
        if level_up.spell_learned is None:
            writeline(file, f"            spell_learned=None,")
        else:
            spell_class_name = level_up.spell_learned.__name__
            writeline(file, f"            spell_learned={spell_class_name},")

        writeline(file, f"            hp_plus={level_up.hp_plus},")
        writeline(file, f"            attack_plus={level_up.attack_plus},")
        writeline(file, f"            defense_plus={level_up.defense_plus},")
        writeline(file, f"            mg_attack_plus={level_up.mg_attack_plus},")
        writeline(file, f"            mg_defense_plus={level_up.mg_defense_plus},")
        writeline(file, f"            hp_plus_bonus={level_up.hp_plus_bonus},")
        writeline(file, f"            attack_plus_bonus={level_up.attack_plus_bonus},")
        writeline(file, f"            defense_plus_bonus={level_up.defense_plus_bonus},")
        writeline(file, f"            mg_attack_plus_bonus={level_up.mg_attack_plus_bonus},")
        writeline(file, f"            mg_defense_plus_bonus={level_up.mg_defense_plus_bonus},")
        writeline(file, f"        ),")
