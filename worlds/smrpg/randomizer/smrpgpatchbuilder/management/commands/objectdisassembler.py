from django.core.management.base import BaseCommand
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
from randomizer.helpers.roomobjecttables import (
    object_type,
    event_initiator,
    post_battle_behaviour,
    radial_direction_table,
    music_table,
    edge_table,
    exit_type_table,
    location_table,
    room_table,
    partition_space_table,
    partition_buffer_table,
)

start = 0x148400
end = 0x14FFFF
ptrstart = 0x148000
ptrend = 0x1483FF

roomevent_start = 0x20E400
roomevent_end = 0x20FFFF  # might be 0x20fdc7
roomevent_ptrstart = 0x20E000
roomevent_ptrend = 0x20E3FF

roomexit_start = 0x1D3166
roomexit_end = 0x1D4904
roomexit_ptrstart = 0x1D2D64
roomexit_ptrend = 0x1D3165

partitionstart = 0x1DDE00
partitionend = 0x1DDFFF  # bumped up from 0x1ddfdf

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
        debug = options["debug"]

        dest = "randomizer/data/roomobjects"
        if debug:
            dest = "randomizer/management/commands/output/disassembler/level"

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        rooms_raw_data = []
        roomevent_raw_data = []
        roomexit_raw_data = []
        partitions = []

        ptrs = []
        roomevent_ptrs = []
        roomexit_ptrs = []
        for i in range(partitionstart, partitionend, 4):
            partition_data = rom[i : i + 4]
            partition = {}
            partition["allow_extra_sprite_buffer"] = partition_data[0] & 0x10 == 0x10
            partition["full_palette_buffer"] = partition_data[0] & 0x80 == 0x80
            partition["ally_sprite_buffer_size"] = (partition_data[0] & 0x60) >> 5
            partition["extra_sprite_buffer_size"] = partition_data[0] & 0x0F
            partition["clone_buffer_a_type"] = partition_data[1] & 0x07
            partition["clone_buffer_a_space"] = (partition_data[1] & 0x70) >> 4
            partition["clone_buffer_a_index_in_main"] = partition_data[1] & 0x80 == 0x80
            partition["clone_buffer_b_type"] = partition_data[2] & 0x07
            partition["clone_buffer_b_space"] = (partition_data[2] & 0x70) >> 4
            partition["clone_buffer_b_index_in_main"] = partition_data[2] & 0x80 == 0x80
            partition["clone_buffer_c_type"] = partition_data[3] & 0x07
            partition["clone_buffer_c_space"] = (partition_data[3] & 0x70) >> 4
            partition["clone_buffer_c_index_in_main"] = partition_data[3] & 0x80 == 0x80
            partitions.append(partition)

        for i in range(ptrstart, ptrend, 2):
            ptrs.append((0x14 << 16) | (shortify(rom, i)))
        for i in range(roomevent_ptrstart, roomevent_ptrend, 2):
            roomevent_ptrs.append((0x20 << 16) | (shortify(rom, i)))
        for i in range(roomexit_ptrstart, roomexit_ptrend, 2):
            roomexit_ptrs.append((0x1D << 16) | (shortify(rom, i)))
        lengths = []
        roomevent_lengths = []
        roomexit_lengths = []

        # get raw data per room
        for i in range(len(ptrs)):
            if i < len(ptrs) - 1:
                lengths.append(ptrs[i + 1] - ptrs[i])
                rooms_raw_data.append(rom[ptrs[i] : ptrs[i + 1]])
                print(i, hex(ptrs[i]), ptrs[i + 1] - ptrs[i])
            else:
                lengths.append(end - ptrs[i])
                rooms_raw_data.append(rom[ptrs[i] : end])
        for i in range(len(roomevent_ptrs)):
            if i < len(roomevent_ptrs) - 1:
                roomevent_lengths.append(roomevent_ptrs[i + 1] - roomevent_ptrs[i])
                roomevent_raw_data.append(
                    rom[roomevent_ptrs[i] : roomevent_ptrs[i + 1]]
                )
            else:
                roomevent_lengths.append(roomevent_ptrend - roomevent_ptrs[i])
                roomevent_raw_data.append(rom[roomevent_ptrs[i] : roomevent_ptrend])
        for i in range(len(roomexit_ptrs)):
            if i < len(roomexit_ptrs) - 1:
                roomexit_lengths.append(roomexit_ptrs[i + 1] - roomexit_ptrs[i])
                roomexit_raw_data.append(rom[roomexit_ptrs[i] : roomexit_ptrs[i + 1]])
            else:
                roomexit_lengths.append(roomexit_end - roomexit_ptrs[i])
                roomexit_raw_data.append(rom[roomexit_ptrs[i] : roomexit_end])

        if len(rooms_raw_data) < 511:
            raise Exception(
                "npc pointer table had %i entries (needs at least 509)"
                % len(rooms_raw_data)
            )
        if len(roomevent_raw_data) < 511:
            raise Exception(
                "event tile pointer table had %i entries (needs at least 509)"
                % len(roomexit_raw_data)
            )
        if len(roomexit_raw_data) < 511:
            raise Exception(
                "exit field pointer table had %i entries (needs at least 509)"
                % len(roomexit_raw_data)
            )

        for i in range(len(rooms_raw_data)):
            d = rooms_raw_data[i]
            r = roomevent_raw_data[i]
            e = roomexit_raw_data[i]
            if i <= 511:
                if i > 509:
                    d = []
                    e = []

                file = open("%s/room_%i.py" % (dest, i), "w")
                writeline(file, "# AUTOGENERATED DO NOT EDIT!!")
                writeline(
                    file, "# Run the following command if you need to rebuild the table"
                )
                writeline(file, "# python manage.py objectdisassembler --rom ROM")
                writeline(
                    file,
                    "from randomizer.helpers.roomobjecttables import ObjectType, Initiator, PostBattle, RadialDirection, Music, Edge, ExitType, Locations, Rooms, PartitionBufferTypes, PartitionMainSpace",
                )

                if len(d) == 0 and len(r) == 0 and len(e) == 0:
                    writeline(file, "room = None")
                else:
                    writeline(file, "room = {")

                    if len(d) > 0:
                        partition = d[0]
                        p = partitions[partition]
                        print(p)
                        writeline(file, '  "partition": {')
                        writeline(
                            file,
                            '    "ally_sprite_buffer_size": %i,'
                            % p["ally_sprite_buffer_size"],
                        )
                        writeline(
                            file,
                            '    "allow_extra_sprite_buffer": %r,'
                            % p["allow_extra_sprite_buffer"],
                        )
                        writeline(
                            file,
                            '    "extra_sprite_buffer_size": %i,'
                            % p["extra_sprite_buffer_size"],
                        )
                        writeline(file, '    "buffer_a": {')
                        type_a, _ = byte(
                            prefix="PartitionBufferTypes", table=partition_buffer_table
                        )([p["clone_buffer_a_type"]])
                        writeline(file, '      "type": %s,' % type_a)
                        space_a, _ = byte(
                            prefix="PartitionMainSpace", table=partition_space_table
                        )([p["clone_buffer_a_space"]])
                        writeline(file, '      "main_buffer_space": %s,' % space_a)
                        writeline(
                            file,
                            '      "index_in_main_buffer": %r,'
                            % p["clone_buffer_a_index_in_main"],
                        )
                        writeline(file, "    },")
                        writeline(file, '    "buffer_b": {')
                        type_b, _ = byte(
                            prefix="PartitionBufferTypes", table=partition_buffer_table
                        )([p["clone_buffer_b_type"]])
                        writeline(file, '      "type": %s,' % type_b)
                        space_b, _ = byte(
                            prefix="PartitionMainSpace", table=partition_space_table
                        )([p["clone_buffer_b_space"]])
                        writeline(file, '      "main_buffer_space": %s,' % space_b)
                        writeline(
                            file,
                            '      "index_in_main_buffer": %r,'
                            % p["clone_buffer_b_index_in_main"],
                        )
                        writeline(file, "    },")
                        writeline(file, '    "buffer_c": {')
                        type_c, _ = byte(
                            prefix="PartitionBufferTypes", table=partition_buffer_table
                        )([p["clone_buffer_c_type"]])
                        writeline(file, '      "type": %s,' % type_c)
                        space_c, _ = byte(
                            prefix="PartitionMainSpace", table=partition_space_table
                        )([p["clone_buffer_c_space"]])
                        writeline(file, '      "main_buffer_space": %s,' % space_c)
                        writeline(
                            file,
                            '      "index_in_main_buffer": %r,'
                            % p["clone_buffer_c_index_in_main"],
                        )
                        writeline(file, "    },")
                        writeline(
                            file,
                            '    "full_palette_buffer": %r,' % p["full_palette_buffer"],
                        )
                        writeline(file, "  },")
                    else:
                        writeline(file, '  "partition": None,')

                    if len(r) > 0:
                        music, _ = byte(prefix="Music", table=music_table)([r[0]])
                        writeline(file, '  "music": %s,' % music)

                        loading_event = (r[2] << 8) + r[1]
                        writeline(file, '  "entrance_event": %i,' % loading_event)

                        event_triggers = []

                        j = 3
                        while j < len(r):
                            length_determinant = r[j + 1] & 0x80 == 0x80
                            if length_determinant == 0:
                                trigger_data = r[j : j + 5]
                                length = 1
                                f_bit = 0
                                byte_8_bit_4 = 0
                                j += 5
                            else:
                                trigger_data = r[j : j + 6]
                                length = 1 + (trigger_data[5] & 0x0F)
                                f_bit = (trigger_data[5] & 0x80) >> 7
                                byte_8_bit_4 = (trigger_data[5] & 0x10) >> 4
                                j += 6
                            f, _ = byte(prefix="Edge", table=edge_table)([f_bit])
                            event_triggers.append(
                                {
                                    "event": ((trigger_data[1] & 0x7F) << 8)
                                    + trigger_data[0],
                                    "enable_x_edge": trigger_data[2] & 0x80 == 0x80,
                                    "enable_y_edge": trigger_data[3] & 0x80 == 0x80,
                                    "x": trigger_data[2] & 0x7F,
                                    "y": trigger_data[3] & 0x7F,
                                    "z": trigger_data[4] & 0x1F,
                                    "f": f,
                                    "height": (trigger_data[4] & 0xF0) >> 5,
                                    "length": length,
                                    "byte_8_bit_4": byte_8_bit_4 == 1,
                                }
                            )

                        if len(event_triggers) == 0:
                            writeline(file, '  "event_tiles": [],')
                        else:
                            writeline(file, '  "event_tiles": [')
                            for j in range(len(event_triggers)):
                                t = event_triggers[j]
                                writeline(file, "    {")
                                writeline(file, '      "event": %i,' % t["event"])
                                writeline(file, '      "x": %i,' % t["x"])
                                writeline(file, '      "y": %i,' % t["y"])
                                writeline(file, '      "z": %i,' % t["z"])
                                writeline(file, '      "f": %s,' % t["f"])
                                writeline(file, '      "length": %i,' % t["length"])
                                writeline(file, '      "height": %i,' % t["height"])
                                writeline(
                                    file,
                                    '      "nw_se_edge_active": %r,'
                                    % t["enable_x_edge"],
                                )
                                writeline(
                                    file,
                                    '      "ne_sw_edge_active": %r,'
                                    % t["enable_y_edge"],
                                )
                                writeline(
                                    file,
                                    '      "byte_8_bit_4": %r,' % t["byte_8_bit_4"],
                                )
                                if j < len(event_triggers) - 1:
                                    writeline(file, "    },")
                                else:
                                    writeline(file, "    }")
                            writeline(file, "  ],")
                    else:
                        writeline(file, '  "music": None,')
                        writeline(file, '  "entrance_event": None,')
                        writeline(file, '  "event_tiles": [],')

                    if len(e) > 0:
                        exit_fields = []
                        j = 0
                        while j < len(e):
                            offset = 0
                            field_data = e[j:]
                            exit_type = (field_data[1] & 0x60) >> 6
                            byte_2_bit_0 = field_data[1] & 0x01
                            byte_2_bit_1 = (field_data[1] & 0x02) >> 1
                            byte_2_bit_2 = (field_data[1] & 0x04) >> 2

                            length_determinant = field_data[1] & 0x80 == 0x80
                            dst = ((field_data[1] << 8) + field_data[0]) & 0x1FF

                            offset += 5
                            if exit_type == 0:  # room
                                dst, _ = byte(prefix="Rooms", table=room_table)([dst])
                                dst_f_val = (field_data[7] & 0xF0) >> 5
                                dst_f, _ = byte(
                                    prefix="RadialDirection",
                                    table=radial_direction_table,
                                )([dst_f_val])
                                dst_props = {
                                    "x": field_data[5] & 0x7F,
                                    "y": field_data[6] & 0x7F,
                                    "z": field_data[7] & 0x1F,
                                    "z_half": (field_data[6] & 0x80) == 0x80,
                                    "f": dst_f,
                                    "x_bit_7": (field_data[5] & 0x80) == 0x80,
                                }
                                offset += 3
                            else:  # world map location
                                dst &= 0xFF
                                dst, _ = byte(prefix="Locations", table=location_table)(
                                    [dst]
                                )
                                dst_props = {
                                    "byte_2_bit_0": byte_2_bit_0 == 1,
                                    "byte_2_bit_1": byte_2_bit_1 == 1,
                                }
                            if length_determinant == 0:
                                length = 1
                                f_bit = 0
                            else:
                                length = 1 + (field_data[offset] & 0x0F)
                                f_bit = (field_data[offset] & 0x80) >> 7
                                offset += 1
                            f, _ = byte(prefix="Edge", table=edge_table)([f_bit])
                            j += offset

                            exit_fields.append(
                                {
                                    "x": field_data[2] & 0x7F,
                                    "y": field_data[3] & 0x7F,
                                    "z": field_data[4] & 0x1F,
                                    "f": f,
                                    "length": length,
                                    "height": (field_data[4] & 0xF0) >> 5,
                                    "enable_x_edge": field_data[2] & 0x80 == 0x80,
                                    "enable_y_edge": field_data[3] & 0x80 == 0x80,
                                    "destination": dst,
                                    "show_message": (field_data[1] & 0x08) == 0x08,
                                    "exit_type": exit_type,
                                    "byte_2_bit_2": byte_2_bit_2 == 1,
                                    "dst_props": dst_props,
                                }
                            )

                        if len(exit_fields) == 0:
                            writeline(file, '  "exit_fields": [],')
                        else:
                            writeline(file, '  "exit_fields": [')
                            for j in range(len(exit_fields)):
                                t = exit_fields[j]
                                exit_type_string, _ = byte(
                                    prefix="ExitType", table=exit_type_table
                                )([t["exit_type"]])
                                writeline(file, "    {")
                                writeline(file, '      "x": %i,' % t["x"])
                                writeline(file, '      "y": %i,' % t["y"])
                                writeline(file, '      "z": %i,' % t["z"])
                                writeline(file, '      "f": %s,' % t["f"])
                                writeline(file, '      "length": %i,' % t["length"])
                                writeline(file, '      "height": %i,' % t["height"])
                                writeline(
                                    file,
                                    '      "nw_se_edge_active": %r,'
                                    % t["enable_x_edge"],
                                )
                                writeline(
                                    file,
                                    '      "ne_sw_edge_active": %r,'
                                    % t["enable_y_edge"],
                                )
                                writeline(
                                    file,
                                    '      "destination_type": %s,' % exit_type_string,
                                )
                                writeline(
                                    file,
                                    '      "byte_2_bit_2": %r,' % t["byte_2_bit_2"],
                                )
                                writeline(
                                    file, '      "destination": %s,' % t["destination"]
                                )
                                writeline(
                                    file,
                                    '      "show_message": %r,' % t["show_message"],
                                )
                                p = t["dst_props"]
                                writeline(file, '      "destination_props": {')
                                if t["exit_type"] == 0:
                                    writeline(file, '        "x": %i,' % p["x"])
                                    writeline(file, '        "y": %i,' % p["y"])
                                    writeline(file, '        "z": %i,' % p["z"])
                                    writeline(
                                        file, '        "z_half": %r,' % p["z_half"]
                                    )
                                    writeline(file, '        "f": %s,' % p["f"])
                                    writeline(
                                        file, '        "x_bit_7": %r' % p["x_bit_7"]
                                    )
                                else:
                                    writeline(
                                        file,
                                        '        "byte_2_bit_0": %r,'
                                        % p["byte_2_bit_0"],
                                    )
                                    writeline(
                                        file,
                                        '        "byte_2_bit_1": %r,'
                                        % p["byte_2_bit_1"],
                                    )
                                writeline(file, "      }")

                                if j < len(exit_fields) - 1:
                                    writeline(file, "    },")
                                else:
                                    writeline(file, "    }")
                            writeline(file, "  ],")
                    else:
                        writeline(file, '  "exit_fields": [],')

                    if len(d) > 0:
                        offset = 1
                        writeline(file, '  "objects": [')
                        n = 0
                        while offset < len(d):
                            l = 12

                            otype = d[offset] >> 4
                            obj_type, _ = byte(prefix="ObjectType", table=object_type)(
                                [d[offset] >> 4]
                            )

                            speed = d[offset + 1] & 0x07

                            assigned_npc = ((d[offset + 4] & 0x0F) << 6) | (
                                d[offset + 3] >> 2
                            )
                            action_scipt = ((d[offset + 5] & 0x3F) << 4) | (
                                (d[offset + 4] & 0xFF) >> 4
                            )

                            writeline(file, "    {")
                            writeline(file, '      "id": %i,' % n)
                            writeline(file, '      "type": %s,' % obj_type)
                            initiator, _ = byte(
                                prefix="Initiator", table=event_initiator
                            )([d[offset + 7] >> 4])
                            writeline(file, '      "initiator": %s,' % initiator)
                            writeline(file, '      "model": %i,' % assigned_npc)
                            if otype <= 1:
                                event = ((d[offset + 7] & 0x0F) << 8) | d[offset + 6]
                                writeline(file, '      "event_script": %i,' % event)
                            elif otype == 2:
                                writeline(
                                    file, '      "battle_pack": %i,' % d[offset + 6]
                                )
                                writeline(
                                    file,
                                    '      "after_battle": %i,'
                                    % (d[offset + 7] & 0x0F),
                                )
                            writeline(file, '      "action_script": %i,' % action_scipt)
                            writeline(file, '      "speed": %i,' % speed)
                            if otype == 0:
                                writeline(
                                    file,
                                    '      "npc_id_offset": %i,'
                                    % (d[offset + 8] & 0x07),
                                )
                                writeline(
                                    file,
                                    '      "event_offset": %i,' % (d[offset + 8] >> 5),
                                )
                                writeline(
                                    file,
                                    '      "action_offset": %i,'
                                    % ((d[offset + 8] & 0x1F) >> 3),
                                )
                            elif otype == 1:
                                writeline(
                                    file,
                                    '      "star_offset": %i,' % (d[offset + 8] & 0x0F),
                                )
                                writeline(
                                    file,
                                    '      "item_offset": %i,' % (d[offset + 8] >> 4),
                                )
                            elif otype == 2:
                                writeline(
                                    file,
                                    '      "action_offset": %i,'
                                    % (d[offset + 8] & 0x0F),
                                )
                                writeline(
                                    file,
                                    '      "pack_offset": %i,' % (d[offset + 8] >> 4),
                                )
                            writeline(
                                file,
                                '      "visible": %r,'
                                % bit_bool_from_num(d[offset + 9], 7),
                            )
                            writeline(file, '      "x": %i,' % (d[offset + 9] & 0x7F))
                            writeline(file, '      "y": %i,' % (d[offset + 10] & 0x7F))
                            writeline(file, '      "z": %i,' % (d[offset + 11] & 0x1F))
                            writeline(
                                file,
                                '      "z_half": %r,'
                                % bit_bool_from_num(d[offset + 10], 7),
                            )
                            direction, _ = byte(
                                prefix="RadialDirection", table=radial_direction_table
                            )([d[offset + 11] >> 5])
                            writeline(file, '      "direction": %s,' % (direction))
                            writeline(
                                file,
                                '      "face_on_trigger": %r,'
                                % bit_bool_from_num(d[offset + 1], 3),
                            )
                            writeline(
                                file,
                                '      "cant_enter_doors": %r,'
                                % bit_bool_from_num(d[offset + 1], 4),
                            )
                            writeline(
                                file,
                                '      "byte2_bit5": %r,'
                                % bit_bool_from_num(d[offset + 1], 5),
                            )
                            writeline(
                                file,
                                '      "set_sequence_playback": %r,'
                                % bit_bool_from_num(d[offset + 1], 6),
                            )
                            writeline(
                                file,
                                '      "cant_float": %r,'
                                % bit_bool_from_num(d[offset + 1], 7),
                            )
                            writeline(
                                file,
                                '      "cant_walk_up_stairs": %r,'
                                % bit_bool_from_num(d[offset + 2], 0),
                            )
                            writeline(
                                file,
                                '      "cant_walk_under": %r,'
                                % bit_bool_from_num(d[offset + 2], 1),
                            )
                            writeline(
                                file,
                                '      "cant_pass_walls": %r,'
                                % bit_bool_from_num(d[offset + 2], 2),
                            )
                            writeline(
                                file,
                                '      "cant_jump_through": %r,'
                                % bit_bool_from_num(d[offset + 2], 3),
                            )
                            writeline(
                                file,
                                '      "cant_pass_npcs": %r,'
                                % bit_bool_from_num(d[offset + 2], 4),
                            )
                            writeline(
                                file,
                                '      "byte3_bit5": %r,'
                                % bit_bool_from_num(d[offset + 2], 5),
                            )
                            writeline(
                                file,
                                '      "cant_walk_through": %r,'
                                % bit_bool_from_num(d[offset + 2], 6),
                            )
                            writeline(
                                file,
                                '      "byte3_bit7": %r,'
                                % bit_bool_from_num(d[offset + 2], 7),
                            )
                            writeline(
                                file,
                                '      "slidable_along_walls": %r,'
                                % bit_bool_from_num(d[offset + 3], 0),
                            )
                            writeline(
                                file,
                                '      "cant_move_if_in_air": %r,'
                                % bit_bool_from_num(d[offset + 3], 1),
                            )
                            writeline(
                                file,
                                '      "byte7_upper2": 0x%02x,' % (d[offset + 5] >> 6),
                            )
                            n += 1
                            extra_length = d[offset] & 0x0F
                            if extra_length > 0:
                                l += extra_length * 4
                                writeline(file, '      "clones": [')

                                for o in range(offset + 12, offset + l - 1, 4):
                                    writeline(file, "        {")
                                    writeline(file, '          "id": %i,' % n)
                                    if otype == 0:
                                        writeline(
                                            file,
                                            '          "npc_id_offset": %i,'
                                            % (d[o] & 0x07),
                                        )
                                        writeline(
                                            file,
                                            '          "event_offset": %i,'
                                            % (d[o] >> 5),
                                        )
                                        writeline(
                                            file,
                                            '          "action_offset": %i,'
                                            % ((d[o] & 0x1F) >> 3),
                                        )
                                    elif otype == 1:
                                        writeline(
                                            file,
                                            '          "star_offset": %i,'
                                            % (d[o] & 0x0F),
                                        )
                                        writeline(
                                            file,
                                            '          "item_offset": %i,'
                                            % (d[o] >> 4),
                                        )
                                    elif otype == 2:
                                        writeline(
                                            file,
                                            '          "action_offset": %i,'
                                            % (d[o] & 0x0F),
                                        )
                                        writeline(
                                            file,
                                            '          "pack_offset": %i,'
                                            % (d[o] >> 4),
                                        )
                                    writeline(
                                        file,
                                        '          "visible": %r,'
                                        % bit_bool_from_num(d[o + 1], 7),
                                    )
                                    writeline(
                                        file, '          "x": %i,' % (d[o + 1] & 0x7F)
                                    )
                                    writeline(
                                        file, '          "y": %i,' % (d[o + 2] & 0x7F)
                                    )
                                    writeline(
                                        file, '          "z": %i,' % (d[o + 3] & 0x1F)
                                    )
                                    writeline(
                                        file,
                                        '          "z_half": %r,'
                                        % bit_bool_from_num(d[o + 2], 7),
                                    )
                                    direction, _ = byte(
                                        prefix="RadialDirection",
                                        table=radial_direction_table,
                                    )([d[o + 3] >> 5])
                                    writeline(
                                        file, '          "direction": %s' % (direction)
                                    )
                                    n += 1
                                    if o + 4 >= offset + l:
                                        writeline(file, "        }")
                                    else:
                                        writeline(file, "        },")
                                writeline(file, "      ]")
                            else:
                                writeline(file, '      "clones": []')

                            if offset + l < len(d):
                                writeline(file, "    },")
                            else:
                                writeline(file, "    }")

                            offset += l
                        writeline(file, "  ]")
                    else:
                        writeline(file, '  "objects": []')

                    writeline(file, "}")

                file.close()

        file = open("%s/roomobjects.py" % dest, "w", encoding="utf-8")
        for i in range(512):
            writeline(
                file,
                "from randomizer.data.roomobjects.room_%i import room as room_%i"
                % (i, i),
            )
        writeline(file, "rooms = [None]*512")
        for i in range(512):
            writeline(file, "rooms[%i] = room_%i" % (i, i))
        file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled 512 room objects to randomizer/data/roomobjects/"
            )
        )
