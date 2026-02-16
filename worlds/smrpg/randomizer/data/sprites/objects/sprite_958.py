# SPR0958_TINY_GLOWING_PIXEL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL765_TINY_GLOWING_PIXEL
sprite = CompleteSprite(
    animation=AnimationPack(443, length=135, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x00\x00\x10\x00\x10\x10\x10\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=129),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x06\x06\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=127),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x06\x06\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x06\x06\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x06\x06\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x00\x00\x00\x10\x00\x00\x10\x00\x10\x10\x10\x10\x10\x10\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=129),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x05\x06\x06\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=127),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x05\x06\x06\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x05\x06\x06\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x05\x06\x06\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x01\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x05\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=127),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x05\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x05\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x05\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b"\x00\x00\x01\x01\x0f\x0f\x1e\x1f3<\x16\x18\';+3\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00\x1f\x03<\x03<"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=127),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b"\x00\x00\x01\x01\x0f\x0f\x1e\x1f3<\x16\x18\';+3\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00\x1f\x03<\x03<"),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b"\x00\x00\x01\x01\x0f\x0f\x1e\x1f3<\x16\x18\';+3\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00\x1f\x03<\x03<"),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x01\x0f\x0f\x1e\x1f3<\x16\x18\';+3\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00\x1f\x03<\x03<"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x01\x01\x1b\x1b\x1f\x1f>?0?1>#<c|\x00\x01\x00\x1b\x00\x1f\x00?\x00?\x00?\x00?\x00\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=127),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x01\x01\x1b\x1b\x1f\x1f>?0?1>#<c|\x00\x01\x00\x1b\x00\x1f\x00?\x00?\x00?\x00?\x00\x7f'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x01\x1b\x1b\x1f\x1f>?0?1>#<c|\x00\x01\x00\x1b\x00\x1f\x00?\x00?\x00?\x00?\x00\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x1b\x1b\x1f\x1f>?0?1>#<c|\x00\x01\x00\x1b\x00\x1f\x00?\x00?\x00?\x00?\x00\x7f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL765_TINY_GLOWING_PIXEL,
    palette_offset=0,
    unknown_num=8
)
