# SPR0580_SMALL_MARIO_HURLY_GLOVES

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL634_MARIO_DOLL_SURPRISED
sprite = CompleteSprite(
    animation=AnimationPack(246, length=157, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x00\x03\x06\x04\x16%%\x12\x13\x11\x00\x00\x00\x00\x01\x00\x03\x00\x07\x02"#\x10\x1d\x15\x0b\x1e\x19'),
                            bytearray(b'\x00\x00\xc0\xc0\x90p\x90\xf0\xf0p\xd0D\x14\x08\xd4\x08\x00\x00\xc0\x00\xb0\x80p\x000\x08\x84\xbc\xc8(\x88h'),
                            bytearray(b'\x00\x00\x00\x03Q\x06|\x0f\x7f\x0f|\x0c00\x00\x00\x0e\r\x00\x04a\x16p\x0fL?o\x1f11\x00\x00'),
                            bytearray(b'x\xb0\xc0\x80@\x80\xc0\x00 \x00\xa0\x00 \x00\xc0\xc00H\x00\xe0 \xe0\xe0 \xe0\x00\xe0\x00\xc0 \xc0\xc0'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                ),
                Mold(1, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x04\x00\x01\x01\x01\x02&\x07\x06\x04\x0e\x15\x15\n\x0b\t\x00\x00\x01\x00\x03\x01\x06\x00\x07\x02\x12\x13\x08\r\r\x03'),
                            bytearray(b'\x00\x00\x80\x80$\xe0\x90\xf0 \xe0\xc0@\xe0H(\x10\x00\x00\x80\x00`\x00p\x00\xe0\x10\x000\x88\xb8\xd0\x10'),
                            bytearray(b'\x00\x03(\x049\x06<\x06?\x06\x1c\x1c\x01\x01\x00\x00\x08\x0c0\x0f9\x06!\x1e7\x0e\x1f\x1e\x01\x01\x00\x00'),
                            bytearray(b'\xe8\x10\xd0\x80\xc0\x00@\x00@\x00@\x00\x80\x80\x00\x00\x90P\x00\xf0\xa0`\xe0 \xe0 \x80@\x80\x80\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=120, y=120),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=8, mold_id=0),
                        AnimationSequenceFrame(duration=8, mold_id=1),
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL634_MARIO_DOLL_SURPRISED,
    palette_offset=0,
    unknown_num=0
)
