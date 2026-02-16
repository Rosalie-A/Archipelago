# SPR0815_GREEN_MUSHROOM_ITEM

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL384_YELLOW_JUICE
sprite = CompleteSprite(
    animation=AnimationPack(163, length=121, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x07\x00\x1f\x00>\x01~\x01}\x03{\x04F|\x00\x00\x00\x03\x00\x03\x00 \x00p\x00p\x00#\x00\x03'),
                            bytearray(b'\x00\x00@@H@\x8c\x84\x86\x8e\x86\x8e\x1e\x04>\x00\x00\x00`\x80x\x80|\x00~\x08~\x08~\x80~\x80'),
                            bytearray(b'8:\x00\x00\x02\x02\x01\x03\x00\x07\x04\x07\x00\x00\x00\x00\x06\x03\x0f\x00\x01\x03\x00\x03\x00\x07\x00\x07\x00\x00\x00\x00'),
                            bytearray(b'|\x80\xf0\x00\x00\x00\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\xfc\x80\xf0\x00\xc0\xc0\xc0\xc0`\xe0`\xe0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL384_YELLOW_JUICE,
    palette_offset=0,
    unknown_num=0
)
