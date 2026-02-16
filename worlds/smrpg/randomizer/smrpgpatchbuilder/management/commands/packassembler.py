"""Assembler for formation packs.

This assembler reads the PackCollection from disassembler output and renders it
to create ROM patches for formation pack data.

Usage:
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packassembler --rom "/path/to/your/smrpg/rom"
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packassembler --text
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packassembler --bin

Options:
    -r, --rom: Path to a Mario RPG ROM to create a BPS patch
    -t, --text: Output assembled bytes as plain text files
    -b, --bin: Output assembled bytes as FlexHEX-compatible img files

Output locations:
    - BPS patches: ./src/assembler_output/packs/bps/
    - Text files: ./src/assembler_output/packs/txt/
    - Binary files: ./src/assembler_output/packs/bin/
"""

import os
import shutil
from django.core.management.base import BaseCommand
from copy import deepcopy
import importlib
from bps.diff import diff_bytearrays
from bps.io import write_bps
from bps.util import bps_progress
from datetime import datetime

class Command(BaseCommand):
    help = "Assemble formation packs from disassembler output and generate ROM patches"

    def add_arguments(self, parser):
        parser.add_argument(
            "-t",
            "--text",
            action="store_true",
            dest="text",
            help="Use -t if you want to output your assembled bytes as plain text files.",
        )
        parser.add_argument(
            "-b",
            "--bin",
            action="store_true",
            dest="bin",
            help="Use -b if you want to output your assembled bytes as FlexHEX-compatible img files.",
        )
        parser.add_argument(
            "-r",
            "--rom",
            dest="rom",
            help="Specify a path to a Mario RPG ROM if you want to output your assembled bytes as a BPS patch.",
        )

    def handle(self, *args, **options):
        module_path = "disassembler_output.packs.pack_collection"

        outputToText = options["text"] or False
        outputToBin = options["bin"] or False
        romPath = options["rom"]
        outputToPatch = romPath is not None

        if not (outputToText or outputToBin or outputToPatch):
            self.stderr.write(
                self.style.ERROR(
                    "You need to specify at least one output format. Options are --text, --bin, --rom"
                )
            )
            exit(1)

        if outputToText:
            shutil.rmtree("./src/assembler_output/packs/txt", ignore_errors=True)
            os.makedirs("./src/assembler_output/packs/txt", exist_ok=True)
        if outputToBin:
            shutil.rmtree("./src/assembler_output/packs/bin", ignore_errors=True)
            os.makedirs("./src/assembler_output/packs/bin", exist_ok=True)
        if outputToPatch:
            os.makedirs("./src/assembler_output/packs/bps", exist_ok=True)

        rom = bytearray()
        if outputToPatch:
            original_rom = bytearray(open(romPath, "rb").read())
            rom = deepcopy(original_rom)

        # Import the packs module and get the PackCollection
        try:
            module = importlib.import_module(module_path)
        except ImportError as e:
            self.stderr.write(
                self.style.ERROR(
                    f"Could not import {module_path}. Make sure you've run packdisassembler first. Error: {e}"
                )
            )
            exit(1)

        try:
            collection = module.pack_collection
        except AttributeError:
            self.stderr.write(
                self.style.ERROR(
                    f"Could not find 'pack_collection' in {module_path}. Make sure you've run packdisassembler first."
                )
            )
            exit(1)

        # Render the collection to get the patch data
        try:
            patch_data = collection.render()
        except ValueError as e:
            error_msg = str(e)
            if "Too many unique formations" in error_msg:
                self.stderr.write(
                    self.style.ERROR(
                        f"\n{error_msg}\n\n"
                        "The game can only support 512 unique formations total.\n"
                        "To fix this:\n"
                        "  1. Review your pack_collection.py and look for duplicate formations\n"
                        "  2. Reuse identical formations across packs instead of creating new ones\n"
                        "  3. Consider if some formations can be made identical by adjusting enemy positions\n"
                    )
                )
            else:
                self.stderr.write(self.style.ERROR(f"Error rendering packs: {e}"))
            exit(1)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Unexpected error rendering packs: {e}"))
            exit(1)

        if patch_data:
            for start, bytes_ in patch_data.items():
                if outputToBin:
                    with open(
                        f"./src/assembler_output/packs/bin/write_to_0x{start:06X}.img",
                        "wb",
                    ) as f:
                        f.write(bytes_)
                if outputToText:
                    with open(
                        f"./src/assembler_output/packs/txt/write_to_0x{start:06X}.txt",
                        "w",
                    ) as f:
                        f.write(" ".join([f"{b:02X}" for b in bytes_]))
                if outputToPatch:
                    end = start + len(bytes_)
                    if end > len(rom):
                        raise ValueError(
                            f"Change at {start:#X} exceeds file size (end = {end:#X})"
                        )
                    rom[start:end] = bytes_

            if outputToPatch:
                blocksize = (len(original_rom) + len(rom)) // 1000000 + 1
                iterable = diff_bytearrays(blocksize, bytes(original_rom), bytes(rom))
                with open(
                    f'./src/assembler_output/packs/bps/smrpg-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps',
                    "wb",
                ) as f:
                    write_bps(bps_progress(iterable), f)

                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully created BPS patch at ./src/assembler_output/packs/bps/"
                    )
                )

            if outputToText:
                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully created text files at ./src/assembler_output/packs/txt/"
                    )
                )

            if outputToBin:
                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully created binary files at ./src/assembler_output/packs/bin/"
                    )
                )
        else:
            self.stdout.write(
                self.style.WARNING("No patch data generated. PackCollection may be empty.")
            )
