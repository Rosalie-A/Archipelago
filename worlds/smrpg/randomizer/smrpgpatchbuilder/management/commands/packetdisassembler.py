from django.core.management.base import BaseCommand
import shutil
import os

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, **options):
        dest = "./src/disassembler_output/packets/"
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest, exist_ok=True)
        open(f"{dest}/__init__.py", "w")

        rom = bytearray(open(options["rom"], "rb").read())

        # Read packet names from config
        packet_names = []
        with open("./config/packet_names.input", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    packet_names.append(line)

        # Pad to 256 if needed
        while len(packet_names) < 256:
            packet_names.append(f"P{len(packet_names):03d}_UNUSED")

        # Read sprite names from config
        sprite_names = []
        with open("./config/sprite_names.input", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    sprite_names.append(line)

        # Read action script names from config
        action_script_names = []
        with open("./config/action_script_names.input", "r") as f:
            for line in f:
                line = line.strip()
                if line:
                    action_script_names.append(line)

        # Read packet data from ROM (256 packets, 5 bytes each)
        base_addr = 0x1DB000
        packets = []

        for packet_index in range(256):
            addr = base_addr + (packet_index * 5)
            packet_bytes = rom[addr:addr + 5]

            # Check if this is an empty packet (all 0xFF)
            if all(b == 0xFF for b in packet_bytes):
                packets.append(None)
            else:
                # Parse the 5-byte packet structure
                byte0 = packet_bytes[0]
                byte1 = packet_bytes[1]
                byte2 = packet_bytes[2]
                byte3 = packet_bytes[3]
                byte4 = packet_bytes[4]

                # Decode sprite_id from byte0
                sprite_id = ((byte0 & 0x3F) + 0xC0)
                unknown_byte_0 = (byte0 >> 6)

                # Decode from byte1
                unknown_byte_1 = (byte1 & 0x07)
                unknown_byte_2 = ((byte1 >> 3) & 0x03)
                unknown_byte_3 = ((byte1 >> 5) & 0x07)

                # Decode from byte2
                unknown_byte_4 = (byte2 & 0x03)
                unknown_bit_0 = bool((byte2 >> 2) & 0x01)
                unknown_bit_1 = bool((byte2 >> 3) & 0x01)
                unknown_bit_2 = bool((byte2 >> 4) & 0x01)
                shadow = bool((byte2 >> 5) & 0x01)
                unknown_byte_5 = ((byte2 >> 6) & 0x03)

                # Decode action_script_id from byte3 and byte4
                action_script_id = byte3 | ((byte4 & 0x03) << 8)
                unknown_byte_6 = ((byte4 >> 4) & 0x0F)

                packet_data = {
                    'index': packet_index,
                    'name': packet_names[packet_index],
                    'sprite_id': sprite_id,
                    'shadow': shadow,
                    'action_script_id': action_script_id,
                    'unknown_bits': [unknown_bit_0, unknown_bit_1, unknown_bit_2],
                    'unknown_bytes': [
                        unknown_byte_0, unknown_byte_1, unknown_byte_2,
                        unknown_byte_3, unknown_byte_4, unknown_byte_5, unknown_byte_6
                    ],
                }

                packets.append(packet_data)

        # Write packets to file
        file = open(f"{dest}/packets.py", "wb")

        file.write("from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.packet import Packet, PacketCollection\n".encode("utf8"))
        file.write("from ..variables.sprite_names import *\n".encode("utf8"))
        file.write("from ..variables.action_script_names import *\n".encode("utf8"))
        file.write("\n\n".encode("utf8"))

        # Generate packet instances
        for i, packet_data in enumerate(packets):
            packet_name = packet_names[i]

            if packet_data is None:
                file.write(f"{packet_name} = None\n".encode("utf8"))
            else:
                # Get sprite and action script names
                sprite_id = packet_data['sprite_id']
                action_id = packet_data['action_script_id']

                sprite_name = sprite_names[sprite_id] if sprite_id < len(sprite_names) else f"{sprite_id}"
                action_name = action_script_names[action_id] if action_id < len(action_script_names) else f"{action_id}"

                file.write(f"{packet_name} = Packet(\n".encode("utf8"))
                file.write(f"    packet_id={packet_data['index']},\n".encode("utf8"))
                file.write(f"    sprite_id={sprite_name},\n".encode("utf8"))
                file.write(f"    shadow={packet_data['shadow']},\n".encode("utf8"))
                file.write(f"    action_script_id={action_name},\n".encode("utf8"))

                # Always write unknown_bits
                bits_str = str(packet_data['unknown_bits'])
                file.write(f"    unknown_bits={bits_str},\n".encode("utf8"))

                # Always write unknown_bytes
                bytes_str = "bytearray([" + ", ".join(f"0x{b:02X}" for b in packet_data['unknown_bytes']) + "])"
                file.write(f"    unknown_bytes={bytes_str},\n".encode("utf8"))

                file.write(")\n".encode("utf8"))

            file.write("\n".encode("utf8"))

        # Create packet collection
        file.write("\n# Packet Collection\n".encode("utf8"))
        file.write("ALL_PACKETS = PacketCollection([\n".encode("utf8"))
        for packet_name in packet_names:
            file.write(f"    {packet_name},\n".encode("utf8"))
        file.write("])\n".encode("utf8"))

        file.close()

        # Generate __init__.py with all packet imports
        init_file = open(f"{dest}/__init__.py", "wb")
        init_file.write("# AUTOGENERATED DO NOT EDIT!!\n".encode("utf8"))
        init_file.write("# This file imports all packet instances from packets.py\n".encode("utf8"))
        init_file.write("\n".encode("utf8"))
        init_file.write("from .packets import (\n".encode("utf8"))
        for packet_name in packet_names:
            init_file.write(f"    {packet_name},\n".encode("utf8"))
        init_file.write("    ALL_PACKETS,\n".encode("utf8"))
        init_file.write(")\n".encode("utf8"))
        init_file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled packet data to ./src/disassembler_output/packets/"
            )
        )
        self.stdout.write(
            self.style.SUCCESS(f"Successfully generated __init__.py with {len(packet_names)} packet imports")
        )
