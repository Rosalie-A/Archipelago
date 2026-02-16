# SPR0713_SAGESTICK

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL762_SAGESTICK
sprite = CompleteSprite(
    animation=AnimationPack(389, length=189, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x08\x00\x08\x00\x08\x00\x08\x10\x08\x10\x08\x10\x18\x10\x10\x10\x08\x18\x08\x18\x08\x18\x08\x18\x08\x18\x08\x18\x08\x18\x08\x18'),
                            None,
                            bytearray(b'\x08\x08\x18\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x08\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x100F\x02\t\x05\x81\xf1(\xca \xce\x02\x0b\x00\x00`\x10\x84z\x04\xfbz\x87\xd7/\xc7\x1f\x07\xff'),
                            None,
                            bytearray(b'\xa3\xe7\x04\x1f\x0e\x0f\x02\x06\x00\n\x06\x18\x0c\x08\x0c\x18\x1f\xff\x7f\x7f\x0f\x0f\x0e\x0e\x16\x1e\x06\x1e\x04\x1c\x04\x1c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=90),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x04\x00\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x06\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b' 0h\x1b\x00Ney\x023\x08;\x01\x03\x05\x0f \x10_\x00o\x10\x08w\x11/7\x0f\x07?\x03\x1f'),
                            bytearray(b'\x00\x00\x80\x80\x00@ \x80 @@\xe0\x80\xe0\x80\xe0\x00\x00\x80\x00\x80@`\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            bytearray(b'\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\xe0\x80\xe0\x00`\x10`\x000\x080\x00\x18\x00\x0c\xe0\xe0\xe0\xe0``pp0088\x18\x18\x0c\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=95),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=123),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0c\x00\x10\x18,\x18P0\x00\x80\x00\xc0\x00\x80\x00\x00\x0c\x00\x10\x04$\x0c \x10 `@\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=107),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00D\xb8\x00\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x009\x03\xbe~'),
                            bytearray(b'\x00\x07\x04\t\x06\x1c . C\x01UU{\n;\x05\x00\n\x15\x18\x01.\x11@\x1f4K\nu1?'),
                            bytearray(b'\x00\xf8\x00\xc0\x80\x80\x80\xc0\x80\x80\x00@\x00\x80\x80\x80x\xf8\xc0\xc0\x80\x80@\xc0@\xc0\xc0\xc0\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=107),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=376),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0c\x00\x10\x18,\x18P0\x00\x80\x00\xc0\x00\x80\x00\x00\x0c\x00\x10\x04$\x0c \x10 `@\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=360),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00D\xb8\x00\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x009\x03\xbe~'),
                            bytearray(b'\x00\x07\x04\t\x06\x1c . C\x01UU{\n;\x05\x00\n\x15\x18\x01.\x11@\x1f4K\nu1?'),
                            bytearray(b'\x00\xf8\x00\xc0\x80\x80\x80\xc0\x80\x80\x00@\x00\x80\x80\x80x\xf8\xc0\xc0\x80\x80@\xc0@\xc0\xc0\xc0\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=360),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=375),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x0c\x00\x10\x18,\x18P0\x00\x80\x00\xc0\x00\x80\x00\x00\x0c\x00\x10\x04$\x0c \x10 `@\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00D\xb8\x00\xc2\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x04\x009\x03\xbe~'),
                            bytearray(b'\x00\x07\x04\t\x06\x1c . C\x01UU{\n;\x05\x00\n\x15\x18\x01.\x11@\x1f4K\nu1?'),
                            bytearray(b'\x00\xf8\x00\xc0\x80\x80\x80\xc0\x80\x80\x00@\x00\x80\x80\x80x\xf8\xc0\xc0\x80\x80@\xc0@\xc0\xc0\xc0\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=101, y=359),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\t\x08\x00\x18\x10\x00\x00\x00\x10(\x10\x00 \x00 \t\x07\x0e\x02\x14\x04\x04\x1c\x18\x088\x080\x100P'),
                            None,
                            bytearray(b'@\x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00   ```\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x00\x00@`d<\x05\xfb"\xce\x04?\xa0\xfe\x00\x8e\x00 `\x10\x04\x1a\xfa\x01\xcd\x13S\x8f\x06\xfe\x1e\xfe'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x02\x06\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x01\x00\x04\x01'),
                            bytearray(b'\xc4N\x18< (\xa0h \xb0@`\xc0\xc0\x00\x80\xbe\xfe||\x18x\xd88\x90p \xe0@\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=84),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x18\x14\x08\x1c\x10\x18\x00\x00\x00\x00\x00\x00\x01\x00\x01\x04\x17\x03\x04,\x08\x18'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x00\x00\x00\x00P\x90\x00\xb0\xc6\x0cd\xb7\x13\xdf\x1c\xb7\x00\x00\x00\x00p\x80\x08\xc0\x1ea\x83\x1c\xc4?\x0f\xff'),
                            bytearray(b'\x00\x00\x1d\x01Q! \xef\x00C\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x03@\x0f_?\xc3\xc3\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe4\xeeD\x9c\xa0\xd8\x00\xb0\x00\xc0\x00\x00\x00\x00\x00\x00\x1e\xfe|\xfc8\xf8\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=149, y=94),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x008\x08?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02(\x07/\x1f\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=110),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90 '),
                            bytearray(b'\x01\x00\x00\xc1\x00\x01\x00\xeb\x00;\x00\x1c\x00\x0f\x02\x07\x01\x00\xc1 \x00\xf9\xf2\xfd=>\x1f\x1f\x0f\x0f\x07\x07'),
                            bytearray(b'X\xb0\xd0\x90\x02\x8c\x08\xb8\x00\x14\x10\xbe\x00x@\xe0\x08P X\xd2<\x94~>\xfen\xfe\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=149, y=102),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x008\x08?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02(\x07/\x1f\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=396, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90 '),
                            bytearray(b'\x01\x00\x00\xc1\x00\x01\x00\xeb\x00;\x00\x1c\x00\x0f\x02\x07\x01\x00\xc1 \x00\xf9\xf2\xfd=>\x1f\x1f\x0f\x0f\x07\x07'),
                            bytearray(b'X\xb0\xd0\x90\x02\x8c\x08\xb8\x00\x14\x10\xbe\x00x@\xe0\x08P X\xd2<\x94~>\xfen\xfe\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=404, y=112),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x008\x08?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x02(\x07/\x1f\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=396, y=118),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xb0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90 '),
                            bytearray(b'\x01\x00\x00\xc1\x00\x01\x00\xeb\x00;\x00\x1c\x00\x0f\x02\x07\x01\x00\xc1 \x00\xf9\xf2\xfd=>\x1f\x1f\x0f\x0f\x07\x07'),
                            bytearray(b'X\xb0\xd0\x90\x02\x8c\x08\xb8\x00\x14\x10\xbe\x00x@\xe0\x08P X\xd2<\x94~>\xfen\xfe\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=404, y=110),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\t\x08\x00\x18\x10\x00\x00\x00\x10(\x10\x00 \x00 \t\x07\x0e\x02\x14\x04\x04\x1c\x18\x088\x080\x100P'),
                            None,
                            bytearray(b'@\x00 \x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00   ```\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=396, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x00\x00@`d<\x05\xfb"\xce\x04?\xa0\xfe\x00\x8e\x00 `\x10\x04\x1a\xfa\x01\xcd\x13S\x8f\x06\xfe\x1e\xfe'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x02\x06\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x01\x00\x04\x01'),
                            bytearray(b'\xc4N\x18< (\xa0h \xb0@`\xc0\xc0\x00\x80\xbe\xfe||\x18x\xd88\x90p \xe0@\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=396, y=100),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL762_SAGESTICK,
    palette_offset=0,
    unknown_num=0
)
