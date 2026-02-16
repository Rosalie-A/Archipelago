# SPR0637_RECOVERY_MUSHROOM_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(326, length=159, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x00\x17\x17\x7f\x1f??\xf9_{]\x7f\x7f\xdf_\x00\x07\x06\x19\x00\x7f _F\x99D\x99d\x9b@\xbf'),
                            bytearray(b'\xc0\xc0\xf0\xf0\x94\x84\x92\x82"\x12\xf3\xcb\xe2\xd2\xb2\x8a \xe0\x0c\xfc\x0e\xfe\x0e\xfe\x0f\xff\xc7?\xcf?\x87\x7f'),
                            bytearray(b'\xf3s\x9f\x9f\x7f\x7f\x06\x1d\x0e\x14!\x00\x18\x07\x1f\x1fO\xbf\x7f\xff\x7f\x7f<%\x14%\x00?\x00\x1f\x1f\x1f'),
                            bytearray(b'\xb6\xb6\xfe\xfe\xfe\xfe\x98\xf8\xc8\xa8\x8cL\x18\x98\xf0\xf0\xff\xff\xff\xff\xfe\xfe\x9c\xfc\x9c\xfc<\xfc|\xfc\xf0\xf0'),
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
