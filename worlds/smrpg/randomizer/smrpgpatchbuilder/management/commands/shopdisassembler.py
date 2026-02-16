"""Disassembler for shops.

This disassembler reads shop data from a Super Mario RPG ROM and outputs a Python file
containing all 33 shops with their items and settings.

Usage:
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py shopdisassembler --rom "/path/to/your/smrpg/rom"

This will produce:
    ./src/disassembler_output/shops/shops.py

Prerequisites:
    - Items must be disassembled first (itemdisassembler)
    - Variable names should be parsed (variableparser)

The output file will contain:
    - A shops array of size 33
    - Each shop assigned to its index using shop_names variables
"""

import os
import shutil
from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import writeline
from .input_file_parser import load_arrays_from_input_files, load_class_names_from_config
from smrpgpatchbuilder.datatypes.shops.classes import (
    SHOP_BASE_ADDRESS,
    TOTAL_SHOPS,
    ITEMS_PER_SHOP,
)

class Command(BaseCommand):
    help = "Disassembles shops from a ROM file"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom", required=True)

    def handle(self, *args, **options):
        # Load variable names and class names from disassembler output
        varnames = load_arrays_from_input_files()
        classnames = load_class_names_from_config()

        # Get shop names from variable output
        SHOP_NAMES = varnames.get("shops", [])

        # Get item class names
        ITEMS = classnames.get("all_items", [])

        # Load ROM
        rom = bytearray(open(options["rom"], "rb").read())

        # Create output directory
        output_path = "./src/disassembler_output/shops"
        shutil.rmtree(output_path, ignore_errors=True)
        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w").close()

        # Disassemble all shops
        shops_data = []
        for shop_id in range(TOTAL_SHOPS):
            shop_data = self.read_shop(rom, shop_id, ITEMS)
            shops_data.append(shop_data)

        # Generate the output file
        self.generate_output_file(output_path, shops_data, SHOP_NAMES)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully disassembled {len(shops_data)} shops to {output_path}/"
            )
        )

    def read_shop(self, rom, shop_id, items):
        """Read a single shop from ROM."""
        offset = SHOP_BASE_ADDRESS + (shop_id * 16)

        # Read flags byte
        flags_byte = rom[offset]
        offset += 1

        # Parse flags
        buy_frog_coin_one = (flags_byte & 0x01) == 0x01
        buy_frog_coin = (flags_byte & 0x02) == 0x02
        buy_only_a = (flags_byte & 0x04) == 0x04
        buy_only_b = (flags_byte & 0x08) == 0x08
        discount_6 = (flags_byte & 0x10) == 0x10
        discount_12 = (flags_byte & 0x20) == 0x20
        discount_25 = (flags_byte & 0x40) == 0x40
        discount_50 = (flags_byte & 0x80) == 0x80

        # Read items (15 bytes)
        shop_items = []
        for i in range(ITEMS_PER_SHOP):
            item_id = rom[offset + i]
            if item_id == 0xFF:
                shop_items.append(None)
            else:
                item_name = items[item_id] if item_id < len(items) else f"ITEM_{item_id}"
                shop_items.append(item_name)

        return {
            'id': shop_id,
            'items': shop_items,
            'buy_frog_coin_one': buy_frog_coin_one,
            'buy_frog_coin': buy_frog_coin,
            'buy_only_a': buy_only_a,
            'buy_only_b': buy_only_b,
            'discount_6': discount_6,
            'discount_12': discount_12,
            'discount_25': discount_25,
            'discount_50': discount_50,
        }

    def generate_output_file(self, output_path, shops_data, shop_names):
        """Generate the Python file with shop data."""
        file_path = f"{output_path}/shops.py"

        with open(file_path, "w") as f:
            # Write imports
            writeline(f, "from smrpgpatchbuilder.datatypes.shops.classes import Shop, ShopCollection")
            writeline(f, "from ..items.items import *")
            writeline(f, "from ..variables.shop_names import *")
            writeline(f, "")
            writeline(f, "")

            writeline(f, "shops: list[Shop] = [None] * 33 # type: ignore")

            # Generate shop definitions
            for shop in shops_data:
                self.write_shop(f, shop, shop_names)

            writeline(f, "")
            writeline(f, "# Shop Collection")
            writeline(f, "shop_collection = ShopCollection(shops)")

    def write_shop(self, f, shop, shop_names):
        """Write a shop definition to the file."""
        shop_id = shop['id']

        # Get shop name from shop_names array, or use generic name
        shop_name = shop_names[shop_id] if shop_id < len(shop_names) and shop_names[shop_id] else f"SHOP_{shop_id}"

        writeline(f, f"shops[{shop_name}] = Shop(")
        writeline(f, f"    index={shop_id},")

        # Write items list (only up to last non-None item)
        last_item_index = -1
        for i in range(len(shop['items']) - 1, -1, -1):
            if shop['items'][i] is not None:
                last_item_index = i
                break

        writeline(f, "    items=[")
        if last_item_index >= 0:
            for i in range(last_item_index + 1):
                item = shop['items'][i]
                if item is None:
                    writeline(f, "        None,")
                else:
                    writeline(f, f"        {item},")
        writeline(f, "    ],")

        # Write boolean flags (only if True)
        if shop['buy_frog_coin_one']:
            writeline(f, "    buy_frog_coin_one=True,")
        if shop['buy_frog_coin']:
            writeline(f, "    buy_frog_coin=True,")
        if shop['buy_only_a']:
            writeline(f, "    buy_only_a=True,")
        if shop['buy_only_b']:
            writeline(f, "    buy_only_b=True,")
        if shop['discount_6']:
            writeline(f, "    discount_6=True,")
        if shop['discount_12']:
            writeline(f, "    discount_12=True,")
        if shop['discount_25']:
            writeline(f, "    discount_25=True,")
        if shop['discount_50']:
            writeline(f, "    discount_50=True,")

        writeline(f, ")")
