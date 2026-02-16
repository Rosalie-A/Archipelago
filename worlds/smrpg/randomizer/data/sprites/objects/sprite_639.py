# SPR0639_ITEM_BAG_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(326, length=159, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x01\x00\x1e\x08\x0b\x04\x07\x02\x01\x02\x05\x02\x0b\x00-0\x00\x02\x08\x07\x00\x07\x02\x04\x04\x07\x00\x07\x03\x0c1\x06'),
                            bytearray(b'\x00\x80\xd0\xd8\xe0\xd0\x00\xa0 \xe0\x00\xc0P\x10\x8c@\x80@\xd8 \xd0 \x80` \xe0 \xe00\xf00\xfc'),
                            bytearray(b'?@\xff\x80\xfe\x80\x7fp\x9f\x10n\x8f\x13c\x07\x18@\x00\x83\x03\x81\x00q\x81\x11\xe1\x0f\xf1\x03\x7f\x00\x1f'),
                            bytearray(b'\xfa\xf8\xc09\xf2\t\xda9m\xa3Q\xcd\xe6\xd6\xc8(\xf8\x06\xf8\xc7\x88\x87\xb8\x87\xa1\x9f\xc3\xbf\xce\xfe\x18\xf8'),
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
