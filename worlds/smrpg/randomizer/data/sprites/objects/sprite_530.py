# SPR0530_STAT_BOOST_ARROWS

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL373_STAT_BOOST_ARROWS
sprite = CompleteSprite(
    animation=AnimationPack(214, length=347, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=367),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=367),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=366),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=366),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=366),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=366),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=365),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=365),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=118),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=364),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=364),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=123),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=117),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=363),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=363),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1e\x01=\x03=\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00?'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xf0\x00\xc08@\xb8\xa0\xd8p\x80\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\xf8\x00\xf8\x00\xf8\x00\xf0'),
                            bytearray(b'=\x02\x1d\x02\x0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x00\x1f\x00\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe8\x108\xe8\x80\xe0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x18\xf8\xf0\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=106),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=122),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x08\x01\x00\x1d\x006\x08.\x1e(\x18\x00\x00\x00\x00\x00\t\x00\x01\x00\x1d\x00>\x00>\x06>'),
                            bytearray(b'\x00\x00\xe0\x00\xd0 \x80@\xc0@\x84\x04\x00\x00\xe0\x00\x00\x00\x00\xe0\x00\xf00\xf00\xf0`\xe4\x04\x04\x00\xe0'),
                            bytearray(b'\x19\x08\x01\x00\x05\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1d\x00\x01\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\xc0p\xf0\xc0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\xf00\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=106),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=121),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=115),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=113),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=120),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b' \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\xf0``\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=114),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x04\x18\x04\x00\x08\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x08\x04\x1c\x1c\x1c\x08\x08\x00\x00'),
                            bytearray(b'\x00\x00@\x00\xa0`@\xc0@\x00\x84\x80`\x00\x80`\x00\x00\x00@\x00\xe0 \xe0@@\x04\x84\x00`\x10\xf0'),
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=106),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1e\x01=\x03=\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00?'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xf0\x00\xc08@\xb8\xa0\xd8p\x80\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\xf8\x00\xf8\x00\xf8\x00\xf0'),
                            bytearray(b'=\x02\x1d\x02\x0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x00\x1f\x00\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe8\x108\xe8\x80\xe0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x18\xf8\xf0\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08\x14\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x1c\x1c\x08\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@@\xa0\x00@\x00\x00\x00\x80\x00\x00@\x00\x00\x00\x00\x00@\xe0\xe0@@\x00\x00\x80\x80 ```\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=106),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=119),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=106),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x08\x01\x00\x1d\x006\x08.\x1e(\x18\x00\x00\x00\x00\x00\t\x00\x01\x00\x1d\x00>\x00>\x06>'),
                            bytearray(b'\x00\x00\xe0\x00\xd0 \x80@\xc0@\x84\x04\x00\x00\xe0\x00\x00\x00\x00\xe0\x00\xf00\xf00\xf0`\xe4\x04\x04\x00\xe0'),
                            bytearray(b'\x19\x08\x01\x00\x05\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1d\x00\x01\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\xc0p\xf0\xc0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\xf00\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=113),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=118),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x04\x18\x04\x00\x08\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x08\x04\x1c\x1c\x1c\x08\x08\x00\x00'),
                            bytearray(b'\x00\x00@\x00\xa0`@\xc0@\x00\x84\x80`\x00\x80`\x00\x00\x00@\x00\xe0 \xe0@@\x04\x84\x00`\x10\xf0'),
                            None,
                            bytearray(b' \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\xf0``\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=113),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x01\x07\x03\x0f\x07\x1f\x0f?\x1f\x7f?\x7f\x7f\x00\x01\x01\x02\x03\x04\x07\x08\x0f\x10\x1f ?@\x7f\x00'),
                            None,
                            bytearray(b'\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x07\x00\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x07\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=117),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08\x14\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x1c\x1c\x08\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@@\xa0\x00@\x00\x00\x00\x80\x00\x00@\x00\x00\x00\x00\x00@\xe0\xe0@@\x00\x00\x80\x80 ```\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1e\x01=\x03=\x03\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00\x1f\x00?\x00?'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xf0\x00\xc08@\xb8\xa0\xd8p\x80\x00\x00\x00\x00\x00\xe0\x00\xf0\x00\xf8\x00\xf8\x00\xf8\x00\xf0'),
                            bytearray(b'=\x02\x1d\x02\x0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00?\x00\x1f\x00\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe8\x108\xe8\x80\xe0\x00\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xf8\x18\xf8\xf0\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x08\x01\x00\x1d\x006\x08.\x1e(\x18\x00\x00\x00\x00\x00\t\x00\x01\x00\x1d\x00>\x00>\x06>'),
                            bytearray(b'\x00\x00\xe0\x00\xd0 \x80@\xc0@\x84\x04\x00\x00\xe0\x00\x00\x00\x00\xe0\x00\xf00\xf00\xf0`\xe4\x04\x04\x00\xe0'),
                            bytearray(b'\x19\x08\x01\x00\x05\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x1d\x00\x01\x00\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\xc0p\xf0\xc0@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\xf00\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x04\x18\x04\x00\x08\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x08\x04\x1c\x1c\x1c\x08\x08\x00\x00'),
                            bytearray(b'\x00\x00@\x00\xa0`@\xc0@\x00\x84\x80`\x00\x80`\x00\x00\x00@\x00\xe0 \xe0@@\x04\x84\x00`\x10\xf0'),
                            None,
                            bytearray(b' \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\xf0``\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08\x14\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x1c\x1c\x08\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@@\xa0\x00@\x00\x00\x00\x80\x00\x00@\x00\x00\x00\x00\x00@\xe0\xe0@@\x00\x00\x80\x80 ```\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
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
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL373_STAT_BOOST_ARROWS,
    palette_offset=0,
    unknown_num=8
)
