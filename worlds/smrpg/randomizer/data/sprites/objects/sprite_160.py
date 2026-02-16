# SPR0160_SHELLY_BOTTOM_SECTION

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL543_SHELLY_BOTTOM_SECTION
sprite = CompleteSprite(
    animation=AnimationPack(401, length=42, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x10\x00\xf8@\xfd\x00\xff\x00\xff\x00\xff\x00\xfe\x01\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x00\x00\xc0\x00\xfc'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x01\x00\x01\x00\x02\x01\x0e\x01\x0e\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'@C\x00g\x10w\x10\xff0\xff\x00\xff\x01\xffo\xff@\x03\x00\x07\x10\x07\x10\x0f0\x0f\x00?\x01~o\x10'),
                            bytearray(b'\x1c\x03|c\xf8\x07\xf0\x0f\xe1\x1f\xc3?\x03\xff\x07\xff\x00\x00`\x00\x00\x00\x00\x00\x01\x00\x03\x00\x03\x00\x07\x00'),
                            bytearray(b'\x7f\xff\x7f\xff\xff\xff\xff\xff\xff\xfe\xfc\xfd\xea\xff\xf1\xfc\x7f\x00\x7f\x00\xff\x00\xff\x00\xff\x01\xfb\x04\xe0\x14\x87\x08'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=116),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\xc0\x00\xe0\x00\xe0\x00\xf0\x00\xf9\x00\xff\x00\xff\x00\xff\x00\x00\x00\x00 \x00 \x00\xf0\x00\xf8\x00\xff\x00\xff\x00\xff'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x80\x80\x80\x00\xe0\x00\xe0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\x00\x00\x00\x00\xe0\x00\xc0'),
                            bytearray(b'\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\x7f\x80\x00\xff\x00\xfe\x00\xff\x00\xfe\x00|\x00\x18\x00\x00\x00\x00'),
                            bytearray(b'\xf8\x08\xfe\x12\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\x08\xc0\x12\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=108, y=116),
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
    palette_id=SPAL543_SHELLY_BOTTOM_SECTION,
    palette_offset=0,
    unknown_num=0
)
