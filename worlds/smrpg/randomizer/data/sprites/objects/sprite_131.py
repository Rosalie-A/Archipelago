# SPR0131_FAN_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL544_WAR_FAN
sprite = CompleteSprite(
    animation=AnimationPack(394, length=216, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(6, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\xe0@\xb0\x00\xe0P\xb0\x10\x90\x10\x90\x00\x00\x00\x00\xc0\xe0\xc0\xf0\xf0\xf0\xc0\xf0`\xf0`\xf0\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=134, y=128),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x02\x17(\x00\xfe?\x00\xfc\x00\x00\x00\x00\x00\x00\x00\x05\x07\xd8\xf8\x01\x01\xc0\xff\x03\xff\x00\x00'),
                            bytearray(b'\x00\x01\x03\x1c\x7f\x80\x80\x7f\x1f\x00\xff\x00\x00\x00\x00\x00\x06\x07l|\x80\x80@@\xe0\xff\x00\xff\xc0\xc0\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=118, y=128),
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
    palette_id=SPAL544_WAR_FAN,
    palette_offset=0,
    unknown_num=0
)
