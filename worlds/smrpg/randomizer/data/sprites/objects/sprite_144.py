# SPR0144_RED_DOT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL420_RED_DOT
sprite = CompleteSprite(
    animation=AnimationPack(346, length=77, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x008\x00H4|\x044L(8\x00\x00\x00\x00\x00\x00\x10\x00\x00 \x00 \x00\x00\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0)
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL420_RED_DOT,
    palette_offset=0,
    unknown_num=0
)
