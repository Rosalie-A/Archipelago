# SPR0271_RAT_FUNK

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL047_RAT_FUNK
sprite = CompleteSprite(
    animation=AnimationPack(16, length=539, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x1d\x03\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\xde?\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_\x82]'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0@\xc0'),
                            bytearray(b'\x0f\x13+\x16+57)sb&\x06\x7f\x08\x07$\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f;?'),
                            bytearray(b'\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf80\xf8 \x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xc8\xf8\xcc\xfc'),
                            bytearray(b'\xc0\x80\x00\x00\x80\x00\x01\x00\x03\x00\x07\x04\x0e\x088 @\xc0\x80\x80\x80\x80\x01\x00\x02\x01\x01\x03\x02\x064\x0c'),
                            bytearray(b"\'_#_iT\xffF\x03\x00\x01\x00\x03\x02\x00\x00tSrQ\x103\x071\x00\x03\x00\x03\x01\x01\x00\x00"),
                            bytearray(b'\xf7)\xcd<\xe7d\xc2>\x82\\\xe0\x0c\xfc<\x00\x00\xce\xff\xf3\xf7\x83\xf9\xfd\xbd\xdf\xfd\xfe\xde\xfc\xfc\x00\x00'),
                            bytearray(b'\xf8P\xf0\xc0\xcf\x0f\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00H\xb80\xf0\xcf\xcf\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x01\x02\x01\x06\x01\x06\x07\x00\x07\x00\x07\x02\x07\x07\x0e\x01\x01\x01\x01\x05\x05\x01\x03\x01\x01\x03\x03\x00\x00\x00\x00\x08'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00\x87\x07\xffg\xef\x9f\xef\x9f\x00\x00\x00\x00\x80\x80\x80\x80\x86\x81\xd87@/A.'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xe0\x80`\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0`\xe0 \xe0'),
                            bytearray(b'\x07\t\x15\x0b\x15\x1a\x1b\x1491\x13\x03?\xc4\t\xc9\x08\x08\x08\x18\x08\t\x01\x03\x04\x0bx?\xfb\xff\xe6\xdf'),
                            bytearray(b'\xfe\xbf\xbc\x7f\xb8\xdf\xf9\x90\xfc\x00<\x00\xff\x1c\xfd\t\x02}E\xfaA\xfeO\xbf<\xfc\xfc\xfc\xe3\xff\xf0\xfe'),
                            bytearray(b'a\xc0\x03\x80G\x04\x8e\x08\x18\x10p@\xf0\xa0\xe1\x01\xa1`\xc2A\xc1\xc3\x82\x86\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            bytearray(b'\tG\x08\x07\n\x05\x07\x01\x01\x01\x00\x00\x01\x01\x01\x01mT\x0c\x04\x04\x0c\x01\x04\x01\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xf9\xc7\xfe\xc6}\x02\xf8\x85\xff`\x7f\x1c\xe0`\x80\x80>\xfe\xb8\x7f>\xfa\xfd\x7f\x1e\xfc?\xff\xa0`\x00\x80'),
                            bytearray(b'fF\xbc\xbc\xf00\xc0@\x80\x00\x00\x00\x00\x00\x00\x00&\xe6\x1c|P0  @@\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x00\x00\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0'),
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            bytearray(b'\xde?\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf8 \x82]\x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xd8\xf8'),
                            bytearray(b'\xc0\x80\xc0\x80\x02\x00\x86\x00\x0e\x08\x1c\x10pP\xf0\xa0@\xc0@\xc0\x82\x80\x84\x82\x02\x06\x04\x0cx\x08\xd00'),
                            bytearray(b'\x03\x00\x13\x0e\x11\x0e\x07\t\x0e\x03/&_O\x00\x00\x0f\x0f\x1b\t\x19\t\t\x1a\x01\x1b\x02\x1f\x0f?\x00\x00'),
                            bytearray(b'\xf9Q\xdfQ\xef\x03\x9f`\x0f\xf1\x8ev\x18`0\x00\x89\xf8\x8c\xff,\x1fwo\xff\xf7\xfev\xf8\xe8pp'),
                            bytearray(b'\xe0@\xc6\x86\x9c\x1c\xf0\xf0\x80\x80\x00\x00\x00\x00\x00\x00 \xe0F\xc6\x9c\x9c\xf0\xf0\x80\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00s \x7f<oJ\x07,\x078\x07\x1c\x00\x00\x00\x004S~\x01f\x11{k;3;\x13'),
                            bytearray(b"\x03\x03/5\xbb\x89\xffB\xffA\xfe\x00\xf8\x10\xf8 \x00\x0f3\x10\'\x80&\xf18\xff\xfe\xfe\xe8\xf8\xc8\xf8"),
                            bytearray(b'\x00\x00\x80\x00\xc0\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x17\x0c\x17\x0c\x0f\x04\x07\x01\x0b\x00\x17\x0f\x0f\x1c\x1f!\x0b\x0b\x0f\x0b\x01\x07\x0f\x00\x04\x03\x0e\x18\x12\x14.$'),
                            bytearray(b'\xf80\xf0\x10\xf8\xe0\xfc@\x9c\x80\xf2\xb0\xf6\xe0|h\xe8\xd8\x88\xf8X\xb88\xfcz\xfen\x1en\x1e\xe4\x1c'),
                            None,
                            bytearray(b"\x0f\x7f\x02x\x038\x07$-\x00\x00\x00\x00\x00\x00\x00|r~{z?ro\'>\x00\x00\x00\x00\x00\x00"),
                            bytearray(b'\xb8\x00\xc8\x80d\x00\xf8\x0c\xce\x03\x03\x00\x00\x00\x00\x00\x88x\xa0x<\xe0\xfe\xf4O\xcd\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x80\xe0`0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xb0\xc000'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x009\x10?\x1e7%\x03\x16\x03\x1c\x00\x00\x00\x00\x00\x00\x1a)?\x003\x08=5\x1d\x19'),
                            bytearray(b'\x00\x00\x01\x01\x17\n\xddD\xff!\xff \xff\x00\xfc\x08\x00\x00\x00\x07\x19\x08\x13\xc0\x13\xf8\x1c\xff\xff\xff\xf4\xfc'),
                            bytearray(b'\x00\x00\x80\x80\xc0\x80\xe0\x80\xc0@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x80\xc0@\xa0`\x00\xc0\x00\x80\x00\x00\x00\x00'),
                            bytearray(b'\x03\x0e\x0b\x06\x0b\x06\x07\x02\x01\x00\r\n_}\x1d\xf8\x1d\t\x05\x05\x07\x05\x00\x03\x07\x00\x02\x03#$\xe5\xee'),
                            bytearray(b'\xfc\x10\xfc\x18\xf8\x08\xfcp\xff\xa0\xc7@\xfb\xd8\xf8p\xe4\xfc\xf4\xec\xc4\xfc\xac\xdc\x9f~?\xfe6\x0f7\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\xc0\xc0'),
                            bytearray(b'\x0e\xea\x1d`\x1e`Y\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe4\xff\xf6o\xf7\xefj[\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbc\xb4\xdc\x80dD\x92\x04|\x06\xff\x80p@\x00\x00s\x0fD<T\xb8>\xf4\x7f\x9a\x7f\x1f\x100\x00\x00'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x80\x00`\x00\xd8\x00<\x00\x80\x80\x00\x00\x00\x00\x00\x00\x80\x00\xa0\x00\xd0\xe4<<'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\xe7A\xffx\xdf\x94\x0fX\x0fp\x0f8\x00\x00\x00\x00h\xa7\xfc\x03\xcc#\xf7\xd7wgw\'"),
                            bytearray(b'\x06\x06?\nw\x12\xff\x85\xfe\x82\xfc\x00\xf0 \xf0@\x00\x1e\x07AN\x01L\xe3p\xfe\xfc\xfc\xd0\xf0\x90\xf0'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'/\x18/\x18\x1f\t\x0f\x02\x17\x01\x1f\x03\x1f\x00\x1b\x01\x17\x17\x1f\x17\x02\x0f\x1e\x01\x08\x07\x0c\x00\x15\x06\x17\x06'),
                            bytearray(b'\xf0`\xe0 \xf0\xc0\xf0\x80\x10\x00\xe0`\xe0\xc0\xf0\xd0\xd0\xb0\x10\xf0\xb0pp\xf0\xf0\xf0\xd00\xd00\xc00'),
                            None,
                            bytearray(b'\x0b\x01\x1d\x00\x01\x1d\x07\x1d\x03\x1d\x07\x08\x07\x00\x00\x00\x02\x17\x03\x17\x0c\x0f\x18\x1b\x1e\x1d\r\x0b\x07\x07\x00\x00'),
                            bytearray(b'p\x00\xd0\x00\x80\x00\xe0\x80p\x04\xc8\x02\x06\x00\x01\x00\x10\xf0\x80\xf0\xf0\xc0x\xe0\xfc\xf4\xcb\xce\x06\x07\x01\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x80\xc0\xc0'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x0e\x00\x0f\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x0e\x00\x0f\x00\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x07\x00\xf9\x06\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04&\xc6\x07\x18\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00x\x00\xfc\xf0X\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x1fx\x06\x0c\x00\x10\x08\x80`\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e\xea\x1d`\x1e`Y\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe4\xff\xf6o\xf7\xefj[\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xbc\xb4\xdc\x80dD\x92\x04|\x06\xff\x80p@\x00\x00s\x0fD<T\xb8>\xf4\x7f\x9a\x7f\x1f\x100\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=127),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x80\xc0\x80\xe0\x80\xc0@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x80\xc0@\xa0`\x00\xc0\x00\x80\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\x80@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xc0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x009\x10?\x1e7%\x03\x16\x03\x1c\x00\x00\x00\x00\x00\x00\x1a)?\x003\x08=5\x1d\x19'),
                            bytearray(b'\x00\x00\x01\x01\x17\n\xddD\xff!\xff \xff\x00\xfc\x08\x00\x00\x00\x07\x19\x08\x13\xc0\x13\xf8\x1c\xff\xff\xff\xf4\xfc'),
                            bytearray(b'\x03\x0e\x0b\x06\x0b\x06\x07\x02\x01\x00\r\n_}\x1d\xf8\x1d\t\x05\x05\x07\x05\x00\x03\x07\x00\x02\x03#$\xe5\xee'),
                            bytearray(b'\xfc\x10\xfc\x18\xf8\x08\xfcp\xff\xa0\xc7@\xfb\xd8\xf8p\xe4\xfc\xf4\xec\xc4\xfc\xac\xdc\x9f~?\xfe6\x0f7\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=111),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\x00@\x00\x00\x00\x00\x00@\x00@\x00@\x00@\x80\x000\x00`\x00@\x00@@\x80@\x80@\x80@\x00'),
                            None,
                            bytearray(b'@\x80@\x80\x00\xc0\x00\xc0 \xc0\x10`\x08p \x00\xc0\x80\xc0\x80\x80\x80@@`@0\xac($ \x18'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x9e\x16\x1d\x00\x13\x11\x04\x00\x07\x00\x04\x03\x00\x00\x00\x00\xe7\xf8\x11\x1e\x15\x0e\x06\x07\x07\x04\x07\x07\x00\x00\x00\x00'),
                            bytearray(b'\xac\x87\xf0\xc78\x07\xbc\x07\x17\x04\x80\x80\x00\x00\x00\x00#s7\x7fo\xf7k\xf32\xf9\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xce\x04\xfe<\xf6R\xe04\xe0\x1c\x00\x00\x00\x00\x00\x00,\xca~\x80f\x88\xde\xd6\xdc\xcc'),
                            None,
                            bytearray(b'\xe08\xe80\xe80\xf0 \xc0\x80\xd0 \xf8\xe0\xdc\x00\xdc\xc8\xd0\xd0\xf0\xd0\x80\xe0\xf0\x00 \xe0H\x00D '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x03\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\xc0\xc0\xf4\xa8\xdd\x91\xffB\xff\x82\x7f\x00\x1f\x08\x00\x00\x00\xf0\xcc\x08\xe4\x01d\x8f\x1c\xff\x7f\x7f\x17\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01'),
                            bytearray(b'\x1f\x04\x1f\x0c\x0f\x08\x1f\x07\xff\x02\xf1\xc1\xef\x8d\x0f\x07\x13\x1f\x17\x1b\x11\x1f\x1a\x1d\xfc\xff>\xff6\xf8\xf6\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x00%\x00\x1a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00`\x05:\x00\x1f'),
                            bytearray(b'\x04\x00\x0c\x00\x10\x08(\x10P  @\x80\x00\x00\x00\x04\x02\x0c\x02\x18\x0c8\x10p(`\xd0\x80`\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x9e\x16\x1d\x00\x13\x11\x04\x00\x07\x00\x04\x03\x00\x00\x00\x00\xe7\xf8\x11\x1e\x15\x0e\x06\x07\x07\x04\x07\x07\x00\x00\x00\x00'),
                            bytearray(b'\xac\x87\xf0\xc78\x07\xbc\x07\x17\x04\x80\x80\x00\x00\x00\x00#s7\x7fo\xf7k\xf32\xf9\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xce\x04\xfe<\xf6R\xe04\xe0\x1c\x00\x00\x00\x00\x00\x00,\xca~\x80f\x88\xde\xd6\xdc\xcc'),
                            None,
                            bytearray(b'\xe08\xe80\xe80\xf0 \xc0\x80\xd0 \xf8\xe0\xdc\x00\xdc\xc8\xd0\xd0\xf0\xd0\x80\xe0\xf0\x00 \xe0H\x00D '),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x03\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\xc0\xc0\xf4\xa8\xdd\x91\xffB\xff\x82\x7f\x00\x1f\x08\x00\x00\x00\xf0\xcc\x08\xe4\x01d\x8f\x1c\xff\x7f\x7f\x17\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01'),
                            bytearray(b'\x1f\x04\x1f\x0c\x0f\x08\x1f\x07\xff\x02\xf1\xc1\xef\x8d\x0f\x07\x13\x1f\x17\x1b\x11\x1f\x1a\x1d\xfc\xff>\xff6\xf8\xf6\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\xe0\xeeH\xcb:\xf54\xef\x11\xc7+\xfc\x00\xf8\xe0\x18\xf8\x86\xf6\xf1\xf7\xc1\xfb\xf2\xd1\xe8\xf9\xf2\xe2\xfc\xfc'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=114),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfc\xc0\xfc\xb0<\x0c\xf0\xb0\xc0\xc0\x00\x00\x00\x00\x00\x00\xfc<\x8c|\x1c\xfcP0\x00@\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=106),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x00\x00\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_'),
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            bytearray(b'\xde?\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf8 \x82]\x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xd8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            bytearray(b'\xe6\xc6\xfc\xdc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe6\xe6\xfc\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x0f\x04\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0f\x0b\x0f\x0e\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xff\x1c\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xff\xff\xff\xff'),
                            bytearray(b'\t\x07\x08\x07\n\x05\x0f\x01\x01\x01\x00\x00\x00\x00\x00\x00\r\x04\x0c\x04\x04\x0c\x01\x0c\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=118),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\xe0\xeeH\xcb:\xf54\xef\x11\xc7+\xfc\x00\xf8\xe0\x18\xf8\x86\xf6\xf1\xf7\xc1\xfb\xf2\xd1\xe8\xf9\xf2\xe2\xfc\xfc'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=374),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=368),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfc\xc0\xfc\xb0<\x0c\xf0\xb0\xc0\xc0\x00\x00\x00\x00\x00\x00\xfc<\x8c|\x1c\xfcP0\x00@\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=381),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=360),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x00\x00\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_'),
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            bytearray(b'\xde?\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf8 \x82]\x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xd8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=360),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            bytearray(b'\xe6\xc6\xfc\xdc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe6\xe6\xfc\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=370),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x0f\x04\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0f\x0b\x0f\x0e\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xff\x1c\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xff\xff\xff\xff'),
                            bytearray(b'\t\x07\x08\x07\n\x05\x0f\x01\x01\x01\x00\x00\x00\x00\x00\x00\r\x04\x0c\x04\x04\x0c\x01\x0c\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=370),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=369),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\xe0\xeeH\xcb:\xf54\xef\x11\xc7+\xfc\x00\xf8\xe0\x18\xf8\x86\xf6\xf1\xf7\xc1\xfb\xf2\xd1\xe8\xf9\xf2\xe2\xfc\xfc'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=371),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=365),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfc\xc0\xfc\xb0<\x0c\xf0\xb0\xc0\xc0\x00\x00\x00\x00\x00\x00\xfc<\x8c|\x1c\xfcP0\x00@\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=379),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=357),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x00\x00\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_'),
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            bytearray(b'\xde?\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf8 \x82]\x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xd8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=357),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            bytearray(b'\xe6\xc6\xfc\xdc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe6\xe6\xfc\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=367),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x0f\x04\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0f\x0b\x0f\x0e\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xff\x1c\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xff\xff\xff\xff'),
                            bytearray(b'\t\x07\x08\x07\n\x05\x0f\x01\x01\x01\x00\x00\x00\x00\x00\x00\r\x04\x0c\x04\x04\x0c\x01\x0c\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=367),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=368),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\xe0\xeeH\xcb:\xf54\xef\x11\xc7+\xfc\x00\xf8\xe0\x18\xf8\x86\xf6\xf1\xf7\xc1\xfb\xf2\xd1\xe8\xf9\xf2\xe2\xfc\xfc'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=370),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=366),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfc\xc0\xfc\xb0<\x0c\xf0\xb0\xc0\xc0\x00\x00\x00\x00\x00\x00\xfc<\x8c|\x1c\xfcP0\x00@\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=380),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=358),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x00\x00\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_'),
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            bytearray(b'\xde?\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf8 \x82]\x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xd8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=358),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            bytearray(b'\xe6\xc6\xfc\xdc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe6\xe6\xfc\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=141, y=368),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x0f\x04\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0f\x0b\x0f\x0e\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xff\x1c\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xff\xff\xff\xff'),
                            bytearray(b'\t\x07\x08\x07\n\x05\x0f\x01\x01\x01\x00\x00\x00\x00\x00\x00\r\x04\x0c\x04\x04\x0c\x01\x0c\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=368),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=365),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\xe0\xeeH\xcb:\xf54\xef\x11\xc7+\xfc\x00\xf8\xe0\x18\xf8\x86\xf6\xf1\xf7\xc1\xfb\xf2\xd1\xe8\xf9\xf2\xe2\xfc\xfc'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=374),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=367),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfc\xc0\xfc\xb0<\x0c\xf0\xb0\xc0\xc0\x00\x00\x00\x00\x00\x00\xfc<\x8c|\x1c\xfcP0\x00@\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=381),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=145, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x00\x00\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_'),
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            bytearray(b'\xde?\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf8 \x82]\x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xd8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=359),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            bytearray(b'\xe6\xc6\xfc\xdc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xe6\xe6\xfc\xfc\xf0\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=369),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x0f\x04\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x0f\x0b\x0f\x0e\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xff\x1c\xff\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfc\xfc\xff\xff\xff\xff'),
                            bytearray(b'\t\x07\x08\x07\n\x05\x0f\x01\x01\x01\x00\x00\x00\x00\x00\x00\r\x04\x0c\x04\x04\x0c\x01\x0c\x01\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=369),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=367),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0@\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x1d\x03\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\xde?\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_\x82]'),
                            bytearray(b'\x0f\x13+\x16+57)sb&\x06\x7f\x08\x07$\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f;?'),
                            bytearray(b'\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf80\xf8 \x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xc8\xf8\xcc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8P\xf0\xc0\xcf\x0f\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00H\xb80\xf0\xcf\xcf\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\'_#_iT\xffF\x03\x00\x01\x00\x03\x02\x00\x00tSrQ\x103\x071\x00\x03\x00\x03\x01\x01\x00\x00"),
                            bytearray(b'\xf7)\xcd<\xe7d\xc2>\x82\\\xe0\x0c\xfc<\x00\x00\xce\xff\xf3\xf7\x83\xf9\xfd\xbd\xdf\xfd\xfe\xde\xfc\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0@\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=392, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x1d\x03\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\xde?\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_\x82]'),
                            bytearray(b'\x0f\x13+\x16+57)sb&\x06\x7f\x08\x07$\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f;?'),
                            bytearray(b'\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf80\xf8 \x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xc8\xf8\xcc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8P\xf0\xc0\xcf\x0f\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00H\xb80\xf0\xcf\xcf\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\'_#_iT\xffF\x03\x00\x01\x00\x03\x02\x00\x00tSrQ\x103\x071\x00\x03\x00\x03\x01\x01\x00\x00"),
                            bytearray(b'\xf9Q\xdfQ\xef\x03\x9f`\x0f\xf1\x8ev\x18`0\x00\x89\xf8\x8c\xff,\x1fwo\xff\xf7\xfev\xf8\xe8pp'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0@\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=364),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x1d\x03\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\xde?\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_\x82]'),
                            bytearray(b'\x0f\x13+\x16+57)sb&\x06\x7f\x08\x07$\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f;?'),
                            bytearray(b'\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf80\xf8 \x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xc8\xf8\xcc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=364),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=391, y=370),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8P\xf0\xc0\xcf\x0f\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00H\xb80\xf0\xcf\xcf\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=391, y=376),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\'_#_iT\xffF\x03\x00\x01\x00\x03\x02\x00\x00tSrQ\x103\x071\x00\x03\x00\x03\x01\x01\x00\x00"),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=120),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0@\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=385, y=117),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x1d\x03\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\xde?\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_\x82]'),
                            None,
                            bytearray(b'\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf80\xf8 \x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xc8\xf8\xcc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=117),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=387, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8P\xf0\xc0\xcf\x0f\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00H\xb80\xf0\xcf\xcf\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=387, y=126),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\'_#_iT\xffF\x03\x00\x01\x00\x03\x02\x00\x00tSrQ\x103\x071\x00\x03\x00\x03\x01\x01\x00\x00"),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=127),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00p\x00\xcc0\x04\xf8\xc48\x0c0\x18\x00\x00\x00\x00\x00P\x08\xb84\xfc\xf8|\xb8|t88'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xee\x19\x7f\x9b_\xbb_\xb5\xbfI\x9f\x1030\xffA\x04\x82\x84\x83\x80\x87\x80\x8f\x14;C\xbf\x8f\xff\xbe\xff'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1d\x03\x0f\x13+\x16+57)sb&\x06\x7f\x08\x00\x10\x10\x10\x101\x10\x13\x02\x07\x08\x17q\x7fw\x7f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=126),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0\x00\xc0\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xc0\xc0@\xc0'),
                            None,
                            bytearray(b'\xc0\x80\xc0\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00@\xc0@\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=119),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x02\x04\x02\x0c\x03\x0c\x0f\x00\x0f\x00\x0f\x04\x0f\x0f\x1d\x03\x02\x02\x02\n\x0b\x03\x07\x03\x03\x07\x07\x00\x00\x00\x00\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\xff\xcf\xdf?\xde?\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x03\xb0o\x80_\x82]'),
                            None,
                            bytearray(b'\xfc\x7fx\xffp\xbe\xf3 \xf8\x00p\x00\xf80\xf8 \x05\xfa\x8b\xf4\x83\xfd\x9f\x7fx\xf8\xf0\xf0\xc8\xf8\xcc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x00\x03\x00\x07\x04\x0e\x08\x18\x10p@\xf0 \xe1\x01\x01\x00\x02\x01\x01\x03\x02\x06\x04\x0ch\x18\x10\xf0\xe1\xe1'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8P\xf0\xc0\xcf\x0f\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00H\xb80\xf0\xcf\xcf\xfc\xfc\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=127),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\'_#_iT\xffF\x03\x00\x01\x00\x03\x02\x00\x00tSrQ\x103\x071\x00\x03\x00\x03\x01\x01\x00\x00"),
                            bytearray(b'\xff\xc7\xff\xc7\x7f\x07\xff\x85\xfe*\x00\x00\x00\x00\x00\x00?\xff\xbf\x7f?\xff\xff\x7f~\xfe\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=127),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=14, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=14, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=14, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=14, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL047_RAT_FUNK,
    palette_offset=0,
    unknown_num=0
)
