
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(83, length=98, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x04\x01\x05\x00\x06\x0c\x00\x1f\x00\x1d\x03\x05\x18\x1e\x00\x00\x05\x05\x0b\x01\x15\x08\x00\x1b\x02\x17\x18\x08\x01\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00@\xc0\xe0\xe0\xb0\xb0\x10\x10\x90\xd0\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xe0@\xb0\xe0\x10 P'),
                            bytearray(b'\x03\x18\x1a\x06 \x1f\x18\x1f\x1f\x07\x1f\x1e\x11\x11\x00\x00\x1f\x00\x04\x05? \x1f \x1f \x1f>\x11\x1f\x00\x07'),
                            bytearray(b'\xc0@\xe0\x900\xc00\xd0\xb0\xd0\x90\xd0\xd0\x00` \xb0@\xe8\x10\xd0\x00\xd0\x10\xf00\xd00\xd0 `\xa0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x04\x01\x05\x00\x06\x0c\x00\x1f\x00\x1d\x03\x05\x18\x1e\x00\x00\x05\x05\x0b\x01\x15\x08\x00\x1b\x02\x17\x18\x08\x01\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00@\xc0\xe0\xe0\xa0\xa0\x10\x10\x80\xc0\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xe0@\xa0\xe0\x10 @'),
                            bytearray(b'\x03\x18\n\x06\x10\x0f\x0f\x0f\x0f\x01\x0f\x0e\x08\x08\x00\x00\x1f\x00\x04\x05\x1f\x10\x0f\x10\x0f\x10\x0f\x1e\x08\x0f\x00\x00'),
                            bytearray(b'\xc0@\xe0\x90p\xa0`\xa0 \xa0\xa0\x00\xc0@\x00\x00\xb8@\xe8\x10\xb8 \xe0`\xa0`\xa0@\xc0@\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x00\x0b\x0c"? /\x18\x0f\x01\x01\x06\x07\x00\x00\x07\x07\x05\r\x00?\x10,\x10\x0c\x1e\x018\x07'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x00\xc0\x18\xc0\xbc\x80\xd8\xc0(\xf0\x00\x00\x00\x00\x80\x00\x00\xc0\x18Xd\xa4(\xc8\x18\xb8'),
                            bytearray(b'\x0c\x0fH\x0f,\x0f\x17\x07\x0e\x00\x0f\x0e\r\x00\x05\x04p\x0fp\x0e0\x0f\x18\x07\x0f\x00\x0f\x0e\r\x02\x05\x06'),
                            bytearray(b' \xe0\x00\xe00\xe0\xd0\xc0\x00 pp\xe0\xe0\xe0\xe0\x00 \x00 \x10p \xc0\xe0\x10p\x80\xe0\x10\xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x00\x05\x06\x11\x1f\x10\x17\x0c\x07\x01\x01\x06\x07\x00\x00\x03\x03\x02\x06\x00\x1f\x08\x16\x08\x06\x1e\x01\x18\x07'),
                            bytearray(b'\x00\x00\x80\x00\xc0@\x00\xe0\x00\xe0P\xc0\xd8\xc08\xe0\x00\x00\x80\x80\xc0\x80\x00\xe0\x00 0P(\xc8\x08\xa8'),
                            bytearray(b'\x06\x07$\x07\x16\x07\x0b\x03\x0e\x00\x1f\x0e\x1d\x00\r\x048\x078\x06\x18\x07\x0c\x03\x0f\x00\x1f\x0e\x1d\x02\r\x06'),
                            bytearray(b'0\xe8\x10\xe8 \xf0\xc0\xd0\x00 pp\xe0\xe0\xe0\xe0\x188\x188\x10p0\xd0\xe0\x10p\x80\xe0\x10\xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x00\x05\x06\x11\x1f\x10\x17\x0c\x07\x01\x01\x06\x07\x00\x00\x03\x03\x02\x06\x00\x1f\x08\x16\x08\x06\x1e\x01\x18\x07'),
                            bytearray(b'\x00\x00\x80\x00\xc0@\x00\xe0\x00\xe0@\xc0\xc0\xc0(\xe0\x00\x00\x80\x80\xc0\x80\x00\xe0\x00  @ \xc0\x08\xa8'),
                            bytearray(b'\x06\x07$\x07\x16\x07\x0b\x03\x0e\x00\x0f\x0e\x1d\x00\r\x058\x078\x06\x18\x07\x0c\x03\x0f\x00\x0f\x0e\x1d\x02\r\x06'),
                            bytearray(b'<\xe0\x18\xe0(\xf0\xc0\xd0\x00 pp\xe0\xe0  \x144\x188\x18x0\xd0\xe0\x10p\x80\xe0\x10 \xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x00\x05\x06\x11\x1f\x10\x17\x0c\x07\x01\x01\x06\x07\x00\x00\x03\x03\x02\x06\x00\x1f\x08\x16\x08\x06\x1e\x01\x18\x07'),
                            bytearray(b'\x00\x00\x80\x00\xc0@\x00\xe0\x00\xe0@\xc0\xc0\xc0 \xe0\x00\x00\x80\x80\xc0\x80\x00\xe0\x00  @ \xc0\x00\xa0'),
                            bytearray(b'\x06\x07$\x07\x16\x07\x0b\x03\x0e\x00\x1f\x0e\x1d\x00\r\x048\x078\x06\x18\x07\x0c\x03\x0f\x00\x1f\x0e\x1d\x02\r\x06'),
                            bytearray(b' \xf0\x10\xe80\xe8\xc0\xd0\x00 pp\xe0\xe0\xe0\xe0\x100\x08(\x18x0\xd0\xe0\x10p\x80\xe0\x10\xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
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
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                    ]
                ),
            ]
        )
    ),
    palette_id=654,
    palette_offset=0,
    unknown_num=0
)
