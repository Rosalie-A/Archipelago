# SPR0172_GENO_DOLL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL685_GENO_WALKING_DOWN_LEFT
sprite = CompleteSprite(
    animation=AnimationPack(279, length=189, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x08\x0b\x06\x07\x02\x02\x03\x00\x01\t\x00\x00\x00\x01\x03\x00\x03\x0f\t\x07\x0c\x0b\x0f\x05\x06\x08'),
                            bytearray(b'\x10`P\xd0 \xe0P\xc0\xd0\xc0 \x10\xc0\x00\x10\x10`\x10\xd00\xe0\x00@\xb0@0\x08\xe8p@\xf00'),
                            bytearray(b'\x08\x00\x05\x05\x08\x08\x06\x06\x01\x00\x01\x01\x06\x06\x01\x01\x07\x0b\x06\x18\x0f\x12\x03\x02\x03\x02\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\x90\xc0\xe4 $\xe0p\xe0Pp\xc0\xc0@@\xc0\xc0 X \xfc\xe0\x1c\xe0\x10\xc0@@@\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x07\x02\x02\x03\x03\x07\x03\x04\x04\x15\x01\x00\x00\x01\x02\x03\x04\x02\x05\x03\x04\x03\x04\x00\x03\x06\x18'),
                            bytearray(b'\x00\x00\x80\x80 \xe0\x80\xe0p`\xe0 \xf0H\xb0\x90\x00\x00\x00@\xe0\x00\xe0\x00`\x90 \xd0@\xf8p\x10'),
                            bytearray(b'\x0b\x01\x15\x07\x15\x07\x05\x03\x07\x06\x06\x06\x05\x00\x03\x03\x01\x0f\x07\x18\x07\x18\x07\x08\x03\x00\x07\x06\x07\x00\x03\x03'),
                            bytearray(b'\xf8\xd8\xe8\xe0\x98\x80\xb0\x80\xc0@\x00\x00\xe0`\x80\x80\xd8\xf8\xe0\x18\x80x\x80\xf0\x80\x00\xc0\xc0\xe0`\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x08\x0b\x06\x07\x02\x02\x03\x00\x01\t\x00\x00\x00\x01\x03\x00\x03\x0f\t\x07\x0c\x0b\x0f\x05\x06\x08'),
                            bytearray(b'\x10`P\xd0 \xe0P\xc0\xd0\xc0 \x10\xc0\x00\x10\x10`\x10\xd00\xe0\x00@\xb0@0\x08\xe8p@\xf00'),
                            bytearray(b'\x08\x00\x05\x05\t\t\t\x0f\x01\x07\x01\x01\x06\x06\x01\x01\x07\x0b\x07\x1b\x0e\x14\x08\x08\x00\x00\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\x90\xc0\xe4 $`\xf0\xe0\xc0\xc0@@@@\xc0\xc0 X \xfc\xe0\x1c`\x10\xc0\xc0\xc0@\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00<\x00f\x00B\x00B\x00f\x00<\x00\x00\x00\x00\x00$$BB\x00\x00\x00\x00BB$$\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x08\x0b\x06\x07\x02\x02\x03\x00\x01\t\x00\x00\x00\x01\x03\x00\x03\x0f\t\x07\x0c\x0b\x0f\x05\x06\x08'),
                            bytearray(b'\x10`P\xd0 \xe0P\xc0\xd0\xc0 \x10\xc0\x00\x10\x10`\x10\xd00\xe0\x00@\xb0@0\x08\xe8p@\xf00'),
                            bytearray(b'\x08\x00\x05\x05\t\t\x0f\x0f\x05\x05\x01\x01\x06\x06\x01\x01\x07\x0b\x07\x1b\x0e\x14\x0c\x0c\x06\x04\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\x90\xc0\xe4 $`\xf0\xe0\xc0\xc0@@@@\xc0\xc0 X \xfc\xe0\x1c`\x10\xc0\xc0\xc0@\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<\x00f\x00\xc3\x00\x81\x00\x81\x00\xc3\x00f\x00<\x00\x00\x00$$BB\x00\x00\x00\x00BB$$\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x08\x0b\x06\x07\x02\x02\x03\x00\x01\t\x00\x00\x00\x01\x03\x00\x03\x0f\t\x07\x0c\x0b\x0f\x05\x06\x08'),
                            bytearray(b'\x10`P\xd0 \xe0P\xc0\xd0\xc0 \x10\xc0\x00\x10\x10`\x10\xd00\xe0\x00@\xb0@0\x08\xe8p@\xf00'),
                            bytearray(b'\x08\x00\x05\x05\t\t\x0f\x0f\x05\x05\x01\x01\x06\x06\x01\x01\x07\x0b\x07\x1b\x0e\x14\x0c\x0c\x06\x04\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\x90\xc0\xe4 $`\xf0\xe0\xc0\xc0@@@@\xc0\xc0 X \xfc\xe0\x1c`\x10\xc0\xc0\xc0@\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x18\x00<\x00<\x00\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x04\x04\x14\x14\x18\x18\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\x0c\x00\x1e\x00\x1e\x00\x0c\x00\x00\x00\x00\x00\x00\x00@@\x04\x04\x12\x12\x14\x14\x0c\x0c\x00\x00'),
                            bytearray(b'p\x00 \x00\x00\x00\x06\x00\x0f\x00\x0f\x00\x06\x00\x00\x00PP  \x00\x00\x02\x02\x01\x01\x07\x07\x06\x06\x00\x00'),
                            bytearray(b'\x00\x00\x04\x00\x0c\x00\x0c\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x08\x08\x04\x04  \x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x08\x0b\x06\x07\x02\x02\x03\x00\x01\t\x00\x00\x00\x01\x03\x00\x03\x0f\t\x07\x0c\x0b\x0f\x05\x06\x08'),
                            bytearray(b'\x10`P\xd0 \xe0P\xc0\xd0\xc0 \x10\xc0\x00\x10\x10`\x10\xd00\xe0\x00@\xb0@0\x08\xe8p@\xf00'),
                            bytearray(b'\x08\x00\x05\x05\t\t\x0f\x0f\x05\x05\x01\x01\x06\x06\x01\x01\x07\x0b\x07\x1b\x0e\x14\x0c\x0c\x06\x04\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\x90\xc0\xe4 $`\xf0\xe0\xc0\xc0@@@@\xc0\xc0 X \xfc\xe0\x1c`\x10\xc0\xc0\xc0@\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x08\x0b\x06\x07\x02\x02\x03\x00\x01\t\x00\x00\x00\x01\x03\x00\x03\x0f\t\x07\x0c\x0b\x0f\x05\x06\x08'),
                            bytearray(b'\x10`P\xd0 \xe0P\xc0\xd0\xc0 \x10\xc0\x00\x10\x10`\x10\xd00\xe0\x00@\xb0@0\x08\xe8p@\xf00'),
                            bytearray(b'\x08\x00\x05\x05\t\t\x0f\x0f\x05\x05\x01\x01\x06\x06\x01\x01\x07\x0b\x07\x1b\x0e\x14\x0c\x0c\x06\x04\x07\x07\x07\x07\x01\x01'),
                            bytearray(b'\x90\xc0\xe4 $`\xf0\xe0\xc0\xc0@@@@\xc0\xc0 X \xfc\xe0\x1c`\x10\xc0\xc0\xc0@\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00  0\xf00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x008\x00, <\xf08\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\xc0\x10\xf0pp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\xc0\x18\xf0|p|\x008\x00\x00\x00\x00\x00\x00\x000\x00\x00\x00\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                    ]
                ),
                Mold(11, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x00\x00\x00\x00\x06\x06\x13\x1e\x03\x1e20pp\xe1\xe0\x00\x00\x00\x00\x06\x08\x1e\x01\x1e!0Op\x8f\xe0\x1f'),
                            None,
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x01\x00\x00\x01\x01\x00\x00\x00\x02\x00\x01\x00\x02\x01\x03\x00\x03\x00\x00\x01\x00\x01\x00\x01\x00\x03'),
                            bytearray(b'\'`\xc7p\xefc_F" f\x81\x98\r\x9f\x90\xe0_\x987\x93\x0f\xa7^\xff%~\x992\xc5\xe0O'),
                            bytearray(b'\x80\x00\x80\x80\x80\x80\x00\x00\xe0\xc0\xf0\x80\x90\x00\x08\x00\x00\x80@@@@\xc0@\xc0\xe0\x80\xf0\x00\xf0\x00\xf8'),
                            bytearray(b'\x02\x00\x13\x12\x11\x11\x12\x12\x12\x12\x0e\x0e\x02\x02\x01\x01\x0c\x03\x1e\x1f\x1f\x1f\x1f\x1e\x1f\x1f\x0f\x0f\x03\x03\x01\x01'),
                            bytearray(b'\xc1\x8f\xeb\x9f\xa3\xa7\x7fr6\x16?\x0f11\xc0\xc0\xff\xa0\xef\x80\xff\xa0\xffr\xef\xc6\xfe\xce\xf1\xf1\xc0\xc0'),
                            bytearray(b'\x18\x00\xa0\x80\xe0\xa0p0\xb00``\xc0\xc0\x00\x00\x00\xf8\x80`\xa0`p\xb0\xd0\x10\xa0 \xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL685_GENO_WALKING_DOWN_LEFT,
    palette_offset=0,
    unknown_num=0
)
