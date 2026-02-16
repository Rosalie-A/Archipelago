# SPR0955_SMALLER_RED_FIREWORK

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL759_SMALLER_RED_FIREWORK
sprite = CompleteSprite(
    animation=AnimationPack(440, length=460, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=4096,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x1c\x14"\x08*\x14"\x00\x1c\x00\x00\x00\x00\x00\x00\x1c\x00>\x006\x00>\x00\x1c\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=123),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x12\x00-\x00\x01\x00\\\x08\x95\x1c\xdd\x08\x14\x00\\\x00\x00\x12\x12?~\x7f7wb\xe36\xf7*>\x00\\'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=123),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\t\x08\r\x00\x0e\x00\x01\x04\x1d\x00\x00\x00\x00\x00\x00\x01\x08\x01\x00\x1f\x01\x0f\x03\x07\x03?'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc8\x00\x00@\x90 \x82\x10\xee\x80\x00\x00\x00\x00\x00\x10\x00\xc8\x80\xd2\xc0\xf8\xe0\xf2p~'),
                            bytearray(b'\x10\x04\x06\x01\x03\x00\t\x08\x02\x00 \x00\x00\x00\x00\x00\x03\x17\x00\x17\x00\x07\x08\x03\x00\x02\x00"\x00\x00\x00\x00'),
                            bytearray(b'\xc8\x10P @\xa0\x88\x08\xa0\x80\x00\x00\x00\x00\x00\x00\xe0\xf8\xc0\xf8\x00\xf0\x08\xa0\x00\xa0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xc8\x80\xa0\x08\x00 \x88p`\x00\x00\x00\x06\x04@\x00px\xf0\xf9\xd8\xf8\x80\xfc\x00\xf1\x00\x00\x14\x92\x00@'),
                            bytearray(b'\x06\x00 \x00 \x00 \x00(\x00\x00\x00\x10\x10\x90\x80\x00\x06\x000\x00`\x00$\x00(\x00 \x10\x00\x800'),
                            bytearray(b'H@\x80\x00\x80\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00H\x00\x88\x00\x81\x00\x88\x80\x00\x00\x02\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00@\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00 \x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=111),
                        Tile(mirror=True, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xb0 \x08\x00\x83\x00\x00\x00\x80\x00\x00\x00\x00\x80\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x00\x00\x90\x00\x80'),
                            bytearray(b'\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x10\x00@@ \x00\x00\x00\x00\x00\x000\x00 \x00\x00\x00\x90@\x04\x00\xa0'),
                            bytearray(b'\xd1\x00\x82\x00\x04P\x88 \xc5\x00\xa8\x00\xf2\x84\xf2\xcc\x00\xd9\x00\x82\xa0\xf4\xd0\xfd\xf8\xfd\xf8\xf9x~0>'),
                            bytearray(b'\x00\x00\x08\x08\x18\x00\x00\x00\x00\x00b \x02\x02\x08\x08\x00\x00\x08\x00\x008\x00\x04\x00\x08\x00b\x00\x02\x08\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=127),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xc8\x80\xa0\x08\x00 \x88p`\x00\x00\x00\x06\x04@\x00px\xf0\xf9\xd8\xf8\x80\xfc\x00\xf1\x00\x00\x14\x92\x00@'),
                            bytearray(b'\x06\x00 \x00 \x00 \x00(\x00\x00\x00\x10\x10\x90\x80\x00\x06\x000\x00`\x00$\x00(\x00 \x10\x00\x800'),
                            bytearray(b'H@\x80\x00\x80\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00H\x00\x88\x00\x81\x00\x88\x80\x00\x00\x02\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00@\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00 \x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xb0 \x08\x00\x83\x00\x00\x00\x80\x00\x00\x00\x00\x80\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x00\x00\x90\x00\x80'),
                            bytearray(b'\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x10\x00@@ \x00\x00\x00\x00\x00\x000\x00 \x00\x00\x00\x90@\x04\x00\xa0'),
                            bytearray(b'\xd1\x00\x82\x00\x04P\x88 \xc5\x00\xa8\x00\xf2\x84\xf2\xcc\x00\xd9\x00\x82\xa0\xf4\xd0\xfd\xf8\xfd\xf8\xf9x~0>'),
                            bytearray(b'\x00\x00\x08\x08\x18\x00\x00\x00\x00\x00b \x02\x02\x08\x08\x00\x00\x08\x00\x008\x00\x04\x00\x08\x00b\x00\x02\x08\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\xc1\x00\x80\x00\xb0\x00\xfc\x00\xfc\x00X\x00>\x00:\x00\x00\xc1\x00\x80\x00\xb0\x00\xfc\x00\xfc\xa0\xf8@\xfe\x00\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc1\x00\x80\x00\xb0\x00\xfc\x00\xfc\x00X\x00>\x00:\x00\x00\xc1\x00\x80\x00\xb0\x00\xfc\x00\xfc\xa0\xf8@\xfe\x00\xfe'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=True, invert=True, format=0, length=5, subtile_bytes=[
                            bytearray(b'8\x00x\x00\xf0\x00\xe0\x00\xe0\x00\x00\x00\x02\x00@\x00@\xf8\x80\xf8\x00\xf8\x00\xe0\x00\xe0\x00\x00\x00\x06\x00@'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00@\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00 \x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=111),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x06\x00 \x00 \x00 \x00(\x00\x00\x00\x10\x10\x90\x80\x00\x06\x000\x00`\x00$\x00(\x00 \x10\x00\x800'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=118),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x10\x00@@ \x00\x00\x00\x00\x00\x000\x00 \x00\x00\x00\x90@\x04\x00\xa0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\xb0 \x08\x00\x83\x00\x00\x00\x80\x00\x00\x00\x00\x80\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x00\x00\x90\x00\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'8\x00x\x00\xf0\x00\xe0\x00\xe0\x00\x00\x00\x02\x00@\x00@\xf8\x80\xf8\x00\xf8\x00\xe0\x00\xe0\x00\x00\x00\x06\x00@'),
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00@\x00\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00P\x00\x00\x00\x00\x00 \x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x06\x00 \x00 \x00 \x00(\x00\x00\x00\x10\x10\x90\x80\x00\x06\x000\x00`\x00$\x00(\x00 \x10\x00\x800'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x08\x08\x18\x00\x00\x00\x00\x00b \x02\x02\x08\x08\x00\x00\x08\x00\x008\x00\x04\x00\x08\x00b\x00\x02\x08\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x10\x00@@ \x00\x00\x00\x00\x00\x000\x00 \x00\x00\x00\x90@\x04\x00\xa0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xb0 \x08\x00\x83\x00\x00\x00\x80\x00\x00\x00\x00\x80\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x00\x00\x90\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'A\x00\x00\x00\x00\x00\x84\x00\xa0\x00`\x804\xc0\x10`\x00A\x00\x00\x00\x00\x00\x84\x00\xa0\x00\xe0\x00\xf4\x00\xf0'),
                            None,
                            bytearray(b'0\xc0`\x80@\x00 \x00\x80\x00\x00\x00\x02\x00\x00\x00\x00\xf0\x00\xe0\x00@\x00 \x00\x80\x00\x00\x00\x02\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'A\x00\x00\x00\x00\x00\x84\x00\xa0\x00`\x804\xc0\x10`\x00A\x00\x00\x00\x00\x00\x84\x00\xa0\x00\xe0\x00\xf4\x00\xf0'),
                            None,
                            bytearray(b'0\xc0`\x80@\x00 \x00\x80\x00\x00\x00\x02\x00\x00\x00\x00\xf0\x00\xe0\x00@\x00 \x00\x80\x00\x00\x00\x02\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x10 \xe0\x00\xc0\x00\x80"\x00\x00\x08\x00\x02\x88\x00\x00\x000\x00\xe0\x00\xc0\x00\xa2\x00\x00\x00\x08\x00\x8a\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'A\x12\x00\x00\x00\x00\x04\x00\x00\x80\xc0 \xb4\x00p\x00\x00S\x00\x00\x00\x00\x00\x04\x00\x80\x00\xe0\x00\xb4\x00p'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10 \xe0\x00\xc0\x00\x80"\x00\x00\x08\x00\x02\x88\x00\x00\x000\x00\xe0\x00\xc0\x00\xa2\x00\x00\x00\x08\x00\x8a\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'A\x12\x00\x00\x00\x00\x04\x00\x00\x80\xc0 \xb4\x00p\x00\x00S\x00\x00\x00\x00\x00\x04\x00\x80\x00\xe0\x00\xb4\x00p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'H@\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x10\x00\x00\x00@\x18\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x10\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=111),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'@\x04J\x00\x88@\x88\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00D\x00J\x00\xc8\x00\x89\x00\x88\x80\x00\x00\x02\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=110),
                        Tile(mirror=True, invert=True, format=0, length=7, subtile_bytes=[
                            bytearray(b'A\x12\x00\x00\x00\x00\x04\x00\x00\x80\xc0 \xb4\x00p\x00\x00S\x00\x00\x00\x00\x00\x04\x00\x80\x00\xe0\x00\xb4\x00p'),
                            bytearray(b'\x00\x00\x04\x04\x1c\x00\x00 \x00\x001\x00\x01\x01D\x00\x00\x00\x04\x00\x00\x1c\x00"\x00\x04\x001\x00\x01\x00D'),
                            bytearray(b'\x10 \xe0\x00\xc0\x00\x80"\x00\x00\x08\x00\x02\x88\x00\x00\x000\x00\xe0\x00\xc0\x00\xa2\x00\x00\x00\x08\x00\x8a\x00\x00'),
                            bytearray(b'\x13@\x10\x000\x00\x10\x004\x80\x00\x00\x08\x08\x00\x00\x00S\x00\x18\x000\x00\x12\x00\xb4\x00\x10\x08\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=119),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x08\x00\x10\x00\x00\x00\x08\x00 \x00\x10\x00\x00\x00\x00\x00\x00\x18\x00\x10\x00\x00\x00H\x00"\x00P\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=135),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\xb0 \x88\x00\x83\x00\x00\x04\x90@\xc0\x00\x00\x00\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x04\x00\xd0\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'H@\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x10\x00\x00\x00@\x18\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x10\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=136),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x04J\x00\x88@\x88\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00D\x00J\x00\xc8\x00\x89\x00\x88\x80\x00\x00\x02\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=137),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'A\x12\x00\x00\x00\x00\x04\x00\x00\x80\xc0 \xb4\x00p\x00\x00S\x00\x00\x00\x00\x00\x04\x00\x80\x00\xe0\x00\xb4\x00p'),
                            bytearray(b'\x00\x00\x04\x04\x1c\x00\x00 \x00\x001\x00\x01\x01D\x00\x00\x00\x04\x00\x00\x1c\x00"\x00\x04\x001\x00\x01\x00D'),
                            bytearray(b'\x10 \xe0\x00\xc0\x00\x80"\x00\x00\x08\x00\x02\x88\x00\x00\x000\x00\xe0\x00\xc0\x00\xa2\x00\x00\x00\x08\x00\x8a\x00\x00'),
                            bytearray(b'\x13@\x10\x000\x00\x10\x004\x80\x00\x00\x08\x08\x00\x00\x00S\x00\x18\x000\x00\x12\x00\xb4\x00\x10\x08\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x08\x00\x10\x00\x00\x00\x08\x00 \x00\x10\x00\x00\x00\x00\x00\x00\x18\x00\x10\x00\x00\x00H\x00"\x00P\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xb0 \x88\x00\x83\x00\x00\x04\x90@\xc0\x00\x00\x00\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x04\x00\xd0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=111),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x10 \xe0\x00\xc0\x00\x80"\x00\x00\x08\x00\x02\x88\x00\x00\x000\x00\xe0\x00\xc0\x00\xa2\x00\x00\x00\x08\x00\x8a\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=129),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'A\x12\x00\x00\x00\x00\x04\x00\x00\x80\xc0 \xb4\x00p\x00\x00S\x00\x00\x00\x00\x00\x04\x00\x80\x00\xe0\x00\xb4\x00p'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=119),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'H@\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x10\x00\x00\x00@\x18\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x10\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=110),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'@\x04J\x00\x88@\x88\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00D\x00J\x00\xc8\x00\x89\x00\x88\x80\x00\x00\x02\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=109),
                        Tile(mirror=True, invert=True, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x04\x04\x1c\x00\x00 \x00\x001\x00\x01\x01D\x00\x00\x00\x04\x00\x00\x1c\x00"\x00\x04\x001\x00\x01\x00D'),
                            None,
                            bytearray(b'\x13@\x10\x000\x00\x10\x004\x80\x00\x00\x08\x08\x00\x00\x00S\x00\x18\x000\x00\x12\x00\xb4\x00\x10\x08\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=119),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x08\x00\x10\x00\x00\x00\x08\x00 \x00\x10\x00\x00\x00\x00\x00\x00\x18\x00\x10\x00\x00\x00H\x00"\x00P\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=136),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\xb0 \x88\x00\x83\x00\x00\x04\x90@\xc0\x00\x00\x00\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x04\x00\xd0\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=137),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x10 \xe0\x00\xc0\x00\x80"\x00\x00\x08\x00\x02\x88\x00\x00\x000\x00\xe0\x00\xc0\x00\xa2\x00\x00\x00\x08\x00\x8a\x00\x00'),
                            None,
                            None,
                            bytearray(b'H@\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x10\x00\x00\x00@\x18\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x10\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x04J\x00\x88@\x88\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00D\x00J\x00\xc8\x00\x89\x00\x88\x80\x00\x00\x02\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=138),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x04\x04\x1c\x00\x00 \x00\x001\x00\x01\x01D\x00\x00\x00\x04\x00\x00\x1c\x00"\x00\x04\x001\x00\x01\x00D'),
                            None,
                            bytearray(b'\x13@\x10\x000\x00\x10\x004\x80\x00\x00\x08\x08\x00\x00\x00S\x00\x18\x000\x00\x12\x00\xb4\x00\x10\x08\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x08\x00\x10\x00\x00\x00\x08\x00 \x00\x10\x00\x00\x00\x00\x00\x00\x18\x00\x10\x00\x00\x00H\x00"\x00P\x00\x00'),
                            bytearray(b'A\x12\x00\x00\x00\x00\x04\x00\x00\x80\xc0 \xb4\x00p\x00\x00S\x00\x00\x00\x00\x00\x04\x00\x80\x00\xe0\x00\xb4\x00p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xb0 \x88\x00\x83\x00\x00\x04\x90@\xc0\x00\x00\x00\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x04\x00\xd0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=110),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=131),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=139),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=127),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=137),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'H@\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x10\x00\x00\x00@\x18\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x10\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=109),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x13@\x10\x000\x00\x10\x004\x80\x00\x00\x08\x08\x00\x00\x00S\x00\x18\x000\x00\x12\x00\xb4\x00\x10\x08\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=119),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\xb0 \x88\x00\x83\x00\x00\x04\x90@\xc0\x00\x00\x00\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x04\x00\xd0\x00\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=138),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'H@\x00\x00\x00\x00 \x00\x00\x00\x00\x00\x10\x00\x00\x00@\x18\x00\x00\x00\x00\x00(\x00\x00\x00\x00\x00\x10\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=138),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            bytearray(b'\x13@\x10\x000\x00\x10\x004\x80\x00\x00\x08\x08\x00\x00\x00S\x00\x18\x000\x00\x12\x00\xb4\x00\x10\x08\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x08\x00\x10\x00\x00\x00\x08\x00 \x00\x10\x00\x00\x00\x00\x00\x00\x18\x00\x10\x00\x00\x00H\x00"\x00P\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xb0 \x88\x00\x83\x00\x00\x04\x90@\xc0\x00\x00\x00\x00\x02\x00\xb0\x00\x88\x00\x83\x00\x04\x00\xd0\x00\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=109),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=110),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=138),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=133),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=129),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=138),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=139),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=134),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=140),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=130),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=138),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=133),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=129),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=139),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=135),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=140),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=141),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=139),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=140),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=141),
                        Tile(mirror=False, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            bytearray(b'@\x02\x08\x00\x00\x00\x02\x00\x00\x00\x00\x08!\x00\x00\x00\x00B\x00\x08\x00\x00\x00\x02\x00\x00\x00\x08\x00!\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=142),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL759_SMALLER_RED_FIREWORK,
    palette_offset=0,
    unknown_num=8
)
