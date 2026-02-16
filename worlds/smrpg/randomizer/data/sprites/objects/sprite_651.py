# SPR0651_TINY_BLOOBER_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL032_BLOOBER

sprite = CompleteSprite(
    animation=AnimationPack(
        11,
        length=435,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    0,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=1,
                            length=13,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x01\x03\x07\x0f\x0f\x1f\x1f???/'\x01\x1c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x0c\x0e"
                                ),
                                bytearray(
                                    b"\x00\x00\x80\x00@\x00\x80\x80\xd0\xd0\xe0\xf0\xd8\xd8\xd8\xd8\x00\x00\x00\x80\x80@@ \x000 \x10 \x180\x08"
                                ),
                                None,
                                bytearray(
                                    b"\x02\x13\t\x1b\x1c=\x06&\x12\x1a\x14\x1d\x01\x00\x00\x00\x17\x1d\x0e?\x03\x03\t\x10\r\x10\x04\x10\x00\x01\x00\x00"
                                ),
                                bytearray(
                                    b"`\xe0\x00\xe0 `00\x90\x90\x80\xc0\x00\x00\x00\x00\x18\x08\xa8\xd8 \xe00\xf00\xf0\xa0\xe0\x00\x00\x00\x00"
                                ),
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=1,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    1,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=1,
                            length=13,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x01\x00\x0f\x0f\x1f?\x0f\x1f\x03\x1b\x00\x00\x00\x00\x00\x00\x01\x02\x00\x10\x00\x00\x00 \x18\x1c"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00@\xc0\xc0\xe0\xc0\xd0\xe8\xe0\xfc\xf4\x00\x00\x00\x00\x00\x00\x00\x00 \x000\x00\x10\x08\x00\x0c"
                                ),
                                None,
                                bytearray(
                                    b'\x187Dw\x19|9=\r\r\x07\x07\x00\x00\x00\x00\x1f7G\x0f\x12\x01\x06h"=\x07\x05\x00\x00\x00\x00'
                                ),
                                bytearray(
                                    b"\xf8\xf4\xa0\\Hh\xd4T4\xa4X\xc8\x00\x00\x00\x00\x80LX\xe4\xd8\xf8L<\xcc|h\xf8\x00\x00\x00\x00"
                                ),
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=1,
                            x=0,
                            y=0),
                    ]),
                Mold(
                    2,
                    gridplane=True,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=1,
                            length=13,
                            subtile_bytes=[
                                bytearray(
                                    b"\x01\x00\x03\x03\x07\x07\x07\x0f\x1f\x1f\x0f\x1f\x1f\x0b\t\x0f\x00\x01\x00\x00\x00\x00\x00\x00\x10\x00\x00\x00\x18\x00\x0f\x06"
                                ),
                                bytearray(
                                    b"\x80\x80\xc0\x80\xa0\x80\xd0\xf0\xd0\xd0\xd0\xf0\xf0\xf0\xf0\xf0\x00\x00\x00@@  \x10 \x10\x08\x18\x08\x18\x18\x08"
                                ),
                                None,
                                bytearray(
                                    b"\x03\x0e\x04\x04\x07\x07\x06\x07\x08\x05\r\x0f\x04\x06\x06\x02\x0f\x0c\x07\x0f\x01\x08\x01\x08\x0f\x00\x03\x04\x02\r\x00\x07"
                                ),
                                bytearray(
                                    b" \xa8@\xc0@\xc0`\xa0`\xa0\xe0\xa0\xe0\xa0\x00\x00\x90\xc8\xc8\xf8\xa0`\xa0`\xa0` \xe0 \xe0\x80\xc0"
                                ),
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=1,
                            x=0,
                            y=0),
                    ]),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=12, mold_id=2),
                    ]
                ),
            ])),
    palette_id=SPAL032_BLOOBER,
    palette_offset=0,
    unknown_num=0)
