# SPR0711_RING_GRIDPLANE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        327,
        length=34,
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
                            format=0,
                            length=10,
                            subtile_bytes=[
                                None,
                                None,
                                None,
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x0c\x03\x10\x0e \x18\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x07\x07\x0e\x0e88"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x00\x00\x00\xf0\x00\x1c\xe0\x06\x00\x02\x05\x00\x00\x00\x00\x00\x00\x00\x00\x10\x10\xf0\xf0\x02\x02\x05\x05"
                                ),
                                None,
                                bytearray(
                                    b'$\x18>\x00\x1b$\x1f\x02\n\x16\x08\x01\x04\x03\x00\x0088\x18\x10$"\x01\x07\x10\x1f\t\x0f\x07\x07\x00\x00'
                                ),
                                bytearray(
                                    b"\x03\x04\x06\x01\x1c\x02x\x84\x00\xf0\x00\xc0\x00\x00\x00\x00\x05\x05\x01\x01\x06\x06\x9c\x9c\xf0\xf0\xc0\xc0\x00\x00\x00\x00"
                                ),
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
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ])),
    palette_id=SPAL523_RING,
    palette_offset=0,
    unknown_num=0)
