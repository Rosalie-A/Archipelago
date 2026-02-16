# SPR0277_SPARKY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL063_FIREBALL_SURFACE_FROM_LAVA
sprite = CompleteSprite(
    animation=AnimationPack(21, length=469, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x10\x10\x00\x00\x04\x04\x0e\x0e\x1f\x1f\x1f\x1f\x00\x00\x00\x00\x00\x10\x00\x00\x00\x04\x00\x0e\x00\x1f\x00\x1f'),
                            bytearray(b'\x00\x00<8~|~~\xff\xfe\xff\xff\xff\xff\xff\xff\x00\x00\x048\x02|\x00~\x01\xfe\x00\xff\x00\xff\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00p`\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10`\x00\xf8'),
                            bytearray(b'????????\x7f\x7f_O}M|L\x00?\x00?\x00?\x00?\x00\x7f\x00o\x02O\x02O'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfb\xfb\xfb{\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x04\xff\x04\x7f'),
                            bytearray(b'\xf8\xf8\xfc\xf8\xfc\xf8~~6622&&\x04\x04\x00\xf8\x04\xf8\x04\xf8\x80\xfe\xc8\xfe\xcc\xfe\xd8\xfe\xf8\xfc'),
                            bytearray(b'1\x0010\x1b\x18\x1b\x18\r\x0c\x01\x00\x00\x00\x00\x00\x0e\x0e\x0e>\x06\x1e\x07\x1f\x03\x0f\x07\x07\x01\x01\x00\x00'),
                            bytearray(b'\xa2"\x80\x00\x87\x00\xbb\x04\xf1\x0e\x80\x7f\x80\x7f\x00<]\x7f\x7f\x7f\x7f\x7f\xff\xff\xff\xff\xff\xff\xc3\xffg\x7f'),
                            bytearray(b'\x0c\x0c\x08\x08(\x08\xf0\x10\xd0\x10\x80\x00\x00\x00\x00\x00\xf0\xfc\xf0\xf8\xf0\xf8\xe0\xf0\xe0\xf0\xc0\xc0\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x01\x01\t\x08\x0f\x0e\x0f\x0f\x1d\x1d\x1d\x19\x1e\x1b\x00\x00\x00\x01\x01\x08\x01\x0e\x00\x0f\x02\x1f\x06\x1f\x05\x1e'),
                            bytearray(b'\xc0\xc0\xee\xee\xef\xef\xf9\xf9\xf9\xf9yy\x00x~\x82\x00\xc0\x00\xee\x00\xef\x06\xff\x06\xff\x86\xff\xff\x87\xfd\x03'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\xc0\x80\xc0\x80``\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80@\x80@\x80\x80\xe0'),
                            bytearray(b'<7=+:/ytzgUC\xf8\xcb\xb0\x88\x0b<\x178\x179\x0cs\x1fa\x0f`\x07\xc0F\xc1'),
                            bytearray(b'\n\xf3ey\xb5yU\x99\xa4yjs5\xc6\xeb\x0c\xfd\x00~\x80~\xc0\x1e\xe0~\xc0|\x80\xf8\x00p\x00'),
                            bytearray(b'`\xe00\xb0p\xf0X\x98x\xb8\xe8\x08\xe8\x00\xf8\x10\x80`@p\x000 8\x00\x18\x10\x18\x18\x10\x08\x10'),
                            bytearray(b"\xb5\x8c\xfb\xc6}B\x7f`\' \x0f\x00\x01\x00\x00\x00B\xc00\xe00`\x18p\x188\x0e\x0c\x07\x06\x00\x00"),
                            bytearray(b'\xb78\xefp\x9f`\xff\x00\xff\x00\xff\x00\xfd\x01\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x86\x03\xf8\xf8'),
                            bytearray(b'\xf0\x10\xf0\x10\xe0 \xe0 \xc0@\x80\x80\x00\x00\x00\x00\x00\x10 \x10\x00 @ \x00@\x00\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x10\x10\x10\x10\x00\x00\x00\x00\x00\x00\x03\x01\x1b\x11;;\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x02\x01\n\x11\x00;'),
                            bytearray(b'\x00\x00PPxx\xfc\xfc\xfc\xfc\xff\xfe\xff\xff\xff\xff\x00\x00\x00P\x00x\x00\xfc\x00\xfc\x01\xfe\x00\xff\x00\xff'),
                            bytearray(b'\x00\x000 0 \x00\x00\x00\x000 \xf00\xf0p\x00\x00\x10 \x10 \x00\x00\x00\x00\x10 \xc00\x80p'),
                            bytearray(b'??\x7f\x7f\x7f\x7fooNN]MyIvB\x00?\x00\x7f\x00\x7f\x10\x7f1\x7f\x02o\x06O\x0cO'),
                            bytearray(b'\xff\xff\xff\xff\xff\xffyy\xfe\xfe\xff\xff\xff\xff\xfb{\x00\xff\x00\xff\x00\xff\x86\xff\x01\xff\x00\xff\x00\xff\x04\x7f'),
                            bytearray(b'\xf8\xf0\xf8\xf8\xf8\xf0\xf8\xf0\xf8\xf0xpxx88\x08\xf0\x00\xf8\x08\xf0\x08\xf0\x08\xf0\x88\xf0\x80\xf8\xc0\xf8'),
                            bytearray(b'w\x0250\x19\x18\x16\x14\t\x08\t\x08\x04\x07\x00\x00L\x0e\x0e>\x06\x1e\x0b\x1f\x07\x0f\x07\x0f\x03\x07\x01\x01'),
                            bytearray(b'\xfb{\x8b\x0b\xa4\x04u\x04\x19\xe0\x1c\xe0\x00\xfc\x00p\x04\x7ft\x7f{\x7f\xfb\xff\x7f\xff\xbf\xff\x0e\xfe\xf8\xf8'),
                            bytearray(b'\xb8\xb8\xb0\xb0`   \x80\x00\x00\x00\x00\x00\x00\x00@\xf8@\xf0\xc0\xe0\xc0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x01\x01\t\x08\x0f\x0e\x0f\x0f\x1d\x1d\x1d\x19\x1e\x1b\x00\x00\x00\x01\x01\x08\x01\x0e\x00\x0f\x02\x1f\x06\x1f\x05\x1e'),
                            bytearray(b'\xc0\xc0\xee\xee\xef\xef\xf9\xf9\xf9\xf9yy\x00x~\x82\x00\xc0\x00\xee\x00\xef\x06\xff\x06\xff\x86\xff\xff\x87\xfd\x03'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\xc0\x80\xc0\x80``\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80@\x80@\x80\x80\xe0'),
                            bytearray(b'<7=+:/ytzgUC\xf8\xcb\xb0\x88\x0b<\x178\x179\x0cs\x1fa\x0f`\x07\xc0F\xc1'),
                            bytearray(b'\n\xf3ey\xb5yU\x99\xa4yjs5\xc6\xeb\x0c\xfd\x00~\x80~\xc0\x1e\xe0~\xc0|\x80\xf8\x00p\x00'),
                            bytearray(b'`\xe00\xb0p\xf0X\x98x\xb8\xe8\x08\xe8\x00\xf8\x10\x80`@p\x000 8\x00\x18\x10\x18\x18\x10\x08\x10'),
                            bytearray(b"\xb5\x8c\xfb\xc6}B\x7f`\' \x0f\x00\x01\x00\x00\x00B\xc00\xe00`\x18p\x188\x0e\x0c\x07\x06\x00\x00"),
                            bytearray(b'\xb78\xefp\x9f`\xff\x00\xff\x00\xff\x00\xfd\x01\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x86\x03\xf8\xf8'),
                            bytearray(b'\xf0\x10\xf0\x10\xe0 \xe0 \xc0@\x80\x80\x00\x00\x00\x00\x00\x10 \x10\x00 @ \x00@\x00\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x000 0 \x00\x00\x00\x000 \xf00\xf0p\x00\x00\x10 \x10 \x00\x00\x00\x00\x10 \xc00\x80p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=102),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x10\x10\x10\x10\x00\x00\x00\x00\x00\x00\x03\x01\x1b\x11;;\x00\x10\x00\x10\x00\x00\x00\x00\x00\x00\x02\x01\n\x11\x00;'),
                            bytearray(b'\x00\x00PPxx\xfc\xfc\xfc\xfc\xff\xfe\xff\xff\xff\xff\x00\x00\x00P\x00x\x00\xfc\x00\xfc\x01\xfe\x00\xff\x00\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=102),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xf8\xf0\xf8\xf8\xf8\xf0\xf8\xf0\xf8\xf0xpxx88\x08\xf0\x00\xf8\x08\xf0\x08\xf0\x08\xf0\x88\xf0\x80\xf8\xc0\xf8'),
                            None,
                            bytearray(b'\xb8\xb8\xb0\xb0`   \x80\x00\x00\x00\x00\x00\x00\x00@\xf8@\xf0\xc0\xe0\xc0\xe0\xc0\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'??\x7f\x7f\x7f\x7fooNN]MyIvB\x00?\x00\x7f\x00\x7f\x10\x7f1\x7f\x02o\x06O\x0cO'),
                            bytearray(b'\xff\xff\xff\xff\xff\xffyy\xfe\xfe\xff\xff\xff\xff\xfb{\x00\xff\x00\xff\x00\xff\x86\xff\x01\xff\x00\xff\x00\xff\x04\x7f'),
                            bytearray(b'w\x0250\x19\x18\x16\x14\t\x08\t\x08\x04\x07\x00\x00L\x0e\x0e>\x06\x1e\x0b\x1f\x07\x0f\x07\x0f\x03\x07\x01\x01'),
                            bytearray(b'\xfb{\x8b\x0b\xa4\x04u\x04\x19\xe0\x1c\xe0\x00\xfc\x00p\x04\x7ft\x7f{\x7f\xfb\xff\x7f\xff\xbf\xff\x0e\xfe\xf8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=110),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xfe\xb0Lr\x8e\xc08\x00\xf0\x00\x00\xc0\xc0\x00\x00\xf6\xfe\xfe\xfe\xfc\xfe\xfc\xfc\xf8\xf8\xf0\xf0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=115),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00  aaAA\xc1\xc1\xe3\xe3\xb6\xb6\x00\x00\x00\x00\x00 \x00a A \xc1\x10\xe3I\xf7'),
                            None,
                            bytearray(b'\xf8\xb8\x9f\x9f\x7f\x7f44;8\x1c\x1c\x07\x07\x01\x01G\xff`\xff\x00\x7f\x0b?\x07?\x03\x1f\x00\x07\x00\x01'),
                            bytearray(b"\xd9\xd8\xfa\xf9\xe3\xe0\xc6\xc1\x05\x00\xe0\xe0\xf9\xf9\xfe\xfe\'\xff\x07\xff\x1f\xff?\xff\xff\xff\x1f\xff\x06\xff\x00\xfe"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=107),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x17\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x0f\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0'),
                            bytearray(b'g`\xdd\xc0\xbd\x9cs3\xa6\xa6NN>>||\x1f\x7f?\xffc\xff\xcc\xffY\xff\xb1\xff\xc1\xff\x83\xff'),
                            bytearray(b'\x00\xf8\x00\xfc\x88\x14\x18\x06X\x06\x98f\x00\xfe\xc0>\x88\xf8\xc4\xfc\xe4\xf4\xe2\xe6\xe2\xe6\xe2\xe6\xc6\xfe\xf6\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=99),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x00\x08\x07+\x1b\x151J$U1\xab\x1b\xc1^\x03\x00\x0f\x00;\x041\x0e`\x1fq\x0e{\x04?\x00'),
                            bytearray(b'\xc0\x00P\x90(\xcc\xa8\xcc\xaa\xcc"\xccW\x98\xaf0\xc0\x00\xe0\x00\xf0\x00\xf0\x00\xf0\x00\xf0\x00\xe0\x00\xc0\x00'),
                            bytearray(b'\x8f@\xa1a_?`\x1f?\x00?\x00\x0f\x00\x03\x00?\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'_`\xbf\xc0~\x80\xfe\x00\xfc\x00\xfc\x00\xf0\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=119),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'RBX@\x0f\x00)&\x04\x03\x18\x1b\x0c\x0c\x02\x02\xbd\x7f\xbf\x7f\x7f?_??\x1f\x07\x1f\x03\x0f\x01\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=130),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80'),
                            bytearray(b"\xc1\xc2C@\'@o\x80a\x9e`\x9e\x00\xfc@8<\xfe\xbc\xfc\x9c\xdc\x9d\x9d\x9f\x9f\x82\x9e\x84\xfc\xd8\xf8"),
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07//oo\x7f\x7f\x7f\x7f\x00\x00\x00\x00\x00\x03\x00\x07\x00/\x10o\x00\x7f\x80\x7f'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x00\x00\x00\x0000pppp\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x000\x00p\x80p'),
                            bytearray(b'ww\xef\xef\xcf\xcf\xcf\xcf\xef\xcf\xef\xcf\xed\xcd\xd5\xc5\x88\x7f\x10\xff0\xff0\xff0\xff0\xff2\xff:\xff'),
                            bytearray(b'\xf8\xf8\xfc\xfc\xfe\xfe\xfe\xfe\xff\xff\xff\xff\xdf\xdf\xce\xce\x00\xf8\x00\xfc\x00\xfe\x00\xfe\x00\xff\x00\xff \xff1\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xfe\xb0Lr\x8e\xc08\x00\xf0\x00\x00\xc0\xc0\x00\x00\xf6\xfe\xfe\xfe\xfc\xfe\xfc\xfc\xf8\xf8\xf0\xf0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=392, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00  aaAA\xc1\xc1\xe3\xe3\xb6\xb6\x00\x00\x00\x00\x00 \x00a A \xc1\x10\xe3I\xf7'),
                            None,
                            bytearray(b'\xf8\xb8\x9f\x9f\x7f\x7f44;8\x1c\x1c\x07\x07\x01\x01G\xff`\xff\x00\x7f\x0b?\x07?\x03\x1f\x00\x07\x00\x01'),
                            bytearray(b"\xd9\xd8\xfa\xf9\xe3\xe0\xc6\xc1\x05\x00\xe0\xe0\xf9\xf9\xfe\xfe\'\xff\x07\xff\x1f\xff?\xff\xff\xff\x1f\xff\x06\xff\x00\xfe"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x17\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x0f\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0'),
                            bytearray(b'g`\xdd\xc0\xbd\x9cs3\xa6\xa6NN>>||\x1f\x7f?\xffc\xff\xcc\xffY\xff\xb1\xff\xc1\xff\x83\xff'),
                            bytearray(b'\x00\xf8\x00\xfc\x88\x14\x18\x06X\x06\x98f\x00\xfe\xc0>\x88\xf8\xc4\xfc\xe4\xf4\xe2\xe6\xe2\xe6\xe2\xe6\xc6\xfe\xf6\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=112),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<<88pp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x048\x08p`\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xbc<\xf4\xf488\x0c\x0c\xe2b\x00\x00\x00\xe0\x00\xf8\xc0\xfc\x00\xf4\xc0\xf8\xf0\xfc\x9c\xfa'),
                            None,
                            bytearray(b'\xf6\x16\xde.\xbe~~\x9e\x0e\x0e\xee\xee\xae\xae\x1c\x1c\xe9\xfe\xf1\xfe\xc1\xfe\xe1\xfe\xf1\xfe\x10\xfeP\xbe`\x1c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x05\x06\x00\x0f\x00\x1f\x00?\x00\x7f\x00\x7f\x00\xff\x00\x01\x03\x07\x0f\x0f\x06\x1f(?H\x7f\x00\x7f\x80\xff'),
                            bytearray(b'||\xcf\x0f\xc79\x1d\xe0\t\xf1\x02\xfa\x01\xfe\x19\xe6\x83\xfc\xf0\xff\xfe\xff\x7f\xff~\xff}\xff\x7f\xff\x1f\xff'),
                            bytearray(b'\x00\xff \xdf`\x9fb\x9df\x19&\x196\t\x0e\x01\x80\xff\x80\xdf\x80\x9f\x80\x9d\x80\x99`y09\x1f\x1f'),
                            bytearray(b'\x1d\xe2\x19\xe6\x03\xfc\x07\xf8\x01\xfe\x03\xfd\x0f\xf3 \xc0\x7f\xff\x7f\xff\x1f\xff\x0f\xff\x0f\xff>\xff|\xff\xfe\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'RBX@\x0f\x00)&\x04\x03\x18\x1b\x0c\x0c\x02\x02\xbd\x7f\xbf\x7f\x7f?_??\x1f\x07\x1f\x03\x0f\x01\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=382),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80'),
                            bytearray(b"\xc1\xc2C@\'@o\x80a\x9e`\x9e\x00\xfc@8<\xfe\xbc\xfc\x9c\xdc\x9d\x9d\x9f\x9f\x82\x9e\x84\xfc\xd8\xf8"),
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=380, y=374),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07//oo\x7f\x7f\x7f\x7f\x00\x00\x00\x00\x00\x03\x00\x07\x00/\x10o\x00\x7f\x80\x7f'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x00\x00\x00\x0000pppp\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x000\x00p\x80p'),
                            bytearray(b'ww\xef\xef\xcf\xcf\xcf\xcf\xef\xcf\xef\xcf\xed\xcd\xd5\xc5\x88\x7f\x10\xff0\xff0\xff0\xff0\xff2\xff:\xff'),
                            bytearray(b'\xf8\xf8\xfc\xfc\xfe\xfe\xfe\xfe\xff\xff\xff\xff\xdf\xdf\xce\xce\x00\xf8\x00\xfc\x00\xfe\x00\xfe\x00\xff\x00\xff \xff1\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=366),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xfe\xb0Lr\x8e\xc08\x00\xf0\x00\x00\xc0\xc0\x00\x00\xf6\xfe\xfe\xfe\xfc\xfe\xfc\xfc\xf8\xf8\xf0\xf0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=394, y=126),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00  aaAA\xc1\xc1\xe3\xe3\xb6\xb6\x00\x00\x00\x00\x00 \x00a A \xc1\x10\xe3I\xf7'),
                            None,
                            bytearray(b'\xf8\xb8\x9f\x9f\x7f\x7f44;8\x1c\x1c\x07\x07\x01\x01G\xff`\xff\x00\x7f\x0b?\x07?\x03\x1f\x00\x07\x00\x01'),
                            bytearray(b"\xd9\xd8\xfa\xf9\xe3\xe0\xc6\xc1\x05\x00\xe0\xe0\xf9\xf9\xfe\xfe\'\xff\x07\xff\x1f\xff?\xff\xff\xff\x1f\xff\x06\xff\x00\xfe"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=378, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x17\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x0f\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0'),
                            bytearray(b'g`\xdd\xc0\xbd\x9cs3\xa6\xa6NN>>||\x1f\x7f?\xffc\xff\xcc\xffY\xff\xb1\xff\xc1\xff\x83\xff'),
                            bytearray(b'\x00\xf8\x00\xfc\x88\x14\x18\x06X\x06\x98f\x00\xfe\xc0>\x88\xf8\xc4\xfc\xe4\xf4\xe2\xe6\xe2\xe6\xe2\xe6\xc6\xfe\xf6\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=110),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<<88pp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x048\x08p`\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=391, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xbc<\xf4\xf488\x0c\x0c\xe2b\x00\x00\x00\xe0\x00\xf8\xc0\xfc\x00\xf4\xc0\xf8\xf0\xfc\x9c\xfa'),
                            None,
                            bytearray(b'\xf6\x16\xde.\xbe~~\x9e\x0e\x0e\xee\xee\xae\xae\x1c\x1c\xe9\xfe\xf1\xfe\xc1\xfe\xe1\xfe\xf1\xfe\x10\xfeP\xbe`\x1c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=391, y=358),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x05\x06\x00\x0f\x00\x1f\x00?\x00\x7f\x00\x7f\x00\xff\x00\x01\x03\x07\x0f\x0f\x06\x1f(?H\x7f\x00\x7f\x80\xff'),
                            bytearray(b'||\xcf\x0f\xc79\x1d\xe0\t\xf1\x02\xfa\x01\xfe\x19\xe6\x83\xfc\xf0\xff\xfe\xff\x7f\xff~\xff}\xff\x7f\xff\x1f\xff'),
                            bytearray(b'\x00\xff \xdf`\x9fb\x9df\x19&\x196\t\x0e\x01\x80\xff\x80\xdf\x80\x9f\x80\x9d\x80\x99`y09\x1f\x1f'),
                            bytearray(b'\x1d\xe2\x19\xe6\x03\xfc\x07\xf8\x01\xfe\x03\xfd\x0f\xf3 \xc0\x7f\xff\x7f\xff\x1f\xff\x0f\xff\x0f\xff>\xff|\xff\xfe\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=358),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'RBX@\x0f\x00)&\x04\x03\x18\x1b\x0c\x0c\x02\x02\xbd\x7f\xbf\x7f\x7f?_??\x1f\x07\x1f\x03\x0f\x01\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=367, y=376),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80'),
                            bytearray(b"\xc1\xc2C@\'@o\x80a\x9e`\x9e\x00\xfc@8<\xfe\xbc\xfc\x9c\xdc\x9d\x9d\x9f\x9f\x82\x9e\x84\xfc\xd8\xf8"),
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=368),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07//oo\x7f\x7f\x7f\x7f\x00\x00\x00\x00\x00\x03\x00\x07\x00/\x10o\x00\x7f\x80\x7f'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x00\x00\x00\x0000pppp\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x000\x00p\x80p'),
                            bytearray(b'ww\xef\xef\xcf\xcf\xcf\xcf\xef\xcf\xef\xcf\xed\xcd\xd5\xc5\x88\x7f\x10\xff0\xff0\xff0\xff0\xff2\xff:\xff'),
                            bytearray(b'\xf8\xf8\xfc\xfc\xfe\xfe\xfe\xfe\xff\xff\xff\xff\xdf\xdf\xce\xce\x00\xf8\x00\xfc\x00\xfe\x00\xfe\x00\xff\x00\xff \xff1\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=367, y=360),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xfe\xb0Lr\x8e\xc08\x00\xf0\x00\x00\xc0\xc0\x00\x00\xf6\xfe\xfe\xfe\xfc\xfe\xfc\xfc\xf8\xf8\xf0\xf0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=391, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00  aaAA\xc1\xc1\xe3\xe3\xb6\xb6\x00\x00\x00\x00\x00 \x00a A \xc1\x10\xe3I\xf7'),
                            None,
                            bytearray(b'\xf8\xb8\x9f\x9f\x7f\x7f44;8\x1c\x1c\x07\x07\x01\x01G\xff`\xff\x00\x7f\x0b?\x07?\x03\x1f\x00\x07\x00\x01'),
                            bytearray(b"\xd9\xd8\xfa\xf9\xe3\xe0\xc6\xc1\x05\x00\xe0\xe0\xf9\xf9\xfe\xfe\'\xff\x07\xff\x1f\xff?\xff\xff\xff\x1f\xff\x06\xff\x00\xfe"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0e\x0e\x17\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x0f\x1f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\xf0\xf0'),
                            bytearray(b'g`\xdd\xc0\xbd\x9cs3\xa6\xa6NN>>||\x1f\x7f?\xffc\xff\xcc\xffY\xff\xb1\xff\xc1\xff\x83\xff'),
                            bytearray(b'\x00\xf8\x00\xfc\x88\x14\x18\x06X\x06\x98f\x00\xfe\xc0>\x88\xf8\xc4\xfc\xe4\xf4\xe2\xe6\xe2\xe6\xe2\xe6\xc6\xfe\xf6\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=383, y=112),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<<88pp\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x048\x08p`\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xbc<\xf4\xf488\x0c\x0c\xe2b\x00\x00\x00\xe0\x00\xf8\xc0\xfc\x00\xf4\xc0\xf8\xf0\xfc\x9c\xfa'),
                            None,
                            bytearray(b'\xf6\x16\xde.\xbe~~\x9e\x0e\x0e\xee\xee\xae\xae\x1c\x1c\xe9\xfe\xf1\xfe\xc1\xfe\xe1\xfe\xf1\xfe\x10\xfeP\xbe`\x1c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x05\x06\x00\x0f\x00\x1f\x00?\x00\x7f\x00\x7f\x00\xff\x00\x01\x03\x07\x0f\x0f\x06\x1f(?H\x7f\x00\x7f\x80\xff'),
                            bytearray(b'||\xcf\x0f\xc79\x1d\xe0\t\xf1\x02\xfa\x01\xfe\x19\xe6\x83\xfc\xf0\xff\xfe\xff\x7f\xff~\xff}\xff\x7f\xff\x1f\xff'),
                            bytearray(b'\x00\xff \xdf`\x9fb\x9df\x19&\x196\t\x0e\x01\x80\xff\x80\xdf\x80\x9f\x80\x9d\x80\x99`y09\x1f\x1f'),
                            bytearray(b'\x1d\xe2\x19\xe6\x03\xfc\x07\xf8\x01\xfe\x03\xfd\x0f\xf3 \xc0\x7f\xff\x7f\xff\x1f\xff\x0f\xff\x0f\xff>\xff|\xff\xfe\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=354),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b' @\xa8\xa8\xbc\xb4\xff\xff\xff\xff\xfe\xfe\xfc\xfc\xc0\xc0\xb0\xf0P\xf8H\xf4\x00\xff\x00\xff\x00\xfe\x00\xfc\x00\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00`  \x00\x00\x00\x00\x00\x00\x01\x01\x03\x0e\x0e\x00\x00@``@\x00\x00\x00\x00\x01\x01\x02\x03\x01\x0f'),
                            None,
                            bytearray(b'==yy\xe9\xd1\xff\xc6\xff\xfe\x7f\x7f\x1f\x1f\x0f\x03\x02?\x06\x7f\x06\xd7\x00\xc6\x00\xfe\x00\x7f\x00\x1f\x0c\x03'),
                            bytearray(b"\x98\x90\xfb\xfb\xff\xffg\xa7\xe7\'\xff\xff\xff\xff\xff\xffo\xff\x04\xff\x00\xff\x18\xbf\x18?\x00\xff\x00\xff\x00\xff"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x000\x10\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 00 \x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00|@\xbe`\x1f\x87\x88\x00\x00\x00\x00\x00\x00\x00\x00d|\xe1\xff\xf7\xff\x7f\xff'),
                            bytearray(b'\x00\x00\x03\x01\x01\x00\x02\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\x00\x06\x07\x07\x06\x02\x00\x00\x00\x00\x00\x00\x80\x80\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=108),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\xf8\xf0\xe0\xf0\xe0\xe0\xc0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\xf8\x10\xe0\x10\xe0 \xc0 \xc0\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=129),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'??\x1f\x1f\x1f\x1f\x0f\r\x05\x01\x01\x01\x00\x00\x00\x00\x00?\x00\x1f\x00\x1f\x02\r\x04\x01\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfd\xfe\xfc\xfc\xf8\xfcx\x00\xff\x00\xff\x00\xff\x00\xff\x02\xfd\x02\xfc\x04\xf8\x84x'),
                            None,
                            bytearray(b'80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x080\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00\xc0\x00\xc0@\x00\x00\x00\x00\x00((\x00\x00\x80\x80\xc0\xc0\xe0\xe0\xe0\xe0\xf0\xf0\xf0\xf0\xd0\xf8'),
                            None,
                            bytearray(b'\xbc\xb8\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xfc\xf8\xf8D\xf8\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x02\x01\x0b\x08\x03\x00\x00\x00\x08\x0899\x00\x00\x01\x01\x06\x07\x07\x0f\x0f\x0f\x1f\x1f\x17\x1f\x06?'),
                            bytearray(b'\x00~\x80\x7f\x00\xff\x07\xf8x\x00 \x00\xc1\xc1\xc7\xc7~~\x81\xff\x07\xff\xff\xff\xff\xff\xff\xff>\xff8\xff'),
                            bytearray(b'-5\x7fg\x7fg\x7fg\x7f\x7f??????\x027\x00g\x00g\x00g\x00\x7f\x00?\x00?\x00?'),
                            bytearray(b'\xc7\xc7O\x8f\xdf\x1f\xff?\xff?\xff\xff\xff\xff\xff\xff8\xff0\xbf ?\x00?\x00?\x00\xff\x00\xff\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=113),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=7),
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
                        AnimationSequenceFrame(duration=2, mold_id=16),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=17),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL063_FIREBALL_SURFACE_FROM_LAVA,
    palette_offset=0,
    unknown_num=0
)
