# SPR0285_AMEBOID

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL083_AMEBOID
sprite = CompleteSprite(
    animation=AnimationPack(28, length=635, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x02\x02\x04\x05\n\x0c\x14\x08\x10\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\r\x00\x1b\x00\x1f\x00'),
                            bytearray(b'\x00\x00\x14"\x19\xe0\x99a\xf5\x06\xc5\x06&\'\xb1\xd9\x00\x00>\x00\xff\x00\xfe\x00\xf8\x00\xf8\x00\xd8\x00\x06\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x00@\x00\xa0\xe0P\xf0(h\x94\x00\x00\x00\x00\x80\x00\xc0\x00`\x000\x00\x18\x00\x0c\x00'),
                            bytearray(b"\x10 \x10 \x10 \x0c0\'<\x10\x1f\x19\x1e\x06\x07?\x00?\x00?\x003\x047\x0c\x1f\x00\x1f\x03\x07\x01"),
                            bytearray(b',\xdc\xe8\x98\x90\xf0\xc0\xe0\x00\x00\x81\x00&\xd9J?\x03\x00\x07\x00\x0f\x00\x1f\x00\xff\x00\xff\x00\xf9\x02\xfb\xc6'),
                            bytearray(b'\xb4\xc0\x88\xfa|j\x1c\x02<\x02\x82\x0e\x82\x1eD\xbc\x0c\x00\x06\x00\x96\x00\xfe\x00\xfe\x00\xf6\x08\xe6\x18\xc48'),
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x03\x03\x03\x00\x01\x01\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\xe4\xff\xd3\x8f\x0f\x91u\xcb\xf0\x7f\xff\xf65?\x0f\x0f\xfe\x01\xfb\x04\xef\x00\xf5\n\xefp\xf9\xe0;0\x0f\x0f'),
                            bytearray(b'\x08\xf8\xe0\xe0\xc0\xc0\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\x80\x80\x08\xf0\xe0\x00\xc0\xc0\xe0\xe0\xe0`\xe0`\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x06\x07\x08\x0c\x10\x08\x11\x12#\x00\x00\x00\x00\x01\x00\x07\x00\x0f\x00\x1f\x00\x1e\x00<\x00'),
                            bytearray(b'\x00\x00\x18fv\x81\x83\x03\x84\x07\xc7\xc4e\xa6\xe2#\x00\x00~\x00\xff\x00\xfc\x00\xf8\x008\x00\x18\x00\x1c\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x00@\x80\xa0@\xd0\xa0x\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00`\x000\x00\x18\x00'),
                            bytearray(b"\x03#\x07\'\x11!.07<2=\x1c\x1f\x0e\x0f<\x008\x00>\x003\x047\x0c?\x00\x1f\x00\x0f\x01"),
                            bytearray(b'\x81A\xc0\xc0\x80\x80\x80\x80\x00\x008\x80\x07\xfcQ?>\x00?\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\xfc\x01\xfd\xe3'),
                            bytearray(b'`\x94\xf8\xfcFB\x1e\n\xba\x0e\xc4<\x88x\x10\xf0\x0c\x00\x04\x00\xbe\x00\xf6\x00\xf6\x00\xec\x10\xc80\x10\xe0'),
                            bytearray(b'\x01\x01\x02\x07\x01\x02\x04\x02\t\x0c\x0c\x0f\x07\x07\x00\x00\x01\x00\x05\x00\x05\x00\x05\x00\x0f\x08\x0f\x0c\x07\x07\x00\x00'),
                            bytearray(b'\xf0\xff\xfd\x93\x9a\xf7\xc7~~\xff\x7f\xff\xc0\xc0\x00\x00\xc87\xcd\x02\xcb\x04\xff\x06\xff~\xff\x7f\xc0\xc0\x00\x00'),
                            bytearray(b'\xe0\xe0p\xf0\xb0p\xb0p`\xe0\xc0\xc0\x00\x00\x00\x00\xe0\x00\xd00\xd00\xf00\xa0`\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x03\x04\x04\x08\x02\x12\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1d\x00'),
                            bytearray(b'\x00\x00\x0c2H\xb1\xed\x10\x99\x01BsRs(X\x00\x00>\x00\xff\x00\xff\x00\xfe\x00\x8c\x00\x8c\x00\x87\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00@\x00 \x00\x90\xa0P@\x88\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00p\x000\x008\x00'),
                            bytearray(b'\x13#!\x01"\x00.\x00\x17,\x10\x1f\r\x0e\x06\x07<\x00>\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01'),
                            bytearray(b'\xe8\x980P  \x80\x00\xf8\x00\x11\xe8\xc78C>\x07\x00\x8f\x00\xdf\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6'),
                            bytearray(b'\xb0\xcc`LXt04\xf0\x94\xec\x84\xe0\x9c\x08x\x1c\x00\x9c\x00\x8c\x00\xcc\x00l\x00|\x00`\x1c\x88p'),
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf7\xf8\xaf\xdf}\xd3)\xfd\xef\xff\xf5\xfb\x0f\x0f\x00\x00\xbf@\xff\x00\xff\x00\xf3\x00\xf1\xe1\xff\xf1\x0f\x0f\x00\x00'),
                            bytearray(b'0\xf0`\xe0`\xe0\xe0\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x000\xc0\xc0 \xa0`\xe0\xe0\xe0\xe0\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x04\x07\n\x0e\x15\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0c\x00\x18\x00'),
                            bytearray(b'\x00\x00\x00\x00(F\x98\x07\t\x06\xc7\xc0\x01\x80\x84\x84\x00\x00\x00\x00~\x00\xff\x00\xff\x00?\x00\x7f\x00{\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80@@ \xa0P0(\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xb0\x00\xd8\x00'),
                            bytearray(b"\x1d\x0b\'\x0b\x1c\\1P1@1\x00\x18(*6\x10\x000\x00c\x00o\x00\x7f\x00?\x007\x009\x00"),
                            bytearray(b'\r\x1bt;\xd7\x19\x89O\x03\xe7\x98`p\x00\x8f\x00\xe0\x00\xc0\x00\xe0\x00\xf0\x00\xf8\x00\xff\x00\xff\x00\xff\x00'),
                            bytearray(b'\x10\x0c\x08\x04\x08\x04\x18\x04\x00\x0c\x04\x1cH8\x18\xf8\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xd8 '),
                            bytearray(b'\x13\x1c\x0f\x0f\x00\x00\x00\x00\x03\x03\x03\x03\x02\x03\x01\x01\x13\x0c\x0f\x00\x00\x00\x00\x00\x00\x03\x02\x02\x03\x02\x01\x01'),
                            bytearray(b'\xce?8\xff\xe1\xcb\xcb\xe7\xff?\x7f\xdf\xdc<\xf0\xf0\xfe\x01\xf0\x0f\xf7\x00\xfc\x03\xff\x0f?\x1f\xfc\x1c\xf0\xf0'),
                            bytearray(b'`\xe0\x80\x80@\xc0 ` \xe0\xe0\xe0\x00\x00\x00\x00`\x80\x80\x00\xc0\x00\xc0 \xe0 \xe0\xe0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x04\t\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x0e\x00'),
                            bytearray(b'\x00\x00\x00\x00(F\x9e\x01\x81\x00\x80\x00@\xc0\xc3C\x00\x00\x00\x00~\x00\xff\x00\xff\x00\xff\x00?\x00<\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80``P\xb0hx \x00\x00\x00\x00\x00\x00\x80\x00\xe0\x00\xb0\x00\x98\x00\xd8\x00'),
                            bytearray(b'\t\x02\x15\x07\x10 \x00 \x10 \x14$\t\x13\x14\x18\x0c\x00\x18\x00?\x00?\x00?\x00;\x00\x1c\x00\x1f\x00'),
                            bytearray(b'\x93\x82\t\x10\t0\xcb2\xea\x13}\x01\x18\x00\x8f\x00|\x00\xfe\x00\xfe\x00\xfc\x00\xfc\x00\xfe\x00\xff\x00\xff\x00'),
                            bytearray(b'H\xc4\x08\xc4\xc8DX\xc4D\xcc\x04\x1cH8\x18\xf8<\x00<\x00<\x00<\x00<\x00\xfc\x00\xf8\x00\xd8 '),
                            bytearray(b'\t\x0e\x01\x01\x01\x01\x03\x03\x03\x03\x03\x03\x01\x01\x00\x00\t\x06\x01\x00\x01\x00\x01\x02\x03\x03\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'\xcc?\xb8\xff\x8bW\x0f\xdf\xaf\x9f_\xbf\xf8\xf8\x00\x00\xfc\x03\xf0\x0f\xbf\x03?\x0f\x7f\x0f\xff\x1f\xf8\xf8\x00\x00'),
                            bytearray(b'`\xe0\x80\x80\x80\x80\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00`\x80\x80\x00\x80\x80\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x05\x00\n\x01\x03\x15\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x06\x00\x0c\x00\x18\x00'),
                            bytearray(b'\x00\x00\x00\x00(D\x9a\x04\xc5\xc2C\xc0\x81\x80\x08\x08\x00\x00\x00\x00|\x00\xfe\x00?\x00?\x00\x7f\x00\xf7\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x00'),
                            bytearray(b'\n.-\x0c(I"A2A2A[h(41\x003\x00w\x00\x7f\x00\x7f\x00\x7f\x00w\x00;\x00'),
                            bytearray(b'\x10\x1c:&>"\xbe2\x1a\x9eD\x840\xc0\xee\x01\xe3\x00\xc1\x00\xc1\x00\xc1\x00\xe1\x00\xfb\x00\xff\x00\xff\x00'),
                            bytearray(b'\x10\x00\x00\x08\x08\x04\x18\x04@\x0c\xf4\x0c\x08\xf8\x18\xf8\xf0\x00\xf8\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xc80\x98`'),
                            bytearray(b'+<\x1e\x1f\r\x0e\x1d\x1e\x0e\x0f\x03\x03\x00\x00\x00\x00+\x14\x1e\x01\x03\x0c\x1f\x1c\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xc0?\x07\xffi\xfe\xffp>\xff\xfe\xff??\x00\x00\xf0\x0f@\xbf\xf3\x00\xff\x00\xff>\xff\xfe??\x00\x00'),
                            bytearray(b'`\xe0\x80\x80\xb0\x100P\x9008\xf8\xe0\xe0\x00\x00`\x80\x80\x00\xe0\x10\xa0\x10\xe0\x10\xd88\xe0\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x00\x00\x02\x14.\x00\x144S\xb5!\xe06A\x18\'\x00\x00\x1e\x00>\x00K\x00\xc8\x00\xdf\x00~\x01\x1c#"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80@\x00\xc0\x80\x80\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x80@\x00\xc0\x80\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=123),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x01\x02\x00\x04\x00\x08\x0f\x0c\x05\x06\x04\x10\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x10\x008\x00/\x00'),
                            bytearray(b'\x00\x00@\x90\xa8D\x90\xd8\xd0\xdc\x12\x99\x8a\x89\x08\x0b\x00\x00\xf0\x00\xfc\x00$\x00"\x00g\x00w\x00\xf7\x00'),
                            bytearray(b'\x1f0#<\x08\x0b\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x1f0?\x00\x0f\x06\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x98\x03\xbeBt\xccx\xf8\x00`\x00\x00\x00\x00\x00\x00\xff\x00\xbe\x00\xf4H\xf8\x00\x00`\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x01\x02\x00\x04\x00\x08\x0f\x0c\x05\x06\x04\x10\x00\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x10\x008\x00/\x00'),
                            None,
                            bytearray(b'\x1f0#<\x08\x0b\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x1f0?\x00\x0f\x06\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x04\n\x13/\x0f?7l\\\x00\x00\x00\x00\x00\x00\x07\x00\x1c\x000\x00@\x00\x83\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\xc0\xe0`\xe0\xe0``\x00\x00\x00\x00\x00\x00\xc0\x000\x00\x18\x00\x18\x00\x9c\x00'),
                            bytearray(b'\xd1\xb0\xa3`L\xc3\xb0\x8f@8\x8cc?\x9fP\xd0\x0f\x00\x1f\x00?\x00\x7f\x00\xff\x00\xff\x00\xff\x00\xd0\x00'),
                            bytearray(b'\x10\x08 \x18\x0c\xf0\x1c\xe4H8\xc0\xc0\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xc0\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00@\x00\xa0\xe0P\xf0(h\x94\xb4\xc0\x00\x00\x80\x00\xc0\x00`\x000\x00\x18\x00\x0c\x00\x0c\x00'),
                            None,
                            bytearray(b'\x88\xfa|j\x1c\x02<\x02\x82\x0e\x82\x1eD\xbc\x08\xf8\x06\x00\x96\x00\xfe\x00\xfe\x00\xf6\x08\xe6\x18\xc48\x08\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x02\x04\x05\n\x0c\x14\x080\x10 \x00\x00\x00\x00\x03\x00\x07\x00\r\x00\x1b\x00?\x00?\x00'),
                            bytearray(b"\x14b\x19\xe0\x99a\xf5\x06\xc5\x06&\'\xb1\xd9,\xdc~\x00\xff\x00\xfe\x00\xf8\x00\xf8\x00\xd8\x00\x06\x00\x03\x00"),
                            bytearray(b"\x10 \x10 \x0c0\'<0?\x19\x1e\x06\x07\x00\x00?\x00?\x003\x047\x0c?\x00\x1f\x03\x07\x01\x00\x00"),
                            bytearray(b'\xe8\x98\x90\xf0\xc0\xe0\x00\x00\x81\x00&\xd9J?\xe4\xff\x07\x00\x0f\x00\x1f\x00\xff\x00\xff\x00\xf9\x02\xfb\xc6\xfe\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00@\x00\xa0\xe0P\xf0(h\x94\xb4\xc0\x00\x00\x80\x00\xc0\x00`\x000\x00\x18\x00\x0c\x00\x0c\x00'),
                            None,
                            bytearray(b'\x88\xfa|j\x1c\x02<\x02\x82\x0e\x82\x1eD\xbc\x08\xf8\x06\x00\x96\x00\xfe\x00\xfe\x00\xf6\x08\xe6\x18\xc48\x08\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=364),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x02\x04\x05\n\x0c\x14\x080\x10 \x00\x00\x00\x00\x03\x00\x07\x00\r\x00\x1b\x00?\x00?\x00'),
                            bytearray(b"\x14b\x19\xe0\x99a\xf5\x06\xc5\x06&\'\xb1\xd9,\xdc~\x00\xff\x00\xfe\x00\xf8\x00\xf8\x00\xd8\x00\x06\x00\x03\x00"),
                            bytearray(b"\x10 \x10 \x0c0\'<0?\x19\x1e\x06\x07\x00\x00?\x00?\x003\x047\x0c?\x00\x1f\x03\x07\x01\x00\x00"),
                            bytearray(b'\xe8\x98\x90\xf0\xc0\xe0\x00\x00\x81\x00&\xd9J?\xe4\xff\x07\x00\x0f\x00\x1f\x00\xff\x00\xff\x00\xf9\x02\xfb\xc6\xfe\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=364),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=379),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=362),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=362),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=377),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00@\x00\xa0\xe0P\xf0(h\x94\xb4\xc0\x00\x00\x80\x00\xc0\x00`\x000\x00\x18\x00\x0c\x00\x0c\x00'),
                            None,
                            bytearray(b'\x88\xfa|j\x1c\x02<\x02\x82\x0e\x82\x1eD\xbc\x08\xf8\x06\x00\x96\x00\xfe\x00\xfe\x00\xf6\x08\xe6\x18\xc48\x08\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=362),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x02\x04\x05\n\x0c\x14\x080\x10 \x00\x00\x00\x00\x03\x00\x07\x00\r\x00\x1b\x00?\x00?\x00'),
                            bytearray(b"\x14b\x19\xe0\x99a\xf5\x06\xc5\x06&\'\xb1\xd9,\xdc~\x00\xff\x00\xfe\x00\xf8\x00\xf8\x00\xd8\x00\x06\x00\x03\x00"),
                            bytearray(b"\x10 \x10 \x0c0\'<0?\x19\x1e\x06\x07\x00\x00?\x00?\x003\x047\x0c?\x00\x1f\x03\x07\x01\x00\x00"),
                            bytearray(b'\xe8\x98\x90\xf0\xc0\xe0\x00\x00\x81\x00&\xd9J?\xe4\xff\x07\x00\x0f\x00\x1f\x00\xff\x00\xff\x00\xf9\x02\xfb\xc6\xfe\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=362),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=377),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=377),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=367),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=367),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=111),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=366),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=366),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=365),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=365),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=363),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x03\x02\x06\x05\n\x06\x04\x1c21$#\x01\x00\x02\x00\x04\x00\x08\x00\x11\x00#\x00O\x00\xdf\x00'),
                            bytearray(b'\x00\x00\x19\x03\x00\x0cx\x19@\xa7D\xda\nv\xf4\x8c\x01\x00\x1c\x00s\x00\x87\x00\x1f\x00>\x00\xbe\x00\xfc\x00'),
                            bytearray(b'\x90\x8e\x0c<\xb0p\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00~\x00\xfc\x00\xf0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=361),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=361),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x03\x02\x06\x05\n\x06\x04\x1c21$#\x01\x00\x02\x00\x04\x00\x08\x00\x11\x00#\x00O\x00\xdf\x00'),
                            bytearray(b'\x00\x00\x19\x03\x00\x0cx\x19@\xa7D\xda\nv\xf4\x8c\x01\x00\x1c\x00s\x00\x87\x00\x1f\x00>\x00\xbe\x00\xfc\x00'),
                            bytearray(b'\x90\x8e\x0c<\xb0p\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00~\x00\xfc\x00\xf0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'xx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=100, y=137),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x03\x02\x06\x05\n\x06\x04\x1c21$#\x01\x00\x02\x00\x04\x00\x08\x00\x11\x00#\x00O\x00\xdf\x00'),
                            bytearray(b'\x00\x00\x19\x03\x00\x0cx\x19@\xa7D\xda\nv\xf4\x8c\x01\x00\x1c\x00s\x00\x87\x00\x1f\x00>\x00\xbe\x00\xfc\x00'),
                            bytearray(b'\x90\x8e\x0c<\xb0p\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00~\x00\xfc\x00\xf0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=356, y=121),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x04\n\x13/\x0f?7l\\\x00\x00\x00\x00\x00\x00\x07\x00\x1c\x000\x00@\x00\x83\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\xc0\xe0`\xe0\xe0``\x00\x00\x00\x00\x00\x00\xc0\x000\x00\x18\x00\x18\x00\x9c\x00'),
                            bytearray(b'\xd1\xb0\xa3`L\xc3\xb0\x8f@8\x8cc?\x9fP\xd0\x0f\x00\x1f\x00?\x00\x7f\x00\xff\x00\xff\x00\xff\x00\xd0\x00'),
                            bytearray(b'\x10\x08 \x18\x0c\xf0\x1c\xe4H8\xc0\xc0\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xc0\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=369),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x04\n\x13/\x0f?7l\\\x00\x00\x00\x00\x00\x00\x07\x00\x1c\x000\x00@\x00\x83\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\xc0\xe0`\xe0\xe0``\x00\x00\x00\x00\x00\x00\xc0\x000\x00\x18\x00\x18\x00\x9c\x00'),
                            bytearray(b'\xd1\xb0\xa3`L\xc3\xb0\x8f@8\x8cc?\x9fP\xd0\x0f\x00\x1f\x00?\x00\x7f\x00\xff\x00\xff\x00\xff\x00\xd0\x00'),
                            bytearray(b'\x10\x08 \x18\x0c\xf0\x1c\xe4H8\xc0\xc0\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xc0\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'xx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=344, y=145),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x03\x02\x06\x05\n\x06\x04\x1c21$#\x01\x00\x02\x00\x04\x00\x08\x00\x11\x00#\x00O\x00\xdf\x00'),
                            bytearray(b'\x00\x00\x19\x03\x00\x0cx\x19@\xa7D\xda\nv\xf4\x8c\x01\x00\x1c\x00s\x00\x87\x00\x1f\x00>\x00\xbe\x00\xfc\x00'),
                            bytearray(b'\x90\x8e\x0c<\xb0p\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00~\x00\xfc\x00\xf0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=344, y=129),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x04\n\x13/\x0f?7l\\\x00\x00\x00\x00\x00\x00\x07\x00\x1c\x000\x00@\x00\x83\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00@\xc0\xe0`\xe0\xe0``\x00\x00\x00\x00\x00\x00\xc0\x000\x00\x18\x00\x18\x00\x9c\x00'),
                            bytearray(b'\xd1\xb0\xa3`L\xc3\xb0\x8f@8\x8cc?\x9fP\xd0\x0f\x00\x1f\x00?\x00\x7f\x00\xff\x00\xff\x00\xff\x00\xd0\x00'),
                            bytearray(b'\x10\x08 \x18\x0c\xf0\x1c\xe4H8\xc0\xc0\x00\x00\x00\x00\xfc\x00\xfc\x00\xfc\x00\xfc\x00\xf8\x00\xc0\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=360, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'xx\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00x\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=103, y=390),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x03\x02\x06\x05\n\x06\x04\x1c21$#\x01\x00\x02\x00\x04\x00\x08\x00\x11\x00#\x00O\x00\xdf\x00'),
                            bytearray(b'\x00\x00\x19\x03\x00\x0cx\x19@\xa7D\xda\nv\xf4\x8c\x01\x00\x1c\x00s\x00\x87\x00\x1f\x00>\x00\xbe\x00\xfc\x00'),
                            bytearray(b'\x90\x8e\x0c<\xb0p\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00~\x00\xfc\x00\xf0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=359, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=365),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=365),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x02\t\x01\x1ao~~\x0f?>\x06\x07\x01\x01\x07\x00\x0f\x00\x1d\x00\x19\x06}\x0e?<\x07\x06\x01\x01'),
                            bytearray(b'\x80\x80 \xe0\xf88\xfc|\x1c\xfc\xfc\xdc\xb8\xf8\xf0\xf0\x80\x00\xe0\x00\xf8\x18\xfc\x1c\xfc\x0c<\x0cx\x18\xf0\xf0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=124),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00@\x00\xa0\xe0P\xf0(h\x94\xb4\xc0\x00\x00\x80\x00\xc0\x00`\x000\x00\x18\x00\x0c\x00\x0c\x00'),
                            None,
                            bytearray(b'\x88\xfa|j\x1c\x02<\x02\x82\x0e\x82\x1eD\xbc\x08\xf8\x06\x00\x96\x00\xfe\x00\xfe\x00\xf6\x08\xe6\x18\xc48\x08\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x02\x04\x05\n\x0c\x14\x080\x10 \x00\x00\x00\x00\x03\x00\x07\x00\r\x00\x1b\x00?\x00?\x00'),
                            bytearray(b"\x14b\x19\xe0\x99a\xf5\x06\xc5\x06&\'\xb1\xd9,\xdc~\x00\xff\x00\xfe\x00\xf8\x00\xf8\x00\xd8\x00\x06\x00\x03\x00"),
                            bytearray(b"\x10 \x10 \x0c0\'<0?\x19\x1e\x06\x07\x00\x00?\x00?\x003\x047\x0c?\x00\x1f\x03\x07\x01\x00\x00"),
                            bytearray(b'\xe8\x98\x90\xf0\xc0\xe0\x00\x00\x81\x00&\xd9J?\xe4\xff\x07\x00\x0f\x00\x1f\x00\xff\x00\xff\x00\xf9\x02\xfb\xc6\xfe\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=117),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80@\x00 \xa0\x08 $@rPj FTb\xc0\x00\xe0\x00\xf8\x00\xdc\x00\x8e\x00\x86\x00\x9e\x00\x8e\x00'),
                            None,
                            bytearray(b'4",:04\xf0\x94\xec\x84\xe0\x9c\x08x0\xf0\xce\x00\xc6\x00\xcc\x00l\x00|\x00`\x1c\x88p0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\r\t\x11\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0e\x00\x1e\x00'),
                            bytearray(b'\x01\x06\t\x16\x1d"3@\x08\x8e\n\x0e\x14,\xf4\xcc\x07\x00\x1f\x00?\x00\x7f\x00\xf1\x00\xf1\x00\xc3\x00\x03\x00'),
                            bytearray(b'\x00\x00\x01 .\x00\x17,\x10\x1f\r\x0e\x06\x07\x00\x00\x1f\x00?\x003\x047\x0c\x1f\x00\x0f\x01\x07\x01\x00\x00'),
                            bytearray(b'\x98\xa8\x10\x10\x80\x00\xf8\x009\xc0\xc78C>\xf7\xf8G\x00\xef\x00\xff\x00\xff\x00\xff\x00\xf9\xc2\xfb\xe6\xbf@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=117),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xa0\xa0P\xe0\xa0Pp00\x04\x04\x1a\x02\x80\x00`\x000\x00\x10\x00\x88\x00\xc8\x00\xfc\x00\xfe\x00'),
                            None,
                            bytearray(b'*\x12\n2\x96f\x0c\x0c\xf0\xf0\x00\x00\x00\x00\x00\x00\xfe\x00\xfe\x00\xfe\x00\xfc\x00\xf0\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x01\x02\x02\x04\x05\x01\x05\t\n\x03\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x06\x00\x0e\x00\x0c\x00'),
                            bytearray(b'\x07\x18c\x03\xc9\x01\x00\x0c\x90\xf4H\xb8\xea\x18\xda8\x1f\x00|\x00\xfe\x00\xff\x00\x0f\x00\x07\x00\x07\x00\x07\x00'),
                            bytearray(b'\x01\x12\x16\x05\t/*\x0e.\x0f\x129\x14\x18\x0f\x0f\x1c\x00\x18\x000\x001\x001\x10?\x0e\x1f\x00\x0f\x00'),
                            bytearray(b'\xb2t\xc2\xcc\x8e\x94\x1e<@\x8f\x17\x8f\x9c|\xf0\xf0\x0f\x00?\x00w\x04\xff\x0c\xff\x00\xff\x00\xfc\x00\xf0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=117),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=10, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=10, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=10, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=10, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=8, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=4, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=23),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=0),
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
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=26),
                        AnimationSequenceFrame(duration=8, mold_id=27),
                        AnimationSequenceFrame(duration=6, mold_id=26),
                        AnimationSequenceFrame(duration=8, mold_id=28),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL083_AMEBOID,
    palette_offset=0,
    unknown_num=0
)
