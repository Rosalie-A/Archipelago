# SPR0716_DRILL_BIT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL230_MACHINE_MADE_DRILL_BIT
sprite = CompleteSprite(
    animation=AnimationPack(123, length=682, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x00\x01\x00\x01\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x02\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00 \x00L\x04\x1c\xe2\x10\xee\x01\xff\x81\x7f\x00\x10\x10\x088\x00p\x04"\x00"\x00\xa0\x01N\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\x000P`\x90\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x100\x000\x10p0'),
                            bytearray(b'\x01\x02\x00\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xcf0\xf7Q~\xc7\xd9\xcfO]wGvB\x1e\x04qQ\x18Q\x01!#\xf1k7]#=C-3'),
                            bytearray(b' \xa0\x148\xc0\xb8\x80\xf0\xc0\xe0\xc0\xf0`p\xc0\xf0\x80\xa0,\x14\xf8\xd8\xf0\xd0\xe0\xe0\xf0\xf0\xf0\xf0\xf0\xf0'),
                            None,
                            bytearray(b'!\x07\x00\x00\x0b\x01\x03\x02\x03\x02\x01\x00\x01\x00\x01\x01\x19?\x1f\x1f\x0f\x0f\x01\x02\x03\x00\x01\x00\x01\x00\x00\x01'),
                            bytearray(b'\xe0\xe0\xe0\xf0`\xf0`0`P@p@p\xc88\xe0\xe0\xf0\xf0\xf0\xf0\xd00\xf00\xb0p\xb0p\xf8x'),
                            None,
                            bytearray(b'\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x00\x00\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x00\x00'),
                            bytearray(b'\xe0\x08\x00\x00\x00\x00\x80\x18\x80\x00\xf84\xdf\x07v\xc6\xf0\xf8\xf8\xf8\xf8\xf8`\xf8\x10 L4g\x07\x8e\xc6'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00'),
                            bytearray(b"\x00\x00\x00\x00\x90\x80\xa6\x82\x0e\xf1\x08\xf7\x80\x7f\xc0?\x00\x08\x08\x04\x1c\x008\x02\x91\x00\x11\x00P\x00\'\x00"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x08\x08\x00\x18\xa8\xb0\xc8\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x18\x00\x18\x888\x98'),
                            bytearray(b'\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b"\xe7\x18{\xa8?\xe3lg\'.;#;!\x0f\x028(\x0c(\x80\x10\x11x5\x1b.\x11\x1e!\x16\x19"),
                            bytearray(b'\x90P\x8a\x9c`\xdc\xc0\xf8\xe0\xf0\xe0\xf808`x\xc0\xd0\x16\x8a\xfc\xec\xf8\xe8\xf0\xf0\xf8\xf8\xf8\xf8\xf8\xf8'),
                            None,
                            bytearray(b'\x10\x03\x00\x00\x05\x00\x01\x01\x03\x02\x02\x00\x02\x00\x03\x02\x0c\x1f\x0f\x0f\x07\x07\x00\x01\x03\x00\x03\x00\x03\x00\x01\x02'),
                            bytearray(b'\xf0\xf0px\xb0\xf8\xa08`P\x80\xe0\x80\xe0\x90p\xf0\xf0\xf8\xf8\xf8\xf8\xd88\xf00`\xe0`\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x03\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00'),
                            bytearray(b'\xc0\x10\x00\x00\x00\x00\x80\x18\x10\x10pX\xbe\x0e\xec\x8c\xe0\xf0\xf8\xf8\xf8\xf8`\xf8 \x10(\xd8\xce\x0e\x1c\x8c'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x02\x02\x02\x00\x03\x00\x03\x02\x01\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x05\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00@\x00\x98\x088\xc4 \xdc\x02\xfe\x03\xff\x00  \x10p\x00\xe0\x08D\x00D\x00@\x02\x9c\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00  \x00`\xa0\xc0 \xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00 `\x00` \xe0`'),
                            bytearray(b'\x03\x04\x01\x06\x00\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x02\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x9ea\xee\xa2\xfd\x8f\xb3\x9f\x9f\xbb\xef\x8f\xec\x84=\t\xe3\xa30\xa2\x03CG\xe3\xd7o\xbbG{\x87[g'),
                            bytearray(b'@@(p\x80p\x00\xe0\x80\xc0\x80\xe0\xc0\xe0\x80\xe0\x00@X(\xf0\xb0\xe0\xa0\xc0\xc0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                            bytearray(b'C\x0f\x01\x01\x16\x03\x06\x04\x03\x02\x00\x00\x00\x00\x01\x013\x7f??\x1f\x1f\x03\x04\x03\x00\x00\x00\x00\x00\x00\x01'),
                            bytearray(b'\xc0\xc0\xc0\xe0\xc0\xe0\xc0``P\xa08\xa08\xc88\xc0\xc0\xe0\xe0\xe0\xe0\xa0`\xf00\xd88\xd88\xf8x'),
                            None,
                            bytearray(b'\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x02\x00\x01\x04\x00\x01\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x03\x00\x06\x04\x01\x01'),
                            bytearray(b'\xe0\x08\x00\x00\x00\x00\x80\x18\x90\x10\xbe\x0e\xc6F\x00\x00\xf0\xf8\xf8\xf8\xf8\xf8`\xf8\x80\x10\xb6\x0e\xbeF\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x01\x01\x01\x01\x05\x05\r\t\x079Gy_\tcy\x00\x01\x03\x00\x03\x04\x07\x0c/\x00?H\x7fH\x7fH'),
                            bytearray(b'\x00\x00\x80\x00\x80\x00\xc0\x00\xc0\xfc\xf8\xfc\xc4\x80\x80\x88\x00\x00\x80\x80\x80\x80\xc0\x80<\xc0\x04\xf8D\xc4\x08\x80'),
                            None,
                            bytearray(b"G\x7f\'=\x06?\x05\x1a\x01\x1e\t\x0e\x0f\x0f\x06\x06zu\x1e1\x1d3\x1f\x17\x1f\x17\x0f\x0f\x0f\x0f\x07\x07"),
                            bytearray(b'\x88\x8f\x81@@\xc0\xe0@\xc8\xe0\x80\x80\x00\x008H\x07\x88\xc1\xc1\x80\xc0\xa0`\xb0xx\xf8\xf8\xf8\x90\xe8'),
                            None,
                            bytearray(b'\x06\x06\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x88x\xc0\\\xc4\x1cx\x1ct\x0c4<\x14<\x14P\x88\xc8\x80\xa8\xc4lplx<8(4< '),
                            None,
                            None,
                            bytearray(b'\x1c0\x02 \x02 \x00&\x0c\x004\x00/\x07\\\x0c8$<><><>\x00\x00>\x04[\x07|\x0c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x02\x02\x03\x02\x0b\n\x1b\x12\x0fs\x8f\xf3\xbf\x13\xc7\xf3\x00\x02\x07\x01\x07\t\x0f\x19^\x01~\x91\xfe\x91\xfe\x91'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x80\xf8\xf0\xf8\x88\x00\x00\x10\x00\x00\x00\x00\x00\x00\x80\x00x\x80\x08\xf0\x88\x88\x10\x00'),
                            None,
                            bytearray(b'\x8f\xffOz\x0c\x7f\x0b4\x03=\x13\x1d\x1e\x1e\x06\x06\xf4\xeb=c;g?.?.\x1e\x1f\x1f\x1f\x07\x07'),
                            bytearray(b'\x10\x1e\x02\x80\x80\x80\xc0\x80\x90\xc0\x00\x00\x00\x008H\x0e\x10\x82\x82\x00\x80@\xc0`\xf0\xf0\xf0\xf0\xf0\x90\xe8'),
                            None,
                            bytearray(b'\x06\x06\x02\x07\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x07\x07\x07\x07\x01\x01\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x88\xf0\x80\xb0\x80p\xe0p\xf00\xd0x(x(P\x88\x90\x00P\x80\xb0\xc0\xb0\xc0\xf0\xe0Phx@'),
                            None,
                            None,
                            bytearray(b'\x1c0\x02 \x02 \x00&r\x00J\x008\x08\x18\x188$<><><>j\x00\xbb\x08s\x08\x18\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x02\x06\x04\x03\x1c#</\x041<\x00\x00\x01\x00\x01\x02\x03\x06\x17\x00\x1f$?$?$'),
                            bytearray(b'\x80\x80\xc0\x80\xc0\x80\xe0\x80\xe0\xfe\xfc\xfe\xe2\xc0\xc0\xc4\x00\x80\xc0@\xc0@\xe0@\x9e`\x82|\xa2b\x84@'),
                            None,
                            bytearray(b'#?\x13\x1e\x03\x1f\x02\r\x00\x0f\x04\x07\x07\x07\x06\x06=:\x0f\x18\x0e\x19\x0f\x0b\x0f\x0b\x07\x07\x07\x07\x07\x07'),
                            bytearray(b'\xc4\xc7\xc0\xa0 \xe0\xf0 \xe4p\xc0@\x80\x808H\x03\xc4`\xe0\xc0\xe0\xd0\xb0\xd8\xbc\xbc\xfc\xfc\xfc\x90\xe8'),
                            bytearray(b'\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x06\x06\x03\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'h\x88|\xc4.b\x0e<\x0e:\x06\x1a\x1e\n<\x14P\x88\xc8\x84Tb686<\x1e\x1c\x14\x1a< '),
                            None,
                            None,
                            bytearray(b'\x1c0\x02 \x02 \x00&\x02\x02\x06\x02\x15\x11\x1b\x118$<><><>\x04\x02\x04\x02\x0b\x11\x1f\x11'),
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=98),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=98),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=365),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=375),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=366),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=375),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=98),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=365),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=372),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=363),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=372),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x03\x00\x06\x00\x06\x18B\x1c \x1e\x00\x04\x04\x02\x0e\x00\r\x00\x19\x00\t\x00q@\x03\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x100\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xa0\x10`\x80'),
                            bytearray(b'\x04;\x1c3\x0f\x0f\t\x0e\x07;\r\x01\r\x00\x0f\t\x19\x101\x10\x10\x11sq\x069\x0f\x00\x0f\x00\x07\x08'),
                            bytearray(b'P\xe0\x90\xe0\x80`\xe0`\xe0`\xe0\xe0\x80\x80\x00\x00\xb0\x10p0\xe0\x80\xe0\xe0\xe0\xe0`\xe0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=96),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=362),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=371),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=362),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=370),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=99),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=102),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'?\x01?\x00\x19\x18\x19\x18\t\x08\x05\x01\x07\x05\x07\x03>??8\x0f\x10\x1f\x00\x0f\x00\x07\x00\x02\x05\x04\x07'),
                            bytearray(b'\xc0\xb0\xc0\xb0\xc0p\xc0\xb0\x80\xf0\x80\xf0\x80\xf0\xc0\xb0p\xf0p\xf0\xb0p\xf0pp\xf0p\xf0p\xf0p\xf0'),
                            bytearray(b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf0\x10\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'?\x01?\x00\x19\x18\x19\x18\t\x08\x05\x01\x07\x05\x07\x03>??8\x0f\x10\x1f\x00\x0f\x00\x07\x00\x02\x05\x04\x07'),
                            bytearray(b'\xc0\xb0\xc0\xb0\xc0p\xc0\xb0\x80\xf0\x80\xf0\x80\xf0\xc0\xb0p\xf0p\xf0\xb0p\xf0pp\xf0p\xf0p\xf0p\xf0'),
                            bytearray(b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf0\x10\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x04\x00\x01\x00\x01\x00\x02\x01\x00\'\x00?\x00\x02\x02\x01\x07\x00\x06\x00\x0e\x00\x0c\x00\x1c\x00\r\x00"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x00\x80@\x08p\x18\xe0\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00@\x00\xd8\x08h\x08'),
                            bytearray(b'\x03\xbc\x17h\x1cw\x1e\x1b\x0f\t\x0e\x08\x0e\x08\x07\x04\x14\x00\x18\x10h\x18\x04\x18\x0f\x00\x0f\x00\x07\x08\x03\x04'),
                            bytearray(b'\x10\xe0\xf0@\xa0\x8c\x00\xb8\x80\xe0\xe0\xe0\xc0\xc0\x80\x80\xe0@@@\\|Hx\x00\xe0 \xe0\x80@\x80\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'?\x01?\x00\x19\x18\x19\x18\t\x08\x05\x01\x07\x05\x07\x03>??8\x0f\x10\x1f\x00\x0f\x00\x07\x00\x02\x05\x04\x07'),
                            bytearray(b'\xc0\xb0\xc0\xb0\xc0p\xc0\xb0\x80\xf0\x80\xf0\x80\xf0\xc0\xb0p\xf0p\xf0\xb0p\xf0pp\xf0p\xf0p\xf0p\xf0'),
                            bytearray(b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf0\x10\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x01\x01\x03\x01\x03\x01\x03\x03\x07\x03\x07?\x1f?\'\x03\x00\x01\x03\x02\x03\x02\x01\x02\x05\x029\x06!\x1e%&"),
                            bytearray(b'\x00\x00\x00\x00@@` \xc08\xc4<\xf4 \x8c<\x00\x00\x80\x00\x80@\xc0`\xe8\x00\xf8$\xfc$\xfc$'),
                            bytearray(b'\x07\x13\x17\xf1\x80\x07\x07\x00\x07\x03\x03\x07\x00\x00\x00\x00\x14\x07\xe6\x17\x87\x87\x07\x06\x05\x06\x04\x07\x00\x00\x00\x00'),
                            bytearray(b'\xc4\xfc\xc8x\xc0\xf8\xa0X\x80x\x90p\xf0\xf0``\xbc\\\xf0\x18p\x98\xf8\xe8\xf8\xe8\xf0\xf0\xf0\xf0``'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'?\x01?\x00\x19\x18\x19\x18\t\x08\x05\x01\x07\x05\x07\x03>??8\x0f\x10\x1f\x00\x0f\x00\x07\x00\x02\x05\x04\x07'),
                            bytearray(b'\xc0\xb0\xc0\xb0\xc0p\xc0\xb0\x80\xf0\x80\xf0\x80\xf0\xc0\xb0p\xf0p\xf0\xb0p\xf0pp\xf0p\xf0p\xf0p\xf0'),
                            bytearray(b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf0\x10\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x03\x00\x06\x00\x06\x18B\x1c \x1e\x00\x04\x04\x02\x0e\x00\r\x00\x19\x00\t\x00q@\x03\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x100\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xa0\x10`\x80'),
                            bytearray(b'\x04;\x1c3\x0f\x0f\t\x0e\x07;\r\x01\r\x00\x0f\t\x19\x101\x10\x10\x11sq\x069\x0f\x00\x0f\x00\x07\x08'),
                            bytearray(b'P\xe0\x90\xe0\x80`\xe0`\xe0`\xe0\xe0\x80\x80\x00\x00\xb0\x10p0\xe0\x80\xe0\xe0\xe0\xe0`\xe0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=103),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'?\x01?\x00\x19\x18\x19\x18\t\x08\x05\x01\x07\x05\x07\x03>??8\x0f\x10\x1f\x00\x0f\x00\x07\x00\x02\x05\x04\x07'),
                            bytearray(b'\xc0\xb0\xc0\xb0\xc0p\xc0\xb0\x80\xf0\x80\xf0\x80\xf0\xc0\xb0p\xf0p\xf0\xb0p\xf0pp\xf0p\xf0p\xf0p\xf0'),
                            bytearray(b'\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf0\x10\xf00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0\xf0\xf0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=351),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=365),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=369),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x00\x03\x00\x06\x00\x06\x18B\x1c \x1e\x00\x04\x04\x02\x0e\x00\r\x00\x19\x00\t\x00q@\x03\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x100\x80\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xa0\x10`\x80'),
                            bytearray(b'\x04;\x1c3\x0f\x0f\t\x0e\x07;\r\x01\r\x00\x0f\t\x19\x101\x10\x10\x11sq\x069\x0f\x00\x0f\x00\x07\x08'),
                            bytearray(b'P\xe0\x90\xe0\x80`\xe0`\xe0`\xe0\xe0\x80\x80\x00\x00\xb0\x10p0\xe0\x80\xe0\xe0\xe0\xe0`\xe0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=96),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=365),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=369),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x02\x03\x02\x07\x05\t\t\x11\x11\x03 \x03 \x00\x01\x01\x02\x03\x00\x07\x00\x0e\x01\x1e\x01?\x01?\x01'),
                            bytearray(b'\xe0 \xa0 \xa0\xb0\xd0\xf0\xf0\xd0\xd0\xf0\xd8\xf8\xf8\xf8\xc0 \xc0 \xd00\xb0p0\xf00\xf08\xf8\x18\xf8'),
                            bytearray(b'\x13"\x8b\xa2_\xc4\\G\x1c\x07\x1c\x17\x1c\x12\x0c\x00\r\x035\x03\x83\x07\x03\x07\x13\x07\x0b\x17\x0e\x16\x0c\x04'),
                            bytearray(b'\xe0X\xf0\x1c\xcc\x10 \xf8\x18\x98\x00\x00\x00\x00\x00\x00\xb8\xe0\xec\xe4\xdc\xcc\xd8\xc0\x80\x88\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=105),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=363),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=369),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x02\x03\x02\x07\x05\t\t\x11\x11\x03 \x03 \x00\x01\x01\x02\x03\x00\x07\x00\x0e\x01\x1e\x01?\x01?\x01'),
                            bytearray(b'\xe0 \xa0 \xa0\xb0\xd0\xf0\xf0\xd0\xd0\xf0\xd8\xf8\xf8\xf8\xc0 \xc0 \xd00\xb0p0\xf00\xf08\xf8\x18\xf8'),
                            bytearray(b'\x13"\x8b\xa2_\xc4\\G\x1c\x07\x1c\x17\x1c\x12\x0c\x00\r\x035\x03\x83\x07\x03\x07\x13\x07\x0b\x17\x0e\x16\x0c\x04'),
                            bytearray(b'\xe0X\xf0\x1c\xcc\x10 \xf8\x18\x98\x00\x00\x00\x00\x00\x00\xb8\xe0\xec\xe4\xdc\xcc\xd8\xc0\x80\x88\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=365, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=380, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=98),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=366),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00H@SA\x07x\x04{@?\xe0\x1f\x00\x04\x04\x02\x0e\x00\x1c\x01H\x00\x08\x00\xa8\x00\x13\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x84\x00\x8cT\xd8d\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x80\x04\x8c\x00\x0cD\x9cL'),
                            bytearray(b's\x8c=\xd4\x1fq63\x13\x17\x1d\x11\x1d\x10\x0f\t\x1c\x14\x86\x14@\x08\x08<\x1a\r\x17\x08\x0f\x10\x07\x08'),
                            bytearray(b'\xc8(\xc5N\xb0\xee`\xfc\xf0p\xf0\xf0\x80\x80\x00\x00`h\x0bE~v\xfct\xf0\xf0p\xf0\x00\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=353),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x03\x00\x04\x00\x00\x00\x00\x04\x00\x00\x00\x01\x00\x00\x00\x00\x03\x03\x07\x07\x07\x07\x07\x03\x07\x03\x03\x01\x01\x00\x00'),
                            bytearray(b'8\xfc<~\x0c\x1e\x18><\xfe\x1c\x1c\x0c|\x00\x00<\xfc\xbe\xfe\xee\xfe\xde\xfe>\xfe\xfc\xfc\x9c\xfc\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=366),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x02@\x00\x00\x00 \x06\x00\x00\x00\x00\x00\x00\x00\x00\x04\x06>~>>\x18>\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=379, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'~\x05~\x056#6%\x14\x07\x14\x07\x1c\x17\x1e\r{\x7f{g\x1d#?\x03\x1b\x07\x1b\x07\x0b\x17\x13\x1f'),
                            None,
                            bytearray(b'\x0f\x01\x0f\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0f\x0f\x0f\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x13\x03\x11\x01?\x06\x1b@\x0e\x18\x00\x00\x00\x00\x00\x00\x11\x03\x03\x05\t\x06l@\x11\x18'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\xe0\xe0\xc0\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=122),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=10, mold_id=20),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=21),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=22),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=21),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=22),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL230_MACHINE_MADE_DRILL_BIT,
    palette_offset=0,
    unknown_num=8
)
