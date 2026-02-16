# SPR0564_BOWSER_S_SPIKE_SHOT

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL382_BOWSER_S_SPIKE_SHOT
sprite = CompleteSprite(
    animation=AnimationPack(220, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x01\x04\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00'),
                            bytearray(b'\x00\x00\x00\x00\x18\x04l\x1a\xd8>*\xe6\xec\xdd4s\x00\x00\x00\x00,\x00\x06\x00\x06\x00\x1e\x01<\x03\xf0\x0f'),
                            bytearray(b'\x0e\x05\x15\x034\r\x10v\xc0\xd0\x00\x00\x00\x00\x00\x00\x03\x00\x0f\x00\x1c\x030\x0e@0\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xd0\xcf@<\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0?\x00\xfc\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
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
    palette_id=SPAL382_BOWSER_S_SPIKE_SHOT,
    palette_offset=0,
    unknown_num=8
)
