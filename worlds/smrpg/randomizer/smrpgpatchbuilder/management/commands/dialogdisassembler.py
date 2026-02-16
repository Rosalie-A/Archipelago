from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import shortify
from smrpgpatchbuilder.datatypes.dialogs.utils import decompress, COMPRESSION_TABLE
import shutil
import os

banks = [
    {
        "id": 0x22,
        "start": 0x220000,
        "end": 0x22FD17,
        "table_size": 0x08,
        "pointers": {"start": 0x37E000, "end": 0x37EFFF},
    },
    {
        "id": 0x23,
        "start": 0x230000,
        "end": 0x23F2D4,
        "table_size": 0x04,
        "pointers": {"start": 0x37F000, "end": 0x37F7FF},
    },
    {
        "id": 0x24,
        "start": 0x240000,
        "end": 0x248FFF,
        "table_size": 0x04,
        "pointers": {"start": 0x37F800, "end": 0x37FFFF},
    },
]

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def handle(self, *args, **options):

        dest = "./src/disassembler_output/dialogs/"
        shutil.rmtree(dest, ignore_errors=True)
        os.makedirs(dest, exist_ok=True)
        os.makedirs(f"{dest}/contents", exist_ok=True)
        os.makedirs(f"{dest}/variables", exist_ok=True)
        open(f"{dest}/__init__.py", "w")
        open(f"{dest}/contents/__init__.py", "w")
        open(f"{dest}/variables/__init__.py", "w")

        # Read dialog names from config
        dialog_names = []
        if os.path.exists("./config/dialog_names.input"):
            with open("./config/dialog_names.input", "r") as f:
                for line in f:
                    line = line.strip()
                    if line:
                        dialog_names.append(line)

        # Pad to 4096 if needed
        while len(dialog_names) < 4096:
            dialog_names.append(f"DIALOG_{len(dialog_names):04X}")

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        # Read compression table from ROM first
        # Pointer table is 256 bytes (0x249000-0x249100)
        # String data starts at 0x249100
        compression_table = []
        comp_ptrs = rom[0x249000:0x249100]  # Read full 256-byte pointer table

        # Only process first 12 pointers (many are unused)
        comp_offsets = []
        for i in range(0, 24, 2):  # 12 pointers = 24 bytes
            comp_offsets.append(0x249100 + comp_ptrs[i] + ((comp_ptrs[i + 1]) << 8))

        for index, offset in enumerate(comp_offsets):
            word = ""
            while True:
                # Don't read past 0x249149
                if offset > 0x249149 or rom[offset] == 0x00:
                    break
                b = rom[offset]
                s = chr(b)
                for tb in COMPRESSION_TABLE:
                    if bytes([b]) == tb[1]:
                        s = tb[0]
                        break
                word += s
                offset += 1
            byte = f"{(14+index):02x}"

            byte_string = bytearray.fromhex(byte)
            compression_table.append((word, byte_string))

        pointers = []
        pointers_relative = []

        # get # of pointers
        for bank in banks:
            bank_id = bank["id"]
            ptrstart = bank["pointers"]["start"]
            ptrend = bank["pointers"]["end"]
            tblsize = bank["table_size"]
            start = bank["start"]
            end = bank["end"]

            bank_pointers = []

            # get pointers
            for i in range(0, (ptrend - ptrstart + 1) // 2):
                if i >= 0x600:
                    pointer = (
                        (bank_id << 16)
                        + shortify(rom, start + 6)
                        + (shortify(rom, ptrstart + i * 2))
                    )
                elif i >= 0x400:
                    pointer = (
                        (bank_id << 16)
                        + shortify(rom, start + 4)
                        + (shortify(rom, ptrstart + i * 2))
                    )
                elif i >= 0x200:
                    pointer = (
                        (bank_id << 16)
                        + shortify(rom, start + 2)
                        + (shortify(rom, ptrstart + i * 2))
                    )
                else:
                    pointer = (
                        (bank_id << 16)
                        + shortify(rom, start)
                        + (shortify(rom, ptrstart + i * 2))
                    )
                if pointer > end:
                    pointer = bank_pointers[i - 1]
                bank_pointers.append(pointer)
            pointers += bank_pointers

        # will store info about positions in each string that the pointers are intended to point to
        # so that changing the strings can make sure the pointers are still going to the right place in the dialog data
        pointers_relative = [None] * len(pointers)

        for bank in banks:
            raw_data = []
            bank_id = bank["id"]

            file = open("%s/contents/dialog_table_0x%02x.py" % (dest, bank_id), "wb")

            ptrstart = bank["pointers"]["start"]
            ptrend = bank["pointers"]["end"]
            tblsize = bank["table_size"]
            start = bank["start"]
            end = bank["end"]

            def note_pointer(cursor, string):
                if cursor in pointers:
                    indices = [i for i, x in enumerate(pointers) if x == cursor]
                    for match_pointer_index in indices:
                        pointers_relative[match_pointer_index] = {
                            "bank": bank_id,
                            "index": len(raw_data),
                            "pos": len(string),
                        }  # only thing to be careful about here is that "position" may be confusing when referencing decompressed dialog

            # get dialog data
            cursor = start + tblsize
            string = bytearray([])
            while cursor <= end:
                note_pointer(cursor, string)
                string.append(rom[cursor])
                if rom[cursor] in [0x1C, 0x0B, 0x0D]:
                    cursor += 1
                    note_pointer(cursor, string)
                    string.append(rom[cursor])
                elif rom[cursor] in [
                    0x00,
                    0x06,
                ]:  # do not terminate if they immediately follow 1c, 0b, or 0d
                    raw_data.append(string)
                    string = bytearray([])
                cursor += 1
            if len(string) > 0:
                raw_data.append(string)

            file.write(("dialog_data = [\"\"]*%i\n" % len(raw_data)).encode("utf8"))

            for i in range(len(raw_data)):
                s = decompress(raw_data[i], COMPRESSION_TABLE + compression_table)
                file.write(("dialog_data[%i] = '''%s'''\n" % (i, s)).encode("utf8"))
                # why do the pointers reset at 0x400???

            file.close()

        # Write dialog names to variables file
        file = open("%s/variables/dialog_names.py" % dest, "wb")
        for i, name in enumerate(dialog_names):
            file.write(f"{name} = {i}\n".encode("utf8"))
        file.close()

        file = open("%s/contents/dialog_pointers.py" % dest, "wb")
        file.write(
            "from smrpgpatchbuilder.datatypes.dialogs.classes import Dialog\n".encode(
                "utf8"
            )
        )
        file.write("from ..variables.dialog_names import *\n".encode("utf8"))
        file.write(("pointers: list[Dialog] = [None]*%i # type: ignore\n" % len(pointers_relative)).encode("utf8"))
        for i in range(len(pointers_relative)):
            ptr = pointers_relative[i]
            if ptr is not None:
                dialog_name = dialog_names[i]
                file.write(
                    (
                        "pointers[%s] = Dialog(bank=0x%02x, index=%i, pos=%i)\n"
                        % (dialog_name, ptr["bank"], ptr["index"], ptr["pos"])
                    ).encode("utf8")
                )
        file.close()

        # Write compression table to file
        file = open("%s/contents/compression_table.py" % dest, "wb")
        file.write("compression_table = [\n".encode("utf8"))
        for word, byte_val in compression_table:
            file.write(f"    ({repr(word)}, {repr(byte_val)}),\n".encode("utf8"))
        file.write("]\n\n".encode("utf8"))

        # Save the original ROM compression table bytes for reference/debugging
        original_comp_table_bytes = rom[0x249000:0x24914A]
        file.write(f"# Original ROM compression table bytes (0x249000-0x249149):\n".encode("utf8"))
        file.write(f"# {original_comp_table_bytes.hex()}\n".encode("utf8"))
        file.write(f"original_compression_table_size = {len(original_comp_table_bytes)}\n".encode("utf8"))
        file.close()

        file = open("%s/dialogs.py" % dest, "wb")
        file.write(
            "from smrpgpatchbuilder.datatypes.dialogs.classes import DialogCollection\n".encode(
                "utf8"
            )
        )
        file.write("from .contents.dialog_pointers import pointers\n".encode("utf8"))
        file.write("from .contents.compression_table import compression_table\n".encode("utf8"))

        args = []
        for index, bank in enumerate(banks):
            file.write(
                f"from .contents.dialog_table_0x{bank["id"]:02x} import dialog_data as data_{index}\n".encode(
                    "utf8"
                )
            )
            args.append(f"data_{index}")
        file.write(
            f"\ndata = DialogCollection(pointers, [{", ".join(args)}], compression_table=compression_table)".encode(
                "utf8"
            )
        )
        file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled dialog data to ./src/disassembler_output/dialogs/"
            )
        )
