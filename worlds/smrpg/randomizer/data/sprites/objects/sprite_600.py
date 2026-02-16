# SPR0600_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL797_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE
sprite = CompleteSprite(
    animation=AnimationPack(363, length=46, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x02\x03\x01\x02\x01\x06\x0c\x0f\x02\x07\x00\x03\x00\x00\x00\x00\x03\x00\x03\x01\x06\x00\x0f\x00\x00\x01\x05\x01'),
                            bytearray(b'\x00\x00\x00\x00@\xc0 \xe00p\xa0\xe0`\xc0p\xd0\x00\x00\x00\x00\xc0\x00\xe0\x00\xf0\x00\xe0\x10\x10 \x00 '),
                            bytearray(b'\x07\x01\x0f\x0f\x06\x0f\x0c\x07\x07\x07\x00\x02\x07\x00\x0f\x0e\x03\x05\x0c\x00\x0b\x08\x08\x0f\x08\x07\x01\x07\x06\t\x0e\x0f'),
                            bytearray(b'\xa0\x80\x80\x00@\xe0\x00\xf0p@P\xc0\xa0\x00\xa0 \xc0\xa0\x80``\x800P\xb0\xf00\xd0\x80`\xa0`'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=114),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x03\x04\x07\x04\x07\x04\x07\x06\x03\x03\x03\x00\x00\x00\x00\x02\x00\x07\x00\x07\x00\x07\x00\x07\x00\x05\x00'),
                            bytearray(b'\x00\x00\x00\x00\x00\xc0 \xe00\xf0\x00\xe0\x08\xf8\x18\xf0\x00\x00\x00\x00\xc0\x00\xe0\x00\xf0\x00\xe0\x10\xf8\x00\xf8\x00'),
                            bytearray(b'\x02\x00\x05\x07\x02\x07\x04\r\x0f\x03\x01\x0f\x07\x03\x06\x04\x02\x01\x03\x05\x06\x01\x08\x0b\x04\x07\x0c\x0f\x04\x03\x04\x07'),
                            bytearray(b'\x90\x80\xe0\xe0\xc0\xc0\xc0\xc0\x00\x00  @\x00\xc0\xc0\x90`\xd0\xe00\xe00\xe0\xe0\xe0\xe0\xe0@\xa0\xc0\xc0'),
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
                            bytearray(b'\x03\x00\x0e\x00\x1c\x10\x19\x11\x1b\x13\x1b\x13\n\x04\x0c\x03\x03\x00\x08\x07\x10\x1f\x11\x1e\x13\x1c\x13\x1c\x0b\x02\x0e\x02'),
                            bytearray(b'\xc2\x00\x02\x02pp\xfe\xfe\xff\xff\x03\x03\xfd\xfc\x83\x01\x02\xfc\x02\xfdp\x8f\xfe\x01\xff\x00\xff\x00\xfd\x02@>'),
                            bytearray(b'\x00\x00\x00\x00\x80\x00\x80\x00@\x00\xf0\x10\xf0\xd0\xd8\x88\x00\x00\x00\x00\x80\x00\x00\x80\x00\xc0\x90p\x100H8'),
                            bytearray(b'\x03\x00\x13\x03\x17\x07\x0f\x07\x1b\x00>\x034\t\x1f&\x03\x0c\x13\x0c\x17\x08\x0f\x00\x04\x03\x1c\x18\x0e\x083>'),
                            bytearray(b'\x03\xc0OL\x85\x87\xf1\xce\xfb8<\xd93\xccC<\x078\xfd\x02\xf0\x08\xc11\x07\xc1?\x197\x07\xc77'),
                            bytearray(b'\xd8\x80\x98\x008\x08\xf0\x00p\xb0\x00\x80\x00\x80\x80\x00@8\x80x\x08\xf8\x08\xf8\xb8\xf8\xf8\xf8\xf8\xf8\xf8x'),
                            bytearray(b'\x0e\x026"\x0e\n\x1e\x1a\x00\x00\x00\x00\x00\x00\x00\x009\x07\x1b\x07\x13\x07\x02\x06\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'3<\r\x0e\x07\x06\x05\x05\x05\x01\x0f\x00\x0f\x07\x07\x07\xc7\xff\xf7\xff\x1f\x1e\n\x08\x06\x00\x0f\x00\x08\x00\x00\x00'),
                            bytearray(b'\xe8\xe8\xc8\xc8\xd8\x18\xd0P\xe0`\xc0@\x80\x80\x00\x00\xf8\xf8\xf8\xf88\xf8\xf0p\xe0`@\xc0\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
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
    palette_id=SPAL797_MARIO_DOLL_UNAFFECTED_BY_MAIN_CHARACTER_PALETTE,
    palette_offset=0,
    unknown_num=0
)
