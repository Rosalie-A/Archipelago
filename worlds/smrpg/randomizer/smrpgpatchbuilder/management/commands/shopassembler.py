"""Assembler for shops.

This assembler reads the ShopCollection from disassembler output and renders it
to create ROM patches for shop data.

Usage:
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py shopassembler --rom "/path/to/your/smrpg/rom"
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py shopassembler --text
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py shopassembler --bin

Options:
    -r, --rom: Path to a Mario RPG ROM to create a BPS patch
    -t, --text: Output assembled bytes as plain text files
    -b, --bin: Output assembled bytes as FlexHEX-compatible img files

Output locations:
    - BPS patches: ./src/assembler_output/shops/bps/
    - Text files: ./src/assembler_output/shops/txt/
    - Binary files: ./src/assembler_output/shops/bin/
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
    help = "Assemble shops from disassembler output and generate ROM patches"

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
        module_path = "disassembler_output.shops.shops"

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
            shutil.rmtree("./src/assembler_output/shops/txt", ignore_errors=True)
            os.makedirs("./src/assembler_output/shops/txt", exist_ok=True)
        if outputToBin:
            shutil.rmtree("./src/assembler_output/shops/bin", ignore_errors=True)
            os.makedirs("./src/assembler_output/shops/bin", exist_ok=True)
        if outputToPatch:
            os.makedirs("./src/assembler_output/shops/bps", exist_ok=True)

        rom = bytearray()
        if outputToPatch:
            original_rom = bytearray(open(romPath, "rb").read())
            rom = deepcopy(original_rom)

        # Import the shops module and get the ShopCollection
        try:
            module = importlib.import_module(module_path)
        except ImportError as e:
            self.stderr.write(
                self.style.ERROR(
                    f"Could not import {module_path}. Make sure you've run shopdisassembler first. Error: {e}"
                )
            )
            exit(1)

        try:
            collection = module.shop_collection
        except AttributeError:
            self.stderr.write(
                self.style.ERROR(
                    f"Could not find 'shop_collection' in {module_path}. Make sure you've run shopdisassembler first."
                )
            )
            exit(1)

        # Render the collection to get the patch data
        try:
            patch_data = collection.render()
        except ValueError as e:
            self.stderr.write(self.style.ERROR(f"Error rendering shops: {e}"))
            exit(1)
        except Exception as e:
            self.stderr.write(self.style.ERROR(f"Unexpected error rendering shops: {e}"))
            exit(1)

        if patch_data:
            for start, bytes_ in patch_data.items():
                if outputToBin:
                    with open(
                        f"./src/assembler_output/shops/bin/write_to_0x{start:06X}.img",
                        "wb",
                    ) as f:
                        f.write(bytes_)
                if outputToText:
                    with open(
                        f"./src/assembler_output/shops/txt/write_to_0x{start:06X}.txt",
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
                    f'./src/assembler_output/shops/bps/smrpg-{datetime.now().strftime("%Y%m%d%H%M%S")}.bps',
                    "wb",
                ) as f:
                    write_bps(bps_progress(iterable), f)

                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully created BPS patch at ./src/assembler_output/shops/bps/"
                    )
                )

            if outputToText:
                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully created text files at ./src/assembler_output/shops/txt/"
                    )
                )

            if outputToBin:
                self.stdout.write(
                    self.style.SUCCESS(
                        "Successfully created binary files at ./src/assembler_output/shops/bin/"
                    )
                )
        else:
            self.stdout.write(
                self.style.WARNING("No patch data generated. ShopCollection may be empty.")
            )
