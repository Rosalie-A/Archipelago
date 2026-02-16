# SPR0440_MICROBOMB

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL243_MICROBOMB_PACKET
sprite = CompleteSprite(
    animation=AnimationPack(127, length=90, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x1f\x10\x1f\x12\x0e5\x00\x7f\x04\xff@\xff\x04\x04\x04\x00\x07\x1c\x01\x12;$\x7f\x7f\xfb\x7f\xbf\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x18\x1c0\xbc(\xfc\x00\xdc\x00\xfc\x00\x00\x00\x00\x00\x00\x04\x08\x8c\x80\xd4\xc8\xdc\xe0\xfc\xe0'),
                            bytearray(b'\x08\xff@\xbf\x08\xf7\x00\x7f\x00?`\x1f\x17\t\x0b\x00\xb7\xbf\xb7\xf7\xf7\xff\x7f\x7f??\x7f\x7f\x7f>\x0f\x0f'),
                            bytearray(b'\x00\xfc\x00\xf8\x00\xe0\x00\xe0\x00\xc0\x00\x80\x00\x80\x00\x80\xfc\xe0\xf8\xe0\xe0\xe0\xe0\xc0\xc0\x80\x80\x00\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=112),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x02\x02\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x00pp  \x00\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x00'),
                            bytearray(b'\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@@\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=127, y=106),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x02\x02\x00\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x00pp  \x00\x00\x00\x00\x00\x10\x00 \x00\x00\x00\x00'),
                            bytearray(b'\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80@@\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=372, y=110),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x1f\x18\x1f\x12\x0e\x04\x00\x00\x00\x00@@\x04\x04\x04\x00\x07\x1c\x01\x12;\x0e\x7f\x00\xff\x04\xbf@'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x04\x18\x0c0\x1c 4\x08\x1c\x00\x00\x00\x00\x00\x00\x00\x04\x04\x8c\x0c\xdc\x1c\xf44\xfc\x1c'),
                            bytearray(b'\x08H\x00H\x00\x08\x00\x00\x00\x00`\x00\x17\x00\t\x00\xb7H\xb7H\xf7\x08\x7f\x00?\x00\x7fa\x7f7\x0f\x0f'),
                            bytearray(b'\x1c\x00\x10\x08\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x00\xfc\x1c\xf8\x90\xe0\x00\xe0 \xc0@\x80\x00\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=111),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x10\x00(\x00\x10\x00\x00\x00\x00\x00\x00\x08\x08  \x08\x18\x108\x08\x18\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=106),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x1c\x008\x00`\x00@\x10\x10\x10\x1088\xf0\xfe`|D|\x0en\x02B'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=130, y=111),
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x0e\x00\x1c\x008\x00`\x00@\x10\x10\x10\x1088\xf0\xfe`|D|\x0en\x02B'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=373, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x1f\x10\x1f\x12\x0e5\x00\x7f\x04\xff@\xff\x04\x04\x04\x00\x07\x1c\x01\x12;$\x7f\x7f\xfb\x7f\xbf\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x18\x1c0\xbc(\xfc\x00\xdc\x00\xfc\x00\x00\x00\x00\x00\x00\x04\x08\x8c\x80\xd4\xc8\xdc\xe0\xfc\xe0'),
                            bytearray(b'\x08\xff@\xbf\x08\xf7\x00\x7f\x00?`\x1f\x17\t\x0b\x00\xb7\xbf\xb7\xf7\xf7\xff\x7f\x7f??\x7f\x7f\x7f>\x0f\x0f'),
                            bytearray(b'\x00\xfc\x00\xf8\x00\xe0\x00\xe0\x00\xc0\x00\x80\x00\x80\x00\x80\xfc\xe0\xf8\xe0\xe0\xe0\xe0\xc0\xc0\x80\x80\x00\x80\x80\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=122, y=112),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=2),
                        AnimationSequenceFrame(duration=2, mold_id=1),
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
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
