from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import (
    shortify,
    bit,
    dbyte,
    named,
    con,
    byte,
    byte_int,
    short,
    short_int,
    parse_flags,
    flags,
    con_int,
    flags_short,
    con_bitarray,
    writeline,
)
from .objectsequencetables import (
    sequence_speed_table,
    vram_priority_table,
    _0x08_flags,
    _0x0A_flags,
    _0x10_flags,
)
from .eventtables import (
    npc_packet_table,
    area_object_table,
    radial_direction_table,
    sound_table,
    coord_table,
    coord_unit_table,
    room_table,
)

start = 0x210800
# end = 0x21BADE
end = 0x21BFFF  # it would be extremely good to expand into this space
pointers = {"start": 0x210000, "end": 0x2107FF}

sequence_lens = [
    1,  # 00
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    3,
    1,
    2,
    2,
    2,
    2,
    2,
    1,
    2,  # 10
    2,
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,  # 20
    1,
    1,
    2,
    5,
    5,
    16,
    16,
    16,
    2,
    1,
    5,
    3,
    3,
    3,
    7,
    3,  # 30
    3,
    3,
    3,
    2,
    3,
    1,
    1,
    1,
    1,
    6,
    6,
    5,
    3,
    5,
    4,
    1,  # 40
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,  # 50
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    1,
    1,
    1,
    1,
    2,  # 60
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    2,
    2,
    1,
    1,
    1,
    1,
    1,  # 70
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    2,
    1,
    2,
    3,
    3,
    3,  # 80
    3,
    3,
    3,
    3,
    1,
    1,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    4,  # 90
    4,
    4,
    4,
    4,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    2,
    3,
    3,
    3,
    2,  # A0
    2,
    2,
    1,
    2,
    2,
    2,
    1,
    3,
    3,
    2,
    2,
    3,
    3,
    1,
    1,
    4,  # B0
    4,
    2,
    2,
    2,
    2,
    3,
    4,
    2,
    2,
    2,
    2,
    3,
    3,
    1,
    1,
    3,  # C0
    2,
    4,
    1,
    2,
    2,
    2,
    2,
    2,
    2,
    1,
    1,
    1,
    1,
    1,
    1,
    3,  # D0
    1,
    3,
    3,
    2,
    1,
    2,
    1,
    4,
    4,
    4,
    3,
    4,
    4,
    4,
    3,
    5,  # E0
    5,
    5,
    5,
    6,
    6,
    5,
    5,
    3,
    5,
    3,
    3,
    3,
    3,
    3,
    3,
    2,  # F0
    3,
    3,
    3,
    1,
    1,
    1,
    1,
    5,
    1,
    1,
    1,
    1,
    0,
    1,
    1,
]

# replicant function - appears to mean it's the same as event function???
# may need to import info from event disassembler
fd_sequence_lens = [
    2,  # 00
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    2,  # 10
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    5,  # 20
    2,
    2,
    4,
    4,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    8,  # 30
    8,
    7,
    5,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    5,
    7,
    5,
    2,  # 40
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 50
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    2,
    2,
    2,
    2,
    2,  # 60
    2,
    2,
    2,
    2,
    2,
    3,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 70
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 80
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # 90
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    3,
    2,
    3,
    2,
    2,  # A0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    4,  # B0
    4,
    4,
    3,
    3,
    3,
    4,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # C0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    4,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # D0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # e0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,  # F0
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
    2,
]

# I'll refactor this later

def tok(rom, start, end):
    dex = start
    script = []
    while dex <= end:
        cmd = rom[dex]
        local_lens = sequence_lens

        if cmd == 0xFD:
            cmd = rom[dex + 1]
            local_lens = fd_sequence_lens

        l = local_lens[cmd]
        script.append((rom[dex : dex + l], dex))
        dex += l
    return script

def parse_line(line, offset):
    if line[0] == 0xFD:
        cmd = line[1]
        rest = line[2:]
        table = fd_names
    else:
        cmd = line[0]
        rest = line[1:]
        table = names
    if table[cmd]:
        name, args = table[cmd](rest)
    else:
        name, args = "db", line
    return name, args

