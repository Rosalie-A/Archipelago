from django.core.management.base import BaseCommand
from randomizer.data import graphics_openmode, graphics_vanilla
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline, bit_bool_from_num
from randomizer.helpers.npcmodeltables import sprite_name_table


import xlsxwriter

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

        parser.add_argument('-d', '--debug', action="store_true",
                            help='If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer')

    def handle(self, *args, **options):

        workbook = xlsxwriter.Workbook("offsetdata.xlsx")
        worksheet = workbook.add_worksheet()

        row = 0
        worksheet.write(row, 0, "Offset")
        worksheet.write(row, 1, "Vanilla")
        worksheet.write(row, 2, "Openmode")
        row += 1

        offsets = list(set([image.graphics_pointer for image in graphics_vanilla.images] + [image.graphics_pointer for image in graphics_openmode.images]))
        offsets.sort()

        for offset in offsets:

            worksheet.write(row, 0, hex(offset))

            vanilla_image_pack_ids = [image_pack.index for image_pack in graphics_vanilla.images if image_pack.graphics_pointer == offset]
            rando_image_pack_ids = [image_pack.index for image_pack in graphics_openmode.images if image_pack.graphics_pointer == offset]

            vanilla_sprite_ids = []
            rando_sprite_ids = []
            for id in vanilla_image_pack_ids:
                sprite_ids_for_this_image_pack = [sprite.index for sprite in graphics_vanilla.sprites if sprite.image_num == id]
                vanilla_sprite_ids += sprite_ids_for_this_image_pack
            for id in rando_image_pack_ids:
                sprite_ids_for_this_image_pack = [sprite.index for sprite in graphics_openmode.sprites if sprite.image_num == id]
                rando_sprite_ids += sprite_ids_for_this_image_pack
            vanilla_sprite_ids = list(set(vanilla_sprite_ids))
            rando_sprite_ids = list(set(rando_sprite_ids))

            vanilla_sprite_names = [byte(prefix="SpriteName", table=sprite_name_table)([sprite_id])[0] for sprite_id in vanilla_sprite_ids]
            rando_sprite_names = [byte(prefix="SpriteName", table=sprite_name_table)([sprite_id])[0] for sprite_id in rando_sprite_ids]

            if len(vanilla_sprite_names) > 0:
                worksheet.write(row, 1, "\n".join(vanilla_sprite_names))
            else:
                worksheet.write(row, 1, "unused")
            if len(rando_sprite_names) > 0:
                worksheet.write(row, 2, "\n".join(rando_sprite_names))
            else:
                worksheet.write(row, 2, "unused")



            row += 1

        workbook.close()



