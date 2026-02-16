# SPR0771_EGG

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL393_EGG
sprite = CompleteSprite(
    animation=AnimationPack(228, length=147, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x02\x07\x04\x0f\x00\x1f\x00?\x00?\x00\x7f\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00'),
                            bytearray(b'\x00\x00\xa0\xe0\xf0\x0c\xf6\x0c\xf4\r\xed\x1d\xea\x19\xda9\x00\x00\x10\x08\x00\x00\x02\x00\x02\x01\x03\x00\x07\x00\x07\x00'),
                            bytearray(b'\x7f\x00\xff\x80~\x81\xfc\x83y\x07;\x076?\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\x00!\x00\x00\x00'),
                            bytearray(b'\x96p<\xf3h\xe4\xd0\xc8\xa0\x90\x00P\x00@\x00\x00\x0e\x01\x0e\x01\x1c\x028\x04p\x08\xc00\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x02\x0f\x00\x1f\x00\x7f\x00\xff\x00\xff\x00\x00\x00\x00\x00\x03\x00\x08\x00\x00 @\x00\x80\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00X\xc0\xf4\x08\xe6\x1c\xc99\xd8< \xf0\x00\x00\x00\x000\x08\x04\x00\x02\x00\x07\x00\x03\x00\x0f\x00'),
                            bytearray(b'\xfe\x01\xe0\x9f\x03?\x1c\x1c\x0f\x00\x02\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00@\x03 \x07\x08\x00\x03\x00\x00\x00\x00'),
                            bytearray(b'b\xe1\xcd\xc3\x13\x0e*\x18\xa8d@0\x00\x00\x00\x00\x1f\x00?\x00\xfe\x01\xf8\x06\xe0\x1c\x00\xf0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x02\x07\x04\x0f\x00\x1f\x00?\x00?\x00\x7f\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00'),
                            bytearray(b'\x00\x00\xa0\xe0\xf0\x0c\xf6\x0c\xf4\r\xed\x1d\xea\x19\xda9\x00\x00\x10\x08\x00\x00\x02\x00\x02\x01\x03\x00\x07\x00\x07\x00'),
                            bytearray(b'\x7f\x00\xff\x80~\x81\xfc\x83y\x07;\x076?\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\x00!\x00\x00\x00'),
                            bytearray(b'\x96p<\xf3h\xe4\xd0\xc8\xa0\x90\x00P\x00@\x00\x00\x0e\x01\x0e\x01\x1c\x028\x04p\x08\xc00\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x02\x07\x00\x0f\x00\x0f\x00\x1f\x00\x1f\x00\x1f\x00\x1f \x02\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00  \x00\x00\x00'),
                            bytearray(b'\x80@\xe0\x00\xf0\x00\xf0\x08\xf0\x08\xe8\x1c\xc88\x90p@\x00 \x00\x10\x00\x00\x08\x08\x00\x00\x04\x00\x04\x0c\x00'),
                            bytearray(b'\x1f \x00?3??\x1f\x00\x00\x0f\x10\x08\x0f\x02\x06\x00\x00\x00\x00\x00\x00 \x00\x1f \x1f\x00\x0f\x00\x02\x05'),
                            bytearray(b'p\xf0\xe4\xe0\xcc\xc0\x10\x08`\x14\xd00p\xe0@ \x0c\x00\x1c\x00<\x00\xf8\x04\xf0\x0c\xf0\x08\xe0\x10\x00\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x02\x07\x04\x0f\x00\x1f\x00?\x00?\x00\x7f\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00'),
                            bytearray(b'\x00\x00\xa0\xe0\xf0\x0c\xf6\x0c\xf4\r\xed\x1d\xea\x19\xda9\x00\x00\x10\x08\x00\x00\x02\x00\x02\x01\x03\x00\x07\x00\x07\x00'),
                            bytearray(b'\x7f\x00\xff\x80~\x81\xfc\x83y\x07;\x076?\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\x00!\x00\x00\x00'),
                            bytearray(b'\x96p<\xf3h\xe4\xd0\xc8\xa0\x90\x00P\x00@\x00\x00\x0e\x01\x0e\x01\x1c\x028\x04p\x08\xc00\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x02\x0f\x00\x1f\x00\x7f\x00\xff\x00\xff\x00\x00\x00\x00\x00\x03\x00\x08\x00\x00 @\x00\x80\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00X\xc0\xf4\x08\xe6\x1c\xc99\xd8< \xf0\x00\x00\x00\x000\x08\x04\x00\x02\x00\x07\x00\x03\x00\x0f\x00'),
                            bytearray(b'\xfe\x01\xe0\x9f\x03?\x1c\x1c\x0f\x00\x02\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00@\x03 \x07\x08\x00\x03\x00\x00\x00\x00'),
                            bytearray(b'b\xe1\xcd\xc3\x13\x0e*\x18\xa8d@0\x00\x00\x00\x00\x1f\x00?\x00\xfe\x01\xf8\x06\xe0\x1c\x00\xf0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x02\x07\x04\x0f\x00\x1f\x00?\x00?\x00\x7f\x00\x00\x00\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00'),
                            bytearray(b'\x00\x00\xa0\xe0\xf0\x0c\xf6\x0c\xf4\r\xed\x1d\xea\x19\xda9\x00\x00\x10\x08\x00\x00\x02\x00\x02\x01\x03\x00\x07\x00\x07\x00'),
                            bytearray(b'\x7f\x00\xff\x80~\x81\xfc\x83y\x07;\x076?\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\x00!\x00\x00\x00'),
                            bytearray(b'\x96p<\xf3h\xe4\xd0\xc8\xa0\x90\x00P\x00@\x00\x00\x0e\x01\x0e\x01\x1c\x028\x04p\x08\xc00\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x02\x07\x00\x0f\x00\x0f\x00\x1f\x00\x1f\x00\x1f\x00\x1f \x02\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00  \x00\x00\x00'),
                            bytearray(b'\x80@\xe0\x00\xf0\x00\xf0\x08\xf0\x08\xe8\x1c\xc88\x90p@\x00 \x00\x10\x00\x00\x08\x08\x00\x00\x04\x00\x04\x0c\x00'),
                            bytearray(b'\x1f \x00?3??\x1f\x00\x00\x0f\x10\x08\x0f\x02\x06\x00\x00\x00\x00\x00\x00 \x00\x1f \x1f\x00\x0f\x00\x02\x05'),
                            bytearray(b'p\xf0\xe4\xe0\xcc\xc0\x10\x08`\x14\xd00p\xe0@ \x0c\x00\x1c\x00<\x00\xf8\x04\xf0\x0c\xf0\x08\xe0\x10\x00\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL393_EGG,
    palette_offset=0,
    unknown_num=8
)
