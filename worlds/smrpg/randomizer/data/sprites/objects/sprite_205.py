# SPR0205_MICROBOMB_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL243_MICROBOMB_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(161, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x1f\x10\x1f\x12\x0e5\x00\x7f\x04\xff@\xff\x04\x04\x04\x00\x07\x1c\x01\x12;$\x7f\x7f\xfb\x7f\xbf\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x18\x1c0\xbc(\xfc\x00\xdc\x00\xfc\x00\x00\x00\x00\x00\x00\x04\x08\x8c\x80\xd4\xc8\xdc\xe0\xfc\xe0'),
                            bytearray(b'\x08\xff@\xbf\x08\xf7\x00\x7f\x00?`\x1f\x17\t\x0b\x00\xb7\xbf\xb7\xf7\xf7\xff\x7f\x7f??\x7f\x7f\x7f>\x0f\x0f'),
                            bytearray(b'\x00\xfc\x00\xf8\x00\xe0\x00\xe0\x00\xc0\x00\x80\x00\x80\x00\x80\xfc\xe0\xf8\xe0\xe0\xe0\xe0\xc0\xc0\x80\x80\x00\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
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
    palette_id=SPAL243_MICROBOMB_PACKET,
    palette_offset=0,
    unknown_num=8
)
