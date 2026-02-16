from django.core.management.base import BaseCommand
from smrpgpatchbuilder.datatypes.dialogs.utils import decompress, COMPRESSION_TABLE
from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import (
    BATTLE_DIALOG_POINTER_ADDRESS,
    BATTLE_DIALOG_DATA_START,
    BATTLE_DIALOG_DATA_END,
    BATTLE_MESSAGE_POINTER_ADDRESS,
    BATTLE_MESSAGE_DATA_START,
    BATTLE_MESSAGE_DATA_END,
)
import shutil
import os

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):

        dest = "./src/disassembler_output/battle_dialogs/"
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest, exist_ok=True)
        open(f"{dest}/__init__.py", "w")

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        # Read compression table from dialog system
        # Battle dialogs use the same compression as psychopath messages
        # which is entries from byte 0x22 onward (index 17) plus battle-specific codes
        battle_compression_table = [
            ("\n", bytearray(b"\x01")),
            ("[await]", bytearray(b"\x02")),
            ("[pause]", bytearray(b"\x03")),
            ("[delay]", bytearray(b"\x0C"))
        ] + [
            (text, bytearray(byte_val)) for text, byte_val in COMPRESSION_TABLE[17:]
        ]

        # Read pointer table (256 pointers, 2 bytes each = 512 bytes)
        pointer_table_bytes = rom[BATTLE_DIALOG_POINTER_ADDRESS:BATTLE_DIALOG_POINTER_ADDRESS + 512]

        battle_dialogs = []

        # Process each of the 256 battle dialog pointers
        for i in range(256):
            # Get the pointer (little-endian 16-bit)
            ptr_offset = i * 2
            pointer = pointer_table_bytes[ptr_offset] + (pointer_table_bytes[ptr_offset + 1] << 8)

            # Calculate absolute address
            # Pointers are relative to bank 0x39, so add bank base
            absolute_addr = 0x390000 + pointer

            # Read message bytes until we hit 0x00 terminator (exclude the 0x00)
            message_bytes = bytearray()
            cursor = absolute_addr
            while cursor <= BATTLE_DIALOG_DATA_END:
                byte = rom[cursor]
                if byte == 0x00:
                    break
                message_bytes.append(byte)
                cursor += 1

            # Decompress the message
            if len(message_bytes) > 0:
                message = decompress(message_bytes, battle_compression_table)
            else:
                message = ""

            battle_dialogs.append(message)

        # Read battle messages (46 entries)
        # Calculate number of pointers: (0x3A274C - 0x3A26F1 + 1) / 2 = 46
        pointer_table_size = BATTLE_MESSAGE_POINTER_ADDRESS + 92  # 46 pointers * 2 bytes
        message_pointer_bytes = rom[BATTLE_MESSAGE_POINTER_ADDRESS:pointer_table_size]

        battle_messages = []

        for i in range(46):
            # Get the pointer (little-endian 16-bit)
            ptr_offset = i * 2
            pointer = message_pointer_bytes[ptr_offset] + (message_pointer_bytes[ptr_offset + 1] << 8)

            # Calculate absolute address (pointers are relative to bank 0x3A)
            absolute_addr = 0x3A0000 + pointer

            # Read message bytes until we hit 0x00 terminator (exclude the 0x00)
            message_bytes = bytearray()
            cursor = absolute_addr
            while cursor <= BATTLE_MESSAGE_DATA_END:
                byte = rom[cursor]
                if byte == 0x00:
                    break
                message_bytes.append(byte)
                cursor += 1

            # Decompress the message
            if len(message_bytes) > 0:
                message = decompress(message_bytes, battle_compression_table)
            else:
                message = ""

            battle_messages.append(message)

        # Write BattleDialogCollection to Python file
        file = open(f"{dest}/battle_dialogs.py", "wb")
        file.write(b"from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import BattleDialogCollection\n\n")

        # Write battle_dialogs list
        file.write(f"battle_dialogs = [\"\"]*{len(battle_dialogs)}\n".encode("utf8"))
        for i, message in enumerate(battle_dialogs):
            file.write(f"battle_dialogs[{i}] = {repr(message)}\n".encode("utf8"))
        file.write(b"\n")

        # Write battle_messages list
        file.write(f"battle_messages = [\"\"]*{len(battle_messages)}\n".encode("utf8"))
        for i, message in enumerate(battle_messages):
            file.write(f"battle_messages[{i}] = {repr(message)}\n".encode("utf8"))
        file.write(b"\n")

        # Create the collection object
        file.write(b"collection = BattleDialogCollection(\n")
        file.write(b"    battle_dialogs=battle_dialogs,\n")
        file.write(b"    battle_messages=battle_messages,\n")
        file.write(b")\n")
        file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled battle dialog data to ./src/disassembler_output/battle_dialogs/"
            )
        )
