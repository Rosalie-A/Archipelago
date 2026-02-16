# SPR0709_BROOCH_GRIDPLANE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING
sprite = CompleteSprite(
    animation=AnimationPack(385, length=130, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x02\x01\x03\x05\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x02\x00\x06\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xd00\xe8\x18\x10\xe8\xcc4\xd0|\x00\x00\x00\x00\x00\x000\x00\xf8\x00\x18\x04L@\x8c\x82'),
                            None,
                            bytearray(b'\x06\x01\x02\x05\x03\x05\x06\x04\x04\x06\x03\x02\x00\x00\x00\x00\x06\x00\x06\x00\x06\x00\x06\x01\x02\x05\x03\x00\x00\x00\x00\x00'),
                            bytearray(b'Dl$\xecd\xec\xc0\xc8\x18\x18\x00\x10 \xe0\x00\x00\x9c\x02\x1c\x02\x1c\x028\x06\x98f\x90l\xe0\x18\x00p'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=1, x=0, y=0),
                    ]
                ),
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
    palette_id=SPAL523_RING,
    palette_offset=0,
    unknown_num=0
)