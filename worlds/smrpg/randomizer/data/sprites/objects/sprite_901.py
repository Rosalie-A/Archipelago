# SPR0901_PARASOL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL559_PARASOL
sprite = CompleteSprite(
    animation=AnimationPack(393, length=260, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=3, length=17, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x02\x06\x04'),
                            bytearray(b'\x00\x01\x00\x01\x00\x01\x00\x07\x0e>\x7f\xff\xff\xff\xff\xff\x00\x01\x00\x01\x06\x07>9\xf1\xc0\x80\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x80\x00\x00\x00\x00\x00\x00\xe0|\xf8\xff\xe0\xff\xe0\xfb\x00\x80\x80\x00\xe0`\xfc|\x9f\x83\x07\x00\x1f\x00\x1f\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xc0@\xe0`'),
                            bytearray(b'\x03\x07\x07\x07\x07\x0f\x0e\x0f\r?\x19\x1f\x19=\x11;\x0c\x08\x08\x08\x18\x10\x11\x10\x12\x00& &\x02.\x04'),
                            bytearray(b'\xff\xff\xff\xff\x7f\xff\xfe\xff\xfe\xff\xfe\xff\xfc\xff\xfc\xff\x00\x00\x00\x00\x80\x00\x01\x00\x01\x00\x01\x00\x03\x00\x03\x00'),
                            bytearray(b'\xf0\xfc\xf8\xfc\xf8\xfd\xfc\xff\xfc\xff\xfc\xfe\xfc\xfex\xfe\x0f\x03\x07\x03\x06\x02\x02\x00\x02\x00\x03\x01\x03\x01\x87\x01'),
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x00\x98\x04\xf8\x04\xf8\x0c\xf0\x1c\xe0\xf0\xf0\xf0\xf0\xf0\xf0``\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x1b\x01\x03\x00\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x04\x06\x04\x03\x00\x03\x02\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\xfe\xf0\xfe\x00\xfc\x00\xe0\x00\x01\x00\x0f\x01\x00\x01\x00\x07\x01\x0f\x01\xff\x03\xff\x1f\xfe\xfe\x00\x00\x01\x00\x01\x01'),
                            bytearray(b'@\xfc\x00\xf8\x00\x01\x00\x03\x01\x06\x00\x10\x00\x00\x80\x00\xbf\x03\xff\x07\xfe\xfe\xfc\xfc\xf8\xf8\xe0\xe0\x80\x80\x80\x80'),
                            bytearray(b'\x18\xe0 \xc0@\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x04\x00\x04\x00\x04\x00\x03\x01\x00\x01\x00\x01\x00\x00\x00\x02\x04\x02\x04\x03\x04\x04\x03\x03\x01'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x07\x0e\x0e\r\x1d\n\x0e\x00\x01\x00\x02\x04\x04\x00\x04\x08\x08\x01\x01\x12\x12\x15\x13'),
                            None,
                            bytearray(b' \x10\x00`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x087\x10`\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=105, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x04\x06\x05\x05\x0f\x0f\xf2\xff\x00\x00\x03\x03\x00\x00\x00\x00\x03\x01\x02\x0210\x01\xc0'),
                            bytearray(b'\x00\x00\x08\x04\x06\x18\xe3\xc2\xe3\xf2\xc7\xf0\x85\xc0\x86P\x06\x00\x03\x0c\x87\x9e\x1b#\x13\x03\xa7\x07\x075\xb6&'),
                            bytearray(b'\xf9\xfa\xf0\xfe\xe0\xf8\x80\xe4\x10\x18P`\x80\xc0\x80\x00\x15\x04`\x01\xc6\x06X\x1a\xe0\xe6\xb0\x8c\x000\x80`'),
                            bytearray(b'@\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00  \x00\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=96),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x02`\x02\x08zxDQ\xd8\xdd\xdd\xdd\x1c>\x00\x1c\x12\x1c24\x06D.*#\xa2"\xa2@@\x18\x10'),
                            None,
                            bytearray(b'\x18\x00\x00\x00\x00\x10\x10\x80\x00\x10H\x00p\x00\x00\x00\x18\x18\x18\x00\x08\x10H\x90\xc8\x10\xf8Hpp\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x10\x00\x00\x10\x00\x10\x00\x00\x10\x188<0<pv\x08\x10\x08\x10\x08\x10\x18\x00\x00\x10\x00 \x08\x00\x1cH'),
                            None,
                            bytearray(b'pvpvpupwRwSrSZ\x18T\x1c\x08\x1c\x08\x8e\x8a\x8e\x88\xac\x88\xad\x8c\xa5\xa4\xea\xa3'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=84),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x03\x03\x03\x03\x0c\x0c\x1f\x1f\x07\x0f\x03\x07\x04\x02\x02\x04\x00\x00\x04\x04\x03\x0b\x00\x11\x10\x10\x04\x04\x07\x07\x02\x06'),
                            bytearray(b'\xc0\xa0\x80\x80\x80\x80\x00\x00\xc0\xa0` \xa0`\x00 p\x18`p@`\x80\xc0@\x80\xc0\xa0\x80 @@'),
                            bytearray(b'\xca\x04\x80\x08\x04\x88\x10\x80x p\x00\x00\x00\x00\x00\x02\xceD\x88T\x8cX\x90\xf8xpp\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=100),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x01\x00\x01\x02\x01\x06\x04\x0c\x0c\x1c\x1e8>x|\x00\x01\x00\x01\x00\x03\x01\x06\x02\n\x02\x10\x06 \x06B'),
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x01\x01\x03\x03\x03\x03\x03\x03\x00\x00\x00\x00\x00\x01\x00\x01\x02\x02\x00\x02\x00\x00\x00\x02'),
                            bytearray(b'\xf8\xfc\xf4\xf4\xf4\xf6\xe4\xf4\xe8\xe8\xec\xf8\xc0\xf8\x98\xf0\x16\x82\x1a\x8a(\x088\nT\x16D\x02\x18\x04H\x04'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=84),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x0c\xe0\xf0\xc0\xc0\x00\xd0\x00`\x80\xc0\x80\x00\x00\x00\xc0\xcc\\0\xb0800\xe0\x80\x00 \x80`\x00\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=104),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00%\x08a\xa4B\x08\x94\x00\x00\x00\x00\x00\x00\x00\x00\x13+\x18f=\xf9K\x80'),
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f\x7f\x7f|\xfd\xbb\xbb\xbe\xfe"\x94\x03\x03\x08\x0c!0\x06@\x82\x82DNA\x11jI'),
                            bytearray(b'O\x81\x1f\x83_\x06b\x04\x00\x01\x00\x00\x00\x00\x00\x00N\xdd|\x9c\xf9Xfa\x01\x07\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\x00\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xbf@\\@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=104),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xc0\x00\xa0\x00\xfc\x8c\xd0\x00\x00\x00\x00\x00\x00\x80\x80\x00@``\x00\x0c|<\x00\xe0\x00\xc0\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00 \x18H,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x18h'),
                            None,
                            bytearray(b'\x14k$K.M\x06\x01? \x0c\x0e\x08\x1c\x05\x00\x14p\xae`\xb3p~\x04??\x11\x11\x11\x13\x0f\n'),
                            bytearray(b'\x1e^?\x7f\x1c|\x80i\x07\x1f\xaaD\x80@\x00\x00as\xce\x80\xe3\x83\x9e\x16\x08\xe0\xaa\x11\x80?\x00?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=108),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xc0\x00\xa0\x00\xfc\x8c\xd0\x00\x00\x00\x00\x00\x00\x80\x80\x00@``\x00\x0c|<\x00\xe0\x00\xc0\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=117),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00 \x18H,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x18h'),
                            None,
                            bytearray(b'\x14k$K.M\x06\x01? \x0c\x0e\x08\x1c\x05\x00\x14p\xae`\xb3p~\x04??\x11\x11\x11\x13\x0f\n'),
                            bytearray(b'\x1e^?\x7f\x1c|\x80i\x07\x1f\xaaD\x80@\x00\x00as\xce\x80\xe3\x83\x9e\x16\x08\xe0\xaa\x11\x80?\x00?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=109),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xc0\x00\xa0\x00\xfc\x8c\xd0\x00\x00\x00\x00\x00\x00\x80\x80\x00@``\x00\x0c|<\x00\xe0\x00\xc0\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=118),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00 \x18H,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x18h'),
                            None,
                            bytearray(b'\x14k$K.M\x06\x01? \x0c\x0e\x08\x1c\x05\x00\x14p\xae`\xb3p~\x04??\x11\x11\x11\x13\x0f\n'),
                            bytearray(b'\x1e^?\x7f\x1c|\x80i\x07\x1f\xaaD\x80@\x00\x00as\xce\x80\xe3\x83\x9e\x16\x08\xe0\xaa\x11\x80?\x00?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=110),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xc0\x00\xa0\x00\xfc\x8c\xd0\x00\x00\x00\x00\x00\x00\x80\x80\x00@``\x00\x0c|<\x00\xe0\x00\xc0\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=371),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00 \x18H,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x18h'),
                            None,
                            bytearray(b'\x14k$K.M\x06\x01? \x0c\x0e\x08\x1c\x05\x00\x14p\xae`\xb3p~\x04??\x11\x11\x11\x13\x0f\n'),
                            bytearray(b'\x1e^?\x7f\x1c|\x80i\x07\x1f\xaaD\x80@\x00\x00as\xce\x80\xe3\x83\x9e\x16\x08\xe0\xaa\x11\x80?\x00?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=363),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'n\x8f\xe6\x17\xe0\x13\xa1T`\x9c\xe0\x1e\xf3\x08\xb2H0\x10H\x08\xae\x0c/\n&\x03D\x01W\x04\x96\x04'),
                            None,
                            bytearray(b'\xb0H0\xc0p\x80`\x80@\x80\xc0\x00\x80\x00\x00\x00\x94\x04\x18\x08\x18\x080\x10` @\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x03\x00?\x00?\x00?\x03<\x7f\x00\x7f\x00|\x03|\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00x\x00'),
                            bytearray(b'\x00\xff\x01\xfe\x07\xf8?\xc0\xfe\x01\xf8\x07\xc0?\x01\xfe\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x00p\x00\x80\x00\x00\x00'),
                            bytearray(b'\x00?\x00\x1f\x00\x0f\x00\x07\x03\x00\x03\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\xfc\x07\xf8\x1e\xe1\xfe\x01\xfc\x03\xf0\x0f\xc1>\x00\xe0\x00\x00\x01\x00\x00\x00\x02\x00\x0c\x000\x00\xc0\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x00@\x00 \x00\x10\x008\x00\xbc\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xe0\xe0\xf0\xc0\xfcD'),
                            None,
                            bytearray(b'\x18\x9c\x18\x9e\x18\xdd\x18\xdb\x00[\x00\x97\x04O\x0e\x1f\xe4`\xe4`\xe7#\xe7%\xff\xa5\xffi\xfb\xb1\xf1\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x07\x00\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x00\x00\x06\x06\x07\x00\x0f\x08\x08\x08\x08\x08\x00\x00\x10\x10'),
                            bytearray(b'\x00\x00\x00\xe6\x00\x00\x00\xe0\xe0\xfc\xf8\xff\xfc\xff\xfe\xff\x00\x00\x00\x00\xff\xff\xff\x1f\x1f\x03\x07\x00\x03\x00\x01\x00'),
                            bytearray(b"\x1f\x1f\x00\x00g_G\'^\x1f\x80\\\x80C\x10\x80  \x7f\x7f\x80\xb8\x98\xe0!@?\xc3<\xdco\x90"),
                            bytearray(b'\xff\xff?\x7f\x03\x87\xf0\xf8>\xff\x00\x00\x00\xff\x00\x00\x00\x00\xc0\x80\xfcx\x0f\x07\xc1\x00\xff\xff\x00\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=102),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'n\x8f\xe6\x17\xe0\x13\xa1T`\x9c\xe0\x1e\xf3\x08\xb2H0\x10H\x08\xae\x0c/\n&\x03D\x01W\x04\x96\x04'),
                            None,
                            bytearray(b'\xb0H0\xc0p\x80`\x80@\x80\xc0\x00\x80\x00\x00\x00\x94\x04\x18\x08\x18\x080\x10` @\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=370),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x03\x00?\x00?\x00?\x03<\x7f\x00\x7f\x00|\x03|\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00x\x00'),
                            bytearray(b'\x00\xff\x01\xfe\x07\xf8?\xc0\xfe\x01\xf8\x07\xc0?\x01\xfe\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x00p\x00\x80\x00\x00\x00'),
                            bytearray(b'\x00?\x00\x1f\x00\x0f\x00\x07\x03\x00\x03\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\xfc\x07\xf8\x1e\xe1\xfe\x01\xfc\x03\xf0\x0f\xc1>\x00\xe0\x00\x00\x01\x00\x00\x00\x02\x00\x0c\x000\x00\xc0\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x00@\x00 \x00\x10\x008\x00\xbc\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xe0\xe0\xf0\xc0\xfcD'),
                            None,
                            bytearray(b'\x18\x9c\x18\x9e\x18\xdd\x18\xdb\x00[\x00\x97\x04O\x0e\x1f\xe4`\xe4`\xe7#\xe7%\xff\xa5\xffi\xfb\xb1\xf1\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x07\x00\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x00\x00\x06\x06\x07\x00\x0f\x08\x08\x08\x08\x08\x00\x00\x10\x10'),
                            bytearray(b'\x00\x00\x00\xe6\x00\x00\x00\xe0\xe0\xfc\xf8\xff\xfc\xff\xfe\xff\x00\x00\x00\x00\xff\xff\xff\x1f\x1f\x03\x07\x00\x03\x00\x01\x00'),
                            bytearray(b"\x1f\x1f\x00\x00g_G\'^\x1f\x80\\\x80C\x10\x80  \x7f\x7f\x80\xb8\x98\xe0!@?\xc3<\xdco\x90"),
                            bytearray(b'\xff\xff?\x7f\x03\x87\xf0\xf8>\xff\x00\x00\x00\xff\x00\x00\x00\x00\xc0\x80\xfcx\x0f\x07\xc1\x00\xff\xff\x00\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=354),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xa8\xec|x\x0e\x04\x06\x00\x06\x02\x02(\x14\x00\x00\x00T\x10\x06\x00\x0e\x0e\x06\x06\x06\x06\x16*<\x14\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=98),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x10\x08\x00\x07\x07\x0e\x0f\x0b\x0f\x0f\x0f\x0c\r\x00\x00\x00\x10\x18\x08\x08\x00\x05\x00\x06\x00\x00\x00\x03\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80\x80\xa0\x00\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0@@@\xc0@'),
                            bytearray(b'\x00\x0f\x00\x02\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x07\x05\x07\x07\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10@\x00\xf0\xb0@ \x84\x80\n\x00\x00z\x01\x80\xd4\xb0\xa0\x00\x00\xb0\x00,X\x86t\x03\xff\xfa\x84**'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=82),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xc0\x00\xa0\x00\xfc\x8c\xd0\x00\x00\x00\x00\x00\x00\x80\x80\x00@``\x00\x0c|<\x00\xe0\x00\xc0\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00 \x18H,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x18h'),
                            None,
                            bytearray(b'\x14k$K.M\x06\x01? \x0c\x0e\x08\x1c\x05\x00\x14p\xae`\xb3p~\x04??\x11\x11\x11\x13\x0f\n'),
                            bytearray(b'\x1e^?\x7f\x1c|\x80i\x07\x1f\xaaD\x80@\x00\x00as\xce\x80\xe3\x83\x9e\x16\x08\xe0\xaa\x11\x80?\x00?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=117),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'n\x8f\xe6\x17\xe0\x13\xa1T`\x9c\xe0\x1e\xf3\x08\xb2H0\x10H\x08\xae\x0c/\n&\x03D\x01W\x04\x96\x04'),
                            None,
                            bytearray(b'\xb0H0\xc0p\x80`\x80@\x80\xc0\x00\x80\x00\x00\x00\x94\x04\x18\x08\x18\x080\x10` @\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1c\x03\x00?\x00?\x00?\x03<\x7f\x00\x7f\x00|\x03|\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00x\x00'),
                            bytearray(b'\x00\xff\x01\xfe\x07\xf8?\xc0\xfe\x01\xf8\x07\xc0?\x01\xfe\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x00p\x00\x80\x00\x00\x00'),
                            bytearray(b'\x00?\x00\x1f\x00\x0f\x00\x07\x03\x00\x03\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\xfc\x07\xf8\x1e\xe1\xfe\x01\xfc\x03\xf0\x0f\xc1>\x00\xe0\x00\x00\x01\x00\x00\x00\x02\x00\x0c\x000\x00\xc0\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x80\x00@\x00 \x00\x10\x008\x00\xbc\x00\x00\x00\x00\x00\x00\x80\x80\xc0\xc0\xe0\xe0\xf0\xc0\xfcD'),
                            None,
                            bytearray(b'\x18\x9c\x18\x9e\x18\xdd\x18\xdb\x00[\x00\x97\x04O\x0e\x1f\xe4`\xe4`\xe7#\xe7%\xff\xa5\xffi\xfb\xb1\xf1\x01'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x07\x00\x07\x07\x07\x07\x07\x0f\x0f\x0f\x0f\x00\x00\x06\x06\x07\x00\x0f\x08\x08\x08\x08\x08\x00\x00\x10\x10'),
                            bytearray(b'\x00\x00\x00\xe6\x00\x00\x00\xe0\xe0\xfc\xf8\xff\xfc\xff\xfe\xff\x00\x00\x00\x00\xff\xff\xff\x1f\x1f\x03\x07\x00\x03\x00\x01\x00'),
                            bytearray(b"\x1f\x1f\x00\x00g_G\'^\x1f\x80\\\x80C\x10\x80  \x7f\x7f\x80\xb8\x98\xe0!@?\xc3<\xdco\x90"),
                            bytearray(b'\xff\xff?\x7f\x03\x87\xf0\xf8>\xff\x00\x00\x00\xff\x00\x00\x00\x00\xc0\x80\xfcx\x0f\x07\xc1\x00\xff\xff\x00\x00\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=12),
                        AnimationSequenceFrame(duration=16, mold_id=13),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL559_PARASOL,
    palette_offset=0,
    unknown_num=0
)
