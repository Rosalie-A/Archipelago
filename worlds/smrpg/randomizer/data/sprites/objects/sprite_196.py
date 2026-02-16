# SPR0196_RING

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        155,
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
                                    b"\x00\x00\x00\x00\x07\x00\x18\x07 \x1c@0H0|\x00\x00\x00\x00\x00\x06\x06\x0f\x0f\x1c\x1cpppp0 "
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\xe0\x008\xc0\x0c\x00\x04\n\x06\x08\x0c\x02\x00\x00\x00\x00  \xe0\xe0\x04\x04\n\n\n\n\x02\x02"
                                ),
                                bytearray(
                                    b"6H>\x05\x14-\x10\x03\x08\x06\x00\x00\x00\x00\x00\x00HD\x03\x0f!?\x13\x1f\x0e\x0e\x00\x00\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"8\x04\xf0\x08\x00\xe0\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x0c\x0c88\xe0\xe0\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00"
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
