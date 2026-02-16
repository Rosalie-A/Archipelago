import os
import shutil
from django.core.management.base import BaseCommand
from copy import deepcopy
import importlib
from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress
from datetime import datetime
from smrpgpatchbuilder.datatypes.battles.battle_dialog_collection import (
    BattleDialogCollection,
)

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-t", "--text", action='store_true', dest="text", help="use -t if you want to output your assembled bytes as plain text files.")
        parser.add_argument("-b", "--bin", action='store_true', dest="bin", help="use -b if you want to output your assembled bytes as flexhex-compatible img files.")
        parser.add_argument("-r", "--rom", dest="rom", help="specify a path to a mario rpg rom if you want to output your assembled bytes as a bps patch.")

    def handle(self, *args, **options):
        module_path = "disassembler_output.battle_dialogs.battle_dialogs"

        outputToText = options["text"] or False
        outputToBin = options["bin"] or False
        romPath = options["rom"]
        outputToPatch = romPath is not None

        if not (outputToText or outputToBin or outputToPatch):
            print("you need to specify at least one output format. options are --text, --bin, --rom")
            exit(1)

        if outputToText:
            shutil.rmtree("./src/assembler_output/battle_dialogs/txt", ignore_errors=True)
            os.makedirs("./src/assembler_output/battle_dialogs/txt", exist_ok=True)
        if outputToBin:
            shutil.rmtree("./src/assembler_output/battle_dialogs/bin", ignore_errors=True)
            os.makedirs("./src/assembler_output/battle_dialogs/bin", exist_ok=True)
        if outputToPatch:
            os.makedirs("./src/assembler_output/battle_dialogs/bps", exist_ok=True)

        rom = bytearray()
        if outputToPatch:
            original_rom = bytearray(open(romPath, "rb").read())
            rom = deepcopy(original_rom)

        # Import the BattleDialogCollection from Python module
        module = importlib.import_module(module_path)
        collection_obj = module.collection

        # Render to get patch data
        collection = collection_obj.render()

        if collection:
            for start, bytes_ in collection.items():
                if outputToBin:
                    with open(f'./src/assembler_output/battle_dialogs/bin/write_to_0x{start:06X}.img', 'wb') as f:
                        f.write(bytes_)
                if outputToText:
                    with open(f'./src/assembler_output/battle_dialogs/txt/write_to_0x{start:06X}.txt', 'w') as f:
                        f.write(" ".join([f'{b:02X}' for b in bytes_]))
                if outputToPatch:
                    end = start + len(bytes_)
                    if end > len(rom):
                        raise ValueError(f"change at {start:#X} exceeds file size (end = {end:#X})")
                    rom[start:end] = bytes_

            if outputToPatch:
                blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
                iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
                with open(f'./src/assembler_output/battle_dialogs/bps/smrpg-battledialogs-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps', 'wb') as f:
                    write_bps(bps_progress(iterable), f)

        self.stdout.write(self.style.SUCCESS("successfully assembled battle dialog data"))
