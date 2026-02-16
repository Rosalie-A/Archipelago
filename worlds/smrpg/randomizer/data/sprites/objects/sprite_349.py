# SPR0349_GOOMBETTE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL109_GOOMBETTE
sprite = CompleteSprite(
    animation=AnimationPack(33, length=291, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x07\x02\x07\x00\x07\x00\x0f\x01\r\x0b\x00\x00\x00\x00\x01\x00\x07\x04\x07\x02\x07\x03\x0e\x02\x06\t'),
                            bytearray(b'\x00\x00\xe0`\xe0 p\xf0\x00\xe0T\xe0\xf40\xf40\x00\x00\xe0\x00\xf0\x10\xb8\x08\xe8x\xe8\xbc\xf0\x8c\xf2\x8e'),
                            None,
                            bytearray(b'\x07\x00\x03\x00\x01\x01\t\x02\x12\x03\x07\x02\x03\x03\x00\x00\r\n\x06\x05\x02\x03\x0c\x00\x1c\x00\x0f\x00\x03\x03\x00\x00'),
                            bytearray(b'\xf2\xb0\xd6p8\xa4L\xb4<\xccN\x86\xdf\xe7\\Lr\x0eP\xae\xb4\\|\xbc<\x9c~\x02\x9f\x87<\x04'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x07\x02\x07\x00\x07\x00\x0f\x01\r\x0b\x00\x00\x00\x00\x01\x00\x07\x04\x07\x02\x07\x03\x0e\x02\x06\t'),
                            bytearray(b'\x00\x00\xe0`\xe0 p\xf0\x00\xe0T\xe0\xf40\xf40\x00\x00\xe0\x00\xf0\x10\xb8\x08\xe8x\xe8\xbc\xf0\x8c\xf2\x8e'),
                            None,
                            bytearray(b'\x07\x00\x03\x00\x00\x01\x05\x02\x0e\x07\x07\x06\x03\x03\x00\x00\r\n\x06\x05\x03\x02\x04\x00\x08\x00\x07\x00\x03\x03\x00\x00'),
                            bytearray(b'\xf2\xb0\xd6p8\xa4L\xb4<\xcc\x9cL\xbe\x8e\xbc\x9cr\x0eP\xae\xb4\\|\xbc<\x9c\xbc\x04~\x0e|\x0c'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x07\x02\x07\x00\x07\x00\x0f\x01\r\x0b\x00\x00\x00\x00\x01\x00\x07\x04\x07\x02\x07\x03\x0e\x02\x06\t'),
                            bytearray(b'\x00\x00\xe0`\xe0 p\xf0\x00\xe0T\xe0\xf40\xf40\x00\x00\xe0\x00\xf0\x10\xb8\x08\xe8x\xe8\xbc\xf0\x8c\xf2\x8e'),
                            None,
                            bytearray(b'\x07\x00\x03\x00\r\x01\x05\x02&\x13?\x02\x0f\x0f\x00\x00\r\n\x06\x05\x0e\x03\x1c\x00,\x00?\x00\x0f\x0f\x00\x00'),
                            bytearray(b'\xf2\xb0\xd6p8\xa4L\xb4>\xceo\xc7\xef\xe3~fr\x0eP\xae\xb4\\|\xbc>\x9e\x7fA\xdf\xc3~B'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x01\x03\x00\x05\x06\x04\x02\x08\x06\x1a\x16\x00\x00\x01\x00\x01\x00\x0f\x0c\x15\x12\x06\x01\x0e\x01\x0e\x01'),
                            bytearray(b'\x00\x00\xc0\x00\xc0\xc0 \x108\x00\xf0\x0c0\x0c`\x1c\x00\x00\xe0 \xd00\x10\xf0\x00\xf8\x0c\xfc\x0c\xfc\x1c\xfc'),
                            None,
                            bytearray(b'\x12\x1e\x02\x1e\x1c\x1d\x00\x0b\x01\x02\x14\x13\x01\x00\x01\x00\x1e\x01\x1e\x01\x1d\x03\x0b\x07\x07\x07\x0f\x01\x1f\x00\x07\x00'),
                            bytearray(b'\xe0\x1c\xc80\x1c\xec<\xcc\xf4\x0c\xfc\x1cxx@@\x1c\xfc8\xf8\xec\xfc\xec\xfc\xcc\xf4\xdc\xe4\xf8\xf8\xc0\xc0'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x01\x03\x00\x05\x06\x04\x02\x08\x06\x1a\x16\x00\x00\x01\x00\x01\x00\x0f\x0c\x15\x12\x06\x01\x0e\x01\x0e\x01'),
                            bytearray(b'\x00\x00\xc0\x00\xc0\xc0 \x108\x00\xf0\x0c0\x0c`\x1c\x00\x00\xe0 \xd00\x10\xf0\x00\xf8\x0c\xfc\x0c\xfc\x1c\xfc'),
                            None,
                            bytearray(b'\x12\x1e\x02\x1e\x1c\x1d\x00\x0b\t\x029&" \x02\x00\x1e\x01\x1e\x01\x1d\x03\x0b\x07\x0f\x07\x1f\x03\x1f\x01\x0f\x01'),
                            bytearray(b'\xe0\x1c\xc80\x18\xe8<\xcc\xf2\x0e\xfe^\xfc\xfc\x80\x80\x1c\xfc8\xf8\xe8\xf8\xec\xfc\xce\xf2\xde\xe2\xfc\xfc\x80\x80'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x01\x03\x00\x05\x06\x04\x02\x08\x06\x1a\x16\x00\x00\x01\x00\x01\x00\x0f\x0c\x15\x12\x06\x01\x0e\x01\x0e\x01'),
                            bytearray(b'\x00\x00\xc0\x00\xc0\xc0 \x108\x00\xf0\x0c0\x0c`\x1c\x00\x00\xe0 \xd00\x10\xf0\x00\xf8\x0c\xfc\x0c\xfc\x1c\xfc'),
                            None,
                            bytearray(b'\x12\x1e\x02\x1e\x1c\x1d\x00\x0b\x01\x02\n\t\x00\x01\x00\x00\x1e\x01\x1e\x01\x1d\x03\x0b\x07\x07\x07\x07\x00\x0e\x00\x03\x00'),
                            bytearray(b'\xe0\x1c\xc80\x10\xf00\xd0\xe8\x18x\x98\xb00\x80\x00\x1c\xfc8\xf8\xf0\xf0\xf0\xf0\xd8\xe8\xd8\xe8\xf0p\xe0`'),
                            None,
                            None,
                            None,
                            None,
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=123),
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=123),
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
