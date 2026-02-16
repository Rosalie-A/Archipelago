# SPR0636_SMALL_FLOWER_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(326, length=159, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\n\x0e\x14\x18Iq\x8f\xe3v\x90`\x1bb\x1e\x00\x03\x0e\x018\'p\x0f\xe4\x1b\x94\t\x18\x84\x1e\x01"),
                            bytearray(b'\x00\x00\xf004\x1c\xfa\xce\xc7\xd73\x05\xe2\x0c\x8a\xfe\x00\xc08\xc8\x1c\xe0\x0e\xf0\x07\xf8\r\xf8\xdc1\xfe\x00'),
                            bytearray(b'\x1f\x10\x0b\x0e\x1f\x1f\xcf/$VXd\x00\x01\x01\x01\x10\x00\x1a\x1c\x7f\x7f\xff\xff\xff\xff\x7f\x7f\x03\x03\x01\x01'),
                            bytearray(b'\x98x\x08\xc8pp\xfe\xfev\xf9\xeds\xa8X\x90\xd0x\x00\xf88\xf0\xf0\xff\xff\xff\xff\xff\xff\xf8\xf8\xf0\xf0'),
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
