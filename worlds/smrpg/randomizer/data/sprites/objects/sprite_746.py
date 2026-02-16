# SPR0746_WATER_CRYSTAL_3D

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL328_WATER_CRYSTAL_3D
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01'),
                            bytearray(b'\x00\x08\x00\x18\x18$ \x1c,^h\x96\xe0\x08\xc2=\x08\x08\x18\x18\x08,\x1c\x14PV\x1c\x82\x17\x02 #'),
                            None,
                            bytearray(b'\x01\x00\x03\x00\x03\x00\x03\x04\x03\x04\x01\x02\x01\x00\x02\x01\x00\x00\x00\x00\x04\x04\x04\x04\x00\x04\x02\x02\x02\x00\x01\x03'),
                            bytearray(b'\xe2\x1c\xe3\x1c\xa7Y\xa7Y\xc0\x7f\x8au\x03\xff\x00\xff\x03!#\x01xGxG?@}\x02\xfc\x83\xff\xff'),
                            bytearray(b'\x00\x00\x00\x80\x00\x00\x80\x80\x00\x80@\xc0\x80`\x00\xe0\x00\x00\x00\x80\x80\x80\x00\x80\xc0@\x80@\xc0\xe0\xc0\xe0'),
                            bytearray(b'\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x01\x00\x01\x01\x01\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe1A\xc2\x00\xee\x08H\x8c|`|\x02>R6L\x91\xef\x81\xfe\x85\xfe\x85\xfe\x8e\xfd\xff\xfd\xec\xffh\xfe'),
                            bytearray(b'@\x00\x80@\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x00\x80\x00\x80\x80\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'0\\<\x04\x1c \x0800\x00\x10\x00\x00\x10\x00\x00\xeczx|8|<(8880\x100\x10\x10'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL328_WATER_CRYSTAL_3D,
    palette_offset=1,
    unknown_num=8
)
