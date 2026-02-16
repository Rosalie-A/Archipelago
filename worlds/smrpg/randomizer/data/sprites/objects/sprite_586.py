# SPR0586_BOX_BOY_SMALL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL811_BOX_BOY_SMALL
sprite = CompleteSprite(
    animation=AnimationPack(97, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x07\x04\x0b\x00\x0f``8\x18~N\xbf\x83\x07\x07\x18\x1f0?p\x7f\x7f\x7f\x9f\xcf\xcf\x8b\xc3\xc1'),
                            bytearray(b'\x00\x00\x00\x00\x04\x84\x02\x02\x06\x06\x1d\x19\x7fs\xff\xc3\xe0\xe0\xf8\xf8|\xfc\xfe\xfe\xfe\xfe\xf9\xf3\xf3\xd1\xc3\x83'),
                            bytearray(b'\x9c\x80\xc0\xc0\xf7\xf1|}y\x7f??\x0f\x0f\x07\x07\xe3\xe3\xff\xff\xf9\xfa~{x\x7f<?\x0c\x0f\x06\x07'),
                            bytearray(b'?\x07??\xffO\x1e^\xce\xfe\xfc\xfc\xf8\xf8\xe0\xe0\xc7\xc7\xff\xffO\xaf\xbe\xee\x0e\xfe\x1c\xfc8\xf8`\xe0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL811_BOX_BOY_SMALL,
    palette_offset=0,
    unknown_num=0
)
