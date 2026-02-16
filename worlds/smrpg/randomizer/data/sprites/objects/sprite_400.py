# SPR0400_JINX_CLONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL581_JINX_CLONE
sprite = CompleteSprite(
    animation=AnimationPack(66, length=193, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x03\x01\x07\x01\x07\x03\x07\x02\x07\x02\x0f\t\x07\x00\x01\x00\x03\x00\x07\x01\x07\x01\x07\x00\x06\x00\x06\x00\x01'),
                            bytearray(b' \xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x00\x80\x00\xe0\x00\xc0\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00@\x00'),
                            bytearray(b'\t\x04\x01\x07\x02\x1f\x05\x17\x00\x07\x02\x02\x01\r\x07\x07\x02\x02\x00\x00\x07\x00\r\x00\x00\x00\x01\x00\x03\x01\x07\x07'),
                            bytearray(b'  Pp\xcc\xfc0~L|hhpp \xe0\xe0\x00\xf0\x0c\xfc\x02\xbe\x11\xcc\x0f\xd8\x00\xf0p  '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x03\x0f\x04\x1c\x04\x1c\x0c\x1c\n\x1e\t?\x00\x00\x00\x07\x00\x0f\x00\x1e\x04\x1e\x04\x1c\x00\x18\x00\x18'),
                            bytearray(b'\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'$\x1e$\x10\x05\x1d\x0b\x7f\nn\x0e\x0e\x02\x1a\x0e\x0f\x01\x04\x0b\x08\x03\x00\x1f\x00\x1b\x00\x01\x00\x07\x02\x0e\x0e'),
                            bytearray(b'\x00\x00\x80\x80@\xc0\x10\xf0@\xfc\xf8\xf8\xf0\xf0@\xc0\x00\x00\x80@\xc00\x80\x08L\x02\xf8\x1e\xf0\xf0@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x01\x03\x00\x03\x04\x1f\t\x1f\x0c\x0b\x00\x00\x00\x01\x00\x03\x00\x03\x00\x02\x00\x04\x00\x01\x00\x00'),
                            bytearray(b'\x08x0\xf0\x80\x80\x80\x80@\xc0\xa0\xe0\x80X\x80\x98\x00x\x00\xf0\x80\xc0\x80\x80\x00\x00\x00\x80 \x00`\x00'),
                            bytearray(b'\x01\x07\x05\x0f\x02\x0e\x06\x06\x04\x0c\x07\x1f\x0e\x0f\x07\x07\x00\x00\x0f\x00\x03\x00\x01\x00\x03\x00\x06\x06\x0e\x0e\x07\x07'),
                            bytearray(b'\x80\xa0\x80\xe0\xc0\xf0\xe8\xf8\xf8\xf8\xc0\xc0`\xe0\xc0\xc0@\x00\xe0\x00p@\xf8`\xf8x\xc0\xc0``\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=111),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x01\x0e\x01\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00'),
                            bytearray(b'\x00\x1c\x06>\x15u\x03\xe3P\x90\x10\xf0b\xeeB\xf6\x00\x1c\x00>\x10\x7f\x00\x13\x08 \x08\x00\x10\x00\x88\x00'),
                            bytearray(b'\x02\x05\x00\x07\x06\x06\x03\x0f\x07\x0f\x04\x05\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x02\x06\x06\x04\x04\x00\x00\x00\x00'),
                            bytearray(b'\xc0\xe0`p\xe8\xf8\xf0\xf8\xf8\xf8@\xc0\xc0\xc0\x00\x00\xf0\x00\xb0 \xf8`\xf8\xf0\xf8\xf0@@\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=118),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x03\x00\x07\x02\x05\x07\x07\x07\x1f\x0e\x1f\x04\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x06\x06\x06\x04\x04'),
                            bytearray(b'\x04<F\xfe/\xff3\xf3\xff\xff\xf6\xfe\xf8\xfe\xf8\xf8\x00\x04\xc0\x02@\x03|\x03 \x0fxr\xf8x\xf8\xf0'),
                            bytearray(b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\xfc\xfc\xfc\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf0\xfc\xc0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=373),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x03\x00\x07\x02\x05\x07\x07\x07\x1f\x0e\x1f\x04\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x06\x06\x06\x04\x04'),
                            bytearray(b'\x04<F\xfe/\xff3\xf3\xff\xff\xf6\xfe\xf8\xfe\xf8\xf8\x00\x04\xc0\x02@\x03|\x03 \x0fxr\xf8x\xf8\xf0'),
                            bytearray(b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\xfc\xfc\xfc\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf0\xfc\xc0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=373),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x01&\x037\x0e\x1f&\x7f\x14}\t\x1f\x00\x0c\x00\x00\x00\x00\x00\x00\x06\x06F&|\x16\x1f\t\x0c\x03'),
                            bytearray(b' \xe0(\xe8\xf0\xf0`\xe0`\xe0\xf0\xf0\xf0\xf0\xd0\xd0\x00\x00\x08\x10P\x08 \x18`\x18px\xf0\xf8\xd0\xe8'),
                            bytearray(b'\x01\r\x00\x00\x00\x00\x00\x03\x00\x00\x01\x01\x07\x07\x00\x00\x01\x03\x00\x03\x00\x00\x00\x03\x00\x00\x01\x01\x07\x07\x00\x00'),
                            bytearray(b'\xd8\xd8L\xccL\xcc\xc0\xc0\x00\x00\xf0\xf0\xe0\xe0\x00\x00\xd0\xf4\x00\xf2\x00\xe2@\xc0\x00\x00\xf0\xf0\xe0\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=104),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x1e\x03\x7f\x00?\x04\x1f\x02\x0f\x00\x00\x00\x00\x00\x00\x1e\x00\x7f\x00?\x00\x1f\x00\x0f\x00'),
                            bytearray(b'\x00\x00\x00\xc0@\xe6D\xc7\xfc\xff\xd7\xf7p\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00@(\xe8\x00\xf1\x08\xf0\x08\xf0\x90'),
                            bytearray(b'\x13?\x03/\x087\x03?\x03\x1f\x07\x0f\x03\x03\x00\x00\x0f \x00 \x000\x00\x18\x00\x1e\x00\x0f\x03\x03\x00\x00'),
                            bytearray(b'\xe0\xe0\xf0\xf0\xc0\xd0\xc0\xcc\xc0\xcc\xb8\xb8||\xf0\xf0\xe0\xe0@\x00@\x00\xc0\x00@\x80\xb8\xb8||\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=105),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x03\x00\x07\x02\x05\x07\x07\x07\x1f\x0e\x1f\x04\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x06\x06\x06\x04\x04'),
                            bytearray(b'\x04<F\xfe/\xff3\xf3\xff\xff\xf6\xfe\xf8\xfe\xf8\xf8\x00\x04\xc0\x02@\x03|\x03 \x0fxr\xf8x\xf8\xf0'),
                            bytearray(b'\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\xfc\xfc\xfc\x18\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xf0\xfc\xc0\x18\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=353),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x03\x0f\x04\x1c\x04\x1c\x0c\x1c\n\x1e\t?\x00\x00\x00\x07\x00\x0f\x00\x1e\x04\x1e\x04\x1c\x00\x18\x00\x18'),
                            bytearray(b'\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'$\x1e$\x10\x05\x1d\x0b\x7f\nn\x0e\x0e\x02\x1a\x0e\x0f\x01\x04\x0b\x08\x03\x00\x1f\x00\x1b\x00\x01\x00\x07\x02\x0e\x0e'),
                            bytearray(b'\x00\x00\x80\x80@\xc0\x10\xf0@\xfc\xf8\xf8\xf0\xf0@\xc0\x00\x00\x80@\xc00\x80\x08L\x02\xf8\x1e\xf0\xf0@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=114),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x01\x03\x00\x03\x04\x1f\t\x1f\x0c\x0b\x00\x00\x00\x01\x00\x03\x00\x03\x00\x02\x00\x04\x00\x01\x00\x00'),
                            bytearray(b'\x08x0\xf0\x80\x80\x80\x80@\xc0\xa0\xe0\x80X\x80\x98\x00x\x00\xf0\x80\xc0\x80\x80\x00\x00\x00\x80 \x00`\x00'),
                            bytearray(b'\x01\x07\x05\x0f\x02\x0e\x06\x06\x04\x0c\x07\x1f\x0e\x0f\x07\x07\x00\x00\x0f\x00\x03\x00\x01\x00\x03\x00\x06\x06\x0e\x0e\x07\x07'),
                            bytearray(b'\x80\xa0\x80\xe0\xc0\xf0\xe8\xf8\xf8\xf8\xc0\xc0`\xe0\xc0\xc0@\x00\xe0\x00p@\xf8`\xf8x\xc0\xc0``\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=115),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\r\x01\x0e\x01\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00'),
                            bytearray(b'\x00\x1c\x06>\x15u\x03\xe3P\x90\x10\xf0b\xeeB\xf6\x00\x1c\x00>\x10\x7f\x00\x13\x08 \x08\x00\x10\x00\x88\x00'),
                            bytearray(b'\x02\x05\x00\x07\x06\x06\x03\x0f\x07\x0f\x04\x05\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x02\x06\x06\x04\x04\x00\x00\x00\x00'),
                            bytearray(b'\xc0\xe0`p\xe8\xf8\xf0\xf8\xf8\xf8@\xc0\xc0\xc0\x00\x00\xf0\x00\xb0 \xf8`\xf8\xf0\xf8\xf0@@\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=114),
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
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=12, mold_id=11),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL581_JINX_CLONE,
    palette_offset=0,
    unknown_num=8
)
