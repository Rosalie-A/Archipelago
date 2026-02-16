# SPR0627_MUSHROOM_HOUSE_DECOR_MAILBOX

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL707_MUSHROOM_HOUSE_DECOR_MAILBOX
sprite = CompleteSprite(
    animation=AnimationPack(407, length=41, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x16\xe8\t6\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xf7\xff??\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc0\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=125, y=138),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\xfe\xfep\xff\xfe\xe3~\xc0\xbc@\xf8\x00\x00\x00\x00\x00\x1e\x00\x00\x00\x1e\x00>\x01<\x02\x18\x04'),
                            None,
                            bytearray(b'\xb0t\xa0\xa4\xe0\xe4p\xe4$\xc0\xe0\x00\xe0\x000@\x0c\x00p,\xe0\xfcp\xfc0\xfc0\xf00\xf0\xb0\xf0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=133, y=122),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x01\x01\x03\x03\x00\x00\x00\x00\x00\x00\x01\x00\x03\x00\x02\x00\x06\x00\x0c\x00'),
                            bytearray(b'88qO\xdc\xa3\xbc\xc3\xf8\x87\xbf\xdf~\xc3\x7f\xc28\x04p\x00\xc0\x00\x00\x00\x00\x00\x1c\x00~\x00~\x00'),
                            bytearray(b'\x07\x07\x1f\x1f\x1f\x1f\x00\x00\x00\x00\x01\x01\x03\x03\x01\x01\x18\x008\x00\x10 \x0f0\x1f\x00\x0f\x01\x03\x03\x01\x01'),
                            bytearray(b'\xff\x80\xfd\x8b\xf4\xd4GG??\xfb\xff\xce\xf0"\xdc\xfc\x00\xf8\x00\xf3\x08\xc7??\xff\xfb\xff\xe3\xff\xe3\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=122),
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
    palette_id=SPAL707_MUSHROOM_HOUSE_DECOR_MAILBOX,
    palette_offset=0,
    unknown_num=0
)
