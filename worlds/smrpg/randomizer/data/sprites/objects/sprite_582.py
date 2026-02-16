# SPR0582_MARIO_CROUCH

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL644_MARIO_ATTACK_UP_RIGHT
sprite = CompleteSprite(
    animation=AnimationPack(245, length=721, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x80\xc0\x80\xc0\x80@\x00\x80\x00\x80\x00\x80\x00\x00\x80\x80\x00\x80@\x80@\x00\xc0\x00\x80\x80\x00\x80\x00'),
                            None,
                            bytearray(b'\x00\x00\x00\x00@\xc0@\xc0\x00\xe0\xe0\x10\xe0\x10\xe0\x00\x00\x00\x00\x00\xc0\x00\xc0\x00\xe0`0000\xa0\xa0'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=136, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'?\x07O\x03W\x11\x13B\x03s Q\x01!\x07\x07\x07?\x03\x7f\x11oE~}~~\x7f./\x08\x0f'),
                            bytearray(b'\xfc\x01\xff\x00\xf8\xfb;;\x17p\x0f\xf0\x0f\xf1\x00\xf9\x02\xfc\x07\xf8\xf7\xf8\x03\xfc\x00\xff\x00\xff\x00\xfe\x07\xff'),
                            bytearray(b'\x12\x13\x10\x118(> ? \x1f\x1f\x00\x00\x00\x00\x1c\x1f\x1e\x1f/?-3.1\x1f\x1f\x00\x00\x00\x00'),
                            bytearray(b'\x00\xff\x04\xff\x10\x16!<\xff\x80\xef\x80\xff\x83||\x00\xff\x00\xff\xe9\xff\xc2\xff\xba\xc5\x98\xe7\xf3\x8f||'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x07'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\xc0\x00\x1e\x1e\x7f\x7f\x00\x00\x00\x00\x00\x00\x00\x00\x1c\x00\x00\xfe\x1e\xe1\x7f\x80'),
                            bytearray(b'\x08\x00\t\x01\t\x01\x18\x00\x1b\x03\x1b\x03\x0f\x03\x07\x05\x00\x0f\x01\x0e\x01\x0e\x00\x1f\x03\x1c\x03\x1c\x03\x0c\r\x06'),
                            bytearray(b'\xff\xff\xff\xff\xff\xff|\x7f\xf9\xff\x82\xfe\xda\xf9\xe4\xe1\xff\x00\xff\x00\xff\x00\x7f\x80\xff\x00\xfe\x01\xf8\x06\xe2\x1c'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=100),
                    ]
                ),
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
    palette_id=SPAL644_MARIO_ATTACK_UP_RIGHT,
    palette_offset=0,
    unknown_num=0
)
