# SPR0210_SPLASH_WATER_DROPLETS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL475_SPLASH_WATER_DROPLETS
sprite = CompleteSprite(
    animation=AnimationPack(358, length=124, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x04\x00\x04\x00\x04\x10\x0c \x1c\x00\x00\x00\x00\x00\x08\x00H\x00I\x00\x1a\x002\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00 \x00\x02\x00\x06\x00\x00\x00\x02\x00\x80\x00\x00\x00\x00\x10\x006\x00\x06\x00\x00\x00\x01\x00A\x00`\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            bytearray(b'\x00 \x00\x02\x00\x06\x00\x00\x00\x02\x00\x80\x00\x00\x00\x00\x10\x006\x00\x06\x00\x00\x00\x01\x00A\x00`\x00\x00\x00'),
                            bytearray(b'\x08\x06\x02\x04\x00\x00\x00\x18\x008\x000\x08\xc4\x04\xc8\x08\x00\x02\x00\x00\x00\x18\x00\x08\x00\x00\x00\xc8\x00\xc4\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                            bytearray(b'\x08\x06\x02\x04\x00\x00\x00\x18\x008\x000\x08\xc4\x04\xc8\x08\x00\x02\x00\x00\x00\x18\x00\x08\x00\x00\x00\xc8\x00\xc4\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x000\x00p\x00`\x02\x00\x07\x00\x02\x00\x18\x008\x000\x00\x10\x00\x00\x00\x02\x00\x05\x00\x02\x00\x10\x00(\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00F\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x06@\x06\xa0\x00@\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00F\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x06@\x06\xa0\x00@\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=112),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00F\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x06@\x06\xa0\x00@\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=114),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x04\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x02\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00F\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00\x06@\x06\xa0\x00@\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=117),
                    ]
                ),
            ],
            sequences=[
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
    palette_id=SPAL475_SPLASH_WATER_DROPLETS,
    palette_offset=0,
    unknown_num=0
)
