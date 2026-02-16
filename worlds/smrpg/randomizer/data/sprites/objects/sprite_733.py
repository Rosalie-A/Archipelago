# SPR0733_CHOMP

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL537_CHOMP_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(391, length=731, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x03\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x06\x00'),
                            bytearray(b'\x0e\x0c\x05\x1e!2$!&\x16\xc0\x8a\x80\xc0 @\x0c\x02\x19\x061\x02 7\x06(\xb8F \xc0 @'),
                            bytearray(b'\x04\x04\x04\x0281\x10x\x84\xc8\x90\x84\x98X\x00(\x04\x06\x00\x057\x08d\x18\xc4\x08\x80\xdc\x18\xa0\xe0\x18'),
                            bytearray(b'\x80 \xc0\xc0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=86),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5p\xbe\xac\xccS Q_0 \n\r\x03\x03D\x84A\x80\xf3\x80?@_` ?\x00\x0f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=161, y=74),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x03\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x06\x00'),
                            bytearray(b'\x0e\x0c\x05\x1e!2$!&\x16\xc0\x8a\x80\xc0 @\x0c\x02\x19\x061\x02 7\x06(\xb8F \xc0 @'),
                            bytearray(b'\x04\x04\x04\x0281\x10x\x84\xc8\x90\x84\x98X\x00(\x04\x06\x00\x057\x08d\x18\xc4\x08\x80\xdc\x18\xa0\xe0\x18'),
                            bytearray(b'\x80 \xc0\xc0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=86),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5p\xbe\xac\xccS Q_0 \n\r\x03\x03D\x84A\x80\xf3\x80?@_` ?\x00\x0f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=162, y=74),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<\x04,\\JNjN\x06&Dt\x08\x00\x08\x00\x10,$XN*N*&ZdL\x10\x08\x10\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=94),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'<\x04,\\JNjN\x06&Dt\x08\x00\x08\x00\x10,$XN*N*&ZdL\x10\x08\x10\x08'),
                            None,
                            bytearray(b'<\x04,\\JNjN\x06&Dt\x08\x00\x08\x00\x10,$XN*N*&ZdL\x10\x08\x10\x08'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=78),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5p\xbe\xac\xccS Q_0 \n\r\x03\x03D\x84A\x80\xf3\x80?@_` ?\x00\x0f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=68),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x03\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x06\x00'),
                            bytearray(b'\x0e\x0c\x05\x1e!2$!&\x16\xc0\x8a\x80\xc0 @\x0c\x02\x19\x061\x02 7\x06(\xb8F \xc0 @'),
                            bytearray(b'\x04\x04\x04\x0281\x10x\x84\xc8\x90\x84\x98X\x00(\x04\x06\x00\x057\x08d\x18\xc4\x08\x80\xdc\x18\xa0\xe0\x18'),
                            bytearray(b'\x80 \xc0\xc0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=86),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5p\xbe\xac\xccS Q_0 \n\r\x03\x03D\x84A\x80\xf3\x80?@_` ?\x00\x0f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=74),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07\x1b\x1c)?s@>\x1e\x81\xff\xe5\xba\xd7\xa8\x07\x07\x18\x1f/0_`!@\x80\x80Y\x98\x88\x08'),
                            bytearray(b'\xe0\xe0\xb8\x18T,>\xa2\xd6z\x1dMu\xc5\t\xe9\xe0\xe0\x18\xf84\xcc\xa2F\xe4\x02\xfd\x03\xfc\x03\xd0\x07'),
                            bytearray(b'=\xf2qL\xbe\xc9\x96\xa1T_! \x11\x1f\x07\x07\xc0@\x0b\x88\xc0\x80\xb8\xc0\x1f`\x00?\x10\x1f\x07\x07'),
                            bytearray(b'\x07\xe9M_\x9f?\x0e\x9e\xde\x1e|\xfc\xf8\xf8\xe0\xe0\xd8\xc7\xb1\x0f\x85\x7fN>\xfc\x0e|\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=88),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=94),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=96),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=98),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07\x1b\x1c)?s@>\x1e\x81\xff\xe5\xba\xd7\xa8\x07\x07\x18\x1f/0_`!@\x80\x80Y\x98\x88\x08'),
                            bytearray(b'\xe0\xe0\xb8\x18T,>\xa2\xd6z\x1dMu\xc5\t\xe9\xe0\xe0\x18\xf84\xcc\xa2F\xe4\x02\xfd\x03\xfc\x03\xd0\x07'),
                            bytearray(b'=\xf2qL\xbe\xc9\x96\xa1T_! \x11\x1f\x07\x07\xc0@\x0b\x88\xc0\x80\xb8\xc0\x1f`\x00?\x10\x1f\x07\x07'),
                            bytearray(b'\x07\xe9M_\x9f?\x0e\x9e\xde\x1e|\xfc\xf8\xf8\xe0\xe0\xd8\xc7\xb1\x0f\x85\x7fN>\xfc\x0e|\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=90),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=94),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=96),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x18\x18)\'ba\x1f~\xa2\xce<BD:\x07\x07\x10\x1f/0\x7f@A\x00\xd1\xc0A\xc09\xb8"),
                            bytearray(b'\xe0\xe0\x18\x18L\x04\x92\xb6P\xd6\xd1[\xf3E\xcbO\xe0\xe0\x18\xf8\x14\xec\x9af\xc4:\xc79\xc79\xcf1'),
                            bytearray(b'\xe1\xfcf!\xd5zaI~~\x03 \x13\x1f\x07\x07\x83\x00X\x80\x08\x88v\x00>A\x00?\x01\x1f\x05\x07'),
                            bytearray(b'\xef_\xa9\x19\x91S>6\xfe~\xfc\xfc\xf8\xf8\xe0\xe0\xc1?i\x07?\x01\xe2\x1e>\xfe|\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=92),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07\x1b\x1c)?s@>\x1e\x81\xff\xe5\xba\xd7\xa8\x07\x07\x18\x1f/0_`!@\x80\x80Y\x98\x88\x08'),
                            bytearray(b'\xe0\xe0\xb8\x18T,>\xa2\xd6z\x1dMu\xc5\t\xe9\xe0\xe0\x18\xf84\xcc\xa2F\xe4\x02\xfd\x03\xfc\x03\xd0\x07'),
                            bytearray(b'=\xf2qL\xbe\xc9\x96\xa1T_! \x11\x1f\x07\x07\xc0@\x0b\x88\xc0\x80\xb8\xc0\x1f`\x00?\x10\x1f\x07\x07'),
                            bytearray(b'\x07\xe9M_\x9f?\x0e\x9e\xde\x1e|\xfc\xf8\xf8\xe0\xe0\xd8\xc7\xb1\x0f\x85\x7fN>\xfc\x0e|\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=90),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=93),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=96),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x07\x07\x1b\x1c)?s@>\x1e\x81\xff\xe5\xba\xd7\xa8\x07\x07\x18\x1f/0_`!@\x80\x80Y\x98\x88\x08'),
                            bytearray(b'\xe0\xe0\xb8\x18T,>\xa2\xd6z\x1dMu\xc5\t\xe9\xe0\xe0\x18\xf84\xcc\xa2F\xe4\x02\xfd\x03\xfc\x03\xd0\x07'),
                            bytearray(b'=\xf2qL\xbe\xc9\x96\xa1T_! \x11\x1f\x07\x07\xc0@\x0b\x88\xc0\x80\xb8\xc0\x1f`\x00?\x10\x1f\x07\x07'),
                            bytearray(b'\x07\xe9M_\x9f?\x0e\x9e\xde\x1e|\xfc\xf8\xf8\xe0\xe0\xd8\xc7\xb1\x0f\x85\x7fN>\xfc\x0e|\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=168, y=88),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=162, y=93),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=95),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=97),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00 0\x0c,\x98\xfc\xbc\x8c\xc0`@\xc0\x00\x00\x00\x008 ,\x18\xb0\xcc\xb4L\x00\xe0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x16\x1b[~\x7f|F\x07]D7?\x00\x00\x01\x01\x11\x1e}@|\x1fe\x06#@3\x0f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=130),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5\xb0~\xd0hc\x00\xf9\x7f<8\x1c\x1f\x03\x03D\x84\xe1\x00\xd7 \xcf0o\xf0\x10?\x08\x1f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x02\x03\x17\x1a[|~\x7fF\x07]E6>\x01\x01\x01\x02\x11\x1c|C}\x1ee\x06#@2\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00(8\x84\xe4\x98\xbc\xfcL@\xe0\x00\x00\x00\x00\x00\x000(\xac\xd0\xb8L0\xcc\xc0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff{.\xb5\xdf\x8f6F{`69\x0f\x0f\x00\x00P\xf0+\xd0\x0f\xf0\x06y`\x7f ?\t\x0f\x00\x00'),
                            bytearray(b'\xf8XP\xcc\xa8\x98\x1c||\xfc\xf0\xf0\xc0\xc0\x00\x00\xc0:\xc2<\x84z\x0c\xfc\x1c\xfcp\xf0\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1e\x1e(?p_\'8\xff\xa0\xc7x\xc3\xfd\x07\x07\x1f\x180 `@\x00@\xc0\x80\x18\x98\x9c\x1c"),
                            bytearray(b'\xc0\xc0ppH\xa8\x04\xf4\x866\x8e6F\xf6\x96\xaa\xc0\xc0\xf00(8$,Z\x16^\x16>6j&'),
                            bytearray(b'Rl2>Y\x98\xa6\x81\xa3\xbf\x81P\xeaIc<\r\x8cA\x80g\x80\xbf\xc0\xbf\xc0\xc0?\xf8\x07\xc54'),
                            bytearray(b'\x08\x8a\xe4\\d\xdc\x90\xb00p`\xe0\xc0\xc0\xe0\xa0\xe2\x1e\xc4>\xc4<\x88p\x00\xf0 \xe0@\xc0\x80`'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x15\x19^{{~G\x04VG-<\x0f\x0f\x00\x00\x11\x1dyF}\x18d\x07-B+\x10\x03\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08$4\x88\xec\x9c\xbc\xf0@@\xe0\x00\x00\x00\x00\x00\x08< \xa8\xdc\xb4L0\xc0\xc0 '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xf5P~t:<\x1c\x1f\x03\x03\x00\x00\x00\x00\x00\x00W\xf8\x07x\x10?\x08\x1f\x02\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x9e\x81\xa0n\\<p\xf0\xc0\xc0\x00\x00\x00\x00\x00\x00\x80\x7f\xe0\x1e\x1c\xfcp\xf0@\xc0\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x00\x00\x00\x00\x06\x07\x13\x1c\'8=@`\x00\xc0\x80"),
                            bytearray(b'\x00\x00\x00\x00`\xe08\xe8\x1c\xecP\x0e"\xec3\xef\x00\x00\x00\x00 \xe0\xe8\x18\xf8\x04\xe4\x02\x1c\x04\x15\x05'),
                            bytearray(b'\x05\xbb\x80?\xab5V\x1e\x99X\x97`\xe1o\\<X\x98^\x9eD\x84a\x80g\x80\xff\x00\xef0\xcc3'),
                            bytearray(b'\xa7\xe5A\x19A#\xb2n\x94HX\xc0\xe3\x80\xb8m\x1a\x01\xf8\x07\xe3\x1f\xe2\x1e\xcc4\xd88\xff\x7f\x1a\xf3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00 0\x0c,\x98\xfc\xbc\x8c\xc0`@\xc0\x00\x00\x00\x008 ,\x18\xb0\xcc\xb4L\x00\xe0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x16\x1b[~\x7f|F\x07]D7?\x00\x00\x01\x01\x11\x1e}@|\x1fe\x06#@3\x0f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x80\x80\x00\x80\x00\x00\x00@\xc0\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x00\x80\x80\x00\x80\xc0\xc0\x80@\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'|\xf8\x1c\x1f\x07\x07\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xb8\x7f\x1c\x1f\x07\x07\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~>p\xf0\xe0\xe0\xe0\xe0\xe0\xa0@\xc0\x00\x00\x00\x00\x0c\xfe\x10\xf0\xe0\xe0`\xe0\xa0`\x00\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x05\x14\x1f;-\x11\xbe/P\x00\x00\x01\x01\x01\x00\x03\x05\x19\x112  \xc0\xa0\x00'),
                            bytearray(b'@@\xe0 \x00\xc0 \xc8.\xd6\xc2>\xe6\x1a\xce:@\x80\x00 \xe0\xc0\xd0\xc8\xce\xc260\x16\x11\x06\x01'),
                            bytearray(b'\xe1\xbe\xf0\xaf1\xael\xb3\xd1\xff4\x84\x19\x08\x1e\xd5N\x8e\xcf\x8fN\x8eB\x820\x80\xcb0\x8fp\x978'),
                            bytearray(b'\xd26\xd76\xed\xe5j\x1a@+\xa0oH\xd7\xb3\x9c\x0e\x01\x0e\x01\x1c\x03\xfb\x04\xe3\x1f\xe3\x1b\xc7?\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00 0\x0c,\x98\xfc\xbc\x8c\xc0`@\xc0\x00\x00\x00\x008 ,\x18\xb0\xcc\xb4L\x00\xe0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x16\x1b[~\x7f|F\x07]D7?\x00\x00\x01\x01\x11\x1e}@|\x1fe\x06#@3\x0f'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=130),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x04\x01\x04\x03\x02\x02\x02\x03\x01\x00\x00\x00\x00\x00\x03\x07\x03\x05\x03\x05\x03\x02\x03\x02\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xb0\x00\xe0\x00\xe0\x00\xc0\x00@\x80\x00\x80\x00\x00@0@0@ \x00`\x00@\x00@\x80\x00\x00\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=135),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x82\xba\x044\x08\xc8\xb0p0\xf0\xe0`@\xc0@\xc08\xc6\xd0\x0c\xe0\xd8@0\x80p@\xe0@\xc0@\xc0'),
                            bytearray(b'\xbcr0O\xdc\xc3@\xd7\xba\x95>~\xbf_\xb8\x08\x03\xfc\x07\xfb\xc3;\xc7?\x80x\x0f\xfe_?H8'),
                            bytearray(b'\x00\x80\x00\x00@\xc0@\xa0  00\xf8\xf8\xfc\xfc\x00\x80\x80\x00\xc0\x80\x80\xa0\xe0\x00\xe0\x10\xf8\x88\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'??\x16\x10\x08\x0b\x0c\r\x04\x07\x02\x03\x01\x01\x00\x00\x1f \t\x10\x03\x0f\x03\r\x01\x07\x01\x02\x01\x01\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x03\x06\x06\x03\x08\x06\t\x01\x1f\x00\x00\x00\x00\x00\x03\x02\x07\x00\x02\x04\x05\x08\x07\x08\x00\x1f'),
                            bytearray(b'\x08\x17\x10Ol\xccs\xc865~8\xfd\xb8\x80\x03f\x86\x12\xa2C0\xcf0\xf78\x98\x7f\x8a|\x07\x83'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x02\x05\x06\x04\x05\x00\x00\x00\x00\x00\x01\x00\x01\x01\x02\x01\x02\x02\x04\x03\x05'),
                            bytearray(b'\x80\x80@@@@\xa0 \xa0 p\xb0\x10\xd08\xd8\x00\x80\x00\xc0\x80@\x00`@ \xa0\x90\xe0\xd0\xd0\xc8'),
                            bytearray(b'\xc6\xcd&%\x04\xed#\xcc\x1e\xd10\xcf@?Qn\x05\xc9\xe9\x11\xf2\xe0\xd0\xc0\xe1\xc1\xaf\x8f\xdf\x1f\x0e\x8e'),
                            bytearray(b'\x0c\xe4\x18\xe4\xc2=\xfc\rB\xb6\x13\xf6\xdd\x14\x9f\r\xf4\xec\xef\xe051\x07\x01\x8f\x80\xce\xc1<\x03\x0c\xf3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=111),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x03\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x06\x00'),
                            bytearray(b'\x0e\x0c\x05\x1e!2$!&\x16\xc0\x8a\x80\xc0 @\x0c\x02\x19\x061\x02 7\x06(\xb8F \xc0 @'),
                            bytearray(b'\x04\x04\x04\x0281\x10x\x84\xc8\x90\x84\x98X\x00(\x04\x06\x00\x057\x08d\x18\xc4\x08\x80\xdc\x18\xa0\xe0\x18'),
                            bytearray(b'\x80 \xc0\xc0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=86),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x80\x80\x00\x80\x00\x00\x00@\xc0\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x00\x80\x80\x00\x80\xc0\xc0\x80@\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=177, y=335),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'|\xf8\x1c\x1f\x07\x07\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xb8\x7f\x1c\x1f\x07\x07\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~>p\xf0\xe0\xe0\xe0\xe0\xe0\xa0@\xc0\x00\x00\x00\x00\x0c\xfe\x10\xf0\xe0\xe0`\xe0\xa0`\x00\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=161, y=343),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x05\x14\x1f;-\x11\xbe/P\x00\x00\x01\x01\x01\x00\x03\x05\x19\x112  \xc0\xa0\x00'),
                            bytearray(b'@@\xe0 \x00\xc0 \xc8.\xd6\xc2>\xe6\x1a\xce:@\x80\x00 \xe0\xc0\xd0\xc8\xce\xc260\x16\x11\x06\x01'),
                            bytearray(b'\xe1\xbe\xf0\xaf1\xael\xb3\xd1\xff4\x84\x19\x08\x1e\xd5N\x8e\xcf\x8fN\x8eB\x820\x80\xcb0\x8fp\x978'),
                            bytearray(b'\xd26\xd76\xed\xe5j\x1a@+\xa0oH\xd7\xb3\x9c\x0e\x01\x0e\x01\x1c\x03\xfb\x04\xe3\x1f\xe3\x1b\xc7?\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=161, y=327),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x03\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x06\x00'),
                            bytearray(b'\x0e\x0c\x05\x1e!2$!&\x16\xc0\x8a\x80\xc0 @\x0c\x02\x19\x061\x02 7\x06(\xb8F \xc0 @'),
                            bytearray(b'\x04\x04\x04\x0281\x10x\x84\xc8\x90\x84\x98X\x00(\x04\x06\x00\x057\x08d\x18\xc4\x08\x80\xdc\x18\xa0\xe0\x18'),
                            bytearray(b'\x80 \xc0\xc0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=86),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x80\x80\x00\x80\x00\x00\x00@\xc0\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x00\x80\x80\x00\x80\xc0\xc0\x80@\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=178, y=335),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'|\xf8\x1c\x1f\x07\x07\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xb8\x7f\x1c\x1f\x07\x07\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~>p\xf0\xe0\xe0\xe0\xe0\xe0\xa0@\xc0\x00\x00\x00\x00\x0c\xfe\x10\xf0\xe0\xe0`\xe0\xa0`\x00\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=162, y=343),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x05\x14\x1f;-\x11\xbe/P\x00\x00\x01\x01\x01\x00\x03\x05\x19\x112  \xc0\xa0\x00'),
                            bytearray(b'@@\xe0 \x00\xc0 \xc8.\xd6\xc2>\xe6\x1a\xce:@\x80\x00 \xe0\xc0\xd0\xc8\xce\xc260\x16\x11\x06\x01'),
                            bytearray(b'\xe1\xbe\xf0\xaf1\xael\xb3\xd1\xff4\x84\x19\x08\x1e\xd5N\x8e\xcf\x8fN\x8eB\x820\x80\xcb0\x8fp\x978'),
                            bytearray(b'\xd26\xd76\xed\xe5j\x1a@+\xa0oH\xd7\xb3\x9c\x0e\x01\x0e\x01\x1c\x03\xfb\x04\xe3\x1f\xe3\x1b\xc7?\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=162, y=327),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'<\x04,\\JNjN\x06&Dt\x08\x00\x08\x00\x10,$XN*N*&ZdL\x10\x08\x10\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=94),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'<\x04,\\JNjN\x06&Dt\x08\x00\x08\x00\x10,$XN*N*&ZdL\x10\x08\x10\x08'),
                            None,
                            bytearray(b'<\x04,\\JNjN\x06&Dt\x08\x00\x08\x00\x10,$XN*N*&ZdL\x10\x08\x10\x08'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=78),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\xe0\x10\xe0@\x10@\xc0\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0p`@\xb0@\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=151, y=72),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x03\x01\x0e\x01\x06\x06\x01\x01\x00\x00\x00\x00\x00\x01\x01\x06\x02\x0e\x0e\x0e\x06\x00\x04\x00\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=72),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x02\x07\x14\x138\'Xg\x1eY\xab\xf7\x05\xbb\x80?\x05\x01\x13\x1b/7?Ge\x01\xc0\x80X\x98^\x9e"),
                            bytearray(b'\x80\xc0\x98h\\\x8c\x10\xae"\xbe-\xe5\xb5\xedA\x19@\x00(\x18\x18$d\x02\xc6\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5p\xbe\xac\xccS Q_0 \n\r\x03\x03D\x84A\x80\xf3\x80?@_` ?\x00\x0f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=68),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x03\x04\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x06\x00'),
                            bytearray(b'\x0e\x0c\x05\x1e!2$!&\x16\xc0\x8a\x80\xc0 @\x0c\x02\x19\x061\x02 7\x06(\xb8F \xc0 @'),
                            bytearray(b'\x04\x04\x04\x0281\x10x\x84\xc8\x90\x84\x98X\x00(\x04\x06\x00\x057\x08d\x18\xc4\x08\x80\xdc\x18\xa0\xe0\x18'),
                            bytearray(b'\x80 \xc0\xc0\x00@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xe0\xc0\x00\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=86),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x00\x80\x80\x80\x00\x80\x00\x00\x00@\xc0\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x00\x80\x80\x00\x80\xc0\xc0\x80@\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=102, y=79),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'|\xf8\x1c\x1f\x07\x07\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xb8\x7f\x1c\x1f\x07\x07\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~>p\xf0\xe0\xe0\xe0\xe0\xe0\xa0@\xc0\x00\x00\x00\x00\x0c\xfe\x10\xf0\xe0\xe0`\xe0\xa0`\x00\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=87),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x05\x14\x1f;-\x11\xbe/P\x00\x00\x01\x01\x01\x00\x03\x05\x19\x112  \xc0\xa0\x00'),
                            bytearray(b'@@\xe0 \x00\xc0 \xc8.\xd6\xc2>\xe6\x1a\xce:@\x80\x00 \xe0\xc0\xd0\xc8\xce\xc260\x16\x11\x06\x01'),
                            bytearray(b'\xe1\xbe\xf0\xaf1\xael\xb3\xd1\xff4\x84\x19\x08\x1e\xd5N\x8e\xcf\x8fN\x8eB\x820\x80\xcb0\x8fp\x978'),
                            bytearray(b'\xd26\xd76\xed\xe5j\x1a@+\xa0oH\xd7\xb3\x9c\x0e\x01\x0e\x01\x1c\x03\xfb\x04\xe3\x1f\xe3\x1b\xc7?\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=110, y=71),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x80\x00@\x00\xc0\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x80@\x80\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=92),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'yF :\x1b\x1c\x17\x1b\x07\t\x01\r\n\x06\x0c\x08\x01@\x1d \x10\x1f\x1a\x17\x00\x03\x0c\x07\x02\n\x08\x0c'),
                            bytearray(b'P\xc0\x04\x1c\xf8x\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\xc69\xf0\x0c`\xf8\x00\xe0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\t\x19\x00\x16\x07?\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x03\x0c\x0f\x10\x18 \xe0\x00'),
                            bytearray(b'\x08\x00\x08\x18\x08p\x08\xf8\x1c\xe8\xa2<6\xfa\x13\xfc\x00\x18\x180x0\xf0p\xa0$\xc4\x02\n\x08\x02\x01'),
                            bytearray(b'\x03\x9d1n!\xbe\xb6i\xe39\xa8\x8b\x13b\xab\x93\xe0\x80N\x8e\xde\x1e\x88\x08G\x80\xf6\x02|\xc0\xc7\x80'),
                            bytearray(b'\xd5\xf3\xaa\x86\xbe\xb6\x80Q@5`\x0bH\xbf\xf0\xdf\x0f\x00~\x01~\x01\xe8\x07k\xa4\x9f\x03\x9f\x87\xdf7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=84),
                        Tile(mirror=True, invert=True, format=0, length=4, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=94),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=96),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=98),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x80\x00@\x00\xc0\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x80@\x80\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=94),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'yF :\x1b\x1c\x17\x1b\x07\t\x01\r\n\x06\x0c\x08\x01@\x1d \x10\x1f\x1a\x17\x00\x03\x0c\x07\x02\n\x08\x0c'),
                            bytearray(b'P\xc0\x04\x1c\xf8x\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\xc69\xf0\x0c`\xf8\x00\xe0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\t\x19\x00\x16\x07?\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x03\x0c\x0f\x10\x18 \xe0\x00'),
                            bytearray(b'\x08\x00\x08\x18\x08p\x08\xf8\x1c\xe8\xa2<6\xfa\x13\xfc\x00\x18\x180x0\xf0p\xa0$\xc4\x02\n\x08\x02\x01'),
                            bytearray(b'\x03\x9d1n!\xbe\xb6i\xe39\xa8\x8b\x13b\xab\x93\xe0\x80N\x8e\xde\x1e\x88\x08G\x80\xf6\x02|\xc0\xc7\x80'),
                            bytearray(b'\xd5\xf3\xaa\x86\xbe\xb6\x80Q@5`\x0bH\xbf\xf0\xdf\x0f\x00~\x01~\x01\xe8\x07k\xa4\x9f\x03\x9f\x87\xdf7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=86),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=94),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=96),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\xe0\x10\xe0@\x10@\xc0\x00\x00\x00\x00\x00\x00\x00\x80\x80\xa0p`@\xb0@\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=96),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x03\x01\x0e\x01\x06\x06\x01\x01\x00\x00\x00\x00\x00\x01\x01\x06\x02\x0e\x0e\x0e\x06\x00\x04\x00\x01\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=95),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'^>X,$\x0c\x00\x18\x18\x08\x10\x10\x00\x00\x00\x00 ^ \\\x10\x0c\x00(\x10\x08\x10\x10\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x18\x18\x00\x18\x04\x1c(\x14\x0et:`\x00\x00\x00\x00\x08\x18\x08\x00\x104\x14\x10p2F\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=85),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x18\x18)\'ba\x1f~\xa2\xce<BD:\x07\x07\x10\x1f/0\x7f@A\x00\xd1\xc0A\xc09\xb8"),
                            bytearray(b'\xe0\xe0\x18\x18L\x04\x92\xb6P\xd6\xd1[\xf3E\xcbO\xe0\xe0\x18\xf8\x14\xec\x9af\xc4:\xc79\xc79\xcf1'),
                            bytearray(b'\xe1\xfcf!\xd5zaI~~\x03 \x13\x1f\x07\x07\x83\x00X\x80\x08\x88v\x00>A\x00?\x01\x1f\x05\x07'),
                            bytearray(b'\xef_\xa9\x19\x91S>6\xfe~\xfc\xfc\xf8\xf8\xe0\xe0\xc1?i\x07?\x01\xe2\x1e>\xfe|\xfc\xf8\xf8\xe0\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=92),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x80\x00@\x00\xc0\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x80@\x80\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=90),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'yF :\x1b\x1c\x17\x1b\x07\t\x01\r\n\x06\x0c\x08\x01@\x1d \x10\x1f\x1a\x17\x00\x03\x0c\x07\x02\n\x08\x0c'),
                            bytearray(b'P\xc0\x04\x1c\xf8x\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\xc69\xf0\x0c`\xf8\x00\xe0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=98),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\t\x19\x00\x16\x07?\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x03\x0c\x0f\x10\x18 \xe0\x00'),
                            bytearray(b'\x08\x00\x08\x18\x08p\x08\xf8\x1c\xe8\xa2<6\xfa\x13\xfc\x00\x18\x180x0\xf0p\xa0$\xc4\x02\n\x08\x02\x01'),
                            bytearray(b'\x03\x9d1n!\xbe\xb6i\xe39\xa8\x8b\x13b\xab\x93\xe0\x80N\x8e\xde\x1e\x88\x08G\x80\xf6\x02|\xc0\xc7\x80'),
                            bytearray(b'\xd5\xf3\xaa\x86\xbe\xb6\x80Q@5`\x0bH\xbf\xf0\xdf\x0f\x00~\x01~\x01\xe8\x07k\xa4\x9f\x03\x9f\x87\xdf7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=82),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=93),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=96),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x80\x80\x80\x80\x80\x80\x80\x00\x00\x80\x00@\x00\xc0\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x80@\x80\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=161, y=92),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'yF :\x1b\x1c\x17\x1b\x07\t\x01\r\n\x06\x0c\x08\x01@\x1d \x10\x1f\x1a\x17\x00\x03\x0c\x07\x02\n\x08\x0c'),
                            bytearray(b'P\xc0\x04\x1c\xf8x\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\xc69\xf0\x0c`\xf8\x00\xe0\x80\x80\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=168, y=100),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\t\x19\x00\x16\x07?\xdf\x00\x00\x00\x00\x00\x00\x00\x00\x03\x0c\x0f\x10\x18 \xe0\x00'),
                            bytearray(b'\x08\x00\x08\x18\x08p\x08\xf8\x1c\xe8\xa2<6\xfa\x13\xfc\x00\x18\x180x0\xf0p\xa0$\xc4\x02\n\x08\x02\x01'),
                            bytearray(b'\x03\x9d1n!\xbe\xb6i\xe39\xa8\x8b\x13b\xab\x93\xe0\x80N\x8e\xde\x1e\x88\x08G\x80\xf6\x02|\xc0\xc7\x80'),
                            bytearray(b'\xd5\xf3\xaa\x86\xbe\xb6\x80Q@5`\x0bH\xbf\xf0\xdf\x0f\x00~\x01~\x01\xe8\x07k\xa4\x9f\x03\x9f\x87\xdf7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=168, y=84),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=162, y=93),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=95),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00,.\x0b0\x01"\xcf\x0e3?\x1c\x1c\x00\x00\x00\x00,22\r\xc1\x12\x0c\xff>!\x1c\x1c\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=97),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00(8\x84\xe4\x98\xbc\xfcL@\xe0\x00\x00\x00\x00\x00\x000(\xac\xd0\xb8L0\xcc\xc0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x02\x03\x17\x1a[|~\x7fF\x07]E6>\x01\x01\x01\x02\x11\x1c|C}\x1ee\x06#@2\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5\xb0~\xd0hc\x00\xf9\x7f<8\x1c\x1f\x03\x03D\x84\xe1\x00\xd7 \xcf0o\xf0\x10?\x08\x1f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08$4\x88\xec\x9c\xbc\xf0@@\xe0\x00\x00\x00\x00\x00\x08< \xa8\xdc\xb4L0\xc0\xc0 '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x15\x19^{{~G\x04VG-<\x0f\x0f\x00\x00\x11\x1dyF}\x18d\x07-B+\x10\x03\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x07\x07\x1b\x1b7\'Zb\x1c_\xab\xf7\x05\xbb\x80?\x06\x07\x13\x1c\'8=@`\x00\xc0\x80X\x98^\x9e"),
                            bytearray(b'`\xe08\xe8\x1c\xecP\x0e"\xfe-\xe5\xb5\xedA\x19 \xe0\xe8\x18\xf8\x04\xe4\x02\x06\x00\x1d\x03\x1c\x03\xf8\x07'),
                            bytearray(b'\xab5\xb0~\xd0hc\x00\xf9\x7f<8\x1c\x1f\x03\x03D\x84\xe1\x00\xd7 \xcf0o\xf0\x10?\x08\x1f\x02\x03'),
                            bytearray(b';y\x15C\xe7_\x8e\xbe^>\xbc|\xf0\xf0\xc0\xc0\xf8\x07\xc1?\xc1?\x86~\x0e\xfe\x1c\xfcp\xf0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00(8\x84\xe4\x98\xbc\xfcL@\xe0\x00\x00\x00\x00\x00\x000(\xac\xd0\xb8L0\xcc\xc0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x02\x03\x17\x1a[|~\x7fF\x07]E6>\x01\x01\x01\x02\x11\x1c|C}\x1ee\x06#@2\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x80\x80\x00\x80\x00\x00\x00@\xc0\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x00\x80\x80\x00\x80\xc0\xc0\x80@\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'|\xf8\x1c\x1f\x07\x07\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xb8\x7f\x1c\x1f\x07\x07\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~>p\xf0\xe0\xe0\xe0\xe0\xe0\xa0@\xc0\x00\x00\x00\x00\x0c\xfe\x10\xf0\xe0\xe0`\xe0\xa0`\x00\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x05\x14\x1f;-\x11\xbe/P\x00\x00\x01\x01\x01\x00\x03\x05\x19\x112  \xc0\xa0\x00'),
                            bytearray(b'@@\xe0 \x00\xc0 \xc8.\xd6\xc2>\xe6\x1a\xce:@\x80\x00 \xe0\xc0\xd0\xc8\xce\xc260\x16\x11\x06\x01'),
                            bytearray(b'\xe1\xbe\xf0\xaf1\xael\xb3\xd1\xff4\x84\x19\x08\x1e\xd5N\x8e\xcf\x8fN\x8eB\x820\x80\xcb0\x8fp\x978'),
                            bytearray(b'\xd26\xd76\xed\xe5j\x1a@+\xa0oH\xd7\xb3\x9c\x0e\x01\x0e\x01\x1c\x03\xfb\x04\xe3\x1f\xe3\x1b\xc7?\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08$4\x88\xec\x9c\xbc\xf0@@\xe0\x00\x00\x00\x00\x00\x08< \xa8\xdc\xb4L0\xc0\xc0 '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x15\x19^{{~G\x04VG-<\x0f\x0f\x00\x00\x11\x1dyF}\x18d\x07-B+\x10\x03\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x80\x80\x00\x80\x00\x00\x00@\xc0\x00\x80\x00\x80\x00\x80\x80\x00\x00\x80\x00\x80\x80\x00\x80\xc0\xc0\x80@\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'|\xf8\x1c\x1f\x07\x07\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\xb8\x7f\x1c\x1f\x07\x07\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'~>p\xf0\xe0\xe0\xe0\xe0\xe0\xa0@\xc0\x00\x00\x00\x00\x0c\xfe\x10\xf0\xe0\xe0`\xe0\xa0`\x00\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=132),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x05\x14\x1f;-\x11\xbe/P\x00\x00\x01\x01\x01\x00\x03\x05\x19\x112  \xc0\xa0\x00'),
                            bytearray(b'@@\xe0 \x00\xc0 \xc8.\xd6\xc2>\xe6\x1a\xce:@\x80\x00 \xe0\xc0\xd0\xc8\xce\xc260\x16\x11\x06\x01'),
                            bytearray(b'\xe1\xbe\xf0\xaf1\xael\xb3\xd1\xff4\x84\x19\x08\x1e\xd5N\x8e\xcf\x8fN\x8eB\x820\x80\xcb0\x8fp\x978'),
                            bytearray(b'\xd26\xd76\xed\xe5j\x1a@+\xa0oH\xd7\xb3\x9c\x0e\x01\x0e\x01\x1c\x03\xfb\x04\xe3\x1f\xe3\x1b\xc7?\x80x'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00(8\x84\xe4\x98\xbc\xfcL@\xe0\x00\x00\x00\x00\x00\x000(\xac\xd0\xb8L0\xcc\xc0 \x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x01\x01\x02\x03\x17\x1a[|~\x7fF\x07]E6>\x01\x01\x01\x02\x11\x1c|C}\x1ee\x06#@2\x0e'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x04\x01\x04\x03\x02\x02\x02\x03\x01\x00\x00\x00\x00\x00\x03\x07\x03\x05\x03\x05\x03\x02\x03\x02\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xb0\x00\xe0\x00\xe0\x00\xc0\x00@\x80\x00\x80\x00\x00@0@0@ \x00`\x00@\x00@\x80\x00\x00\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=135),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x82\xba\x044\x08\xc8\xb0p0\xf0\xe0`@\xc0@\xc08\xc6\xd0\x0c\xe0\xd8@0\x80p@\xe0@\xc0@\xc0'),
                            bytearray(b'\xbcr0O\xdc\xc3@\xd7\xba\x95>~\xbf_\xb8\x08\x03\xfc\x07\xfb\xc3;\xc7?\x80x\x0f\xfe_?H8'),
                            bytearray(b'\x00\x80\x00\x00@\xc0@\xa0  00\xf8\xf8\xfc\xfc\x00\x80\x80\x00\xc0\x80\x80\xa0\xe0\x00\xe0\x10\xf8\x88\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'??\x16\x10\x08\x0b\x0c\r\x04\x07\x02\x03\x01\x01\x00\x00\x1f \t\x10\x03\x0f\x03\r\x01\x07\x01\x02\x01\x01\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x03\x06\x06\x03\x08\x06\t\x01\x1f\x00\x00\x00\x00\x00\x03\x02\x07\x00\x02\x04\x05\x08\x07\x08\x00\x1f'),
                            bytearray(b'\x08\x17\x10Ol\xccs\xc865~8\xfd\xb8\x80\x03f\x86\x12\xa2C0\xcf0\xf78\x98\x7f\x8a|\x07\x83'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x02\x05\x06\x04\x05\x00\x00\x00\x00\x00\x01\x00\x01\x01\x02\x01\x02\x02\x04\x03\x05'),
                            bytearray(b'\x80\x80@@@@\xa0 \xa0 p\xb0\x10\xd08\xd8\x00\x80\x00\xc0\x80@\x00`@ \xa0\x90\xe0\xd0\xd0\xc8'),
                            bytearray(b'\xc6\xcd&%\x04\xed#\xcc\x1e\xd10\xcf@?Qn\x05\xc9\xe9\x11\xf2\xe0\xd0\xc0\xe1\xc1\xaf\x8f\xdf\x1f\x0e\x8e'),
                            bytearray(b'\x0c\xe4\x18\xe4\xc2=\xfc\rB\xb6\x13\xf6\xdd\x14\x9f\r\xf4\xec\xef\xe051\x07\x01\x8f\x80\xce\xc1<\x03\x0c\xf3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=111),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x08\x08$4\x88\xec\x9c\xbc\xf0@@\xe0\x00\x00\x00\x00\x00\x08< \xa8\xdc\xb4L0\xc0\xc0 '),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=126),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x15\x19^{{~G\x04VG-<\x0f\x0f\x00\x00\x11\x1dyF}\x18d\x07-B+\x10\x03\x0f\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=129),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x07\x04\x01\x04\x03\x02\x02\x02\x03\x01\x00\x00\x00\x00\x00\x03\x07\x03\x05\x03\x05\x03\x02\x03\x02\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\xb0\x00\xb0\x00\xe0\x00\xe0\x00\xc0\x00@\x80\x00\x80\x00\x00@0@0@ \x00`\x00@\x00@\x80\x00\x00\x80'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=135),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x82\xba\x044\x08\xc8\xb0p0\xf0\xe0`@\xc0@\xc08\xc6\xd0\x0c\xe0\xd8@0\x80p@\xe0@\xc0@\xc0'),
                            bytearray(b'\xbcr0O\xdc\xc3@\xd7\xba\x95>~\xbf_\xb8\x08\x03\xfc\x07\xfb\xc3;\xc7?\x80x\x0f\xfe_?H8'),
                            bytearray(b'\x00\x80\x00\x00@\xc0@\xa0  00\xf8\xf8\xfc\xfc\x00\x80\x80\x00\xc0\x80\x80\xa0\xe0\x00\xe0\x10\xf8\x88\xfc\xfc'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'??\x16\x10\x08\x0b\x0c\r\x04\x07\x02\x03\x01\x01\x00\x00\x1f \t\x10\x03\x0f\x03\r\x01\x07\x01\x02\x01\x01\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x03\x06\x06\x03\x08\x06\t\x01\x1f\x00\x00\x00\x00\x00\x03\x02\x07\x00\x02\x04\x05\x08\x07\x08\x00\x1f'),
                            bytearray(b'\x08\x17\x10Ol\xccs\xc865~8\xfd\xb8\x80\x03f\x86\x12\xa2C0\xcf0\xf78\x98\x7f\x8a|\x07\x83'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x02\x05\x06\x04\x05\x00\x00\x00\x00\x00\x01\x00\x01\x01\x02\x01\x02\x02\x04\x03\x05'),
                            bytearray(b'\x80\x80@@@@\xa0 \xa0 p\xb0\x10\xd08\xd8\x00\x80\x00\xc0\x80@\x00`@ \xa0\x90\xe0\xd0\xd0\xc8'),
                            bytearray(b'\xc6\xcd&%\x04\xed#\xcc\x1e\xd10\xcf@?Qn\x05\xc9\xe9\x11\xf2\xe0\xd0\xc0\xe1\xc1\xaf\x8f\xdf\x1f\x0e\x8e'),
                            bytearray(b'\x0c\xe4\x18\xe4\xc2=\xfc\rB\xb6\x13\xf6\xdd\x14\x9f\r\xf4\xec\xef\xe051\x07\x01\x8f\x80\xce\xc1<\x03\x0c\xf3'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=111),
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
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=23),
                        AnimationSequenceFrame(duration=4, mold_id=24),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                        AnimationSequenceFrame(duration=2, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=21),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=25),
                        AnimationSequenceFrame(duration=4, mold_id=26),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=27),
                        AnimationSequenceFrame(duration=4, mold_id=28),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL537_CHOMP_PACKET,
    palette_offset=0,
    unknown_num=0
)
