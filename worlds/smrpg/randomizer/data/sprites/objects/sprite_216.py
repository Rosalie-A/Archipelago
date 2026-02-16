# SPR0216_CROWN

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL523_RING

sprite = CompleteSprite(
    animation=AnimationPack(
        172,
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
                                    b"\x00\x00\x10\x10\x08\x19\x133\xe5a\xe6b\xacb\xde!\x00\x00\x10\x00\x11\x083\x0c [\xc4;\xca1\xe3\x00"
                                ),
                                bytearray(
                                    b"\x00\x00\x04\x84\x80\x88\x88\x98\x8a\x8a2\x12>\x1eZ:\x00\x00\x84@\x08\xc4\x10\xec\x02\xfc2\xcc0\xcep\x8e"
                                ),
                                bytearray(
                                    b'\xbf\x00\xbd">\x07\xfe\x8f<C1?\x07\x07\x00\x00\xe3\xc0\xd3%\xd1\xce\xd9\x06g\x00?\x00\x00\x07\x00\x00'
                                ),
                                bytearray(
                                    b"\xfe>\xbe>\xde\x1e\x1e\x1e\xfc\xfc\xf8\xf8\xe0\xe0\x00\x00\xf8\x06\xf8F\xf8fh\xd6\x10\xec\x80x\x00\xe0\x00\x00"
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
