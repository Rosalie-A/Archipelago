# SPR0708_CROWN_GRIDPLANE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        377,
        length=124,
        unknown=0x0002,
        properties=AnimationPackProperties(
            vram_size=2048,
            molds=[
                Mold(
                    4,
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
                                    b"\x00\x00\x00\x00\x08\x08\x04\x0c\t\x19r0s1V1\x00\x00\x00\x00\x08\x00\x08\x04\x19\x06\x10-b\x1de\x18"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x00\x02B@\xc4\xc4\xcc\xc5\xc5\x19\t\x1f\x0f\x00\x00\x00\x00B \x84b\x88v\x01\xfe\x19\xe6\x18\xe7"
                                ),
                                None,
                                bytearray(
                                    b"o\x10_\x00^\x11\x1f\x03\x7fG\x1e!\x18\x1f\x03\x03q\x00q`i\x12hgl\x033\x00\x1f\x00\x00\x03"
                                ),
                                bytearray(
                                    b"-\x9d\xff\x1f\xdf\x1fo\x8f\x0f\x8f~\xfe\xfc\xfc\xf0\xf0\xb8G\xfc\x03\xfc\xa3\xfc3\xb4k\x88v\xc0<\x00\xf0"
                                ),
                                None,
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=1,
                            x=0,
                            y=0),
                    ])
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
