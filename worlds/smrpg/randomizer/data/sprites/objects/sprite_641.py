# SPR0641_AMANITA_MUSHROOM_STANDALONE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL096_AMANITA
sprite = CompleteSprite(
    animation=AnimationPack(9, length=327, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            None,
                            None,
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x00\x01\x01\x01\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x02\x03\x02\x03\x02\x03\x03\x03'),
                            bytearray(b'\x0e\x00# \xce\xfe\xe4\x9er\x8e\xf3\x0f`\x9c\x88\xf8>>\xdf\xff\x00\xffb\x9dp\x8f0\xcf#\xdf\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x00\x00\x00\x00@\x00@\x00\xc0\x00\x00\x00\x00\x00\x80\x80\x00\x80\xc0\xc0\xc0\xc0\xc0\xc0\xc0\xc0'),
                            bytearray(b'\x02\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x01\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'a`\xdf\x00\xf8\x07\x10\x10\xa0\xa1\xc1\x83~~\x00\x00\x99\xff\xff\xff\xff\xff\x92m\xe7\x99\xef\xd3~~\x00\x00'),
                            bytearray(b'\x80\x00\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0)
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL096_AMANITA,
    palette_offset=0,
    unknown_num=0
)
