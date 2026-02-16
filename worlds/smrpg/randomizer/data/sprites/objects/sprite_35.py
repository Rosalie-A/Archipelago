# SPR0035_EMPTY

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL000_NOTHING
sprite = CompleteSprite(
    animation=AnimationPack(0, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xff\xf0\xff\xc0\xff\x80\xff\x80\xff\x00\xff\x00\xff\x00\xff\x00\x0f\xff?\xff\x7f\xff~\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xe0\xe0'),
                            bytearray(b'\xff\x0f\xff\x03\xff\x01\xff\x01\xff\x00\xff\x00\xff\x00\xff\x00\xf0\xff\xfc\xff\xfe\xff~\x7f\x7f\x7f\x7f\x7f\x7f\x7f\x07\x07'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\xff\x00\xff\x80\xff\x80\xff\xc0\xff\xf0\xe0\xe0\xfe\xfe\xfe\xfe\xfe\xfe~\xfe\x7f\xff?\xff\x0f\xff'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\xff\x00\xff\x01\xff\x01\xff\x03\xff\x0f\x07\x07\x7f\x7f\x7f\x7f\x7f\x7f~\x7f\xfe\xff\xfc\xff\xf0\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL000_NOTHING,
    palette_offset=0,
    unknown_num=8
)
