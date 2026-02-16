# SPR0038_RED_MUSHROOM

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL503_RED_MUSHROOM
sprite = CompleteSprite(
    animation=AnimationPack(272, length=458, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'?\x00\x1f\x00\x03\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00$$\x1e\x1e\x0f\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xfe\x01`\x98\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x0f\x0f\xef\xef\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=110),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x01\x02\x07\x08\x0f\x00?\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x03\x03\x08\x08\x08\x08\x04\x04\'\'ww"),
                            bytearray(b"\x00\x00\x1e \xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xfc\x03\x00\x00>>\x86\x86\x02\x02\x00\x00cc\'\'\xff\xff"),
                            bytearray(b'\xfe\x01\xff\x00\xff\x00\xff\x00\xff\x00\x7f\x00\x7f\x00\x7f\x00\xc7\xc7\x83\x83\x8f\x8f\x97\x97\xe3\xe3FFDD@@'),
                            bytearray(b'8\xc4\x00\x80\x00\x80\xb8@\xfc\x02\xff\x00\xff\x00\xff\x00\xfc\xfc\x80\x80\x80\x80\xf8\xf8\xee\xee&&\x04\x04\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=94),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'?\x00\x1f\x00\x03\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00$$\x1e\x1e\x0f\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xfe\x01`\x98\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x0f\x0f\xef\xef\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x01\x02\x07\x08\x0f\x00?\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x03\x03\x08\x08\x08\x08\x04\x04\'\'ww"),
                            bytearray(b"\x00\x00\x1e \xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xfc\x03\x00\x00>>\x86\x86\x02\x02\x00\x00cc\'\'\xff\xff"),
                            bytearray(b'\xfe\x01\xff\x00\xff\x00\xff\x00\xff\x00\x7f\x00\x7f\x00\x7f\x00\xc7\xc7\x83\x83\x8f\x8f\x97\x97\xe3\xe3FFDD@@'),
                            bytearray(b'8\xc4\x00\x80\x00\x80\xb8@\xfc\x02\xff\x00\xff\x00\xff\x00\xfc\xfc\x80\x80\x80\x80\xf8\xf8\xee\xee&&\x04\x04\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=94),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'?\x00\x1f\x00\x03\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00$$\x1e\x1e\x0f\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xfe\x01`\x98\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x0f\x0f\xef\xef\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=364),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x01\x02\x07\x08\x0f\x00?\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x03\x03\x08\x08\x08\x08\x04\x04\'\'ww"),
                            bytearray(b"\x00\x00\x1e \xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xfc\x03\x00\x00>>\x86\x86\x02\x02\x00\x00cc\'\'\xff\xff"),
                            bytearray(b'\xfe\x01\xff\x00\xff\x00\xff\x00\xff\x00\x7f\x00\x7f\x00\x7f\x00\xc7\xc7\x83\x83\x8f\x8f\x97\x97\xe3\xe3FFDD@@'),
                            bytearray(b'8\xc4\x00\x80\x00\x80\xb8@\xfc\x02\xff\x00\xff\x00\xff\x00\xfc\xfc\x80\x80\x80\x80\xf8\xf8\xee\xee&&\x04\x04\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=348),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'?\x00\x1f\x00\x03\x0c\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00$$\x1e\x1e\x0f\x0f\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00\xff\x00\xfe\x01`\x98\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x0f\x0f\xef\xef\xf8\xf8\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=364),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x01\x02\x07\x08\x0f\x00?\x00\x7f\x00\x7f\x00\x00\x00\x00\x00\x03\x03\x08\x08\x08\x08\x04\x04\'\'ww"),
                            bytearray(b"\x00\x00\x1e \xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xfc\x03\x00\x00>>\x86\x86\x02\x02\x00\x00cc\'\'\xff\xff"),
                            bytearray(b'\xfe\x01\xff\x00\xff\x00\xff\x00\xff\x00\x7f\x00\x7f\x00\x7f\x00\xc7\xc7\x83\x83\x8f\x8f\x97\x97\xe3\xe3FFDD@@'),
                            bytearray(b'8\xc4\x00\x80\x00\x80\xb8@\xfc\x02\xff\x00\xff\x00\xff\x00\xfc\xfc\x80\x80\x80\x80\xf8\xf8\xee\xee&&\x04\x04\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=348),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x1f\x00?\x00>\x00?\x00\x7f\x00\x00\x00\x01\x01\x00\x00\x06\x06\x13\x1322;;cc'),
                            bytearray(b'\x18\x00\xfe\x00\xff\x00\xff\x00\xfe\x00\xfe\x008\x00\x00\x00\x18\x18\xc4\xc4\x01\x01##\xa6\xa6\xe6\xe688\x00\x00'),
                            bytearray(b'~\x00|\x00;\x00\x0f\x00\x1f\x00\x1f\x00\x0f\x00\x03\x00ZZ\\\\::\x0e\x0e\x18\x18\x14\x14\x04\x04\x03\x03'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xfc\x00\xfe\x00\xff\x00\xff\x00\xfc\x00\x00\x00\x00\x00``$$\x00\x00\x01\x01\x83\x83\x1c\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=92),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x1f\x00?\x00>\x00?\x00\x7f\x00\x00\x00\x01\x01\x00\x00\x06\x06\x13\x1322;;cc'),
                            bytearray(b'\x18\x00\xfe\x00\xff\x00\xff\x00\xfe\x00\xfe\x008\x00\x00\x00\x18\x18\xc4\xc4\x01\x01##\xa6\xa6\xe6\xe688\x00\x00'),
                            bytearray(b'~\x00|\x00;\x00\x0f\x00\x1f\x00\x1f\x00\x0f\x00\x03\x00ZZ\\\\::\x0e\x0e\x18\x18\x14\x14\x04\x04\x03\x03'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xfc\x00\xfe\x00\xff\x00\xff\x00\xfc\x00\x00\x00\x00\x00``$$\x00\x00\x01\x01\x83\x83\x1c\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=92),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x1f\x00?\x00>\x00?\x00\x7f\x00\x00\x00\x01\x01\x00\x00\x06\x06\x13\x1322;;cc'),
                            bytearray(b'\x18\x00\xfe\x00\xff\x00\xff\x00\xfe\x00\xfe\x008\x00\x00\x00\x18\x18\xc4\xc4\x01\x01##\xa6\xa6\xe6\xe688\x00\x00'),
                            bytearray(b'~\x00|\x00;\x00\x0f\x00\x1f\x00\x1f\x00\x0f\x00\x03\x00ZZ\\\\::\x0e\x0e\x18\x18\x14\x14\x04\x04\x03\x03'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xfc\x00\xfe\x00\xff\x00\xff\x00\xfc\x00\x00\x00\x00\x00``$$\x00\x00\x01\x01\x83\x83\x1c\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=346),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x03\x00\x1f\x00?\x00>\x00?\x00\x7f\x00\x00\x00\x01\x01\x00\x00\x06\x06\x13\x1322;;cc'),
                            bytearray(b'\x18\x00\xfe\x00\xff\x00\xff\x00\xfe\x00\xfe\x008\x00\x00\x00\x18\x18\xc4\xc4\x01\x01##\xa6\xa6\xe6\xe688\x00\x00'),
                            bytearray(b'~\x00|\x00;\x00\x0f\x00\x1f\x00\x1f\x00\x0f\x00\x03\x00ZZ\\\\::\x0e\x0e\x18\x18\x14\x14\x04\x04\x03\x03'),
                            bytearray(b'\x00\x00\x00\x00\xe0\x00\xfc\x00\xfe\x00\xff\x00\xff\x00\xfc\x00\x00\x00\x00\x00``$$\x00\x00\x01\x01\x83\x83\x1c\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=346),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x04\x00\n\x00\x1c\x00\x1f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x04\x04\n\n\x1c\x1c\x13\x13\x1a\x1a'),
                            bytearray(b'\x00\x00\x18\x00\xdc\x00~\x00\xfc\x00~\x004\x00\x00\x00\x00\x00\x18\x18\xc4\xc4""\xe4\xe4~~$$\x00\x00'),
                            bytearray(b'>\x004\x00\x1b\x00\x07\x00\x0f\x00\x03\x00\x01\x00\x00\x00**$$\x1b\x1b\x06\x06\r\r\x01\x01\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\x9c\x00\xce\x00\xbe\x00\x1c\x00\x00\x00\x00\x00\x00\x00@@\x04\x04\x02\x02\x02\x02\x1c\x1c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=88),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x04\x00\n\x00\x1c\x00\x1f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x04\x04\n\n\x1c\x1c\x13\x13\x1a\x1a'),
                            bytearray(b'\x00\x00\x18\x00\xdc\x00~\x00\xfc\x00~\x004\x00\x00\x00\x00\x00\x18\x18\xc4\xc4""\xe4\xe4~~$$\x00\x00'),
                            bytearray(b'>\x004\x00\x1b\x00\x07\x00\x0f\x00\x03\x00\x01\x00\x00\x00**$$\x1b\x1b\x06\x06\r\r\x01\x01\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\x9c\x00\xce\x00\xbe\x00\x1c\x00\x00\x00\x00\x00\x00\x00@@\x04\x04\x02\x02\x02\x02\x1c\x1c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=88),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                        Tile(mirror=True, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x04\x00\n\x00\x1c\x00\x1f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x04\x04\n\n\x1c\x1c\x13\x13\x1a\x1a'),
                            bytearray(b'\x00\x00\x18\x00\xdc\x00~\x00\xfc\x00~\x004\x00\x00\x00\x00\x00\x18\x18\xc4\xc4""\xe4\xe4~~$$\x00\x00'),
                            bytearray(b'>\x004\x00\x1b\x00\x07\x00\x0f\x00\x03\x00\x01\x00\x00\x00**$$\x1b\x1b\x06\x06\r\r\x01\x01\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\x9c\x00\xce\x00\xbe\x00\x1c\x00\x00\x00\x00\x00\x00\x00@@\x04\x04\x02\x02\x02\x02\x1c\x1c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=342),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x04\x00\n\x00\x1c\x00\x1f\x00\x1e\x00\x00\x00\x00\x00\x00\x00\x04\x04\n\n\x1c\x1c\x13\x13\x1a\x1a'),
                            bytearray(b'\x00\x00\x18\x00\xdc\x00~\x00\xfc\x00~\x004\x00\x00\x00\x00\x00\x18\x18\xc4\xc4""\xe4\xe4~~$$\x00\x00'),
                            bytearray(b'>\x004\x00\x1b\x00\x07\x00\x0f\x00\x03\x00\x01\x00\x00\x00**$$\x1b\x1b\x06\x06\r\r\x01\x01\x01\x01\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\xc0\x00\x9c\x00\xce\x00\xbe\x00\x1c\x00\x00\x00\x00\x00\x00\x00@@\x04\x04\x02\x02\x02\x02\x1c\x1c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=342),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=386, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=370, y=109),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=126),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=126),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=384, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=368, y=110),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=127),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=127),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=382, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=366, y=111),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00`\xe0\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\r\x07\r\x07\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\t\x01\t\x01\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00O\xdbK\xd9\x0b\xf9\x87\x01\xff\x87\xff\xff\x00\x00\xc0?gCgA\x07\x01\xff\x01\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x80\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x80\x80\xc0@\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'\x90\x08p\x88x\xa0x\x90x\xb0x\xb0\xf8\x18\xf00\x08\xf8\x88\xf8\xf8\xa0\xf8\x90\xf8\xb0\xf8\xb0\xf8\x18\xf00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x06\x01\x0e\x01\x0f\x11\r\x13\x1f\x1f\x00\x00\x00\x00\x03\x00\x05\x05\t\x08\x11\x10\x1b\x18\x1f '),
                            bytearray(b'\x00\x00||\xff\xfe\xc7\xff\xbb\xc7\xff\x83\xff\x83\xbb\xc7\x00\x00|\x00\xff\x01\xff\x10\xc7\x04\x83\x00\x83\x00\xc7D'),
                            bytearray(b'\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x17\x18\x0e\x01\x1f \x1d,\x000\x18(\x19)\x1d\r\x1f\x1f\t\x07'),
                            bytearray(b'\xcc\xfc\xfc\xfdp\xf3\xe0c\xc0G\xc0G\xc2A\x80\x83\xfc3\xfd\x03\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf\x83\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=109),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=110),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0c\x03\r\x04\x0c\x0f\x0c\t\x0f\x0e\x03\x03\x00\x00\x00\x00\x0b\x07\x0b\x00\x08\x08\x0e\x08\x0f\x0e\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\x80\x83\xff\x83?\x9f\x1b\xf9\x87\x03\xff\x87\xff\xff\x00\x00\x83\x7f\x83\xff\x7f\x1f\x07\x01\xff\x03\xff\x87\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=117),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=122),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x03\x02\x00\x02\x03\x02\x03\x06\x07\x06\x04\x07\x07\x01\x01\x07\x03\x07\x00\x04\x00\x04\x00\x04\x04\x07\x04\x07\x07\x01\x01'),
                            bytearray(b'\x80\x83\xffG\x1f\xdf\x1f\xf7\x1f\xf3\x17\xf3\xcf\x07\xff\xcf\x83\x7f\xc7\x7f?\x1f\x0f\x07\x0f\x03\x0f\x03\xff\x07\xff\xcf'),
                            None,
                            bytearray(b'~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=122),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=362),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=362),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=363),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=363),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=122),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x03\x02\x00\x02\x03\x02\x03\x06\x07\x06\x04\x07\x07\x01\x01\x07\x03\x07\x00\x04\x00\x04\x00\x04\x04\x07\x04\x07\x07\x01\x01'),
                            bytearray(b'\x80\x83\xffG\x1f\xdf\x1f\xf7\x1f\xf3\x17\xf3\xcf\x07\xff\xcf\x83\x7f\xc7\x7f?\x1f\x0f\x07\x0f\x03\x0f\x03\xff\x07\xff\xcf'),
                            None,
                            bytearray(b'~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=122),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=370),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x03\x02\x00\x02\x03\x02\x03\x06\x07\x06\x04\x07\x07\x01\x01\x07\x03\x07\x00\x04\x00\x04\x00\x04\x04\x07\x04\x07\x07\x01\x01'),
                            bytearray(b'\x80\x83\xffG\x1f\xdf\x1f\xf7\x1f\xf3\x17\xf3\xcf\x07\xff\xcf\x83\x7f\xc7\x7f?\x1f\x0f\x07\x0f\x03\x0f\x03\xff\x07\xff\xcf'),
                            None,
                            bytearray(b'~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=354),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=368),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x03\x02\x00\x02\x03\x02\x03\x06\x07\x06\x04\x07\x07\x01\x01\x07\x03\x07\x00\x04\x00\x04\x00\x04\x04\x07\x04\x07\x07\x01\x01'),
                            bytearray(b'\x80\x83\xffG\x1f\xdf\x1f\xf7\x1f\xf3\x17\xf3\xcf\x07\xff\xcf\x83\x7f\xc7\x7f?\x1f\x0f\x07\x0f\x03\x0f\x03\xff\x07\xff\xcf'),
                            None,
                            bytearray(b'~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=352),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=352),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=366),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x03\x02\x00\x02\x03\x02\x03\x06\x07\x06\x04\x07\x07\x01\x01\x07\x03\x07\x00\x04\x00\x04\x00\x04\x04\x07\x04\x07\x07\x01\x01'),
                            bytearray(b'\x80\x83\xffG\x1f\xdf\x1f\xf7\x1f\xf3\x17\xf3\xcf\x07\xff\xcf\x83\x7f\xc7\x7f?\x1f\x0f\x07\x0f\x03\x0f\x03\xff\x07\xff\xcf'),
                            None,
                            bytearray(b'~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=366),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=350),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=350),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80\xe0`\x80\x80\x80\x80\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=365),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x04\x03\x02\x00\x02\x03\x02\x03\x06\x07\x06\x04\x07\x07\x01\x01\x07\x03\x07\x00\x04\x00\x04\x00\x04\x04\x07\x04\x07\x07\x01\x01'),
                            bytearray(b'\x80\x83\xffG\x1f\xdf\x1f\xf7\x1f\xf3\x17\xf3\xcf\x07\xff\xcf\x83\x7f\xc7\x7f?\x1f\x0f\x07\x0f\x03\x0f\x03\xff\x07\xff\xcf'),
                            None,
                            bytearray(b'~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=365),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xa0\xc0\xe0\xe0\xe0\xe0\x90\x88\x00\x00\x00\x00\x00\x00\xc0\xc0\xe0 \xe0\x10\xe0\x10\x88x'),
                            None,
                            bytearray(b'0\x08\xf8 x\x90x\xb0\xf80\xf8\x10p\x90`\xa0\x08\xf88\xe0\xf8\x90\xf8\xb0\xf80\xf8\x10\xf0\x90\xe0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=349),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x03\x07\x07\x06\t\x0e\x11\x1f\x01\r\x13\x00\x00\x00\x00\x03\x00\x07\x00\t\t\x11\x10\x11\x10\x130'),
                            bytearray(b'\x00\x00||\xff\xfe\xfe\xff\xff\xff\xc7\xff\xbb\xc7\xff\x83\x00\x00|\x00\xfe\x00\xff\x00\xff\x00\xff\x10\xc7\x04\x83\x00'),
                            bytearray(b'\x1f\x1f\x1f\x1f\x16\x19\x0f\x00\x1f\x10\x1f\x10\x1f\x10\x07\x08\x1f \x1f \x19(\x000\x18(\x19)\x1d\r\x0f\x0f'),
                            bytearray(b'\xff\x83\xf8\xc4\xe4\xfdp\xf3\xe0c\xc0G\xc4C\xc2A\x83\x00\xc4\x07\xfd\x1b\xf3\x0fc\x1f\xc7\xbf\xc7\xbf\xc3\xbf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=349),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=8, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=4, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
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
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL503_RED_MUSHROOM,
    palette_offset=0,
    unknown_num=0
)
