# SPR0123_YOSHI_BABY_EGG

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL478_YOSHI_BABY_EGG
sprite = CompleteSprite(
    animation=AnimationPack(361, length=666, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xc0\x01\x00\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff\x00>\x00\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd04\x88d\x88d\x14\xcc\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x0c\x00\x1c\x00\x1c\x00<'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x18\x17\x18\x17\x183\x04\x13 \x16\x08\x00\x00 \x00 \x00 \x00 \x00\x008\x00<'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~\xf0p\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x01p\x0f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=135),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=119),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=387),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=371),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=371),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=383),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=367),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=367),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=376),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=360),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=360),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=375),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=359),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=357),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=357),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=354),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=352),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=352),
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xbdf\xbdf\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbdf\xbdf<\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xe0\x00\xc0`\x00\x80\x80\xa0\x00\xfcX$h\xc4T\x8c\x00\xc0\x00\xc0`\x80`\x808\xc40\xdc \xfc@|'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x01\x00\x01\x02\x00\x03\x04\x01\x05\x04\x00\x00\x00\x00\x00\x01\x00\x01\x00\x03\x00\x03\x00\x07\x04\x03'),
                            bytearray(b'\x00\x00\xa5\x18ZB~B\xc3<\x18\xe7\x99\x18\x18<\x00\x00\x00\xffB\xbdB\xbd\x00\xff\x00\xff\x18\xe7\x18\xe7'),
                            bytearray(b'\x05\x00\x03\x06\x08\x01\t\x05\x00\x1f\x10\x0f;\x06\x17 \x00\x03\x00\x03\x0e\x01\x0e\x01<\x03<\x13\x0c:\x04<'),
                            bytearray(b'\x18\x18\x00\x00\x81\x00~\x81\xc3\xff\xc5\x02e\xc3\xa8U\x18\xe7\x00\xff\x00\xff\x00\xff\x00\xff\xfe\x01^\xa0\x1cb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=367),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=351),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=351),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=135),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=387),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=371),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=371),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=383),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=367),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=367),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x04\x04$\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x1f~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x04\x04$\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x1f~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=376),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=360),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=360),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=375),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=359),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x04\x04$\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x1f~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x04\x04$\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x1f~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=357),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=357),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=354),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x04\x04$\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x1f~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x04\x04$\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x1f~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=374),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=352),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=352),
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=375),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00P\x00\x04\x04\x04\x05A\x02\x00\x00\x00\x00\x07\x01\x0f\x07\xdf\x8f\xff\xff\x7f\x7f~>'),
                            None,
                            bytearray(b'\x02\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00?=?\x1e?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=375),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x00\x00 \rA\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x13~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x06\x00\x08\x00\x10\x00\x00\x00 \rA\x02\x00\x00\x00\x00\x07\x01\x0f\x07\x1f\x0f\x1f\x1f?\x13~>'),
                            None,
                            bytearray(b'\x82\x01!\x00 \x004\x00\x1c \x0f\x10\x00\x0f\x00\x00\xff}\xff\xde?\x1f?\x1f?\x17\x1f\x08\x0f\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=367),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=351),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=351),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00 `p\xd0\xdc\x08\x04\x88\x04T\x8c\x00\x00\x00\x00\x00\x00\x00\x00(\x04\xf0\x0c\xe0\x1c@<'),
                            None,
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x02\x02\x07\x04\t\x0e\x00\x1f\x10\x0f9\x06\x17 \x00\x00\x00\x00\x03\x00\x07\x00?\x00?\x10\x0e8\x04<'),
                            bytearray(b'\x00\x08\x00\x1c>>\x0f\x0f\xe3\x03x\x80\x1d\xe0\x8dp\x00\x00\x00\x00\x00\x00p\x00\xfc\x00\xff\x00\xfe\x00|\x02'),
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xe0\x19\x10\xe1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8&\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=135),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x03\x03\x03\x03\x07\x07?\x07?\x1f\x0e>\x04<'),
                            None,
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe|~'),
                            bytearray(b'\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=387),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=371),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=371),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x03\x03\x03\x03\x07\x07?\x07?\x1f\x0e>\x04<'),
                            None,
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe|~'),
                            bytearray(b'\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
                Mold(21, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=383),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=367),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=367),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x03\x03\x03\x03\x07\x07?\x07?\x1f\x0e>\x04<'),
                            None,
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe|~'),
                            bytearray(b'\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                    ]
                ),
                Mold(22, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x03\x03\x03\x03\x07\x07?\x07?\x1f\x0e>\x04<'),
                            None,
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe|~'),
                            bytearray(b'\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=376),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=360),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=360),
                    ]
                ),
                Mold(23, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x03\x03\x03\x03\x07\x07?\x07?\x1f\x0e>\x04<'),
                            None,
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff~\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff~~\xff\xff\xff\xff\xfe\xfe|~'),
                            bytearray(b'\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=375),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=359),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=359),
                    ]
                ),
                Mold(24, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x01\x01\x03\x03\x03\x03\x07\x07\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x03\x03\x03\x03\x07\x07?\x07?\x1f\x0e>\x04<'),
                            None,
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=128),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00~~'),
                            None,
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff~\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff~~\xff\xff\xff\xff\xfe\xfe|~'),
                            bytearray(b'\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xc0\xc0\xc0\xc0\xe0\xe0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=373),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=357),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=357),
                    ]
                ),
                Mold(25, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80\xe0\xe0\xc0\xc0\xf0\xf0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xe0\xe0\xc0\xc0\xf0\xf0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00**~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00**~~'),
                            bytearray(b'\x01\x01\x07\x07\x03\x03\x0f\x0f\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x07\x07\x03\x03\x0f\x0f?\x07?\x1f\x0e>\x04<'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff~\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff~~\xff\xff\xff\xff\xfe\xfe|~'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=370),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=354),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=354),
                    ]
                ),
                Mold(26, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80\xe0\xe0\xc0\xc0\xf0\xf0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xe0\xe0\xc0\xc0\xf0\xf0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00**~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00**~~'),
                            bytearray(b'\x01\x01\x07\x07\x03\x03\x0f\x0f\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x07\x07\x03\x03\x0f\x0f?\x07?\x1f\x0e>\x04<'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff~\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff~~\xff\xff\xff\xff\xfe\xfe|~'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=368),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=352),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=352),
                    ]
                ),
                Mold(27, gridplane=False,
                    tiles=[
                        Tile(mirror=True, invert=False, format=0, length=4, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x081$9\x13\x1d\x19\x1f\x0e\x0c\x01\x06\x00\x03\x00\x00\x00>\x00>\x00\x1e\x00\x1e\x03\x0c\x07\x00\x03\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=136),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x80\x80\xe0\xe0\xc0\xc0\xf0\xf0\xe0\xfc\xf8\xf4\xe8\xe4T\xcc\x80\x80\xe0\xe0\xc0\xc0\xf0\xf0\xf8\xe4\xf0\xfc\xe0\xfc\x00|'),
                            bytearray(b'\xf89\x10\xf1\x01\xff\xff\xff\x00\x00\xf0\x0f\x1f\xff\x7f\xff8>\x10\x1e\x00\x00\x00\x00\xff\x00\xc0?\x80\x7f\x80\x7f'),
                            bytearray(b'T\xccl\xdc\xa8\x988\x18@0\x80`\x00\xc0\x00\x00\x00<\x00<@8\xe0\x18\xf0\x00\xe0\x00@\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=128),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00**~~\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00**~~'),
                            bytearray(b'\x01\x01\x07\x07\x03\x03\x0f\x0f\x07\x1f\x1f\x0f?\x06\x17$\x01\x01\x07\x07\x03\x03\x0f\x0f?\x07?\x1f\x0e>\x04<'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff\xff~\xff\xff\xff\xff\xfe\xff\xfd|\xff\xff\xff\xff\xff\xff~~\xff\xff\xff\xff\xfe\xfe|~'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=120),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x008\x00\x10\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=367),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00@\x00\xa0\x80\xa0\x80\xc0\xc0\xd0\xf0\x00\x00\x00\x00\x00\x80\x00\xc0\x80`\x80`\xd0 \xc0\x00'),
                            None,
                            bytearray(b'\xd80\xd80\xd40\xd40\xd00\x80`\x80`\x00@\x08\x00\x08\x00\x0c\x00\x0c\x00\x00\x08\x00\x10\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=351),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x02\x00\x05\x01\x05\x01\x0b\x03\x0b\x03\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x01\x06\x03\x0c\x03\x0c'),
                            bytearray(b'<<\xbb\xc4|\x84\xff\x87\xff\x87\xff\x87\xff\x83\xff\x00\x00\x00\x00\x03\x04\x03\x87\x00\x87\x00\x87\x00\x83\x00\x00\x00'),
                            bytearray(b'\x17\x06\x17\x187\x187\x187\x18\x17\x18\x02\x04\x00\x00\x16\x08\x00\x00 \x00 \x00 \x00\x00\x00\x00\x08\x00\x04'),
                            bytearray(b'\xff\x00\xff<\xff~\xff\x7f\xff\x7f\xff\x7f\xfe~pp\x00\x00<\x00~\x00\x7f\x00\x7f\x00\x7f\x00~\x00p\x0c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=351),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=4),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                        AnimationSequenceFrame(duration=4, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=3),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=10),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=4, mold_id=12),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=17),
                        AnimationSequenceFrame(duration=4, mold_id=18),
                        AnimationSequenceFrame(duration=4, mold_id=17),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=11),
                        AnimationSequenceFrame(duration=6, mold_id=10),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=19),
                        AnimationSequenceFrame(duration=4, mold_id=20),
                        AnimationSequenceFrame(duration=4, mold_id=21),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=22),
                        AnimationSequenceFrame(duration=4, mold_id=23),
                        AnimationSequenceFrame(duration=4, mold_id=24),
                        AnimationSequenceFrame(duration=4, mold_id=25),
                        AnimationSequenceFrame(duration=4, mold_id=26),
                        AnimationSequenceFrame(duration=4, mold_id=27),
                        AnimationSequenceFrame(duration=4, mold_id=26),
                        AnimationSequenceFrame(duration=4, mold_id=25),
                        AnimationSequenceFrame(duration=4, mold_id=24),
                        AnimationSequenceFrame(duration=4, mold_id=23),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=21),
                        AnimationSequenceFrame(duration=4, mold_id=20),
                        AnimationSequenceFrame(duration=6, mold_id=19),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL478_YOSHI_BABY_EGG,
    palette_offset=0,
    unknown_num=0
)
