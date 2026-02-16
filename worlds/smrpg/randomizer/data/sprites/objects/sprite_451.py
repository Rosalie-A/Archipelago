# SPR0451_JINX_2

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL581_JINX_CLONE
sprite = CompleteSprite(
    animation=AnimationPack(67, length=364, unknown=0x0002,
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
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x01\x03\x01\x03\x01\x07\x04\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00'),
                            bytearray(b'\x00p0\xf0@\xc0\x80\x80\x80\x80@\xc0 \xe0\x80\xc0\x00p\x00\xf0\x00\xe0\x80\xc0\x80\x80\x00\x00\x00\x00 \x80'),
                            bytearray(b'\x04\x02\x04\x0f\x02\x17\x05\x07\x00\x07\x00\x00\x01\x03\x03\x03\x01\x01\x00\x00\x0f\x00\x05\x00\x00\x00\x01\x00\x01\x01\x03\x03'),
                            bytearray(b'\x90\x10\xa8\xb8\xc8\xf80|\x18~hhpp0\xf0p\x80x\x04\xf8\x04\xbc\x13\x9e\x19\x98\x08\xf0p00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x0e\x06\x1e\x088\x10p0pP\xf0H\xf8 \xf0\x00\x0e\x00\x1e\x00<\x10x\x10p\x00\xc0\x00\xc0\x08 '),
                            bytearray(b'\x01\x00\x01\x01\x02\x07\x05\x07\x00\x03\x00\x00\x01\x03\x01\x01\x00\x00\x00\x00\x07\x00\x05\x00\x00\x00\x01\x00\x01\x01\x01\x01'),
                            bytearray(b'$\x84(\xec\xcc\xfc2~8\xfe~\xfepp0\xf0\\`\x1c\x02\xfc\x00\xbe\x10>8>8\xf0x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x07\x03\x0f\x04\x1c\x088\x188\x18x$\xfc\x90x\x00\x07\x00\x0f\x00\x1e\x088\x088\x00p\x00`\x04\x10'),
                            bytearray(b'\x00\x01\x00\x01\x02\x03\x02\x03\x00\x01\x00\x01\x06\x06\x02\x03\x00\x00\x01\x00\x03\x00\x02\x00\x00\x00\x02\x00\x07\x06\x02\x02'),
                            bytearray(b'\x90@\x96\xf6l\xfc\x00pH\xf8\xc0\xf0\xe0\xe0`\xe0,0\x0e\x00\xfc\x00\xf0\x08x@pL\xe0\xfc``'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=114),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x06\x03\x07\x02\x0e\x00\x0c\x06\x0e\x05\x0f\x00\x1f\x12\x0f\x00\x06\x00\x07\x00\x0f\x00\x0f\x02\x0e\x00\x0c\x00\x08\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe4\x04|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00d\x00\xfc\x00'),
                            bytearray(b'\x12\x08\x02\x0e\x05\x7f*~\x00\x0e\x02\x02\x01\r\x01\r\x05\x04\x01\x00\x0f\x00+\x001\x00\x01\x00\x03\x01\x03\x01'),
                            bytearray(b'L|\xa0\xe0\xb8\xf8`\xe0\xe0\xe0xx\x90\x90\xe0\xe0\xfc\x00\xe0\x1c\xf88` \xe0`\xf88\xf0\x90\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=114),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x1c\x02\x0e\x02\x0e\x02\x0e&\x0eE\x0f@\x1f\x92\x0f\x00\x1c\x00\x0e\x00\x0f\x02\x0f\x02\x0e\x00\x0c\x00\x08\x00\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x90\xf0\x10p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00p\x00\xf0\x08'),
                            bytearray(b'\xb2\n\x82\x1e\xc5\x1f\xda\x1e\xf0>\x92r\x83\x7f\x11m\x05\x06\x01\x00\x0f\x00\x1b\x00\x11\x00\x11\x00\x03\x01\x03\x01'),
                            bytearray(b'``\xa0\xe0\x90\xf0`\xe0\xe0\xe0\xf8\xf8\x90\x90\xe0\xe0\xe0\x18\xe0\x10\xd0\x10` \xe0`\xf8\xb8\xf0\x90\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=114),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x1c\x02\x0e\x02\x0e\x02\x0e\x06\x0e\x05\x0f\x00\x1f\x10\x0f\x00\x1c\x00\x0e\x00\x0f\x02\x0f\x02\x0e\x00\x0c\x00\x08\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x90\xf0\x10p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\x00p\x00\xf0\x08'),
                            bytearray(b'\x12\x0e\x06\x1e\x05?\x1a>1\x7f\x12r3\x7f\x01\r\x01\x02\x01\x04\x0f\x00\x1b\x00\x10\x00\x01\x00\x03\x01\x03\x01'),
                            bytearray(b'``\xa0\xe0\xb0\xf0\xe0\xe0\xe0\xe0\xf8\xf8\x90\x90\xe0\xe0\xe0\x18\xe0\x10\xd0\x10` \xe0`\xf8\xb8\xf0\x90\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=114),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x03\x01\x03\x01\x07\x03\x07\x02\x07\x00\x0f\t\x07\x00\x01\x00\x03\x00\x03\x01\x07\x01\x07\x00\x06\x00\x04\x00\x01'),
                            bytearray(b'@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x00\x80\x00\xc0\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00@\x00'),
                            bytearray(b'\t\x04\x01\x07\x02\x07\r\x0f\x00\x0b\x02\x02\x01\r\x05\r\x02\x02\x00\x00\x07\x00\r\x00\x04\x00\x01\x00\x03\x01\x03\x01'),
                            bytearray(b'  Pp\xc8\xf8<|L|hh\x90\x90\xe0\xe0\xe0\x00\xf0\x00\xf8\x00\xbc\x18\xcc\x08\xd8\x08\xf0\x90\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\t\x04\x01\x07\x02\x07\r\x0f\x00\x0b\x02\x02\x01\r\x05\r\x02\x02\x00\x00\x07\x00\r\x00\x04\x00\x01\x00\x03\x01\x03\x01'),
                            bytearray(b'  Pp\xc8\xf8<|L|hh\x90\x90\xe0\xe0\xe0\x00\xf0\x00\xf8\x00\xbc\x18\xcc\x08\xd8\x08\xf0\x90\xe0\xe0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x03\x01\x03\x01\x07\x03\x07\x02\x07\x00\x0f\t\x07\x00\x01\x00\x03\x00\x03\x01\x07\x01\x07\x00\x06\x00\x04\x00\x01'),
                            bytearray(b'@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x00\x80\x00\xc0\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00@\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=114),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x01\x07\x82G\x00\xefj\x87\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x00\x00\x02'),
                            bytearray(b'\x100\x10\xf0@\xc0\x80\x80\x80\x80\x80\x80@\xc0\x00\x80\x000\x00\xf0\x00\xe0\x80\xc0\x80\x80\x00\x00\x00\x00@\x00'),
                            bytearray(b'\xea1\xe1\x07r\x0fb\x03\x1c\x01\x0b\x0c\x0f\x0f\x07\x07$\x04\x00\x00\x03\x00\x07\x00\x03\x00\x0c\x08\x0f\x0f\x07\x07'),
                            bytearray(b'\x00\x00@`\xe0\xe00\xf00\xf0\xf00\xe0\xe0\xc0\xc0\xc0\x00\xe0\x00\xe0\x00\xf0\x10\xf0\x1000\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=114),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x06\x02\x06\x02\xeeE\xaf \xff0k\x14"\x00\x01\x00\x07\x02\x07\x02\x0e\x00\x0c\x00\x00\x04\x04\t\x08'),
                            bytearray(b'\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00'),
                            bytearray(b'\x06\x1e\x05\x0f\x04\x07\x02\x03\x04\x05\x08\x0f\x0f\x0f\x07\x07\x01\x00\x07\x00\x03\x00\x07\x00\x03\x00\x0f\x08\x0f\x0f\x07\x07'),
                            bytearray(b'\x80\xc0\xc0\xc00\xf00\xf00\xf0\xb0\xf0\xe0\xe0\xc0\xc0\xc0\x00\xc0\x00\xf0\x00\xf0\x10\xf0\x10\xf00\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=114),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x00\x03\x01\x03\x01\x03\x01\x07\x04\x03\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x00\x03\x00\x03\x00\x00'),
                            bytearray(b'\x10\xf0`\xe0\x80\x80\x80\x80\x80\x80@\xc0 \xe0\x80\xc0\x00\xf0\x00\xe0\x00\xc0\x80\xc0\x80\x80\x00\x00\x00\x00 \x80'),
                            bytearray(b'\x04\x02\x00\x03\x02\x1f\x05\x17\x00\x07\x01\x01\x03\x03\x00\x07\x01\x01\x00\x00\x07\x00\r\x00\x00\x00\x02\x00\x05\x01\x00\x00'),
                            bytearray(b'\x90\x10\xa8\xb8\xc0\xf84|L~ll\xf0\xf0\xe0\xe0p\x00x\x00\xf8\x04\xbc\x12\xce\t\x9c\x07\xf0\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=113),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x0e\x01\x07\x01\x07\x01\x07\x03\x07\x02\x07\x02\x0f\x08\x07\x00\x0e\x00\x07\x00\x07\x01\x07\x01\x07\x00\x06\x00\x06\x00\x00'),
                            bytearray(b'\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80L\xc0\x92\x8c\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00@\x00'),
                            bytearray(b'\t\x07\x01\x07\x02\x0f\x057\x0e\x7f\x1d,\x0f\x01\x07\x07\x00\x01\x00\x01\x0f\x00=\x00~\x0e.\x0c\x00\x00\x07\x07'),
                            bytearray(b'\x02\x1cB|\xb4\xe8x\xd8h\x18\xe8(\xf0\xf0\xe0\xe0\xc0\x00\xe0\x00\x80\x00\x00\x00\x88\x08\x18\x00\xf0\xf0\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=111),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x0e\x01\x07\x01\x07\x01\x07\x03\x07\x02\x07\x02\x0f\x08\x07\x00\x0e\x00\x07\x00\x07\x01\x07\x01\x07\x00\x06\x00\x06\x00\x00'),
                            bytearray(b'\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80@\xc6\x00\x8e\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00@\x00'),
                            bytearray(b'\t\x07\x01\x07\x02\x0f\x05\x17\x0e\x7f\x0f?\x0f\x0f\x07\x07\x00\x01\x00\x01\x0f\x00\x1d\x00~\x0e?\x0f\x0e\x0e\x07\x07'),
                            bytearray(b'\x00\x1eD|\xb8\xf8h\xe8hxhh\xf0\xf0\xe0\xe0\xc0\x00\xe0\x00\x80\x008(\xe8(\xf8 \xf0\xf0\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x0e\x01\x07\x01\x07\x01\x07\x03\x07\x02\x07\x02\x0f\x08\x07\x00\x0e\x00\x07\x00\x07\x01\x07\x01\x07\x00\x06\x00\x06\x00\x00'),
                            bytearray(b'\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x80\x80L\xc0\x92\x8c\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00@\x00'),
                            bytearray(b'\t\x07\x01\x07\x02\x0f\x057\x0e\x7f\x1d,\x0f\x01\x07\x07\x00\x01\x00\x01\x0f\x00=\x00~\x0e.\x0c\x00\x00\x07\x07'),
                            bytearray(b'\x02\x1cB|\xb4\xe8x\xd8h\x18\xe8(\xf0\xf0\xe0\xe0\xc0\x00\xe0\x00\x80\x00\x00\x00\x88\x08\x18\x00\xf0\xf0\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=111),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x03\x0f\x04\x1c\x04\x1c\x0c\x1c\n\x1e\t?\x00\x00\x00\x07\x00\x0f\x00\x1e\x04\x1e\x04\x1c\x00\x18\x00\x18'),
                            bytearray(b'\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'$\x1e$\x10\x05\x1d\x0b\x7f\nn\x0e\x0e\x02\x1a\x0e\x0f\x01\x04\x0b\x08\x03\x00\x1f\x00\x1b\x00\x01\x00\x07\x02\x0e\x0e'),
                            bytearray(b'\x00\x00\x80\x80@\xc0\x10\xf0@\xfc\xf8\xf8\xf0\xf0@\xc0\x00\x00\x80@\xc00\x80\x08L\x02\xf8\x1e\xf0\xf0@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x07\x03\x0f\x04\x1c\x04\x1c\x0c\x1c\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x00\x1e\x04\x1e\x04\x1c'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\n\x1e\t?$\x1e$\x10%}\nj\x0e\x1e\x0e\x0f\x00\x18\x00\x18\x01\x04\x0b\x08\x03\x00\x05\x00\x07\x06\x0e\x0e'),
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\x10\xf0@\xfc\xf8\xf8\xf0\xf0@\xc0\x00\x00\x00@\xc00\x80\x08\xcc\x02\xf8\x1e\xf0\xf0@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00`\x009\x04\x1d\x04\x1d\x0e\x7f\n?\x01?$\x1e\x00`\x01<\x01\x1e\x05\x1eg\x1c!\x18\x00\x10\x01\x04'),
                            bytearray(b'\x00\x00\x00\xc0 \xe00\xf0\x10\xf0P\xd0\xe0\xe0\x80\x98\x00\x00\xc0\x00\xe0\x00\xf0\x00\xf0\x08\xd0 \xe0\x00\x80\xe0'),
                            bytearray(b'$\x10\x05\x1d\x0b?\x011\x00\x01\x00\x01\x00\x00\x00\x00\x0b\x08\x03\x00\x1f\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\xf8x\xf8\xd8\xd8\x98\x98\x80\x80\x00\x80\x00\x00\x00\x00\xe0`\xf8`\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=113),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00`\x009\x04\x1d\x04\x1d\x0e\x7f\n?\x01?$\x1e\x00`\x01<\x01\x1e\x05\x1eg\x1c!\x18\x00\x10\x01\x04'),
                            bytearray(b'\x00\x00\x00\xc0 \xe00\xf0\x10\xf0P\xd0\xe0\xe0\x80\x98\x00\x00\xc0\x00\xe0\x00\xf0\x00\xf0\x08\xd0 \xe0\x00\x80\xe0'),
                            bytearray(b'$\x10\x05\x1d\x0b?\x011\x00\x01\x00\x01\x00\x00\x00\x00\x0b\x08\x03\x00\x1f\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\xf8x\xf8\xd8\xd8\x98\x98\x80\x80\x00\x80\x00\x00\x00\x00\xe0`\xf8`\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=330),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xc0\x00p\x088\x088\x0e\x1f\n?\x01?$\x1e\x00\xc0\x00x\x00<\x08<\x07\x1c!\x18\x00\x10\x01\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x10\xf0\xe0\xe0\x80\x98\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xf0\x00\xe0\x1c\x80\xe6'),
                            bytearray(b'$\x10\x05\x1d\x0b?\x011\x00\x01\x00\x01\x00\x00\x00\x00\x0b\x08\x03\x00\x1f\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\xf8x\xf8\xd8\xd8\x98\x98\x80\x80\x00\x80\x00\x00\x00\x00\xe0f\xf8`\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=74),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x07\x04o\x05?\x04\x1d\x04\x1d\x06\x0f\x01\x1d\x03;\x00\x00\x00`\x008\x00\x1c\x04\x1c\x02\x0c\x03\n\x04\x04'),
                            bytearray(b'\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\xcc\xcc\xfe\xfe\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\xcc\x00\xfe\x00'),
                            bytearray(b'"\x1e\x06>\x0c\x1d\x0b\x1f\x04\x07\x19\x19\x08\x08\x00\x00\x01\x00\x01\x00\x03\x00\x1f\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe3\xe3\xd8\xd8\xf8\xf8x\xf8\xe0\xe0\xc0\xc0@\xc0\x00\x00c\x1c\x98\xbe\x98\x1c\x98\x18\xa0\xa0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=71),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x03\x01\x07\x02\x06\x03\'B\x0f@\x0f\x89\x07\x00\x00\x00\x03\x00\x07\x02\x07!\'\x08\x06\x00\x04\x00\x01"),
                            bytearray(b'\x00\xc0\x00\x80\x00\x00\x00\x01\x80\xf6\x84\xfcx\xf8$\xa4\x00\xc0\x00\xc0\x00\x80\x01\x00\xf6\x01|\x038\x06d<'),
                            bytearray(b'\x89\x04\xa1\x07\xa2\x07\xb0DP\x0cn\x011\x07\x0c\x03\x02\x02\x00\x00\x07\x00@@\x08\x08\x00\x00\x01\x00\x00\x00'),
                            bytearray(b'>>~~\xb6\xf6F\xc6\x00\xc0`\xe0`\xe0`\xe0\xfe\x1e\xde\x18\xb00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=80),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x03\x01\x03\x03\x07\x02\x0f\x00\x0f\t\x07\x00\x00\x00\x01\x00\x03\x01\x03\x01\x07\x08\x06\x00\x04\x00\x01'),
                            bytearray(b'\x00`\x00\xc0\x9c\xbc\x0e?\x88\xfe\x84\xfcx\xf8$\xa4\x00`\x00\xe0<\xc0?\x80\xfe\x01|\x038\x06d<'),
                            bytearray(b'\t\x04\x01\x07\x02\x07\x00\x04\x00\x02\x01\x03\x00\x03\x00\x01\x02\x02\x00\x00\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'>>~~\xb6\xf6@\xc0\x00\xc00\xf0\xb0\xf0 \xe0\xf8\x18\xd0\x10\xb00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=81),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x1e\x1e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00`\x009\x04\x1d\x04\x1d\x0e\x7f\n?\x01?$\x1e\x00`\x01<\x01\x1e\x05\x1eg\x1c!\x18\x00\x10\x01\x04'),
                            bytearray(b'\x00\x00\x00\xc0 \xe00\xf0\x10\xf0P\xd0\xe0\xe0\x80\x98\x00\x00\xc0\x00\xe0\x00\xf0\x00\xf0\x08\xd0 \xe0\x00\x80\xe0'),
                            bytearray(b'$\x10\x05\x1d\x0b?\x011\x00\x01\x00\x01\x00\x00\x00\x00\x0b\x08\x03\x00\x1f\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\xf8x\xf8\xd8\xd8\x98\x98\x80\x80\x00\x80\x00\x00\x00\x00\xe0`\xf8`\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=368),
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
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=6, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=14),
                        AnimationSequenceFrame(duration=14, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=10, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=6, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL581_JINX_CLONE,
    palette_offset=0,
    unknown_num=8
)
