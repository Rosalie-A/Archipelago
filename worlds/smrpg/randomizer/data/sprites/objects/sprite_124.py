# SPR0124_GAMEBOY_KID

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL500_GAMEBOY_KID
sprite = CompleteSprite(
    animation=AnimationPack(397, length=116, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x18\x7f@\xbf\xc0?\xc0?\xc0\x1f\xe0\x9f\xe0_`\x00\x1f\x00p\x00\xf0\x8ep\x9f`\x9f`\x1f\xe0\x9f\xe0'),
                            bytearray(b'\x80`\xf0\x08\xf8\x04\xfc\x02\xf8\x06\xf9\x07\xe7\x19\x0c\xf3\x00\xe0\x008\x00\x1c\x00\x0e\x00\x1e\x00\xff\x06\xf9\x0f\xf0'),
                            None,
                            bytearray(b".1,/    \x08\x18#/ p\x12[Nq0?\'?\x00\x1f\x00\x07\x10\x00\x17\x08/\x10"),
                            bytearray(b'\x18\xf70\xfep~\x80\x80\xc8\xc8\x90\x90\xd0\xd0 \xe0\x0f\xf0\x0e\xf0\x8e\xf0\xfc\xbc\xb8\x08p\x10\xf0\x00\xd0\x00'),
                            None,
                            bytearray(b'\x1f\x03/\rp`\xe0\xecbg~~\x03\x03\x01\x01 70?\x7f\x1f\xaf\x1fg\x9f~\x7f\x03\x02\x01\x01'),
                            bytearray(b'0p\xe0\xf0\x00p P0\xc0\xc0\xd0\xf0\xf0\xe0\xe0\x90\x000\x10\xf0\xf0\xf0\xf0\xf0\xf0\xd00p\x10\xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(1, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x18\x7f@\xbf\xc0?\xc0?\xc0\x1f\xe0\x9f\xe0_`\x00\x1f\x00p\x00\xf0\x8ep\x9f`\x9f`\x1f\xe0\x9f\xe0'),
                            bytearray(b'\x80`\xf0\x08\xf8\x04\xfc\x02\xf8\x06\xf9\x07\xe7\x19\x0c\xf3\x00\xe0\x008\x00\x1c\x00\x0e\x00\x1e\x00\xff\x06\xf9\x0f\xf0'),
                            None,
                            bytearray(b".1,/    \x08\x18#/@pR[Nq0?\'?\x00\x1f\x00\x07\x10\x00\x17\x08/\x10"),
                            bytearray(b'\x18\xf70\xfep~\x80\x80\xc8\xc8\x90\x90\xd0\xd0 \xe0\x0f\xf0\x0e\xf0\x8e\xf0\xfc\xbc\xb8\x08p\x10\xf0\x00\xd0\x00'),
                            None,
                            bytearray(b'\x1f\x03/\rp`\xe0\xecbg~~\x03\x03\x01\x01 70?\x7f\x1f\xaf\x1fg\x9f~\x7f\x03\x02\x01\x01'),
                            bytearray(b'0\xf0`p\x00p P0\xc0\xc0\xd0\xf0\xf0\xe0\xe0\x10\x00\xb0\x10\xf0\xf0\xf0\xf0\xf0\xf0\xd00p\x10\xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(2, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            None,
                            bytearray(b'\x07\x18\x7f@\xbf\xc0?\xc0?\xc0\x1f\xe0\x9f\xe0_`\x00\x1f\x00p\x00\xf0\x8ep\x9f`\x9f`\x1f\xe0\x9f\xe0'),
                            bytearray(b'\x80`\xf0\x08\xf8\x04\xfc\x02\xf8\x06\xf9\x07\xe7\x19\x0c\xf3\x00\xe0\x008\x00\x1c\x00\x0e\x00\x1e\x00\xff\x06\xf9\x0f\xf0'),
                            None,
                            bytearray(b".1,/    \x08\x18#o0p2\x0bNq0?\'?\x00\x1f\x00\x07\x10\x00\x07\x18\x078"),
                            bytearray(b'\x18\xf70\xfep~\x80\x80\xc8\xc8\x90\x90\xc0\xc0@\xc0\x0f\xf0\x0e\xf0\x8e\xf0\xfc\xbc\xb8\x08p\x10\xe0\x00\xa0\x00'),
                            None,
                            bytearray(b'\x1c\x116\x06ph\xe0\xeebg~~\x03\x03\x01\x01">9>~\x1f\xaf\x1fg\x9f~\x7f\x03\x02\x01\x01'),
                            bytearray(b'@\xc0\xa0\xb0\x00p Pp\x80\xc0\xd0\xf0\xf0\xe0\xe0 \x00p\x10\xf0\xf0\xf0\xf0\xf0\xf0\xd00p\x10\xe0 '),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
                Mold(3, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x03\x0c\x0f\x10\x1f \x7f@\x7f\x80\x7f\x80\x7f\x80?\xc0\x00\x0f\x00\x18\x000\x00`\xc0 \xc0 \xc00\xc0?'),
                            bytearray(b'\xc00\xf0\x0c\xfc\x02\xfe\x01\xfe\x01\xfe\x01\xfe\x01\xfe\x01\x00\xf0\x00\x1c\x00\x06\x00\x07\x00\x07\x00\x0f\x00\x1f\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x80\x80\x00\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x80\x00\x80\x00'),
                            bytearray(b"\x0fpOp/0\x00\x1f\x00\x0fP0Yy\x00\x01@?\x0fp_`? \x1f\x10\x08\'\x05C}B"),
                            bytearray(b'\xfc\x03q\x8f\x8ex|\xf3p\xff\x00\x0c\x000\xe0\x10\x00\xff\x00\xff\x87y\x8fp\x8fp|\xf08\xc0\xf0\x08'),
                            bytearray(b'\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'\x10\x13\x00\x0f\x0f\x00ghtt<<??\x00\x00#<\x1f\x10\x0f\x0fo\x1fT\x0f<C??\x00\x00'),
                            bytearray(b'\xe0\x18\xf0\x08\xe0\x18\x80xLL\xf8\xf8\x00\x00\x00\x00\xf8\x00\xf8\x00\xf8\xf8\xf8\xfcL\xf4\xf8\xf8\x00\x00\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=0, y=0),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                        AnimationSequenceFrame(duration=48, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=4, mold_id=0),
                        AnimationSequenceFrame(duration=4, mold_id=1),
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=2),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=2),
                        AnimationSequenceFrame(duration=32, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=6, mold_id=1),
                        AnimationSequenceFrame(duration=6, mold_id=0),
                        AnimationSequenceFrame(duration=10, mold_id=2),
                    ]
                ),
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=3),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL500_GAMEBOY_KID,
    palette_offset=0,
    unknown_num=0
)
