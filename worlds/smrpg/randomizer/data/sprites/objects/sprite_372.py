# SPR0372_POUNDER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL574_MAD_MALLET
sprite = CompleteSprite(
    animation=AnimationPack(32, length=473, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0\x00 \x00\x00\x00\xa0\x80\xb0\xf8\x84\xf4\xc0\xfe\x00\x1c\xc0\x00\xe0\x00\xf0\xd0\xf0\xd0\x80\xf8\x88\xfc\x80\xfe">'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xc0\x00\xf0\x00\xf8\x00\xf8\x00\xfc\x00\xfc0\xdc\x10\x0c\xc0\xc0\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\xfc\xfc\xfc\xfc\x1c\x1c'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x17\x16\x07?\x07{\x03|\x01~\x00\x7f\x00\x7f\x00\x00\x0b\x01?8\x7f|~\x7f\x7f\x7f\x7f\x7f\x7f\x7f'),
                            bytearray(b'\x00\x0f\x00?\x80\x7f\xfcw\xf83\xb8c\xbcw\x18\xff\x0b\x0b??\xff\xff\xfb\xfb\xef\xeb\xb7\xbb\xe7\xe3\xfe\xfe'),
                            bytearray(b'\x00\x7f\x00?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x00\x00\x00\x7f\x7f????\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfe\x00\xfe\x00\xfe\x08\xea\x0c\xc4\x06\x825\x01\x17Q\xf8\xf8\xe0\xe0\xe0\xe0\xc4\xcc\xca\xc6\x8c\x82<\x03.Q'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00@ \x80\xe0 \xf8\x00|\xc0\xfc\x00\x18\x00\x00\x80\x00\xc0 \x10\xf0\x00\xf8\x80\xfc\x80\xfc$<'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x06\x00\x00\x00\x00\x01\x01\x03\x03\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x01\x01\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'8\x08\x1a\x0e\x10\x03\xc7\x87\x93\x83\xf0\xff\x0f\x0f\x00\x00w\x08w\x0ew\x0f\xf3\x8f\xd7\xef\xff\xff\x0f\x0f\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\xe0\x00\xf0\x00\xf0\x00\xf8\x00\xf8`\xb8 \x18\x80\x80\xe0\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf8\xf8\xf8\xf888'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00.,\x0f~\x0f\xf6\x07\xf8\x03\xfc\x01\xfe\x00\xff\x00\x00\x16\x02\x7fq\xff\xf9\xfd\xff\xff\xff\xff\xff\xff\xff'),
                            bytearray(b'\x00\x1f\x00\x7f\x00\xff\xf8\xef\xf0gp\xc7x\xef0\xfe\x17\x17\x7f\x7f\xff\xff\xf7\xf7\xdf\xd7ow\xcf\xc7\xfc\xfc'),
                            bytearray(b'\x00\xff\x00\x7f\x00\x7f\x00?\x00?\x05?\x01\x1d\x00\x0e\xff\xff\x7f\x7f\x7f\x7f??\x1f?\r=\x02\x1f\x01\x0f'),
                            bytearray(b'\x00\xf8\x00\xf0\x00\xf0\x00\xd0\x00\x90@\xd0` .\x08\xf0\xf0\xc0\xc0\xc0\xc0\xa0\xa0\xe0\xe0 `\xd0\xb0\xe6\x98'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc4\xfcXx00\xe0\xe0\xf8\xf8\xf0\xf0\xc0\xc0\x00\x00\x80\xfc\x00x\x100\xe0\xe0\xf8\xf8\xf0\xf0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00'),
                            bytearray(b"\x1d\x05\x0b\x01J\x02\x03\x03I\xa1O\xcf/\xaf\x00\x00:\x05;\x05z\x06Y\'k\xb7?\xff\x1f\xff\x00\x00"),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00\xe0\x00\xf0\x00\xf0\x00\xf8\x00\xf8`\xb8\x00\x00\x80\x80\xe0\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf8\xf8\xf8\xf8'),
                            None,
                            bytearray(b' \x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c`>\x82\x1e88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\xc0>\xa0~'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00.,\x0f~\x0f\xf6\x07\xf8\x03\xfc\x01\xfe\x00\x00\x00\x00\x16\x02\x7fq\xff\xf9\xfd\xff\xff\xff\xff\xff'),
                            bytearray(b'\x00\x00\x00\x1f\x00\x7f\x00\xff\xf8\xef\xf0gp\xc7x\xef\x00\x00\x17\x17\x7f\x7f\xff\xff\xf7\xf7\xdf\xd7ow\xcf\xc7'),
                            bytearray(b'\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x0f\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f??\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'0\xfe\x00\xf8\x00\xf8\x00\xf8\x00\xc8 \xa81\x10\x16\x04\xfc\xfc\xf0\xf0\xc0\xc0\xc0\xc0\xb0\xb0\x90\xb0)\x183\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\xc0 \xe0``\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x80 \xe0\x00\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x00\x03\x01\x07\x00\x07\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x03\x00\x07\x00\x07\x00\x00'),
                            bytearray(b'J Y1@\x01\x02!\r\xe1\x9c\xbe@\xc0\x00\x00n\x11\xee\x11\xff1\xefqo\xf3~\xfe \xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80`\xc0\xb0\xe0X\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0pp\xf8\xb8'),
                            None,
                            bytearray(b' \xd8\x00\xfc\x10\xec\x00\xfc\x00|\x00\x1c\x00\x0c\x00\x0088\xbc\xbc\xfc\xfc\xfc\xfc||\x1c\x1c\x0c\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x05\x05\x0f\x07\x03\x0c\x00\x1f\x00\x1f\x00\x1f\x00\x1f\x01\x00\x02\x00\r\x08\x0f\x0f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f'),
                            bytearray(b'\x80`\xc0\xb0\x80x\x08\xf6\x0c\xf3\x07\xfa\x7f\x99n\x89\xe0\xe0\xf0p\xf8\xf8\xfe\xfe\xff\xff\xff\xfd\xa7\xe6\xff\xe7'),
                            bytearray(b'\x00\x1f\x00\x0f\x00\x0f\x00\x07\x00\x01\x00\x00\x00\x00\x00\x00\x1f\x1f\x0f\x0f\x0f\x0f\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\\\x930\xcf\x00\xff\x00\xef\x10\xd0( , \x08\x00\xaf\xcf\xff\xff\xff\xff\xff\xff\xec\xfc\x084\x0c0,0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00@@\xc0p\x000(\xa8\x90\xd0\x00\x00\x00\x00\x80\x00\x80`\x80pH\xf8\xd8\xf8\xf0\xf0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x1e\x01\x0f\x01\x07\x02\x02\x00\x00\x00\x00\x01\x01\x00\x00\x01\x1e\x00\x0f\x00\x07\x01\x03\x00\x00\x00\x00\x01\x01\x00\x00'),
                            bytearray(b'x\x00\x04\x00\x08\x08\x02\x00\x04\x04\xf1\xf1\xee\xee\x00\x00\xff\x00w\xf8\x83\x8c\x0b\x0c\t\x0e\xff\xff\xee\xee\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80`\xc0\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0pp'),
                            None,
                            bytearray(b'\xe0X \xd8\x00\xfc\x10\xec\x00\xfc\x00|\x00\x1c\x00\x0c\xf8\xb888\xbc\xbc\xfc\xfc\xfc\xfc||\x1c\x1c\x0c\x0c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x05\x05\x0f\x07\x03\x0c\x00\x1f\x00\x1f\x00\x1f\x00\x00\x01\x00\x02\x00\r\x08\x0f\x0f\x1f\x1f\x1f\x1f\x1f\x1f'),
                            bytearray(b'\x00\x00\x80`\xc0\xb0\x80x\x08\xf6\x0c\xf3\x07\xfa\x7f\x99\x00\x00\xe0\xe0\xf0p\xf8\xf8\xfe\xfe\xff\xff\xff\xfd\xa7\xe6'),
                            bytearray(b'\x00\x1f\x00\x1f\x00\x0f\x00\x0f\x00\x07\x00\x01\x00\x00\x00\x1c\x1f\x1f\x1f\x1f\x0f\x0f\x0f\x0f\x07\x07\x01\x01\x00\x00\x00\x1c'),
                            bytearray(b'n\x89\\\x930\xcf\x00\xff\x00\xe7\x18\xd8\x04\x00\x0c\x00\xff\xe7\xaf\xcf\xff\xff\xff\xff\xff\xff\xc4\xdc\x14\x18\xfe\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'@\x03\x92\x01S\x01\t!\x01\xb1^\xde(\xe8\x10\xf0|\x83\xfe\x01\xff!\xadss\xff>\xfe\x18\xf8\x10\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x80`\xc0\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0\xe0\xf0p'),
                            None,
                            bytearray(b'@\xb0\x00\xf8 \xd8\x00\xf8\x00\xf8\x008\x00\x98\x00\x80ppxx\xf8\xf8\xf8\xf8\xf8\xf888\x18\x98\x00\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x02\x0b\x0b\x1f\x0e\x06\x19\x00?\x00?\x00?\x00?\x03\x01\x05\x00\x1b\x11\x1f\x1f????????'),
                            bytearray(b'\x00\xc0\x80`\x00\xf0\x10\xec\x19\xe7\x0f\xf4\xff3\xdd\x12\xc0\xc0\xe0\xe0\xf0\xf0\xfc\xfc\xff\xff\xff\xfbN\xcc\xff\xcf'),
                            bytearray(b'\x00?\x00\x1f\x00\x1f\x00\x0f\x00\x03\x00\x00\x00\x00\x00\x00??\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"\xb8\'`\x9f\x00\xff\x00\x9f@\xc0\x00\x00\xb0\x83 \x07^\x9e\xff\xff\xff\xff\xff\xff\xb0\xf0\x80\xf00\xc3\xb8\xc7"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc4\xfcXx00\xe0\xe0\xf8\xf8\xf0\xf0\xc0\xc0\x00\x00\x80\xfc\x00x\x100\xe0\xe0\xf8\xf8\xf0\xf0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x06\x00\x00\x00\x00\x01\x01\x03\x03\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x01\x01\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b':\x0b\x1e\x0f\x11\x03\xc7\x87\x93\x83\xf0\xff\x0f\x0f\x00\x00u\x0bs\x0fw\x0f\xf3\x8f\xd7\xef\xff\xff\x0f\x0f\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\x00\xe0\x00\xf0\x00\xf0\x00\xf8\x00\xf8`\xb8 \x18\x80\x80\xe0\xe0\xf0\xf0\xf0\xf0\xf0\xf0\xf8\xf8\xf8\xf888'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x80<\xc0\xfc\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\xc0|\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00.,\x0f~\x0f\xf6\x07\xf8\x03\xfc\x01\xfe\x00\xff\x00\x00\x16\x02\x7fq\xff\xf9\xfd\xff\xff\xff\xff\xff\xff\xff'),
                            bytearray(b'\x00\x1f\x00\x7f\x00\xff\xa4\xc7\xc2KB\x8b&\xe7<\xde\x17\x17\x7f\x7f\xff\xff\xfb\xe3\xff\xc9}I\x99\x81\xf6\xe2'),
                            bytearray(b'\x00\xff\x00\x7f\x00\x7f\x00?\x00?\x05?\x01\x1d\x00\x0e\xff\xff\x7f\x7f\x7f\x7f??\x1f?\r=\x02\x1f\x01\x0f'),
                            bytearray(b'\x00\xf8\x00\xf0\x00\xf0\x00\xd0\x00\x90@\xd0b -\x08\xf0\xf0\xc0\xc0\xc0\xc0\xa0\xa0\xe0\xe0 `\xd3\xb0\xe7\x98'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=102),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xc0\x00\xf0\x00\xf8\x00\xf8\x00\xfc\x00\xfc0\xdc\x10\x0c\xc0\xc0\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\xfc\xfc\xfc\xfc\x1c\x1c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x17\x16\x07?\x07{\x03|\x01~\x00\x7f\x00\x7f\x00\x00\x0b\x01?8\x7f|~\x7f\x7f\x7f\x7f\x7f\x7f\x7f'),
                            bytearray(b'\x00\x0f\x00?\x80\x7f\xfcw\xf83\xb8c\xbcw\x18\xff\x0b\x0b??\xff\xff\xfb\xfb\xef\xeb\xb7\xbb\xe7\xe3\xfe\xfe'),
                            bytearray(b'\x00\x7f\x00?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x00\x00\x00\x7f\x7f????\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0\x00 \x00\x00\x00\xa0\x80\xb0\xf8\x84\xf4\xc0\xfe\x00\x1c\xc0\x00\xe0\x00\xf0\xd0\xf0\xd0\x80\xf8\x88\xfc\x80\xfe">'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xff\x00\xf0\x02\xe2\x00\xe0\x00\xc0\x00\x80\x00\x00\x00\x00\xf8\xf8\xef\xef\xe0\xe3\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00@\x00\x00\xa0\x10X\x00,\x00.\x02\x15C\x00\x00\x80\x80\x00\xe0\xf0\x00x\x00<\x00<\x02\x1ea'),
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xc0\x00\xf0\x00\xf8\x00\xf8\x00\xfc\x00\xfc0\xdc\x10\x0c\xc0\xc0\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\xfc\xfc\xfc\xfc\x1c\x1c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x17\x16\x07?\x07{\x03|\x01~\x00\x7f\x00\x7f\x00\x00\x0b\x01?8\x7f|~\x7f\x7f\x7f\x7f\x7f\x7f\x7f'),
                            bytearray(b'\x00\x0f\x00?\x80\x7f\xfcw\xf83\xb8c\xbcw\x18\xff\x0b\x0b??\xff\xff\xfb\xfb\xef\xeb\xb7\xbb\xe7\xe3\xfe\xfe'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00\xc0\x00@\x80\x80\x80\x00@@\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\xc0@\x00\xc0\x00\x80'),
                            None,
                            bytearray(b'\xc0\x00 \x00\x00\x00\xa0\x80\xb0\xf8\x84\xf4\xc0\xfe\x00\x1c\xc0\x00\xe0\x00\xf0\xd0\xf0\xd0\x80\xf8\x88\xfc\x80\xfe">'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x7f\x00?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x00\x00\x00\x7f\x7f????\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x00\xff\x00\xff\x00\xf8\x01\xe1\x00\xc0\x00\x808\x00\x19P\xf8\xf8\xe0\xe0\xe7\xe7\xc0\xc1\xc1\xc0\x83\x80?\x00/P'),
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xc1\x00\'\x04\x06\x01\xa0\x83\xb0\xf8\x84\xf4\xc0\xfe\x00\x1c\xc2\x01\xe1\x03\xf7\xd7\xf3\xd3\x80\xf8\x88\xfc\x80\xfe">'),
                            bytearray(b'\x80p\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0``\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x07\x07\x1f\x1f?????\x1f\x1f/\x00\x00\x00\x00\x04\x00\x10\x00 \x00 \x00  \x10\x10'),
                            bytearray(b'\x00\x00\x00\x00\xf0\xf0\xfc\xfc\xfe\xfe\xfe\xfc\xfe\xfc\xfc\xfa\x00\x00\x00\x00\x10\x00\x04\x00\x02\x00\x02\x02\x02\x02\x06\x06'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x1f\x00\x0f\x00\x07\x00\x07\x03\x02\x01\x05\x08\x04\x1a\x02\x1c\x18\x0f\x0f\x07\x07\x07\x07\x01\x07\x0c\x03<\x03\xf9\x07'),
                            bytearray(b'\xf0\xee\x00\xfc\x0c\xf8\x18\xe4(\xc4\x18\xfc\x08\xf4\x00\xfc\x06\x16\xc4\xc4\xf4\xf4\xec\xec\xf4\xe4\xe4\xe4\xfc\xfc\xfc\xfc'),
                            bytearray(b'v\x05\xf01`\xe1\xc0\xc1\x80\x81\x01\x00\x01\x00\x01\x01\xf3\x0f\xc11\x81a\x00\xc0\x01\x81\x01\x01\x00\x01\x80\x80'),
                            bytearray(b'\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xf8\x00\xf0\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8\xfc\xfc\xf0\xf0xxpp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x00\x01\x02\x01\n\x003\x01\x11S\x01\x00\x03\x00\x03\x00\x07\x00\x07\x00\x0e\x01>\x01.Q'),
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\xc0\xc0\xe0\xe0\xf0px\xa08\xc0\x00\xfc\x00\xfc\x00\x00\x00\x00\x00\x00\xf0\x80\xf8\xd8\xf8\xf8\xfc\xfc\xfc\xfc'),
                            None,
                            bytearray(b'\x00\xfc\x00\xfc\x80|\x00\xfc\x00\xf8\x00p\x00\x00\x00\x00\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8pp\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00>\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'8\x00M,\xb00@\xc0@@\x80\x80\x80\x80\x00 \xf8\x07\xe1\x1e\x80p\x80@\x00\xc0\x00\x80\x00\x80\xa0\xa0'),
                            bytearray(b"\x01\x01\x83C\xe1\x07`\x07(\x07 \'\x10\x17 O\x00\xc0\xc0 \xe7\x16g\x17/\x1f\x0f?/?\x7f\x7f"),
                            bytearray(b'\xc00 \x1f\x03\r\xa0\x8f\xb0\xff\x84\xf7\xc0\xff\x00\x1d\xf00\xff\x1f\xff\xde\xff\xdf\x87\xff\x8b\xff\x81\xff#?'),
                            bytearray(b' \xdfQ\xae\xe2\xdc\xc78\x06\xfb\x00\xff\x00\xfc\x00\xe0??\xdf\xdf}<\xf9\xfd\xf9\xfd\xff\xff\xf4\xf4\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x030\x02\x15S\x00\x00\x01\x00\x03\x00\x07\x00\x07\x00\x0f\x00>\x01.Q'),
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0\x00 \x00\x00\x00\xa0\x80\xb0\xf8\x84\xf4\xc0\xfe\x00\x1c\xc0\x00\xe0\x00\xf0\xd0\xf0\xd0\x80\xf8\x88\xfc\x80\xfe">'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80x'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x0f\x04\x1f\x0c\x1b\x00\x00\x01\x01\x02\x02\x06\x06\x05\x05\r\r\r\t\r\x05'),
                            bytearray(b'\x00\xe0\x00\xf0\x00\xf0\x00\xe0\x00\xc0\x00\xc0\x03\xc0\x0f\xc0  00pp\xe0\xe0\xc0\xc0\xc0\xc0\xc3\xc0\xcf\xc0'),
                            bytearray(b'\x04\x13\x0c;\x08?\x087\x00?\x00?\x00?\x03?\r\x05\x15\x15\x0b\x03\x0b\x0b\x13\x13\x1f\x1f???<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x05\xc9\x10\xd8\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\xcc\xd3\xe8\xf4\xe0\xf8\xe0\xf0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\xe0\xe000\x16\x10\x1e\x10\n\x00\x0b\x003\x00\x13P\x00\xfc\x00>\x06\x18\x0e\x10\x0e\x01\x0f\x00?\x00/P'),
                            bytearray(b'\x80\xc0 `\xb0p0\xf08\xc00\xc8\x00\xf8\x00\xf8@@\xc0@\xc0\xc0\xf0\xc0\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02>\x03<A\x7f@\x7f`_`\xdf\x00\xff\x00\xff?<???>\xbf?\xff?\xff\xbf\xff\xff\xff\xff'),
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x7f\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x7f\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=120),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0\x00 \x00\x00\x00\xa0\x80\xb0\xf8\x84\xf4\xc0\xfe\x00\x1c\xc0\x00\xe0\x00\xf0\xd0\xf0\xd0\x80\xf8\x88\xfc\x80\xfe">'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00\x80x'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=105),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x0f\x04\x1f\x0c\x1b\x00\x00\x01\x01\x02\x02\x06\x06\x05\x05\r\r\r\t\r\x05'),
                            bytearray(b'\x00\xe0\x00\xf0\x00\xf0\x00\xe0\x00\xc0\x00\xc0\x03\xc0\x0f\xc0  00pp\xe0\xe0\xc0\xc0\xc0\xc0\xc3\xc0\xcf\xc0'),
                            bytearray(b'\x04\x13\x0c;\x08?\x087\x00?\x00?\x00?\x03?\r\x05\x15\x15\x0b\x03\x0b\x0b\x13\x13\x1f\x1f???<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x05\xc9\x10\xd8\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\xcc\xd3\xe8\xf4\xe0\xf8\xe0\xf0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\xe0\xe000\x16\x10\x1e\x10\n\x00\x0b\x003\x00\x13P\x00\xfc\x00>\x06\x18\x0e\x10\x0e\x01\x0f\x00?\x00/P'),
                            bytearray(b'\x80\xc0 `\xb0p0\xf08\xc00\xc8\x00\xf8\x00\xf8@@\xc0@\xc0\xc0\xf0\xc0\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8'),
                            bytearray(b'\x06\xf0C\xc0"\xa0\x02\x00\x02\x00\x02\x02\x01\x01\x00\x00\x1e\xf1?\xf0\x1e\xf1\x0e\x01\x06\t\x01\x07\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02>\x03<A\x7f@\x7f`_`\xdf\x00\xff\x00\xff?<???>\xbf?\xff?\xff\xbf\xff\xff\xff\xff'),
                            bytearray(b'\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x7f\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x7f\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=121),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x06\x00\x03\x00\x03\x00\x03\x00\x02\x00\x02\x02\x00\x00\x00\x00\x0e\x01\x0f\x00\x0f\x00\x0f\x00\x06\t\x01\x07\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0@\xc0@\xc0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xc0\x00\xf0\x00\xf8\x00\xf8\x00\xfc\x00\xfc0\xdc\x10\x0c\xc0\xc0\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8\xfc\xfc\xfc\xfc\x1c\x1c'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x17\x16\x07?\x07{\x03|\x01~\x00\x7f\x00\x7f\x00\x00\x0b\x01?8\x7f|~\x7f\x7f\x7f\x7f\x7f\x7f\x7f'),
                            bytearray(b'\x00\x0f\x00?\x80\x7f\xfcw\xf83\xb8c\xbcw\x18\xff\x0b\x0b??\xff\xff\xfb\xfb\xef\xeb\xb7\xbb\xe7\xe3\xfe\xfe'),
                            bytearray(b'\x00\x7f\x00?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x00\x00\x00\x7f\x7f????\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfe\x00\xfe\x00\xe6\x08\xea\x0c\xc4\x06\x82\x05\x01\x07\x01\xf8\xf8\xe0\xe0\xf8\xf8\xc4\xcc\xca\xc6\x8c\x82\x0c\x03\x0e\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02>\x03<A\x7f@\x7f`_`\xdf\x00\xff\x00\xff?<???>\xbf?\xff?\xff\xbf\xff\xff\xff\xff'),
                            bytearray(b'\x80\xc0 `\xb0p0\xf08\xc00\xc8\x00\xf8\x00\xf8@@\xc0@\xc0\xc0\xf0\xc0\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8'),
                            bytearray(b'\x00\x7f\x00\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x7f\x7f\x1f\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x0c\x04\x10\x00\xb0\x00\x00\x00\x00\x00\x00\x00p\x00\xf8\x00\xf8\x04\xf4\x0c\xf8\x08'),
                            None,
                            bytearray(b'\xc0@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0p@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x0f\x04\x1f\x0c\x1b\x00\x00\x01\x01\x02\x02\x06\x06\x05\x05\r\r\r\t\r\x05'),
                            bytearray(b'\x00\xe0\x00\xf0\x00\xf0\x00\xe0\x00\xc0\x00\xc0\x00\xc0\x00\xc0\xa0\xa000pp\xe0\xe0\xc0\xc0\xc0\xc0\xc1\xc0\xc3\xc0'),
                            bytearray(b'\x04\x13\x0c;\x08?\x087\x00?\x00?\x00?\x03?\r\x05\x15\x15\x0b\x03\x0b\x0b\x13\x13\x1f\x1f???<'),
                            bytearray(b'\x03\xc0\x06\xc1\n\xc2\x00\xc0\x00\xc8\x00\xf0\x00\xe0\x00\xc0\xc7\xc0\xcf\xd0\xe9\xf7\xe6\xfe\xf0\xf0\xc0\xc0\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=104),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xf0\x00\xff\x03}\x01~\x00?\x00\x1f\x00\x0f\x00\x03\xf0\xf0\xff\xff?>\x7f\x7f??\x1f\x1f\x0f\x0f\x02\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=118),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\xc0\xc0\xe0\xe0\xf0px\xa08\xc0\x00\xfc\x00\xfc\x00\x00\x00\x00\x00\x00\xf0\x80\xf8\xd8\xf8\xf8\xfc\xfc\xfc\xfc'),
                            bytearray(b' \xdfQ\xae\xe2\xdc\xc78\x06\xfb\x00\xff\x00\xfc\x00\xe0??\xdf\xdf}<\xf9\xfd\xf9\xfd\xff\xff\xf4\xf4\xe0\xe0'),
                            bytearray(b'\x00\xfc\x00\xfc\x80|\x00\xfc\x00\xf8\x00p\x00\x00\x00\x00\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8pp\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x05\x01\x03\x00\x03\x00\x03\x00\x00\x00\x07\x00\x0f\x00\x0f\x00\x0e\x01\x07\x00\x03\x00\x03\x00'),
                            bytearray(b'\x00\x00\x80\x00\x80\x00@@\xc0\xc0\xc0\xc0\x00\x00\x80\x00\x00\x00\x80\x00\x80@\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x80@'),
                            bytearray(b'\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00``'),
                            bytearray(b'\x81\x01\x83\x03\xc1\x07\xd0\x17X\x17`\x07\x00\x07`o\x80@\x80`\xc7&\xc77O?o\x1f\x0f\x7f\x1f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=102),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xf8\x00\xf0\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8\xfc\xfc\xf0\xf0xxpp'),
                            bytearray(b'\x01\x00\x07\x04\x06\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01\x01\x03\x07\x07\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80p\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0``\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            None,
                            bytearray(b'\x01\x00\x07\x00\x1c\x008\x00""\x18\x18\x00\x00\x00\x00\x0f\x00?\x00<\x038\x07\x00>\x00\x18\x00\x00\x00\x00'),
                            bytearray(b'\xcc\r01@A\x80\x81\x00\x01\x01\x00\x01\x00\x01\x01\xc1=\x01\xf1\x01\xc1\x00\x80\x01\x01\x01\x01\x00\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x07\x07\x1f\x1f?????\x1f\x1f/\x00\x00\x00\x00\x04\x00\x10\x00 \x00 \x00  \x10\x10'),
                            bytearray(b'\x00\x00\x00\x00\xf0\xf0\xfc\xfc\xfe\xfe\xfe\xfc\xfe\xfc\xfc\xfa\x00\x00\x00\x00\x10\x00\x04\x00\x02\x00\x02\x02\x02\x02\x06\x06'),
                            bytearray(b'\x07\x1f\x00\x0f\x00\x07\x00\x07\x03\x02\x01\x01\x18\x002\x02\x1c\x18\x0f\x0f\x07\x07\x07\x07\x05\x03\x04\x038\x07\xf1\x0f'),
                            bytearray(b'\xf0\xee\x00\xfc\x0c\xf8\x18\xe4(\xc4\x18\xfc\x08\xf4\x00\xfc\x06\x16\xc4\xc4\xf4\xf4\xec\xec\xf4\xe4\xe4\xe4\xfc\xfc\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=92),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=10, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=10, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=10, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=10, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=16, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=8, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL574_MAD_MALLET,
    palette_offset=1,
    unknown_num=0
)
