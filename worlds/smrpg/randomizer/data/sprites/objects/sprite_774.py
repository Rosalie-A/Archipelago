# SPR0774_LARGE_YELLOW_SPIKE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL552_LARGE_YELLOW_SPIKE
sprite = CompleteSprite(
    animation=AnimationPack(168, length=31, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x03\x02\x07\x07\x06\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x02\x00\x04\x00\x0e\t'),
                            bytearray(b'\x00\x00\x10(l\\\xccR\x1e\xb4\xa032u\x8c\x82\x00\x00\x08\x00\x04\x00\xaa\x06r\x0e\x8f\x7f\x0f\xff~\xfe'),
                            bytearray(b'\x0e\x03\x1c\x0e&\x1dxw\xe0x\x00\xc0\x00\x00\x00\x00\x1e\x11\x1d\x033\x0fo\x1f\xd8\xb8\xc0\xc0\x00\x00\x00\x00'),
                            bytearray(b'xF\xc08\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xbe\xfe\xf8\xf8\xe0\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
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
    palette_id=SPAL552_LARGE_YELLOW_SPIKE,
    palette_offset=0,
    unknown_num=8
)
