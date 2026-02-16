# SPR0545_THROWN_HAMMER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL349_HAMMER_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(201, length=140, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x000\x008\x00\x18\x00\x18\x00\x0c\x00\x0c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=130),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x07\x04\x05\t\t\x18%\x1e=\x06\x00\x00\x00\x00\x03\x00\r\x00\n\x00\x16\x00\x1a\x00v\x00'),
                            bytearray(b'\x00\x00\x80\x80\xc0 `\x98\\\xb8\xfc\x0c\xf0\x10\xf02\x00\x00\x00@\xe0\x10\x98\x00\xa4\x00\x02\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x7f\x0c\xd7\x90o\x01_I*.\x0c\r\x00\x01\x00\nq\x0c\x96h\xb8\x10\xac\x00U\x002\x00\x1e\x00\x04\x00'),
                            bytearray(b'\xe0l\xc0\xdc\x80\x98\x000\x00\xf0\x00\xe0\x00\xe0\x00p\x10\x00 \x00`\x00\xe0 \x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=114),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x88\x88\x00\xa8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00P\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x00\x0f\x08\x03\x0e\x17\n= 7(;\x147\x10\x07\x07\x0f\x07\x1f\x01\r\x02\x05\x02(\x00\x04\x00H\x00'),
                            bytearray(b'\x00\x00\xe0\x00p\x08\xe0\x80\xc0\x80\xc0\x00\xc0@\xc0Y\x00\xc0\xe0\xf0x\xf0\x18\x008\x008\x00?\x00&\x00'),
                            bytearray(b"\'\x01\'0/\'>68\x18\x1c\x1c\x00\x05\x00\x00x\x00X\x10\x10\x00A\x00\x07\x00\x03\x00\x02\x00\x00\x00"),
                            bytearray(b'\x80\x92@x\x000\x00p\x00\xe0\x00\xe0\x00\xc0\x00\x00j\x02\x80\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80@@\x00\x00\x00\x80\x00\xe0\x00\xc0\x00\xc0\x00\x00@\x00\x80\x00\xe0\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00` \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=131),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x03\x07'),
                            None,
                            bytearray(b'\x07\x00\x07\x00\x07\x00\x07\x00\x01\x03\x00\x01\x00\x00\x00\x00\x07\x07\x07\x07\x07\x07\x07\x03\x03\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"\xff\t\xf7\x17\xf4\x1c\xe0\x11\x80\'\x00\xff\x00\xff\x00\x7f\xf0\xf0\xf8\xe0\xe3\xe0\xee\xc0\xd8\x00\x00\x00\x00\x00\x80\x00"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=123),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x18\x08\x00\x100\x10\x00 `0\x00@\xc0\xe0\x80\x00\x00\x00\x18\x00\x00\x000\x00\x00\x00`\x00\x80\x00@\x00'),
                            bytearray(b'\x01\x01\x01\x01\x03\x02\x03\x01\x06D^\x03\x7f\t\xff\x00\x00\x00\x01\x00\x03\x00\x02\x00\xa3@\xb0\xf0\xfc\xf0\xe4\xf0'),
                            bytearray(b'\x80\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=115),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x7fH?Uo<wy>9>?\x1c\x1d\x00\x02z4~\x08\x9c\x00\x0e\x00@\x00\x00\x00\x02\x00\x0c\x00'),
                            bytearray(b'\xf8\x1a\xe0f\x80\x9c\x00<\x00x\x00\xe0\x00\xe0\x00@\x04\x00\x18\x00`\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=132),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x00\x0c\x0c\x00\x02\x00\x02\x00\x02\x04\x06\x00\x00\x00\x01\x00\x00\x00\x00\x04\x00\x0c\x00\x04\x00\x00\x00\x06\x00\x06\x00'),
                            None,
                            bytearray(b'\x02\x03\x00\x00\x02\x02\x02\x02\x02\x07\x03\x0c\x00\x1f\x03<\x00\x00\x07\x00\x01\x00\x01\x00\x04\x00\x0c\x00\x1f\x00<\x00'),
                            bytearray(b'\x00\x00\x00\x00PPxhL\x04>\xd0\xee\x16\xb8H\x00\x00\x00\x00 \x00\x9c\x00\xcc0\xfa\x00p\x00\xc7\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\xfc\x04\xf6b\xfe\x86\xbc\x8dx\x00\xf0\x10\x00\x00\x80\xe0\xbc\xf8v\x1c\x81@\x02\xc0g\x80\xae\x00'),
                            None,
                            bytearray(b'\xf0\x12\xf06\xf06\xe0l\xc0\xdc\x00\x18\x80\xb0\x00pL\x00\x08\x00\x08\x00\x10\x00 \x00\xe0\x00@\x00\x80\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x05\x0c\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x03\x00\x01\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x07\x00\x01\x06\xf7\x98\x00\xf1\x00\x00\x00\x01\x01\x00\x03\x00\x05\x00\x06\x00\t\x00\x8f\x80'),
                            None,
                            bytearray(b'\x01\x16\x08\x05\x03\x06\x03\x17\x13\x17\x03\x0b\x03\x07\x00\x00\x0c\x04\x07\x04\x1c\x04\x08\x00\x08\x00\x04\x00\x02\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x02\x03\x02\x00\x06\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x07\x00\x04\x00\x00\x00'),
                            bytearray(b'   `@\xa0\x80@\x00\x80\x00\x00\x00\x00\x00\x00p\x00@\x00\xa0 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x00\x0f\x00\x0f\x00\x1d\x00\x1f\x00\x1e\x00\x00\x00\x00\x01\x03\x07\x0f\x0f\x0f\x1f\x1f\x1f\x1f\x1f\x1f\x1f'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\xf4\x04\xf8\x10\xe8\x00ll@@\x00\x00\x00\x00\xc0\xc0\xec\xe0\xe4\xe0\xf4\xc0\xd0\x80>\x80'),
                            bytearray(b'\x1f\x1a\x0f\x0b\x0f\x0f\x00\x00\x04\x00\x04\x05\x18\x190 \x0b\x04\x10\x00\x00\x00\x0f\x00\x0b\x00\x12\x08\x14\x00\x08\x00'),
                            bytearray(b'\xc0\xc0\x80\x8c\x80\x8e\x00>\x00<\x00\xfe\x00\xfc\x00\xf0>\x00r\x00q\x00\xc0\x00\xc2\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=116),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x01\x00\x01\x01\x01\x01\x03\x03\x02\x02\x00\x00\x02\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00\x01\x00\x03\x00'),
                            bytearray(b'\x00\x80\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=131),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x00\x03\x04\x17\x18\x04\x03_@wr[\x08\x00\x00\x00\x00\x04\x00\x08\x00\x1f<N<v\x0cZ6'),
                            bytearray(b'@\xc0\xb8\xa8\xf8D~\x86\xbeF\xf8\x18\xe8h\xc0\xc7\x80\x00@\x00&\x00\xb2\x00A\x00\x07\x00\x17\x008\x00'),
                            bytearray(b'=]~,\x1e5\x10\r\x08\x0b\x00\x01\x00\x01\x00\x03|\x02\x7f\x00>\x00>\x00\x04\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x1e\x00>\x00\xf8\x00\xf0\x00\xc0\x00\x80\x00\x80\x00\x80\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=115),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL349_HAMMER_PACKET,
    palette_offset=0,
    unknown_num=8
)
