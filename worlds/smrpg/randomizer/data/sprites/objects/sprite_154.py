# SPR0154_GUNYOLK_OUTER_SECTION

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL602_GUNYOLK_TOP_SECTION
sprite = CompleteSprite(
    animation=AnimationPack(161, length=56, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=False,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=6, subtile_bytes=[
                            None,
                            bytearray(b'\x00\x00\x06\x02\x0f\x03\x0e\x0b\x0c\x17;?6>\x18x\x00\x00\x06\x06\x0f\x0f\x0f\x07\x0f\x1f\x0f?\x1e>xx'),
                            bytearray(b'\x00\x00\x00\x03\x07\x05\x0b\x07\x0e\x0b\x0f\x0b\x02\x0f\x02\x06\x00\x00\x03\x03\x07\x03\x0f\x0b\x07\x0f\x07\x0f\x0f\x0f\x06\x06'),
                            bytearray(b' \xf0`\xe0\xc0\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00\xf0\xf0\xe0\xe0\xc0\xc0\x80\x80\x80\x80\x00\x00\x00\x00\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=148, y=112),
                        Tile(mirror=False, invert=False, format=0, length=5, subtile_bytes=[
                            bytearray(b'=A1M<Ey\x07y\x07|\x03\x01\x7f\x00\x00\x03\x00\x05\x02\x05\x02\x03\x00\x01\x00\x01\x00\x03\x00\x00\x00'),
                            bytearray(b'{\xfd\x9b\xff\x80\xdd\x03sI\x7f3m\xff\xff\x00\x00\xce?\xfe\x01\xff\x00\xfe\x01y\x87\x1e\xff\xff\x00\x00\x00'),
                            None,
                            None,
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=117),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x03\x00\x02\x05\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01\x01\x02\x01\x00\x00\x00'),
                            bytearray(b'\x05\n%/Of7\xbd\x04\x17\x04\xf5\x80\xcb\x80D\x07\x0f\x00?i\x1f\xf2\x0f\xe0\x0f\xd4\x0b\xe8\x178\x03'),
                            bytearray(b'\x10\x1d\t\x17.0\x1f \x1f\x00?\x00?\x00>\x00\x0e\x10\x13\x00\x01 \x00  \x00\x00\x00\x00@A\x00'),
                            bytearray(b'\xc0& Z\x97\xa7F\xe7\xa3c\x8dn\xb4w\x97\x9a\x1a\x01\x8e\x01\xcf\x00\x7f\x00<\x03/\x13\x7f\x03\x97o'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=117, y=101),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b'\x00\x00\t\t\x124\x00Nt\xfe\x82|\xf3\x1d\xe4\x87\x00\x00\n\x159\x00\x7f\x00\x11n>\x7f\x0f\x1f\x94\x08'),
                            bytearray(b'\x00\x00\x00\x00` `\x00@\xb0l\xb4,\xe8~\xfb\x00\x00\x00\x00\xc0`\xe0`\xf0`\xc8|\xcc\xfc~\xfd'),
                            bytearray(b'~\x01\n\x17\x1b\x07\x08\x07\x03\x01\x00\x00\x00\x00\x00\x00\x00\x00#\x01\x1f\x1f\x0f\x0f\x03\x03\x00\x00\x00\x00\x00\x00'),
                            bytearray(b'M\xff\xc4\xfbX\xf7 \xff\xc0\xff\xc0\x7f\x00<\x00\x00\xfb\xfe\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff<<\x00\x00'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=111, y=98),
                        Tile(mirror=False, invert=False, format=0, length=7, subtile_bytes=[
                            bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x01\x0f\x07\x03\'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x03\x08\x0f\x1c\x03"),
                            bytearray(b'\x00\x00\x00\x00\x00\x00\x0b\x07o\x1e\xff<\x9f`o\x93\x00\x00\x00\x00\x00\x00\x08\x0fq\x7f\xc3\xff\x9f\xff\x7f\xff'),
                            bytearray(b'\xc1\xff\xbd\xaf\xed\xbd\x9a\x06N/v\x08=\x02\x06/`\x81\xf7\x18\xdb|\\?\x06\x19\x00\x01\x01\x01\r3'),
                            bytearray(b'\xdf\xef~\xbe|\xfcX\xf8P\xf0 \xe0@\x80\x80\x00?\xff\xfe\xfe\xfc\xfc\xf8\xf8\xf0\xf0\xe0\xe0\xc0\xc0\x80\x80'),
                        ], is_16bit=False, y_plus=0, y_minus=0, x=107, y=109),
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
    palette_id=SPAL602_GUNYOLK_TOP_SECTION,
    palette_offset=0,
    unknown_num=0
)
