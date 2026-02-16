# SPR0005_MARIO_HAMMER_ATTACK_UP_RIGHT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL644_MARIO_ATTACK_UP_RIGHT
sprite = CompleteSprite(
    animation=AnimationPack(244, length=677, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0H\xf8\x00\xf8\x00p\x88\xa0\xd0@\xe0\x00\x80\x80\x80\xf8\xf8\x88\x88\x88\x88\x98\x98\xf0p\xe0 \x80@\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\t\x00\x07\x07/\x0fO\x0f\x1e\x1f\x00\x00\x00\x00\x00\x01\x00\x0f\x07\x18\x0f0\x0fp\x1f`'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc0\x00\xa0\x80\xd0\xc0\xe0\xe00\xf0\x00\x00\x00\x00\x00\xe0\x00\xf0\x80x\xc08\xe0\x18\xf0\x08'),
                            bytearray(b'\xbe?\xbc?|\x7f|\x7f<?p\x7f\xb0?\x9f\x9f?\xc0?\xc0\x7f\x80\x7f\x80?\xc0\x7f\x80?\xc0\x9f\xe0'),
                            bytearray(b'\x1c\xf8\x0c\xf8\x04\xf4\x14\xf4\r\xed\r\xc5\x0e\x93HS\xf8\x04\xf8\x04\xf4\x0c\xf4\r\xed\x1e\xcd6\xabDk\xc4'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'a\x00?#\x13 \x0eo}\x1fp\x9fh\x8fT7\x00\x7f#?<\x0fp_`\x7f\xa0\xbf\xb0\xbfh\x7f'),
                            bytearray(b'\xf4\xc6\xe4\xc4\xe4\xe0h\xe0\xe0\xe00\xe0\x04\xe4\xe0\xe0\xe6\xd9\xc4\xfa\x00\xfc\x04\xfc\x0c\xfc\x1c\xec\x1c\xfc\x18\xf8'),
                            bytearray(b'\x04\x1c\x02\x1e"\x1e \x1c7\x00?"\x1f\x1f\x00\x00\x03\x1f\x01\x1f\x01?\x03?<\x03*7\x1f\x1f\x00\x00'),
                            bytearray(b'pp\xd0\xf0\x14\xf4\x16\xf2\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x88\xf8\x08\xf8\x0c\xfc\n\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0H\xf8\x00\xf8\x00p\x88\xa0\xd0@\xe0\x00\x80\x80\x80\xf8\xf8\x88\x88\x88\x88\x98\x98\xf0p\xe0 \x80@\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\t\x00\x07\x07/\x0fO\x0f\x1e\x1f\x00\x00\x00\x00\x00\x01\x00\x0f\x07\x18\x0f0\x0fp\x1f`'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc0\x00\xa0\x80\xd0\xc0\xe0\xe00\xf0\x00\x00\x00\x00\x00\xe0\x00\xf0\x80x\xc08\xe0\x18\xf0\x08'),
                            bytearray(b'\xbe?\xbc?|\x7f|\x7f<?p\x7f\xb0?\x9f\x9f?\xc0?\xc0\x7f\x80\x7f\x80?\xc0\x7f\x80?\xc0\x9f\xe0'),
                            bytearray(b'\x1c\xf8\x0c\xf8\x04\xf4\x14\xf4\r\xed\r\xc5\x0e\x93HS\xf8\x04\xf8\x04\xf4\x0c\xf4\r\xed\x1e\xcd6\xabDk\xc4'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'a\x00?#\x13 \x0eo}\x1fp\x9fh\x8fT7\x00\x7f#?<\x0fp_`\x7f\xa0\xbf\xb0\xbfh\x7f'),
                            bytearray(b'\xf4\xc6\xe4\xc4\xe4\xe0h\xe0\xe0\xe00\xe0\x04\xe4\xe0\xe0\xe6\xd9\xc4\xfa\x00\xfc\x04\xfc\x0c\xfc\x1c\xec\x1c\xfc\x18\xf8'),
                            bytearray(b'\x04\x1c\x02\x1e"\x1e \x1c7\x00?"\x1f\x1f\x00\x00\x03\x1f\x01\x1f\x01?\x03?<\x03*7\x1f\x1f\x00\x00'),
                            bytearray(b'pp\xd0\xf0\x14\xf4\x16\xf2\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x88\xf8\x08\xf8\x0c\xfc\n\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0H\xf8\x00\xf8\x00p\x88\xa0\xd0@\xe0\x00\x80\x80\x80\xf8\xf8\x88\x88\x88\x88\x98\x98\xf0p\xe0 \x80@\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'a\x00?#\x13 \x0eo}\x1fp\x9fh\x8fT7\x00\x7f#?<\x0fp_`\x7f\xa0\xbf\xb0\xbfh\x7f'),
                            bytearray(b'\xf4\xc6\xe4\xc4\xe4\xe0h\xe0\xe0\xe00\xe0\x04\xe4\xe0\xe0\xe6\xd9\xc4\xfa\x00\xfc\x04\xfc\x0c\xfc\x1c\xec\x1c\xfc\x18\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\t\x00\x07\x07/\x0fO\x0f\x1e\x1f\x00\x00\x00\x00\x00\x01\x00\x0f\x07\x18\x0f0\x0fp\x1f`'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc0\x00\xa0\x80\xd0\xc0\xe0\xe00\xf0\x00\x00\x00\x00\x00\xe0\x00\xf0\x80x\xc08\xe0\x18\xf0\x08'),
                            bytearray(b'\xbe?\xbc?|\x7f|\x7f<?p\x7f\xb0?\x9f\x9f?\xc0?\xc0\x7f\x80\x7f\x80?\xc0\x7f\x80?\xc0\x9f\xe0'),
                            bytearray(b'\x1c\xf8\x0c\xf8\x04\xf4\x14\xf4\r\xed\r\xc5\x0e\x93HS\xf8\x04\xf8\x04\xf4\x0c\xf4\r\xed\x1e\xcd6\xabDk\xc4'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=102),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x04\x1c\x02\x1e"\x1e \x1c7\x00?"\x1f\x1f\x00\x00\x03\x1f\x01\x1f\x01?\x03?<\x03*7\x1f\x1f\x00\x00'),
                            bytearray(b'pp\xd0\xf0\x14\xf4\x16\xf2\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x88\xf8\x08\xf8\x0c\xfc\n\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x01\x00\x01\x02\x01\x02\x01\x02\x00\x01\x00\x00\x00\x00\x01\x01\x01\x01\x03\x03\x02\x02\x02\x02\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x10\x10\x16\x17\x02\x03\t\t2>AGd\x00\xff\x01\x1f\x1f\x18\x1f\x1c\x1f\x16\x1f!?xG;Gy\x87'),
                            bytearray(b'\xc4\xf8\x00\xfc\x04\xfc\xfc\xfc$<\xa0\xbc\xc2\xfe\xfe\x00\x04\xf8\x00\xfc\x00\xfc\x02\xfe\xc2\xfe\xc2\xfe\x80\xfe8\xc6'),
                            bytearray(b'\xfe\x00\xfe\x00|\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x86x\x86p\x0c\x00p\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xee\x00\xff\xf0\x7fx><\x00\x00\x00\x00\x00\x00\x00\x00\x1c\xe2\xf4\xfbx\x7f<>\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x00\x03/\x0fO\x0f\x9c\x1f\x0c\xff\xf8\x00\xfd\x03\x01\x02\x03\x0c/\x10\x0fp\x1f\xe0\xff\xe0x\x7fA@'),
                            bytearray(b'\xc0\x00p\xe08\xf0\x90\xf0p\xf80\xf80p\x8c\x80\xe0\x00\xf0\x00\xb8\x00\xf0\x08\xf8\x00\xf8\x00p\x88\x8cp'),
                            bytearray(b'\xfe\x01\xfd\x03x\x84\xc6>\xbe>N\x0e \x00\x1f\x10\xc3\xc2ED\xfc\xff\xfe\xf9>\xc1\x0eq\x00?\x10\x1f'),
                            bytearray(b'4\xf4\x88\xf8p80\x1cp\x1cd \xfc \x000\xf0\x08\xf8\x048\xc4\x1c\xe2\x1c\xe2 \xfe \xfc\xc0\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=96),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x01\x00\x01\x02\x01\x02\x01\x02\x00\x01\x00\x00\x00\x00\x01\x01\x01\x01\x03\x03\x02\x02\x02\x02\x01\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x10\x10\x16\x17\x02\x03\t\t2>AGd\x00\xff\x01\x1f\x1f\x18\x1f\x1c\x1f\x16\x1f!?xG;Gy\x87'),
                            bytearray(b'\xc4\xf8\x00\xfc\x04\xfc\xfc\xfc$<\xa0\xbc\xc2\xfe\xfe\x00\x04\xf8\x00\xfc\x00\xfc\x02\xfe\xc2\xfe\xc2\xfe\x80\xfe8\xc6'),
                            bytearray(b'\xfe\x00\xfe\x00|\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x86x\x86p\x0c\x00p\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xee\x00\xff\xf0\x7fx><\x00\x00\x00\x00\x00\x00\x00\x00\x1c\xe2\xf4\xfbx\x7f<>\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=366),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x00\x03/\x0fO\x0f\x9c\x1f\x0c\xff\xf8\x00\xfd\x03\x01\x02\x03\x0c/\x10\x0fp\x1f\xe0\xff\xe0x\x7fA@'),
                            bytearray(b'\xc0\x00p\xe08\xf0\x90\xf0p\xf80\xf80p\x8c\x80\xe0\x00\xf0\x00\xb8\x00\xf0\x08\xf8\x00\xf8\x00p\x88\x8cp'),
                            bytearray(b'\xfe\x01\xfd\x03x\x84\xc6>\xbe>N\x0e \x00\x1f\x10\xc3\xc2ED\xfc\xff\xfe\xf9>\xc1\x0eq\x00?\x10\x1f'),
                            bytearray(b'4\xf4\x88\xf8p80\x1cp\x1cd \xfc \x000\xf0\x08\xf8\x048\xc4\x1c\xe2\x1c\xe2 \xfe \xfc\xc0\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=350),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'p@???-.+LK\\_X_P_@\x7f??-?6;t{`\x7f`\x7f`\x7f'),
                            bytearray(b'\xfc\x0c\xf8\x98\xc8\x98\xf0\xb0X\xb0\x08\xe8\x10\xe0\x00\xf0\x1c\xe0\xb8\xc4\xb8\xc4p\x88p\x88(\xd8\x08\xf8\x08\xf8'),
                            bytearray(b'(/47\x10\x10\x10\x16\x1f\x1c\x0c\x00\x07\x00\x00\x000?8?\x1f\x1f\x19\x1f\x1a\x1d\x07\x08\x00\x07\x00\x00'),
                            bytearray(b'\x10\xf0N\xdcKx\x8b\xf8\x7fx\xbf\xb1\x1e\x0688\x08\xf8$\xfe\x84\xff\x04\xff\x84\xfb\xc1\xfff~88'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=106),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x06\x03\x04\x0c\x003\x03G\x07\x00\x00\x00\x00\x01\x01\x06\x06\x07\x06\x00\x0f\x03<\x07x'),
                            bytearray(b'\x00\x00\x00\x00\x00\xf0\xde!\x9ea\x1f\x00\xe7\xe8\xfc\xf2\x00\x00\x00\x00\xf0\xf0ss\xf1q\x19\xf9\xed\x1d\xf7\x08'),
                            bytearray(b'\x0f\x0f\x8f\x0f\xbf?\x1f\x1f\x83\x03\x9f\x1f|?_\x1f\x0fp\x0f\xf0?\xc0\x1f\xe0\x03\xfc\x1f\xe0?@\x1f`'),
                            bytearray(b'\x94\xf3\x90\xf3\x8d\xfb\x01\xf3\x0c\xf6\x00\xe6J\xce\xa8\x8c\xf3\x0c\xf3\x0c\xfb\x04\xf3\x0c\xf6\t\xe6\x19\xde \xbcB'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=90),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'p@???-.+LK\\_X_P_@\x7f??-?6;t{`\x7f`\x7f`\x7f'),
                            bytearray(b'\xfc\x0c\xf8\x98\xc8\x98\xf0\xb0X\xb0\x08\xe8\x10\xe0\x00\xf0\x1c\xe0\xb8\xc4\xb8\xc4p\x88p\x88(\xd8\x08\xf8\x08\xf8'),
                            bytearray(b'(/47\x10\x10\x10\x16\x1f\x1c\x0c\x00\x07\x00\x00\x000?8?\x1f\x1f\x19\x1f\x1a\x1d\x07\x08\x00\x07\x00\x00'),
                            bytearray(b'\x10\xf0N\xdcKx\x8b\xf8\x7fx\xbf\xb1\x1e\x0688\x08\xf8$\xfe\x84\xff\x04\xff\x84\xfb\xc1\xfff~88'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x06\x03\x04\x0c\x003\x03G\x07\x00\x00\x00\x00\x01\x01\x06\x06\x07\x06\x00\x0f\x03<\x07x'),
                            bytearray(b'\x00\x00\x00\x00\x00\xf0\xde!\x9ea\x1f\x00\xe7\xe8\xfc\xf2\x00\x00\x00\x00\xf0\xf0ss\xf1q\x19\xf9\xed\x1d\xf7\x08'),
                            bytearray(b'\x0f\x0f\x8f\x0f\xbf?\x1f\x1f\x83\x03\x9f\x1f|?_\x1f\x0fp\x0f\xf0?\xc0\x1f\xe0\x03\xfc\x1f\xe0?@\x1f`'),
                            bytearray(b'\x94\xf3\x90\xf3\x8d\xfb\x01\xf3\x0c\xf6\x00\xe6J\xce\xa8\x8c\xf3\x0c\xf3\x0c\xfb\x04\xf3\x0c\xf6\t\xe6\x19\xde \xbcB'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=92),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=124),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'|\x008\x808\xf8@\xc0@@\x00\x00\x00\x00\x00\x00\x80\xfc@\xf88\xf8 \xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0b\x0b\x08\x0b\x00\x03\x05\x05\x03\x03\x00\x00\x00\x00\x00\x00\x0c\x0f\x0c\x0f\x04\x07\x06\x07\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfd\x00\xff\x00\xff\x00\xff\xff\xff\xfe\xfe\x00\x00\x00\x00\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\xe0\xfe\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00@\x00 \x00\xc0\xc0\xf0\xe0\xf0\xe0\xd0\xc0 \xc0\x00\x00\x00\xc0\x00\xe0\xc0 \xe0\x10\xe0\x10\xc00\x80 '),
                            None,
                            bytearray(b'`\xc0`\x80\xc0\x00p\x00\xf8\x00\xf8\x80\xec\x80\xfc\x80\x00 @ \xc0\x00\xc00\x90h\xb8\xc0\xb8\xc4\xb8\xc4'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=98),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x03\x02\x02\x00\x03\x02\x01\x01\x03\x01\x00\x00\x00\x00\x00\x01\x02\x03\x02\x01\x00\x01\x03\x01\x01\x03'),
                            bytearray(b'\x1f\x00\xc0\x00\x80\x00\x03\x03||\xf1\xffc\x7f\xdf\x1f\x00\x1f\x00\xff\x00\xff\x03\xfc|\x83\xff\x00\x7f\x80\x1f\xe0'),
                            bytearray(b'\x03\x01\x07\x02\x0f\x03\x1b\x01\x1e\x04\x1d\x1d\x19\x19\x08\x08\x01\x03\x02\x07\x03\x0f\x07\x19\x05\x1f\x1e\x1f\x1e\x1f\x0f\x0f'),
                            bytearray(b'\xe3\x88\xf7\x80\xff\xfd\x98\x1b\xaf/\xb8\xb6\x0f>\x07\xfe\x89\xf6\x8d\xf2\xfc\xfe\xfc\x18\xd0\x00\x8fpF\xf9\x06\xf9'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=98),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'|\x008\x808\xf8@\xc0@@\x00\x00\x00\x00\x00\x00\x80\xfc@\xf88\xf8 \xe0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0b\x0b\x08\x0b\x00\x03\x05\x05\x03\x03\x00\x00\x00\x00\x00\x00\x0c\x0f\x0c\x0f\x04\x07\x06\x07\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfd\x00\xff\x00\xff\x00\xff\xff\xff\xfe\xfe\x00\x00\x00\x00\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\xe0\xfe\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00@\x00 \x00\xc0\xc0\xf0\xe0\xf0\xe0\xd0\xc0 \xc0\x00\x00\x00\xc0\x00\xe0\xc0 \xe0\x10\xe0\x10\xc00\x80 '),
                            None,
                            bytearray(b'`\xc0`\x80\xc0\x00p\x00\xf8\x00\xf8\x80\xec\x80\xfc\x80\x00 @ \xc0\x00\xc00\x90h\xb8\xc0\xb8\xc4\xb8\xc4'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x03\x02\x02\x00\x03\x02\x01\x01\x03\x01\x00\x00\x00\x00\x00\x01\x02\x03\x02\x01\x00\x01\x03\x01\x01\x03'),
                            bytearray(b'\x1f\x00\xc0\x00\x80\x00\x03\x03||\xf1\xffc\x7f\xdf\x1f\x00\x1f\x00\xff\x00\xff\x03\xfc|\x83\xff\x00\x7f\x80\x1f\xe0'),
                            bytearray(b'\x03\x01\x07\x02\x0f\x03\x1b\x01\x1e\x04\x1d\x1d\x19\x19\x08\x08\x01\x03\x02\x07\x03\x0f\x07\x19\x05\x1f\x1e\x1f\x1e\x1f\x0f\x0f'),
                            bytearray(b'\xe3\x88\xf7\x80\xff\xfd\x98\x1b\xaf/\xb8\xb6\x0f>\x07\xfe\x89\xf6\x8d\xf2\xfc\xfe\xfc\x18\xd0\x00\x8fpF\xf9\x06\xf9'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'."MMOC\x04\x07\x10\x1fP_\x00\x0f&\';7~sp\x7fx\x7f`\x7f`\x7f0?8?'),
                            bytearray(b"@ \xb0\xb6\xa6\xb9T\xdb\x04\xe3\n\xfe\x17\xf4\xcf\xdc\xa0\xd06\xce?\xc7\x1b\xe3\x07\xff\x06\xfe\x0c\xff\'\xfc"),
                            bytearray(b'\x16\x16\x13\x13\x0f\x08\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x1d\x1f\x08\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'I\xfc\t|;9\x9e\x82||\x00\x00\x00\x00\x00\x00\x03\xfc\x82\xfd\xc5\xff\xe2\xfe||\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x00\x0c\x00;\x03g\x07O\x0f\x9f\x1f\x00\x00\x00\x00\x00\x03\x00\x0f\x03<\x07x\x0fp\x1f\xe0'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xf0\xe0\xf8\xf0\xf0\xf0\x9c\xf8\x88\xf8\x00\x00\x00\x00\x00\xe0\xe0\x10\xf0\x08\xf0\x08\xf8\x04\xf8\x04'),
                            bytearray(b'\xbf?\x8f\x0f\x9e\x1f\xd0\x1f\\_~N\x7fx?\x1f?\xc0\x0f\xf0\x1f\xe0\x1f\xe0_`Nqx\x7f\x1f?'),
                            bytearray(b'\x88\xf8\x0c\xf8\x14\xf0,\xec\xfc\xdc\xe8\x00\xe8\x88\xc8\x00\xf8\x04\xf8\x04\xf4\x08\xe4\x14\xc4$8\xc0\x90\xe08\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8\x00\x00\x00\x00\xc0\xc0\xfe\xfe\xff\xff\xff\xff\xfe\xfe\xf8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x0c\x0c\x12\x1e\x00\x0874;H\x7f\x08|\x10\xf0\x0c\x0c\x1e\x1e\x06\x06???\x0f\x7f\x07|\x04\xf0\x08'),
                            None,
                            bytearray(b'@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=111),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x04\x1c\x02\x1e"\x1e \x1c7\x00?"\x1f\x1f\x00\x00\x03\x1f\x01\x1f\x01?\x03?<\x03*7\x1f\x1f\x00\x00'),
                            bytearray(b'pp\xd0\xf0\x14\xf4\x16\xf2\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x88\xf8\x08\xf8\x0c\xfc\n\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x0f\x0f\x07\x07\x00\x00\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x10\x1f\x18\x1f\x1f\x1f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=108),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x0c\x0c\x12\x1e\x00\x0874;H\x7f\x08|\x10\xf0\x0c\x0c\x1e\x1e\x06\x06???\x0f\x7f\x07|\x04\xf0\x08'),
                            None,
                            bytearray(b'@\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc00\x80@\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x04\x1c\x02\x1e"\x1e \x1c7\x00?"\x1f\x1f\x00\x00\x03\x1f\x01\x1f\x01?\x03?<\x03*7\x1f\x1f\x00\x00'),
                            bytearray(b'pp\xd0\xf0\x14\xf4\x16\xf2\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x88\xf8\x08\xf8\x0c\xfc\n\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'1\x007\x17\x03\x03\x0f\x0f\x0e\x0f\x0f\x0f\x07\x07\x00\x00\x00?\x0f?\x1f\x1f\x10\x1f\x10\x1f\x10\x1f\x18\x1f\x1f\x1f'),
                            bytearray(b'\xe0h\xcc\xc4\xcc\xc0\x0c\xc08\xe0\x18\xf8\x88\xf8\xf0\xf0`\xf8\xc0\xfc\x00\xfc\x00\xfc\x04\xfc\x04\xfc\x04\xfc\x08\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=116),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0e\x00\x00\x00\x0c\x0f\r\x01\x02\x00\x00\x00\x00\x00\x00\x01\x02\r\x00\x0f\x0f\x00\x01\x0e\x00\x03\x00\x00'),
                            bytearray(b'`\x90P\xae\x1ea>\xc1>\xe0\xe0\xfc\x00\x00\x00\x00\xf0\xf0\xee\xeek\xeb\xe1!\xf2\x12\xfc\x1c\x00\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x00\x01\x00\r\x0c\x18\x1f\x00\x1f\x10\x1f\xc3O\xf0p\x04\x07\x0e\x0f\x12\x1f ?`\x7f`\x7f0\xff\x0f\xff'),
                            bytearray(b'\xf88\xf0\x00\x88\x00\xc8\xc0\xe8\xe0\xc0\xc0\xfc\xfc\x1c\x1c8\xf8\x08\xf8p\xf80\xf8\x10\xf8<\xfc\x00\xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0e\x00\x00\x00\x0c\x0f\r\x01\x02\x00\x00\x00\x00\x00\x00\x01\x02\r\x00\x0f\x0f\x00\x01\x0e\x00\x03\x00\x00'),
                            bytearray(b'`\x90P\xae\x1ea>\xc1>\xe0\xe0\xfc\x00\x00\x00\x00\xf0\xf0\xee\xeek\xeb\xe1!\xf2\x12\xfc\x1c\x00\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x00\x01\x00\r\x0c\x18\x1f\x00\x1f\x10\x1f\xc3O\xf0p\x04\x07\x0e\x0f\x12\x1f ?`\x7f`\x7f0\xff\x0f\xff'),
                            bytearray(b'\xf88\xf0\x00\x88\x00\xc8\xc0\xe8\xe0\xc0\xc0\xfc\xfc\x1c\x1c8\xf8\x08\xf8p\xf80\xf8\x10\xf8<\xfc\x00\xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00x@p\x10\xf0\xf0h`\xf0\x00\x00\x00\x00\x00\x00\x00@x\x90\xe8\xf0\x08`\x98\x00\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x03\x1c\x00  8?0?\x10\x1f\xc9O\xf0p#?#?\x1f?@\x7f@\x7f`\x7f0\xff\x0f\xff'),
                            bytearray(b'\xe0\xc0\xe0\x00\x00\x00\xc0\xc0`\xe0@\xc0\xfc\xfc\x1c\x1c\xc0\xfc\x00\xfc\xf0\xf08\xf8\x18\xf8<\xfc\x00\xfc\xe0\xfc'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=128),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'  \xe8`xptp\xb0?O\x10/\x10\x1f  P`\x98p\x88p\x8c?\xcf\x19y\x10000'),
                            bytearray(b'\x00\x008\x10\x10\x10x80\xb0\xa8 \x88\x00 \x80\x00\x10\x10(\x10(8@\xb0\xc8 \xd8\x80\xf8\x80\xe0'),
                            bytearray(b'\x0e\x11\x06\x19\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x1b\x1f\x1f\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x00\x01\x00\r\x0c\x18\x1f\x00\x1f\x10\x1f\xc3O\xf0p\x04\x07\x0e\x0f\x12\x1f ?`\x7f`\x7f0\xff\x0f\xff'),
                            bytearray(b'\xf88\xf0\x00\x88\x00\xc8\xc0\xe8\xe0\xc0\xc0\xfc\xfc\x1c\x1c8\xf8\x08\xf8p\xf80\xf8\x10\xf8<\xfc\x00\xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'  \xe8`xptp\xb0?O\x10/\x10\x1f  P`\x98p\x88p\x8c?\xcf\x19y\x10000'),
                            bytearray(b'\x00\x008\x10\x10\x10x80\xb0\xa8 \x88\x00 \x80\x00\x10\x10(\x10(8@\xb0\xc8 \xd8\x80\xf8\x80\xe0'),
                            bytearray(b'\x0e\x11\x06\x19\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x1b\x1f\x1f\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x00\x01\x00\r\x0c\x18\x1f\x00\x1f\x10\x1f\xc3O\xf0p\x04\x07\x0e\x0f\x12\x1f ?`\x7f`\x7f0\xff\x0f\xff'),
                            bytearray(b'\xf88\xf0\x00\x88\x00\xc8\xc0\xe8\xe0\xc0\xc0\xfc\xfc\x1c\x1c8\xf8\x08\xf8p\xf80\xf8\x10\xf8<\xfc\x00\xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'  \xe8`xptp\xb0?O\x10/\x10\x1f  P`\x98p\x88p\x8c?\xcf\x19y\x10000'),
                            bytearray(b'\x00\x008\x10\x10\x10x80\xb0\xa8 \x88\x00 \x80\x00\x10\x10(\x10(8@\xb0\xc8 \xd8\x80\xf8\x80\xe0'),
                            bytearray(b'\x0e\x11\x06\x19\x00\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1b\x1b\x1f\x1f\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x01\x00\x04\x00\t\x01\x13\x037\'7\'vg\x00\x00\x01\x00\x00\x07\x01\x0e\x03\x1c\'8\'8gx"),
                            bytearray(b'\x00\x00\xc0\x00\xe0\xe0\xc0\xe0\xc0\xf0A\xf0k\xfa\\\xdc\x00\x00\xc0\x00\xc0\x00\xe0\x00\xf0\x10\xe1\x0e\xeb\x04\xdc"'),
                            bytearray(b'\xe6\x07\xad\x0f\x8e\x0e\x84\x04\xc1\x81~C\x1d\x1d\x1e\x0c\x07\xf8\x0f\xf0\x0e\xf1\x04\xfb\x82\xfc@|\x1e\x1c\r\x1e'),
                            bytearray(b'\xcc\xfc\x80\xbb0\xbf\xc3{\xe6:\xe6\xba\x04\xf0\xc8\xc0\xff\x00\xbc@\xcc\x0c\x04\x80\x86B\x06B\x0c\x008\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x00\x01\x00\r\x0c\x18\x1f\x00\x1f\x10\x1f\xc3O\xf0p\x04\x07\x0e\x0f\x12\x1f ?`\x7f`\x7f0\xff\x0f\xff'),
                            bytearray(b'\xf88\xf0\x00\x88\x00\xc8\xc0\xe8\xe0\xc0\xc0\xfc\xfc\x1c\x1c8\xf8\x08\xf8p\xf80\xf8\x10\xf8<\xfc\x00\xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'80pp\xf0pxp\xe8\xe0\xe0\xe0\xd0\xc0 \x000Hp\x08p\x88p\x88\xe0\x18\xe0\x10\xc00\x00\xe0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbf\x07\x99\x00\x07\x07<?0?0?\xccO\xf0pG\xfff\xff\xf8\xff@\x7f@\x7f@\x7f0\xff\x0f\xff'),
                            bytearray(b'\xc0\xc0\xc0\x00\x80\x80`\xe0 \xe00\xf0\\\xdc\x1c\x1c\xc0\xc0 \xe0p\xf0\x18\xf8\x18\xf8\x0c\xfc \xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'80pp\xf0pxp\xe8\xe0\xe0\xe0\xd0\xc0 \x000Hp\x08p\x88p\x88\xe0\x18\xe0\x10\xc00\x00\xe0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbf\x07\x99\x00\x07\x07<?0?0?\xccO\xf0pG\xfff\xff\xf8\xff@\x7f@\x7f@\x7f0\xff\x0f\xff'),
                            bytearray(b'\xc0\xc0\xc0\x00\x80\x80`\xe0 \xe00\xf0\\\xdc\x1c\x1c\xc0\xc0 \xe0p\xf0\x18\xf8\x18\xf8\x0c\xfc \xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'80pp\xf0pxp\xe8\xe0\xe0\xe0\xd0\xc0 \x000Hp\x08p\x88p\x88\xe0\x18\xe0\x10\xc00\x00\xe0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbf\x07\x99\x00\x07\x07<?0?0?\xccO\xf0pG\xfff\xff\xf8\xff@\x7f@\x7f@\x7f0\xff\x0f\xff'),
                            bytearray(b'\xc0\xc0\xc0\x00\x80\x80`\xe0 \xe00\xf0\\\xdc\x1c\x1c\xc0\xc0 \xe0p\xf0\x18\xf8\x18\xf8\x0c\xfc \xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00x@p\x10\xf0\xf0h`\xf0\x00\x00\x00\x00\x00\x00\x00@x\x90\xe8\xf0\x08`\x98\x00\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbf\x07\x99\x00\x07\x07<?0?0?\xccO\xf0pG\xfff\xff\xf8\xff@\x7f@\x7f@\x7f0\xff\x0f\xff'),
                            bytearray(b'\xc0\xc0\xc0\x00\x80\x80`\xe0 \xe00\xf0\\\xdc\x1c\x1c\xc0\xc0 \xe0p\xf0\x18\xf8\x18\xf8\x0c\xfc \xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\x10lx\x86~\x88{\x081\x00\x0c\x00\x03\x00\x0c\x0c||\x9e\x9e\x98\x96\x18\x17\x00?\x00\x0f\x00\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=114),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00x@p\x10\xf0\xf0h`\xf0\x00\x00\x00\x00\x00\x00\x00@x\x90\xe8\xf0\x08`\x98\x00\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbf\x07\x99\x00\x07\x07<?0?0?\xccO\xf0pG\xfff\xff\xf8\xff@\x7f@\x7f@\x7f0\xff\x0f\xff'),
                            bytearray(b'\xc0\xc0\xc0\x00\x80\x80`\xe0 \xe00\xf0\\\xdc\x1c\x1c\xc0\xc0 \xe0p\xf0\x18\xf8\x18\xf8\x0c\xfc \xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\x10lx\x86~\x88{\x081\x00\x0c\x00\x03\x00\x0c\x0c||\x9e\x9e\x98\x96\x18\x17\x00?\x00\x0f\x00\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=115),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x07\x07\x1f\x1f>?x\x7f\x00\x00\x00\x00\x00\x00\x01\x06\x07\x18\x1f ?@\x7f\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xc0\xf0\xe0\xe0\xe08\xf02\xf0\x00\x00\x00\x00\x00\x00\xc0 \xe0\x10\xe0\x1c\xf0\x0c\xf2\x0c'),
                            bytearray(b'x\x7fx\x7f\x18\x1f\x00\x076?0?<?\x1f\x1f\x7f\x80\x7f\x80\x1f\xe0\x07\xf8?@?@?\x00\x1f '),
                            bytearray(b'\x1e\xf8\x0e\xf8\x0c\xfc\x04\xf4\x1c\xf4\x14\xc8\xb4\x98\xf0 \xfa\x04\xfa\x04\xfc\x04\xf4\x0c\xfc\x04\xd4 \x84`8\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00x@p\x10\xf0\xf0h`\xf0\x00\x00\x00\x00\x00\x00\x00@x\x90\xe8\xf0\x08`\x98\x00\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xbf\x07\x99\x00\x07\x07<?0?0?\xccO\xf0pG\xfff\xff\xf8\xff@\x7f@\x7f@\x7f0\xff\x0f\xff'),
                            bytearray(b'\xc0\xc0\xc0\x00\x80\x80`\xe0 \xe00\xf0\\\xdc\x1c\x1c\xc0\xc0 \xe0p\xf0\x18\xf8\x18\xf8\x0c\xfc \xfc\xe0\xfc'),
                            bytearray(b'\xd8\x00\xff\x8e\x7f~\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00\xf5\r\xae\xdf~\x7f\x1f\x1f\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'.:\x0e\xe2\xfe\x06\xfc\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xc2\xfe\x12\xfe\xf6\x0e\xec\x1c\xf0\xf0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\x10lx\x86~\x88{\x081\x00\x0c\x00\x03\x00\x0c\x0c||\x9e\x9e\x98\x96\x18\x17\x00?\x00\x0f\x00\x03'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=116),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=10, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=8, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=4, mold_id=23),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL644_MARIO_ATTACK_UP_RIGHT,
    palette_offset=0,
    unknown_num=0
)
