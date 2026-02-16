# SPR0934_TADPOLE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL719_TADPOLE
sprite = CompleteSprite(
    animation=AnimationPack(419, length=140, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18<|>\x9e\xdf_`\xce\x18>\x008\x00\x00\x00\x18\x00|z\xff<\xff\xa0\x1e8F\x008'),
                            bytearray(b'\x00\x00\x00\x00p\x00\x08\x00\x00\xfe`\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\x08\xf0\x00\xfe`\x10\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18||\xbe\xbe>\x9f\xdaVL4\x00\x18\x00\x00\x00\x18\x00|\xba\x7f|\xff\xb0n0L\x00\x18'),
                            bytearray(b'\x00\x00`\x0c\x80\x10\x00\xe0 \x80\x00\x00\x00\x00\x00\x00\x00\x00`\x1c\x80x\x00\xf0 \xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18<\x9c\x1e\xde\xdf\xe6\x02:\x04D\x00\x18\x00\x00\x00\x18`\xfc8\xffD?x\x87\x00|\x00\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00`\x00\x18\xc0\x000\xe0\x0c\x00\x00\x00\x00\x00\x00\x00\x00`\x80\x18\xe0\x00\xf8\xe0\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00>\x00c\x00@\x00@\x00d\x00`\x00\x00\x00\x00\x00><\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x7f'),
                            bytearray(b'\x00\x00\x00\x00\xf8\x00\x0c\x00\x0e\x00\xde\x00\xfe\x00|\x00\x00\x00\x00\x00\xf8p\xfc\xf8\xfe\xfc\xfe\xfc\xfe\xfc\xfc\xf8'),
                            bytearray(b'8\x00x\x00~\x00g\x00c\x00?\x00\x0f\x00\x00\x00??\x7f\x7f\x7f\x7f\x7f?\x7f??\x0e\x0f\x00\x00\x00'),
                            bytearray(b'>\x00?\x00w\x00\xe7\x00\xee\x00\xfc\x008\x00\x00\x00\xfe\xfc\xff\xfe\xff\xfe\xff\xfe\xfe\xfc\xfcp8\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00>\x00c\x00@\x00O\x00|\x00x\x000\x00\x00\x00>\x18\x7f?\x7f\x7f\x7f\x7f\x7f\x7f\x7f??\x1f'),
                            bytearray(b'\x00\x00\xf8\x00\x0c\x00\x8e\x00\xf6\x00\xfe\x00|\x00\x1e\x00\x00\x00\xf8p\xfc\xf8\xfe\xfc\xfe\xfc\xfe\xd8\xfc\xe0\xfe\xf8'),
                            bytearray(b'{\x00\x7f\x00c\x00g\x00?\x00\n\x00\x00\x00\x00\x00\x7f\x0f\x7f?\x7f?\x7f>?\x0c\n\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbf\x00\xe3\x00\xf7\x00\xfe\x00|\x00\x10\x00\x00\x00\x00\x00\xff\xfc\xff\xfe\xff>\xfe\x1c|@\x10\x10\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'>\x00c\x00O\x00\\\x00x\x00\x7f\x007\x00\x7f\x00>\x18\x7f?\x7f\x7f\x7f\x7f\x7fg\x7f\x0f?\x1c\x7f\x0e'),
                            bytearray(b'\xf8\x00\x0c\x00\xfe\x00v\x00>\x00p\x00\xda\x00\xfe\x00\xf8p\xfc\xf8\xfe\x1c\xfe\xfc\xfe\xd8\xf0\xc0\xfa\xe0\xfe|'),
                            bytearray(b"s\x00w\x00\'\x00\x08\x00\x02\x00\x00\x00\x00\x00\x00\x00\x7f\x1e\x7f.\'\x01\x08\x08\x02\x02\x00\x00\x00\x00\x00\x00"),
                            bytearray(b'\xe6\x00\xbc\x00@\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\xfe<\xbc\x08@@\x00\x00  \x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'>\x00g\x00_\x00`\x00O\x00\x00\x00\x1e\x00?\x00>\x18\x7f>\x7f8c\x03O\x01\x00\x00\x1e\x10?\x06'),
                            bytearray(b'\x98\x00l\x00~\x00\x9e\x00\xf6\x00\xe4\x00\x00\x00x\x00\x98\x10|x~\x0c\x9e\x00\xf6\x80\xe4@\x00\x00xp'),
                            bytearray(b'1\x00@\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x001\x00@\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbc\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbc\x08\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18<|>\x9e\xdf_`\xce\x18>\x008\x00\x00\x00\x18\x00|z\xff<\xff\xa0\x1e8F\x008'),
                            bytearray(b'\x00\x00\x00\x00p\x00\x08\x00\x00\xfe`\x00\x00\x00\x00\x00\x00\x00\x00\x00p\x00\x08\xf0\x00\xfe`\x10\x00\x00\x00\x00'),
                            bytearray(b'\x08\x08\x08\x08<<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x08\x00<\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=125),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18<|>\x9e\xdf_`\xce\x18>\x008\x00\x00\x00\x18\x00|z\xff<\xff\xa0\x1e8F\x008'),
                            bytearray(b'\x00\x00`\x0c\x80\x10\x00\xe0 \x80\x00\x00\x00\x00\x00\x00\x00\x00`\x1c\x80x\x00\xf0 \xc0\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1c\x1c\xa3\xa3ff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\xa3\x00f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=125),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18<|>\x9e\xdf_`\xce\x18>\x008\x00\x00\x00\x18\x00|z\xff<\xff\xa0\x1e8F\x008'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00`\x00\x18\xc0\x000\xe0\x0c\x00\x00\x00\x00\x00\x00\x00\x00`\x80\x18\xe0\x00\xf8\xe0\x1c\x00\x00'),
                            bytearray(b'\x1c\x1c\xa3\xa3ff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\xa3\x00f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=125),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=8, mold_id=8),
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL719_TADPOLE,
    palette_offset=0,
    unknown_num=8
)
