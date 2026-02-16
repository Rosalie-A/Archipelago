# SPR0252_FEATHER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL584_FEATHER
sprite = CompleteSprite(
    animation=AnimationPack(202, length=29, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x18\x18<<<<\x0e>&.$$DDP@\x18\x18<<<<>\x0e\x1e6\x1c<<|8x'),
                            None,
                            bytearray(b'P@P@@@  @\x00\x10\x000\x10\x00\x008x8x8xXxpp0000\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=120),
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
    palette_id=SPAL584_FEATHER,
    palette_offset=0,
    unknown_num=0
)
