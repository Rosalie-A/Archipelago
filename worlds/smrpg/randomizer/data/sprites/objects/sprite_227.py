# SPR0227_LIGHT_GREEN_PIPE_TOP_EDGE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL486_LIGHT_GREEN_PIPE_TOP_EDGE
sprite = CompleteSprite(
    animation=AnimationPack(366, length=40, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x04\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'\x04\x00<0\xfc\x00\xfc\x0c\xc4\xfc\x1c\xfc,\xfc\x9c|\x00\x00\x00\x00\x00\x00\x00\x00\xfc<\xfc\xfc\xfc\xfc\xfc\xfc'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=140, y=96),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\xfe\x7f\xd0/\xe0\x1f\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x81\x00\xff\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xff\x00\xff\x00}\xfa~\xf9\xff\xf8\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x07\xff\x07\xff\x07\xff'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=104),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00  \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            bytearray(b'  8\x08?\x01?\x00!% & & $\x00\x00\x00\x00\x00\x00\x00\x00:\x00\x19\x009\x00;\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\xff\x00\xff\x00\xdf\xc0\xdf\xc0\xcf\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0?\xc0?\xc0?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=96),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL486_LIGHT_GREEN_PIPE_TOP_EDGE,
    palette_offset=0,
    unknown_num=0
)
