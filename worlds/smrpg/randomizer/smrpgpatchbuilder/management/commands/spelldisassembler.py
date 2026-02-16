from django.core.management.base import BaseCommand
from smrpgpatchbuilder.datatypes.spells.ids.misc import (
    SPELL_BASE_ADDRESS,
    SPELL_BASE_NAME_ADDRESS,
    SPELL_BASE_DESC_POINTER_ADDRESS,
    SPELL_BASE_DESC_DATA_START,
    SPELL_BASE_DESC_DATA_END,
    SPELL_TIMING_MODIFIERS_BASE_ADDRESS,
    SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS,
)
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.items.encoding import decode_item_description
from smrpgpatchbuilder.datatypes.spells.enums import (
    SpellType,
    EffectType,
    Element,
    Status,
    InflictFunction,
    TempStatBuff,
)
from smrpgpatchbuilder.datatypes.spells.arguments import timing_properties, damage_modifiers
import shutil
import os

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, **options):
        dest = "./src/disassembler_output/spells/"
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest, exist_ok=True)
        open(f"{dest}/__init__.py", "w")

        rom = bytearray(open(options["rom"], "rb").read())

        # Build lookup dictionaries for timing and damage modifier constants
        timing_lookup = {}
        for name in dir(timing_properties):
            if not name.startswith('_'):
                obj = getattr(timing_properties, name)
                if hasattr(obj, '__class__') and obj.__class__.__name__ == 'TimingProperties':
                    timing_lookup[int(obj)] = name

        damage_lookup = {}
        for name in dir(damage_modifiers):
            if not name.startswith('_'):
                obj = getattr(damage_modifiers, name)
                if hasattr(obj, '__class__') and obj.__class__.__name__ == 'DamageModifiers':
                    damage_lookup[int(obj)] = name

        # There are 128 spell slots (0-127)
        # Indices 0-26 are character spells, the rest are enemy spells

        spells = []

        for spell_index in range(128):
            # Read spell stats (12 bytes per spell)
            base_addr = SPELL_BASE_ADDRESS + (spell_index * 12)

            byte0 = rom[base_addr]
            check_stats = bool(byte0 & 0x01)
            ignore_defense = bool(byte0 & 0x02)
            check_ohko = bool(byte0 & 0x20)
            usable_outside_of_battle = bool(byte0 & 0x80)

            byte1 = rom[base_addr + 1]
            spell_type_val = byte1 & 0x01
            effect_type_val = byte1 & 0x06
            quad9s = bool(byte1 & 0x08)

            fp = rom[base_addr + 2]

            byte3 = rom[base_addr + 3]
            target_others = bool(byte3 & 0x02)
            target_enemies = bool(byte3 & 0x04)
            target_party = bool(byte3 & 0x10)
            target_wounded = bool(byte3 & 0x20)
            target_one_party = bool(byte3 & 0x40)
            target_not_self = bool(byte3 & 0x80)

            element_byte = rom[base_addr + 4]
            power = rom[base_addr + 5]
            hit_rate = rom[base_addr + 6]

            status_byte = rom[base_addr + 7]
            boosts_byte = rom[base_addr + 8]

            inflict_byte = rom[base_addr + 10]
            byte11 = rom[base_addr + 11]
            hide_num = bool(byte11 & 0x04)

            # Parse spell type
            spell_type = SpellType.DAMAGE if spell_type_val == 0 else SpellType.HEAL

            # Parse effect type
            effect_type = None
            if effect_type_val == 0x02:
                effect_type = EffectType.INFLICT
            elif effect_type_val == 0x04:
                effect_type = EffectType.NULLIFY

            # Parse element
            element = None
            for elem in Element:
                if hasattr(elem, 'spell_value') and elem.spell_value == element_byte:
                    element = elem
                    break

            # Parse inflict function
            # 0xFF means no inflict function, 0 is InflictFunction.SCAN
            inflict = None
            if inflict_byte == 0xFF:
                inflict = None
            else:
                for inf in InflictFunction:
                    if inf.value == inflict_byte:
                        inflict = inf
                        break

            # Parse status effects
            status_effects = []
            for status in Status:
                if hasattr(status, 'spell_value'):
                    bit = status.spell_value
                    if status_byte & (1 << bit):
                        status_effects.append(status)

            # Parse boosts
            boosts = []
            for boost_val in range(8):
                if boosts_byte & (1 << boost_val):
                    try:
                        boosts.append(TempStatBuff(boost_val))
                    except ValueError:
                        pass

            # Read spell name (15 bytes)
            name_addr = SPELL_BASE_NAME_ADDRESS + (spell_index * 15)
            name_bytes = rom[name_addr:name_addr + 15]

            # Parse prefix and name (same pattern as items)
            first_byte = name_bytes[0]
            prefix = None
            start_idx = 0

            # Known prefix values (from ItemPrefix enum, especially STAR = 0x40 for character spells)
            known_prefixes = {0x7F, 0x22, 0x28, 0x23, 0x21, 0x29, 0x25, 0x27, 0x26, 0x3C, 0x3D, 0x2D, 0x2E, 0x3B, 0x3F, 0x40}

            if first_byte in known_prefixes:
                try:
                    prefix = ItemPrefix(first_byte)
                    start_idx = 1
                except ValueError:
                    pass

            # Extract the name portion and strip trailing spaces (0x20)
            name_chars = list(name_bytes[start_idx:])
            while name_chars and name_chars[-1] == 0x20:
                name_chars.pop()

            # Convert to string (latin-1 encoding)
            try:
                title = bytes(name_chars).decode('latin-1')
            except:
                title = ""

            # Determine if this is a character spell (indices 0-26) or enemy spell
            is_character_spell = spell_index < 27

            spell_data = {
                'index': spell_index,
                'is_character': is_character_spell,
                'title': title,
                'prefix': prefix,
                'fp': fp,
                'power': power,
                'hit_rate': hit_rate,
                'spell_type': spell_type,
                'effect_type': effect_type,
                'element': element,
                'inflict': inflict,
                'check_stats': check_stats,
                'ignore_defense': ignore_defense,
                'check_ohko': check_ohko,
                'usable_outside_of_battle': usable_outside_of_battle,
                'quad9s': quad9s,
                'hide_num': hide_num,
                'target_others': target_others,
                'target_enemies': target_enemies,
                'target_party': target_party,
                'target_wounded': target_wounded,
                'target_one_party': target_one_party,
                'target_not_self': target_not_self,
                'status_effects': status_effects,
                'boosts': boosts,
            }

            # For character spells, read timing and damage modifiers
            if is_character_spell:
                timing_addr = SPELL_TIMING_MODIFIERS_BASE_ADDRESS + (spell_index * 2)
                timing_val = rom[timing_addr] + (rom[timing_addr + 1] << 8)
                spell_data['timing_modifiers'] = timing_val

                damage_addr = SPELL_DAMAGE_MODIFIERS_BASE_ADDRESS + (spell_index * 2)
                damage_val = rom[damage_addr] + (rom[damage_addr + 1] << 8)
                spell_data['damage_modifiers'] = damage_val

            spells.append(spell_data)

        # Read character spell descriptions (27 descriptions)
        desc_pointers = []
        for i in range(27):
            ptr_addr = SPELL_BASE_DESC_POINTER_ADDRESS + (i * 2)
            pointer = rom[ptr_addr] + (rom[ptr_addr + 1] << 8)
            # Pointer is relative to bank 0x3A
            absolute_addr = 0x3A0000 + pointer
            desc_pointers.append(absolute_addr)

        # Read description data
        descriptions = []
        for i in range(27):
            start_addr = desc_pointers[i]
            # Read until null terminator
            desc_bytes = bytearray()
            cursor = start_addr
            while cursor <= SPELL_BASE_DESC_DATA_END:
                byte = rom[cursor]
                if byte == 0x00:
                    break
                desc_bytes.append(byte)
                cursor += 1

            # Decode description
            desc = decode_item_description(desc_bytes) if len(desc_bytes) > 0 else ""
            descriptions.append(desc)

        # Write spells to file
        file = open(f"{dest}/spells.py", "wb")

        file.write("from smrpgpatchbuilder.datatypes.spells.classes import CharacterSpell, EnemySpell, SpellCollection\n".encode("utf8"))
        file.write("from smrpgpatchbuilder.datatypes.spells.enums import SpellType, EffectType, Element, Status, InflictFunction, TempStatBuff\n".encode("utf8"))
        file.write("from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix\n".encode("utf8"))
        file.write("from smrpgpatchbuilder.datatypes.spells.arguments.types.classes import TimingProperties, DamageModifiers\n".encode("utf8"))

        # Write imports for timing and damage constants if needed
        used_timing_constants = set()
        used_damage_constants = set()
        for spell_data in spells:
            if spell_data['is_character']:
                if spell_data['timing_modifiers'] in timing_lookup:
                    used_timing_constants.add(timing_lookup[spell_data['timing_modifiers']])
                if spell_data['damage_modifiers'] in damage_lookup:
                    used_damage_constants.add(damage_lookup[spell_data['damage_modifiers']])

        if used_timing_constants:
            timing_imports = ", ".join(sorted(used_timing_constants))
            file.write(f"from smrpgpatchbuilder.datatypes.spells.arguments.timing_properties import {timing_imports}\n".encode("utf8"))

        if used_damage_constants:
            damage_imports = ", ".join(sorted(used_damage_constants))
            file.write(f"from smrpgpatchbuilder.datatypes.spells.arguments.damage_modifiers import {damage_imports}\n".encode("utf8"))

        file.write("\n\n".encode("utf8"))

        # First pass: count name occurrences to detect duplicates
        name_counts = {}
        name_occurrence = {}  # Track which occurrence number this is for duplicates
        for spell_data in spells:
            if spell_data['title']:
                # Strip special characters
                base_name = spell_data['title'].replace(" ", "").replace("'", "").replace("!", "").replace("-", "").replace(".", "")
                name_counts[base_name] = name_counts.get(base_name, 0) + 1

        # Second pass: generate spell classes
        spell_class_names = []  # Store the class names for later use

        for spell_data in spells:
            # Determine class name
            if spell_data['title']:
                # Use the spell title, strip special characters
                base_name = spell_data['title'].replace(" ", "").replace("'", "").replace("!", "").replace("-", "").replace(".", "")

                # Track which occurrence this is (1st, 2nd, 3rd, etc.)
                if base_name not in name_occurrence:
                    name_occurrence[base_name] = 1
                else:
                    name_occurrence[base_name] += 1

                # If this name appears more than once, append the occurrence number
                if name_counts[base_name] > 1:
                    class_name = f"{base_name}Spell{name_occurrence[base_name]}"
                else:
                    class_name = f"{base_name}Spell"
            else:
                # Blank title - use Spell{ID}
                class_name = f"Spell{spell_data['index']}"

            base_class = "CharacterSpell" if spell_data['is_character'] else "EnemySpell"

            # Store the class name for later use in the collection
            spell_class_names.append(class_name)

            file.write(f"class {class_name}({base_class}):\n".encode("utf8"))
            file.write(f"    _index = {spell_data['index']}\n".encode("utf8"))
            file.write(f"    _title = {repr(spell_data['title'])}\n".encode("utf8"))

            if spell_data['prefix']:
                file.write(f"    _prefix = ItemPrefix.{spell_data['prefix'].name}\n".encode("utf8"))

            file.write(f"    _fp = {spell_data['fp']}\n".encode("utf8"))
            file.write(f"    _power = {spell_data['power']}\n".encode("utf8"))
            file.write(f"    _hit_rate = {spell_data['hit_rate']}\n".encode("utf8"))
            file.write(f"    _spell_type = SpellType.{spell_data['spell_type'].name}\n".encode("utf8"))

            if spell_data['effect_type']:
                file.write(f"    _effect_type = EffectType.{spell_data['effect_type'].name}\n".encode("utf8"))

            if spell_data['element']:
                file.write(f"    _element = Element.{spell_data['element']._name_}\n".encode("utf8"))

            if spell_data['inflict'] is not None:
                file.write(f"    _inflict = InflictFunction.{spell_data['inflict'].name}\n".encode("utf8"))

            file.write(f"    _check_stats = {spell_data['check_stats']}\n".encode("utf8"))
            file.write(f"    _ignore_defense = {spell_data['ignore_defense']}\n".encode("utf8"))
            file.write(f"    _check_ohko = {spell_data['check_ohko']}\n".encode("utf8"))
            file.write(f"    _usable_outside_of_battle = {spell_data['usable_outside_of_battle']}\n".encode("utf8"))
            file.write(f"    _quad9s = {spell_data['quad9s']}\n".encode("utf8"))
            file.write(f"    _hide_num = {spell_data['hide_num']}\n".encode("utf8"))
            file.write(f"    _target_others = {spell_data['target_others']}\n".encode("utf8"))
            file.write(f"    _target_enemies = {spell_data['target_enemies']}\n".encode("utf8"))
            file.write(f"    _target_party = {spell_data['target_party']}\n".encode("utf8"))
            file.write(f"    _target_wounded = {spell_data['target_wounded']}\n".encode("utf8"))
            file.write(f"    _target_one_party = {spell_data['target_one_party']}\n".encode("utf8"))
            file.write(f"    _target_not_self = {spell_data['target_not_self']}\n".encode("utf8"))

            if spell_data['status_effects']:
                status_list = ", ".join([f"Status.{s._name_}" for s in spell_data['status_effects']])
                file.write(f"    _status_effects = [{status_list}]\n".encode("utf8"))

            if spell_data['boosts']:
                boosts_list = ", ".join([f"TempStatBuff({b})" for b in spell_data['boosts']])
                file.write(f"    _boosts = [{boosts_list}]\n".encode("utf8"))

            # Add character spell specific properties
            if spell_data['is_character']:
                # Use constant name if available, otherwise use hex value
                timing_val = spell_data['timing_modifiers']
                if timing_val in timing_lookup:
                    file.write(f"    _timing_modifiers = {timing_lookup[timing_val]}\n".encode("utf8"))
                else:
                    file.write(f"    _timing_modifiers = TimingProperties(0x{timing_val:04X})\n".encode("utf8"))

                damage_val = spell_data['damage_modifiers']
                if damage_val in damage_lookup:
                    file.write(f"    _damage_modifiers = {damage_lookup[damage_val]}\n".encode("utf8"))
                else:
                    file.write(f"    _damage_modifiers = DamageModifiers(0x{damage_val:04X})\n".encode("utf8"))

                # Add description
                if spell_data['index'] < len(descriptions):
                    file.write(f"    _description = {repr(descriptions[spell_data['index']])}\n".encode("utf8"))

            file.write("\n\n".encode("utf8"))

        # Create spell collection
        file.write("ALL_SPELLS = SpellCollection([\n".encode("utf8"))
        for class_name in spell_class_names:
            file.write(f"    {class_name}(),\n".encode("utf8"))
        file.write("])\n".encode("utf8"))

        file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled spell data to ./src/disassembler_output/spells/"
            )
        )
