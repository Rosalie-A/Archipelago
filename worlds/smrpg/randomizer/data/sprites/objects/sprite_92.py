# SPR0092_TOADSTOOL_DOLL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL654_TOADSTOOL_WALKING_DOWN_LEFT
sprite = CompleteSprite(
    animation=AnimationPack(282, length=46, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x02\x00\x02\x00\x03\x06\x00\x0f\x00\x06\x01\x02\x0c\x0f\x01\x0c\x02\x02\x05\x00\n\x04\x00\r\x01\x02\x0c\x04\x00\x08\x0f\x00'),
                            bytearray(b'\x00\x80\x80\x00 `p\xf0P\xd0\x88\x88@`\xe0 \x80\x80\xc0\x80\x80`\x00\xf0 \xd0p\x08\x90 \xd8 '),
                            bytearray(b'\x01\x05\n\x06\x19\x0f\x00\x0f\x00\x0f\x0e\x0f\r\r\n\x08\x07\n\x04\x05\x1f\x10\x0f\x00\x0f\x10\x0f\x10\r\x12\n\r'),
                            bytearray(b'\x10\xd0\xe0\x90p\x80p\xa0`\xa0 \xa0 \x00@@\xe8\x10\xe8\x10\xb8\x00\xb0 \xe0`\xa0` \xc0@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x00\x07\x04\x01\x0f\x00\x0f\x04\x07\x07\x07\x08\x0f\x00\x00\x03\x03\x06\x02\x00\x0f\x00\x08\x08\x04\x08\x07\x00\x0b'),
                            bytearray(b'\x00\x00\x80\x00@\xc0\x10\xf0\x10\xd0`\xc0\x00\x00\xc0\xc0\x00\x00\x80\x80\x80\xc0\x00\xf0 \xd0 \xc0\xf0\x000\xc0'),
                            bytearray(b'\x08\x0f\x00\x0f\x18\x0f\x17\x07\x00\x08\x1d\x1c\x0f\x0e\x0f\x0e\x00\t\x00\x08\x10\x1d\x08\x07\x0f\x10\x1d\x02\x0f\x10\x0f\x08'),
                            bytearray(b'\xc0\xc0H\xc0\xd0\xc0\xa0\x80\xe0\x00\xe0\xe0`\x00@@8\xc08\xc00\xc0`\x80\xe0\x00\xe0\xe0`\x80@\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(2, gridplane=False,
                    tiles=[]
                ),
                Mold(3, gridplane=False,
                    tiles=[]
                ),
                Mold(4, gridplane=False,
                    tiles=[]
                ),
                Mold(5, gridplane=False,
                    tiles=[]
                ),
                Mold(6, gridplane=False,
                    tiles=[]
                ),
                Mold(7, gridplane=False,
                    tiles=[]
                ),
                Mold(8, gridplane=False,
                    tiles=[]
                ),
                Mold(9, gridplane=False,
                    tiles=[]
                ),
                Mold(10, gridplane=False,
                    tiles=[]
                ),
                Mold(11, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\x00\x03\x00\x0b\x08\x12\x1d\x01\x0f0?\x00\x00\x00\x00\x01\x01\x02\x02\x06\n\x03\x1e\x11\x0e\x00?'),
                            bytearray(b'\x00\x00\x00\x00\xa0\x18\xf0\x08\xb4\xa4\xc2^\xc2\x8e\xc4\xfc\x00\x00\x00\x00\x18\x18\x08\x08Z\xb4\xb1\xfe\xb1.\x03\xfc'),
                            None,
                            bytearray(b' ?\x18\x1f\x0c\x0f\x08\x08\x03\x03\x02\x03%5@\x06\x00<\x00\x1c\x10\r\x17\x08\x1e\x02\x0c\x10\x04\nG9'),
                            bytearray(b'\x04\xfc%\xfd\x01\x11\xd0\xd0\xe8\xe3\x11\xc9!>\x83.\x03\xfc\x02\xfd\xee\x11/\x10\xdc\xc3>\x07\xff\x00\xaf\xd0'),
                            bytearray(b'\x00\x00\x00\x00\x80\x80\x00\x00\x80\x80@\xc0\x80\x80\x00@\x80\x00\x80\x00@\x80\xe0\x00p\x800\xc0x\x80\xb8@'),
                            bytearray(b'\x00\x0f1?=?\x9e\x1e\x8f\x8ea@?8\x07\x07\x0fp?\xc0?\xc0\x9ea\x8f\xf0a^?8\x07\x07'),
                            bytearray(b'\x0e\xee\x05\xff\x83\xf2\xe2\xe1C@\x07\x01\xfe\x06\xf8\xf8\xef\x10\xf8\x00\xf1\r\xe3\x1dC\xbc\x07\xf9\xfe\x06\xf8\xf8'),
                            bytearray(b' `\x80 \x80\x00\xc0\x00\xe0\x00\x80\xc0\x00\x00\x00\x00\x98`\xd8 p\x00\xf0\xc0`@\xc0\xc0\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=1, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=1),
                    ]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=11),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL654_TOADSTOOL_WALKING_DOWN_LEFT,
    palette_offset=0,
    unknown_num=0
)
