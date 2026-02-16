# SPR0744_EARTH_CRYSTAL_3D

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL326_EARTH_CRYSTAL_3D
sprite = CompleteSprite(
    animation=AnimationPack(233, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=1, length=13, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x08\x00\x14\x048$\x0c\x004H\xe0\x9eM\x0f\xc2\x01\x08\x00\x1c\x0c,(<<V\x1c\x02\x1c\xbe\xac="'),
                            None,
                            bytearray(b'\x01\x00\x01\x00\x07\x04\x07\x00\x07\x04\x01\x00\x03\x00\x00\x00\x00\x00\x02\x02\x00\x00\x04\x00\x00\x00\x02\x02\x00\x02\x03\x01'),
                            bytearray(b'\xfc\x0f\xc1"\x97 \xe1\x1e\xc4;L3@?\xfe\x01->\x1d#A\x7fA\x7f@\x7f\xc0\xff\xc0\xff\xff\xfe'),
                            bytearray(b'\x00\x00\x80\x80\x80\x00\xc0@@\x80@\x80\xc0 \xc0\x00\x00\x00\x80\x00\x80\x80\x80\x80@\xc0@\xc0\xe0\xc0\xe0\xc0'),
                            bytearray(b'\x01\x00\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xe0\x01\xc3\x03\x8f\x03\x8c\x00oC\xff\x91~\x00\x7f\x11\xd8\xe6\xbe\xc0\x9e\xec\xb7\xcc\r\xfcm\xfeo\xfe\xef\x7f'),
                            bytearray(b'\x00@\x00@\x80\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\x00\x80\x00\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'nP~\x02<\x00(\x108 \x10\x000 \x00\x00,~>~|<,8\x188\x18000\x10\x00'),
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
    palette_id=SPAL326_EARTH_CRYSTAL_3D,
    palette_offset=1,
    unknown_num=8
)
