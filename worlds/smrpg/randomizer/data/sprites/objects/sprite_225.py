# SPR0225_LEVEL_UP_BONUS_SELECTION_BOX

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL492_LEVEL_UP_BONUS_SELECTION_BOX
sprite = CompleteSprite(
    animation=AnimationPack(374, length=68, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xff\x00\x00\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00\x00\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=144),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'),
                            None,
                            bytearray(b'\x02\x03\x03\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x00\x0c\x00\x07\x00\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xff\x00\x00\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'),
                            None,
                            bytearray(b'\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00'),
                            bytearray(b'\xff\x00\x00\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000\x000\x00\xe0\x00\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=136),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00'),
                            None,
                            bytearray(b'\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=144, y=120),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0@\xc0\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xe0\x000\x000\x00'),
                            None,
                            bytearray(b'\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\xa0`\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00\x10\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=104),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x02\x03\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07\x00\x0c\x00\x0c\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\xff\x00\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x05\x06\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00\x08\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=104, y=104),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=4, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL492_LEVEL_UP_BONUS_SELECTION_BOX,
    palette_offset=0,
    unknown_num=0
)
