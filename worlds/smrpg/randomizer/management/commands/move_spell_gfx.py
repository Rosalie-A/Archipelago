from django.core.management.base import BaseCommand
from randomizer.data import graphics_bowser as graphics
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline, bit_bool_from_num
from randomizer.helpers.npcmodeltables import sprite_name_table

import copy

class AnimationBank:
    start = 0
    end = 0
    tiles = bytearray([])

    @property
    def remaining_space(self):
        return self.end - self.start - len(self.tiles)

    @property
    def current_offset(self):
        return self.start + len(self.tiles)

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.tiles = bytearray([])


class Effect:
    index = 0
    image_bytes = bytearray([])
    used_by = []
    offset = 0

    def __init__(self):
        self.index = 0
        self.image_bytes = bytearray([])
        self.used_by = []
        self.offset = 0

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

        parser.add_argument('-d', '--debug', action="store_true",
                            help='If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer')

    def handle(self, *args, **options):

        effects = []

        animation_banks = [
            AnimationBank(0x330000, 0x340000),
            AnimationBank(0x340000, 0x350000)
        ]

        def place_bytes(these_bytes):
            if len(these_bytes) <= animation_banks[1].remaining_space:
                offset = animation_banks[1].current_offset
                animation_banks[1].tiles += these_bytes
            else:
                offset = animation_banks[0].end - len(animation_banks[0].tiles) - len(these_bytes)
                animation_banks[0].tiles = these_bytes + animation_banks[0].tiles
            print(hex(offset))
            return offset

        global rom
        rom = bytearray(open(options['rom'], 'rb').read())

        index_bytes = rom[0x251000:0x251800]

        for index in range(0, 128):
            animation_id = index_bytes[index * 4 + 1] & 0xFF
            # print("")
            # print(index)
            # print(animation_id)
            ptr_offset = 0x252C00 + animation_id * 3
            image_data_pointer = (rom[ptr_offset] & 0xFF) + ((rom[ptr_offset+1] & 0xFF) << 8) + ((rom[ptr_offset+2] & 0xFF) << 16) - 0xC00000
            # print(hex(ptr_offset))
            # print(rom[ptr_offset], rom[ptr_offset+1], rom[ptr_offset+2])
            # print(hex(image_data_pointer))
            data_length = (rom[image_data_pointer] & 0xFF) + ((rom[image_data_pointer+1] & 0xFF) << 8)

            image_data = rom[image_data_pointer:image_data_pointer+data_length]

            dupe = None
            for e_i, e in enumerate(effects):
                if image_data == e.image_bytes:
                    dupe = e_i
                    break
            if dupe is not None:
                e = effects[dupe]
                e.used_by.append(index)
                effects[dupe] = e
            else:
                e = Effect()
                e.image_bytes = image_data
                e.used_by = [index]
                e.index = len(effects)
                effects.append(e)


        output_image_data = bytearray([])
        output_pointer_data = bytearray([])

        effects.sort(key=lambda x: len(x.image_bytes), reverse=True)

        for e_index, e in enumerate(effects):
            for spell in e.used_by:
                index_bytes[spell * 4 + 1] = (e.index & 0xFF)

            output_ptr = place_bytes(e.image_bytes)
            effects[e_index].offset = output_ptr
            
        effects.sort(key=lambda x: x.index)

        for e_index, e in enumerate(effects):
            output_ptr = e.offset + 0xC00000
            output_pointer_data += bytearray([(output_ptr & 0xFF), ((output_ptr >> 8) & 0xFF), ((output_ptr >> 16) & 0xFF)])
            

        animation_banks[1].tiles += bytearray([0] * (animation_banks[1].end - animation_banks[1].start - len(animation_banks[1].tiles)))
        buffer = 0x20 - (len(animation_banks[0].tiles) % 0x20)
        animation_banks[0].tiles = bytearray([0] * buffer) + animation_banks[0].tiles

        output_pointer_data += bytearray([0] * (0x253000 - 0x252C00 - len(output_pointer_data)))
        #output_image_data = bytearray([0] * (anim_data_offset - 0x330000)) + output_image_data
        #output_image_data += bytearray([0] * (0x350000 - 0x330000 - len(output_image_data)))
        for b in animation_banks:
            output_image_data += b.tiles
        data_starts_at = 0x350000 - len(output_image_data)
        output_image_data = bytearray([0] * (data_starts_at - 0x330000)) + output_image_data

        
        f = open(f'write_to_0x251000.img', 'wb')
        f.write(index_bytes)
        f.close()

        
        f = open(f'write_to_0x252C00.img', 'wb')
        f.write(output_pointer_data)
        f.close()

        
        f = open(f'write_to_0x330000.img', 'wb')
        f.write(output_image_data)
        f.close()


# This needs to be improved
# Make sure no data is overflowing from 0x33FFFF into 0x340000
# What to do: Have 2 banks (one of any size, one of exactly 0x10000 bytes)
# Sort effects list from longest to shortest byte set
# Try to assign bytes into the 2nd bank. If they dont fit, assign them to the 1st
# That way we will fit in as many as possible

# Do this also for NPC sprite data assembler.
# The concept will be to assign sprites into whichever bank has the most remaining space.
        


