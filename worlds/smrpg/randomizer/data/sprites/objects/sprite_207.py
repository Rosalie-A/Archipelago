# SPR0207_BROOCH

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        165,
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
                                    b"\x00\x00\x03\x00\x07\x00\x04\x0b\x0b\x04\x0f\x15\x19\x05\x08\x17\x00\x00\x00\x00\x07\x00\x0c\x00\t\x01\x1a\x02\x1a\x00\x18\x00"
                                ),
                                bytearray(
                                    b"\x00\x00@\xc0\xa0`@\xa00\xd0@\xf0\x10\xb0\x90\xb0\x00\x00\xc0\x00\xe0\x00`\x100\x000\x08p\x08p\x08"
                                ),
                                bytearray(
                                    b"\r\x17\x1b\x13\x10\x18\x0c\x08\x00\x03\x00\x00\x00\x00\x00\x00\x18\x00\x18\x04\n\x15\x0e\x01\x03\x00\x00\x01\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x90\xb0\x00 ``\x00@\x80\x80\x00\x00\x00\x00\x00\x00p\x08\xe0\x18`\x98@\xb0\x80`\x00\xc0\x00\x00\x00\x00"
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
