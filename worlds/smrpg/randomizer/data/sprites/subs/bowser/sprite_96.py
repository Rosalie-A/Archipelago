
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(84, length=88, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'#402\x07;#>/\x1e\x15\x02\x02\x00\x19\x1c\x13\x10\x05\x02?8 4 \x11\x1f\n\x0f\t\x03\x04'),
                            bytearray(b'J\x00H\x06\xba\x0c\xc0\x1c<\x9c\xb0XL\xb0\x9c\x18@\x00\xaaj\xf0\x10|<\xacL\xe0H\x0c\xf0\xfc|'),
                            bytearray(b'\x04\x1f\x1b\x0c\xbeQ8\xc7\xea\x17w\x08q\x08\x01\x00\x01\x1b\x11\x06\xe0\xe0\xf0\xe0\xe9\x15q\x0eq\x08\x01\x00'),
                            bytearray(b'0<z\x848\xc4\xf8\x04\xf8\x00\xc8 \xd0 \xc0\x00\xfc\xfcf\x9c$\\d\x1c \x18\xd80\xd0 \xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'#4p2\x07;#~/\x1e\x15\x02\x82\x00Y\x1c\x13\x10\x05\x02?8`t \x11\x1f\n\x8f\x89\x03\x04'),
                            bytearray(b'J\x00H\x06\xba\x0c\xc0\x1c<\x9c\xb2XL\xb0\x9c\x18@\x00\xaaj\xf0\x10|<\xacL\xe0H\x0c\xf0\xfc|'),
                            bytearray(b'\x04\x1f\x1b\x0c\xbeQ;\xc4\xef\x10w\x08w\x08\x00\x00\x01\x1b\x11\x06\xe0\xe0\xf0\xe0\xef\x10w\x08w\x08\x00\x00'),
                            bytearray(b'0<z\x848\xc4\xf8\x048\x80r\x80\x00\x00\x00\x00\xfc\xfcf\x9c$\\d\x1c`\xd8p\x80\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x08\x01\x0c\xa0\x08(\xc8\xc0h\xf2\xd0\xe5\xba@?\x07\x01\x07\x04\x07\x04\xa7\xe0\x07h\x1fX=\x05\x7f@'),
                            bytearray(b'\x00@\x80\xc0(\x80H0\x980\xf8\xd88\xe8\x10\xe0\x00@\x00@\x00\x80\xe8\xb8\x00\xb0\xc0\xd0\xe0\x00\xf0\x10'),
                            bytearray(b'@?o?X\x08`\x02G:\x7f"tGp\x03=\x00-\x00\x087@\x7fe \x18} UD7'),
                            bytearray(b'\x10\xe0\xb0\xe0\xd0\x800\x00\x10\xe0\xf0 p\x10p\x10\xe0\x00\xa0\x00\x80`\x10\xf00 \xc0\xf0 P\x00p'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x04\xa0\x06 \xc4\xc4d\xc0\xe4yh2\x1d \x1f\x03\x00\x03\x02\xa3\xe2\x03`\x03d\x0f,\x1e\x022-'),
                            bytearray(b"@\x00` \x05 \x01\x06#\x06\xb3\'[\xb7\x0e\xf6\xc0@\xc0\x00\xc0 \xe5\'\xc0&\xe0&pDX\xa8"),
                            bytearray(b' \x1f \x1f7\x1fp\x01c=~As\x03\x01\x01? \x1e\x00\x16\x00`?\x12p,^@2\x02\x03'),
                            bytearray(b'\x08\xf0\x08\xf0\xf8\xf0\x18\x80\xc8\xb0\xf8\x90\x18\xc8\x18\xc8\xf8\x08p\x00p\x00\x08\xf8X\x10 x\x10H\x00\xd8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x04\x00\x06\x00\x04\xa4\x04 \xc4\xd9h\xf2\xdd`_\x03\x00\x03\x02\x03\x02\x03\x00\xa3\xe4\x0fl\x1eB\x12\r'),
                            bytearray(b"@\x00` \x00 \x00\x00%\x00\xb1&[\xb6\x0b\xf7\xc0@\xc0\x00\xc0 \xe0 \xc0 \xe5\'pFX\xae"),
                            bytearray(b' \x1f \x1f7\x1f0\x01\x13\r\x1e\x11\x1f\x03\x01\x01? \x1e\x00\x16\x00 ?\x02\x10\x0c\x16\x10\x0e\x02\x03'),
                            bytearray(b'\x0b\xf7\x0e\xf6\xf8\xf0\x18\x80\xc8\xb0\xf8\x90\x18\xc8\x18\xc8\xf8\x0cp\x00p\x00\x08\xf8X\x10 x\x10H\x00\xd8'),
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
    palette_id=664,
    palette_offset=0,
    unknown_num=0
)
