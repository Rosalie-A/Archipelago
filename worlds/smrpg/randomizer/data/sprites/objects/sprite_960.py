# SPR0960_GOOMBETTE_LOWER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL109_GOOMBETTE
sprite = CompleteSprite(
    animation=AnimationPack(268, length=285, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b"\x0e\x06\x1e\x02w/p\x0eu\x0e\xff\x13\xdf\xb3\x7f\x0b\x0e\x00\x1f\x01{@~'~;\xef(o\x98\xd7\xa0"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00@\x00 \x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\xc0\x00\xc0 \xe0 \xe0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'=\x07\x13\x1a\x94+#<t(=>\x05\x04\x00\x00eZ+5\xc7\x0b\xc3\t\xf7\x0098\x03\x00\x00\x00'),
                            bytearray(b'`\x00\x80@\xc0@\xc0\xc0\xe0`\xf0p\xc0\xc0\x00\x00\x00\xe0@\xc0\xc0\xc0\xc0\xc0\xe0 \xf0p\xc0@\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b"\x0e\x06\x1e\x02w/p\x0eu\x0e\xff\x13\xdf\xb3\x7f\x0b\x0e\x00\x1f\x01{@~'~;\xef(o\x98\xd7\xa0"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00@\x00 \x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\xc0\x00\xc0 \xe0 \xe0'),
                            None,
                            bytearray(b'=\x07\x03\x1aT+\xe3|yd;8\x0b\t\x00\x00eZ;%G\x0b\x83\t{\x0070\x07\x00\x00\x00'),
                            bytearray(b'`\x00\x80@\xc0@\xc0\xc0\xc0\xc0\xe0\xe0\xc0\xc0\x00\x00\x00\xe0@\xc0\xc0\xc0\xc0\xc0\xc0@\xe0\xe0\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            bytearray(b"\x0e\x06\x1e\x02w/p\x0eu\x0e\xff\x13\xdf\xb3\x7f\x0b\x0e\x00\x1f\x01{@~'~;\xef(o\x98\xd7\xa0"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\x00@\x00@\x00 \x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\xc0\x00\xc0 \xe0 \xe0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'=\x07\xd3\x1aT+c<\xf6,\xfe\xfe\x07\x06\x00\x00eZ\xeb5\xc7\x0b\xc3\t\xf7\x04\xfd\xfc\x07\x04\x00\x00'),
                            bytearray(b'`\x00\x80@\xc0@\xe0\xe0\xf0p\xf00\xe0`\x00\x00\x00\xe0@\xc0\xc0\xc0\xe0\xe0\xf0\x10\xf00\xe0 \x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x0c\x10\x0c\x1c2\x01S`O \x83`\xa6a.\xe1\x1e\x02\x1d\x03\xf1\xcfP/`\x1f\xe0\x1f\xe1\x1f\xe1\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\x00\x01\x01\x01\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b',\xe3\xc1\xde\x03\xbc\x1f O1\x17\x07\x14\x04\x00\x00\xe3\x1f\xde?\xbe\x7f|\x7f\xfd\x1e\xff\x0f|\x0c\x00\x00'),
                            bytearray(b'\x80\x00\xc0\xc0\xc0\xc0@\xc0\xc0\xc0\x80\x80\x00\x00\x00\x00\x80\x80\xc0\xc0\xc0\xc0\xc0@\xc0@\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x0c\x10\x0c\x1c2\x01S`O \x83`\xa6a.\xe1\x1e\x02\x1d\x03\xf1\xcfP/`\x1f\xe0\x1f\xe1\x1f\xe1\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\x00\x01\x01\x01\x00\x00\x00\x00\x03\x02\x02\x02\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b',\xe3\xc1\xde\x03\xbc\x9f \x9fe/\x0f(\x08\x00\x00\xe3\x1f\xde?\xbe\x7f\xfc\x7f\xfd>\xff\x1f\xf8\x18\x00\x00'),
                            bytearray(b'\x80\x00\x80\x80\xc0\xc0 \xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x80\x80\x80\x80\xc0\xc0\xe0 \xe0 \xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x0c\x10\x0c\x1c2\x01S`O \x83`\xa6a.\xe1\x1e\x02\x1d\x03\xf1\xcfP/`\x1f\xe0\x1f\xe1\x1f\xe1\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x00\xc0\x00\xc0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b',\xe3\xc1\xdf\x03\xbd\x1e!\xa7\x99\x0b\x13\x08\x00\x00\x00\xe3\x1f\xdf?\xbf\x7f}~}\x0e\xef\x07>\x06\x00\x00'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\t\x02\x12\x03\x07\x02\x03\x03\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x1c\x00\x0f\x00\x03\x03\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf0\xe0H\xb0|\x8cN\x86\xdf\xe7\\L\x00\x00\xe0\x000\xd0x\xb8|\x9c~\x02\x9f\x87<\x04'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x0b\x03\x11\x02\x0e\x03\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x01\x1c\x00\x0c\x00\x01\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\xd0\xe0F\xb2O\xb3\x8ef\x1c\x1c\x00\x00\x00\x00\xc0\xc0p\xb0~\xb0o\xa3\xfeb\x1c\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x0088\xfc\xfcxx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0088\xfc\xfcxx\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=125),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\t\x02\x12\x03\x07\x02\x03\x03\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x1c\x00\x0f\x00\x03\x03\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf0\xe0H\xb0|\x8cN\x86\xdf\xe7\\L\x00\x00\xe0\x000\xd0x\xb8|\x9c~\x02\x9f\x87<\x04'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x0e\x05\x1e\x01?\x02;&\x0f\x01\x0f\x00\x01\x00\x03\x00\x0f\x08\x1f\x06=\x05\x1d#2<\x0c\x03'),
                            bytearray(b'\xc0@\xe0`\xf0\xf0\x04\xe04\xf0\xf40\xf30\xd7\xf0\xe0 \xf0\x108\x08\xe8\xfc\xf0\xcc\xf2\x0e\xf3\x0f\xd0/'),
                            None,
                            bytearray(b'\xce\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\t\x02\x12\x03\x07\x02\x03\x03\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x1c\x00\x0f\x00\x03\x03\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf0\xe0H\xb0|\x8cN\x86\xdf\xe7\\L\x00\x00\xe0\x000\xd0x\xb8|\x9c~\x02\x9f\x87<\x04'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=371),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\t\x02\x12\x03\x07\x02\x03\x03\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x1c\x00\x0f\x00\x03\x03\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf0\xe0H\xb0|\x8cN\x86\xdf\xe7\\L\x00\x00\xe0\x000\xd0x\xb8|\x9c~\x02\x9f\x87<\x04'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\t\x02\x12\x03\x07\x02\x03\x03\x00\x00\x00\x00\x00\x00\x00\x01\x0c\x00\x1c\x00\x0f\x00\x03\x03\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf0\xe0H\xb0|\x8cN\x86\xdf\xe7\\L\x00\x00\xe0\x000\xd0x\xb8|\x9c~\x02\x9f\x87<\x04'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=123),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=369),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\t\x01\x13\x02\x07\x02\x07\x07\x03\x03\x07\x07\x00\x00\x00\x00\x0c\x01\x1e\x00\x0f\x00\x07\x05\x03\x03\x07\x07'),
                            bytearray(b'\x00\x00pp\xf8\xe0H\xb0\x9c\x0c\xbc\x9c\xfe\x8e\xf8\xf8\x00\x00p\x008\xd8x\xb8\xfc\x1c|\x04\xfe\x8e\xf8\xe8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=122),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\t\x01\x13\x02\x07\x02\x07\x07\x03\x03\x07\x07\x00\x00\x00\x00\x0c\x01\x1e\x00\x0f\x00\x07\x05\x03\x03\x07\x07'),
                            bytearray(b'\x00\x00pp\xf8\xe0H\xb0\x9c\x0c\xbc\x9c\xfe\x8e\xf8\xf8\x00\x00p\x008\xd8x\xb8\xfc\x1c|\x04\xfe\x8e\xf8\xe8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=122),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x07\x00\x0e\x01\x06\x01\x0e\x01\x0f\x01\r\x03\x0b\x00\x01\x00\x07\x04\x0f\x0c\x07\x04\x0f\x07\x0e\x04\x0e\x01\x0c\x07'),
                            bytearray(b'\xc0\xc0\xc0@\xe0\xe0\x08\xc0\xec\x00\xf4\x10\xf8\x19\xfaY\xc0\x00\xe0 p\x10\xd0\xf8\xf0\x9c\xf2\x8e\xf9\x87\xb9\x07'),
                            bytearray(b'\x07\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x03\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc;\xfc\x12\xc0(\x80\x08\xc0\xf0\x00\x00\x00\x00\x00\x00;\xc7\x1e\xee\x08\xf8\x08\xf8\xf00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x0b\x03\x11\x02\x0e\x03\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x01\x1c\x00\x0c\x00\x01\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\xd0\xe0F\xb2O\xb3\x8ef\x1c\x1c\x00\x00\x00\x00\xc0\xc0p\xb0~\xb0o\xa3\xfeb\x1c\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=123),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x01\x03\x00\x03\x00\x07\x00\x06\x05\x03\x00\x00\x00\x00\x00\x03\x02\x03\x01\x03\x01\x07\x01\x03\x04\x06\x05'),
                            bytearray(b'p0\xf0\x10\xb8x\x80p\xaap\xfa\x98\xfa\x98\xf9Xp\x00\xf8\x08\xdc\x04\xf4<\xf4\xdexFy\xc7\xb9\x07'),
                            bytearray(b'\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xeb8\x1c\xd2$8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00(\xd7\xda.<\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x0b\x03\x11\x02\x0e\x03\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x01\x1c\x00\x0c\x00\x01\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\xd0\xe0F\xb2O\xb3\x8ef\x1c\x1c\x00\x00\x00\x00\xc0\xc0p\xb0~\xb0o\xa3\xfeb\x1c\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=123),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=8, mold_id=14),
                        AnimationSequenceFrame(duration=6, mold_id=15),
                        AnimationSequenceFrame(duration=6, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=6, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL109_GOOMBETTE,
    palette_offset=0,
    unknown_num=0
)