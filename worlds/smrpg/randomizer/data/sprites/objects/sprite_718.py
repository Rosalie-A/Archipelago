# SPR0718_SCARECROW

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL677_SCARECROW
sprite = CompleteSprite(
    animation=AnimationPack(60, length=267, unknown=0x0000,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x02\x02\x03\x03\x01\x01\x07\x07\x0f\x0f\x0f\x0f\x07\x07\x01\x01\x02\x01\x03\x01\x01\x01\x07\x07\x0f\x0f\x0f\x0f\x07\x07\x01\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\xf8X\xf7\xd0\xff\x8c\xba\x05\xd1\xc6C\xc0\xe1``\x00\xf8X\xae\x801A\x07\xffF6\x039\xa1\x18\x00\xf0'),
                            bytearray(b'\x00\x00\x00\x80\xe0\x00\xf8\x00x\x84\xec\x10\xb0H\x00 \x00\x00\x80\x80\x80\x80\x18\x18\xac\xac\xb44\xf8x  '),
                            bytearray(b'\x80\x80\x80\x00\x00\x00@@\xf0p\xf0\xf0\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xc0@\xf0p\xf0\xf0\xf0\xf0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x0f\x00\x19\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\t\t\x17\x17'),
                            None,
                            bytearray(b'\x06\x19\x03\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1b\x07\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x7f\x87\xef\x04\x0f\x06\x05\x02\x0f\t\x0f\x0e\x0f\x0f\x07\x07\xcc\xb4\xe7\x0c\x03\n\x01\x0c\x04\x02\x07\x14\x0f\x18\x07\x04'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x00\x01\x02\x01\x00\x00\x00\x00\x00\x01\x00\x01\x01\x00\x01\x02\x01\x02\x01\x0e'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0@\xc0\x00\x80\x00\xc0\x80@\x80`\xc0 \xc0 \xc00\xc00'),
                            bytearray(b'\x0c\x0f\xfc\x7f??\x7f\x7f/\xffl\x97\xffo\xdf\x17\x0f0\x7f\x80?\xc0\x7f\x00\xff\xc0\xd7\xa8\x9d\r\xe9\x01'),
                            bytearray(b'h\xe8\xfe\xfe\xfe\xfe\xfd\xfc~\xfe8\xfc\xf0p\xe0\xe0\xe8\x14\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfc\x00\xf0@``'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x07\x07\x0f\x0f\x0f\x0f\x07\x07\x01\x01\x01\x00\x01\x01\x01\x01\x07\x07\x0f\x0f\x0f\x0f\x07\x07\x01\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xe0\xc0x\xd8\xf7\xb0\xbf\x0c^A\xd5\xc0\xd2\xc1A@\xe0\xc08\x18\x0e@\x11\xe1G\xbf\xc64\xc31A\xe0'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xe0\x00\xf8\x00\xf4\x08X\xa4\xe8\x10\x00\x00\x00\x00@\x00\x80\x80\x18\x18\xac\xac\xa4\xa4\xb88'),
                            bytearray(b'\x80\x80\x00\x00\x00\x00\xc0@\xf0p\xf0\xf0\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xc0@\xf0p\xf0\xf0\xf0\xf0\xc0\xc0'),
                            bytearray(b'@ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00``\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=True, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x04\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x06\x06\t\t'),
                            None,
                            bytearray(b'\x1f\x00\x12\r\x19\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x11\x11\x1f\x1f\x1f\x16\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xdb\x14|\x87\xec\x07\x07\x03\x0f\x0c\x0f\x0f\x1f\x1f\x13\x13\xeb\x00\xc8\xb0\xe0\x08\x00\x0c\x0c\x13\x0f\x10\x1f\x04\x13\x02'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=108),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x00\x03\x00\x02\x00\x00\x00\x00\x01\x00\x01\x01\x00\x00\x03\x00\x03\x00\x03\x00\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\x00\x80\x00\x80\x80@\x80@\xc0\x00\xc0 \xc0 \xc00'),
                            bytearray(b'\x02\x00|<\xff?\x7f\x7fq\x7f<\xdb\xe4\x03\xffg\x00?<\xc3?\xc0\x7f\x80\x7f\x00\xdb\xe4\xe3\x84\x9f\x07'),
                            bytearray(b'\xcc\xcc\xfe\xfe\xff\xfc\xff\xff\xbe\xfe0\xfc\x00\xf0\xe0\xe0\xcc0\xfe\x01\xfc\x03\xff\x00\xfe\x01\xfc\x00\xf0\x00\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'@\x00\xfe\x01\xffN\xe1\x80\xd1\x00\xe8H\xe8\xe8\xd8\xd8\xc0\x00\xbfA1\x81\x01a\xc11(\x98\x88\x18\xd88'),
                            bytearray(b'`\x80\xf8\x00\xdc \xda$\x9e`.Pf\x00`\x00\xa0\xa0(($$ll\xfe\xfezxF@`\x00'),
                            bytearray(b'\x80\x80\x80\x00\x00\x00pp\xf8x\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xf0p\xf8x\xf8\xf8\xf0\xf0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x06\x01\x1f\x00?\x00?@?\x00T*f\x00\x06\x00\x05\x05\x05\x05\x04\x04@@K\x0b~>d\x04\x06\x00'),
                            bytearray(b'\x07\x03\x02\x84}\xf6\x07\x87\x0f\x8d\x1f\x1e\x1d\x1e\n\x08\x00\x04\xf9\x82\x88\x81\x86\x80\x8e\x80\x19\x00\x18\x01\x08\x07'),
                            None,
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03\x01\x03\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x03\x02\x03\x00\x03\x00\x01\x00\x03\x01\x02\x01\x02\x03\x04\x03\x04\x03\x04\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x80@\x80@\x80`\x80p'),
                            bytearray(b'\x04\x07|\x7f\xbe?\xff\xff8/\x00\x0f\x06\x06\x06\x06\x07x\x7f\x80?\xc0\xff\x00/P\x0f\x10\x03\x02\x03\x02'),
                            bytearray(b'x\xf8~\xfe\xfe\xfe\xfd\xfc\xe4\xfc0\xf0`@@@\xf8\x06\xfe\x01\xfe\x01\xfc\x03\xfc\x02\xf0\x08\xe0@\xc0@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03\x01\x03\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03'),
                            bytearray(b'\x80\x80\x80\x00\x00\x00pp\xf8x\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xf0p\xf8x\xf8\xf8\xf0\xf0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\x80\xf8\x00\xdc \xda$\x9e`.Pf\x00`\x00\xa0\xa0(($$ll\xfe\xfezxF@`\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x07\x03\x02\x84}\xf6\x07\x87\x0f\x8d\x1f\x1e\x1d\x1e\n\x08\x00\x04\xf9\x82\x88\x81\x86\x80\x8e\x80\x19\x00\x18\x01\x08\x07'),
                            bytearray(b'@\x00\xfe\x01\xffN\xe1\x80\xd1\x00\xe8H\xe8\xe8\xd8\xd8\xc0\x00\xbfA1\x81\x01a\xc11(\x98\x88\x18\xd88'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x06\x01\x1f\x00?\x00?@?\x00T*f\x00\x06\x00\x05\x05\x05\x05\x04\x04@@K\x0b~>d\x04\x06\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x03\x02\x03\x00\x03\x00\x01\x00\x03\x01\x02\x01\x02\x03\x04\x03\x04\x03\x04\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x80@\x80@\x80`\x80p'),
                            bytearray(b'\x04\x07|\x7f\xbe?\xff\xff8/\x00\x0f\x06\x06\x06\x06\x07x\x7f\x80?\xc0\xff\x00/P\x0f\x10\x03\x02\x03\x02'),
                            bytearray(b'x\xf8~\xfe\xfe\xfe\xfd\xfc\xe4\xfc0\xf0`@@@\xf8\x06\xfe\x01\xfe\x01\xfc\x03\xfc\x02\xf0\x08\xe0@\xc0@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=100),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03\x01\x03\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03'),
                            bytearray(b'\x80\x80\x80\x00\x00\x00pp\xf8x\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xf0p\xf8x\xf8\xf8\xf0\xf0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\x80\xf8\x00\xdc \xda$\x9e`.Pf\x00`\x00\xa0\xa0(($$ll\xfe\xfezxF@`\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x07\x03\x02\x84}\xf6\x07\x87\x0f\x8d\x1f\x1e\x1d\x1e\n\x08\x00\x04\xf9\x82\x88\x81\x86\x80\x8e\x80\x19\x00\x18\x01\x08\x07'),
                            bytearray(b'@\x00\xfe\x01\xffN\xe1\x80\xd1\x00\xe8H\xe8\xe8\xd8\xd8\xc0\x00\xbfA1\x81\x01a\xc11(\x98\x88\x18\xd88'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x06\x01\x1f\x00?\x00?@?\x00T*f\x00\x06\x00\x05\x05\x05\x05\x04\x04@@K\x0b~>d\x04\x06\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x03\x02\x03\x00\x03\x00\x01\x00\x03\x01\x02\x01\x02\x03\x04\x03\x04\x03\x04\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x80@\x80@\x80`\x80p'),
                            bytearray(b'\x04\x07|\x7f\xbe?\xff\xff8/\x00\x0f\x06\x06\x06\x06\x07x\x7f\x80?\xc0\xff\x00/P\x0f\x10\x03\x02\x03\x02'),
                            bytearray(b'x\xf8~\xfe\xfe\xfe\xfd\xfc\xe4\xfc0\xf0`@@@\xf8\x06\xfe\x01\xfe\x01\xfc\x03\xfc\x02\xf0\x08\xe0@\xc0@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=100),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03\x01\x03\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03'),
                            bytearray(b'\x80\x80\x80\x00\x00\x00pp\xf8x\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xf0p\xf8x\xf8\xf8\xf0\xf0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\x80\xf8\x00\xdc \xda$\x9e`.Pf\x00`\x00\xa0\xa0(($$ll\xfe\xfezxF@`\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x07\x03\x02\x84}\xf6\x07\x87\x0f\x8d\x1f\x1e\x1d\x1e\n\x08\x00\x04\xf9\x82\x88\x81\x86\x80\x8e\x80\x19\x00\x18\x01\x08\x07'),
                            bytearray(b'@\x00\xfe\x01\xffN\xe1\x80\xd1\x00\xe8H\xe8\xe8\xd8\xd8\xc0\x00\xbfA1\x81\x01a\xc11(\x98\x88\x18\xd88'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x06\x01\x1f\x00?\x00?@?\x00T*f\x00\x06\x00\x05\x05\x05\x05\x04\x04@@K\x0b~>d\x04\x06\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x03\x02\x03\x00\x03\x00\x01\x00\x03\x01\x02\x01\x02\x03\x04\x03\x04\x03\x04\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x80@\x80@\x80`\x80p'),
                            bytearray(b'\x04\x07|\x7f\xbe?\xff\xff8/\x00\x0f\x06\x06\x06\x06\x07x\x7f\x80?\xc0\xff\x00/P\x0f\x10\x03\x02\x03\x02'),
                            bytearray(b'x\xf8~\xfe\xfe\xfe\xfd\xfc\xe4\xfc0\xf0`@@@\xf8\x06\xfe\x01\xfe\x01\xfc\x03\xfc\x02\xf0\x08\xe0@\xc0@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03\x01\x03\x01\x01\x01\x01\x0f\x0f\x1f\x1f\x1f\x1f\x0f\x0f\x03\x03'),
                            bytearray(b'\x80\x80\x80\x00\x00\x00pp\xf8x\xf8\xf8\xf0\xf0\xc0\xc0\x80\x80\x80\x00\x80\x00\xf0p\xf8x\xf8\xf8\xf0\xf0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'`\x80\xf8\x00\xdc \xda$\x9e`.Pf\x00`\x00\xa0\xa0(($$ll\xfe\xfezxF@`\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x07\x03\x02\x84}\xf6\x07\x87\x0f\x8d\x1f\x1e\x1d\x1e\n\x08\x00\x04\xf9\x82\x88\x81\x86\x80\x8e\x80\x19\x00\x18\x01\x08\x07'),
                            bytearray(b'@\x00\xfe\x01\xffN\xe1\x80\xd1\x00\xe8H\xe8\xe8\xd8\xd8\xc0\x00\xbfA1\x81\x01a\xc11(\x98\x88\x18\xd88'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x06\x01\x1f\x00?\x00?@?\x00T*f\x00\x06\x00\x05\x05\x05\x05\x04\x04@@K\x0b~>d\x04\x06\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x03\x02\x03\x00\x03\x00\x01\x00\x03\x01\x02\x01\x02\x03\x04\x03\x04\x03\x04\x03\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x80@\x80@\x80`\x80p'),
                            bytearray(b'\x04\x07|\x7f\xbe?\xff\xff8/\x00\x0f\x06\x06\x06\x06\x07x\x7f\x80?\xc0\xff\x00/P\x0f\x10\x03\x02\x03\x02'),
                            bytearray(b'x\xf8~\xfe\xfe\xfe\xfd\xfc\xe4\xfc0\xf0`@@@\xf8\x06\xfe\x01\xfe\x01\xfc\x03\xfc\x02\xf0\x08\xe0@\xc0@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=2),
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
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL677_SCARECROW,
    palette_offset=0,
    unknown_num=0
)
