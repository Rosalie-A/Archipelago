from django.core.management.base import BaseCommand
from randomizer.data import graphics_bowser as graphics
from randomizer.management.disassembler_common import (
    shortify,
    bit,
    dbyte,
    hbyte,
    named,
    con,
    byte,
    byte_int,
    short,
    short_int,
    build_table,
    use_table_name,
    get_flag_string,
    flags,
    con_int,
    flags_short,
    writeline,
    bit_bool_from_num,
)
from randomizer.helpers.npcmodeltables import sprite_name_table

import copy

removable_offsets = []

START = 0x280000
END = 0x330000
TOTAL_LENGTH = END - START

ANIM_PTR_START = 0x252000
ANIM_PTR_END = 0x252C00

PTR_START = 0x251800

insert_at_offsets = [
    # (0x31B960, 352), # Geno normal
    # (0x31E560, 226) # Geno attack
    # (0x3201A0, 363), # Mallow normal
    # (0x322F00, 139) # Mallow attack
    # (0x30FAC0, 303), # Peach normal
    # (0x3120A0, 225) # Peach attack
    # (0x313CC0, 445) # Bowser attack
    (0x31B9A0, 294)  # Bowser attack
]

# blank_starts = 0x32B460
blank_starts = 0x32F9A0

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

        parser.add_argument(
            "-d",
            "--debug",
            action="store_true",
            help="If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer",
        )

    def handle(self, *args, **options):

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        images = copy.deepcopy(graphics.images)

        offsets = list(set([image.graphics_pointer for image in graphics.images]))
        offsets.sort()
        print([hex(x) for x in offsets])

        gfx_data = bytearray([])
        ptr_bytes = bytearray([])

        available_space = END - blank_starts

        print(hex(available_space))

        for i, offset in enumerate(offsets):
            if i < len(offsets) - 1:
                next_offset = offsets[i + 1]
            else:
                next_offset = blank_starts

            for img_index, image in enumerate(images):
                if image.graphics_pointer == offset:
                    image.graphics_pointer = START + len(gfx_data)
                    images[img_index] = image

            gfx_data += rom[offset:next_offset]
            for gfx_offset, tile_offset in insert_at_offsets:
                if gfx_offset == offset:
                    inserting = min(available_space, (512 - tile_offset) * 0x20)
                    print(inserting)
                    if inserting > 0:
                        gfx_data += bytearray([0] * inserting)
                        available_space -= inserting
                    print(available_space)

        print(hex(len(gfx_data)))

        if len(gfx_data) < END - START:
            gfx_data += bytearray([0] * (END - START - len(gfx_data)))

        # f = open(f'write_to_0x280000.img', 'wb')
        # f.write(gfx_data)
        # f.close()

        for img_index, image in enumerate(images):
            bank = ((image.graphics_pointer - 0x280000) >> 16) & 0x0F
            gfx_short = image.graphics_pointer & 0xFFF0
            gfx_ptr = gfx_short + bank

            palette_ptr = (image.palette_pointer - 0x250000) & 0xFFFF

            ptr_bytes += bytearray(
                [
                    gfx_ptr & 0xFF,
                    (gfx_ptr & 0xFF00) >> 8,
                    palette_ptr & 0xFF,
                    (palette_ptr & 0xFF00) >> 8,
                ]
            )

        # f = open(f'write_to_0x251800.img', 'wb')
        # f.write(ptr_bytes)
        # f.close()

        used_anims = []

        for s in graphics.sprites:
            if s.animation_num not in used_anims:
                used_anims.append(s.animation_num)

        animation_ptrs = bytearray([])
        animation_bytes_1 = bytearray([])
        animation_bytes_2 = bytearray([])

        basic_anim_offset = 0x259000

        for i in range(0, (ANIM_PTR_END - ANIM_PTR_START) // 3):
            # if i > max(used_anims):
            if i > 460:
                break

            ptr_offset = ANIM_PTR_START + i * 3

            if i in used_anims:
                anim_offset = (
                    (rom[ptr_offset + 2] << 16)
                    + (rom[ptr_offset + 1] << 8)
                    + (rom[ptr_offset])
                ) - 0xC00000
                anim_length = rom[anim_offset] + (rom[anim_offset + 1] << 8)
                ib = rom[anim_offset : anim_offset + anim_length]
            else:
                ib = bytearray(
                    [
                        0x1F,
                        0x00,
                        0x0C,
                        0x00,
                        0x13,
                        0x00,
                        0x01,
                        0x01,
                        0x08,
                        0x00,
                        0x02,
                        0x00,
                        0x10,
                        0x00,
                        0x00,
                        0x00,
                        0x10,
                        0x00,
                        0x00,
                        0x17,
                        0x00,
                        0x00,
                        0x00,
                        0xF0,
                        0xF8,
                        0xF8,
                        0x01,
                        0x02,
                        0x03,
                        0x04,
                        0x00,
                    ]
                )
                anim_length = len(ib)

            if (
                basic_anim_offset + len(animation_bytes_1) + anim_length > START
                and basic_anim_offset != 0x360000
            ):
                basic_anim_offset = 0x360000

            if basic_anim_offset == 0x360000:
                new_anim_offset = basic_anim_offset + len(animation_bytes_2) + 0xC00000
                animation_bytes_2 += ib
            else:
                new_anim_offset = basic_anim_offset + len(animation_bytes_1) + 0xC00000
                animation_bytes_1 += ib

            animation_ptrs += bytearray(
                [
                    new_anim_offset & 0xFF,
                    (new_anim_offset >> 8) & 0xFF,
                    new_anim_offset >> 16,
                ]
            )

        animation_ptrs += bytearray(
            [0] * (ANIM_PTR_END - ANIM_PTR_START - len(animation_ptrs))
        )

        animation_bytes_1 += bytearray(
            [0] * (START - 0x259000 - len(animation_bytes_1))
        )

        animation_bytes_2 += bytearray(
            [0] * (0x370000 - 0x360000 - len(animation_bytes_2))
        )

        f = open(f"write_to_0x251800.img", "wb")
        f.write(ptr_bytes + animation_ptrs)
        f.close()

        f = open(f"write_to_0x259000.img", "wb")
        f.write(animation_bytes_1 + gfx_data)
        f.close()

        f = open(f"write_to_0x360000.img", "wb")
        f.write(animation_bytes_2)
        f.close()
