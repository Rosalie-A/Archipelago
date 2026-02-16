# SPR0220_GREEN_ITEM_COLLECTION

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(222, length=181, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x00\x1f\x00>\x01~\x01}\x03{\x04F|\x00\x00\x00\x03\x00\x03\x00 \x00p\x00p\x00#\x00\x03'),
                            bytearray(b'\x00\x00@@H@\x8c\x84\x86\x8e\x86\x8e\x1e\x04>\x00\x00\x00`\x80x\x80|\x00~\x08~\x08~\x80~\x80'),
                            bytearray(b'8:\x00\x00\x02\x02\x01\x03\x00\x07\x04\x07\x00\x00\x00\x00\x06\x03\x0f\x00\x01\x03\x00\x03\x00\x07\x00\x07\x00\x00\x00\x00'),
                            bytearray(b'|\x80\xf0\x00\x00\x00\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\xfc\x80\xf0\x00\xc0\xc0\xc0\xc0`\xe0`\xe0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x03\x06\x03\x0c\x00\x0c\x03\x02\x00\x00\x00\x18\x00\x1e\x01\x00\x03\x00\x07\x03\x0f\x03\x0e\x00\x07\x00\x0c\x00\x1c\x00>'),
                            bytearray(b'\x00\x80\x80\x80\x00 `\xf0`\xe0\x00\x10\x00\x08\xc0$@\xc0@\xe0\xe0\xf0\xf0\x10\xe0\x80\x10\x00\x08\x00\x04\x00'),
                            bytearray(b">\x01?\x009\x06;\x1cd\' \x00\x11\x00\x05\x00\x00>\x00|\x00x\x00`X\x00?\x00\x1f\x00\x07\x00"),
                            bytearray(b'\xf8\x04\xf8\x06\xf8\x06\xfc\n\\\xc2x\x04\xf0\x08\xc0 \x04\x00\x02\x00\x02\x00\x06\x00>\x00\xfc\x00\xf8\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x00\x04\x07\x02\x00\x04\x00\x0c\x00\x0f\x10\x1f\x01\x00\x0f\x00\x0f\x07\x00\x00\x03\x00\x04\x00\x08\x00\x0f\x00\x16'),
                            bytearray(b'\xf0\x00\xf0\x00 \xe0@\xc0\x00 \x00\x10\xe0\x08\xf8\x10\x00\xf0\x00\xf0\xe0\x00\xc0\x80 \x00\x10\x00\x08\xe0H '),
                            bytearray(b'\x1e\x00\x1f\x00\x1f\x00\x1a\x06\x19\x06\x1a\x06\x1a\x06\n\x06\x03\x14\x00\x07\x00\x07\x01\x00\x01\x03\x01\x00\x01\x00\x01\x00'),
                            bytearray(b'\xf8\x90\xf0\x08\xe0\x18\x80x\xc0\xf8\x80x\x80x\x80pH \x98`\x18\xe0\xf8\x008\xc0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0e\x01\x0e\x01\x0e\x01\x0e\x01\x0e\x01\r\x03\r\x03\x05\x03\x01\x06\x01\x06\x01\x06\x01\x06\x01\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10\xf8\x90x\x10\xf8\x908\x908@8@8`\x10\xf8 x\xa0\xf8`8\xe08\xe0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0e\x01\x0e\x01\x0e\x01\x0e\x01\x0e\x01\r\x03\r\x03\x05\x03\x01\x06\x01\x06\x01\x06\x01\x06\x01\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10\xb8\x90x\x90x\x10\xb8\x908@8@8`\x10\xb8`x\xa0x\xa0\xb8`8\xe0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0f\x00\x0f\x00\x0c\x02\x0c\x02\x0f\x00\r\x03\r\x03\x05\x03\x00\x07\x00\x07\x03\x07\x03\x07\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x008\x00\x18\x008\x008\x808@8@8`\x10\xf8\xf0\xb8\xf0\xb8\xf0\xb8\xf08\xf0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0f\x00\x0f\x00\x0e\x00\x0f\x00\x0f\x00\r\x03\r\x03\x05\x03\x00\x07\x02\x05\x01\x06\x00\x07\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x908\x108P8\x108\x908@8@8`\x10\xb8`\xb8@\xf8 \xb8`8\xe0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0e\x01\x0e\x01\x0e\x01\x0e\x01\x0f\x00\r\x03\r\x03\x05\x03\x01\x06\x01\x06\x01\x06\x01\x06\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10\xf8\x90x\x10\xb8\x90x\x908@8@8`\x10\xf8 x\xa0\xb8`x\xa08\xe0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x00\x06\x02\x07\x02\x1f\x03\x19\x00\x0f\x00\n\x06\x0f\x00\x00|\x02\x04\x02\x05\x03\x1c\x00\x1f\x00\x07\x01\x00\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\xf0\x00|\x00\xfc\x00\xf0\x08\x80x\x908\x00\x00\x00\x00\x00\xf0\x00\xfc\x00\xfc\x08\xf0\xf8\x008\xe0'),
                            bytearray(b'\x0f\x00\x0c\x03\x0e\x01\x0e\x01\x0f\x00\r\x03\r\x03\x05\x03\x00\x07\x03\x04\x01\x06\x01\x06\x00\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10\xb8\x10\xf8\x10\xf8\x90x\x908@8@8`\x10\xb8`\xf8\x00\xf8 x\xa08\xe0\xf8\x00\xf8\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x18\x108\x10\x98@\xd7L\x0f\x08\x0f\x10\x0f\x10\x1c\x03\x00\x00\x00\x000\x000\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00@\x00PP\xc8p\xe8\x10(\x00\x00\x00\x00\x00\x00@\x80p\xc08\x00\x18\x008\xe0'),
                            bytearray(b'\x19\x07\x1b\x07\n\x16\n\x06\x06\x07\x00\x00\x00\x00\x00\x00\x00\x18\x00\x18\x01\x00\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\x18 \xb8\xa0X\x80p\x93\xeb\x00\x03\x1e\x0c\x18\x08\x18\xe0\xb8\xc0\xf8\x00\xf0\x00\xfc\x00\x1f\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x00\x1f\x00?\x00\x7f\x00\x7f\x00\xff\x00\xfc\x03y\x82\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x03\x0c\x02\r'),
                            bytearray(b'\xe0\x00\xe8\x18\xc88\x9ax4\xf2\x18\x17\x10\x9f\x90\x7f\x00\x00\x00\x00\x04\x00\x06\x00\x0e\x00\x1f\xe0\x9f`\x7f\xa0'),
                            bytearray(b'\x80\xf3pr\x80\x0fp\x0f\x00\x7f\x00?\x00\x1f\x00\x07\x03\x0c\x82\r\xff\x0c\x7f\x0f\x7f\x00?\x00\x1f\x00\x07\x00'),
                            bytearray(b'\x10\xff\x10\x7f\x10\xff\xf0\xfe\x00\xfe\x00\xfc\x00\xf8\x00\xe0\xff`\x7f\xa0\xff \xfe\x00\xfe\x00\xfc\x00\xf8\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=4),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=8),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=10),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL384_YELLOW_JUICE,
    palette_offset=0,
    unknown_num=8
)