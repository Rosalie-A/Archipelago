# SPR0773_SMALL_YELLOW_SPIKE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL545_SMALL_YELLOW_SPIKE
sprite = CompleteSprite(
    animation=AnimationPack(167, length=28, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x06\x01\x0e\n\x15\x048@0\x00\xc0\x00\x00\x00\x00\x00\x02\x01\x03\x0b\x07\x14\x0c@0\x80@'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=124),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL545_SMALL_YELLOW_SPIKE,
    palette_offset=0,
    unknown_num=8
)
