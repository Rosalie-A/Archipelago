# SPR0211_SMALL_FROG_COIN

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(325, length=413, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x01\x0e\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x00\x00\x08\x0e\x01\x0c\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00` 0\x10\xf0\x10\xc8\x88h\x08\x00\x00\x00\x00\x00\x00 \xe0\x10\xf0\x90p\xf88X\xb8'),
                            bytearray(b'\x0f\x00\x0f\x00\x07\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x01\x0c\x01\x06\t\x06\x01\x01\x02\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x08h\x08xX0\x10` \x00\x00\x00\x00\x00\x00X\xb8X\xb8\x18\xb8\x10\xf0 \xe0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x06\x00\x07\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x01\x01\x08\n\x01\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80@\xc0 \x10p\x90P\x10\xd0\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x10\xf0\xb0p0p'),
                            bytearray(b'\t\x06\t\x06\r\x02\r\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x0c\x01\x04\t\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x90P\x90P\x90P  @@\x00\x00\x00\x00\x00\x000p0p\xb0p`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x06\x02\r\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\r\x00\t\x08\x02\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00 \xa0\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0 \xe0`\xe0'),
                            bytearray(b'\r\x00\r\x00\x0f\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x08\x02\x01\n\x02\x05\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'   \xa0 \xa0  @@\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0\x00\xc0@\xc0'),
                            bytearray(b'\x03\x00\x03\x00\x03\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x00\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x80\x00\x80\x00\x00@@\x00\x00\x00\x00\x00\x00@\xc0@\xc0@\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0\x00\xc0@\xc0'),
                            bytearray(b'\x03\x00\x03\x00\x03\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x00\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x80\x00\x80\x00\x00@@\x00\x00\x00\x00\x00\x00@\xc0@\xc0@\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x06\x02\r\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\r\x00\t\x08\x02\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00 \xa0\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0 \xe0`\xe0'),
                            bytearray(b'\r\x00\r\x00\x0f\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x08\x02\x01\n\x02\x05\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'   \xa0 \xa0  @@\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x06\x00\x07\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x01\x01\x08\n\x01\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80@\xc0 \x10p\x90P\x10\xd0\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x10\xf0\xb0p0p'),
                            bytearray(b'\t\x06\t\x06\r\x02\r\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x0c\x01\x04\t\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x90P\x90P\x90P  @@\x00\x00\x00\x00\x00\x000p0p\xb0p`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x01\x0e\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x00\x00\x08\x0e\x01\x0c\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00` 0\x10\xf0\x10\xc8\x88h\x08\x00\x00\x00\x00\x00\x00 \xe0\x10\xf0\x90p\xf88X\xb8'),
                            bytearray(b'\x0f\x00\x0f\x00\x07\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x01\x0c\x01\x06\t\x06\x01\x01\x02\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x08h\x08xX0\x10` \x00\x00\x00\x00\x00\x00X\xb8X\xb8\x18\xb8\x10\xf0 \xe0\x00\x00\x00\x00\x00\x00'),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=131),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x01\x0e\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x00\x00\x08\x0e\x01\x0c\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00` 0\x10\xf0\x10\xc8\x88h\x08\x00\x00\x00\x00\x00\x00 \xe0\x10\xf0\x90p\xf88X\xb8'),
                            bytearray(b'\x0f\x00\x0f\x00\x07\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x01\x0c\x01\x06\t\x06\x01\x01\x02\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x08h\x08xX0\x10` \x00\x00\x00\x00\x00\x00X\xb8X\xb8\x18\xb8\x10\xf0 \xe0\x00\x00\x00\x00\x00\x00'),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=133),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x06\x00\x07\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x01\x01\x08\n\x01\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80@\xc0 \x10p\x90P\x10\xd0\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x10\xf0\xb0p0p'),
                            bytearray(b'\t\x06\t\x06\r\x02\r\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x0c\x01\x04\t\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x90P\x90P\x90P  @@\x00\x00\x00\x00\x00\x000p0p\xb0p`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=135),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x06\x02\r\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\r\x00\t\x08\x02\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00 \xa0\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0 \xe0`\xe0'),
                            bytearray(b'\r\x00\r\x00\x0f\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x08\x02\x01\n\x02\x05\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'   \xa0 \xa0  @@\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=133),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=137),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0\x00\xc0@\xc0'),
                            bytearray(b'\x03\x00\x03\x00\x03\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x00\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x80\x00\x80\x00\x00@@\x00\x00\x00\x00\x00\x00@\xc0@\xc0@\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=135),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=141),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80@\xc0\x00\xc0\x00\xc0@\xc0'),
                            bytearray(b'\x03\x00\x03\x00\x03\x00\x03\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x03\x00\x00\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x80\x00\x80\x00\x00@@\x00\x00\x00\x00\x00\x00@\xc0@\xc0@\xc0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=144),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x06\x02\r\x00\r\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\r\x00\t\x08\x02\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\xc0\x00\xc0\x00 \xa0\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0 \xe0`\xe0'),
                            bytearray(b'\r\x00\r\x00\x0f\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x08\x02\x01\n\x02\x05\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'   \xa0 \xa0  @@\x00\x00\x00\x00\x00\x00\xe0\xe0`\xe0`\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=139),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x06\x00\x07\x00\x0e\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x01\x01\x08\n\x01\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80@\xc0 \x10p\x90P\x10\xd0\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x10\xf0\xb0p0p'),
                            bytearray(b'\t\x06\t\x06\r\x02\r\x02\x04\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x0c\x01\x04\t\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x90P\x90P\x90P  @@\x00\x00\x00\x00\x00\x000p0p\xb0p`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=134),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x07\x01\x0e\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x03\x05\x00\x00\x08\x0e\x01\x0c\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00` 0\x10\xf0\x10\xc8\x88h\x08\x00\x00\x00\x00\x00\x00 \xe0\x10\xf0\x90p\xf88X\xb8'),
                            bytearray(b'\x0f\x00\x0f\x00\x07\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x0c\x01\x0c\x01\x06\t\x06\x01\x01\x02\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x08h\x08xX0\x10` \x00\x00\x00\x00\x00\x00X\xb8X\xb8\x18\xb8\x10\xf0 \xe0\x00\x00\x00\x00\x00\x00'),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=122),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=119),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=121),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=125),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=125),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x08\x00\x1c\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x14\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=128),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=133),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=133),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=139),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=139),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x08*\x14\x00\x08\x08\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00"\x00\x00\x00\x08\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=141),
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
    palette_offset=2,
    unknown_num=0
)
