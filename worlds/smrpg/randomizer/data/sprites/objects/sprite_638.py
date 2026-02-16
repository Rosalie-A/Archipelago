# SPR0638_KEY_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(326, length=159, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00<"z\x07m\x1f\x9a{\x98\xd8\xbf\xd9\x99\xfa\x00\x1e \x01\x00@\x8c\xcc\x1c\x8c\x1c?\x1a<\x18<'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\xa1\x00\xfe@\x86x\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00@\xff\xa0\x01\x00\x01'),
                            bytearray(b'\xb8\xdc\x98\xf8\x89\xc8\x82aA3\x0c7 \x1e\x00\x0c\x18?\x1f?\x1e?\x0e\x9c\x8c\xcc\x08\x00\x00!\x01\x13'),
                            bytearray(b'\x00\x00\x00\x00\x14\x08\x9c\x08\x94\x18\x14\x18\x00\x00\x00\x00\x01\xff\xe4\xfc\xd0\xc4\xd0D\xd0D\x90\x84\x8c\x8c\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=0,
    unknown_num=0
)
