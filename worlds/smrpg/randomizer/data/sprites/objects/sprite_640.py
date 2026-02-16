# SPR0640_MUSIC_NOTE_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(326, length=159, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x02\x02\x03\x03\x03\x03\x03\x03\x02\x02\x02\x02\x02\x02\x02\x02\x02\x02\x03\x03\x03\x03\x03\x03\x02\x02\x02\x02\x02\x02\x02\x02'),
                            bytearray(b'\x00\x00\x80\x80\xe0\xe0\xf0\xf000\x10\x10    \x00\x00\x80\x80\xe0\xe0\xf0\xf000\x10\x10    '),
                            bytearray(b'\x02\x02\x1e\x1eoo\xa7\x87\x8f\x8f\xff\xff~~<<\x02\x02\x1e\x1e\x7f\x7f\xdf\xdf\xff\xff\xff\xff~~<<'),
                            None,
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
