# SPR0928_MARCHING_LUIGI

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL681_MARCHING_LUIGI
sprite = CompleteSprite(
    animation=AnimationPack(413, length=98, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x14\x08\x1c\x00\t\x03\x0b\x03\x01\t\x00\x00\x00\x00\x00\x00\x00\x14\x00\x1c\x08\x08\x00\x00\t\t'),
                            bytearray(b'\x00\x00\xb8\xb8\xc0\xd8`x\xdc\xbcF\xae6N\x84\xd4\x00\x00\xb8\x00\xd8 8\x04|\xc2\x0e\x90\xb6\x00\xac\x84'),
                            bytearray(b'\x0c\x00\x0f\x03\x00\x08\x08\x00\x1c\x00\x14\x08\x00\x00\x00\x00\x04\x07\x03\x03\x08\x08\x08\x08\x00\x1c\x00\x14\x00\x00\x00\x00'),
                            bytearray(b'hh\xbc\xbc\x8c\x0cLp\x184Pp0\x00\xf8\xf8\x18\x88\xfc\xc0\x8cp\x80\xf0\xcc\xfc@p\xf0\x00\xf8\xf8'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\n\x04\x0f\x01\x03\x05\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\n\x00\x0e\x06\x06\x01\x01'),
                            bytearray(b'\x00\x00\xb8\xb8\xc0\xd8`x\xdc\xbcF\xae6N\x84\xd4\x00\x00\xb8\x00\xd8 8\x04|\xc2\x0e\x90\xb6\x00\xac\x84'),
                            bytearray(b'\x00\x03\x05\x04\x05\x04\x00\x00\x03\x02\x03\x02\x01\x01\x00\x00\x03\x03\x04\x02\x05\x03\x00\x00\x03\x02\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'hh\xbc<\x8e\x08\x04\xba\xfe\x1a\xaeB\xcc\x0c\xfe\xfe\x18\x08\xfc\xc0\x08p\xc6\xfe\x06\xfa\x1e\xb2\xcc\x0c\xfe\xfe'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'(\x108\x00\x10 \x008(\x10)\x17\x03{A!\x00(\x008  88\x10\x10\x14\x14x|!#'),
                            bytearray(b'\x00\x00\xb8\xb8\xc0\xd8`x\xdc\xbcF\xae6N\x84\xd4\x00\x00\xb8\x00\xd8 8\x04|\xc2\x0e\x90\xb6\x00\xac\x84'),
                            bytearray(b'\xe0\x00\xa0@\x00\x00\x02\x02\x03\x02\x03\x02\x01\x01\x00\x00\x00\xe0\x00\xa0\x00\x00\x03\x02\x03\x02\x03\x02\x01\x01\x00\x00'),
                            bytearray(b'h(88\x88\x08<$SM\x8b\r\xd2\xd2\xff\xffX\x88xD\x88t\xc0\xe4\xbb\xfd\xd3]\xde\xd2\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=121),
                    ]
                ),
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\r\x01\x18\x04\x12\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x0c\x14\x14\x18\x1a'),
                            bytearray(b'\x00\x000,\x02>\xc4D\xfe\xb9\xc6\xb9\xb2(|8\x00\x00,@>\xc0\xfc\x02\xc6\xec\x82\xa8\xd6\x10|8'),
                            bytearray(b'\x07\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x06\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'DDR>\x03?#8kl\xda\xfe\xfa\x92\xee\xee|\xc4V\xa8CUD|\x11}\x92\xfe\xfe\x92\xee\xee'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(4, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x03\x00\x01\x02\x05\x01\t\x05\x1c\x00,\x10\x00\x00\x00\x00\x00\x03\x00\x01\x00\x00\x0c\x0c\x10\x10\x10\x10'),
                            bytearray(b'\x00\x000,\x02>\xc4D\xfe\xb9\xc6\xb9\xb2(|8\x00\x00,@>\xc0\xfc\x02\xc6\xec\x82\xa8\xd6\x10|8'),
                            bytearray(b'\x86F\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x06\x89\x00\xc7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'DDF.\x06;$?\xe4\xec\xcc\xe0\xfe\x9e\xf0\xf0|\xc4F\xb8GQC\x7f\x90\xfc\x9c\xf0\xfe\x9e\xf0\xf0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(5, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x00\x01\x02\x05\x01\t\x05\x1c\x00,\x10\x84D\x00\x00\x00\x03\x00\x01\x00\x00\x0c\x0c\x10\x10\x10\x10\x04\x8b'),
                            bytearray(b'\x00\x000,\x02>\xc4D\xfe\xb9\xc6\xb9\xb2(|8\x00\x00,@>\xc0\xfc\x02\xc6\xec\x82\xa8\xd6\x10|8'),
                            bytearray(b'\xc1\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\xc6\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'DDF(\x068$>*.j\x0e\xfa\xf2\x1e\x1e|\xc4D\xbcDTB~R~r\x1e\xfe\xf2\x1e\x1e'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=4),
                        AnimationSequenceFrame(duration=8, mold_id=3),
                        AnimationSequenceFrame(duration=8, mold_id=5),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL681_MARCHING_LUIGI,
    palette_offset=0,
    unknown_num=8
)
