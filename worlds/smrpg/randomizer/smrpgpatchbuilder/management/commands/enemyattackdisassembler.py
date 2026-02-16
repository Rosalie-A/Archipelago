from django.core.management.base import BaseCommand
from smrpgpatchbuilder.datatypes.enemy_attacks.constants import (
    ENEMY_ATTACK_BASE_ADDRESS,
    ENEMY_ATTACK_NAME_ADDRESS,
    ENEMY_ATTACK_NAME_LENGTH,
)
from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix
from smrpgpatchbuilder.datatypes.spells.enums import Status, TempStatBuff
import shutil
import os

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, **options):
        dest = "./src/disassembler_output/enemy_attacks/"
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest, exist_ok=True)
        open(f"{dest}/__init__.py", "w")

        rom = bytearray(open(options["rom"], "rb").read())

        attacks = []

        for attack_index in range(129):
            # Read attack stats (4 bytes per attack)
            base_addr = ENEMY_ATTACK_BASE_ADDRESS + (attack_index * 4)

            byte0 = rom[base_addr]
            attack_level = byte0 & 0x07  # bits 0-2
            ohko = bool(byte0 & 0x08)  # bit 3
            damageless_flag_1 = bool(byte0 & 0x10)  # bit 4
            hide_numbers = bool(byte0 & 0x20)  # bit 5
            damageless_flag_2 = bool(byte0 & 0x40)  # bit 6

            hit_rate = rom[base_addr + 1]
            status_byte = rom[base_addr + 2]
            buffs_byte = rom[base_addr + 3]

            # Parse status effects
            status_effects = []
            for status in Status:
                if hasattr(status, 'spell_value'):
                    bit = status.spell_value
                    if status_byte & (1 << bit):
                        status_effects.append(status)

            # Parse buffs
            buffs = []
            for buff_val in range(8):
                if buffs_byte & (1 << buff_val):
                    try:
                        buffs.append(TempStatBuff(buff_val))
                    except ValueError:
                        pass

            # Read attack name (13 bytes)
            name_addr = ENEMY_ATTACK_NAME_ADDRESS + (attack_index * ENEMY_ATTACK_NAME_LENGTH)
            name_bytes = rom[name_addr:name_addr + ENEMY_ATTACK_NAME_LENGTH]

            # Parse prefix and name
            first_byte = name_bytes[0]
            prefix = None
            start_idx = 0

            # Known prefix values
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
                attack_name = bytes(name_chars).decode('latin-1')
                # Replace \x9c with &
                attack_name = attack_name.replace('\x9c', '&')
            except:
                attack_name = ""

            attack_data = {
                'index': attack_index,
                'name': attack_name,
                'prefix': prefix,
                'attack_level': attack_level,
                'ohko': ohko,
                'damageless_flag_1': damageless_flag_1,
                'hide_numbers': hide_numbers,
                'damageless_flag_2': damageless_flag_2,
                'hit_rate': hit_rate,
                'status_effects': status_effects,
                'buffs': buffs,
            }

            attacks.append(attack_data)

        # Write attacks to file
        file = open(f"{dest}/attacks.py", "wb")

        file.write("from smrpgpatchbuilder.datatypes.enemy_attacks.classes import EnemyAttack, EnemyAttackCollection\n".encode("utf8"))
        file.write("from smrpgpatchbuilder.datatypes.spells.enums import Status, TempStatBuff\n".encode("utf8"))
        file.write("from smrpgpatchbuilder.datatypes.items.enums import ItemPrefix\n".encode("utf8"))
        file.write("\n\n".encode("utf8"))

        # First pass: count name occurrences to detect duplicates
        name_counts = {}
        name_occurrence = {}  # Track which occurrence number this is for duplicates
        for attack_data in attacks:
            if attack_data['name']:
                # Strip special characters
                base_name = attack_data['name'].replace(" ", "").replace("'", "").replace("!", "").replace("-", "").replace(".", "").replace("&", "")
                name_counts[base_name] = name_counts.get(base_name, 0) + 1

        # Second pass: generate attack classes
        attack_class_names = []  # Store the class names for later use

        for attack_data in attacks:
            # Determine class name
            if attack_data['name']:
                # Use the attack name, strip special characters
                base_name = attack_data['name'].replace(" ", "").replace("'", "").replace("!", "").replace("-", "").replace(".", "").replace("&", "")

                # Track which occurrence this is (1st, 2nd, 3rd, etc.)
                if base_name not in name_occurrence:
                    name_occurrence[base_name] = 1
                else:
                    name_occurrence[base_name] += 1

                # If this name appears more than once, append the occurrence number
                if name_counts[base_name] > 1:
                    class_name = f"{base_name}Attack{name_occurrence[base_name]}"
                else:
                    class_name = f"{base_name}Attack"
            else:
                # Blank name - use Attack{ID}
                class_name = f"Attack{attack_data['index']}"

            # Store the class name
            attack_class_names.append(class_name)

            file.write(f"class {class_name}(EnemyAttack):\n".encode("utf8"))
            file.write(f"    _index = {attack_data['index']}\n".encode("utf8"))

            if attack_data['name']:
                file.write(f"    _name = {repr(attack_data['name'])}\n".encode("utf8"))

            if attack_data['prefix']:
                file.write(f"    _prefix = ItemPrefix.{attack_data['prefix'].name}\n".encode("utf8"))

            file.write(f"    _attack_level = {attack_data['attack_level']}\n".encode("utf8"))
            file.write(f"    _ohko = {attack_data['ohko']}\n".encode("utf8"))
            file.write(f"    _damageless_flag_1 = {attack_data['damageless_flag_1']}\n".encode("utf8"))
            file.write(f"    _hide_numbers = {attack_data['hide_numbers']}\n".encode("utf8"))
            file.write(f"    _damageless_flag_2 = {attack_data['damageless_flag_2']}\n".encode("utf8"))
            file.write(f"    _hit_rate = {attack_data['hit_rate']}\n".encode("utf8"))

            if attack_data['status_effects']:
                status_list = ", ".join([f"Status.{s._name_}" for s in attack_data['status_effects']])
                file.write(f"    _status_effects = [{status_list}]\n".encode("utf8"))

            if attack_data['buffs']:
                buffs_list = ", ".join([f"TempStatBuff({b})" for b in attack_data['buffs']])
                file.write(f"    _buffs = [{buffs_list}]\n".encode("utf8"))

            file.write("\n\n".encode("utf8"))

        # Write the collection instantiation
        file.write("\n".encode("utf8"))
        file.write("collection = EnemyAttackCollection([\n".encode("utf8"))
        for class_name in attack_class_names:
            file.write(f"    {class_name}(),\n".encode("utf8"))
        file.write("])\n".encode("utf8"))

        file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled enemy attack data to ./src/disassembler_output/enemy_attacks/"
            )
        )
