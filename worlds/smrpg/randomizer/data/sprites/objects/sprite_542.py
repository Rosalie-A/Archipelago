# SPR0542_BLINKING_YELLOW_LIGHT_CIRCLE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL380_BLINKING_YELLOW_LIGHT_CIRCLE
sprite = CompleteSprite(
    animation=AnimationPack(218, length=176, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x02\x03\x13\x1c\x1eap\x8f\xc0?\x80\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f\x7f\x7f\xff\xff'),
                            bytearray(b"\x03\x04\x06\t\x04\x0b\x1c\x13\x08\x17\x08\x178\'\x10/\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f"),
                            bytearray(b'\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x02\x03\x13\x1c\x1eap\x8f\xc0?\x80\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f\x7f\x7f\xff\xff'),
                            bytearray(b"\x03\x04\x06\t\x04\x0b\x1c\x13\x08\x17\x08\x178\'\x10/\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f"),
                            bytearray(b'\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x02\x03\x13\x1c\x1eap\x8f\xc0?\x80\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f\x7f\x7f\xff\xff'),
                            bytearray(b"\x03\x04\x06\t\x04\x0b\x1c\x13\x08\x17\x08\x178\'\x10/\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f"),
                            bytearray(b'\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x02\x03\x13\x1c\x1eap\x8f\xc0?\x80\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x1f\x1f\x7f\x7f\xff\xff'),
                            bytearray(b"\x03\x04\x06\t\x04\x0b\x1c\x13\x08\x17\x08\x178\'\x10/\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f"),
                            bytearray(b'\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x04\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x01\x08\x1b X\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x08\x04\x08\x10\x10\x00\x000 0\x00\x00\x00 \x00`\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00 \x00 \x00`\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=True, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x04\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x01\x08\x1b X\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x08\x04\x08\x10\x10\x00\x000 0\x00\x00\x00 \x00`\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00 \x00 \x00`\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x04\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x01\x08\x1b X\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x08\x04\x08\x10\x10\x00\x000 0\x00\x00\x00 \x00`\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00 \x00 \x00`\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x04\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x01\x08\x1b X\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x08\x04\x08\x10\x10\x00\x000 0\x00\x00\x00 \x00`\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00 \x00 \x00`\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x02\x00\x04\x00\x08\x00\x10\x00\x00 \x00\x00\x00\x00\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00 \x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=True, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x02\x00\x04\x00\x08\x00\x10\x00\x00 \x00\x00\x00\x00\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00 \x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=128),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x02\x00\x04\x00\x08\x00\x10\x00\x00 \x00\x00\x00\x00\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00 \x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x02\x00\x04\x00\x08\x00\x10\x00\x00 \x00\x00\x00\x00\x01\x00\x02\x00\x04\x00\x08\x00\x10\x00 \x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x01\x00\x03\x04\x08\x07\x10\x0f\x00? \x1f`\x1f\x00\x00\x01\x00\x01\x01\x07\x07\x0f\x0f\x1f\x1f\x1f\x1f\x7f?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x01\x00\x03\x04\x08\x07\x10\x0f\x00? \x1f`\x1f\x00\x00\x01\x00\x01\x01\x07\x07\x0f\x0f\x1f\x1f\x1f\x1f\x7f?'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x00\x03\x04\x08\x07\x10\x0f\x00? \x1f`\x1f\x00\x00\x01\x00\x01\x01\x07\x07\x0f\x0f\x1f\x1f\x1f\x1f\x7f?'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x03\x04\x08\x07\x10\x0f\x00? \x1f`\x1f\x00\x00\x01\x00\x01\x01\x07\x07\x0f\x0f\x1f\x1f\x1f\x1f\x7f?'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x01\x00\x04\x0c\x10\x00\x00   \x00\x00@\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x01\x00\x04\x0c\x10\x00\x00   \x00\x00@\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x00\x04\x0c\x10\x00\x00   \x00\x00@\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0c\x10\x00\x00   \x00\x00@\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x10\x10\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x10\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x10\x10\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x10\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x10\x10\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x10\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x10\x00\x00@@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x10\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL380_BLINKING_YELLOW_LIGHT_CIRCLE,
    palette_offset=0,
    unknown_num=8
)
