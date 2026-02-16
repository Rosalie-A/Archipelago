# SPR0022_MALLOW_NONPROTAGONIST_4

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
        263,
        length=1064,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=108),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=151, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=153, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\xa0`\x90p0\xd0\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x0b\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x0f\xf0a\x9f\xd4<\xb0r`\xec\xc0\xc8\x000@\x88\x00\x00\x00\x00\x03\x00\x0e\x02\x1c\x0c8\x08\xf08\xc8\xb8'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=137, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x02\x07\x04\x07\x00\x0b\x04\x07\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x10\x00\x00\x00'),
                            bytearray(b' \x1c\x008\x008\xc2=\xef\x10\xff\x00\xff\x00\xff\x00< 8\x06\xf8\x068\x00\x10\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\n\x17\r\x03\x06\x01\x0b\x08\x02\x13\t!\x086\x18\x13\x00\x00\x10\x008\x004\x00<\x10>0?6+\x17'),
                            bytearray(b'\xfe\x013\xcfe\x9e\xfb\x04\x18\xe7\xe7\xff\x7f\x7f\x03\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xff\x8b'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'  \xe0`p\x80@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x18\xc0\x98\x80p\xf0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x08\x08\x07\x05\x01\x06\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x10\x1f\x0b\n\x04\x04\x03\x03\x01\x01\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x0f\xf0\x8c\x80,\xdf\xef\x7f\xe0\x00hX\xdf\xaf||\xff\xf0\x81\x7f0?\x90\x9f\xe0\x1fx\xa7\xff\xd7||'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=114),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=156, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\xa0`\x90p0\xd0\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x0b\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x02\x07\x04\x07\x00\x0b\x04\x07\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x10\x00\x00\x00'),
                            bytearray(b' \x1c\x008\x008\xc2=\xef\x10\xff\x00\xff\x00\xff\x00< 8\x06\xf8\x068\x00\x10\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0f\xf0a\x9f\xd4<\xb0r`\xec\xc0\xc8\x000@\x88\x00\x00\x00\x00\x03\x00\x0e\x02\x1c\x0c8\x08\xf08\xc8\xb8'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'  \xe0`p\x80@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x18\xc0\x98\x80p\xf0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\n\x17\r\x03\x06\x01\x0b\x08\x02\x13\t!\x086\x18\x13\x00\x00\x10\x008\x004\x00<\x10>0?6+\x17'),
                            bytearray(b'\xfe\x013\xcfe\x9e\xfb\x04\x18\xe7\xe7\xff\x7f\x7f\x03\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xff\x8b'),
                            bytearray(b'\x08\x08\x07\x05\x01\x06\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x10\x1f\x0b\n\x04\x04\x03\x03\x01\x01\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x0f\xf0\x8c\x80,\xdf\xef\x7f\xe0\x00hX\xdf\xaf||\xff\xf0\x81\x7f0?\x90\x9f\xe0\x1fx\xa7\xff\xd7||'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=114),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\xa0`\x90p0\xd0\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x0b\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x02\x07\x04\x07\x00\x0b\x04\x07\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x10\x00\x00\x00'),
                            bytearray(b' \x1c\x008\x008\xc2=\xef\x10\xff\x00\xff\x00\xff\x00< 8\x06\xf8\x068\x00\x10\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0f\xf0a\x9f\xd4<\xb0r`\xec\xc0\xc8\x000@\x88\x00\x00\x00\x00\x03\x00\x0e\x02\x1c\x0c8\x08\xf08\xc8\xb8'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'  \xe0`p\x80@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x18\xc0\x98\x80p\xf0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\n\x17\r\x03\x06\x01\x0b\x08\x02\x13\t!\x086\x18\x13\x00\x00\x10\x008\x004\x00<\x10>0?6+\x17'),
                            bytearray(b'\xfe\x013\xcfe\x9e\xfb\x04\x18\xe7\xe7\xff\x7f\x7f\x03\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xff\x8b'),
                            bytearray(b'\x08\x08\x07\x05\x01\x06\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x10\x1f\x0b\n\x04\x04\x03\x03\x01\x01\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x0f\xf0\x8c\x80,\xdf\xef\x7f\xe0\x00hX\xdf\xaf||\xff\xf0\x81\x7f0?\x90\x9f\xe0\x1fx\xa7\xff\xd7||'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=158, y=103),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=154, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xc0@\xa0`\x90p0\xd0\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x0b\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x02\x07\x04\x07\x00\x0b\x04\x07\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x10\x00\x00\x00'),
                            bytearray(b' \x1c\x008\x008\xc2=\xef\x10\xff\x00\xff\x00\xff\x00< 8\x06\xf8\x068\x00\x10\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x0f\xf0a\x9f\xd4<\xb0r`\xec\xc0\xc8\x000@\x88\x00\x00\x00\x00\x03\x00\x0e\x02\x1c\x0c8\x08\xf08\xc8\xb8'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'  \xe0`p\x80@@\xc0\xc0\xc0\xc0\x80\x80\x00\x00\x18\xc0\x98\x80p\xf0\xc0\xc0\xc0\xc0\xc0\xc0\x80\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\n\x17\r\x03\x06\x01\x0b\x08\x02\x13\t!\x086\x18\x13\x00\x00\x10\x008\x004\x00<\x10>0?6+\x17'),
                            bytearray(b'\xfe\x013\xcfe\x9e\xfb\x04\x18\xe7\xe7\xff\x7f\x7f\x03\x88\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xff\x8b'),
                            bytearray(b'\x08\x08\x07\x05\x01\x06\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x10\x1f\x0b\n\x04\x04\x03\x03\x01\x01\x01\x01\x00\x00\x00\x00'),
                            bytearray(b'\x0f\xf0\x8c\x80,\xdf\xef\x7f\xe0\x00hX\xdf\xaf||\xff\xf0\x81\x7f0?\x90\x9f\xe0\x1fx\xa7\xff\xd7||'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=160, y=102),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=142, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=105),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=110),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=121),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8p\xf0\xf0\x10\xf0\x00\xf0\x08\xe4\x18\xf0\x00\xf8\x00\xf8\x00\xf0\x00\x00\x00\x08\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\xc6:<\xf2\xf8\x06\xe6\x1e\x9c|\xf0\xf8\xe0\xe0h\x10\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x06\x00\x1f\x00\xf9v'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            bytearray(b'\x01\x00\x02\x01<#<C\xfe\x81\x7f\x80\x7f\x80\xff\x80\x01\x01\x0f\x02\x03\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            bytearray(b'\xbf\xc0\xd0?k\x9c?@c|??\x03\xc3\x00q\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xc0\x00\xfc\xc0\x7f\xf1'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=113),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00!! #WX\xbf\xc0\x80\xffcc\x00\x00\x03\x00V\x00\xdc\x00\xa0\x00\x00\x00\x00\x00\x9c\x00a\x00'),
                            bytearray(b'\xc0\xf8\x80\xc4\x00\xcc \xec \xe8 \xe8\xc0\xc0\x00088<\x04<\x0c\x1c\x0c\x18\x08\x18\x080\x00\xf00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b"\x00\x000\'@wh_x\x7f\x18\x1b\x00\x03\x00\x07<\x00O\x07\x8f\x07\x87\x07\x87\x07g\x03?\x03\x1f\x07"),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=115),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=146, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=106),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=108),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=149, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=139, y=105),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=153, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=143, y=103),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=111),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0e*&y"}\x02=!?r\xce\xe4\'\x80\x9f1 @@@@@\x00@\x00\x81\x80\x1b\x03\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\x80\x00@\x00@\x00@\x00\xc0\x00\x80\x00\x00\x80\x80\x80\x80\xc0@\xc0@\xc0@\xc0\xc0\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=155, y=105),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\n..q.v\x0c=&9w\xc9\xec-\x80\x9f1 @@A@C\x01@\x00\x80\x80\x13\x01\x7f\x1f'),
                            bytearray(b'\x00\x80\x00\xc0\x00\xc0\x00@\x80\xc0\x00\x00\x00\x80\x00\x00\x80\x80@@@@\xc0@@@\x80\x00\x80\x80\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=145, y=102),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=111),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\r\x034\x0c\xd00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x00'),
                            bytearray(b'\x03\x00\r\x034\x0c\xd00@\xc0\x00\x00\x00\x00\x00\x00\x04\x00\x10\x00C\x00\x0c\x000\x00\xc0\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x06\x17\x18_`\xbb\xc4v\x8f\xff\x00\xff\x00_\xe0\t\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\xd0\xc0,\xe8\x1a\xfc\x00\xfe\x03\xfc\x01\xf4\x0f\x80\x000\x10\x1c\x0c\x06\x02\x02\x00\x01\x01\x03\x01\x03\x03'),
                            bytearray(b"\'x\x17\xd4\x87h^\x01:\x06\x10\x0b\x03\x04\x03\x0c\xc0@\xe8\xc0\xf0``\x00\x01\x00\x07\x03\x0f\x04\x0f\x0c"),
                            bytearray(b'\xe8\x1b\x80wc\xec\x83\xbcG\xb8\xde \xfc\x00\xe0\x00\x07\x03\x0f\x07\x1f\x0c\x7f<\xff\xb8\xfe \xfc\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=104),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=106),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x06\x17\x18_`\xbb\xc4v\x8f\xff\x00\xff\x00_\xe0\t\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\xd0\xc0,\xe8\x1a\xfc\x00\xfe\x03\xfc\x01\xf4\x0f\x80\x000\x10\x1c\x0c\x06\x02\x02\x00\x01\x01\x03\x01\x03\x03'),
                            bytearray(b"\'x\x17\xd4\x87h^\x01:\x06\x10\x0b\x03\x04\x03\x0c\xc0@\xe8\xc0\xf0``\x00\x01\x00\x07\x03\x0f\x04\x0f\x0c"),
                            bytearray(b'\xe8\x1b\x80wc\xec\x83\xbcG\xb8\xde \xfc\x00\xe0\x00\x07\x03\x0f\x07\x1f\x0c\x7f<\xff\xb8\xfe \xfc\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=99),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=102),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x06\x17\x18_`\xbb\xc4v\x8f\xff\x00\xff\x00_\xe0\t\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\xd0\xc0,\xe8\x1a\xfc\x00\xfe\x03\xfc\x01\xf4\x0f\x80\x000\x10\x1c\x0c\x06\x02\x02\x00\x01\x01\x03\x01\x03\x03'),
                            bytearray(b"\'x\x17\xd4\x87h^\x01:\x06\x10\x0b\x03\x04\x03\x0c\xc0@\xe8\xc0\xf0``\x00\x01\x00\x07\x03\x0f\x04\x0f\x0c"),
                            bytearray(b'\xe8\x1b\x80wc\xec\x83\xbcG\xb8\xde \xfc\x00\xe0\x00\x07\x03\x0f\x07\x1f\x0c\x7f<\xff\xb8\xfe \xfc\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=98),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=101),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=107),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x06\x17\x18_`\xbb\xc4v\x8f\xff\x00\xff\x00_\xe0\t\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\xd0\xc0,\xe8\x1a\xfc\x00\xfe\x03\xfc\x01\xf4\x0f\x80\x000\x10\x1c\x0c\x06\x02\x02\x00\x01\x01\x03\x01\x03\x03'),
                            bytearray(b"\'x\x17\xd4\x87h^\x01:\x06\x10\x0b\x03\x04\x03\x0c\xc0@\xe8\xc0\xf0``\x00\x01\x00\x07\x03\x0f\x04\x0f\x0c"),
                            bytearray(b'\xe8\x1b\x80wc\xec\x83\xbcG\xb8\xde \xfc\x00\xe0\x00\x07\x03\x0f\x07\x1f\x0c\x7f<\xff\xb8\xfe \xfc\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=152, y=97),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=100),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=111),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x06\x06\x17\x18_`\xbb\xc4v\x8f\xff\x00\xff\x00_\xe0\t\x00 \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\xd0\xc0,\xe8\x1a\xfc\x00\xfe\x03\xfc\x01\xf4\x0f\x80\x000\x10\x1c\x0c\x06\x02\x02\x00\x01\x01\x03\x01\x03\x03'),
                            bytearray(b"\'x\x17\xd4\x87h^\x01:\x06\x10\x0b\x03\x04\x03\x0c\xc0@\xe8\xc0\xf0``\x00\x01\x00\x07\x03\x0f\x04\x0f\x0c"),
                            bytearray(b'\xe8\x1b\x80wc\xec\x83\xbcG\xb8\xde \xfc\x00\xe0\x00\x07\x03\x0f\x07\x1f\x0c\x7f<\xff\xb8\xfe \xfc\x00\xe0\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x02\x00'),
                            None,
                            bytearray(b'\x03\x02\x00\x01\x00\x00\x05\x05\x00\x06\x05\x00\x01\x06\x07\x02\x00\x00\x02\x00\x03\x00\x02\x04\x03\x06\x07\x06\x07\x06\x05\x02'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=109),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xe4\x04\x9e\x0c\x8e\xf0\xe4\xe4\x04\x04D\xc4\xf8x\xc0\xc0\xe3\x183\xf2\x0e\xfe\x14\xfc\x04\xfc\xc4<\xf8\xb8\xc0\xc0'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x01\x1e\xf1\xb0%\xdb]o\x7fx;:\x0e\r\x03\x03\x1f\xfepO\x86\x87rs\x7fx;=\x0f\x0e\x03\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x00\x04\x0f>#?\x01?@?\xc0\xdf`\x00\x00\x01\x01\x11\x00\x01\x00@\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xf0\x08\xf8\x18\xf8\x10\xf0x\x80\xf8\x04\xfc\x02\xf2\x0c\xf0\x00\xf8\x00\xf8\x00\xe8\x00\x84\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\xafp\xc87=\xc3\xdf\xe00?\x9f\x1f\x87g\x808\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x00\xf8`\xbfx'),
                            bytearray(b'\xe1\x1f\x02\xfd}\x83\xfb\x07/\xdf\xff\xfe{z4\x89\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x84\x00\xfe\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00'),
                            bytearray(b'\x00\x00\x00\x00\x0f\x00\x1e\x11\x1d#z\x06\xe9\x1a\xc2,\x00\x00\x00\x00\x00\x00 \x00@\x00\x81\x00\x07\x02\x1e\x0c'),
                            bytearray(b'\x0f\x08.1Xe\x88\xfa\xe0\xe8\x00 \x00\x00\x00\x00\x10\x00@\x00\x83\x01\x06\x02\x18\x08` \x00\x00\x00\x00'),
                            bytearray(b'H\xd0\x00`\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x10\xe0`\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=107),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x1f\x0f\x0878{G|D\x117\x93\x90\x93\x9c\x1f\x1f0\x00@\x00\x80\x00\x83\x00\xce\x06l\x00`\x00'),
                            bytearray(b'\x00\xc0\x00p\xe0\xec\x00B\xfc\xc4:\xc6\xbcB\xfd\x03\xc0\xc0\xf0p\x1c\x0c\xfeB\x02\x00\x01\x00\x01\x00\x00\x00'),
                            bytearray(b"\x03|\x0c\xf3\x1f\x90\x1b\xdc\x07G@\'`\x1e$\x1a\xa0 \xa0\xa0\xe0\x80\xe0\xc0x@\x7f\'\x7f\x1e?\x1a"),
                            bytearray(b'\xfc\x03\xfd\x03\xf9\x07\xf6\x0e\xd89\xf0\xf2\xf0\xf4\xe0\xe0\x00\x00\x00\x00\x00\x00\x01\x00\x07\x01\x0e\x02\x0c\x04\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=79),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x18\x9a\x00\x9a\x08\xd2\x18R\x1cv\x1cv\x0c$\x08$\xe6\x82\xe6\x82\xe6\xc2fBbbbb2 2 '),
                            None,
                            bytearray(b'\x00,\x08\x1c\n\x1f\x02\x17\x00\x07\x04\x06\x04\x06\x04\x062 \x12\x10\x11\x11\x19\x11\t\x01\t\x00\t\x00\t\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=129, y=95),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80`\xc0 \xe0\x00\xe0\xc0\xc0\xa0\x80@\x00\x80\x00\x00\xe0`\xe0 \xe0\xe0  ``\xc0\xc0\x80\x80\x00\x80'),
                            None,
                            bytearray(b'@@@@@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80@\x80@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1f!\x0f\x10CxF\x7f}}AAA@\x01\x00\x1f>88z\x06\x7f\x03}\x03A?A>\x01>'),
                            bytearray(b'\xf2\xe3\xc98\xc6?\xa1\x7f\xcf\r\xe5\xbc\xc3\xff\xc2\xfe\xfd\x0fyv\x01?\xc0\xfe\xf2>\xfd\x83\xff\x80\xfe\x81'),
                            bytearray(b'!!\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1f\x12\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0e\x0e\x00\x00\x08\x08\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x0eq\x00?\x08\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=114),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'@\xb0\x10\xf0`\xe0\xe0h@\xd8\xc0\xd0\x80\xf0`\x10\x00\x00\x00\x00\x10\x00\x18\x088\x180\x10pp\x90p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=98),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x08\x0f\x00\x1f\x10\x0f\x10\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x000\x08x\x88x\x14\xfa\x16\xf9\x8fp\x7f\xc0\xfe\x010\x00x\x00\xf8\x80\xf6\x06\xf0\x00\xe0\x80\x00\x00\x00\x00'),
                            bytearray(b'\x17\x18\x1f\x0816\x10\x13\x03\x01\x077\t\x01/< \x000\x10\x08\x00,\x00>\x0280\x0e8\x1f3'),
                            bytearray(b'\xfe\x01\xfd\x03\xe3\x1f?\xfe\xba\x9d\x11O\xdf\xdfg\xe7\x00\x00\x00\x00\x00\x00\x00\x00` \xf0P \x00\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=98),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x18\x9a\x00\x9a\x08\xd2\x18R\x1cv\x1cv\x0c$\x08$\xe6\x82\xe6\x82\xe6\xc2fBbbbb2 2 '),
                            None,
                            bytearray(b'\x00,\x08\x1c\n\x1f\x02\x17\x00\x07\x04\x06\x04\x06\x04\x062 \x12\x10\x11\x11\x19\x11\t\x01\t\x00\t\x00\t\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=91),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x1f\x0f\x0878{G|D\x117\x93\x90\x93\x9c\x1f\x1f0\x00@\x00\x80\x00\x83\x00\xce\x06l\x00`\x00'),
                            bytearray(b'\x00\xc0\x00p\xe0\xec\x00B\xfc\xc4:\xc6\xbcB\xfd\x03\xc0\xc0\xf0p\x1c\x0c\xfeB\x02\x00\x01\x00\x01\x00\x00\x00'),
                            bytearray(b"\x03|\x0c\xf3\x1f\x90\x1b\xdc\x07G@\'`\x1e$\x1a\xa0 \xa0\xa0\xe0\x80\xe0\xc0x@\x7f\'\x7f\x1e?\x1a"),
                            bytearray(b'\xfc\x03\xfd\x03\xf9\x07\xf6\x0e\xd89\xf0\xf2\xf0\xf4\xe0\xe0\x00\x00\x00\x00\x00\x00\x01\x00\x07\x01\x0e\x02\x0c\x04\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=77),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x18\x9a\x00\x9a\x08\xd2\x18R\x1cv\x1cv\x0c$\x08$\xe6\x82\xe6\x82\xe6\xc2fBbbbb2 2 '),
                            None,
                            bytearray(b'\x00,\x08\x1c\n\x1f\x02\x17\x00\x07\x04\x06\x04\x06\x04\x062 \x12\x10\x11\x11\x19\x11\t\x01\t\x00\t\x00\t\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=93),
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
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x18\x9a\x00\x9a\x08\xd2\x18R\x1cv\x1cv\x0c$\x08$\xe6\x82\xe6\x82\xe6\xc2fBbbbb2 2 '),
                            None,
                            bytearray(b'\x00,\x08\x1c\n\x1f\x02\x17\x00\x07\x04\x06\x04\x06\x04\x062 \x12\x10\x11\x11\x19\x11\t\x01\t\x00\t\x00\t\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=121, y=89),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x1f\x0f\x0878{G|D\x117\x93\x90\x93\x9c\x1f\x1f0\x00@\x00\x80\x00\x83\x00\xce\x06l\x00`\x00'),
                            bytearray(b'\x00\xc0\x00p\xe0\xec\x00B\xfc\xc4:\xc6\xbcB\xfd\x03\xc0\xc0\xf0p\x1c\x0c\xfeB\x02\x00\x01\x00\x01\x00\x00\x00'),
                            bytearray(b"\x03|\x0c\xf3\x1f\x90\x1b\xdc\x07G@\'`\x1e$\x1a\xa0 \xa0\xa0\xe0\x80\xe0\xc0x@\x7f\'\x7f\x1e?\x1a"),
                            bytearray(b'\xfc\x03\xfd\x03\xf9\x07\xf6\x0e\xd89\xf0\xf2\xf0\xf4\xe0\xe0\x00\x00\x00\x00\x00\x00\x01\x00\x07\x01\x0e\x02\x0c\x04\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=75),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x18\x9a\x00\x9a\x08\xd2\x18R\x1cv\x1cv\x0c$\x08$\xe6\x82\xe6\x82\xe6\xc2fBbbbb2 2 '),
                            None,
                            bytearray(b'\x00,\x08\x1c\n\x1f\x02\x17\x00\x07\x04\x06\x04\x06\x04\x062 \x12\x10\x11\x11\x19\x11\t\x01\t\x00\t\x00\t\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=91),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80`\xc0 \xe0\x00\xe0\xc0\xc0\xa0\x80@\x00\x80\x00\x00\xe0`\xe0 \xe0\xe0  ``\xc0\xc0\x80\x80\x00\x80'),
                            None,
                            bytearray(b'@@@@@@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00@\x80@\x80@\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=366),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x1f!\x0f\x10CxF\x7f}}AAA@\x01\x00\x1f>88z\x06\x7f\x03}\x03A?A>\x01>'),
                            bytearray(b'\xf2\xe3\xc98\xc6?\xa1\x7f\xcf\r\xe5\xbc\xc3\xff\xc2\xfe\xfd\x0fyv\x01?\xc0\xfe\xf2>\xfd\x83\xff\x80\xfe\x81'),
                            bytearray(b'!!\x12\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00!\x1f\x12\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x0e\x0e\x00\x00\x08\x08\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x0eq\x00?\x08\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=366),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\xc0 \xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'@\xb0\x10\xf0`\xe0\xe0h@\xd8\xc0\xd0\x80\xf0`\x10\x00\x00\x00\x00\x10\x00\x18\x088\x180\x10pp\x90p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=350),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x08\x0f\x00\x1f\x10\x0f\x10\x00\x00\x00\x00\x01\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x000\x08x\x88x\x14\xfa\x16\xf9\x8fp\x7f\xc0\xfe\x010\x00x\x00\xf8\x80\xf6\x06\xf0\x00\xe0\x80\x00\x00\x00\x00'),
                            bytearray(b'\x17\x18\x1f\x0816\x10\x13\x03\x01\x077\t\x01/< \x000\x10\x08\x00,\x00>\x0280\x0e8\x1f3'),
                            bytearray(b'\xfe\x01\xfd\x03\xe3\x1f?\xfe\xba\x9d\x11O\xdf\xdfg\xe7\x00\x00\x00\x00\x00\x00\x00\x00` \xf0P \x00\x18\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=350),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x18\x9a\x00\x9a\x08\xd2\x18R\x1cv\x1cv\x0c$\x08$\xe6\x82\xe6\x82\xe6\xc2fBbbbb2 2 '),
                            None,
                            bytearray(b'\x00,\x08\x1c\n\x1f\x02\x17\x00\x07\x04\x06\x04\x06\x04\x062 \x12\x10\x11\x11\x19\x11\t\x01\t\x00\t\x00\t\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=87),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0\xb0\xf8\xb8\xc8\xc8\xc8\xc8\xd0\xd0\xa0\xa0\xc0\xc0\x80\x80P\x10xx\xc8\xf8\xc88\xd00\xa0`\xc0\xc0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b' #\x1e\x16\x04\x1b\x13\x15\x1f\x1d\x0f\x0f\x00\x00\x00\x00C\x7f.)\x10\x10\x16\x1e\x1d\x13\x0f\x0f\x00\x00\x00\x00'),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf9\xc1\xf8\xff\x18\x1e\x0f\x0f\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf9\xc6\xff\xf0\x1e\x19\x0f\x0f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
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
                            bytearray(b'\x00\xcc|\x85\xd7(\xcf\x08\x03\xec\x1f\xf0\xff\x00\xc1>\xfc\xcc\x03\x01\x00\x000\x00\x18\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00@\x80\xa0@\xd0\x90p\xa0`\x80P\x00\x00\x00\x00\xc0@` 0\x10\x00\x00\x10\x000\x10'),
                            bytearray(b'\x00\xff\x07\xe7\x80~\xf8\x07\xf8\x07\x1f\x00\x00\x07\x00\x00\x00\x00\xf8\xe0\xff~\xff\x07\xff\x07\x1f\x00\x07\x07\x00\x00'),
                            bytearray(b'\xc0P\x80\xb0\x10` \xc0`\x80\xc0\x00\x00\x80\x00\x000\x10p0\xf0`\xe0\xc0\xe0\x80\xc0\x00\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=147, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x000\xf0\xf0\x03\xff\xf0\x0f\xff\x00\xff\x00\xe7\xf8\x0e\xcf\xf00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xc0'),
                            bytearray(b'\x00\x01\x01\xf9\xf1\xfe\x03\xfc\xf0\x0f\xff\x00\xff\x00?\xc0\x01\x01\xfe\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'<?\x00\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xff\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=103),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xb0\xb0\xf8\xb8\xc8\xc8\xc8\xc8\xd0\xd0\xa0\xa0\xc0\xc0\x80\x80P\x10xx\xc8\xf8\xc88\xd00\xa0`\xc0\xc0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b' #\x1e\x16\x04\x1b\x13\x15\x1f\x1d\x0f\x0f\x00\x00\x00\x00C\x7f.)\x10\x10\x16\x1e\x1d\x13\x0f\x0f\x00\x00\x00\x00'),
                            bytearray(b'<\xc03\x01\xb1~\xbc\xfc\xf9\xc1\xf8\xff\x18\x1e\x0f\x0f\xfc\xc3\x06\xfe\xc1\xffB\x7f\xf9\xc6\xff\xf0\x1e\x19\x0f\x0f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=118),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\xc0\x00\x80@ \xe0\x00\x00\x80\x80\x80\x80\x80\x80@\x00\x00\x00 \x00\x00\x00'),
                            None,
                            bytearray(b'\xa0`\xb0P\x10\xf0\xf0\xf0\xa0\xa0@P    \x00\x00\x00\x00\x00\x00\x00\x00P\x00\x900\x00\xc0\x00\xc0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=102),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xcc|\x85\xd7(\xcf\x08\x03\xec\x1f\xf0\xff\x00\xc1>\xfc\xcc\x03\x01\x00\x000\x00\x18\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00@\x80\xa0@\xd0\x90p\xa0`\x80P\x00\x00\x00\x00\xc0@` 0\x10\x00\x00\x10\x000\x10'),
                            bytearray(b'\x00\xff\x07\xe7\x80~\xf8\x07\xf8\x07\x1f\x00\x00\x07\x00\x00\x00\x00\xf8\xe0\xff~\xff\x07\xff\x07\x1f\x00\x07\x07\x00\x00'),
                            bytearray(b'\xc0P\x80\xb0\x10` \xc0`\x80\xc0\x00\x00\x80\x00\x000\x10p0\xf0`\xe0\xc0\xe0\x80\xc0\x00\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=147, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x000\xf0\xf0\x03\xff\xf0\x0f\xff\x00\xff\x00\xe7\xf8\x0e\xcf\xf00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xc0'),
                            bytearray(b'\x00\x01\x01\xf9\xf1\xfe\x03\xfc\xf0\x0f\xff\x00\xff\x00?\xc0\x01\x01\xfe\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'<?\x00\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xff\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=106),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00\x00\x00\x07\x07\x1f\x1f????\x1f\x1f\x07\x07\x00\x00'),
                            bytearray(b'\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\x00\x00\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
                Mold(28, gridplane=False,
                    tiles=[
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
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xcc|\x85\xd7(\xcf\x08\x03\xec\x1f\xf0\xff\x00\xc1>\xfc\xcc\x03\x01\x00\x000\x00\x18\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00@\x80\xa0@\xd0\x90p\xa0`\x80P\x00\x00\x00\x00\xc0@` 0\x10\x00\x00\x10\x000\x10'),
                            bytearray(b'\x00\xff\x07\xe7\x80~\xf8\x07\xf8\x07\x1f\x00\x00\x07\x00\x00\x00\x00\xf8\xe0\xff~\xff\x07\xff\x07\x1f\x00\x07\x07\x00\x00'),
                            bytearray(b'\xc0P\x80\xb0\x10` \xc0`\x80\xc0\x00\x00\x80\x00\x000\x10p0\xf0`\xe0\xc0\xe0\x80\xc0\x00\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=114),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x000\xf0\xf0\x03\xff\xf0\x0f\xff\x00\xff\x00\xe7\xf8\x0e\xcf\xf00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xc0'),
                            bytearray(b'\x00\x01\x01\xf9\xf1\xfe\x03\xfc\xf0\x0f\xff\x00\xff\x00?\xc0\x01\x01\xfe\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'<?\x00\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xff\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=114),
                    ]
                ),
                Mold(29, gridplane=False,
                    tiles=[
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
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x03\x00\x07\x04\x0f\x00\x1f\x00? \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x00\x00'),
                            bytearray(b'\x02\x02\x04\x03\xc0/\xf0\x0f\xff\x00\xff\x00\xff\x00\xff\x00\x01\x00\x0b\x00\x1f\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'? 3<\x1f\\\x0e\x0f\x03C \x08 X`N\x00\x00@\x00`@p\x00|@\x7fH\x7fX/^'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\x0e\xf1\xbb\xff\xc3\xc3\x01\x01\x01\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<\x00\xfe\x00\xff\x06'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\xcc|\x85\xd7(\xcf\x08\x03\xec\x1f\xf0\xff\x00\xc1>\xfc\xcc\x03\x01\x00\x000\x00\x18\x08\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00@\x80\xa0@\xd0\x90p\xa0`\x80P\x00\x00\x00\x00\xc0@` 0\x10\x00\x00\x10\x000\x10'),
                            bytearray(b'\x00\xff\x07\xe7\x80~\xf8\x07\xf8\x07\x1f\x00\x00\x07\x00\x00\x00\x00\xf8\xe0\xff~\xff\x07\xff\x07\x1f\x00\x07\x07\x00\x00'),
                            bytearray(b'\xc0P\x80\xb0\x10` \xc0`\x80\xc0\x00\x00\x80\x00\x000\x10p0\xf0`\xe0\xc0\xe0\x80\xc0\x00\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=150, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x000\xf0\xf0\x03\xff\xf0\x0f\xff\x00\xff\x00\xe7\xf8\x0e\xcf\xf00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xc0'),
                            bytearray(b'\x00\x01\x01\xf9\xf1\xfe\x03\xfc\xf0\x0f\xff\x00\xff\x00?\xc0\x01\x01\xfe\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xfc\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'<?\x00\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xff\xf1\xff\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=115),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=2, mold_id=8),
                        AnimationSequenceFrame(duration=2, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=15),
                        AnimationSequenceFrame(duration=2, mold_id=16),
                        AnimationSequenceFrame(duration=2, mold_id=17),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=6, mold_id=14),
                        AnimationSequenceFrame(duration=6, mold_id=18),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=4, mold_id=21),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=20),
                        AnimationSequenceFrame(duration=2, mold_id=19),
                        AnimationSequenceFrame(duration=2, mold_id=18),
                        AnimationSequenceFrame(duration=6, mold_id=22),
                        AnimationSequenceFrame(duration=2, mold_id=23),
                        AnimationSequenceFrame(duration=2, mold_id=24),
                        AnimationSequenceFrame(duration=6, mold_id=25),
                        AnimationSequenceFrame(duration=2, mold_id=26),
                        AnimationSequenceFrame(duration=2, mold_id=27),
                        AnimationSequenceFrame(duration=2, mold_id=28),
                        AnimationSequenceFrame(duration=2, mold_id=29),
                        AnimationSequenceFrame(duration=4, mold_id=28),
                    ]
                ),
            ],
        ),
    ),
    palette_id=SPAL702_MALLOW_PUNCH,
    palette_offset=0,
    unknown_num=0,
)