fd_names = [None] * 256
names = [None] * 256

# This is weird in LS, may not reflect output, however it does follow the docs

def set_sprite_sequence(args):
    sprite = args[0] & 0x07
    flag_short = shortify(args, 0)
    f = parse_flags(flag_short, "_0x08Flags", _0x08_flags, [3, 4, 6, 15])
    sequence = args[1] & 0x7F
    return "set_sprite_sequence", [sequence, sprite, f]

def set_animation_speed(args):
    speed = args[0] & 0x07
    flag_short = args[0] >> 6
    f = parse_flags(flag_short, "_0x10Flags", _0x10_flags, [0, 1])
    return "set_animation_speed", [speed, f]

def set_object_memory_bits(obj):
    def inner_set_object_memory_bits(args):
        f = parse_flags(args[0])
        return "set_object_memory_bits", [obj, f]

    return inner_set_object_memory_bits

def transfer_to_xyzf(args):
    x = args[0]
    y = args[1]
    z = args[2] & 0x1F
    direction = args[2] >> 5
    return "transfer_to_xyzf", [x, y, z, direction]

def transfer_xyzf_steps(args):
    x = args[0]
    y = args[1]
    z = args[2] & 0x1F
    direction = args[2] >> 5
    return "transfer_xyzf_steps", [x, y, z, direction]

def transfer_xyzf_pixels(args):
    x = args[0]
    y = args[1]
    z = args[2] & 0x1F
    direction = args[2] >> 5
    return "transfer_xyzf_pixels", [x, y, z, direction]

def fade_out_sound_to_volume(args):
    return "fade_out_sound_to_volume", args

def parse_target_bit(cmd, args):
    bit = args[0] & 0x07
    addr = 0x7040 + (0x0020 * (cmd & 0x0F)) + (args[0] >> 3)
    return addr, bit

# name bit vars eventually
def set_bit(cmd):
    def inner_set_bit(args):
        addr, bit = parse_target_bit(cmd, args)
        return "set_bit", [addr, bit]

    return inner_set_bit

def clear_bit(cmd):
    def inner_clear_bit(args):
        addr, bit = parse_target_bit(cmd - 0xA4, args)
        return "clear_bit", [addr, bit]

    return inner_clear_bit

def parse_object_coord(cmd):
    def inner_parse_object_coord(args):
        obj = args[0] & 0x3F
        unit = bit(args, 0, 6)
        coord = cmd - 0xC4
        func_params = [
            obj,
            coord,
            parse_flags(args[0], bits=[7]),
        ]
        if cmd < 0xC9:
            func_params.append(unit)
        return "set_700C_to_object_coord", func_params

    return inner_parse_object_coord

def jmp_if_bit_clear(cmd):
    def inner_jmp_if_bit_clear(args):
        addr, bit = parse_target_bit(cmd - 0xDC, args)
        to_addr = shortify(args, 1)
        return "jmp_if_bit_clear", [
            addr,
            bit,
            to_addr,
        ]

    return inner_jmp_if_bit_clear

def jmp_if_bit_set(cmd):
    def inner_jmp_if_bit_set(args):
        addr, bit = parse_target_bit(cmd - 0xD8, args)
        to_addr = shortify(args, 1)
        return "jmp_if_bit_set", [
            addr,
            bit,
            to_addr,
        ]

    return inner_jmp_if_bit_set

def pause(args):
    return "pause", [args[0] + 1]

def pauseshort(args):
    s = shortify(args, 0)
    return "pause", [s + 1]

