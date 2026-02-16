# SPR0433_MUKUMUKU

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL144_MUKUMUKU
sprite = CompleteSprite(
    animation=AnimationPack(47, length=776, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x10\x88\x88\xbe\x8e\xb1\x81\xa0\x80````\x00\x00\xe0\xf0x\xf8~\xfeq\xf1`\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\r\xf4\x9b\xac@[\x17\x1e3\x05\x13\x0e)0\x11\n\x1c\xe3H\xf7$\x7f\x01\x1f\x12.\x18&2\x08\x00\x18'),
                            None,
                            bytearray(b'\x01\x02\x1f\x1c=>mn\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1888ll\x04\x04\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x9bn\xe7\x7f\xb0/\xa4[\xcd;{\x9frr@@9\x07p\x0f _\x00?\x00\x07\x00\x07BB@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00@\x00\xc0@`\x80\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\xc0@\x80\x00\xe0'),
                            bytearray(b"\x97w\'\xe7\xb3\x83\xc5\x07\xf6\xfb\x1e\xe5\xd9\'\xf6\n\x08\xff\x18\xff|\xf3\xf8\xc7\x02\r\x0c\x13\x1c\x039\x07"),
                            bytearray(b'`\x80\xa0\xc0\x90\xe0\x90\xa0\x10 \xa0\xb0 0\x90\x10\x00\xe0\x00\xe0\x00\xf0@\xf0\xc0\xf0@\xf0\xc0\xf0\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01\x07\x01\x1f\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x04\x07\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0 \xf8 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\x18'),
                            bytearray(b'?\x12?`?$\x7f\xc0\xff\x00\xfe\xb0\xde\xe0\xbfb\x1f ?@wH?\xc0\x7f\x80\xbfA\x8fq\x0e\xf1'),
                            bytearray(b'\xf84\xfe\x03\xfaG\xf5\x8b\xce01\x0e\xec\x9f\xdf?\xf8\x04\xfe\x01x\x87\xf9\x06\xf0\x0f\x80\xff\x80\xff\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"o\xa0|\xb3\xfc\x13\xf6\x19n\x9b~\x85\xd9\'\xf6\n _0\x0f\x10\x0f\x10\x0f\n\x05\x0c\x13\x1c\x039\x07"),
                            bytearray(b'\xc0\x00`\x80 \xc0\xa0\xc0\x000\xa0\xb0 0\x90\x10\x00\xc0\x00\xe0\x00\xe0\x00\xe0\xc0\xf0@\xf0\xc0\xf0\xe0\xf0'),
                            bytearray(b'\x9bn\xe7\x7f\xb0/\xa4[\xcd;{\x9frr@@9\x07p\x0f _\x00?\x00\x07\x00\x07BB@@'),
                            bytearray(b'\x10\x10\x88\x88\xbe\x8e\xb1\x81\xa0\x80````\x00\x00\xe0\xf0x\xf8~\xfeq\xf1`\xe0\xe0\xe0``\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0f\xff:;\x0c\x01\x1c\x110\x05\x12\x0f*3\x11\n\x00\xfe\x04<\x02\x0c\x1a\x04\x12,\x18$0\x08\x00\x18'),
                            None,
                            bytearray(b'\x01\x02\x1f\x1c=>mn\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1888ll\x04\x04\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00@\x80\x80@\xc0\x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\x00\xc0\xc0\x00\xe0\x10'),
                            None,
                            bytearray(b"\xf8@\xfc\x08\xde\xa0\xcfp\'\xc9\xef\r\xf9\x01\xde\x00\xf0\x08\xd8$\x10\xee\\\xa3\t\xf6\r\xf2\x01\xfe\x00\xff"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x80@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00;F\xff\x0e\xffH\xff\x81\x00\x00\x00\x00\x00\x00\x00\x01\x03|\x7f\x80\x7f\x80\xfd\x02'),
                            bytearray(b'\x0f\x02\x0f\x0c\x07\t\n\x05\x0e\x0f\x0f\x03\x04\x0c\x05\x06\x03\x0c\x07\x08\x07\x08\x07\x08\x0f\x00\x03\x0c\x00\x0f\x00\x07'),
                            bytearray(b'\xff \xffP\xff\x01\xfbG\xff|\xff\xe0|\x03\xf2\x0f\xef\x10\x7f\x80\xff\xc0\xbf\xc0|\x83\xe0\x1f\x00\xff\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=104),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x10\x88\x88\xbe\x8e\xb1\x81\xa0\x80````\x00\x00\xe0\xf0x\xf8~\xfeq\xf1`\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x02\x1f\x1c=>mn\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1888ll\x04\x04\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x9bn\xe7\x7f\xb0/\xa4[\xcd;{\x9frr@@9\x07p\x0f _\x00?\x00\x07\x00\x07BB@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@`\xc0\xe0\xe0 \xe0 \xe0\xa0\x80`@``\xa0@ \xc0 \x80`\xc0 \xc0 \xc0 \x00\xe0@\xe0'),
                            None,
                            bytearray(b'`\xa0 \xe0@\xc0\xe0\xe0\xe0 \xe0 \xe0 \xa0 @\xe0\x00\xe0 \xe0\x00\xe0\xc0\xe0\xc0\xe0\xc0\xe0\xc0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x03\x01\x00\x03\x02\x01\x02\x03\x00\x03\x02\x02\x03\x03\x00\x01\x02\x01\x02\x00\x03\x01\x02\x01\x02\x03\x00\x02\x01\x01\x03'),
                            bytearray(b'<B\xffQ\xff\x08\xffA\xff\x98\xffA\xfe\x81\xfc\x1e\x00~w\x88\xff\x00\xff\x00\xbeA\xef\x10\xff\x00~\x81'),
                            bytearray(b'\x06\x00\x0c\x01\x0f\x05\x1d\x160\x07\x12\x0f-6\x15\x0e\x03\x05\x05\n\r\x02\x1c\x03\x10/\x18$0\x0c\x00\x1c'),
                            bytearray(b'\xea\x82\x80}h\x91\xd5|)\xf7\x7f\xc0&\xfe\xf1\x0f\xe2\x1d\xe0\x1f\xec\x1ft\x8b(\xdf?\xff\x01\x1f8\x07'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x10\x88\x88\xbe\x8e\xb1\x81\xa0\x80````\x00\x00\xe0\xf0x\xf8~\xfeq\xf1`\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x02\x1f\x1c=>mn\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x18\x1888ll\x04\x04\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x9bn\xe7\x7f\xb0/\xa4[\xcd;{\x9frr@@9\x07p\x0f _\x00?\x00\x07\x00\x07BB@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'@`\xc0\xe0\xe0 \xe0 \xe0\xa0\x80`@``\xa0@ \xc0 \x80`\xc0 \xc0 \xc0 \x00\xe0@\xe0'),
                            None,
                            bytearray(b'`\xa0 \xe0@\xc0\xe0\xe0\xe0 \xe0 \xe0 \xa0 @\xe0\x00\xe0 \xe0\x00\xe0\xc0\xe0\xc0\xe0\xc0\xe0\xc0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x03\x01\x00\x03\x02\x01\x02\x03\x00\x03\x02\x02\x03\x03\x00\x01\x02\x01\x02\x00\x03\x01\x02\x01\x02\x03\x00\x02\x01\x01\x03'),
                            bytearray(b'<B\xffQ\xff\x08\xffA\xff\x98\xffA\xfe\x81\xfc\x1e\x00~w\x88\xff\x00\xff\x00\xbeA\xef\x10\xff\x00~\x81'),
                            bytearray(b'\x06\x00\x0c\x01\x0f\x05\x1d\x160\x07\x12\x0f-6\x15\x0e\x03\x05\x05\n\r\x02\x1c\x03\x10/\x18$0\x0c\x00\x1c'),
                            bytearray(b'\xe2\x8a\xa0A|\x89\xd5t)\xd7\x7f\xc0&\xfe\xf1\x0f\xe2\x1d\xfc\x1f\xe0\x1f|\x8b\x08\xff?\xff\x01\x1f8\x07'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe8\x00\xfc\xf8\xbe~1\xc1\xa0\x80````\x00\x00\xfc\xfc\x04\xfc\x0e\xfe1\xf1`\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x02\x1f\x1f?=om\x06\x07\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x1c?<mn\x04\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"O\xd8\xb3\xf3\xb9x\xd98\t\xf9\x99\xf9bb@@\'\x9f\x8c\x03\x06\x01\x06\x01\x06\x01\x06\x01RB@@"),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x88L\xf8<\xfc\x04\xfc$\xfc\x14\x00\x00\x00\x00\x00\x00\x08\xc4\xf8\x04\xf0\x0c\xf8\x04\xd8$'),
                            None,
                            bytearray(b'\xf0,\xc0,\x84\xd4LL\x04\xbc\x088\xb8\x988\xe0\xf8\x04\xe0\x1c\xc8<P\xbc\x00\xfc\x84\xfc\x84|\x1c\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02'),
                            bytearray(b"\x00\x00\x00\x00\x00\x00\'h?\n\x7fA\xbfh\xdf3\x00\x00\x00\x00\x00\x00 O.Q\x1f`\xbf@\x97h"),
                            bytearray(b'\x01\x00\x02\x01\x00\x02\x01\x03\x03\x03\x01\x01\x01\x01\x00\x01\x01\x02\x00\x03\x01\x03\x00\x03\x00\x03\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x9f\xe8?\x90\x7fcMp\xa8\xdf\xad\xd2\xda\xefe\xfe\x9db_\xe0\x8f\xf0\x8c\xf3\x1c\xe3\x1d\xe3\x0e\xf1\x05\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x0f=sj\x16\xf5\x1c\xea8\xf2\x9e\x00`\x00\x00\x00\x0f0\x0fq\x0f\xf3\x0f\xe7\x1f\x80~\x00`'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x04\x0f\x17\x18?";&%\x1c\x00\x00\x00\x00\x00\x00\x07\x08\x1e\x01>\x018\x07\x10-\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x02\x1d\x1e=>on\x05\x05\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c<<ll\x06\x04\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80  \x80\xa0\xc0\xe0\xa0\xa0\xa0\xa0\xa0\xa0\x90\x90`\xe0\xc0\xe0@\xe0\x00\xe0@\xe0@\xe0@\xe0`\xf0'),
                            bytearray(b'\xfd\x07\xfd\x07\xfd\x07\xfd\x03\xef\x1bz\x9err@@\x04\x03\x04\x03\x04\x03\x00\x07\x00\x07\x01\x07BB@@'),
                            bytearray(b'\x90\x90\x88\x88\xbe\x8e1\x01`\x00\xe0```\x00\x00`\xf0x\xf8~\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x00\x01\x02'),
                            None,
                            bytearray(b'\x02\x01\x02\x03\x02\x03\x03\x02\x03\x02\x03\x02\x03\x02\x01\x02\x01\x02\x03\x00\x03\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'L\xbc\xee\x1e\xe5\x1f\xe5\x1f\xf3\r\xff\x05\xff\x05\xfd\x07\x83\x00\x01\x00\x00\x03\x04\x03\x04\x03\x04\x03\x04\x03\x04\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x06\x03\x1f\x08\x0f\xf5?\xc0\x00\x00\x00\x00\x00\x00\x00\x01\x03\x04\x0f\x10\xfd\x02\x9f`'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x80 \xd0\xe8P\xacx\x00\xfe\x00\x00\x00\x00\x00\x80\x80@\xc00\xd0(\xf8\x04\xfc\x02'),
                            bytearray(b"\x7f\x00\xfdS\xfb\xc5\x1c\xe3\xd9\'\xa7\x7f\xbf|P\xff?@x\x87\xf9\x06\xff\x00\xff\x00\xff\x00\xfc\x03\xc0\x0f"),
                            bytearray(b'\xe3\x1d\xc3\xbd\x89\xeb\xf5\xeb\xd6\xc0F&\x98x0\xf0\xfc\x030\xcf\xe4\x1f\xe4\x1f\xce>\x18\xfe\x00\xf8\x00\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'44\xb8\xfc$\xfc4\xcc\xf8\x08\x9cx\xf0\x10\xd8\xf0\x08<\x00|\x00|\x00|\x04|t\x0cx\x08\xf8\x08'),
                            None,
                            bytearray(b'\xf0\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa8X\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=122),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x1c\x14\x0e\x12\x07\x1d\x0b\x0e\x06\x04\x00\x02\x00\x02\x00\x00\x1c\x00\x1e\x00\x07\x18\x03\x0c\x00\x06\x00\x02\x00\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x02\x1d\x1e=>on\x05\x05\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c<<ll\x06\x04\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80  \x80\xa0\xc0\xe0\xa0\xa0\xa0\xa0\xa0\xa0\x90\x90`\xe0\xc0\xe0@\xe0\x00\xe0@\xe0@\xe0@\xe0`\xf0'),
                            bytearray(b'\xfd\x07\xfd\x07\xfd\x07\xfd\x03\xef\x1bz\x9err@@\x04\x03\x04\x03\x04\x03\x00\x07\x00\x07\x01\x07BB@@'),
                            bytearray(b'\x90\x90\x88\x88\xbe\x8e1\x01`\x00\xe0```\x00\x00`\xf0x\xf8~\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x00\x01\x02'),
                            None,
                            bytearray(b'\x02\x01\x02\x03\x02\x03\x03\x02\x03\x02\x03\x02\x03\x02\x01\x02\x01\x02\x03\x00\x03\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'L\xbc\xee\x1e\xe5\x1f\xe5\x1f\xf3\r\xff\x05\xff\x05\xfd\x07\x83\x00\x01\x00\x00\x03\x04\x03\x04\x03\x04\x03\x04\x03\x04\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x06\x03\x1f\x08\x0f\xf5?\xc0\x00\x00\x00\x00\x00\x00\x00\x01\x03\x04\x0f\x10\xfd\x02\x9f`'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x80 \xd0\xe8P\xacx\x00\xfe\x00\x00\x00\x00\x00\x80\x80@\xc00\xd0(\xf8\x04\xfc\x02'),
                            bytearray(b"\x7f\x00\xfdS\xfb\xc5\x1c\xe3\xd9\'\xa7\x7f\xbf|P\xff?@x\x87\xf9\x06\xff\x00\xff\x00\xff\x00\xfc\x03\xc0\x0f"),
                            bytearray(b'\xe3\x1d\xc3\xbd\x89\xeb\xf5\xeb\xd6\xc0F&\x98x0\xf0\xfc\x030\xcf\xe4\x1f\xe4\x1f\xce>\x18\xfe\x00\xf8\x00\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x88\xf4\x0c\xe5\x15\x17s\x17\x13\t\x08\x06\x00\x00\x00p\x08\xf3\x0fJ\xbf\x0c\x7f\x0c\x1f\x07\x0f\x06\x06\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x03\x03\x03\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x02\x01\x02\x01\x00\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x02\x1d\x1e=>on\x05\x05\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1c<<ll\x06\x04\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80  \x80\xa0\xc0\xe0\xa0\xa0\xa0\xa0\xa0\xa0\x90\x90`\xe0\xc0\xe0@\xe0\x00\xe0@\xe0@\xe0@\xe0`\xf0'),
                            bytearray(b'\xfd\x07\xfd\x07\xfd\x07\xfd\x03\xef\x1bz\x9err@@\x04\x03\x04\x03\x04\x03\x00\x07\x00\x07\x01\x07BB@@'),
                            bytearray(b'\x90\x90\x88\x88\xbe\x8e1\x01`\x00\xe0```\x00\x00`\xf0x\xf8~\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x01\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x00\x01\x02'),
                            None,
                            bytearray(b'\x02\x01\x02\x03\x02\x03\x03\x02\x03\x02\x03\x02\x03\x02\x01\x02\x01\x02\x03\x00\x03\x00\x02\x00\x02\x00\x02\x00\x02\x00\x00\x00'),
                            bytearray(b'L\xbc\xee\x1e\xe5\x1f\xe5\x1f\xf3\r\xff\x05\xff\x05\xfd\x07\x83\x00\x01\x00\x00\x03\x04\x03\x04\x03\x04\x03\x04\x03\x04\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x06\x03\x1f\x08\x0f\xf5?\xc0\x00\x00\x00\x00\x00\x00\x00\x01\x03\x04\x0f\x10\xfd\x02\x9f`'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x80 \xd0\xe8P\xacx\x00\xfe\x00\x00\x00\x00\x00\x80\x80@\xc00\xd0(\xf8\x04\xfc\x02'),
                            bytearray(b"\x7f\x00\xfdS\xfb\xc5\x1c\xe3\xd9\'\xa7\x7f\xbf|P\xff?@x\x87\xf9\x06\xff\x00\xff\x00\xff\x00\xfc\x03\xc0\x0f"),
                            bytearray(b'\xe3\x1d\xc3\xbd\x89\xeb\xf5\xeb\xd6\xc0F&\x98x0\xf0\xfc\x030\xcf\xe4\x1f\xe4\x1f\xce>\x18\xfe\x00\xf8\x00\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'p\x10h\x08~\x0e\xf1A\xe0`\xe0\xe0``\x00\x00\xe0\xf0\xf8\xf8\xfe\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x06\x19\x198<ml\x06\x06\x01\x01\x00\x00\x00\x00\x01\x07\x18\x1f8?mn\x04\x07\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'CC\xc5\xc7a\x7f\xadsb\xd6\xd5\xe4sq@@\xbc\xc38\xc7\x00\xff\xb0O\x11\xef\x03\xffO\x7f@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80\x00\xc0\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xc0\x00\xe0'),
                            None,
                            bytearray(b'@` 0\xa00\xa00\xd0\x10\xd0\x10\xd0\x10\xf0\x10\x80\xe0\xc0\xf0\xc0\xf0\xc0\xf0\xe0\xf0\xe0\xf0\xe0\xf0\xe0\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x1d\x1e\x1f\x1c?\x00?\x10?\t?\x00/\x00\x00\x00\x18\x07\x1e\x01\x0e1\x17(\x1d"\x1d"\x1f0'),
                            bytearray(b'\x00\x00\xe0\xd8\xbev\xde7\xdd\x16\x90?\x97/\xc7\x0f\x00\x00\xc08v\x88\xf0\x0f\xd0/\x90o\xa0_\xc0?'),
                            bytearray(b"/\x00?\x026\x1f\x168\x18\x01\x0c\x15\x1e\x1f\x07\x07\x1f0\x0f0\x1f \x18\'\x06\x1f\x02\x1f\x02\x1f\x00\x07"),
                            bytearray(b'\x86N5\x8c\x0f\xbcK8\x9fxq\xf0\x00\x80\x80\x80\xf1?\xb3\x7f\x83\x7f\x07\xff\x07\xff\x0f\xff\x7f\xf3\x7f\xe3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'P\x10\x08\x08\xbe\x8e\xb1\x81\xa0\x80````\x00\x00\xe0\xf0\xf8\xf8~\xfeq\xf1`\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0c\r\x04\x05\x02\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x02\x0c\x02\x04\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x01\x01\x1e\x1f>?no\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1e<<ll\x06\x06\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfd\x0b\xfd\x0b\xfd\x0b\xfd\x0b\xed\x1b{\x9frr@@\x08\x07\x08\x07\x08\x07\x08\x07\x00\x07\x00\x07BB@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x80\x00\x80\x00\xc0\x00@\x80\x80\xe0\x80\xe0@`\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\xe0\x00\xe0\x80\xe0'),
                            bytearray(b'^\xb3i\xb9\xf5\r\xfe\x16\xf8\x04\xfe\n\xfd\x0b\xfd\x0b\x0c\x7f&\x1f\x02\x1f\x11\x0f\x03\x0f\t\x07\x08\x07\x08\x07'),
                            bytearray(b'\x80\xa0\xa0\xb0\xa0\xb0`0\xe00\xe00`0P\x10@\xe0@\xf0@\xf0\xc0\xf0\xc0\xf0\xc0\xf0\xc0\xf0\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x1f>\x7f\xc0?G\x7f\x80\xff\xa0?\xe0\x00\x00\x00\x00\x1e!\x7f\x80\xb8\xc7>\xc1?\xc0\x1f\xe0'),
                            bytearray(b'\x00\x00\x00\x00\x80`\xf0\xc8\xe9\x17\xfeG\xf8\x06\xf7\t\x00\x00\x00\x00\x00\xe0\xc08\x7f\x80|\x83\xf8\x06\xf9\x06'),
                            bytearray(b'o\xf0x\x1f_g\xf3<\xf4\xf7([*;\x1e\x1f\x7f\x80\x1f`\x07x\xc0?\xe8\x17\x04{\x049\x00\x1c'),
                            bytearray(b"\xeb\x1c\x19\xf6\xf8\xe7\xf6\x0f\'\xdf\xff\x83\xf0\x0e\xaco\xf8\x07\xf0\x0f\xe0\x1f\x00\xffp\x8f\xf0\x0f\x01\xff\x10\xff"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x03\x03\x07\x0788\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x03\x03\x07\x0788\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00@@\x80\x80\xf0\xf0LL@@\x00\x00\x00\x00\x00\x00@@\x80\x80\xf0\xf0LL@@\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x02\x02??\x9f\x9f\x0f\x0f\x18\x18  \x00\x00\x01\x01\x02\x02??\x9f\x9f\x0f\x0f\x18\x18  \x00\x00'),
                            bytearray(b'\x00\x00\x00\x0088\xe4\xe4\xc3\xc3  \x00\x00\x00\x00\x00\x00\x00\x0088\xe4\xe4\xc3\xc3  \x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x07<4\x9e\x97\x08\x0f\x18\x18  \x00\x00\x01\x01\x00\x077;\x94\x9b\x00\x0f\x18\x18  \x00\x00'),
                            bytearray(b'\x00\x00\x00\xc0\xd88\xc4$\xc3\xc3  \x00\x00\x00\x00\x00\x00\x00\xc0\x18\xf8\x04\xe4C\xc3  \x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x0c\x0b\x17,0\x93\x9e\r\x0f\x18\x18  \x00\x00\x00\x0f\x00\x1f#?\x90\x9f\x00\x0f\x18\x18  \x00\x00'),
                            bytearray(b'\x80@\xc0`\xc8\xb8\xa4d\xc3\xc3  \x00\x00\x00\x00\x00\xc0@\xa0\x08\xf8\x04\xe4C\xc3  \x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xe0`P\x80\xb0\x00\xf0\x00\x00\x00\x00\x00\x80\x80@\xc0 \x80\xf0@\xf0\x00\xf0'),
                            None,
                            bytearray(b'0\xf0x\xf8~\xfe\xe1\xc1\xe0\x00````\x00\x00\x00\xf0\x00\xf8\x1e\xfe!\xe1\xe0\xe0````\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01'),
                            bytearray(b'\x00\x00\x0cr\xeb\xf6\xadS\x1f\xe7\xdf\xbb\xd3\x7f\xff\x03\x00\x00\x00~\xc69\x1f\xe0\x1f\xe0\x9bd\xc3<\x7f\x00'),
                            bytearray(b'\x01\x01\x02\x02??oo\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02??oo\x07\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x7f\x82\x7f\x80\xe6\x99\x05{\xfa\xfe66BB@@\x1e\x01\x1c\x03\x00\x07\x80\x07\x81\x87J\x06rB@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\x80P@v\xe6\xe1\xc1\xe0\x80````\x00\x00x\xf8\xb8\xf8\x1e\xfe\xa1a`\xe0````\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x02>=mo\x06\x06\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01<?lo\x05\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~\x85>\xc1\xa4\xdb\x05{\xf9\xfe66BB@@\x04\x03\x00\x07\x00\x07\x81\x06\x80\x87J\x06rB@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xa0\x00`\x00\xe0\x00\xf0\x00\x00\x00\x00\x00\x80\x80@\x00\xe0\x80\xe0\x00\xe0\x00\xf0'),
                            None,
                            bytearray(b'\x10\xe8(\xf0X\xd8\xd0\xd0\x90\x90\x88\x88\x88\x88\x80\x80\x00\xf8\x00\xf8 \xf8 \xf0`\xf0p\xf8p\xf8x\xf8'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x01\x02\x02\x03\x03\x01\x01\x02\x01\x02\x02\x03\x00\x00\x01\x00\x00\x03\x00\x03\x01\x02\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\x18\xe4\xd6m_\xa1\x1f\xe9\xb8v\xa1\xff\xd9>\xf3\x0e\x00\xfc\x0c\xf3?\xc0?\xc07\xc9\x86y\xfe\x01>\x01'),
                            bytearray(b'\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'c\x9e/\xdc\x0e\xf9\x04\xfbu\x8b}\x87~\x85~\x85\x1e\x01\x1c\x03\x08\x07\x00\x07\x00\x07\x04\x03\x04\x03\x04\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xd0\x10\xc8\x08\xfe\x0e\xf1\x01\xe0\x00\xe0```\x00\x00\xe0\xf0\xf8\xf8\xfe\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\r\xf4\x9b\xac@[\x17\x1e\x0e\x08\x06\x0c\x0f\x03\r\x07\x1c\xe3H\xf7$\x7f\x01\x1f\x07\x0e\x03\x0e\x00\x0f\x04\x0b'),
                            None,
                            bytearray(b'\n\x0e\x1c\x1c>>oo\x07\x07\x00\x00\x00\x00\x00\x00\x01\x0f\x1b\x1f?>nn\x06\x06\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'%\xdc\xcb8\xb0\xf0\xe2\xe2\xfa:{\x9brr@@\xc3?\x07\xff\x0f\xff\x1d\x03\x05\x03\x04\x03BB@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00@\x00\xc0@`\x80\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\xc0@\x80\x00\xe0'),
                            bytearray(b'\x93s!\xe1\xb1\x81\xcf\x0f??jn\x02\xfe\x13\xee\x0c\xff\x1e\xff~\xff\xf0\xcf\xc0\x0f\x91\x0f\x01\xffa\x9f'),
                            bytearray(b'`\x80\xa0\xc0\x90\xe0\xd0\xe0P` 0\xa00\xd0\x10\x00\xe0\x00\xe0\x00\xf0\x00\xf0\x80\xf0\xc0\xf0\xc0\xf0\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01\x07\x01\x1f\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x04\x07\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0 \xf8 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xe0\x18'),
                            bytearray(b'?\x12?`?$\x7f\xc0\xff\x00\xfe\xb0\xde\xe0\xbfb\x1f ?@wH?\xc0\x7f\x80\xbfA\x8fq\x0e\xf1'),
                            bytearray(b'\xf84\xfe\x03\xfaG\xf5\x8b\xce01\x0e\xec\x9f\xdf?\xf8\x04\xfe\x01x\x87\xf9\x06\xf0\x0f\x80\xff\x80\xff\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'P\x10\x08\x08\xbe\x8e\xb1\x81\xa0\x80````\x00\x00\xe0\xf0\xf8\xf8~\xfeq\xf1`\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'de\x00\x01\x02\x03\x01\x01\x01\x01\x01\x01\x01\x01\x01\x01\x1a|\x0e\x0c\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x01\x01\x1e\x1f>?no\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x1e<<ll\x06\x06\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfd\x0b\xfd\x0b\xfd\x0b\xfd\x0b\xed\x1b{\x9frr@@\x08\x07\x08\x07\x08\x07\x08\x07\x00\x07\x00\x07BB@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x80\x00\x80\x00\xc0\x00@\x80\x80\xe0\x80\xe0@`\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xc0\x00\xe0\x00\xe0\x80\xe0'),
                            bytearray(b'D\xff8\xef\xbdC\xfe0\xde>\xfc\x0c\xfb\x0f\xfd\x0b\x00?8\x078\x071\x0f\x01?\x03\x0f\x08\x07\x08\x07'),
                            bytearray(b'\x80\xa0\xa0\xb0\xa0\xb0`0\xe00\xe00`0P\x10@\xe0@\xf0@\xf0\xc0\xf0\xc0\xf0\xc0\xf0\xc0\xf0\xe0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x1f>\x7f\xc0?G\x7f\x80\xff\xa0?\xe0\x00\x00\x00\x00\x1e!\x7f\x80\xb8\xc7>\xc1?\xc0\x1f\xe0'),
                            bytearray(b'\x00\x00\x00\x00\x80`\xf0\xc8\xe9\x17\xfeG\xf8\x06\xf7\t\x00\x00\x00\x00\x00\xe0\xc08\x7f\x80|\x83\xf8\x06\xf9\x06'),
                            bytearray(b'o\xf0x\x1f_g3<\x14\x17\xe8\x1b\xfa;\x9f\xdf\x7f\x80\x1f`\x07x\x00?\x08\x17D\xbb\xc49\xe0<'),
                            bytearray(b'\xeb\x1c\x19\xf6\xf8\xe7\xf6\x0f\x0f\xffq\xf18\xf8\x99\xf9\xf8\x07\xf0\x0f\xe0\x1f\x00\xff\x00\xff\x0e\xff\x07\xff\x06\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=104),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'p\x10h\x08~\x0e\xf1A\xe0`\xe0\xe0``\x00\x00\xe0\xf0\xf8\xf8\xfe\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x06\x19\x19<8il\x04\x06\x02\x03\x01\x01\x00\x00\x01\x07\x18\x1f8?in\x00\x07\x00\x03\x00\x01\x00\x00'),
                            bytearray(b'\x03\x03\xbf\xbfA\xff\xads\xeaVm\xbc\xf2\xc2@@\xfc\x83@\xbf\x00\xff\xb0O\x91oC\xffr\xf2@@'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80\x00\xc0\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xc0\x00\xe0'),
                            None,
                            bytearray(b'@` 0\xa00\xa00\xd0\x10\xd0\x10\xd0\x10\xf0\x10\x80\xe0\xc0\xf0\xc0\xf0\xc0\xf0\xe0\xf0\xe0\xf0\xe0\xf0\xe0\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x1d\x1e\x1f\x1c?\x00?\x10?\t?\x00/\x00\x00\x00\x18\x07\x1e\x01\x0e1\x17(\x1d"\x1d"\x1f0'),
                            bytearray(b'\x00\x00\xe0\xd8\xbev\xde7\xdd\x16\x90?\x97/\xc7\x0f\x00\x00\xc08v\x88\xf0\x0f\xd0/\x90o\xa0_\xc0?'),
                            bytearray(b"/\x00?\x026\x1f\x168\x18\x01\x0c\x15\x1e\x1f\x07\x07\x1f0\x0f0\x1f \x18\'\x06\x1f\x02\x1f\x02\x1f\x00\x07"),
                            bytearray(b'\x86N5\x8c\x0f\xbcK8\x9fxq\xf0\x00\x80\x80\x80\xf1?\xb3\x7f\x83\x7f\x07\xff\x07\xff\x0f\xff\x7f\xf3\x7f\xe3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'p\x10h\x08~\x0e\xf1A\xe0`\xe0\xe0``\x00\x00\xe0\xf0\xf8\xf8\xfe\xfe\xf1\xf1\xe0\xe0\xe0\xe0``\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x06\x18\x1b8<ol\x06\x07\x01\x01\x00\x00\x00\x00\x01\x07\x18\x1f8?in\x04\x07\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'CC\xc7\xc7\rO\x05cV\xca\xe9\xd4CYF@\xbc\xc38\xc70\xcf\x00\xff\x19\xe7\x13\xefg\x7f^^'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80\x00\xc0\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xc0\x00\xe0'),
                            None,
                            bytearray(b'@` 0\xa00\xa00\xd0\x10\xd0\x10\xd0\x10\xf0\x10\x80\xe0\xc0\xf0\xc0\xf0\xc0\xf0\xe0\xf0\xe0\xf0\xe0\xf0\xe0\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x1d\x1e\x1f\x1c?\x00?\x10?\t?\x00/\x00\x00\x00\x18\x07\x1e\x01\x0e1\x17(\x1d"\x1d"\x1f0'),
                            bytearray(b'\x00\x00\xe0\xd8\xbev\xde7\xdd\x16\x90?\x97/\xc7\x0f\x00\x00\xc08v\x88\xf0\x0f\xd0/\x90o\xa0_\xc0?'),
                            bytearray(b"/\x00?\x026\x1f\x168\x18\x01\x0c\x15\x1e\x1f\x07\x07\x1f0\x0f0\x1f \x18\'\x06\x1f\x02\x1f\x02\x1f\x00\x07"),
                            bytearray(b'\x86N5\x8c\x0f\xbcK8\x9fxq\xf0\x00\x80\x80\x80\xf1?\xb3\x7f\x83\x7f\x07\xff\x07\xff\x0f\xff\x7f\xf3\x7f\xe3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=12, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=32, mold_id=16),
                        AnimationSequenceFrame(duration=32, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=17),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=32, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=48, mold_id=2),
                        AnimationSequenceFrame(duration=48, mold_id=2),
                        AnimationSequenceFrame(duration=16, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=18),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=19),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=18),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=19),
                        AnimationSequenceFrame(duration=32, mold_id=8),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=10),
                        AnimationSequenceFrame(duration=16, mold_id=11),
                        AnimationSequenceFrame(duration=12, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                        AnimationSequenceFrame(duration=6, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                        AnimationSequenceFrame(duration=22, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                        AnimationSequenceFrame(duration=6, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                        AnimationSequenceFrame(duration=6, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=13),
                        AnimationSequenceFrame(duration=32, mold_id=12),
                        AnimationSequenceFrame(duration=16, mold_id=11),
                        AnimationSequenceFrame(duration=6, mold_id=12),
                        AnimationSequenceFrame(duration=6, mold_id=14),
                        AnimationSequenceFrame(duration=6, mold_id=15),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=32, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=48, mold_id=2),
                        AnimationSequenceFrame(duration=16, mold_id=2),
                        AnimationSequenceFrame(duration=32, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
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
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=32, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=16, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=16, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=18),
                        AnimationSequenceFrame(duration=6, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=19),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL144_MUKUMUKU,
    palette_offset=0,
    unknown_num=8
)
