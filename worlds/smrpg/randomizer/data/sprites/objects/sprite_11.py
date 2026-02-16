# SPR0011_TOADSTOOL_NONPROTAGONIST_5

from randomizer.data.variables.sprite_palette_names import SPAL659_TOADSTOOL_SLAP_ATTACK
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
        252,
        length=392,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x80\x00\x00\x80@\xc0@\xc0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\xc0\x00\xc0\x00\x80@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x08\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x03\x0b\x15\x0f'),
                            bytearray(b'\x00\x00\x18\x00\x18\x00\x1c\x00\x0ep\x06\xf8\xc78\xc3<\x00\x00\x18\x18\x10\x10\x14\x14\nz\x80\xc8\xc5\r\xe2>'),
                            bytearray(b'\x1a\x16\x16\x0e8\x00\xfe\x04u\x008\x008\x00|\x00\x01\x169\x0e\x7f\x00\xff\x04\x7f\x00?\x00?\x00\x7f\x00'),
                            bytearray(b'\xe1\x1e\xe1>\x03\xfe\xa6?\x7f\x7fy\x7f8:\x15\x10\xe0>\xc1\x7f\xc1\xff\xc0>\x81~\x81~\xc4;\xef\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x80\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xd0\xf0\xd0\xf0\x80@\x00\xc0\x00\xc0@\xa0`\x90 \xd00\xc80\xc8'),
                            None,
                            bytearray(b'\x100\xd00\xf0\xb0\xe0`hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x88\xe0\x18h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00'),
                            bytearray(b'\x0f\x01\xe9\x01\xc1\x01\xe3\x03\xe1\x01\xe1\x01\xf0\x00\xf0\x00\xfe\x01\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfe\x01\xff\x00\xff\x00'),
                            bytearray(b'\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xf0\x00\xfc\x00\xff\x80\xff\xff\xfe\xfc\xfb\xe3\xfb\xc3\x7f\x7f\xff\x00\xff\x00\xff\x80\xff\xff\xfe\xfd\xfb\xe4\xfb\xc4\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x18\x98d\xf8\x04p\x88p\x80\x00\x00\x00\x00\x00\x00\x98\x98||\xdc\xdc\xf8\xf8\xf0\xf0'),
                            None,
                            bytearray(b'`\x80`\x80`\x80\xe0\x00\xc0 \xc0 \xc0\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xa0\xa0\xa0\xa0  @\xc0\xc0\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x08\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x03\x0b\x15\x0f'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x01\x01p\x01\xf2\xc78\xc0?\x00\x00\x00\x00\x00\x00\x01\x01\x01q\x83\xc3\xc4\x0c\xe3?'),
                            bytearray(b'\x1a\x16\x16\x0e8\x00\xfe\x04u\x008\x008\x00|\x00\x01\x169\x0e\x7f\x00\xff\x04\x7f\x00?\x00?\x00\x7f\x00'),
                            bytearray(b'\xe1\x1e\xe1>\x03\xfe\xa7>~\x7fx~8:\x15\x11\xe1>\xc1~\xc1\xfe\xc1>\x81\x7f\x80\x7f\xc4;\xef\x10'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=100),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x80\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xd0\xf0\xd0\xf0\x80@\x00\xc0\x00\xc0@\xa0`\x90 \xd00\xc80\xc8'),
                            None,
                            bytearray(b'\x100\xd00\xf0\xb0\xe0`hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x88\xe0\x18h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00'),
                            bytearray(b'\x0f\x01\xe9\x01\xc1\x01\xe3\x03\xe1\x01\xe1\x01\xf0\x00\xf0\x00\xfe\x01\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfe\x01\xff\x00\xff\x00'),
                            bytearray(b'\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xf0\x00\xfc\x00\xff\x80\xff\xff\xfe\xfc\xfb\xe3\xfb\xc3\x7f\x7f\xff\x00\xff\x00\xff\x80\xff\xff\xfe\xfd\xfb\xe4\xfb\xc4\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=100),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=101),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xb0\x90p\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00p\x88\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x06\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x06\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xc1\x01\xf3\x00\xff\x80\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xfe\x01\xff\x00\xff\x80\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'2\xf20\xf00\xf0 \xe0`\xe0`\xe0\xc0\xc0\xd0\xf0\x0c\xf2\n\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xf0 \xd00\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x0f\x00\x1f ?\x10\x1f`\x07r\x03\x00\x00\x00\x01\x00\x0c\x00\x10\x000 \x18x\x06|\x03'),
                            None,
                            bytearray(b's\x03{\x038\x00<\x00\x1e\x00\x0f\x00\x07\x00\x07\x00|\x03|\x03?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x07\x00'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xff\xf0\xffx\x7f<?\x1f\x1f\x83\x03\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\xc0?\xe0\x1f\xfc\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x11\x190?0? ?\x00\x00\x00\x00\x00\x00\x00\x00\x02\x19\x00>\x00<\x00<'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x90\x80\x1e\xc0\x1a\xe0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x000\xb0\x0en\x1a6\t\x19'),
                            bytearray(b'\x00\x7f\x00\xff\x00\xff\x01\xff\x01\xff\x00\xff\x00\xff\x00\xff\x00O\x00\x07\x00\x07\x00\x07\x00\x03\x00\x01\x00\x00\x00\x03'),
                            bytearray(b'\x0c\xf8\x06\xfe\x06\xfe\xce\xfe\xfe\xfe\xfe\xfe~\xff\x1b\xfb\x07\x1f\x00\x9e\x01\xfe\x01\xfe\x01\xfe\x00\xfe\x00\xff\x04\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=100),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xb0\x90p\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00p\x88\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x06\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x06\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xc1\x01\xf3\x00\xff\x80\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xfe\x01\xff\x00\xff\x80\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'2\xf20\xf00\xf0 \xe0`\xe0`\xe0\xc0\xc0\xd0\xf0\x0c\xf2\n\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xf0 \xd00\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=117),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x0f\x00\x1f ?\x10\x1f`\x07r\x03\x00\x00\x00\x01\x00\x0c\x00\x10\x000 \x18x\x06|\x03'),
                            None,
                            bytearray(b's\x03{\x038\x00<\x00\x1e\x00\x0f\x00\x07\x00\x07\x00|\x03|\x03?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x07\x00'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xff\xf0\xffx\x7f<?\x1f\x1f\x83\x03\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\xc0?\xe0\x1f\xfc\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x11\x190?0? ?\x00\x00\x00\x00\x00\x00\x00\x00\x02\x19\x00>\x00<\x00<'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x90\x80\x1e\xc0\x1a\xe0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x000\xb0\x0en\x1a6\t\x19'),
                            bytearray(b'\x00\x7f\x00\xff\x00\xff\x01\xff\x01\xff\x00\xff\x00\xff\x00\xff\x00O\x00\x07\x00\x07\x00\x07\x00\x03\x00\x01\x00\x00\x00\x03'),
                            bytearray(b'\x0c\xf8\x06\xfe\x06\xfe\xce\xfe\xfe\xfe\xfe\xfe~\xff\x1b\xfb\x07\x1f\x00\x9e\x01\xfe\x01\xfe\x01\xfe\x00\xfe\x00\xff\x04\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=101),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xb0\x90p\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00p\x88\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x06\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x00\x0f\x06\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xc1\x01\xf3\x00\xff\x80\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xfe\x01\xff\x00\xff\x80\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'2\xf20\xf00\xf0 \xe0`\xe0`\xe0\xc0\xc0\xd0\xf0\x0c\xf2\n\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xf0 \xd00\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=387, y=117),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x01\x00\x0f\x00\x1f ?\x10\x1f`\x07r\x03\x00\x00\x00\x01\x00\x0c\x00\x10\x000 \x18x\x06|\x03'),
                            None,
                            bytearray(b's\x03{\x038\x00<\x00\x1e\x00\x0f\x00\x07\x00\x07\x00|\x03|\x03?\x00?\x00\x1f\x00\x0f\x00\x07\x00\x07\x00'),
                            bytearray(b'\x00\xff\x80\xff\xc0\xff\xf0\xffx\x7f<?\x1f\x1f\x83\x03\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\xc0?\xe0\x1f\xfc\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=371, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x11\x190?0? ?\x00\x00\x00\x00\x00\x00\x00\x00\x02\x19\x00>\x00<\x00<'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x90\x80\x1e\xc0\x1a\xe0\x0f\xf0\x00\x00\x00\x00\x00\x00\x00\x000\xb0\x0en\x1a6\t\x19'),
                            bytearray(b'\x00\x7f\x00\xff\x00\xff\x01\xff\x01\xff\x00\xff\x00\xff\x00\xff\x00O\x00\x07\x00\x07\x00\x07\x00\x03\x00\x01\x00\x00\x00\x03'),
                            bytearray(b'\x0c\xf8\x06\xfe\x06\xfe\xce\xfe\xfe\xfe\xfe\xfe~\xff\x1b\xfb\x07\x1f\x00\x9e\x01\xfe\x01\xfe\x01\xfe\x00\xfe\x00\xff\x04\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=379, y=101),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x100\xd00\xf0\xb0\xe0`hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x88\xe0\x18h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xf0\x00\xfc\x00\xff\x80\xff\xff\xfe\xfc\xfb\xe3\xfb\xc3\x7f\x7f\xff\x00\xff\x00\xff\x80\xff\xff\xfe\xfd\xfb\xe4\xfb\xc4\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x80\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xd0\xf0\xd0\xf0\x80@\x00\xc0\x00\xc0@\xa0`\x90 \xd00\xc80\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00'),
                            bytearray(b'\x0f\x01\xe9\x01\xc1\x01\xe3\x03\xe1\x01\xe1\x01\xf0\x00\xf0\x00\xfe\x01\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfe\x01\xff\x00\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x80\x00\x00\x80@\xc0@\xc0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\xc0\x00\xc0\x00\x80@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x08\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x03\x0b\x15\x0f'),
                            bytearray(b'\x00\x00\x18\x00\x18\x00\x1c\x00\x0ep\x06\xf8\xc78\xc3<\x00\x00\x18\x18\x10\x10\x14\x14\nz\x80\xc8\xc5\r\xe2>'),
                            bytearray(b'\x1a\x16\x16\x0e8\x00\xfe\x04u\x008\x008\x00|\x00\x01\x169\x0e\x7f\x00\xff\x04\x7f\x00?\x00?\x00\x7f\x00'),
                            bytearray(b'\xe1\x1e\xe1>\x03\xfe\xa6?\x7f\x7fy\x7f8:\x15\x10\xe0>\xc1\x7f\xc1\xff\xc0>\x81~\x81~\xc4;\xef\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=100),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x100\xd00\xf0\xb0\xe0`hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x88\xe0\x18h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00\x0f\x00\x0f\x0c\x0f\x0f\x0f\x0f\x0f\x0f\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\xf0\x00\xfc\x00\xff\x80\xff\xff\xfe\xfc\xfb\xe3\xfb\xc3\x7f\x7f\xff\x00\xff\x00\xff\x80\xff\xff\xfe\xfd\xfb\xe4\xfb\xc4\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x00\x80\x80\x80\xc0\xc0\xe0\xe0\xc0\xe0\xd0\xf0\xd0\xf0\x80@\x00\xc0\x00\xc0@\xa0`\x90 \xd00\xc80\xc8'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00\x7f\x00\x7f\x00\xff\x00\xff\x00\x7f\x00\x7f\x00?\x00\x1f\x00'),
                            bytearray(b'\x0f\x01\xe9\x01\xc1\x01\xe3\x03\xe1\x01\xe1\x01\xf0\x00\xf0\x00\xfe\x01\xfe\x01\xfe\x01\xfc\x03\xfe\x01\xfe\x01\xff\x00\xff\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=116),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x00\x80\x00\x80\x00\x80\x00\x00\x80@\xc0@\xc0\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\xc0\x00\xc0\x00\x80@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x00\x0f\x08\x06\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x07\x03\x0b\x15\x0f'),
                            bytearray(b'\x00\x00\x18\x00\x18\x00\x1c\x00\x0ep\x06\xf8\xc78\xc3<\x00\x00\x18\x18\x10\x10\x14\x14\nz\x80\xc8\xc5\r\xe2>'),
                            bytearray(b'\x1a\x16\x16\x0e8\x00\xfe\x04u\x008\x008\x00|\x00\x01\x169\x0e\x7f\x00\xff\x04\x7f\x00?\x00?\x00\x7f\x00'),
                            bytearray(b'\xe1\x1e\xe1>\x03\xfe\xa6?\x7f\x7fy\x7f8:\x15\x10\xe0>\xc1\x7f\xc1\xff\xc0>\x81~\x81~\xc4;\xef\x11'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=100),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=100),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=100),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=100),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x90\xf0\x10\xf0\xf0\xf0``hh\x90\x10\xe0\xe0\x00\x00\xf0\x08\xf0\x08\xf0\x08`\x98h\x98\x90p\xe0\xe0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00\x0f\x03\x0f\x07\x0f\x07\x0f\x0c\x0f\x08\x07\x04\x03\x03\x00\x00'),
                            bytearray(b'\xff\xe0\xfe\xc0\xf3\xc3\xe7\x07\x97\x07\x17\x07\x97\x87\x7f\x7f\xff\xe0\xfe\xc1\xf3\xcc\xe7\x18\x97h\x17\xe8\x97\xe8\x7f\x7f'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\xf00\xf0p\xf0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\xd00\x08\xf4\x08\xf0\x00\xf0\x10\xe0\x10\xe0\xe0\x10\xe0\x10\xf0\x08'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'9\x01\x1c\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03>\x01\x1f\x00\x1f\x00\x0f\x00\x07\x00\x07\x00\x07\x02\x07\x03'),
                            bytearray(b'\xc0\xff0?\x08\x0f\xc3\x03\xc0\x00\xe0\x00\xf8\x00\xfc\xc0\x00\xff\xc0?\xf0\x0f\xfc\x03\xff\x00\xff\x00\xff\x00\xff\xc0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=117),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'0\xc0\xf8\x00`\x00\x04\xfc\x04\xfe\x06\xfe\x06\xfe\x04\xfc\xe0\xe0\x98\x180\xb8\x00\xfc\x00~\x00\x0e\x00\x1e\x02\xfc'),
                            None,
                            bytearray(b'\x04\xfc\x08\xf8\x08\xfa\x08\xfe\x0e\xf8\x0e\xf8\x0c\xfe\x18\xf8\x02\xfc\x04\xf8\x06\xfa\x06\xfe\x06\xfe\x02\xfa\x06\xfa\x00\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00'),
                            bytearray(b'\x01\x00\x00\x04\x10\x1f\x00\xdf@\x7f0?\x9c\x1f\x8e\x8f\x03\x03\x00\x07\x00\x19\x00\xdc\x80p\xc0<\xe0\x1cp\x8f'),
                            bytearray(b'\x01\x01\x01\x01\x03\x03\x04\x07\x08\x0f\x18\x1f\x1c\x1f>\x0f\x00\x01\x00\x01\x00\x03\x00\x07\x00\x0f\x00\x1f\x00\x1f0\x0f'),
                            bytearray(b'\x8e\xcf\x9e\xff\x87\xff\x80\xff\x80\xff\x00\xff\x00\xff\x80\xff0\xcf\x00\xff\x00\xff\x00\xc7\x00\xc3\x00\xc7\x00\xcf\x00\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=101),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x00\x00@@\x80\x80\x00\x00\x00\x00\x80\xc0\x80@\x80@\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x7f\x1f\x7f>\x7f>\x7f`|@8 \x1c\x1c\x03\x03\x7f\x1f\x7f>\x7f>\x7f`|C8\'\x1c\x1f\x03\x03"),
                            bytearray(b'\xff`\xfe?\x9f\x1f;;\xbb;\xbc8\xbf?\xf8\xf8\xff`\xff>\x9f`;\xc4\xbbD\xbcC\xbfG\xf8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x00?\x18?\x1e?\x00?\x00?\x00\x1f\x00\x1f\x00?\x00?\x18?\x1e'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xf0\x00\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=100),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x80\x80\x80\x80\x80\x80\x00\x00@@\x80\x80\x00\x00\x00\x00\x80\xc0\x80@\x80@\x00\xc0@\xc0\x80\x80\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b"\x7f\x1f\x7f>\x7f>\x7f`|@8 \x1c\x1c\x03\x03\x7f\x1f\x7f>\x7f>\x7f`|C8\'\x1c\x1f\x03\x03"),
                            bytearray(b'\xff`\xfe?\x9f\x1f;;\xbb;\xbc8\xbf?\xf8\xf8\xff`\xff>\x9f`;\xc4\xbbD\xbcC\xbfG\xf8\xf8'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x08\xf8\x00\xf8\x00\xf0\x10\xf0\xe0\xe0\xe0\xe0\xc0\xc0@\x00\x008\x008\x08\xf0\x00\xf0\x10\xe0\x00\xe0\x00\xc0\xc0\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=117),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f\x10\x1f\x02\x03\x00\x00\x00\x00\x00\x01\x00\x03\x00\x07\x00\x1f \x1f<\x03'),
                            None,
                            bytearray(b'8\x00<\x00<\x00\x1e\x00\x1f\x00?\x00?\x18?\x1e?\x00?\x00?\x00\x1f\x00\x1f\x00?\x00?\x18?\x1e'),
                            bytearray(b'\x80\xffx\x7f<???\x9f\x1f\xc7\x07\xe3\x03\xf0\x00\x00\xf0\x80|\xc0?\xc0?\xe0\x1f\xf8\x07\xfc\x03\xff\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\x80\xcf`\x7f\xb0\xbf\x00\x00\x00\x00\x00\x00\x01\x01\x00\x07\x00\xc8\x00|@\xbe'),
                            bytearray(b'\x00\x00\x00\x00`\x00\xb8\x04\xf4@\x04\xf0\x00\xfc\x02\xfe\x00\x00\x00\x00@@\xfc\xbc\xac\xec\x0c\x8c\x00\x1c\x00\x06'),
                            bytearray(b'P\x7f\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\x7f\x00\xff\x00\xc7\x00\xc0\x00\xc0\x00\x80\x00\x80\x00\xc0'),
                            bytearray(b'\x02\xfe\x01\xff\x06\xfe\x06\xfe\x0c\xfc\x08\xf8\x08\xf8\x08\xf8\x00\xfe\x00\xff\x01\xfe\x00~\x02<\x048\x008\x008'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=101),
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
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=5),
                        AnimationSequenceFrame(duration=2, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=4),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=6),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=2, mold_id=10),
                        AnimationSequenceFrame(duration=2, mold_id=11),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=8, mold_id=14),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=14),
                    ]
                ),
            ],
        ),
    ),
    palette_id=SPAL659_TOADSTOOL_SLAP_ATTACK,
    palette_offset=0,
    unknown_num=0,
)
