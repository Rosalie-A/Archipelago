
from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
sprite = CompleteSprite(
    animation=AnimationPack(246, length=141, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x0b\x18\t\x08\r\r\x00\x00\x00\x00\x00\x00\x00\x01\x0b\x02\x07\x00\x07\x02\x0e\x02'),
                            bytearray(b'  \x10p\x14\xf0\xb4\xf0\xe4\xe0\xc0\x08\xe0\x18\x0e\x08 \x10p\x08\xf0\xcc0L\xe0\x1c\x84\xb0$ \xf4\x12'),
                            bytearray(b'\n\x00\x00\x00\x17\x10\x11\x01\x19\x18\x0c\x08\x00\x00\x00\x00\x01\x1f\x07\n\x08\x0f\x1e\x04\x1f\x1e\x0c\x08\x00\x00\x00\x00'),
                            bytearray(b'\xc5\xc8\xe1\x1cpxh\x08\x90\x90\xb0\x90\xe0\xc0``\xb0\x8f\x00\xf3\xe0\x84\x88\xf4\xf0\x98\xf0\xd0\xe0\xc0``'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x04\x00\x00\x00\x00\x00 \x00\x03\x00\x01\x00\x00&\x00\x00\x00\x00\x00\x00\x00\x01\x03\x02\x03\x00\x03\x02\x19\x07'),
                            bytearray(b'  \x10p\x15\xf0\xb4\xf0\xe4\xe0\xc0\x08\xe0\x18\x0e\x08 \x10p\x08\xf0\xcc0L\xe0\x1c\x84\xb0$ \xf4\x12'),
                            bytearray(b'\x103\x00\x00\x0b\x08\x0f\x05\x0c\x0c\x0c\x0c\x02\x00\x00\x00\x0c\x07\x0f\x02\x14\x13\x1a\x10\x0f\x0e\x0f\x0f\x02\x00\x00\x00'),
                            bytearray(b'\r\x00\xc5,\xe8hh\x08\x00\x00\xc0\xc0\xc0\xc0\xc0\xc0\xf0\xcf\x14\xe3h\x94\x88\xf4\xc0\x88\xc0\xc0\xc0\xc0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x05\x00\n\x00\x05\x0b\x0b\x0b\x0b\x07\x03\x07\x03\x00\x00\x00\x05\x04\t\t\x02\x03\x04\x03\x04\x03\x04\x03\x04'),
                            bytearray(b'\x00\x00\xa0\xa0 $\x00\xfa\xb0\xf4\xfe\xfa\xfa\xfa\xb0\xb0\x00\x00@\xa0`\x94\xf4\x02\xf2\x08\xf8\x04\xfc\x00\xb4H'),
                            bytearray(b'\x04\x04\x0e\x08\x08\x00\x08\x00\x0b\x01\n\x02\x0e\x0e\x00\x00\x04\x07\x08\x0f\x08\x0f\x00\x0f\r\x07\x0e\x06\x0e\x0e\x00\x00'),
                            bytearray(b'\xcc\xc0\xee\xb8n|~~T@\xb4\x04T\x04\x1c\x1c\xc0\xfc\xb8\xc6|\x82~\x80@\xbe\x1c\xec\x1cL\x1c\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x03\x03\x00 \x00S\x07\'GGKC/\'\x19\x19\x00\x03\x00##DG\x08\'(3\x1c\x17\x08\t\x0f"),
                            bytearray(b'@@\x00\x00\x00\xe2`\xe5\xf8\xf2\xf1\xf1aa\x9a\x82\x80@\x80@\xe0\x02\xe2\x11\xf1\x08\xfa\x02n\x94\x84\xf8'),
                            bytearray(b'\x1d\x11\x10\x10\x0e\x00\x14\x00\x14\x04\x1d\x1c\x00\x00\x00\x00\x11\x1f\x10\x1f\x00\x0f\x18\x0f\x1c\x0f\x1c\x1d\x00\x00\x00\x00'),
                            bytearray(b'\xdcp\xdc\xf888\xcc\xcc\xa8\x80h\x08\xa8\x0888p\x8c\xf8\x048\xcc\xcc0\x80|8\xd88\x9888'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x06\x00\x00\x00\x07\x0e\x0f\x0f\x0f\x17G\x1e\xae3s\x01\x06\x01\x06\x07\x08\x0f\x10\x0f\x10\x07XN1\x13\x1f'),
                            bytearray(b'\x80\x80\x00\x00\x00\xc0\xc0\xc0\xf0\xe0\xe0\xe2\xc0\xc58\n\x00\x80\x00\x80\xc0\x00\xc0 \xe0\x10\xf0\x02\xda,\x04\xf0'),
                            bytearray(b'[B!!\x1c\x00\t\x01\x0b\x01\n\x02\x0f\x0e\x00\x00"\x1f!>\x00\x1f\x01\x0e\r\x06\x0e\x07\x0e\x0f\x00\x00'),
                            bytearray(b'\xb8\xe0\xb8\xf0pp\x98\x98P\x00\xd0\x10P\x10pp\xe0\x18\xf0\x08p\x98\x98`\x00\xf8p\xb0p0pp'),
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
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
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
    palette_id=685,
    palette_offset=0,
    unknown_num=0
)
