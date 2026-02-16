# SPR0251_PARASOL_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL559_PARASOL
sprite = CompleteSprite(
    animation=AnimationPack(393, length=260, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x80\xc0\xc0\x00\xa0\x00\xfc\x8c\xd0\x00\x00\x00\x00\x00\x00\x80\x80\x00@``\x00\x0c|<\x00\xe0\x00\xc0\x00\x80'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=129),
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x00 \x18H,\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x18\x008\x18h'),
                            None,
                            bytearray(b'\x14k$K.M\x06\x01? \x0c\x0e\x08\x1c\x05\x00\x14p\xae`\xb3p~\x04??\x11\x11\x11\x13\x0f\n'),
                            bytearray(b'\x1e^?\x7f\x1c|\x80i\x07\x1f\xaaD\x80@\x00\x00as\xce\x80\xe3\x83\x9e\x16\x08\xe0\xaa\x11\x80?\x00?'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=121),
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
    palette_id=SPAL559_PARASOL,
    palette_offset=0,
    unknown_num=0
)
