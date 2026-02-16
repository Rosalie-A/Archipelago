from types import SimpleNamespace

_0x08_flags = {
    3: 'READ_AS_MOLD',
    4: 'LOOPING_OFF',
    6: 'READ_AS_SEQUENCE',
    15: 'MIRROR_SPRITE',
}

_0x08Flags = SimpleNamespace()
for i in _0x08_flags:
    setattr(_0x08Flags, _0x08_flags[i], i)

_0x0A_flags = {
    0: 'BIT_0',
    1: 'CANT_WALK_UNDER',
    2: 'CANT_PASS_WALLS',
    3: 'CANT_JUMP_THROUGH',
    4: 'BIT_4',
    5: 'CANT_PASS_NPCS',
    6: 'CANT_WALK_THROUGH',
    7: 'BIT_7'
}

_0x0AFlags = SimpleNamespace()
for i in _0x0A_flags:
    setattr(_0x0AFlags, _0x0A_flags[i], i)

_0x10_flags = {
    0: 'WALKING',
    1: 'SEQUENCE'
}

_0x10Flags = SimpleNamespace()
for i in _0x10_flags:
    setattr(_0x10Flags, _0x10_flags[i], i)

sequence_speed_table = {
    0: 'NORMAL',
    1: 'FAST',
    2: 'FASTER',
    3: 'VERY_FAST',
    4: 'FASTEST',
    5: 'SLOW',
    6: 'VERY_SLOW'
}

SequenceSpeeds = SimpleNamespace()
for i in sequence_speed_table:
    setattr(SequenceSpeeds, sequence_speed_table[i], i)

vram_priority_table = {
    0: 'MARIO_OVERLAPS_ON_ALL_SIDES',
    1: 'NORMAL',
    2: 'OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES',
    3: 'PRIORITY_3'
}

VramPriority = SimpleNamespace()
for i in vram_priority_table:
    setattr(VramPriority, vram_priority_table[i], i)
