# SPR0550_BOLT_HARDWARE_WISE

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL413_BOLT_HARDWARE_WISE
sprite = CompleteSprite(
    animation=AnimationPack(238, length=52, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=4, subtile_bytes=[
                            bytearray(b'\x18\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00<|\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'),
                            None,
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=124, y=140),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x80~\x80|\x80p\x80@\x00\x80\x00\x80\x00\x80\x00\x80\xfe\xfe\xfc\xfc\xf0\xf0\xc0\xc0\x80\x80\x80\x80\x80\x80\x80\x80'),
                            None,
                            bytearray(b'\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x80\x00\x00\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x80\x00\x00'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=124),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'|8<\x08\x0c\x00\x00\x00\x02\x02\x03\x02\x01\x00\x00\x01E\x835C-3\t\x0f\x00\x01\x01\x00\x01\x02\x00\x03'),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\xa0\x9fPO\xd8G\xecc\xff\xff\xff\xff\xff\xff\xff\xff\x7f\xff?\xff\xbf\x7f\x9f\x7f'),
                            bytearray(b'\x03\x00\x01\x00\x01\x00\x00\x00\x01\x02\x01\x00\x01\x02\x00\x00\x03\x00\x01\x02\x01\x02\x00\x03\x01\x02\x01\x02\x01\x02\x00\x01'),
                            bytearray(b'XG\xacc\x98G\xeccXG\xecc\xd8G\xac#?\xff\x9f\x7f\xbf\x7f\x9f\x7f?\xff\x9f\x7f\xbf\x7f\x9f\x7f'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=124),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'\x00\x00\x80\x80\xe0\xe0\xf8\xf8\xfc\xfc\xfc\xfc\xfc\xfc\xfa\xf8\x00\x00@\xc0\x10\xf0\x04\xfc\x02\xfe\x02\xfe\x02\xfe\x06\xfe'),
                            None,
                            bytearray(b'\xea\xe4\xa2\x9c\x82|\x82|\x82|\x82|\x82|\x82|\x1e\xfe~\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe\xfe'),
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=132, y=108),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x03\x03\x0f\x0f??\x7f\x7f\xff\xff\xff\xff?\x7f\x01\x01\x04\x07\x10\x1f@\x7f\x80\xff\x00\xff\x00\xff\x00\xff'),
                            bytearray(b'\xfe\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff\x00\xff'),
                            bytearray(b'\x9f?\xe7\xcf\xf8\xf2\xfc\xf8\xfc\xf8\xfc\xf8\xfc\xf8\xfc\xf8\x80\x7f \x1f\t\x07\x05\x03\x05\x03\x05\x03\x05\x03\x05\x03'),
                            bytearray(b'\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xff\x00\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=116, y=108),
                    ]
                ),
            ],
            sequences=[
                AnimationSequence(
                    frames=[
                        AnimationSequenceFrame(duration=16, mold_id=0),
                    ]
                ),
            ]
        )
    ),
    palette_id=SPAL413_BOLT_HARDWARE_WISE,
    palette_offset=0,
    unknown_num=8
)
