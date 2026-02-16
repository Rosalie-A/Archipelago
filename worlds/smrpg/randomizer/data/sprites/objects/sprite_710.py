# SPR0710_SHOES_GRIDPLANE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        325,
        length=413,
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
                                None,
                                None,
                                None,
                                bytearray(
                                    b"\x00\x00\x00\x00\x00\x01\x01\x02\x06\x01\n\x05\x1b\x07\x0f\x1f\x00\x00\x00\x00\x00\x01\x00\x03\x03\x06\x04\x0b\x00\x1f\x07\x1f"
                                ),
                                bytearray(
                                    b"|8\x7f\x9d\x87{_\xbb\xbb\x7f\xf2\xf6\xe2\xe6\x80\x80\x18|\x19\xffA\xbf\x83\x7f\x1b\xffr\xf6\xe2\xe6\x80\x80"
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
                )
            ])),
    palette_id=SPAL523_RING,
    palette_offset=0,
    unknown_num=0)
