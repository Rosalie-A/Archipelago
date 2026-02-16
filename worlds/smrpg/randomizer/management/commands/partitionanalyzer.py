from django.core.management.base import BaseCommand
from randomizer.management.commands.output.disassembler_copy.event.events import scripts as eventscripts
from randomizer.management.commands.output.disassembler_copy.action.actions import scripts as actionscripts
from randomizer.management.commands.output.disassembler_copy.level.roomobjects import rooms as roomdata
from randomizer.management.commands.output.disassembler_copy.npcmodels import models as npcmodels
from randomizer.data.graphics import sprites, images, animations
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline, bit_bool_from_num
from randomizer.helpers.roomobjecttables import object_type, event_initiator, post_battle_behaviour, radial_direction_table, music_table, edge_table, exit_type_table, location_table, room_table, partition_space_table, partition_buffer_table
from randomizer.helpers.eventtables import Rooms
from randomizer.helpers.npcmodeltables import sprite_name_table

import xlsxwriter

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

        parser.add_argument('-d', '--debug', action="store_true",
                            help='If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer')

    def handle(self, *args, **options):

        workbook = xlsxwriter.Workbook("partitiondata_.xlsx")
        worksheet = workbook.add_worksheet()

        row = 0
        for col, item in enumerate(["room", "ally buffer", "ex. sprite buffer", "ex. buffer size", "A type", "A main space", "A main index", "B type", "B main space", "B main index", "C type", "C main space", "C main index", "full"]):
            worksheet.write(row, col, item)
        row += 1


        for room_index, room in enumerate(roomdata):
            if room is not None and room["partition"] is not None:
                partition = room["partition"]
                column = 0
                ind = use_table_name('Rooms', room_table, room_index)
                worksheet.write(row, column, ind.split(".")[1])
                column += 1
                worksheet.write(row, column, partition["ally_sprite_buffer_size"])
                column += 1
                worksheet.write(row, column, partition["allow_extra_sprite_buffer"])
                column += 1
                worksheet.write(row, column, partition["extra_sprite_buffer_size"] if partition["allow_extra_sprite_buffer"] else -1)
                column += 1
                for buffer in ["buffer_a", "buffer_b", "buffer_c"]:
                    typ, _ = byte(prefix="PartitionBufferTypes", table=partition_buffer_table)([partition[buffer]["type"]])
                    worksheet.write(row, column, typ.split(".")[1])
                    column += 1
                    typ, _ = byte(prefix="PartitionMainSpace", table=partition_space_table)([partition[buffer]["main_buffer_space"]])
                    worksheet.write(row, column, typ.split(".")[1])
                    column += 1
                    worksheet.write(row, column, partition[buffer]["index_in_main_buffer"])
                    column += 1
                worksheet.write(row, column, partition["full_palette_buffer"])
                column += 1


                for o in room["objects"]:
                    model_id = o["model"]
                    model_data = npcmodels[model_id]
                    sprite_id = model_data["sprite"]
                    dont_store_in_clone_buffer = model_data["cannot_clone"]
                    if sprite_id < 575:
                        sprite_name, _ = byte(prefix="SpriteName", table=sprite_name_table)([sprite_id])
                        sprite_data = sprites[sprite_id]
                        image_data = images[sprite_data.image_num]
                        animation_data = animations[sprite_data.animation_num]
                        vram_size = animation_data.properties.vram_size

                        fmt = "?"
                        default_mold = animation_data.properties.molds[0]
                        if not default_mold.gridplane:
                            fmt = "non-gridplane"
                        elif default_mold.tiles[0].format == 0:
                            fmt = "▫24h24w"
                        elif default_mold.tiles[0].format == 1:
                            fmt = "▯32h24w"
                        elif default_mold.tiles[0].format == 2:
                            fmt = "▭24h32w"
                        elif default_mold.tiles[0].format == 3:
                            fmt = "⬜32h32w"

                        item_string = "ID: %i\nSprite: %s\nFormat:%s\nVRAM:%i\nClones:%i\nExclude from clone buf:%r" % (model_id, sprite_name.split(".")[1], fmt, vram_size, len(o["clones"]), dont_store_in_clone_buffer)
                    else:
                        item_string = "ID: %i\nSprite: %i\nClones:%i\nExclude from clone buf:%r" % (model_id, sprite_id, len(o["clones"]), dont_store_in_clone_buffer)
                    worksheet.write(row, column, item_string)
                    
                    column += 1



                row += 1

        workbook.close()



