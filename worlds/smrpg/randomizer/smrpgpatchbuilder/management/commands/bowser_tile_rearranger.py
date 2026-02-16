from django.core.management.base import BaseCommand
from randomizer.data import graphics_bowser as graphics
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline, bit_bool_from_num
from randomizer.helpers.npcmodeltables import sprite_name_table
from randomizer.logic.sprites import Sprites 

import copy

removable_offsets = []

START = 0x280000
END = 0x330000
TOTAL_LENGTH = END - START

ANIM_PTR_START = 0x252000
ANIM_PTR_END = 0x252C00

PTR_START = 0x251800

insert_at_offsets = [
    (0x313CC0, 445), # Bowser attack
    (0x317460, 294) # Bowser attack
]

class ReplacementTile:
    old_id = 0
    new_id = 0
    b = bytearray([])
    def __init__(self, old_id, new_id, b):
        self.old_id = old_id
        self.new_id = new_id
        self.b = b

blank_starts = 0x32B460

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

        parser.add_argument('-d', '--debug', action="store_true",
                            help='If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer')

    def handle(self, *args, **options):

        global rom
        rom = bytearray(open(options['rom'], 'rb').read())

        
        animations_to_consider = [254, 255, 256]
        animations = copy.deepcopy(graphics.animations)

        # 338, 339

        images = copy.deepcopy(graphics.images)
        sprites = copy.deepcopy(graphics.sprites)
        sprites[2].image_num = 338
        sprites[3].image_num = 339

        images[338].palette_pointer = 0x257dd0
        images[339].palette_pointer = 0x257dd0

        anim_subtiles = [None] * 3

        for ind, a_ in enumerate(animations_to_consider):
            a = animations[a_]
            anim_subtiles[ind] = []
            for m in a.properties.molds:
                for t in m.tiles:
                    if t.is_clone:
                        for t_ in t.tiles:
                            for s in t_.subtile_bytes:
                                if s > 0 and s not in anim_subtiles[ind]:
                                    anim_subtiles[ind].append(s)
                    else:
                        for s in t.subtile_bytes:
                            if s > 0 and s not in anim_subtiles[ind]:
                                anim_subtiles[ind].append(s)
            anim_subtiles[ind].sort()

        anim1_only = []
        anim1_and_anim2_only = []
        anim2_only = []
        anim1_and_anim3 = []
        anim2_and_anim3 = []
        anim3_only = []
        anim_all = []

        for i in range(1, 446):
            if i in anim_subtiles[0] and i not in anim_subtiles[1] and i not in anim_subtiles[2]:
                anim1_only.append(i)
            elif i in anim_subtiles[0] and i in anim_subtiles[1] and i not in anim_subtiles[2]:
                anim1_and_anim2_only.append(i)
            elif i not in anim_subtiles[0] and i in anim_subtiles[1] and i not in anim_subtiles[2]:
                anim2_only.append(i)
            elif i in anim_subtiles[0] and i not in anim_subtiles[1] and i in anim_subtiles[2]:
                anim1_and_anim3.append(i)
            elif i in anim_subtiles[0] and i in anim_subtiles[1] and i in anim_subtiles[2]:
                anim_all.append(i)
            elif i not in anim_subtiles[0] and i in anim_subtiles[1] and i in anim_subtiles[2]:
                anim2_and_anim3.append(i)
            elif i not in anim_subtiles[0] and i not in anim_subtiles[1] and i in anim_subtiles[2]:
                anim3_only.append(i)

        def replace_subtile(anim_index, old_ind, new_ind):
            for mold_index, a in enumerate(animations[anim_index].properties.molds):

                for tile_index, t in enumerate(a.tiles):
                    if t.is_clone:
                        for t_ind, t_ in enumerate(t.tiles):
                            before = ("before:",  mold_index, old_ind, new_ind, t_.subtile_bytes)
                            for s_ind, s in enumerate(t_.subtile_bytes):
                                if s == old_ind and not isinstance(s, str):
                                    animations[anim_index].properties.molds[mold_index].tiles[tile_index].tiles[t_ind].subtile_bytes[s_ind] = "%i" % new_ind
                                    # print(new_ind)
                    else:
                        before = ("before:",  mold_index, old_ind, new_ind, t.subtile_bytes)
                        for s_ind, s in enumerate(t.subtile_bytes):
                            if s == old_ind and not isinstance(s, str):
                                animations[anim_index].properties.molds[mold_index].tiles[tile_index].subtile_bytes[s_ind] = "%i" % new_ind
                                # print(new_ind)
                

        blank_at_start = 512 - (len(anim1_only) + len(anim1_and_anim2_only) + len(anim2_only) + len(anim1_and_anim3) + len(anim_all))

        output_gfx = bytearray([0] * blank_at_start * 0x20)

        anim1_index = blank_at_start
        anim2_index = 0
        anim3_index = 0

        bowser_gfx_offset = 0x313CC0

        anim1_offset = bowser_gfx_offset

        for ind, subt in enumerate(anim1_only):
            anim1_index += 1
            #print(anim1_index, subt)

            replace_subtile(254, subt, anim1_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        anim2_offset = bowser_gfx_offset + len(output_gfx)

        for ind, subt in enumerate(anim1_and_anim2_only):
            anim1_index += 1
            anim2_index += 1

            replace_subtile(254, subt, anim1_index)
            replace_subtile(255, subt, anim2_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        for ind, subt in enumerate(anim2_only):
            anim1_index += 1
            anim2_index += 1

            replace_subtile(255, subt, anim2_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        anim3_offset = bowser_gfx_offset + len(output_gfx)

        for ind, subt in enumerate(anim1_and_anim3):
            anim1_index += 1
            anim2_index += 1
            anim3_index += 1

            replace_subtile(254, subt, anim1_index)
            replace_subtile(256, subt, anim3_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        for ind, subt in enumerate(anim_all):
            anim1_index += 1
            anim2_index += 1
            anim3_index += 1

            replace_subtile(254, subt, anim1_index)
            replace_subtile(255, subt, anim2_index)
            replace_subtile(256, subt, anim3_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        for ind, subt in enumerate(anim2_and_anim3):
            anim1_index += 1
            anim2_index += 1
            anim3_index += 1

            replace_subtile(255, subt, anim2_index)
            replace_subtile(256, subt, anim3_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        for ind, subt in enumerate(anim3_only):
            anim1_index += 1
            anim2_index += 1
            anim3_index += 1

            replace_subtile(256, subt, anim3_index)

            gfx_offset = bowser_gfx_offset + 0x20 * (subt - 1)
            output_gfx += rom[gfx_offset:gfx_offset+0x20]

        delta = anim3_offset - anim1_offset
        included_in_anim3 = len(output_gfx) - delta
        fill = 512 * 0x20 - included_in_anim3

        output_gfx += bytearray([0] * fill)

        for a_id in animations_to_consider:
            for mold_index, mold in enumerate(animations[a_id].properties.molds):
                for tile_index, tile in enumerate(mold.tiles):
                    if tile.is_clone:
                        for c_index, c in enumerate(tile.tiles):
                            #if a_id == 254 and mold_index <= 1:
                                #print(c.subtile_bytes)
                            for b_index, b in enumerate(c.subtile_bytes):
                                val = int(animations[a_id].properties.molds[mold_index].tiles[tile_index].tiles[c_index].subtile_bytes[b_index])
                                animations[a_id].properties.molds[mold_index].tiles[tile_index].tiles[c_index].subtile_bytes[b_index] = int(animations[a_id].properties.molds[mold_index].tiles[tile_index].tiles[c_index].subtile_bytes[b_index])
                            if val > 255:
                                animations[a_id].properties.molds[mold_index].tiles[tile_index].tiles[c_index].format = 1
                        #print(animations[a_id].properties.molds[mold_index].tiles[tile_index].tiles[c_index].subtile_bytes)
                    else:
                        #if a_id == 254 and mold_index <= 1:
                            #print(tile.subtile_bytes)
                        for b_index, b in enumerate(tile.subtile_bytes):
                            val = int(animations[a_id].properties.molds[mold_index].tiles[tile_index].subtile_bytes[b_index])
                            animations[a_id].properties.molds[mold_index].tiles[tile_index].subtile_bytes[b_index] = int(animations[a_id].properties.molds[mold_index].tiles[tile_index].subtile_bytes[b_index])
                            if val > 255:
                                animations[a_id].properties.molds[mold_index].tiles[tile_index].format = 1

                    #print(animations[a_id].properties.molds[mold_index].tiles[tile_index].subtile_bytes)

        images[297].graphics_pointer = anim1_offset
        images[338].graphics_pointer = -1
        images[339].graphics_pointer = -1
        offsets = list(set([image.graphics_pointer for image in images]))
        offsets.sort()

        gfx_data = bytearray([])
        ptr_bytes = bytearray([])

        #print(len(offsets))
        #print(len(gfx_data))

        start_of_bowser_data = 0
        delta = 0

        for i, offset in enumerate(offsets):
            if offset == anim1_offset:
                pass
            elif i < len(offsets) - 1:
                next_offset = offsets[i + 1]
            else:
                next_offset = END

            print(hex(offset), hex(next_offset), hex(START + len(gfx_data)))
            if offset in [anim1_offset, anim2_offset, anim3_offset]:
                print("")

            for img_index, image in enumerate(images):
                if image.graphics_pointer == offset:
                    if offset in [anim1_offset, anim2_offset, anim3_offset]:
                        image.graphics_pointer = offset - delta
                    else:
                        image.graphics_pointer = START + len(gfx_data)
                    images[img_index] = image

            if offset == anim1_offset:
                gfx_data += output_gfx
            elif offset not in [anim2_offset, anim3_offset]:
                gfx_data += rom[offset:next_offset]

        gfx_data += bytearray([0] * (END - START - len(gfx_data)))

        
        images[338].graphics_pointer = anim2_offset
        images[339].graphics_pointer = anim3_offset

        sprite_data, image_data, animation_pointers, animation_data_bank_1, animation_data_bank_2 = Sprites.assemble_from_tables(sprites, images, animations)

        f = open(f'write_to_0x250000.img', 'wb')
        f.write(sprite_data)
        f.close() 

        f = open(f'write_to_0x251800.img', 'wb')
        f.write(image_data + animation_pointers)
        f.close()

        
        f = open(f'write_to_0x259000.img', 'wb')
        f.write(animation_data_bank_1 + gfx_data)
        f.close()

        
        f = open(f'write_to_0x360000.img', 'wb')
        f.write(animation_data_bank_2)
        f.close()

