# SPR0081_MALLOW_DOLL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL697_MALLOW_WALKING_DOWN_LEFT
sprite = CompleteSprite(
    animation=AnimationPack(363, length=46, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00`p\xe0\x00p\xa1\x82\xcb$3\x1a\x17\x00\x00\x00\x00\x90\x10\x10\x00\x01\x00=\x08J\x02"\x02'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x0e\xc8\x07\xd1A\xbb\xe2\x86\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xb8\x10\x94\x90\x99\x80'),
                            bytearray(b'\x0f\x00\x13\x1fw\x7f\x9e\xf9\x88\xff[x77\x00\x00\x10\x00\x03\x10i\x18\xff\x87\xf8\x83\x7fO77\x00\x00'),
                            bytearray(b'x\x98P0\xc0\xc8h\x90xpHx\xc8\xf8pp\x06\x00\x8c\x008\x08\xf8\x90\xb8\xc0\xf8\x80\xf8\x80pp'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
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
    palette_id=SPAL697_MALLOW_WALKING_DOWN_LEFT,
    palette_offset=0,
    unknown_num=0
)
