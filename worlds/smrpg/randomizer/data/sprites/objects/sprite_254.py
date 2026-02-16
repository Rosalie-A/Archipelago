# SPR0254_YOSHI_COOKIE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL674_GREEN_YOSHI

sprite = CompleteSprite(
    animation=AnimationPack(
        203,
        length=29,
        unknown=0x0002,
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
                            length=5,
                            subtile_bytes=[
                                bytearray(
                                    b"\x00\x07\x03\x1c\x14/#\x1f<#\x1f\x18\x07\x07\x00\x00\x00\x03\x00\x06\x10\x17\x00#\x04\x1c\x00\x07\x00\x00\x00\x00"
                                ),
                                bytearray(
                                    b"\x00\xe0\xa0xH\xd4\x048<\xc4\xf8\x18\xe0\xe0\x00\x00\x00\xc0\x00\xe0(\xe8\xc0\xc4 8\x00\xe0\x00\x00\x00\x00"
                                ),
                                None,
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=120,
                            y=124),
                    ]),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=1, mold_id=0),
                    ]
                ),
            ])),
    palette_id=SPAL674_GREEN_YOSHI,
    palette_offset=0,
    unknown_num=0)
