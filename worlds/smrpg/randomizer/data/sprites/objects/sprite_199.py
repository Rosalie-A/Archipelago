# SPR0199_FRYING_PAN_PACKET

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL538_FRYING_PAN
sprite = CompleteSprite(
    animation=AnimationPack(392, length=154, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(3, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x01\t\x02C\x98\x1c\x000\xc0\xc0\x00\x00\x00\x00\x01\x01\x06\x00=\x00\xe7\x03\xfc\x0c00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=133),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x0f\x07\x1f\x19?*?O/_?_\x7f_\x07\x07\x1e\x1e>>||p7\xf0\xaf\xe0\xbf\xa0\xbf'),
                            bytearray(b'\x00\x00\x80\x80\xe0\xe0\xf8p\xfc\x18\xe8\x94\xe6\x98\xf2\xee\x00\x00`\xe0\x100\x00`\x00\x18\x02\x82\x00\x80\x01\xe1'),
                            bytearray(b'\x7f\x7f\x7f\x7f\xdf\xff/\x1f\x07\x0f\x01\x03\x00\x00\x00\x00\x80\x8f\x80\xbf \x1f\xf0\xef\x18\x11\x0f\r\x03\x03\x00\x00'),
                            bytearray(b'\xf2\xee\xfe\xf2\xfe\xfa\xfc\xf8\xf8\xf8\x90\xf0\x00\x00\x00\x00\x01\xe3\x01\xf3\x01\xf9\x02\xfa\x04\xf4\xf8\x98\xe0\xe0\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=125),
                    ]
                )
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=2, mold_id=0)
                    ]
                )
            ]
        )
    ),
    palette_id=SPAL538_FRYING_PAN,
    palette_offset=0,
    unknown_num=0
)
