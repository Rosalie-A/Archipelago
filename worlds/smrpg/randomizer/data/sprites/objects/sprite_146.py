# SPR0146_COMMANDER_TROOPA

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL566_COMMANDER_TROOPA
sprite = CompleteSprite(
    animation=AnimationPack(154, length=381, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00PP\x0c\x0c\x84\xb4\x0cl\x1c\x1c\x0c\x0c\xa0\xb0\x00\x00`\x10t\x0c\xcc\x04\x9c\x04\xd0,\xcc<P\xb0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=129),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'88t|\\\x1c>>,<\x00\x00\x00\x00\x00\x0088l\x1c\x00|\x06><<\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=129),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x18\x00|\x00\xf0\x18\xe00\xc0@\x00\x00\x00\x00\x00\x00\x18\x00\x0c\x00\x00\x08\x00\x10\x80\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=118),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=366),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=123),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00?\x12\xff\x00\xfc\x10\xc0\x00\x00\xc0\x00\xc0\x00\xc0\x00\x00!\x00\x00\x00\x0c\x00\x80@\xc0\xc0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=115),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0f\x00\x1f\x10\x1f\x00\x1f\x10\x1f\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\xc0@\xe0\x00\xf0@\xf0\xc0\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\x000\x00\x10\x00'),
                            bytearray(b'\x1e\x05\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x1a\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b"\x00\xf0\xc2,\x83^\x07\xf8\x07\xd8\x00\xdb\x00m\x80c\x00\xf0\xd0\xfe\xa0\xfc \xf8\'\xf8\'\xff\xb3\xff_\xff"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=107),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00PP\x0c\x0c\x84\xb4\x0cl\x1c\x1c\x0c\x0c\xa0\xb0\x00\x00`\x10t\x0c\xcc\x04\x9c\x04\xd0,\xcc<P\xb0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=384),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'88t|\\\x1c>>,<\x00\x00\x00\x00\x00\x0088l\x1c\x00|\x06><<\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=384),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=120),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=112),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=125),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x1c\x18~0\xfe\xc0\xfe@\xfc\x80\x00\x00\x00\x00\x00\x00\x04\x00H\x06\x00\x1e\x00>\x00|'),
                            None,
                            bytearray(b'\xf8\x00\xf0\x00\xe0\x00\xe0\x00\xc0\x00\x00\x80\x00\x80\x00\xe0\x00\xf8\x00\xf0\x00\xe0\x00\xe0\x00\xc0\xc0\xc0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=109),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x1c\x1c~\x10\xfc\x00\xfc \xfc@\xf9\x81\xf1\x10\x00\x00\x00\x00\x08\x06\x10\x0c\x00\x1c8\x04`\x18\xd00'),
                            bytearray(b'\x02\x01\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x00\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x13\xe3\xc3=\x87b\x07\xf8\x07\xf8\x00\xde\x00\\\x80q\x00\xf0\xc0\xfc\x98\xf9\x0c\xf3$\xfb!\xff\xa3\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=109),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00PP\x0c\x0c\x84\xb4\x0cl\x1c\x1c\x0c\x0c\xa0\xb0\x00\x00`\x10t\x0c\xcc\x04\x9c\x04\xd0,\xcc<P\xb0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=130),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'88t|\\\x1c>>,<\x00\x00\x00\x00\x00\x0088l\x1c\x00|\x06><<\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=130),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfe\xfe\xfc\xf8\xf8\xf8tt.,\x164\x08\x08\x00\x00\xfe\xfe\xe8\xf4\xd8\xe4`|\x04:0.\x08\x08\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=129),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'^M\x1a\x0c6\x0f\x07\x03\x07\x01\x07\x04\x07\x04\x0f\x06PC\x03\x05!\t\x01\x01\x00\x01\x01\x00\x02\x04\x00\x0f'),
                            None,
                            bytearray(b'\x0e\x07\x0f\x07\x07\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x00\x0f\x04\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x04\xdf\xf3\x00\x00\x0b\x0b\x08\x08\t\t\x04\x04\x00\x00s\x80\xf3\xff\x07\x08\x03\x0c\x00\x0f\x04\x0b\x04\x07\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=121),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x04\x1f\x10>$>\x00~\x00|\xd0\x10\xf0\x08\xf0\x01\x00\x00\x00\x02\x00\x02\x00\x00\x02\x00\x8c\x00\xe0\x00\xf8'),
                            bytearray(b'\x08\x7f\x00\xa7\x00\xf8\x00\xf8\x80\xfc\xd0\xff\xff\xbf\xff0\xfc\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff~?\x0b\x04'),
                            bytearray(b'\xc00\x04\xf4\x00\x80\x00\x80\x00\\z\x84\xfeb\xff\x1c\xc8\xf8\x0c\xfc\xfc\xfc\xfc\xfc\xec\xfc\xc6\x8c\x9c\x00\xd6='),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=123, y=113),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x07$o@\x1e@O\x12w\x00\x00\x00\x00\x00\x00\x07\x00\x1eP>!\x0f0\x07x'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0``pp\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 `\x80`\x90'),
                            bytearray(b'\xb99+\xbb\xff\xff\xfd\xff\xc1\xcf\xd5\xff]^;\x7fY\xbe\xe8?x\xbf\x12\xff\xce\xff\xfa\xdf\\\x7fZ?'),
                            bytearray(b'XXxx\xf8\xe8\xf8\x00\xf8\x00\xf8\x07\xfc\x03\xfc\x03\x08\xf8\x08\xf8\x18\x88x\x80\x18\xe0\x08\xf7\x04\xfb\x04\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=105),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xfe\xfe\xfc\xf8\xf8\xf8tt.,\x164\x08\x08\x00\x00\xfe\xfe\xe8\xf4\xd8\xe4`|\x04:0.\x08\x08\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=384),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'^M\x1a\x0c6\x0f\x07\x03\x07\x01\x07\x04\x07\x04\x0f\x06PC\x03\x05!\t\x01\x01\x00\x01\x01\x00\x02\x04\x00\x0f'),
                            bytearray(b'\x0c{\x00\xa7\x00\xf8\x00\xf8\x80\xfc\xd0\xff\xff\xbf\xff0\xf8\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff~?\x0b\x04'),
                            bytearray(b'\x0e\x07\x0f\x07\x07\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x01\x0f\x00\x0f\x04\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x04\xdf\xf3\x00\x00\x0b\x0b\x08\x08\t\t\x04\x04\x00\x00s\x80\xf3\xff\x07\x08\x03\x0c\x00\x0f\x04\x0b\x04\x07\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x1f\x08?\x83\x0e\xf8\x00\xe0\x00\x00\x00\x00\x00\x00\x01\x00\x10\x00\x00\x80\x18\xfe\x10\xf0'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xe0\xe0\xe0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00 \x00\x00\xc0\x00\x00\x00\x00'),
                            bytearray(b'\xc00\x04\xf4\x00\x80\x00\x80\x00\\z\x84\xfeb\xff\x1c\xc8\xf8\x0c\xfc\xfc\xfc\xfc\xfc\xec\xfc\xc6\x8c\x9c\x00\xd6='),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=112),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x07$o@\x1e@O\x12w\x00\x00\x00\x00\x00\x00\x07\x00\x1eP>!\x0f0\x07x'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0``pp\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 `\x80`\x90'),
                            bytearray(b'\xb99+\xbb\xff\xff\xfd\xff\xc1\xcf\xd6\xff]^;\x7fY\xbe\xe8?x\xbf\x12\xff\xce\xff\xf9\xdf\\\x7fZ?'),
                            bytearray(b'XXXX\xf8\xf8\xf0\xf0\xd0\xd0\x80\x9f\xfeI\xfc\x03\x08\xf8\x08\xf8(\xd8 \xd0\x00\xf0 \xff\x86\x012\xcf'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=104),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xc00\x04\xf4\x00\x80\x00\x80\x00\\z\x84\xfeb\xff\x1c\xc8\xf8\x0c\xfc\xfc\xfc\xfc\xfc\xec\xfc\xc6\x8c\x9c\x00\xd6='),
                            None,
                            bytearray(b'\xfe\xfe\xfc\xf8\xf4\xf4||><\x1e<\x08\x08\x00\x00\xfe\xfe\xe8\xf4\xc0\xfc`|\x00> >\x08\x08\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=121),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'^M\x1a\x0c6\x0f\x07\x03\x07\x01\x07\x04\x07\x04\x0f\x06PC\x03\x05!\t\x01\x01\x00\x01\x01\x00\x02\x04\x00\x0f'),
                            bytearray(b'L{\x00\xa7\x00\xf8\x00\xf8\x80\xfc\xd0\xff\xff\xbf\xff0\xb0\xff\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff~?\x0b\x04'),
                            bytearray(b'\x0c\x07\x0c\x07\x07\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00\x03\x0f\x03\x0f\x04\x07\x06\x06\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x04\xdf\xf3\x03\x03\n\n\t\t\x0f\x0f\x07\x07\x00\x00s\x80\xf3\xff\x07\x08\x02\r\x00\x0f\x00\x0f\x04\x07\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=121),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x14>4\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x02'),
                            None,
                            bytearray(b'>\x00|\x0c|\x04\xfc\x10\xfc\x04\xf8@8\xe8\x00\xf0$\x1aH<X \x00\xfc\x04\xfc\x18\xe0\x00\xf8\x10\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=105),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x07$o@\x1e@O\x12w\x00\x00\x00\x00\x00\x00\x07\x00\x1eP>!\x0f0\x07x'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\xc0``pp\x00\x00\x00\x00\x00\x00\x00\x80\x80@\xc0 `\x80`\x90'),
                            bytearray(b'\xb99+\xbb\xff\xff\xfd\xff\xc1\xcf\xd7\xff]^;\x7fY\xbe\xe8?x\xbf\x12\xff\xce\xff\xf8\xdf\\\x7fZ?'),
                            bytearray(b'xH|@\xfc\x98\xfc8\xfc8\xfc|\xf8w\xf8w0\xc0\x04\xf8@\xbc\x80|\x04\xf8\x04\xfc\x08\xf7\x08\xf7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=105),
                    ]
                ),
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00PP\x0c\x0c\x84\xb4\x0cl\x1c\x1c\x0c\x0c\xa0\xb0\x00\x00`\x10t\x0c\xcc\x04\x9c\x04\xd0,\xcc<P\xb0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=384),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'88t|\\\x1c>>,<\x00\x00\x00\x00\x00\x0088l\x1c\x00|\x06><<\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=384),
                    ]
                ),
                Mold(7, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00PP\x0c\x0c\x84\xb4\x0cl\x1c\x1c\x0c\x0c\xa0\xb0\x00\x00`\x10t\x0c\xcc\x04\x9c\x04\xd0,\xcc<P\xb0'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=384),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'88t|\\\x1c>>,<\x00\x00\x00\x00\x00\x0088l\x1c\x00|\x06><<\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=388, y=383),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x11\x11@H\x01\x19TU..>>\x00\x00\x00\x00\x1e\x01w\x00d\x03=C\x1a&:>\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=128),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=128),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x11\x11@H\x01\x19TU..>>\x00\x00\x00\x00\x1e\x01w\x00d\x03=C\x1a&:>\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=376, y=383),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=128),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x11\x11@H\x01\x19TU..>>\x00\x00\x00\x00\x1e\x01w\x00d\x03=C\x1a&:>\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=375, y=382),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=128),
                    ]
                ),
                Mold(11, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x11\x11@H\x01\x19TU..>>\x00\x00\x00\x00\x1e\x01w\x00d\x03=C\x1a&:>\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=374, y=381),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1e\x04>\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x02\x00\x0e'),
                            None,
                            bytearray(b'~\x00\xfc@\xf0\x00\xe0\x00\xa0`\x00\xc0\x00\xe0\x00\xe0\x00\x1e\x00<\x80p\x00\xe0`\xe0\xe0\xe0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x01\x01\x00\x03\x00\x07\x04\x07\x00\x0f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00'),
                            bytearray(b'\x00\x00``\xf0\x00\xf0\x00\xf0\x00\xf8\x08\xf8\x10\xf0\x00\x00\x00\x00\x00\x00\x00\x10\x00\x10\x00\x00\x00\x08\x00\x10\x00'),
                            bytearray(b'\x0e\x07\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x08\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x08\xf0\xc0>\x81n\x03\xdc\x03\xfc\x00\xdd\x00N\x80q\x00\xf8\xc0\xfe\x90\xfe%\xf8&\xf9#\xff\xb1\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=108),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=128),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x10\x10\x00@\x0cl\x066\x02\x1a\x06\x06\x1c\x1c\x00\x00`\x10 \x98\x18\x84N\x02f\x02:\x06\x18\x04\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=119),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf0\x00\xf8\x00\xf8\x00\xc4X\x00\x00\x00\x00\x00\x00\x00\x00\x90\x00\x08\x00\x08\x00\x84\x18\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=128, y=119),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x06\x08\x0f\x14\x1f\x04\x1b\x00\x03\x10@<\x00V\x00\x00\x01\x0b\x02\x10\x12\x10\x1e\x16\x07\x0b@\x03!\x08'),
                            bytearray(b'\x00\x00\x10\xd0\x800\xc4\x94\xfc\\tt\xac,:~\x00\x00@\xb00H\x10l\xa0\xfc\x80\xdc\x04\xfc\x9a>'),
                            bytearray(b'\x01\xf1\x00\xe0\x01\xc1\x8b\x0b#/\x7f\x7f\x1d\x1d\x00\x00\x8f\x00\x9e\x01\xbd\x03{\x87._\x7f\x7f\x1c\x1c\x00\x00'),
                            bytearray(b'\x1e^\x9c\x9c\xb5\xbe\xb7\xffw\xfd\xfc\xd8\xf8\x10\xf0\x00\xae\x1e\xec\x1c\x9d\xf7x\xf7\xf8\xf7\xe6\xca\x04\x0cH\xb8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=112, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0\xe0\xe0\xe0\xe0\xe0\x00\xe0\x00\xe0`\xc0\xc0\x00\x00\xe0\xe0\xe0\xe0\xe0\xe0 \xc0\x00 `\xe0\xc0\xc0\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=380),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff|\xbd\xbe/?\x0e.\x1e\x1e\x07\x07\x03\x03\x00\x00}\xfe\xbf\xfe>\x1f#<\x1e\x11\x07\x07\x03\x03\x00\x00'),
                            bytearray(b'\x80C\xc1w\xf7\x8f\xff\xd0?\xf0\xff\xff\xff\xff\x00\x00\xff\x7f\xbf\x1f\x1f\x0fA\xe0\xf6\xf8\xff\xff\xff\xff\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=380),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x1c\x18~0\xfe\xc0\xfe@\xfc\x80\x00\x00\x00\x00\x00\x00\x04\x00H\x06\x00\x1e\x00>\x00|'),
                            None,
                            bytearray(b'\xf8\x00\xf0\x00\xe0\x00\xe0\x00\xc0\x00\x00\x80\x00\x80\x00\xe0\x00\xf8\x00\xf0\x00\xe0\x00\xe0\x00\xc0\xc0\xc0\xe0\xe0\xe0\xe0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=135, y=364),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x01\x00\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x1c\x1c~\x10\xfc\x00\xfc \xfc@\xf9\x81\xf1\x10\x00\x00\x00\x00\x08\x06\x10\x0c\x00\x1c8\x04`\x18\xd00'),
                            bytearray(b'\x02\x01\x00\x0f\x01\x1e\x10\x1f87\xfc\x8b\xffr\xff|\x00\x01\x00\x0f\x01\x1f\x10\x0f\x08Gt\x83u\xf8{\xfc'),
                            bytearray(b'\x13\xe3\xc3=\x87b\x07\xf8\x07\xf8\x00\xde\x00\\\x80q\x00\xf0\xc0\xfc\x98\xf9\x0c\xf3$\xfb!\xff\xa3\xffo\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=119, y=364),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'$&\n\n..\x1c\x1c00\x00\x00\x00\x00\x00\x00>\x028\x06b\x1eL<\x10p\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=128),
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
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                        AnimationSequenceFrame(duration=2, mold_id=6),
                        AnimationSequenceFrame(duration=2, mold_id=7),
                        AnimationSequenceFrame(duration=4, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=6, mold_id=10),
                        AnimationSequenceFrame(duration=8, mold_id=11),
                        AnimationSequenceFrame(duration=14, mold_id=12),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL566_COMMANDER_TROOPA,
    palette_offset=2,
    unknown_num=8
)
