# SPR0570_GREEN_SPORE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL411_SPORE_PINK_GREEN
sprite = CompleteSprite(
    animation=AnimationPack(237, length=228, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x01\x08\x07\x00?\x00?\x00?\x00\x7f\x00\xff\x00\x00\x03\x03\x0f\x0f????\x7f\x7f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00P\x80\x00\xf0\x04\xf8\x04\xf8\x04\xf8\x1e\xe0^\xa0\x00\x00\xd0\xd0\xf0\xf0\xfc\xfc\xfc\xfc\xfe\xfe\xfe\xfe\xfe\xfe'),
                            bytearray(b'\x11\xeeq\x0e\x7f\x00\x1f\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f????\x0f\x0f\x03\x03'),
                            bytearray(b'\xec\x00\xf4\x00\xf0\x00\xb0\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x0c6D\xba@\xeb\x13\xfb\x03f\x06\x0c0\x00\x00\x10\x00zB\xff\xc3\xfc\x18\xfc\x18x\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=130),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00 \x00 \x00@\x00@\x00\x10\x10\x10\x10\x10\x10      @@@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=126),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x0c6D\xba@\xeb\x13\xfb\x03f\x06\x0c0\x00\x00\x10\x00zB\xff\xc3\xfc\x18\xfc\x18x\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x10\x00\x10\x008888\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=126),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x01\x08\x07\x00?\x00?\x00?\x00\x7f\x00\xff\x00\x00\x03\x03\x0f\x0f????\x7f\x7f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00P\x80\x00\xf0\x04\xf8\x04\xf8\x04\xf8\x1e\xe0^\xa0\x00\x00\xd0\xd0\xf0\xf0\xfc\xfc\xfc\xfc\xfe\xfe\xfe\xfe\xfe\xfe'),
                            bytearray(b'\x11\xeeq\x0e\x7f\x00\x1f\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f????\x0f\x0f\x03\x03'),
                            bytearray(b'\xec\x00\xf4\x00\xf0\x00\xb0\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x01\x08\x07\x00?\x00?\x00?\x00\x7f\x00\xff\x00\x00\x03\x03\x0f\x0f????\x7f\x7f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00P\x80\x00\xf0\x04\xf8\x04\xf8\x04\xf8\x1e\xe0^\xa0\x00\x00\xd0\xd0\xf0\xf0\xfc\xfc\xfc\xfc\xfe\xfe\xfe\xfe\xfe\xfe'),
                            bytearray(b'\x11\xeeq\x0e\x7f\x00\x1f\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f????\x0f\x0f\x03\x03'),
                            bytearray(b'\xec\x00\xf4\x00\xf0\x00\xb0\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x0c6D\xba@\xeb\x13\xfb\x03f\x06\x0c0\x00\x00\x10\x00zB\xff\xc3\xfc\x18\xfc\x18x\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00 \x00 \x00@\x00@\x00\x10\x10\x10\x10\x10\x10      @@@@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=126),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x01\x08\x07\x00?\x00?\x00?\x00\x7f\x00\xff\x00\x00\x03\x03\x0f\x0f????\x7f\x7f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00P\x80\x00\xf0\x04\xf8\x04\xf8\x04\xf8\x1e\xe0^\xa0\x00\x00\xd0\xd0\xf0\xf0\xfc\xfc\xfc\xfc\xfe\xfe\xfe\xfe\xfe\xfe'),
                            bytearray(b'\x11\xeeq\x0e\x7f\x00\x1f\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f????\x0f\x0f\x03\x03'),
                            bytearray(b'\xec\x00\xf4\x00\xf0\x00\xb0\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x08\x08\x0e\x08/\x18\x1f\xb8\xff\xc0\xffp~\x00\x00\x08\x10\x0ep/\xf4\x1f\xe0\xffB\xff<~\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00 \x00 \x00@\x00@\x00\x10\x10\x10\x10\x10\x10      @@@@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=126),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x08\x08\x0e\x08/\x18\x1f\xb8\xff\xc0\xffp~\x00\x00\x08\x10\x0ep/\xf4\x1f\xe0\xffB\xff<~\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x10\x00\x10\x008888\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10\x10'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=126),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x01\x08\x07\x00?\x00?\x00?\x00\x7f\x00\xff\x00\x00\x03\x03\x0f\x0f????\x7f\x7f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00P\x80\x00\xf0\x04\xf8\x04\xf8\x04\xf8\x1e\xe0^\xa0\x00\x00\xd0\xd0\xf0\xf0\xfc\xfc\xfc\xfc\xfe\xfe\xfe\xfe\xfe\xfe'),
                            bytearray(b'\x11\xeeq\x0e\x7f\x00\x1f\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f????\x0f\x0f\x03\x03'),
                            bytearray(b'\xec\x00\xf4\x00\xf0\x00\xb0\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x01\x08\x07\x00?\x00?\x00?\x00\x7f\x00\xff\x00\x00\x03\x03\x0f\x0f????\x7f\x7f\x7f\x7f\xff\xff'),
                            bytearray(b'\x00\x00P\x80\x00\xf0\x04\xf8\x04\xf8\x04\xf8\x1e\xe0^\xa0\x00\x00\xd0\xd0\xf0\xf0\xfc\xfc\xfc\xfc\xfe\xfe\xfe\xfe\xfe\xfe'),
                            bytearray(b'\x11\xeeq\x0e\x7f\x00\x1f\x00\x1f\x00\x0c\x00\x00\x00\x00\x00\xff\xff\xff\xff\x7f\x7f\x7f\x7f????\x0f\x0f\x03\x03'),
                            bytearray(b'\xec\x00\xf4\x00\xf0\x00\xb0\x00\x80\x00\x00\x00\x00\x00\x00\x00\xff\xff\xff\xff\xff\xff\xfe\xfe\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x08\x08\x0e\x08/\x18\x1f\xb8\xff\xc0\xffp~\x00\x00\x08\x10\x0ep/\xf4\x1f\xe0\xffB\xff<~\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=130),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00 \x00 \x00@\x00@\x00\x10\x10\x10\x10\x10\x10      @@@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=126),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x80\x00`\x00|\x007\x08 \x1f7\x0f\x17\x0f\x17\x0f\x00\x80\x00`\x00|\x00?\x00?\x00?\x00\x1f\x00\x1f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=132),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x00`\x00|\x007\x08 \x1f7\x0f\x17\x0f\x17\x0f\x00\x80\x00`\x00|\x00?\x00?\x00?\x00\x1f\x00\x1f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x80\x00`\x00|\x007\x08 \x1f7\x0f\x17\x0f\x17\x0f\x00\x80\x00`\x00|\x00?\x00?\x00?\x00\x1f\x00\x1f'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00`\x00|\x007\x08 \x1f7\x0f\x17\x0f\x17\x0f\x00\x80\x00`\x00|\x00?\x00?\x00?\x00\x1f\x00\x1f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x08\x07\x03\x07\x03\x07\x00\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x0f\x00\x07\x00\x07'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=132),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x08\x07\x03\x07\x03\x07\x00\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x0f\x00\x07\x00\x07'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x08\x07\x03\x07\x03\x07\x00\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x0f\x00\x07\x00\x07'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x08\x07\x03\x07\x03\x07\x00\x00\x00\x00\x00 \x00\x10\x00\x0c\x00\x0f\x00\x07\x00\x07'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=134),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=134),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=122),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=135),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=135),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x00\x00\x00\x08\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00"\x00\x00\x00\x08\x00\x80\x00\x00\x00\x00\x00@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=121),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=0),
                        AnimationSequenceFrame(duration=12, mold_id=1),
                        AnimationSequenceFrame(duration=12, mold_id=2),
                        AnimationSequenceFrame(duration=12, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=3),
                        AnimationSequenceFrame(duration=12, mold_id=4),
                        AnimationSequenceFrame(duration=12, mold_id=5),
                        AnimationSequenceFrame(duration=12, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL411_SPORE_PINK_GREEN,
    palette_offset=1,
    unknown_num=8
)
