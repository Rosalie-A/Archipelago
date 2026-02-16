# SPR0720_THWOMP
#SPR0720_THWOMP

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL608_SHY_RANGER
sprite = CompleteSprite(
    animation=AnimationPack(116, length=865, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03'),
                            bytearray(b"\x00\x00\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\x00\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80"),
                            bytearray(b'\x00\x00\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe\x00\x00\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~'),
                            bytearray(b'\x03\x00\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x02\x02\x07\x07\x03\x01\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x02\x06\x01'),
                            bytearray(b'\xa5\xc0\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10\x9e\x8c\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 '),
                            bytearray(b'<\xbc<\xbc(\xb8\xac\xbc\xbc\xbcx<p>\xec~||<|(x,|||\xfc|~\xfe\xf2\xfe'),
                            bytearray(b'\x03\x07\x00\x00\x01\x01\x01\x03\x03\x00\x01\x00\x00\x00\x00\x00\x04\x07\x01\x01\x01\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b' 8\xe3\xc1\xff\x7f\xf8\x0f\xefx\xc8C;\x04\t\x02\x87\xc1c\xff?\xff\x07\xff8\x07\x07888\x08\x0c'),
                            bytearray(b'\xfc\xfa\xfc\xfa\xf6\xfe\xe7\xfe\xc1~?\xfc\xc6\x00\xe4 \xea\xf6\xfa\xf6\xfa\xfe\xff\xff?\xff\xc7?6\x0e\x0c\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03'),
                            bytearray(b"\x00\x00\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\x00\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80"),
                            bytearray(b'\x00\x00\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe\x00\x00\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~'),
                            bytearray(b'\x03\x00\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x04\x06\x0e\x0f\x03\x01\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x03\x06\r\x03'),
                            bytearray(b'\xa5\xc0\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10\x9e\x8c\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 '),
                            bytearray(b'<\xbc<\xbc(\xb8\xac\xbc\xbc\xbcx<p>\xec~||<|(x,|||\xfc|~\xfe\xf2\xfe'),
                            bytearray(b'\x06\x0f\x00\x00\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\t\x0f\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b' 8\xe3\xc1\xff\x7f\xf8\x0f/8\x08\x03\x07\x08\x03\x04\x87\xc1c\xff?\xff\x07\xff\xf8\x07\x078\x00\x00\x00\x08'),
                            bytearray(b'\xf6\xfd\xf6\xfd\xf3\xff\xe7\xfe\xc1~>\xfc\x8c\x00\xc8@\xed\xfb\xfd\xfb\xfd\xff\xff\xff?\xff\xc6>l\x1c\x188'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03'),
                            bytearray(b"\x00\x00\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\x00\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80"),
                            bytearray(b'\x00\x00\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe\x00\x00\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~'),
                            bytearray(b'\x03\x00\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x03\x03\x03\x01\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x03'),
                            bytearray(b'\xa5\xc0\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10\x9e\x8c\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 '),
                            bytearray(b'<\xbc<\xbc(\xb8\xac\xbc\xbc\xbcx8p8\xe8|||<|(x,|||\xf8xx\xf8\xf4\xfc'),
                            bytearray(b'\x00\x03\x00\x00\x01\x01\x03\x01\x07\x00\x00\x00\x03\x00\x00\x00\x03\x03\x01\x01\x01\x00\x04\x00\x00\x00\x03\x00\x03\x03\x00\x00'),
                            bytearray(b' 8\xe3\xc1\xff\x7f\xf8\x0f\xef\xb8\x18#\xf9\x02\x00\x00\x87\xc1c\xff?\xff\x07\xff8G\xe7x\xf8\xfc\x00\x00'),
                            bytearray(b'\xf8\xf4\xf8\xf4\xec\xfc\xce\xfc\xc1~?\xfc\xe4 \x00\x00\xd4\xec\xf4\xec\xf4\xfc\xfe\xfe?\xff\xc7?\x0c\x1c\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x03\x03\x03\x03\x03'),
                            bytearray(b'\x1c\x08B?\xe3~\xc7\xfc\xff\xfc\x7f\xf8\x8f\xfd\xe7\xfd\x16\x02_\x00\xbe\x01|\x03<\xc3\x88\xf7\xf1\xfe\xf9\xfe'),
                            bytearray(b'\x00\x00\xc0\xc0\xe0 \xf0\x10\xf8\x08\xf8\xc8\xfc\xc4\xf2\xde\x00\x00\x00\xc0\x00\xe0\x00\xf0\x08\xf8\xc08\xc0<\xde '),
                            bytearray(b'\x03\x01\x03\x01\x03\x01\x01\x01\x01\x01\x01\x00\x01\x01\x00\x01\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x01\x01'),
                            bytearray(b'\xf3\xff8\xff\xbf\xff\xd0\xe0\xfc\xfe\xff\xfc\xef\xff\xe7\xff\xfc\xff?\xff\xbf\xff\xf0\xff\xc7\xf8\x80\xffp\x9fX\xbf'),
                            bytearray(b'\xfc\xfc\xc8\xf8\xf8\xf08x|\xec\xf6\x0e\xfe>\xf0\xf6\x9c`8\xf8\xf8\xf80\xf8\x80|\x08\xfe\x08\xfe\x0e\xfe'),
                            bytearray(b'\x00\x01\x02\x01\x02\x01\x03\x01\x01\x00\x02\x00\x01\x00\x00\x00\x01\x01\x03\x03\x03\x03\x03\x03\x03\x01\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'\xf3\xff\xbf\xffB\xff\xfc\xe7\xbc\xf7\xe7\x7f\xff\x7f\x1e\x17<\xff\x7f\xff\xff\xff\x87\xf8\xc7\xf8\xf8\xff\x83\xfcgx'),
                            bytearray(b'\x90\xf0\xe8\xf0x\xc0<\xe8\xfc\xd8\xfc\x04\xf8\xe8`\xf0x\xf8\xf0\xf8\x80\xf8\xe0\x1c\xc0<\x00\xfc\xe0\x18\x90p'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x03\x03\x03\x03\x03'),
                            bytearray(b'\x1c\x08B?\xe3~\xc7\xfc\xff\xfc\x7f\xf8\x8f\xfd\xe7\xfd\x16\x02_\x00\xbe\x01|\x03<\xc3\x88\xf7\xf1\xfe\xf9\xfe'),
                            bytearray(b'\x00\x00\xc0\xc0\xe0 \xf0\x10\xf8\x08\xf8\xc8\xfc\xc4\xf2\xde\x00\x00\x00\xc0\x00\xe0\x00\xf0\x08\xf8\xc08\xc0<\xde '),
                            bytearray(b'\x03\x01\x03\x01\x03\x01\x01\x01\x01\x01\x01\x00\x01\x01\x00\x00\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x00\x00'),
                            bytearray(b'\xf3\xff8\xff\xbf\xff\xd0\xe0\xfc\xfe\xff\xfc\xef\xffw\xff\xfc\xff?\xff\xbf\xff\xf0\xff\xc7\xf8\x80\xffp\x9f\xa8\xdf'),
                            bytearray(b'\xfc\xfc\xc8\xf8\xf8\xf08xx\xe8\xf4\x0c\xfc<\xf8\xfc\x9c`8\xf8\xf8\xf80\xf8\x80x\x08\xfc\x08\xfc\x0c\xfc'),
                            bytearray(b'\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x02\x00\x01\x00\x00\x00\x00\x00\x01\x01\x01\x03\x07\x01\x03\x05\x03\x02\x01\x01\x00\x00'),
                            bytearray(b's\xff_\xff"\xff\xfc\xf7\xfc\xf7\xe7~\xbf\x7f\x00\x1f\x9c\xff\xbf\xff\xff\xff\xc7\xf8\x87\xf8\x98\xff\xc3\xfc\x7f\x7f'),
                            bytearray(b'\x90\xf0\xe8\xf0x\xc0<\xe8\xfc\xd8\xfc\x04\xf0\xe0\x00\xe0x\xf8\xf0\xf8\x80\xf8\xe0\x1c\xc0<\x00\xfe\xec\x12\xf8\xe4'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x03\x03\x03\x03\x03'),
                            bytearray(b'\x1c\x08B?\xe3~\xc7\xfc\xff\xfc\x7f\xf8\x8f\xfd\xe7\xfd\x16\x02_\x00\xbe\x01|\x03<\xc3\x88\xf7\xf1\xfe\xf9\xfe'),
                            bytearray(b'\x00\x00\xc0\xc0\xe0 \xf0\x10\xf8\x08\xf8\xc8\xfc\xc4\xf2\xde\x00\x00\x00\xc0\x00\xe0\x00\xf0\x08\xf8\xc08\xc0<\xde '),
                            bytearray(b'\x03\x01\x03\x01\x03\x01\x01\x01\x01\x01\x01\x00\x01\x01\x01\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x02\x03'),
                            bytearray(b'\xf3\xff8\xff\xbf\xff\xd0\xe0\xfc\xfe\xff\xfc\xef\xff\xe7\xff\xfc\xff?\xff\xbf\xff\xf0\xff\xc7\xf8\x80\xffp\x9f\xb8\x7f'),
                            bytearray(b'\xfc\xfc\xc8\xf8\xf8\xf04|v\xee\xf3\x0f\xf77\xf0\xf3\x9c`8\xf8\xf8\xf88\xfc\x88~\x0c\xff\x04\xf7\x07\xf7'),
                            bytearray(b'\x01\x03\x01\x03\x00\x03\x03\x01\x01\x02\x02\x01\x01\x00\x00\x00\x02\x03\x02\x03\x03\x03\x03\x03\x01\x03\x02\x03\x01\x01\x00\x00'),
                            bytearray(b'\xf3\xff\x7f\xff\x82\xff\xfc\xe7\xbc\xf7\xdf\x7f\xfe~\x18\x10|\xff\xff\xff\xff\xff\x87\xf8\xc7\xf8\xfe\xe1\x9f\xe0gx'),
                            bytearray(b'\x90\xf0\xe8\xf0x\xc0<\xe8\xf8\xdc\xf8\x98\xc0\xf0@px\xf8\xf0\xf8\x80\xf8\xe0\x1c\xc4<\x00\xf80\xf0\xb0p'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=118),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=374),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x00\x02\x03\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x03\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x00\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfe\x01\xff\x00\xbdB\xbf\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x80\x80"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xadD\xed\x04\xff\x00\xff\x00\xfe!7\x89\x0c0 8\x8e\x9e\x0e\x1e\x00\x00\x00\x00\x00\x00 `\xc3\x00\x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=373),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=373),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=371),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x1f7:6\x1e>\x0c<\x00\x00\x00\x00\x00\x00\x08\x0f!?\x16.&><<\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x01\x00\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x03\x02\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x02\x00\x02\x00\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x03\x03\x02\x02\x01\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xe9\x18\xa0\x16\xa0\t\xba\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x06\x88\xc9B\x16\xd5\x95"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xf8\x00e\x00\xb5@x\x83\xf2\r7\x89,\x10 8SU[\xcb\x8e\x84\x07\x00\x00\x00 `\xe3 \x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80@\xc0@\xc0\xc0@\xc0\xc0\xc0\xc0 \xe0p\xe0\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0\xe0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x03\x03\x03\x01\x03\x00\x03\x0f\r\x1f1?\x06\x00\x00\x00\x03\x00\x03\x02\x03\x07\x07\x17\x1f\x01\x06\x02\x01'),
                            bytearray(b'\xf9\xff\xfc\xff\xfc\xff\xf0\xff\x01\xfe\xff\x1f\xff\xff\x8e\xff\x07\xff\x03\xff\x03\xff\x0f\xff\xff\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'\x1c\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x02\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb3\x87\xbc@\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x83\x83\x80\x99\xa7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=115),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'08|\x7f>\x7f\n\x1f\x02\x07\x05\x07\x03\x01\x00\x00\x18(c\x1fA\x7f\x15\x1f\r\x0f\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=114),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x1f7:6\x1e>\x0c<\x00\x00\x00\x00\x00\x00\x08\x0f!?\x16.&><<\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=368),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x01\x00\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x03\x02\x02'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=358),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x02\x00\x02\x00\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x03\x03\x02\x02\x01\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=366),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xe9\x18\xa0\x16\xa0\t\xba\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x06\x88\xc9B\x16\xd5\x95"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xf8\x00e\x00\xb5@x\x83\xf2\r7\x89,\x10 8SU[\xcb\x8e\x84\x07\x00\x00\x00 `\xe3 \x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=358),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80@\xc0@\xc0\xc0@\xc0\xc0\xc0\xc0 \xe0p\xe0\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0\xe0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=369),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x03\x03\x03\x01\x03\x00\x03\x0f\r\x1f1?\x06\x00\x00\x00\x03\x00\x03\x02\x03\x07\x07\x17\x1f\x01\x06\x02\x01'),
                            bytearray(b'\xf9\xff\xfc\xff\xfc\xff\xf0\xff\x01\xfe\xff\x1f\xff\xff\x8e\xff\x07\xff\x03\xff\x03\xff\x0f\xff\xff\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'\x1c\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x02\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb3\x87\xbc@\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x83\x83\x80\x99\xa7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=369),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'08|\x7f>\x7f\n\x1f\x02\x07\x05\x07\x03\x01\x00\x00\x18(c\x1fA\x7f\x15\x1f\r\x0f\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=367),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x1c\x1a\xfa5\xff\xf1\xfe\xfaB\xfc\x9f~\xe3\x00r\x90\xba~\xfd\xff\xfd\xff\xfe\xfe\xbe\xfec\x9f\x1b\x07\x06\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x02\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x82\xc7x\xf0\x7f_\x00\x7f\xe7\x1f\xfb\x04\xfa\x08v\x10\xe8p\x98\xff\x0f\x7f\x7f\x7f\x1f\xff\x04\xfb\x02\x07F\x0f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x0f\t\x18\x073\x0c_`\xff\x80\x7f\x00G\x00\x00\x00\x01\x0e\x07\x18\x000\x00@@\x80\x00\x80(\x90'),
                            bytearray(b'\xf0\x90\xf8Hx\x880\xf8\xf0<\xd0<\xe4\x0c\x144\x00\xf0@\xb8\x80xH8\x0c<\x0c\x1c\x1c\x0c\xcc\x0c'),
                            bytearray(b'\xf0\x06\xf8\x0e\xf8\x06\xd0\x06\xf8\x079F\x1b$\x9a\xc5\xb98\xb89\xb89\x909\x80\x00\x00\x00B\x02b\xc2'),
                            bytearray(b'D\x14\xc4T\xc4T\xc4\x14\x044,\xc4\xe8,\x9c\x0e\xec\xcc\xe4\xec\xe4\xec\xc4\xec\x04\xcc\x1c\x0c\x0c\x1cz\x1e'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=107),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xc0\xe0\x00\x00\x80\x80\x80\xc0\xc0\x00\x80\x00\x00\x00\x00\x00 \xe0\x80\x80\x80\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"?_?_o\x7f\xe7\x7f\x83~\xfc?c\x00\'\x04Wo_o_\x7f\xff\xff\xfc\xff\xe3\xfclp08"),
                            bytearray(b'\x04\x1c\xc7\x83\xff\xfe\x1f\xf0\xf7\x1e\x13\xc2\xdc \x90@\xe1\x83\xc6\xff\xfc\xff\xe0\xff\x1c\xe0\xe0\x1c\x1c\x1c\x100'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\xc0\x80\xc0'),
                            None,
                            bytearray(b'\xc0\x00\xc0\x00@\x00@\x80\xc0\x00\x00\x80@@\xe0\xe0\xc0\x80\xc0\x80@\x80@\x00@\x00\x00\x00\x80@`\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x7ff\xbf\xff\xbf\xbe\x8f\xbd\xc6\xfeq}\x00\x00\x0b\x0c&Y\x7f\x80N\xf1\xf0\xff\xf9\xfe~~'),
                            bytearray(b'\x00\x00\xe0`\xe48\x9cb~\x81_\xa0\xfe\x00\x8dC\x00\x00@\xa0<\xc0@\x80\x80\x00\x00\x00\x00\x011\x01'),
                            bytearray(b'<=<=\x14\x1d5===\x1e<\x0e|7~>><>\x14\x1e4>>>?>~\x7fO\x7f'),
                            bytearray(b'\xa5\x03\xb5"\xb4"\xb6\x01\x87HO\xb4\xec\x914\x08y1qyqy0x00\x00\x00\x04\x06\xc7\x04'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\t\x1f\x0e?\x0f;o{\x8d\x7f@?\x1c\x00\x00\x00\x1f\x1f9?:={}\xfb\xff\x7f\x7f\x1c\x1f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\xe4\xf2\xe0\xfe\xfa\xc2\xfe\x0c\xf4\xfa\x04\xe0\x98\x00\x00\xea\xf0\xf2\xfe\xe2\xfc\xfc\xfe\xf0\xec\x02\xfa\x00\x04\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x7ff\xbf\xff\xbf\xbf\x8f\xbf\xc7\xffq\x7f\x00\x00\x0b\x0c&Y\x7f\x80O\xf0\xf3\xfc\xf8\xff~\x7f'),
                            bytearray(b'\x00\x00\xe0`\xe48\xacR\xe6\x98\xce1\xd2\xe1Xa\x00\x00@\xa0<\xc0P\xa0\x80`\x00\xc0\x0c\x80\x8e\x8c'),
                            bytearray(b'??\x1f\x1f\x13\x1f\x13\x1f\x1f\x1f\x1f\x1f\x07\x1f\x0b\x1f??\x1f\x1f\x13\x1f\x13\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f\x1f'),
                            bytearray(b'\x0ci\x0ci\x0ca\x10#\x10/\xa1\x9e\x8b\x95\xce\x80\x9c\x8e\x1c\x8e\x1c\x8eL\x8c\xc0\x80\xc0\x80\xa1\xc1\xf1\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x13\x1f/\x1f<\x07x/~7\x7fA?/\x0c\x1f<?\x1f?\x03?\x0fp\x07x\x00\x7f\x0f0\x13\x1c'),
                            bytearray(b'\x9e\xff\xfa\xff\x84\xff\x7f\xcf{\xde\xce\xfc\xff\xfc\xf0\xd0y\xff\xfd\xff\xff\xff\xc3?\xc7??\xfe\x83\x7f\xcc<'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80'),
                            None,
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=107),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x07\x0f\x08\x1f\x10? ?&\x7fG\x9f\xf7\x00\x00\x01\x06\x00\x0f\x00\x1f ?\x069\x07x\xf7\x08'),
                            bytearray(b'p \x84\xf8\x8e\xfc\xc7~\xfe~\xfc>\xe3\x7f\xcf\x7f\xd0\x80\xf4\x00\xfa\x00}\x80y\x86#\xdf\x1f\xff?\xff'),
                            bytearray(b'\x7f\x7f&??\x1f8<|n\xdf\xe0\xff\xf9\x1f\xdfr\r9???\x18?\x03| \xff \xff\xe0\xff'),
                            bytearray(b'\x9f\xff9\xff\xfb\xff\x17\x0f\x7f\xff\xff~\xef\xff\xce\xff\x7f\xff\xf9\xff\xfb\xff\x1f\xff\xc7?\x03\xff\x1d\xf35\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=107),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\xff\x7f\x7fA\x7f\xfe\xf3\xde{\xe7<\x7f?\x0f\x0b\xfe\xff\x7f\x7f\x7f\x7f\xc3\xfc\xe3\xfc\xf8\xffA~3<'),
                            bytearray(b'\xcb\xfb\xf4\xfc<\xe4\x1e\xf4~\xec\xfe\x02\xfc\xf40\xf8?\xff\xf8\xfc\xc0\xfc\xf0\x0e\xe0\x1e\x00\xfe\xf0\x0c\xc88'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=123),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x0f\x06\x01\x1f1?#>?>?<\x07>3>\t\x00\x0f\x00\x1f\x00~A^aD{x\x7f|\x7f'),
                            bytearray(b'\xc0\x00`\xe0\xf0\x10\xf8\x08\xf8\x00\xf8`\xf8\xe8\xf0\xe8\xc0\x00\x80`\x00\xf0\x00\xf8\x00\xf8`\x98\xe0\x18\xe8\x18'),
                            bytearray(b'y?\\?_?hp~s\xff\xfc\x7f\xff_\xff~\x7f_\x7f_\x7fx\x7fC|\xb0\xcf\x90\xff\xb0\xff'),
                            bytearray(b'\xe0\xf8L\xf8\xfc\xf8\x1cx>v\xff\x07\xfb\x9f\xff\xffX\xb8\xbc\xfc\xfc\xfc\x1c\xfc\xc2>\x01\xff\x04\xff\x04\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=107),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\xe8\xf0x\xc0<\xe8\xfc\xd8\xfc\x04\xf8\xe8`\xf0x\xf8\xf0\xf8\x80\xf8\xe0\x1c\xc0<\x00\xfc\xe0\x18\x90p'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x01\x02\x01\x02\x01\x03\x01\x01\x00\x02\x00\x01\x00\x00\x00\x01\x01\x03\x03\x03\x03\x03\x03\x03\x01\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'\xf3\xff\xbf\xffB\xff\xfc\xe7\xbc\xf7\xe7\x7f\xff\x7f\x1e\x17<\xff\x7f\xff\xff\xff\x87\xf8\xc7\xf8\xf8\xff\x83\xfcgx'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\xc0\xc0\xe0 \xf0\x10\xf8\x08\xf8\xc8\xfc\xc4\xf2\xde\x00\x00\x00\xc0\x00\xe0\x00\xf0\x08\xf8\xc08\xc0<\xde '),
                            None,
                            bytearray(b'\xfc\xfc\xc8\xf8\xf8\xf08x|\xec\xf6\x0e\xfe>\xf0\xf6\x9c`8\xf8\xf8\xf80\xf8\x80|\x08\xfe\x08\xfe\x0e\xfe'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=107),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x03\x03\x03\x03\x03'),
                            bytearray(b'\x1c\x08B?\xe3~\xc7\xfc\xff\xfc\x7f\xf8\x8f\xfd\xe7\xfd\x16\x02_\x00\xbe\x01|\x03<\xc3\x88\xf7\xf1\xfe\xf9\xfe'),
                            bytearray(b'\x03\x01\x03\x01\x03\x01\x01\x01\x01\x01\x01\x00\x01\x01\x00\x01\x03\x03\x03\x03\x03\x03\x03\x03\x03\x03\x01\x01\x01\x01\x01\x01'),
                            bytearray(b'\xf3\xff8\xff\xbf\xff\xd0\xe0\xfc\xfe\xff\xfc\xef\xff\xe7\xff\xfc\xff?\xff\xbf\xff\xf0\xff\xc7\xf8\x80\xffp\x9fX\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=107),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf8p\xfc\xf0\xdc\xf6\xde\xb1\xfe\x02\xfc8\x00\x00\x00\xf8\xf8\x9c\xfc\\\xbc\xde\xbe\xdf\xff\xfe\xfe8\xf8\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=123),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b"\x07\'O\x07\x7f_C\x7f0/_ \x07\x19\x00\x00W\x0fO\x7fG??\x7f\x0f7@_\x00 \x00\x00"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x07\x06\'\x1c5Jg\x19s\x8cK\x87\x1a\x86\x00\x00\x02\x05<\x03\n\x05\x01\x06\x00\x030\x01q1"),
                            bytearray(b'\x00\x00\xe0\xf0\xfef\xfd\xff\xfd\xfd\xf1\xfd\xe3\xff\x8e\xfe\x00\x00\xd00d\x9a\xfe\x01\xf2\x0f\xcf?\x1f\xff~\xfe'),
                            bytearray(b'0\x960\x960\x86\x08\xc4\x08\xf4\x85y\xd1\xa9s\x019q8q8q21\x03\x01\x03\x01\x85\x83\x8f\x03'),
                            bytearray(b'\xfc\xfc\xf8\xf8\xc8\xf8\xc8\xf8\xf8\xf8\xf8\xf8\xe0\xf8\xd0\xf8\xfc\xfc\xf8\xf8\xc8\xf8\xc8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=107),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00D\x00\x90\x00\xa8\x00\x9a\x00l\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x1f7:6\x1e>\x0c<\x00\x00\x00\x00\x00\x00\x08\x0f!?\x16.&><<\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x01\x00\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x03\x02\x02'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xe9\x18\xa0\x16\xa0\t\xba\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x06\x88\xc9B\x16\xd5\x95"),
                            bytearray(b'\x03\x00\x02\x00\x02\x00\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x03\x03\x02\x02\x01\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x00e\x00\xb5@x\x83\xf2\r7\x89,\x10 8SU[\xcb\x8e\x84\x07\x00\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'08|\x7f>\x7f\n\x1f\x02\x07\x05\x07\x03\x01\x00\x00\x18(c\x1fA\x7f\x15\x1f\r\x0f\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=374, y=119),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00D\x00\x90\x00\xa8\x00\x9a\x00l\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=367, y=105),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x1f7:6\x1e>\x0c<\x00\x00\x00\x00\x00\x00\x08\x0f!?\x16.&><<\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=387, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=379),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x01\x00\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x03\x02\x02'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xe9\x18\xa0\x16\xa0\t\xba\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x06\x88\xc9B\x16\xd5\x95"),
                            bytearray(b'\x03\x00\x02\x00\x02\x00\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x03\x03\x02\x02\x01\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x00e\x00\xb5@x\x83\xf2\r7\x89,\x10 8SU[\xcb\x8e\x84\x07\x00\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=363),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80@\xc0@\xc0\xc0@\xc0\xc0\xc0\xc0 \xe0p\xe0\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0\xe0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0\xe0\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=390, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x03\x03\x03\x01\x03\x00\x03\x0f\r\x1f1?\x06\x00\x00\x00\x03\x00\x03\x02\x03\x07\x07\x17\x1f\x01\x06\x02\x01'),
                            bytearray(b'\xf9\xff\xfc\xff\xfc\xff\xf0\xff\x01\xfe\xff\x1f\xff\xff\x8e\xff\x07\xff\x03\xff\x03\xff\x0f\xff\xff\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'\x1c\x05\x07\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x19\x02\x07\x07\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb3\x87\xbc@\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00L\x83\x83\x80\x99\xa7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=374, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'08|\x7f>\x7f\n\x1f\x02\x07\x05\x07\x03\x01\x00\x00\x18(c\x1fA\x7f\x15\x1f\r\x0f\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=374, y=120),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00D\x00\x90\x00\xa8\x00\x9a\x00l\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=359),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=385, y=376),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=385, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x01\x00\x02\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x01\x03\x02\x02'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xe9\x18\xa0\x16\xa0\t\xba\x00\x02\x05<\x03\x02\x01\x01\x00\x00\x06\x88\xc9B\x16\xd5\x95"),
                            bytearray(b'\x03\x00\x02\x00\x02\x00\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x03\x03\x02\x02\x01\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x00e\x00\xb5@x\x83\xf2\r7\x89,\x10 8SU[\xcb\x8e\x84\x07\x00\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'08|\x7f>\x7f\n\x1f\x02\x07\x05\x07\x03\x01\x00\x00\x18(c\x1fA\x7f\x15\x1f\r\x0f\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=373, y=120),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=376),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=379),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=363),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=373),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=374),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=378),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=362),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=362),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=371),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x02\x00\x02\x03\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x03\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x00\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=369, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfe\x01\xff\x00\xbdB\xbf\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x80\x80"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xadD\xed\x04\xff\x00\xff\x00\xfe!7\x89\x0c0 8\x8e\x9e\x0e\x1e\x00\x00\x00\x00\x00\x00 `\xc3\x00\x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=377, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=118),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=385, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=118),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc3\x00g!'),
                            None,
                            bytearray(b'\x00\x12\x00\x04\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00>\x12<\x04\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=111),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x18\x1888484\x0c\x1c\x0c\x0c\x00\x00\x00\x00\x18\x18 8\x14,4,\x14\x1c\x0c\x0c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc3\x00g!'),
                            None,
                            bytearray(b'\x00\x12\x00\x04\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00>\x12<\x04\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=111),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc3\x00g!'),
                            None,
                            bytearray(b'\x00\x12\x00\x04\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00>\x12<\x04\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc3\x00g!'),
                            None,
                            bytearray(b'\x00\x12\x00\x04\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00>\x12<\x04\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=373, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x0e\x0f>?z\x7f1w\x0f\r\x00\x00\x00\x00\x01\x01\x01\x0f\x11/e\x1fO\x7f\x0f\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc3\x00g!'),
                            None,
                            bytearray(b'\x00\x12\x00\x04\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00>\x12<\x04\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=373, y=113),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x0f\x0b\xef\xfb\x1b\x1f66\xc0\xc0\x00\x00\x00\x00\x00\x00\x08\x07\x1a\x15\x04\x1f\x07\x07\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xbf\xc0\xbf\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x80\x80\x80\x80"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xbf@-Dm\x92\xed\x12\xe257\x81l\x10 8\x80\x80\x8e\x9e\x00\x00\x00\x00\x08\x008p\x83\x00\x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                    ]
                ),
                Mold(29, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x19\x08\x1b\t'),
                            None,
                            bytearray(b'\x00\n\x00\x02\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00\x1e\n\x1e\x02\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f\x10\x10\x00\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x0f\x0b\xef\xfb\x1b\x1f66\xc0\xc0\x00\x00\x00\x00\x00\x00\x08\x07\x1a\x15\x04\x1f\x07\x07\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=118),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xbf\xc0\xbf\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x80\x80\x80\x80"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xbf@-Dm\x92\xed\x12\xe257\x81l\x10 8\x80\x80\x8e\x9e\x00\x00\x00\x00\x08\x008p\x83\x00\x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                    ]
                ),
                Mold(30, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x19\x08\x1b\t'),
                            None,
                            bytearray(b'\x00\n\x00\x02\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00\x1e\n\x1e\x02\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x0f\x0f\x10\x10\x00\x00\x00\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x0f\x0b\xef\xfb\x1b\x1f66\xc0\xc0\x00\x00\x00\x00\x00\x00\x08\x07\x1a\x15\x04\x1f\x07\x07\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=372),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xbf\xc0\xbf\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x80\x80\x80\x80"),
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            bytearray(b'\xbf@-Dm\x92\xed\x12\xe257\x81l\x10 8\x80\x80\x8e\x9e\x00\x00\x00\x00\x08\x008p\x83\x00\x87\xc1'),
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                    ]
                ),
                Mold(31, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x10  AA\x82\x82\x8c\x8c00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=113, y=115),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xc3\x00g!'),
                            None,
                            bytearray(b'\x00\x12\x00\x04\x00\x08bnfn\x00\x0e\x0c\x0c\x00\x00>\x12<\x04\x18\x08\\.<n>\x0e<\x0c\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x0f\x1f7:6\x1e>\x0c<\x00\x00\x00\x00\x00\x00\x08\x0f!?\x16.&><<\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=387, y=117),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xe0\xf0\xfef\xfd\xff\xfd}\xf1\xbdc\x7f\x8e\xbe<\xbc\xd00d\x9a\xfe\x01r\x8f\x0f\xff\x9f\x7f~~||'),
                            None,
                            bytearray(b'<\xbc(\xb8\xac\xbc\xbc\xbcx8p0\xe0`\xc0\xc0<|(x,|||\xf8xp\xf0\xe0\xe0\xc0\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x01\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x03\x01\x03\x03\x01'),
                            bytearray(b"\x07\x06\'\x1c9F~\x81\xfa\x05\x7f\x00\xb1\xc2\xa5\xc0\x02\x05<\x03\x02\x01\x01\x00\x00\x00\x00\x80\x8c\x80\x9e\x8c"),
                            bytearray(b'\x03\x00\x02\x00\x02\x01\x03\x00\x00\x01\x00\x00\x00\x00\x00\x00\x03\x01\x02\x01\x02\x00\x02\x00\x00\x00\x01\x00\x00\x00\x00\x00'),
                            bytearray(b'\xadD-Dm\x80\xe1\x12\xf2-7\x89,\x10 8\x8e\x9e\x8e\x9e\x0c\x1e\x0c\x0c\x00\x00 `\xe3 \x87\xc1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0 \xe0p\xe0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\xc0\xc0\xe0\xe0\xf0\xf0'),
                            None,
                            bytearray(b'\x10\xe0\xf0\xc0`\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xf0p\xf0`\xe0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x01\x07\x07\x07\x07\x03\x07\x01\x07\x0e\r\x1f\x17\x1f0\x00\x01\x00\x07\x00\x07\x04\x07\x0e\x0f\x17\x1f\x13\x0f\x00\x0f'),
                            bytearray(b'\xf3\xff\xf8\xff\xf8\xff\xe0\xff\x81\xff?\xdf\xff\xff\x8e\xff\x0f\xff\x07\xff\x07\xff\x1f\xff\x7f\xff\xff\xff\xff\xff\x7f\xff'),
                            bytearray(b'>\x07\x1c\x04\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x10\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\x87\x83?\xbc@\x9e"\x00\x00\x00\x00\x00\x00\x00\x00\x83\x7f|\x83\x83\x80\x80\xc1\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=119),
                    ]
                ),
            ],
            sequences=[
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
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=6, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=5),
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
                        AnimationSequenceFrame(duration=2, mold_id=23),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=2, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=26),
                        AnimationSequenceFrame(duration=4, mold_id=27),
                        AnimationSequenceFrame(duration=4, mold_id=28),
                        AnimationSequenceFrame(duration=6, mold_id=29),
                        AnimationSequenceFrame(duration=8, mold_id=30),
                        AnimationSequenceFrame(duration=8, mold_id=31),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=6, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=18),
                        AnimationSequenceFrame(duration=6, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=19),
                        AnimationSequenceFrame(duration=6, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=18),
                        AnimationSequenceFrame(duration=6, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=20),
                        AnimationSequenceFrame(duration=6, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=8, mold_id=22),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=17),
                        AnimationSequenceFrame(duration=12, mold_id=18),
                        AnimationSequenceFrame(duration=8, mold_id=17),
                        AnimationSequenceFrame(duration=12, mold_id=19),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL608_SHY_RANGER,
    palette_offset=0,
    unknown_num=0
)
