# SPR0249_RED_SHELL

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL370_RED_SHELL
sprite = CompleteSprite(
    animation=AnimationPack(213, length=176, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x80\x00@\x80P\x00\x88p\x88@\x00\xc00\x00\x00\x80@p\x80H\xa0\x80p\x84p<\xf0<\xf0'),
                            None,
                            bytearray(b'\xb080x`\xe8\xc0\xd8\x08\xf8\x10\xf0``\x80\x80t\xf0\xf4\xf0\xf0\xe8\xe0\xd0\x00x\x00\xd0\x80`\x00\x80'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=131, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x00\x00\x00\x03\x01\x02\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x00\x03\x03\x00\x03\x00'),
                            bytearray(b'\x00\x00\x10\x07\x11h<\xc0\x04\xfb\x88#t\x9ad\xb8\x00\x1f\x07xx\x86\xf8\x07\xfb\x04#\xdc\x8aE\x98G'),
                            bytearray(b'\x00\x03\x00\x07\x00\x01\x07\x07\x03\x03\x03\x03\x01\x01\x00\x00\x04\x03\x08\x07\x0e\x00\x00\x07\x03\x01\x01\x02\x00\x01\x00\x00'),
                            bytearray(b'\x80x@\xf8\x00\xf3\x01\xef\x00p\x80\xbf\xc0\xdf\x7fAz\x07;\x877\xcf\x1f_\x8f`@\xbf\xe0\x06>\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=115, y=124),
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
    palette_id=SPAL370_RED_SHELL,
    palette_offset=0,
    unknown_num=0
)
