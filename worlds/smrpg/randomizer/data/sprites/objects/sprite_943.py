# SPR0943_BOOSTER_RIDING_TRAIN

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL735_BOOSTER_RIDING_TRAIN
sprite = CompleteSprite(
    animation=AnimationPack(428, length=272, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00``\x90`\x90\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x00\x01\x03\x02\x01\x01\x0b\t\x0b\x0b\x04\x07\x03\x04\x00\x00\x01\x01\x03\x00\x01\x03\x04\x01\x07\x03\x05\x04\x07\x00'),
                            bytearray(b' \x80`\x80\xa0@\xb0\xd0\xb8\xf8\xf0\xf0p\xf0\xf0p\x00 \x80\xa0\x00 \xf0\xd0\xb8\xf8\xf0\xf0pp\xf0p'),
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00<\x18d<B8F\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x02\x01\x00\x03\x07\x04\x03\x03\x0b\t\x0b\x0b\x00\x07\x00\x00\x00\x00\x03\x03\x06\x00\x03\x07\x04\x01\x07\x03\x05\x00'),
                            bytearray(b'\x00\x00@\x00\xc0\x00`\xa0x\xb8\xb0\xf0\xf0\xf0p\xf0\x00\x00\x00@\x00@ `\xf8\xb8\xb0\xf0\xf0\xf0pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x06\x06\t\x06\t\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x00\x01\x03\x02\x01\x01\x0b\t\x0b\x0b\x04\x07\x03\x04\x00\x00\x01\x01\x03\x00\x01\x03\x04\x01\x07\x03\x05\x04\x07\x00'),
                            bytearray(b' \x80`\x80\xa0@\xb0\xd0\xb8\xf8\xf0\xf0p\xf0\xf0p\x00 \x80\xa0\x00 \xf0\xd0\xb8\xf8\xf0\xf0pp\xf0p'),
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x02\x02\x05\x00\x02\x00\x00\x00\x00\x00@@\xa0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x02\x01\x00\x03\x07\x04\x03\x03\x0b\t\x0b\x0b\x00\x07\x00\x00\x00\x00\x03\x03\x06\x00\x03\x07\x04\x01\x07\x03\x05\x00'),
                            bytearray(b'\x00\x00@\x00\xc0\x00`\xa0x\xb8\xb0\xf0\xf0\xf0p\xf0\x00\x00\x00@\x00@ `\xf8\xb8\xb0\xf0\xf0\xf0pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x00\x01\x03\x02\x01\x01\x0b\t\x0b\x0b\x04\x07\x03\x04\x00\x00\x01\x01\x03\x00\x01\x03\x04\x01\x07\x03\x05\x04\x07\x00'),
                            bytearray(b' \x80`\x80\xa0@\xb0\xd0\xb8\xf8\xf0\xf0p\xf0\xf0p\x00 \x80\xa0\x00 \xf0\xd0\xb8\xf8\xf0\xf0pp\xf0p'),
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\t\x00\x18\x01\x17\t\x07\x07\x0f\r\x1e\x1e\x08\x0f\x1b\x1c\x00\x00\x01\x11\x03\x10\x07\x07\x08\x0c\x1f\x1e\r\x08\x1f\x18'),
                            bytearray(b'\x10\x80\x18\xc0\xe8\x90\xf0\xf0\xf0\xb0xx\x10\xf0\xf8\x18\x00\x00\xc0\xc8\xc0\x08\xf0\xf0\x100\xf8xP\x10\xf8\x18'),
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00\x03\x00\x02\x01\x06\x05\x0e\x0f\x07\x07\x07\x07\x07\x07\x00\x02\x00\x02\x00\x02\x07\x05\x0e\x0f\x07\x07\x07\x07\x07\x07'),
                            bytearray(b'@\x80\x00\xc0\xe0 \xc0\xc0\xe8\xc8\xe8\xe8\x10\xf0\xe0\x10\x00\x00\xc0\xc0`\x00\xc0\xe0\x90\xc0\xf0\xe0P\x10\xf0\x00'),
                            bytearray(b'\x0f\x0f)7/6v\x1b\x0f\xca\x07\x87\x00\x00\x00\x00\x0f\x0f\x007\x017&2MH\x86\x86\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xf8\xe0@\x90\x00\xc00\xf0\xf0\xc0@\x00\x00\x00\x00\xf8\xf8\xe0\xc0\xf0\x00\x00\x00\xf0\xf0\xc0@\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x01\x06\x01\x05\x02\r\x0b\x1d\x1f\x0f\xef\x1e\xef\xff\xee\x00\x04\x01\x05\x00\x04\x0f\x0b\x1d\x1f\x0f\xef\x0e\xee\x07\xee'),
                            bytearray(b'\x80\x00\x00\x80\xc0@\x80\x80\xd0\x90\xd0\xd0 \xe0\xc0 \x00\x00\x80\x80\xc0\x00\x80\xc0 \x80\xe0\xc0\xa0 \xe0\x00'),
                            bytearray(b"\'_\x0f\x03\t\x00\x07\t\x0f\x0e\x01\x01\x00\x00\x00\x00\x03\x0f\x0f\x0f\x0f\x00\x01\x01\x0f\x0e\x01\x01\x00\x00\x00\x00"),
                            bytearray(b'\xf0\xf0\xe0\xe0\xc0@\xe0\xc0\xe0\xe0\x80\x80\x00\x00\x00\x00\xf0\xf0\xe0\xe0\xc0@\xa0\x80``\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x01\x06\x01\x05\x02\r\x0b\x1d\x1f\x0f\x0f\x0e\x0f\x0f\x0e\x00\x04\x01\x05\x00\x04\x0f\x0b\x1d\x1f\x0f\x0f\x0e\x0e\x0f\x0e'),
                            bytearray(b'\x80\x00\x00\x80\xc0@\x80\x80\xd0\x90\xd0\xd0 \xe0\xc0 \x00\x00\x80\x80\xc0\x00\x80\xc0 \x80\xe0\xc0\xa0 \xe0\x00'),
                            bytearray(b'\x1f\x1f\x07\x03\n\x03\x04\x0b\x05\x06\x0c\x0b\x0e\x0f\x00\x00\x1f\x1f\x06\x03\x0c\x03\x00\x03\x04\x04\x0c\x0b\x0c\x0f\x00\x00'),
                            bytearray(b'\xf0\xf0\xe0\xe0\xe0\x00\x80\xe0\xc0@`\xa0\xe0\xe0\x00\x00\xf0\xf0\xe0\xe0\xe0\x00\x00\x80@@`\xa0`\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x01\x06\x01\x05\x02\r\x0b\x1d\x1f\x0f\x0f\x0e\x0f\x0f\x0e\x00\x04\x01\x05\x00\x04\x0f\x0b\x1d\x1f\x0f\x0f\x0e\x0e\x0f\x0e'),
                            bytearray(b'\x80\x00\x00\x80\xc0@\x80\x80\xd0\x90\xd0\xd0 \xe0\xc0 \x00\x00\x80\x80\xc0\x00\x80\xc0 \x80\xe0\xc0\xa0 \xe0\x00'),
                            bytearray(b'\x1f\x1f\x07\x03\x0c\x06\x16\x19\x11\x0f\x1b\x1e\x0f\x0f\x00\x00\x1f\x1f\x05\x03\t\x06\x10\x10\x11\x0f\x11\x1e\x0f\x0f\x00\x00'),
                            bytearray(b'\xf0\xf0\xe0\xe0`\x000\xf0\xd8\xe8\xf8\xd8\xe0\xe0\x00\x00\xf0\xf0\xe0\xe0\xe0\x0000\xf8\xc88\x18\xe0\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x01\x06\x01\x05\x02\r\x0b\x1d\x1f\x0f\x0f\x0e\x0f\x0f\x0e\x00\x04\x01\x05\x00\x04\x0f\x0b\x1d\x1f\x0f\x0f\x0e\x0e\x0f\x0e'),
                            bytearray(b'\x80\x00\x00\x80\xc0@\x80\x80\xd0\x90\xd0\xd0 \xe0\xc0 \x00\x00\x80\x80\xc0\x00\x80\xc0 \x80\xe0\xc0\xa0 \xe0\x00'),
                            bytearray(b"\x1f\x1f\x07\x03\t\x01\x1a\x1d?/?6\x0f\x0f\x00\x00\x1f\x1f\x06\x03\x0e\x01\x18\x187\'90\x0f\x0f\x00\x00"),
                            bytearray(b'\xf0\xf0\xe0\xe0@\xc0\xc0 \x10\xe0\xb0\xf0\xe0\xe0\x00\x00\xf0\xf0`\xe0\x00\xc0\x00\x00\x10\xe0\x10\xf0\xe0\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x07\x08\x03<\x1f ?@?@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\xc0\x80x\xe0\x18\xf8\x04\xf8\x04\x90n\x00\x00\x00\x00@@\x08\x08\x00\x00\x00\x00\x00\x00\x02\x02'),
                            bytearray(b'7H\x078\x03\x1c\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00  \x08\x08\x0c\x0c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0>\xc0<\x00\xfc\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x04\x04\x0c\x0c``\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x07\x18\x07x\x1f`?\xc0\x7f\x80\x7f\x80\x00\x00\x04\x04\x10\x10@@\x00\x00\x80\x80\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\xc0\xc00\xf0\x0c\xf0\x0e\xfc\x02\xfc\x02\xfc\x03\x00\x00@@\x00\x00\x04\x04\x02\x02\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\x7f\x80\x7f\x80\x17h\x07x\x00?\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@@\x00\x00\x18\x18\x00\x00\x00\x00'),
                            bytearray(b'\xe8\x17\xe0\x1f\xe0\x1e\x80~\x00\xfc\x00\xf0\x00\x00\x00\x00\x01\x01\x03\x03\x02\x02\x06\x06\x1c\x1cpp\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00``\x90`\x90\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x0e\t\x06K\x06\x7f\x07\x1f?\x1c\x18\x1c\xff\x00\x00\x08\x08\x07\x06\x0f\x04\x0fC\x1c\x1c\x13\x18\x1e\xfc'),
                            bytearray(b'\x80\x00\xc0\x00\x00\xc0\xe0\xe0\xf0\xfe\xf0~\xbe\xfep\xbc\x00\x00\x00@\x00\x00\xe0\xe0p\xfep~\xb0\xbe\xf00'),
                            bytearray(b';\xfc\x19\x7f\x0f\x0f\n\x08\x05\x01\x01\x06\x03\x02\x01\x01\x1b\xf8\r\x19\x0f\x0f\x0b\x08\x06\x00\x00\x00\x03\x02\x01\x01'),
                            bytearray(b'\xb8x|\xfc\xc0\x80`h\xec\x9c\xfcd\xf8x\x80\x80\xa88||\xf8\x80\x90\x00\x0c\x0c|d\xf0p\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=113),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00<\x18d<B8F\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x07\no\x07\x7f\x0f\x1c8\x1c\xff\x1b\xfc\x00\x00\x04\x04\x0b\x08\x0fC\x0cl\x13\x18\x1e\xfc\x1b\xf8'),
                            bytearray(b'@\x00\xc0\x00\x00\xc0\xe0\xfc\xe0|\xbc\xfcp\xbc\xf88\x00\x00\x00\x80\x00\x00`\xfc`|\xa0\xbc\xf00\xf08'),
                            bytearray(b'\xfb\xfc\x1b|\x1c\x1f\x0f\x0f\r\t\x01\x06\x03\x02\x01\x01\x1f\xf8\x0f\x18\r\x1c\x0f\x0f\x0e\x08\x00\x00\x03\x02\x01\x01'),
                            bytearray(b'\xf88\x9c|x\xf8\xe0\xe8\xec\x9c\xfcd\xf8x\x80\x80\xf08\xdc\x1cxx\x90\x80\x0c\x0c|d\xf0p\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=113),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x06\x06\t\x06\t\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x0e\t\x06K\x06\x7f\x07\x1f?\x1c\x18\x1c\xff\x00\x00\x08\x08\x07\x06\x0f\x04\x0fC\x1c\x1c\x13\x18\x1e\xfc'),
                            bytearray(b'\x80\x00\xc0\x00\x00\xc0\xe0\xe0\xf0\xfe\xf0~\xbe\xfep\xbc\x00\x00\x00@\x00\x00\xe0\xe0p\xfep~\xb0\xbe\xf00'),
                            bytearray(b';\xfc\x19\x7f\x0f\x0f\n\x08\x05\x01\x01\x06\x03\x02\x01\x01\x1b\xf8\r\x19\x0f\x0f\x0b\x08\x06\x00\x00\x00\x03\x02\x01\x01'),
                            bytearray(b'\xb8x|\xfc\xc0\x80`h\xec\x9c\xfcd\xf8x\x80\x80\xa88||\xf8\x80\x90\x00\x0c\x0c|d\xf0p\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=113),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02\x02\x05\x00\x02\x00\x00\x00\x00\x00@@\xa0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x07\no\x07\x7f\x0f\x1c8\x1c\xff\x1b\xfc\x00\x00\x04\x04\x0b\x08\x0fC\x0cl\x13\x18\x1e\xfc\x1b\xf8'),
                            bytearray(b'@\x00\xc0\x00\x00\xc0\xe0\xfc\xe0|\xbc\xfcp\xbc\xf88\x00\x00\x00\x80\x00\x00`\xfc`|\xa0\xbc\xf00\xf08'),
                            bytearray(b'\xfb\xfc\x1b|\x1c\x1f\x0f\x0f\r\t\x01\x06\x03\x02\x01\x01\x1f\xf8\x0f\x18\r\x1c\x0f\x0f\x0e\x08\x00\x00\x03\x02\x01\x01'),
                            bytearray(b'\xf88\x9c|x\xf8\xe0\xe8\xec\x9c\xfcd\xf8x\x80\x80\xf08\xdc\x1cxx\x90\x80\x0c\x0c|d\xf0p\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=113),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=5),
                        AnimationSequenceFrame(duration=8, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=8),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=8, mold_id=8),
                        AnimationSequenceFrame(duration=8, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=11),
                        AnimationSequenceFrame(duration=8, mold_id=12),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=8, mold_id=14),
                        AnimationSequenceFrame(duration=8, mold_id=15),
                        AnimationSequenceFrame(duration=8, mold_id=16),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL735_BOOSTER_RIDING_TRAIN,
    palette_offset=0,
    unknown_num=8
)
