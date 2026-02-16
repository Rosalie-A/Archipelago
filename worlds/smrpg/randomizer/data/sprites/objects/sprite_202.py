# SPR0202_SHOES

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        161,
        length=31,
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
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x02\x05\x05\n\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x03\x01\x06\x02\r"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\xf0\xe0\xfct\x1c\xec|\xec\x00\x00\x00\x00\x00\x00\x00\x00`\xf0d\xfc\x04\xfc\x0c\xfc"
                                ),
                                bytearray(
                                    b"\x1a\x05+\x17o\x1f>~\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x1b\x11/\x03\x7f\x1e~\x00\x00\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\xec\xfc\xc8\xd8\x88\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00l\xfc\xc8\xd8\x88\x98\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
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
    palette_id=SPAL523_RING,
    palette_offset=0,
    unknown_num=0)
