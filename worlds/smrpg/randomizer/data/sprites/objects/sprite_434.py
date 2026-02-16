# SPR0434_ZEOSTAR

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL222_STARSLAP
sprite = CompleteSprite(
    animation=AnimationPack(120, length=586, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x12\x1a\x1b\x043\x0c\xa1^\x00\x00\x01\x01\x03\x02\x07\x00\r\x10$\x04L\x0c\x1e\x1e'),
                            bytearray(b'(\x18\xf1^\xc0\xbf\x0ft\x87\xba\x9f\xb4\x90\x98\xf0pP`n\xf0_\xe0\xf3\x03\x7f\x0fb\x07n\x01\x0c\x03'),
                            bytearray(b'\x00\x00 \xa0\x10\x00\x80\xd0`\xd0\x98\x04\x0c\x00\x00\x00\x00\x00\x80` \xd0\x08\xf4\xa6\x18z\x86\x1c\xe4\x00\xfc'),
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'A\xbc@\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"$ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb070\xd71\xdc2\xcc6L<H(\x00\x00\x00H\x07\x00\x0f\x01\x0f\x12\x0e\x12\x0e\x14\x0c\x18\x18\x00\x00'),
                            bytearray(b'\x00\x08\x82\xc0\xed"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x03\xfd\xcd\xf3\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x01\x04\x03\x07\x0f\x1f\x03>B\x00\x00\x00\x00\x00\x00\x00\x01\x03\x04\x18\x00 \x00\x81\x00'),
                            bytearray(b'\x00\x00\x18\x18\x03\x1f\x83~\x00\xff\x08\xe7\x1ck\x03s\x00\x00\x00\x18<\x03}\x81\xff\x04\xff\x18\xff\x1c\xfc\x0c'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x90\x90\xc0\x00\x00\x98\x82\xb0\xef\xd0\x00\x00\x00\x00\x00\x00\xe0\xf0\xc0\xf8\x80~B=/\x10'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'|\x82\x18\xe5\x189\x01\x00\x01\x02\x01\x02\x00\x03\x00\x00\x01\x00\x1a\x00\x02|\x02\x04\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\xc3\xd7\xc3\xc0\xc3`\x82Aq\x91\xff \xe0\x80\x80\x004\x08$\x18$\x18\x068n\x1f\xdf?`\xe0\x80\x80'),
                            bytearray(b'\xd8`L\x90\xe8\x10 \xd8\x80x$\x1c\x04\x00\x00\x00\x1f\x07\xac\x84\x0c\x04\xc4\xc4\xa0$\xe0\xc4<<\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x07\x01\x06\x0e\x1e?\x18e\x03{\x068\x00\x00\x00\x01\x03\x07\x1b\x03A\x00\x83\x00\x84\x00A\x00'),
                            bytearray(b'\x1c\x14\xc2\xbe\x87}\x87}\t\xe0\x1c\xfb\x18\xf6\x00\x00\x00\x1c<\xc2x\x80x\x80\xea\x1c\xff\x1c\xff\x18\xff\x00'),
                            bytearray(b'\x00\x00\x00\x00@@\x10\xf0\x00\x00\x00\x08\x0c\x1e\x00~\x00\x00\x00\x00\x80@\xe0\x10\xc08\x82~\x80~\x01\xff'),
                            None,
                            bytearray(b'\x06\x18\x0e\x00\x17\x08\x08\x17\x06\x18\x07\x04\x00\x00\x00\x00\x01\x00\x10\x01\x0b\x080\x10&\x01;\x07\x00\x00\x00\x00'),
                            bytearray(b'<\x006\x08\xc3<\x01\xfe\xf0\x9f\x84\x05\x00\x00\x00\x00\xa3@)\xc8\xdc\x1c\x1e\x1eg\xff\x80\x86\x00\x00\x00\x00'),
                            bytearray(b'\x1a>\x1e`\x10\xa0\x80\x00\xc0 \x00\xe0\x00\x00\x00\x00\x01\xff\x9e~\x10p\x00`@ \x00`\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x01\x01\x05\x00\x0b\x03\x01\x11\x07\x1f/\x10\x10\x0f\x00\x00\x00\x01\x02\x05\x1f\x13-\x03`@@`//'),
                            bytearray(b'\x00\x00\xfc\n@\xb3\x8f{\x8c\xf3\xc9\xf6\xcb\x1c\xf24\x00\x00\x1b\xfc\xbfL\xf0\x80\xf3\x806\x014\x03\x0c\x03'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xc0\x80\x90P\xf0\x00\x00\x18\x00\xfe\x00\x00\x00\x00\x80\x00\x00\x00@\xb0\x00\xf8\x00\xfc\x00\xfe'),
                            None,
                            bytearray(b"\x07\x18\x078\tp\x80g\x00\x00\x00\x00\x00\x00\x00\x008\x18x8\xf6p8\'\x00\x00\x00\x00\x00\x00\x00\x00"),
                            bytearray(b'p\xb1P\x82\xd1"\x91d\x03\xfc\x17(\x06\x1c\x00\x18\x8c\x83\xa8\x87\t\x06\t\x06\x03\x85G\x01"\x06\x00\x18'),
                            bytearray(b'\x00\x7f\x02\x0e\xf3\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x01\xff\xff\x7f\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(4, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x06\x06\x07\x05\x03\x03\x03\x01\x06\x07??\xff\x03\x00\x00\x01\x00\x00\x00\x04\x00\x00\x04\x01\x08\x00@\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x80\x8f\xe0~\xe0\x9f\x00\xff\xcd\xff\xcf\xf4\x00\x00\x80@O0\x9f\x80\x7f\xe0\xff\x006\x043\x07'),
                            bytearray(b'\x00\x00\x00\x00\x00\x80\xf8\x80h\x100\x00\xf4\xe0\xf8\xc0\x00\x00\x00\x00\xf8\x00\x04\x00\x90\x14\xcc\x04\x04\x0c\x00\x84'),
                            bytearray(b'\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x7f\x80\x13l\xe0\xe1\xfe\xee\x1f\x1f\x03\x03\x00\x00\x00\x00\x00\x00\x8c\x0c\x00\xfe\xf0\xff\x1e\x1f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xf9v\xf0\x7f\xf1.}\x81\xb7D\xa7\xc3\xcc\xccpp\x06\x06\x0f\x0f\x0e\x0e\x00\x03\x8b\x07\x17\x8f\xac\xdcpp'),
                            bytearray(b'\xf0\xcc\xfe\x00\xe0\x00\xff\x01\xfe\xfe\x00\x00\x00\x00\x00\x00\x0e\x0c\x01\x00\xe6\x19\xff\xff\xfe\xfe\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(5, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x06\x06\x07\x05\x03\x03\x03\x01\x06\x07??\xff\x03\x00\x00\x01\x00\x00\x00\x04\x00\x00\x04\x01\x08\x00@\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x80\x8f\xb0\xae`_\x03\xfd\xcf\xfe\xc9\xf1\x00\x00\x80@O0\x7fp\xff\xe0\xff\x037\x076\x06'),
                            bytearray(b'\x00\x00\x00\x00\x00\x80\xf8\x80h\x100\x00\xf4\xe0\xf8\xc0\x00\x00\x00\x00\xf8\x00\x04\x00\x90\x14\xcc\x04\x04\x0c\x00\x04'),
                            bytearray(b'\x00\x00\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x7f\x80\x13l\xe0\xe1\xfe\xee\x1f\x1f\x03\x03\x00\x00\x00\x00\x00\x00\x8c\x0c\x00\xfe\xf0\xff\x1e\x1f\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xf9v\xf0\x7f\xf1.}\x81\xb7D\xa7\xc3\xcc\xccpp\x06\x06\x0f\x0f\x0e\x0e\x00\x03\x8b\x07\x17\x8f\xac\xdcpp'),
                            bytearray(b'\xf0\xcc\xfe\x00\xe0\x00\xff\x01\xfe\xfe\x00\x00\x00\x00\x00\x00\x0e\x0c\x01\x00\xe6\x19\xff\xff\xfe\xfe\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(6, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x00\x00\x02\x00\x00\x02\x06\x01\x07\x02\x0f\x0b\x0f\x0b\xbf;\x00\x00\x00\x02\x07\x02\x01\x01\x00\x00\x00\x08\x00\x08@8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00@\xc0a\xe14\xdf\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xa1\x80\x92\x00\xf38'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x080\x08`\x08`\xe0`\xe0\x00\x00\x00\x00\x00\x00\x1c\x0cL\x0c\x94\x04\x9c\x04\x98\x08'),
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1e\xef,\xd7\x18o\xc8\xd0gk43\x18\x18\x0e\x0e\xc1\xc0\xc3\xc0\xe7`\xb7Px\x088\x00\x1f\x04\x0f\x01'),
                            bytearray(b'i\xe7q\x8e\x07\xfbfx\xd3\xb7\x8fp00\xfc\xfc\xf6x\x8fq\xfb\x07\x9a\x07, pp\xffH\xff\x03'),
                            bytearray(b'\xc0\xc0\xf4@\x04H*\x92\\,\xd8\x18\xb0 \xe0\x00(\x18\x8a\x80\xfa\x88\xd6\x10\xac 8\x00p\xd0\xe0\xe0'),
                            None,
                            bytearray(b'\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xf0\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x0f\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(7, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x00\x00\x02\x00\x00\x02\x06\x01\x07\x02\x0f\x0b\x0f\x0b\xbf;\x00\x00\x00\x02\x07\x02\x01\x01\x00\x00\x00\x08\x00\x08@8'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00@\xc0a\xe14\xdf\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xa1\x80\x92\x00\xf38'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x080\x08`\x08`\xe0`\xe0\x00\x00\x00\x00\x00\x00\x1c\x0cL\x0c\x94\x04\x9c\x04\x98\x08'),
                            bytearray(b'\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x1e\xef,\xd7\x18o\xc8\xd0gk43\x18\x18\x0e\x0e\xc1\xc0\xc3\xc0\xe7`\xb7Px\x088\x00\x1f\x04\x0f\x01'),
                            bytearray(b'i\xe7q\x8e\x07\xfbfx\xd3\xb7\x8fp00\xfc\xfc\xf6x\x8fq\xfb\x07\x9a\x07, pp\xffH\xff\x03'),
                            bytearray(b'\xc0\xc0\xf4@\x04H*\x92\\,\xd8\x18\xb0 \xe0\x00(\x18\x8a\x80\xfa\x88\xd6\x10\xac 8\x00p\xd0\xe0\xe0'),
                            None,
                            bytearray(b'\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\xf0\xff\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x0f\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(8, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'] \x10b\x13\x0fy\x05\x1b\x12ycq{53\x01~\x01\x7fa~c~\x01\x1fq~q~9>'),
                            bytearray(b'\x00\x80\x80\x80\x80\x80\x80\x00\x80\x00\x80\x00\x80\x00\x80\x80\x00\x80\x80\x00\x80\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00'),
                            bytearray(b'9;\x19\x1b\r\r\x07\x06\x00\x00\x00\x00\x00\x00\x00\x008?\x1c\x1f\x0e\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x04\x08\x04\x05\t\x19%9\x05\x1f!\x00\x00\x00\x00\x00\x02\x08\x02\x03\x00w$G\x04#`'),
                            None,
                            bytearray(b'\x1f)-\x0bLJF`cL7\x1c3^y\x14#`Q@rCxAXpXp\x1cp\x16x'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x00\x00\x80\x00\x00\x80\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x00@@'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                    ]
                ),
                Mold(9, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'{\x02\x7f\x00\x7f\x00O@?\x04\xff\x02\xff\xfd?>\x06\xff\x00\xff\x00\xff0\xff\xf8\xff\xfc\xff\xfe\xff??'),
                            bytearray(b'\xc4\x14\x8c(80\x18\x1080\x188\x988\x88\xa8\x0c\xf8\x1c\xf4\x18\xe88\xe8\x18\xe8\x18\xe0\x18\xe0\x18\xf0'),
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x88h\xf8\xa0\xf8\xc000\x00\x00\x00\x00\x00\x00\x00\x00\x98\xf0\xd8\xf8\xf8\xf800\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80'),
                            None,
                            bytearray(b'\x00@\x00\xa0\xa0P\x98h\xc8\xb0\xf8\xfc\x00\xc0\x82j\x00\xc0\x00`@P`h40\x02\x00\xf2\x0ef\x9c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x03\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x04\x00\x00\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x00\x07\x14\x1a\x14\x1e\xc5<\x01\xf8\x00\x00\x00\x00\x04\x01\x04\r\x08\x19\x80a\x03\x00\x07\x00'),
                            bytearray(b'\x01\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x04\x03\x02\x02\x03\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x88\xd0\xe4\xf0\\\xf0~\xc4y\xc6\x7f\xe7\x9ew\x8a\x07\x00/ O\xc0O\xc0\x7f\xc6\x7f\xc6\x1e\xe7\x0e\xf7'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                    ]
                ),
                Mold(10, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\xf8\x10\xb0\x80\xe0\xe0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\xf8\xe8\xb0\xb0\xe0\xe0\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=132),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x0b\x0c\x02\x01\x03\x00\x03\x08\x04\x02\x01\x0c\x03\x00\x07\x07\x00\x0f\t\x0e\x08\x0f\x00\x0f\x01\x0f\x03\x0f\x0f\x0f\x07\x07'),
                            None,
                            None,
                            bytearray(b'\xfe\xfe\x7f\x7f\x1f\x1f\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\xfe\xfe\x7f\x7f\x1f\x1f\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x80\x00\x00\x06v\xfe\x83y\xfb\x06\xce\xc6$\x1c\xd8\x00\x80@\xa0\x88\x01\x00\x01\x85\x02\xe6\x18\x1e\xfa<\xe4'),
                            bytearray(b'\x7f\x82\xff\x00\xff\x00\x83\x8cq\x02\xfe\x00\xe7\xe0\xff\xfc\x86\x7f\x00\xff\x00\xffp\xff\xfc\xff\xff\xff\xe7\xe7\xff\xff'),
                            bytearray(b'\x18\x908\xa0p\xe0\xd0@\x90@\xd0\x10\x10p\x980x\xe8x\xd80\xd00\xf00\xf00\xe0\x90\xe0\xd8\xe8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06'),
                            bytearray(b'\x00\x00\x00\x00\x04\x0c(48,rVr:q\xfb\x00\x00\x00\x00\x10\x04\x10\x14B\x06\x08\x06\x89\x07\x08\x07'),
                            bytearray(b'<Cr\r? OO)4\x07\x19\x13\x1d\x0b\x0c\x00\x80\x0c\x8c\x00@\x10`\x05;\x01\x1f\x01\x1f\x01\x0f'),
                            bytearray(b'1\xf9\xb0\xf9\xf0\xd8\xf0\x8c\xf0\x0f\xf6\xdc\x87\xfe\x87\xfeH\x07H\x07\x08\x07\x0c\x03\x8f\x80\x8e\x87\xfe\x87\xfe\x87'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
                Mold(11, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=2, length=13, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x01\x00\x03\x12\x1a\x1b\x043\x0c\xa1^\x00\x00\x01\x01\x03\x02\x07\x00\r\x10$\x04L\x0c\x1e\x1e'),
                            bytearray(b'(\x18\xf1^\xc0\xbf\x0ft\x87\xba\x9f\xb4\x90\x98\xf0pP`n\xf0_\xe0\xf3\x03\x7f\x0fb\x07n\x01\x0c\x03'),
                            bytearray(b'\x00\x00 \xa0\x10\x00\x80\xd0`\xd0\x98\x04\x0c\x00\x00\x00\x00\x00\x80` \xd0\x08\xf4\xa6\x18z\x86\x1c\xe4\x00\xfc'),
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'A\xbc@\x81\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"$ \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xb070\xd71\xdc2\xcc6L<H(\x00\x00\x00H\x07\x00\x0f\x01\x0f\x12\x0e\x12\x0e\x14\x0c\x18\x18\x00\x00'),
                            bytearray(b'\x00\x08\x82\xc0\xed"\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xfe\x03\xfd\xcd\xf3\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
                Mold(12, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'~\x9c\xfe\x9a\xdc\x14\xf8(\xb000\x10`\x00\x80\x00\x8e\x12\x0e\x16\x1c,\x188P0\xb0p`\xe0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=125),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00'),
                            None,
                            bytearray(b'\x03\x04\x08\x0b\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x04\x08\x08\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x03\x9fc\x07\t\xf3t\xfd\n\x1d\x06\x06\x02\x03\x00\x00\x00``\x00\xf0\x80\xf8\xf4\xf8\x18\x1c\x05\x06\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\x80@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xa0\x811\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00@\x80`\x00\x10\x00\x88\x10\xc0\x08\x00\x00\x00\x00\x00\x00\xa0\x80\x10\x80(\xc0\x00\xe0\x14\xe0'),
                            bytearray(b'\x80H@\x00\x04[\x02M\x1a\x1dp\x7f\xe0\xff\xfc\xff7\x00\xbf\x00?\x84?\x82g\x82\x0f\x80\x1f\x00\x03\x00'),
                            bytearray(b' \xdc\x00\xdc\x01\xc5\x07\xf1\x0f\xf3\xcf??\xde?\xde\xc2 \xe2\x00\xfb\x00\xf9\x00\xf1\x12\xc3\xcc\xdf\x01\xdf\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=126, y=109),
                    ]
                ),
                Mold(13, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'~\x9c\xfe\x9a\xdc\x14\xf8(\xb000\x10`\x00\x80\x00\x8e\x12\x0e\x16\x1c,\x188P0\xb0p`\xe0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=138, y=379),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00'),
                            None,
                            bytearray(b'\x03\x04\x08\x0b\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x04\x08\x08\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x03\x9fc\x07\t\xf3t\xfd\n\x1d\x06\x06\x02\x03\x00\x00\x00``\x00\xf0\x80\xf8\xf4\xf8\x18\x1c\x05\x06\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=371),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\x80@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xa0\x811\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00@\x80`\x00\x10\x00\x88\x10\xc0\x08\x00\x00\x00\x00\x00\x00\xa0\x80\x10\x80(\xc0\x00\xe0\x14\xe0'),
                            bytearray(b'\x80H@\x00\x04[\x02M\x1a\x1dp\x7f\xe0\xff\xfc\xff7\x00\xbf\x00?\x84?\x82g\x82\x0f\x80\x1f\x00\x03\x00'),
                            bytearray(b' \xdc\x00\xdc\x01\xc5\x07\xf1\x0f\xf3\xcf??\xde?\xde\xc2 \xe2\x00\xfb\x00\xf9\x00\xf1\x12\xc3\xcc\xdf\x01\xdf\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=363),
                    ]
                ),
                Mold(14, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'~\x9c\xfe\x9a\xdc\x14\xf8(\xb000\x10`\x00\x80\x00\x8e\x12\x0e\x16\x1c,\x188P0\xb0p`\xe0\x80\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=378),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00'),
                            None,
                            bytearray(b'\x03\x04\x08\x0b\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x04\x08\x08\x0f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x03\x9fc\x07\t\xf3t\xfd\n\x1d\x06\x06\x02\x03\x00\x00\x00``\x00\xf0\x80\xf8\xf4\xf8\x18\x1c\x05\x06\x03\x03'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=370),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80@\x80\x80@\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\xa0\x811\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00@\x80`\x00\x10\x00\x88\x10\xc0\x08\x00\x00\x00\x00\x00\x00\xa0\x80\x10\x80(\xc0\x00\xe0\x14\xe0'),
                            bytearray(b'\x80H@\x00\x04[\x02M\x1a\x1dp\x7f\xe0\xff\xfc\xff7\x00\xbf\x00?\x84?\x82g\x82\x0f\x80\x1f\x00\x03\x00'),
                            bytearray(b' \xdc\x00\xdc\x01\xc5\x07\xf1\x0f\xf3\xcf??\xde?\xde\xc2 \xe2\x00\xfb\x00\xf9\x00\xf1\x12\xc3\xcc\xdf\x01\xdf\x01'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=362),
                    ]
                ),
                Mold(15, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'{\x02\x7f\x00\x7f\x00O@?\x04\xff\x02\xff\xfd?>\x06\xff\x00\xff\x00\xff0\xff\xf8\xff\xfc\xff\xfe\xff??'),
                            bytearray(b'pp0000\x10\x1088\x188\x988\x88\xa8\xf0\x80p\xc0\x10\xe00\xe0\x18\xe0\x18\xe0\x18\xe0\x18\xf0'),
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x88h\xf8\xa0\xf8\xc000\x00\x00\x00\x00\x00\x00\x00\x00\x98\xf0\xd8\xf8\xf8\xf800\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x02\x04\x02\x06\x00\n\x14\x12\x0c\x17\x08\x00\x00\x00\x00\x00\x01\x04\x01\x01\x00=\x14-\x0c\t('),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x80\x00'),
                            bytearray(b'\x0c\x15\x1a\x0c0?`\x7fF\x19\x07z\x87\xff6\xca2\x10%"/\'?g=a}\x06~\x87O\xb7'),
                            bytearray(b'\x00\x00\xc0\x00 \xc0 \xc0 \xc0\xf0\x10\xf0\x10\xf0\xf0\x00\x80@\x00\xe0\xc0\xe0\xc0\xd0\xd0\x00\x10\xa0\x10\x10\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                    ]
                ),
                Mold(16, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x88h\xf8\xa0\xf8\xc000\x00\x00\x00\x00\x00\x00\x00\x00\x98\xf0\xd8\xf8\xf8\xf800\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=132),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80@@\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x80@\x00@@\x80\x80\x00\x80\x80\x00\x00'),
                            bytearray(b'\xc4\x14\x8c(80\x18\x1080\x188\x988\x88\xa8\x0c\xf8\x1c\xf4\x18\xe88\xe8\x18\xe8\x18\xe0\x18\xe0\x18\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=116),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x01\x00\x02\x01\x01\x02\x02\x00\x00\x00\x00\x00\x01\x01\x01\x01\x02\x00\x01\x01\x02\x02\x01\x00\x02\x01\x03\x03\x01\x00\x01\x00'),
                            None,
                            None,
                            bytearray(b'\x7f\x01\x7f\x00\x7f\x00O@?\x04\xff\x02\xff\xfd?>\x03\xff\x00\xff\x00\xff0\xff\xf8\xff\xfc\xff\xfe\xff??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x03\n\r\x0e\x03\x1c\x15\x1c\x0c\x18h\x00\x00\x00\x00\x04\x01\x04\x05\x10\x01\x02\x01"\x01\x06\x81'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x00\x80@\xc0\x00\xc0'),
                            bytearray(b"\x98\x98\x188P4`.`_b^\xc3\x9e\xbb\xc7g\x00\'\xc0/\xc0\xff\xe0\xff\xe0\xff\xe3\x7f\xe3\x07\xfb"),
                            bytearray(b'\x00`\x00\x80\xe0\x98~A>\xbe\x00\xf1\x01\xf9\x87v\x00\xe0\x10h\x07\x00\x80\x00\xc1\x00\xf8\x07\xe7\x1eO\xb9'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                    ]
                ),
                Mold(17, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\\\x03>\x19\x07$]@=\x1c\xfe<\xff\xff?>\x03\xfc\x01\xfe\x18\xff<\xff\xfe\xff\xfe\xff\xfe\xff??'),
                            bytearray(b'\x18\xd0\xb8p\xb80\xb80\xb80\x988\x188\x88\xa8\xb8h\x18\xe8\x18\xe8\x18\xe8\x18\xe8\x18\xe0\x18\xe0\x18\xf0'),
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x88h\xf8\xa0\xf8\xc000\x00\x00\x00\x00\x00\x00\x00\x00\x98\xf0\xd8\xf8\xf8\xf800\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00\xe1\x01\xf2\x025.\x12\x16+6\x1f\x00\x00A\x00\xc3\xc1&"\xc8\x00A\x80\xe9\x88y('),
                            bytearray(b'`\x00\x00\xc0\xe0       00\x1c\x02\xa0\x00\x80\xa0\xc0 \xa0@ \xc0 \xc0\x00\xf0\xe1\x00'),
                            bytearray(b'?6?\x1c?\x1e\x0b~\x03|\x00|\x80\xff\x18\xe7 p#s#sw\x03\x7f\x03\x7f\x03\x7f\x80g\x98'),
                            bytearray(b'\x8cq1\xd3\xd3\xf6\x06\xcc\x0e\x9c\x1c\xb8<\xf8\x18\xd0rq\xcd\xc2)\x07\xf2\x0e\xee\x12\xcc4\x9cd\xb8h'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=108),
                    ]
                ),
                Mold(18, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x88h\xf8\xa0\xf8\xc000\x00\x00\x00\x00\x00\x00\x00\x00\x98\xf0\xd8\xf8\xf8\xf800\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=132),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x80\x00\xc0\x00\xe0\x80\xe0p\xe0\x00p\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x90\x10\x80\x80\x00'),
                            None,
                            bytearray(b'\xb0@8\xc8x\x98\xf88\xf8\xc8xh\xb88\x88\xa8@@\xd8\xc0\xa8\x90X \xf80x\x908\xc0\x18\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=116),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x02\x00\x04\x01\x08\x00\x11\x0b\x17\x03\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x07\x01\x0c\x0b\x08\x07'),
                            bytearray(b'$\x18O0\x90d\xd2\x12}\x01\xfc\x81zc\xb6\x83X\x18\xb00o`-\x1e\xfe\xff\xfe\xff\xfc\xff|\xff'),
                            None,
                            bytearray(b'\x07\xc4B$_8OH?\x04\xff\x02\xff\xfd?>;\xff\x19\xfe\x00\xfe0\xfe\xf8\xff\xfc\xff\xfe\xff??'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=116),
                    ]
                ),
                Mold(19, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xd4\x14\xa8(P@p@p`00\xb00\x00 \x0c\xf8\x18\xf00\xf00\xf00\xd0\x10\xe0\x10\xe0\x10\xf0'),
                            None,
                            bytearray(b'\x80`\xf0\xa0\xf0\xc000\x00\x00\x00\x00\x00\x00\x00\x00\x90\xf0\xd0\xf0\xf0\xf000\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=124),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x02\x00\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b's\x8a\xbb$\x0f\x007\x00/\x00\xff0\xff\xfd?>\x8ew\x04\xfb0\xffx\xff\xe8\xef\xfc\xff\xfe\xff??'),
                            None,
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80'),
                            None,
                            bytearray(b'\x00@\x00\xa0\xa0P\x98h\xc8\xb0\xf8\xfc\x00\xc0\x82j\x00\xc0\x00`@P`h40\x02\x00\xf2\x0ef\x9c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x03\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x04\x00\x00\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x00\x07\x14\x1a\x14\x1e\xc5<\x01\xf8\x00\x00\x00\x00\x04\x01\x04\r\x08\x19\x80a\x03\x00\x07\x00'),
                            bytearray(b'\x00\x01\x00\x00\x01\x01\x00\x03\x00\x03\x02\x00\x01\x00\x02\x00\x07\x04\x03\x02\x02\x02\x01\x02\x01\x02\x01\x02\x02\x00\x01\x02'),
                            bytearray(b"\xf8\xf8P\xf2P~\xf0~\xe4yF=\x07>\'\xde\x07\x00\xaf \xcf\xc0\xcf\xc0\xdf\xc6\xff\xc6\xfe\x07\xde\'"),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                    ]
                ),
                Mold(20, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x7f\x00\x7f\x80\x7f\x00\r>_\xc1\xf1\x00\xfe\xfe??\x83\xff\x00\xff\x00\xff\x00\xff>\xff\xf1\xf1\xfe\xfe??'),
                            bytearray(b'\xc4\x14\xec H\xa0\xa0Ph\x08(\x08\x80\x00\xc8H\x0c\xf8\x1c\xfc\x98xH\xb8\x00\xf8\x00\xf8\x88\xf8\x88\xf0'),
                            bytearray(b'\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x1f\x1f\x07\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc8\xa8\xf8\xa0\xf8\xc000\x00\x00\x00\x00\x00\x00\x00\x00\xd8\xf0\xd8\xf8\xf8\xf800\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\x80'),
                            None,
                            bytearray(b'\x00@\x00\xa0\xa0P\x98h\xc8\xb0\xf8\xfc\x00\xc0\x82j\x00\xc0\x00`@P`h40\x02\x00\xf2\x0ef\x9c'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x00\x00\x03\x07\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x04\x04\x00\x00\x04'),
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x00\x07\x14\x1a\x14\x1e\xc5<\x01\xf8\x00\x00\x00\x00\x04\x01\x04\r\x08\x19\x80a\x03\x00\x07\x00'),
                            bytearray(b'\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x04\x03\x02\x01\x01\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xfc\xcc\xe8\xdc\x98\x0c\xb0>`=b>s\r{\x05\x03\x00\x17\x10g\xe0o\xe0\xbf\xe2\xbf\xe3\xaf\xf3\x87\xfb'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=114, y=108),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=11),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=11),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=8, mold_id=7),
                        AnimationSequenceFrame(duration=6, mold_id=6),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=12),
                        AnimationSequenceFrame(duration=4, mold_id=13),
                        AnimationSequenceFrame(duration=4, mold_id=14),
                        AnimationSequenceFrame(duration=2, mold_id=13),
                        AnimationSequenceFrame(duration=2, mold_id=12),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=15),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=4, mold_id=16),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=16, mold_id=18),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=16, mold_id=18),
                        AnimationSequenceFrame(duration=13, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=19),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=16, mold_id=20),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=2),
                        AnimationSequenceFrame(duration=4, mold_id=3),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=10, mold_id=8),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                        AnimationSequenceFrame(duration=10, mold_id=10),
                        AnimationSequenceFrame(duration=6, mold_id=9),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=64, mold_id=4),
                        AnimationSequenceFrame(duration=64, mold_id=4),
                        AnimationSequenceFrame(duration=64, mold_id=4),
                        AnimationSequenceFrame(duration=64, mold_id=4),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=6, mold_id=5),
                        AnimationSequenceFrame(duration=6, mold_id=4),
                        AnimationSequenceFrame(duration=48, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=1, mold_id=5),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=12, mold_id=6),
                        AnimationSequenceFrame(duration=12, mold_id=7),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=19),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=20),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=15),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=16),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=17),
                        AnimationSequenceFrame(duration=8, mold_id=9),
                        AnimationSequenceFrame(duration=12, mold_id=18),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=6, mold_id=19),
                        AnimationSequenceFrame(duration=4, mold_id=9),
                        AnimationSequenceFrame(duration=6, mold_id=20),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL222_STARSLAP,
    palette_offset=2,
    unknown_num=8
)