def set_object_presence_in_level(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    if presence:
        func = "summon_to_level"
    else:
        func = "remove_from_level"
    return func, [obj, level]

def set_object_trigger_in_level(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    if presence:
        func = "enable_trigger_in_level"
    else:
        func = "disable_trigger_in_level"
    return func, [obj, level]

def jmp_depending_on_object_presence(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    addr = shortify(args, 2)
    if presence:
        func = "jmp_if_object_in_level"
    else:
        func = "jmp_if_object_not_in_level"
    return func, [obj, level, addr]

def mem_700C_shift_left(args):
    addr = 2 * args[0] + 0x7000
    shift = 256 - args[1]
    return "mem_700C_shift_left", [addr, shift]

names[0x00] = named("visibility_on")
names[0x01] = named("visibility_off")
names[0x02] = named("sequence_playback_on")
names[0x03] = named("sequence_playback_off")
names[0x04] = named("sequence_looping_on")
names[0x05] = named("sequence_looping_off")
names[0x06] = named("fixed_f_coord_on")
names[0x07] = named("fixed_f_coord_off")
names[0x08] = set_sprite_sequence
names[0x09] = named("reset_properties")
names[0x0A] = named("overwrite_solidity", flags(prefix="_0x0AFlags", table=_0x0A_flags))
names[0x0B] = named("set_solidity_bits", flags(prefix="_0x0AFlags", table=_0x0A_flags))
names[0x0C] = named(
    "clear_solidity_bits", flags(prefix="_0x0AFlags", table=_0x0A_flags)
)
names[0x0D] = named("set_palette_row", byte_int())
names[0x0E] = named("inc_palette_row_by", byte_int())
names[0x0F] = named("inc_palette_row_by", con(1))
names[0x10] = set_animation_speed
names[0x11] = set_object_memory_bits(0x0D)
names[0x12] = set_object_memory_bits(0x0B)
names[0x13] = named(
    "set_vram_priority", byte(prefix="VramPriority", table=vram_priority_table)
)
names[0x14] = set_object_memory_bits(0x0E)
names[0x15] = named("set_movement_bits", flags(prefix="_0x0AFlags", table=_0x0A_flags))
# 0x16 - 0x20 undocumented
names[0x21] = named("bpl_26_27_28")
names[0x22] = named("bmi_26_27_28")
# 0x23 - 0x25 undocumented
names[0x26] = named(
    "embedded_animation_routine",
    con(0x26),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
)
names[0x27] = named(
    "embedded_animation_routine",
    con(0x27),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
)
names[0x28] = named(
    "embedded_animation_routine",
    con(0x28),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
    byte(),
)
# 0x29 undocumented
names[0x2A] = named("bpl_26_27")
# 0x2B - 0x3A undocumented
names[0x3A] = named(
    "jmp_if_object_within_range",
    byte(prefix="AreaObjects", table=area_object_table),
    byte_int(),
    byte_int(),
    short(),
)
names[0x3B] = named(
    "jmp_if_object_within_range_same_z",
    byte(prefix="AreaObjects", table=area_object_table),
    byte_int(),
    byte_int(),
    short(),
)
names[0x3C] = named("unknown_jmp_3C", byte(), byte(), short())
names[0x3D] = named("jmp_if_mario_in_air", short())
names[0x3E] = named(
    "create_packet_at_npc_coords",
    byte(prefix="NPCPackets", table=npc_packet_table),
    byte(prefix="AreaObjects", table=area_object_table),
    short(),
)
names[0x3F] = named(
    "create_packet_at_7010", byte(prefix="NPCPackets", table=npc_packet_table), short()
)
names[0x40] = named("walk_1_step_east")
names[0x41] = named("walk_1_step_southeast")
names[0x42] = named("walk_1_step_south")
names[0x43] = named("walk_1_step_southwest")
names[0x44] = named("walk_1_step_west")
names[0x45] = named("walk_1_step_northwest")
names[0x46] = named("walk_1_step_north")
names[0x47] = named("walk_1_step_northeast")
names[0x48] = named("walk_1_step_f_direction")
# 0x49 undocumented
names[0x4A] = named("add_z_coord_1_step")
names[0x4B] = named("dec_z_coord_1_step")
# 0x4C - 0x4F undocumented
names[0x50] = named("shift_east_steps", byte_int())
names[0x51] = named("shift_southeast_steps", byte_int())
names[0x52] = named("shift_south_steps", byte_int())
names[0x53] = named("shift_southwest_steps", byte_int())
names[0x54] = named("shift_west_steps", byte_int())
names[0x55] = named("shift_northwest_steps", byte_int())
names[0x56] = named("shift_north_steps", byte_int())
names[0x57] = named("shift_northeast_steps", byte_int())
names[0x58] = named("shift_f_direction_steps", byte_int())
names[0x59] = named("shift_z_20_steps")
names[0x5A] = named("shift_z_up_steps", byte_int())
names[0x5B] = named("shift_z_down_steps", byte_int())
names[0x5C] = named("shift_z_up_20_steps")
names[0x5D] = named("shift_z_down_20_steps")
# 0x5E - 0x5F undocumented
names[0x60] = named("shift_east_pixels", byte_int())
names[0x61] = named("shift_southeast_pixels", byte_int())
names[0x62] = named("shift_south_pixels", byte_int())
names[0x63] = named("shift_southwest_pixels", byte_int())
names[0x64] = named("shift_west_pixels", byte_int())
names[0x65] = named("shift_northwest_pixels", byte_int())
names[0x66] = named("shift_north_pixels", byte_int())
names[0x67] = named("shift_northeast_pixels", byte_int())
names[0x68] = named("shift_f_direction_pixels", byte_int())
names[0x69] = named("walk_f_direction_16_pixels")
names[0x6A] = named("shift_z_up_pixels", byte_int())
names[0x6B] = named("shift_z_down_pixels", byte_int())
# 0x6C - 0x6F undocumented
names[0x70] = named("face_east")
names[0x71] = named("face_southeast")
names[0x72] = named("face_south")
names[0x73] = named("face_southwest")
names[0x74] = named("face_west")
names[0x75] = named("face_northwest")
names[0x76] = named("face_north")
names[0x77] = named("face_northeast")
names[0x78] = named("face_mario")
names[0x79] = named("turn_clockwise_45_degrees")
names[0x7A] = named("turn_random_direction")
names[0x7B] = named("turn_clockwise_45_degrees_n_times", byte_int())
names[0x7C] = named("face_east_7C")  # indistinguishable from 0x70
names[0x7D] = named("face_southwest_7D", byte())  # indistinguishable from 0x73
names[0x7E] = named("jump_to_height_silent", short_int())
names[0x7F] = named("jump_to_height", short_int())
names[0x80] = named("walk_to_xy_coords", byte_int(), byte_int())
names[0x81] = named("walk_xy_steps", byte_int(), byte_int())
names[0x82] = named("shift_to_xy_coords", byte_int(), byte_int())
names[0x83] = named("shift_xy_steps", byte_int(), byte_int())
names[0x84] = named("shift_xy_pixels", byte_int(), byte_int())
names[0x85] = named("maximize_sequence_speed")
# indistinguishable from 0x85
names[0x86] = named("maximize_sequence_speed_86")
names[0x87] = named(
    "transfer_to_object_xy", byte(prefix="AreaObjects", table=area_object_table)
)
names[0x88] = named("walk_to_7016_7018")
names[0x89] = named("transfer_to_7016_7018")
names[0x8A] = named("run_away_shift")
# 0x8B - 0x8F undocumented
names[0x90] = named("bounce_to_xy_with_height", byte_int(), byte_int(), byte_int())
names[0x91] = named("bounce_xy_steps_with_height", byte_int(), byte_int(), byte_int())
names[0x92] = transfer_to_xyzf
names[0x93] = transfer_xyzf_steps
names[0x94] = transfer_xyzf_pixels
names[0x95] = named(
    "transfer_to_object_xyz", byte(prefix="AreaObjects", table=area_object_table)
)
# 0x96 - 0x9A undocumented
names[0x9B] = named("stop_sound")
names[0x9C] = named("play_sound", byte(prefix="Sounds", table=sound_table), con_int(6))
names[0x9D] = named(
    "play_sound_balance", byte(prefix="Sounds", table=sound_table), byte_int()
)
names[0x9E] = fade_out_sound_to_volume
# 0x9F undocumented
# Pretty much all of the functions below are copies of their event script disassembler counterparts. I could have reduced the repetition here, but... eh
names[0xA0] = set_bit(0xA0)
names[0xA1] = set_bit(0xA1)
names[0xA2] = set_bit(0xA2)
names[0xA3] = named("set_mem_704x_at_700C_bit")
names[0xA4] = clear_bit(0xA4)
names[0xA5] = clear_bit(0xA5)
names[0xA6] = clear_bit(0xA6)
names[0xA7] = named("clear_mem_704x_at_700C_bit")
names[0xA8] = named("set_var_to_const", byte(0x70A0), byte_int())
names[0xA9] = named("add", byte(0x70A0), byte_int())
names[0xAA] = named("inc", byte(0x70A0))
names[0xAB] = named("dec", byte(0x70A0))
names[0xAC] = named("set_var_to_const", con(0x700C), short_int())
names[0xAD] = named("add", con(0x700C), short_int())
names[0xAE] = named("inc", con(0x700C))
names[0xAF] = named("dec", con(0x700C))
names[0xB0] = named("set_var_to_const", dbyte(0x7000), short())
names[0xB1] = named("add", dbyte(0x7000), short())
names[0xB2] = named("inc", dbyte(0x7000))
names[0xB3] = named("dec", dbyte(0x7000))
names[0xB4] = named("copy_var_to_var", byte(0x70A0), con(0x700C))
names[0xB5] = named("copy_var_to_var", con(0x700C), byte(0x70A0))
names[0xB6] = named("set_var_to_random", con(0x700C), short_int())
names[0xB7] = named(
    "set_var_to_random", dbyte(0x7000), short_int()
)  # may be confused for 0xB6
names[0xB8] = named("add_short_mem_to_700C", dbyte(0x7000))
names[0xB9] = named("dec_short_mem_from_700C", dbyte(0x7000))
names[0xBA] = named("copy_var_to_var", dbyte(0x7000), con(0x700C))
names[0xBB] = named("copy_var_to_var", con(0x700C), dbyte(0x7000))
names[0xBC] = named("copy_var_to_var", dbyte(0x7000), dbyte(0x7000))
names[0xBD] = named("swap_vars", dbyte(0x7000), dbyte(0x7000))
names[0xBE] = named("move_7010_7015_to_7016_701B")
names[0xBF] = named("move_7016_701B_to_7010_7015")
names[0xC0] = named("mem_compare_val", con(0x700C), short_int())
names[0xC1] = named("compare_700C_to_var", dbyte(0x7000))
names[0xC2] = named("mem_compare", dbyte(0x7000), short_int())
names[0xC3] = named("set_700C_to_current_level")
names[0xC4] = parse_object_coord(0xC4)
names[0xC5] = parse_object_coord(0xC5)
names[0xC6] = parse_object_coord(0xC6)
# 0xC7 - 0xC8 undocumented
names[0xC9] = parse_object_coord(0xC9)
names[0xCA] = named("set_700C_to_pressed_button")
names[0xCB] = named("set_700C_to_tapped_button")
# 0xCC - 0xCF undocumented
names[0xD0] = named("jmp_to_script", short_int())
# 0xD1 undocumented
names[0xD2] = named("jmp", short())
names[0xD3] = named("jmp_to_subroutine", short())
names[0xD4] = named("start_loop_n_times", byte_int())
# 0xD5 undocumented
names[0xD6] = named("load_mem", dbyte(0x7000))
names[0xD7] = named("end_loop")
names[0xD8] = jmp_if_bit_set(0xD8)
names[0xD9] = jmp_if_bit_set(0xD9)
names[0xDA] = jmp_if_bit_set(0xDA)
names[0xDB] = named("jmp_if_mem_704x_at_700C_bit_set", short())
names[0xDC] = jmp_if_bit_clear(0xDC)
names[0xDD] = jmp_if_bit_clear(0xDD)
names[0xDE] = jmp_if_bit_clear(0xDE)
names[0xDF] = named("jmp_if_mem_704x_at_700C_bit_clear", short())
names[0xE0] = named("jmp_if_var_equals_const", byte(0x70A0), byte_int(), short())
names[0xE1] = named("jmp_if_var_not_equals_const", byte(0x70A0), byte_int(), short())
names[0xE2] = named("jmp_if_var_equals_const", con(0x700C), short_int(), short())
names[0xE3] = named("jmp_if_var_not_equals_const", con(0x700C), short_int(), short())
names[0xE4] = named("jmp_if_var_equals_const", dbyte(0x7000), short_int(), short())
names[0xE5] = named(
    "jmp_if_var_not_equals_const", dbyte(0x7000), short_int(), short()
)  # may be confused for 0xE3
names[0xE6] = named("jmp_if_700C_all_bits_clear", flags_short(), short())
names[0xE7] = named("jmp_if_700C_any_bits_set", flags_short(), short())
names[0xE8] = named("jmp_if_random_above_128", short())
names[0xE9] = named("jmp_if_random_above_66", short(), short())
names[0xEA] = named("jmp_if_loaded_memory_is_0", short())
names[0xEB] = named("jmp_if_loaded_memory_is_not_0", short())
names[0xEC] = named("jmp_if_comparison_result_is_greater_or_equal", short())
names[0xED] = named("jmp_if_comparison_result_is_lesser", short())
names[0xEE] = named("jmp_if_loaded_memory_is_below_0", short())
names[0xEF] = named("jmp_if_loaded_memory_is_above_or_equal_0", short())
names[0xF0] = pause
names[0xF1] = pauseshort
names[0xF2] = set_object_presence_in_level
names[0xF3] = set_object_trigger_in_level
names[0xF4] = named("summon_object_at_70A8_to_current_level")
names[0xF5] = named("remove_object_at_70A8_from_current_level")
names[0xF6] = named("enable_trigger_at_70A8")
names[0xF7] = named("disable_trigger_at_70A8")
names[0xF8] = jmp_depending_on_object_presence
names[0xF9] = named("jmp_to_start_of_this_script")
# indistinguishable from F9
names[0xFA] = named("jmp_to_start_of_this_script_FA")
# 0xFB - 0xFC undocumented
# 0xFD is a special case
names[0xFE] = named("ret")
names[0xFF] = named("end_all")

fd_names[0x00] = named("shadow_off")
fd_names[0x01] = named("shadow_on")
fd_names[0x02] = named("floating_on")
fd_names[0x03] = named("floating_off")
fd_names[0x04] = named("object_memory_set_bit", con(0x0E), con_bitarray([4]))
fd_names[0x05] = named("object_memory_clear_bit", con(0x0E), con_bitarray([4]))
fd_names[0x06] = named("object_memory_set_bit", con(0x0E), con_bitarray([5]))
fd_names[0x07] = named("object_memory_clear_bit", con(0x0E), con_bitarray([5]))
fd_names[0x08] = named("object_memory_set_bit", con(0x09), con_bitarray([7]))
fd_names[0x09] = named("object_memory_clear_bit", con(0x09), con_bitarray([7]))
fd_names[0x0A] = named("object_memory_set_bit", con(0x08), con_bitarray([4]))
fd_names[0x0B] = named("object_memory_clear_bit", con(0x08), con_bitarray([3, 4]))
fd_names[0x0C] = named("object_memory_clear_bit", con(0x30), con_bitarray([4]))
fd_names[0x0D] = named("object_memory_set_bit", con(0x30), con_bitarray([4]))
fd_names[0x0E] = named(
    "object_memory_modify_bits", con(0x09), con_bitarray([5]), con_bitarray([4, 6])
)
fd_names[0x0F] = named("set_priority", byte_int())
fd_names[0x10] = named("object_memory_clear_bit", con(0x12), con_bitarray([5]))
fd_names[0x11] = named("object_memory_set_bit", con(0x12), con_bitarray([5]))
# 0x12 undocumented
fd_names[0x13] = named("object_memory_clear_bit", con(0x0C), con_bitarray([3, 4, 5]))
fd_names[0x14] = named("object_memory_set_bit", con(0x0C), con_bitarray([3, 4, 5]))
fd_names[0x15] = named(
    "object_memory_modify_bits", con(0x0C), con_bitarray([4]), con_bitarray([3, 5])
)
fd_names[0x16] = named("object_memory_clear_bit", con(0x0B), con_bitarray([3]))
fd_names[0x17] = named("object_memory_set_bit", con(0x0B), con_bitarray([3]))
fd_names[0x18] = named("object_memory_set_bit", con(0x3C), con_bitarray([6]))
fd_names[0x19] = named("object_memory_set_bit", con(0x0D), con_bitarray([6]))
# 0x1A - 0x3C undocumented
fd_names[0x3D] = named(
    "jmp_if_object_in_air", byte(prefix="AreaObjects", table=area_object_table), short()
)
fd_names[0x3E] = named(
    "create_packet_at_7010_with_event",
    byte(prefix="NPCPackets", table=npc_packet_table),
    short_int(),
    short(),
)
# 0x3F - 0x9D undocumented
fd_names[0x9E] = named(
    "play_sound", byte(prefix="Sounds", table=sound_table), con_int(4)
)
# 0x9F - 0xAF undocumented
fd_names[0xB0] = named("mem_700C_and_const", short())
fd_names[0xB1] = named("mem_700C_or_const", short())
fd_names[0xB2] = named("mem_700C_xor_const", short())
fd_names[0xB3] = named("mem_700C_and_var", dbyte(0x7000))
fd_names[0xB4] = named("mem_700C_or_var", dbyte(0x7000))
fd_names[0xB5] = named("mem_700C_xor_var", dbyte(0x7000))
fd_names[0xB6] = mem_700C_shift_left
# 0xB7 - 0xFF undocumented

jmp_cmds = [
    0x3A,
    0x3B,
    0x3C,
    0x3D,
    0x3E,
    0x3F,
    0xD2,
    0xD3,
    0xDC,
    0xDD,
    0xDE,
    0xD8,
    0xD9,
    0xDA,
    0xDB,
    0xDF,
    0xE0,
    0xE1,
    0xE2,
    0xE4,
    0xE3,
    0xE5,
    0xE6,
    0xE7,
    0xE8,
    0xEA,
    0xEB,
    0xEC,
    0xED,
    0xEE,
    0xEF,
    0xF8,
]

jmp_cmds_double = [0xE9]

jmp_cmds_fd = [0x3D, 0x3E]

def get_jump_args(line, args):
    if line[0] in jmp_cmds_double:
        return -2
    else:
        return -1

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

    def get_embedded_script(self, arr):
        if isinstance(arr, str):
            arr = eval(arr)
        commands_output = []
        a = tok(arr, 0, len(arr) - 1)
        offset = 0
        for line, _ in a:
            if line[0] == 0xFD:
                cmd = line[1]
                rest = line[2:]
                table = fd_names
                has_jump = cmd in jmp_cmds_fd
            else:
                cmd = line[0]
                rest = line[1:]
                table = names
                has_jump = (cmd in jmp_cmds) or (cmd in jmp_cmds_double)
            # print (f"0x{cmd:02X}", f"0x{offset:06X}", line)
            if table[cmd]:
                name, args = table[cmd](rest)
            else:
                name, args = "db", line
            if has_jump:
                arg_index = get_jump_args(line, args)
                jump_args = [ja for ja in args[arg_index:]]
            else:
                jump_args = []
            commands_output.append(
                {
                    "cmd": cmd,
                    "name": name,
                    "args": rest,
                    "parsed_args": args,
                    "has_jump": has_jump,
                    "original_offset": offset,
                    "jumps": jump_args,
                }
            )
            offset += len(line)
        return {
            "header": "OSCommand()",
            "commands": commands_output,
            "footer": ".fin()",
        }

    def handle(self, *args, **options):

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        scripts_data = []
        scripts = []
        ptrs = []

        for i in range(pointers["start"], pointers["end"], 2):
            ptrs.append((0x21 << 16) | (shortify(rom, i)))
        event_lengths = []
        for i in range(len(ptrs)):
            ptr = ptrs[i]
            if i < len(ptrs) - 1:
                event_lengths.append(ptrs[i + 1] - ptrs[i])
                script_content = tok(rom, ptrs[i], ptrs[i + 1] - 1)
            else:
                event_lengths.append(end - ptrs[i])
                script_content = tok(rom, ptrs[i], end)
            scripts.append(script_content)

        # translate lines into commands and note any jump addresses
        for i in range(len(scripts)):
            script = scripts[i]
            sd = []
            for j in range(len(script)):
                line, offset = script[j]
                name, args = parse_line(line, offset)
                identifier = "ACTION_%i_%s_%i" % (i, name, j)
                if (
                    line[0] in jmp_cmds
                    or line[0] in jmp_cmds_double
                    or (line[0] == 0xFD and line[1] in jmp_cmds_fd)
                ):
                    arg_index = get_jump_args(line, args)
                    jump_args = [(ja | (offset & 0xFF0000)) for ja in args[arg_index:]]
                else:
                    jump_args = []
                c = {
                    "command": name,
                    "args": args,
                    "original_offset": offset,
                    "identifier": identifier,
                    "jumps": jump_args,
                }
                sd.append(c)
            scripts_data.append(sd)

        scripts_with_named_jumps = []

        # get the identifiers corresponding to where the jumps are going
        for i in range(len(scripts_data)):
            script = scripts_data[i]
            this_script = []
            for cmd in script:
                jumps = []
                commands_to_replace = len(cmd["jumps"]) * -1
                for j in cmd["jumps"]:
                    for sd in scripts_data:
                        candidates = [c for c in sd if c["original_offset"] == j]
                        if len(candidates) > 0:
                            jumped_command = candidates[0]
                            jumps.append("%s" % jumped_command["identifier"])
                if commands_to_replace == 0:
                    new_args = cmd["args"]
                else:
                    new_args = cmd["args"][:commands_to_replace] + jumps
                cmd_with_named_jumps = {
                    "command": cmd["command"],
                    "args": new_args,
                    "identifier": cmd["identifier"],
                }
                this_script.append(cmd_with_named_jumps)
            scripts_with_named_jumps.append(this_script)

        return scripts_with_named_jumps
        # output (old)
        for i in range(len(scripts_with_named_jumps)):
            file = open("%s/script_%i.py" % (dest, i), "w")
            writeline(file, "# AUTOGENERATED DO NOT EDIT!!")
            writeline(
                file, "# Run the following command if you need to rebuild the table"
            )
            writeline(
                file,
                "# python manage.py objectsequencedisassembler --rom ROM > openmode_sequence_debug.txt",
            )
            writeline(
                file,
                "from randomizer.helpers.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags",
            )
            writeline(
                file,
                "from randomizer.helpers.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms",
            )
            script = scripts_with_named_jumps[i]
            if len(script) == 0:
                writeline(file, "script = []")
            else:
                writeline(file, "script = [")
                for j in range(len(script)):
                    cmd = script[j]
                    writeline(file, "    {")
                    writeline(file, '        "identifier": %r,' % cmd["identifier"])
                    if len(cmd["args"]) == 0:
                        writeline(file, '        "command": %r' % cmd["command"])
                    else:
                        writeline(file, '        "command": %r,' % cmd["command"])
                        writeline(file, '        "args": [%s]' % ", ".join(cmd["args"]))
                    if j == len(script) - 1:
                        writeline(file, "    }")
                    else:
                        writeline(file, "    },")
                writeline(file, "]")
            file.close()

        file = open("%s/actions.py" % dest, "w", encoding="utf-8")
        writeline(file, "# AUTOGENERATED DO NOT EDIT!!")
        writeline(file, "# Run the following command if you need to rebuild the table")
        writeline(
            file,
            "# python manage.py objectsequencedisassembler --rom ROM > openmode_sequence_debug.txt",
        )
        for i in range(len(scripts_data)):
            writeline(
                file,
                "from randomizer.data.actionscripts.script_%i import script as script_%i"
                % (i, i),
            )
        writeline(file, "scripts = [None]*%i" % len(scripts_data))
        for i in range(len(scripts_data)):
            writeline(file, "scripts[%i] = script_%i" % (i, i))
        file.close()
