# SPR0192_COIN

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(324, length=490, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x10\x1f\x00\x1f\x00\x1f\x00?\x00\x00\x00\x07\x00\x08\x00\x03\x00\x07\x00\x1c\x00\x1c =\x00'),
                            bytearray(b'` \x08\x08\xcc\x04\xfc\x80|@"\x02\xb0\x000\x00 \xe0\x08\xf8\xc4<@<`\x9c.\xde>\xce>\xce'),
                            bytearray(b'?\x00?\x00\x1f\x00? \x1b\x00\x1b\x03\x0f\x00\x03\x02=\x00=\x00\x1f ? \x1b\x04\x18\x04\x0e\x01\x03\x04'),
                            bytearray(b'8\x000\x08\xb0\x00\xb2\x12\xa0\x00d\x84\xc8\x08  6\xce6\xce>\xce.\xce,\xdc|\x9c\xf88 \xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x04\x17\x00\x1f\t\x1e \x1e ?\x00<\x02\x00\x01\x06\x01\x01\x18\x00\x10\x12!\x10!\x00!\x00!'),
                            bytearray(b'\x80\x00p\x10\xf0\x00\xb8\x08\xf0\x00\x00\xc0\x00\xc0\xc0\x00@\xc0\x10\xf0\x80p\x88x\xc88888888'),
                            bytearray(b'\x14\n4\n5\n\x1d"9"\x1a\x03\x17\x00\x02\x00\x00!\x00!\x14!\x1c!8%\x08\x15\x05\x1a\x02\x05'),
                            bytearray(b'\xe0\x00\xc0 \x00\xc0\xc8\x08\x88\x08\x80\x00\x10\x10\xc0\xc0\x188\x18888\xf88\xb8x\xf0pp\xf0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x0e\x00\x1f\x00\x1f\x02\x1d\x00\x1d\x00\x1d\x00\x1d\x00\x00\x03\x06\t\x01\x10\x00\x10\x10\x02\x10\x02\x00\x02\x00\x02'),
                            bytearray(b'\x80\x00\x00\x00\x80\x00p\x00\xf0\x00\xc88\x88h\x88H\x00\x80 \xe0\x10\xf0\x00\xf0\x00p\x08x\x18x8x'),
                            bytearray(b'\x1d\x00\x1d\x00\x1d\x00\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x04\x01\x02\x00\x02\x10\x02\x10\x02\x10\x02\x08\x10\x0f\x10\x06\t'),
                            bytearray(b'\x88\x08\x88H\x88H\x88h\xc0 \x80@\x90\x10\xe0`xx8x8x\x18x\x90p\xb0pp\xf0`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x00\x07\x00\x0f\x04\x0f\x00\x0f\x00\x0e\x01\x0e\x01\x00\x03\x06\x01\x00\x01\x00\t\x0c\x01\x0c\x01\x04\x01\x04\x01'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\xc0\x00\xc0\x00 \xe0 \xa0  \x00\x80@\xc0 \xe0\x00\xc0\x00\xc0 \xe0`\xe0\xe0\xe0'),
                            bytearray(b'\n\x00\n\x01\n\x01\n\x01\x0b\x00\x0e\x01\x0e\x00\x05\x01\x01\x05\x00\x05\x08\x05\x08\x05\x08\x05\x00\t\x03\t\x05\x03'),
                            bytearray(b'       \xa0\x00\x80\x00\x00@@\x80\x80\xe0\xe0\xe0\xe0\xe0\xe0`\xe0@\xc0\xc0\xc0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x00\x07\x00\x0f\x04\x0f\x00\x0f\x00\x0e\x01\x0e\x01\x00\x03\x06\x01\x00\x01\x00\t\x0c\x01\x0c\x01\x04\x01\x04\x01'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\xc0\x00\xc0\x00 \xe0 \xa0  \x00\x80@\xc0 \xe0\x00\xc0\x00\xc0 \xe0`\xe0\xe0\xe0'),
                            bytearray(b'\n\x00\n\x01\n\x01\n\x01\x0b\x00\x0e\x01\x0e\x00\x05\x01\x01\x05\x00\x05\x08\x05\x08\x05\x08\x05\x00\t\x03\t\x05\x03'),
                            bytearray(b'       \xa0\x00\x80\x00\x00@@\x80\x80\xe0\xe0\xe0\xe0\xe0\xe0`\xe0@\xc0\xc0\xc0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x0e\x00\x1f\x00\x1f\x02\x1d\x00\x1d\x00\x1d\x00\x1d\x00\x00\x03\x06\t\x01\x10\x00\x10\x10\x02\x10\x02\x00\x02\x00\x02'),
                            bytearray(b'\x80\x00\x00\x00\x80\x00p\x00\xf0\x00\xc88\x88h\x88H\x00\x80 \xe0\x10\xf0\x00\xf0\x00p\x08x\x18x8x'),
                            bytearray(b'\x1d\x00\x1d\x00\x1d\x00\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x04\x01\x02\x00\x02\x10\x02\x10\x02\x10\x02\x08\x10\x0f\x10\x06\t'),
                            bytearray(b'\x88\x08\x88H\x88H\x88h\xc0 \x80@\x90\x10\xe0`xx8x8x\x18x\x90p\xb0pp\xf0`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x04\x17\x00\x1f\t\x1e \x1e ?\x00<\x02\x00\x01\x06\x01\x01\x18\x00\x10\x12!\x10!\x00!\x00!'),
                            bytearray(b'\x80\x00p\x10\xf0\x00\xb8\x08\xf0\x00\x00\xc0\x00\xc0\xc0\x00@\xc0\x10\xf0\x80p\x88x\xc88888888'),
                            bytearray(b'\x14\n4\n5\n\x1d"9"\x1a\x03\x17\x00\x02\x00\x00!\x00!\x14!\x1c!8%\x08\x15\x05\x1a\x02\x05'),
                            bytearray(b'\xe0\x00\xc0 \x00\xc0\xc8\x08\x88\x08\x80\x00\x10\x10\xc0\xc0\x188\x18888\xf88\xb8x\xf0pp\xf0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x10\x1f\x00\x1f\x00\x1f\x00?\x00\x00\x00\x07\x00\x08\x00\x03\x00\x07\x00\x1c\x00\x1c =\x00'),
                            bytearray(b'` \x08\x08\xcc\x04\xfc\x80|@"\x02\xb0\x000\x00 \xe0\x08\xf8\xc4<@<`\x9c.\xde>\xce>\xce'),
                            bytearray(b'?\x00?\x00\x1f\x00? \x1b\x00\x1b\x03\x0f\x00\x03\x02=\x00=\x00\x1f ? \x1b\x04\x18\x04\x0e\x01\x03\x04'),
                            bytearray(b'8\x000\x08\xb0\x00\xb2\x12\xa0\x00d\x84\xc8\x08  6\xce6\xce>\xce.\xce,\xdc|\x9c\xf88 \xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=133),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x10\x1f\x00\x1f\x00\x1f\x00?\x00\x00\x00\x07\x00\x08\x00\x03\x00\x07\x00\x1c\x00\x1c =\x00'),
                            bytearray(b'` \x08\x08\xcc\x04\xfc\x80|@"\x02\xb0\x000\x00 \xe0\x08\xf8\xc4<@<`\x9c.\xde>\xce>\xce'),
                            bytearray(b'?\x00?\x00\x1f\x00? \x1b\x00\x1b\x03\x0f\x00\x03\x02=\x00=\x00\x1f ? \x1b\x04\x18\x04\x0e\x01\x03\x04'),
                            bytearray(b'8\x000\x08\xb0\x00\xb2\x12\xa0\x00d\x84\xc8\x08  6\xce6\xce>\xce.\xce,\xdc|\x9c\xf88 \xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=136),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x04\x17\x00\x1f\t\x1e \x1e ?\x00<\x02\x00\x01\x06\x01\x01\x18\x00\x10\x12!\x10!\x00!\x00!'),
                            bytearray(b'\x80\x00p\x10\xf0\x00\xb8\x08\xf0\x00\x00\xc0\x00\xc0\xc0\x00@\xc0\x10\xf0\x80p\x88x\xc88888888'),
                            bytearray(b'\x14\n4\n5\n\x1d"9"\x1a\x03\x17\x00\x02\x00\x00!\x00!\x14!\x1c!8%\x08\x15\x05\x1a\x02\x05'),
                            bytearray(b'\xe0\x00\xc0 \x00\xc0\xc8\x08\x88\x08\x80\x00\x10\x10\xc0\xc0\x188\x18888\xf88\xb8x\xf0pp\xf0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=133),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=138),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x0e\x00\x1f\x00\x1f\x02\x1d\x00\x1d\x00\x1d\x00\x1d\x00\x00\x03\x06\t\x01\x10\x00\x10\x10\x02\x10\x02\x00\x02\x00\x02'),
                            bytearray(b'\x80\x00\x00\x00\x80\x00p\x00\xf0\x00\xc88\x88h\x88H\x00\x80 \xe0\x10\xf0\x00\xf0\x00p\x08x\x18x8x'),
                            bytearray(b'\x1d\x00\x1d\x00\x1d\x00\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x04\x01\x02\x00\x02\x10\x02\x10\x02\x10\x02\x08\x10\x0f\x10\x06\t'),
                            bytearray(b'\x88\x08\x88H\x88H\x88h\xc0 \x80@\x90\x10\xe0`xx8x8x\x18x\x90p\xb0pp\xf0`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=140),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x00\x07\x00\x0f\x04\x0f\x00\x0f\x00\x0e\x01\x0e\x01\x00\x03\x06\x01\x00\x01\x00\t\x0c\x01\x0c\x01\x04\x01\x04\x01'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\xc0\x00\xc0\x00 \xe0 \xa0  \x00\x80@\xc0 \xe0\x00\xc0\x00\xc0 \xe0`\xe0\xe0\xe0'),
                            bytearray(b'\n\x00\n\x01\n\x01\n\x01\x0b\x00\x0e\x01\x0e\x00\x05\x01\x01\x05\x00\x05\x08\x05\x08\x05\x08\x05\x00\t\x03\t\x05\x03'),
                            bytearray(b'       \xa0\x00\x80\x00\x00@@\x80\x80\xe0\xe0\xe0\xe0\xe0\xe0`\xe0@\xc0\xc0\xc0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=133),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=140),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=143),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x00\x07\x00\x0f\x04\x0f\x00\x0f\x00\x0e\x01\x0e\x01\x00\x03\x06\x01\x00\x01\x00\t\x0c\x01\x0c\x01\x04\x01\x04\x01'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\xc0\x00\xc0\x00 \xe0 \xa0  \x00\x80@\xc0 \xe0\x00\xc0\x00\xc0 \xe0`\xe0\xe0\xe0'),
                            bytearray(b'\n\x00\n\x01\n\x01\n\x01\x0b\x00\x0e\x01\x0e\x00\x05\x01\x01\x05\x00\x05\x08\x05\x08\x05\x08\x05\x00\t\x03\t\x05\x03'),
                            bytearray(b'       \xa0\x00\x80\x00\x00@@\x80\x80\xe0\xe0\xe0\xe0\xe0\xe0`\xe0@\xc0\xc0\xc0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=142),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=144),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x0e\x00\x1f\x00\x1f\x02\x1d\x00\x1d\x00\x1d\x00\x1d\x00\x00\x03\x06\t\x01\x10\x00\x10\x10\x02\x10\x02\x00\x02\x00\x02'),
                            bytearray(b'\x80\x00\x00\x00\x80\x00p\x00\xf0\x00\xc88\x88h\x88H\x00\x80 \xe0\x10\xf0\x00\xf0\x00p\x08x\x18x8x'),
                            bytearray(b'\x1d\x00\x1d\x00\x1d\x00\x1f\x00\x1f\x00\x1f\x00\x1f\x00\x0e\x04\x01\x02\x00\x02\x10\x02\x10\x02\x10\x02\x08\x10\x0f\x10\x06\t'),
                            bytearray(b'\x88\x08\x88H\x88H\x88h\xc0 \x80@\x90\x10\xe0`xx8x8x\x18x\x90p\xb0pp\xf0`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=138),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=144),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x04\x17\x00\x1f\t\x1e \x1e ?\x00<\x02\x00\x01\x06\x01\x01\x18\x00\x10\x12!\x10!\x00!\x00!'),
                            bytearray(b'\x80\x00p\x10\xf0\x00\xb8\x08\xf0\x00\x00\xc0\x00\xc0\xc0\x00@\xc0\x10\xf0\x80p\x88x\xc88888888'),
                            bytearray(b'\x14\n4\n5\n\x1d"9"\x1a\x03\x17\x00\x02\x00\x00!\x00!\x14!\x1c!8%\x08\x15\x05\x1a\x02\x05'),
                            bytearray(b'\xe0\x00\xc0 \x00\xc0\xc8\x08\x88\x08\x80\x00\x10\x10\xc0\xc0\x188\x18888\xf88\xb8x\xf0pp\xf0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=139),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=145),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x04\x0f\x00\x1f\x10\x1f\x00\x1f\x00\x1f\x00?\x00\x00\x00\x07\x00\x08\x00\x03\x00\x07\x00\x1c\x00\x1c =\x00'),
                            bytearray(b'` \x08\x08\xcc\x04\xfc\x80|@"\x02\xb0\x000\x00 \xe0\x08\xf8\xc4<@<`\x9c.\xde>\xce>\xce'),
                            bytearray(b'?\x00?\x00\x1f\x00? \x1b\x00\x1b\x03\x0f\x00\x03\x02=\x00=\x00\x1f ? \x1b\x04\x18\x04\x0e\x01\x03\x04'),
                            bytearray(b'8\x000\x08\xb0\x00\xb2\x12\xa0\x00d\x84\xc8\x08  6\xce6\xce>\xce.\xce,\xdc|\x9c\xf88 \xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=125),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=123),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=126),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=119),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=124),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=134),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=128),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=139),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=133),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=133),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=142),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=107, y=136),
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
                AnimationSequence(
                    frames=[
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
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=23),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=0,
    unknown_num=0
)
