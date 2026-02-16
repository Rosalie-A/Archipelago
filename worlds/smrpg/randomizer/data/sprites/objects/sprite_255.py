# SPR0255_BEETLE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL423_BEETLE

sprite = CompleteSprite(
    animation=AnimationPack(
        199,
        length=66,
        unknown=0x0000,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    0,
                    gridplane=False,
                    tiles=[
                        Tile(
                            mirror=False,
                            invert=False,
                            format=0,
                            length=7,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x06\x07\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00  00\xc0\xc0\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\t\x0f\x0b\r\x0e\x0e\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x02\x06\x06\x00\x08\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xc0\xc0\xa0\xa0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=120,
                            y=120),
                    ]),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ])),
    palette_id=SPAL423_BEETLE,
    palette_offset=0,
    unknown_num=0)
