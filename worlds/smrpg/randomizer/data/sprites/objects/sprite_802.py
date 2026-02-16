# SPR0802_BACKWARDS_YELLOW_SPIKE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL309_BACKWARDS_YELLOW_SPIKE
sprite = CompleteSprite(
    animation=AnimationPack(175, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x04\x02#\x1cw:\xa8\xd0\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x00}\x00\x0f\x00'),
                            bytearray(b'\x00\x00\x00\x00\t\x06\xa3d\x96\x18lp\x1c`\xf8\xa0\x00\x00\x00\x00\x00\x00\x18\x00\xe0\x00\x80\x00\x80\x00\x00\x00'),
                            bytearray(b'}\x85\xfe\x03|\x83\xfe\x01\x7f@\x1f \x0c\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'0\xc0`\x80\xe0\x00\xc0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
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
    palette_id=SPAL309_BACKWARDS_YELLOW_SPIKE,
    palette_offset=0,
    unknown_num=8
)
