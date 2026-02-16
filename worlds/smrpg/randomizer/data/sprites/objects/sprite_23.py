# SPR0023_MALLOW_NONPROTAGONIST_5

from randomizer.data.variables.sprite_palette_names import SPAL702_MALLOW_PUNCH
from smrpgpatchbuilder.datatypes.graphics.classes import (
    CompleteSprite,
    AnimationPack,
    AnimationPackProperties,
    AnimationSequence,
    AnimationSequenceFrame,
    Mold,
    Tile,
    Clone,
)

sprite = CompleteSprite(
    animation=AnimationPack(
        264,
        length=622,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80\x80\xc0\x00@\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00@\x00@@\xc0@\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x01\x02\x03\x06\x06\x00\x0c\x1e\x11\x12\x1e\x04\x01\x01\x0f\x00\x00\x00\x00\x01\x00\x03\x00\x03\x03\x01\x01\x1f\x05\x1e\x0f'),
                            None,
                            bytearray(b'\x02\x1c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1d\x0c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe0\x1d\x02\xfd|\x83\xfb\x07/\xdf\xfe\xfexy4\x88\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x87\x01\xfc\xbb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18(\x1c.v\x0e\x00\x00\x00\x00\x00\x00\x00\x008\x00\x04\x00B\x02\x80\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x81\xf8\x05\xfc\x02\xf0\x0f\xf1\x00\xf9\x00\xf8\x00\xe8\x00\x85\x01\x01\x01\x03\x02\x02\x02'),
                            bytearray(b'v\x8et\x8c\xe8\x98\xa0\xe4@\xd0\xc0@@\xe0\x00\xa0\x00\x00\x02\x00\x06\x00\x1c\x040\x10 \x00  ` '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=100),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\xc0\x00@\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00@\x00@@\xc0@\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=117),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'v\x8et\x8c\xe8\x98\xa0\xe4@\xd0\xc0@@\xe0\x00\xa0\x00\x00\x02\x00\x06\x00\x1c\x040\x10 \x00  ` '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02\x1c\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1d\x0c\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x01\x02\x03\x06\x06\x00\x0c\x1e\x11\x12\x1e\x04\x01\x01\x0f\x00\x00\x00\x00\x01\x00\x03\x00\x03\x03\x01\x01\x1f\x05\x1e\x0f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x81\xf8\x05\xfc\x02\xf0\x0f\xf1\x00\xf9\x00\xf8\x00\xe8\x00\x85\x01\x01\x01\x03\x02\x02\x02'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe0\x1d\x02\xfd|\x83\xfb\x07/\xdf\xfe\xfexy4\x88\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x87\x01\xfc\xbb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18(\x1c.v\x0e\x00\x00\x00\x00\x00\x00\x00\x008\x00\x04\x00B\x02\x80\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=101),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\xc0\x00\xe0p\xf0\xb0\xb8\x10\xdc\x08.\x00\x00\xc0\x00 \x00\x10\x00\x08\x00@\x00\xe0\xc00 '),
                            None,
                            bytearray(b'\x04\x17\x00\x0b\x01\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x10\x0c\x08\x06\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x03\x01\x07\t\x0f\x06\n\x1c\x11\x1d\x17\x1a\x17\x02\x07\x00\x00\x00\x00\x00\x00\x11\x00#\x01"\x02$\x04<\x04'),
                            bytearray(b'\x00 \x80\xb8\x00\xf3\x18\xdf\x80\xff9\xc7z\x86`\x9d\xe0 y8\xfc\xf0\xe0\xc0\x00\x00\x00\x00\x01\x00\x03\x01'),
                            bytearray(b'\x03\x0b\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x08\x0f\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b',>(\xfa0408\x00\x00\x00\x00\x00\x00\x00\x00\xc2\x02\xc6\xc2\x0c\x04\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'!!\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1f\x12\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80`\xc0 \xe0\x00\xe0\xc0\xc0\xa0\x80@\x00\x80\x00\x00\xe0`\xe0 \xe0\xe0  ``\xc0\xc0\x80\x80\x00\x80'),
                            bytearray(b'\x0e\x0e\x00\x00\x08\x08\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x0eq\x00?\x08\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@@@@@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80@\x80@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'@\xb0\x10\xf0`\xe0\xe0h@\xd8\xc0\xd0\x80\xf0`\x10\x00\x00\x00\x00\x10\x00\x18\x088\x180\x10pp\x90p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x08\x0f\x00\x1f\x10\x0f\x10\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x000\x08x\x88x\x14\xfa\x16\xf9\x8fp\x7f\xc0\xfe\x010\x00x\x00\xf8\x80\xf6\x06\xf0\x00\xe0\x80\x00\x00\x00\x00'),
                            bytearray(b'\x17\x18\x1f\x0816\x10\x13\x03\x01\x077\t\x01/< \x000\x10\x08\x00,\x00>\x0280\x0e8\x1f3'),
                            bytearray(b'\xfe\x01\xfd\x03\xe3\x1f?\xfe\xba\x9d\x11O\xdf\xdfg\xe7\x00\x00\x00\x00\x00\x00\x00\x00` \xf0P \x00\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1f!\x0f\x10CxF\x7f}}AAA@\x01\x00\x1f>88z\x06\x7f\x03}\x03A?A>\x01>'),
                            bytearray(b'\xf2\xe3\xc98\xc6?\xa1\x7f\xcf\r\xe5\xbc\xc3\xff\xc2\xfe\xfd\x0fyv\x01?\xc0\xfe\xf2>\xfd\x83\xff\x80\xfe\x81'),
                            bytearray(b'\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x0f\x0f\x00\x00\x00\x00\x0f\x0f??\x7f\x7f\x7f\x7f??\x0f\x0f\x00\x00'),
                            bytearray(b'\x00\x00\xf0\xf0\xfc\xfc\xfe\xfe\xfe\xfe\xfc\xfc\xf0\xf0\x00\x00\x00\x00\xf0\xf0\xfc\xfc\xfe\xfe\xfe\xfe\xfc\xfc\xf0\xf0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\xc0\x00\xe0p\xf0\xb0\xb8\x10\xdc\x08.\x00\x00\xc0\x00 \x00\x10\x00\x08\x00@\x00\xe0\xc00 '),
                            None,
                            bytearray(b'\x04\x17\x00\x0b\x01\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x10\x0c\x08\x06\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=355),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x03\x01\x07\t\x0f\x06\n\x1c\x11\x1d\x17\x1a\x17\x02\x07\x00\x00\x00\x00\x00\x00\x11\x00#\x01"\x02$\x04<\x04'),
                            bytearray(b'\x00 \x80\xb8\x00\xf3\x18\xdf\x80\xff9\xc7z\x86`\x9d\xe0 y8\xfc\xf0\xe0\xc0\x00\x00\x00\x00\x01\x00\x03\x01'),
                            bytearray(b'\x03\x0b\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x08\x0f\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b',>(\xfa0408\x00\x00\x00\x00\x00\x00\x00\x00\xc2\x02\xc6\xc2\x0c\x04\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=355),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80`\xc0 \xe0\x00\xe0\xc0\xc0\xa0\x80@\x00\x80\x00\x00\xe0`\xe0 \xe0\xe0  ``\xc0\xc0\x80\x80\x00\x80'),
                            None,
                            bytearray(b'@@@@@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80@\x80@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1f!\x0f\x10CxF\x7f}}AAA@\x01\x00\x1f>88z\x06\x7f\x03}\x03A?A>\x01>'),
                            bytearray(b'\xf2\xe3\xc98\xc6?\xa1\x7f\xcf\r\xe5\xbc\xc3\xff\xc2\xfe\xfd\x0fyv\x01?\xc0\xfe\xf2>\xfd\x83\xff\x80\xfe\x81'),
                            bytearray(b'!!\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1f\x12\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0e\x0e\x00\x00\x08\x08\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x0eq\x00?\x08\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'@\xb0\x10\xf0`\xe0\xe0h@\xd8\xc0\xd0\x80\xf0`\x10\x00\x00\x00\x00\x10\x00\x18\x088\x180\x10pp\x90p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=353),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x08\x0f\x00\x1f\x10\x0f\x10\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x000\x08x\x88x\x14\xfa\x16\xf9\x8fp\x7f\xc0\xfe\x010\x00x\x00\xf8\x80\xf6\x06\xf0\x00\xe0\x80\x00\x00\x00\x00'),
                            bytearray(b'\x17\x18\x1f\x0816\x10\x13\x03\x01\x077\t\x01/< \x000\x10\x08\x00,\x00>\x0280\x0e8\x1f3'),
                            bytearray(b'\xfe\x01\xfd\x03\xe3\x1f?\xfe\xba\x9d\x11O\xdf\xdfg\xe7\x00\x00\x00\x00\x00\x00\x00\x00` \xf0P \x00\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=353),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\xc0\x00\xe0p\xf0\xb0\xb8\x10\xdc\x08.\x00\x00\xc0\x00 \x00\x10\x00\x08\x00@\x00\xe0\xc00 '),
                            None,
                            bytearray(b'\x04\x17\x00\x0b\x01\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x10\x0c\x08\x06\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x03\x03\x01\x07\t\x0f\x06\n\x1c\x11\x1d\x17\x1a\x17\x02\x07\x00\x00\x00\x00\x00\x00\x11\x00#\x01"\x02$\x04<\x04'),
                            bytearray(b'\x00 \x80\xb8\x00\xf3\x18\xdf\x80\xff9\xc7z\x86`\x9d\xe0 y8\xfc\xf0\xe0\xc0\x00\x00\x00\x00\x01\x00\x03\x01'),
                            bytearray(b'\x03\x0b\x00\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x08\x0f\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b',>(\xfa0408\x00\x00\x00\x00\x00\x00\x00\x00\xc2\x02\xc6\xc2\x0c\x04\x08\x08\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=109, y=354),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80`\xc0 \xe0\x00\xe0\xc0\xc0\xa0\x80@\x00\x80\x00\x00\xe0`\xe0 \xe0\xe0  ``\xc0\xc0\x80\x80\x00\x80'),
                            None,
                            bytearray(b'@@@@@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80@\x80@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=368),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1f!\x0f\x10CxF\x7f}}AAA@\x01\x00\x1f>88z\x06\x7f\x03}\x03A?A>\x01>'),
                            bytearray(b'\xf2\xe3\xc98\xc6?\xa1\x7f\xcf\r\xe5\xbc\xc3\xff\xc2\xfe\xfd\x0fyv\x01?\xc0\xfe\xf2>\xfd\x83\xff\x80\xfe\x81'),
                            bytearray(b'!!\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1f\x12\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0e\x0e\x00\x00\x08\x08\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x0eq\x00?\x08\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'@\xb0\x10\xf0`\xe0\xe0h@\xd8\xc0\xd0\x80\xf0`\x10\x00\x00\x00\x00\x10\x00\x18\x088\x180\x10pp\x90p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=352),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x08\x0f\x00\x1f\x10\x0f\x10\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x000\x08x\x88x\x14\xfa\x16\xf9\x8fp\x7f\xc0\xfe\x010\x00x\x00\xf8\x80\xf6\x06\xf0\x00\xe0\x80\x00\x00\x00\x00'),
                            bytearray(b'\x17\x18\x1f\x0816\x10\x13\x03\x01\x077\t\x01/< \x000\x10\x08\x00,\x00>\x0280\x0e8\x1f3'),
                            bytearray(b'\xfe\x01\xfd\x03\xe3\x1f?\xfe\xba\x9d\x11O\xdf\xdfg\xe7\x00\x00\x00\x00\x00\x00\x00\x00` \xf0P \x00\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=352),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0\xb0\xf8\xb8\xc8\xc8\xc8\xc8\xd0\xd0\xa0\xa0\xc0\xc0\x80\x80P\x10xx\xc8\xf8\xc88\xd00\xa0`\xc0\xc0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b' #\x1e\x16\x04\x1b\x13\x15\x1f\x1d\x0f\x0f\x00\x00\x00\x00C\x7f.)\x10\x10\x16\x1e\x1d\x13\x0f\x0f\x00\x00\x00\x00'),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf9\xc1\xf8\xff\x18\x1e\x0f\x0f\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf9\xc6\xff\xf0\x1e\x19\x0f\x0f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=96),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=96),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0\xb0\xf8\xb8\xc8\xc8\xc8\xc8\xd0\xd0\xa0\xa0\xc0\xc0\x80\x80P\x10xx\xc8\xf8\xc88\xd00\xa0`\xc0\xc0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b' #\x1e\x16\x04\x1b\x13\x15\x1f\x1d\x0f\x0f\x00\x00\x00\x00C\x7f.)\x10\x10\x16\x1e\x1d\x13\x0f\x0f\x00\x00\x00\x00'),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf9\xc1\xf8\xff\x18\x1e\x0f\x0f\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf9\xc6\xff\xf0\x1e\x19\x0f\x0f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=113),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=97),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=97),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0\xb0\xf8\xb8\xc8\xc8\xc8\xc8\xd0\xd0\xa0\xa0\xc0\xc0\x80\x80P\x10xx\xc8\xf8\xc88\xd00\xa0`\xc0\xc0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b' #\x1e\x16\x04\x1b\x13\x15\x1f\x1d\x0f\x0f\x00\x00\x00\x00C\x7f.)\x10\x10\x16\x1e\x1d\x13\x0f\x0f\x00\x00\x00\x00'),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf9\xc1\xf8\xff\x18\x1e\x0f\x0f\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf9\xc6\xff\xf0\x1e\x19\x0f\x0f'),
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\x00p\x80\xf8\xe0\x14\xf0<\x88\x8c\x18\xe0\xe0\x00\xe0\xe0\x90\x10\x08\x08\x0c\x04\x04\x04t\x04\xf8\xe0\xe0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x06\x07\x07\x18\xe7\xc3\xfc\x81\x83\x18\xe7\x00\x00\x01\x01\x07\x06\x18\x00\x00\x00\x00\x00|\x00\xff\xe7\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xa0\xa0\xc0\x80\xc0\xc0      \xc0\xc0\x00\x00@\x00@@\xc0\xc0 \xe0 \xe0 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b" #\x1e\x16\x04\x1b35;9\x1f\x1f\x00\x00\x00\x00C\x7f.)\x10\x106.9\'\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf8\xc0\xda\xd6wk\x1e\x1e\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf8\xc7\xde\xe9\x7fu\x1e\x1e'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=110),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x01\x00\x06\x07\x07\x18\xe7\xc3\xfc\x81\x83\x18\xe7\x00\x00\x01\x01\x07\x06\x18\x00\x00\x00\x00\x00|\x00\xff\xe7\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=117),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xa0\xa0\xc0\x80\xc0\xc0      \xc0\xc0\x00\x00@\x00@@\xc0\xc0 \xe0 \xe0 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b" #\x1e\x16\x04\x1b35;9\x1f\x1f\x00\x00\x00\x00C\x7f.)\x10\x106.9\'\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf8\xc0\xda\xd6wk\x1e\x1e\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf8\xc7\xde\xe9\x7fu\x1e\x1e'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            bytearray(b'\x00\xe0\x00p\x80\xf8\xe0\x14\xf0<\x88\x8c\x18\xe0\xe0\x00\xe0\xe0\x90\x10\x08\x08\x0c\x04\x04\x04t\x04\xf8\xe0\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x03\x01\x05\x0c\x0f\x1b\xe4\xc1\xff\x80\x9f\x01\xe0\x00\x00\x03\x03\x06\x040\x00\x00\x00\x00\x00\x7f\x1f\xe1\xe0'),
                            bytearray(b'\x00\xe0\x00p\x80\xf4\xe0\x1c\xf8<\x80\x98\x10\xe0\xe0\x00\xe0\xe0\x90\x10\x0c\x04\x04\x04\x04\x04x\x18\xf0\xe0\xe0\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xa0\xa0\xc0\x80\xc0\xc0      \xc0\xc0\x00\x00@\x00@@\xc0\xc0 \xe0 \xe0 \xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b" #\x1e\x16\x04\x1b35;9\x1f\x1f\x00\x00\x00\x00C\x7f.)\x10\x106.9\'\x1f\x1f\x00\x00\x00\x00"),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf8\xc0\xda\xd6wk\x1e\x1e\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf8\xc7\xde\xe9\x7fu\x1e\x1e'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00n`\xd68\xb2|\xf0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x01\x04\x07!?\x08x`f\x80\xb0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x9e\x06p0@\xc0\x00\x00'),
                            bytearray(b'\xf8\xff|\xff\x06\x06\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xfc\x1c\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            None,
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x01\x01\x01\x01\x00\x01'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'd\x1c\xf0\x90p\x1e0N\x10lXh040<\x00\x00\x0c\x00\x80\x00\x80\x00\x80\x00\x84\x00L\x04L\x0c'),
                            None,
                            bytearray(b'\x00\x0c\x00\x1e\x00\x1e\x00\x1e\x00\x0e\x00\x0e\x00\x0c\x00\x0c<\x0c>\x1e\x1e\x1e\x1e\x1e\x0e\x0e\x0e\x0e\x0c\x0c\x0c\x0c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=106),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00n`\xd68\xb2|\xf0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xf8\xff|\xff\x06\x06\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xfc\x1c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x04\x07!?\x08x`f\x80\xb0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x9e\x06p0@\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            None,
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x01\x01\x01\x01\x00\x01'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\x00\x1e\x00\x1e\x00\x1e\x00\x0e\x00\x0e\x00\x0c\x00\x0c<\x0c>\x1e\x1e\x1e\x1e\x1e\x0e\x0e\x0e\x0e\x0c\x0c\x0c\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'd\x1c\xf0\x90p\x1e0N\x10lXh040<\x00\x00\x0c\x00\x80\x00\x80\x00\x80\x00\x84\x00L\x04L\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=107),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00n`\xd68\xb2|\xf0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xf8\xff|\xff\x06\x06\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xfc\x1c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x04\x07!?\x08x`f\x80\xb0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x9e\x06p0@\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            None,
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x01\x01\x01\x01\x00\x01'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\x00\x1e\x00\x1e\x00\x1e\x00\x0e\x00\x0e\x00\x0c\x00\x0c<\x0c>\x1e\x1e\x1e\x1e\x1e\x0e\x0e\x0e\x0e\x0c\x0c\x0c\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'd\x1c\xf0\x90p\x1e0N\x10lXh040<\x00\x00\x0c\x00\x80\x00\x80\x00\x80\x00\x84\x00L\x04L\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\t\x0f\x02\x0e\x04\x1c\x08:\xe0\xe8@P\x00\x00\x00\x00\x00\x00\x11\x00#\x00F\x02\x18\x08\xb0\x10\x00\x00\x00\x00'),
                            bytearray(b'\x00\x08\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x08\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x03\x01\x03\x02\x01\x02\x05\x04\x07\x00\x00\x00\x00\x00\x00\x02\x02\x00\x00\x00\x00\x04\x04\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00`\x80`\x90\x18\xf8x\xf8\xf0\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x18\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=107),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=108),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x03\x01\x03\x02\x01\x02\x05\x04\x07\x00\x00\x00\x00\x00\x00\x02\x02\x00\x00\x00\x00\x04\x04\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00`\x80`\x90\x18\xf8x\xf8\xf0\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x18\x00'),
                            bytearray(b'\t\x0f\x02\x0e\x04\x1c\x08:\xe0\xe8@P\x00\x00\x00\x00\x00\x00\x11\x00#\x00F\x02\x18\x08\xb0\x10\x00\x00\x00\x00'),
                            bytearray(b'\x00\x08\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x08\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=108),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\t\x0f\x02\x0e\x04\x1c\x08:\xe0\xe8@P\x00\x00\x00\x00\x00\x00\x11\x00#\x00F\x02\x18\x08\xb0\x10\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=114),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x03\x01\x03\x02\x01\x02\x05\x04\x07\x00\x00\x00\x00\x00\x00\x02\x02\x00\x00\x00\x00\x04\x04\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00`\x80`\x90\x18\xf8x\xf8\xf0\xf0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x18\x00'),
                            None,
                            bytearray(b'\x00\x08\x000\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x08\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=108),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00n`\xd68\xb2|\xf0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x01\x04\x07!?\x08x`f\x80\xb0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x9e\x06p0@\xc0\x00\x00'),
                            bytearray(b'\xf8\xff|\xff\x06\x06\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xfc\x1c\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            None,
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x01\x01\x01\x01\x00\x01'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'd\x1c\xf0\x90p\x1e0N\x10lXh040<\x00\x00\x0c\x00\x80\x00\x80\x00\x80\x00\x84\x00L\x04L\x0c'),
                            None,
                            bytearray(b'\x00\x0c\x00\x1e\x00\x1e\x00\x1e\x00\x0e\x00\x0e\x00\x0c\x00\x0c<\x0c>\x1e\x1e\x1e\x1e\x1e\x0e\x0e\x0e\x0e\x0c\x0c\x0c\x0c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=106),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00n`\xd68\xb2|\xf0\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xf8\xff|\xff\x06\x06\x00\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf8\x00\xfc\x1c\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x04\x07!?\x08x`f\x80\xb0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x9e\x06p0@\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf2\x02\xcf\x06\xc7\xfb\xf0\xf0\xe0\x00hX\xdf\xafxx\xf1\x0c\x19\xf9\x07\xff\x08\xff\xe0\x1fx\xa7\xff\xd7xx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            None,
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x01\x01\x01\x01\x00\x01'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x8fxX\x12m\xce\xd7\xef\xe7\x7f\x7f\x01\x01\x00\x00\x0f\xff\xb8\xa7CC\xd9\xb9\xe7\x9f\x7f\x7f\x01\x01\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\x00\x1e\x00\x1e\x00\x1e\x00\x0e\x00\x0e\x00\x0c\x00\x0c<\x0c>\x1e\x1e\x1e\x1e\x1e\x0e\x0e\x0e\x0e\x0c\x0c\x0c\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=114),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'd\x1c\xf0\x90p\x1e0N\x10lXh040<\x00\x00\x0c\x00\x80\x00\x80\x00\x80\x00\x84\x00L\x04L\x0c'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=106),
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
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                    ]
                ),
            ],
        ),
    ),
    palette_id=SPAL702_MALLOW_PUNCH,
    palette_offset=0,
    unknown_num=0,
)
