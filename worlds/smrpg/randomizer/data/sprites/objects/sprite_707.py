# SPR0707_BANANA_GRIDPLANE

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
                                    b"\x00\x00\x00\x00\x00\x00\x01\x00\x01\x02\x03\x00\x03\x01\x03\x01\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x03\x01\x03\x01"
                                ),
                                bytearray(
                                    b"\x00\x00\x00\x80\xc0@\xa0`\xc0 \xc0 \xc0`\xe0`\x00\x00\x80\x00\xc0\x00\xe0\x00\xe0\x00\xe0\x00\xe0@\xe0@"
                                ),
                                None,
                                bytearray(
                                    b"\x03\x05\x07\x00\x87\x08\xfd\x02\xf9\x86g^\x01\x00\x00\x00\x07\x01\x07\x00\x8f\x00\xff\x00\xff\x00\x7f\x00\x01\x06\x00\x00"
                                ),
                                bytearray(
                                    b"\xf0p\xb3s\x82}\x97x\xb5{\x84d\xe0\x00\xe0\x00\xf0@\xf3\x00\xff\x00\xff\x00\xff\x00\xe4\x18\xe0\x10\xe0\x10"
                                ),
                                bytearray(
                                    b"\x00\x00\xc0\x00\x80@\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xc0\x00\x80@\x00\x80\x00\x00\x00\x00\x00\x00"
                                ),
                            ],
                            is_16bit=False,
                            y_plus=0,
                            y_minus=0,
                            x=0,
                            y=0),
                    ])
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
