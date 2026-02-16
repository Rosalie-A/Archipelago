# SPR0605_BIG_FLOWER

from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.data.variables.sprite_palette_names import SPAL008_MIMIC_FACE_STANDALONE
sprite = CompleteSprite(
    animation=AnimationPack(327, length=34, unknown=0x0002,
        properties=AnimationPackProperties(vram_size=2048,
            molds=[
                Mold(0, gridplane=True,
                    tiles=[
                        Tile(mirror=False, invert=False, format=0, length=10, subtile_bytes=[
                            bytearray(b'\x00\x00\x01\x01\x02\x03\x04\x07\t\x0eb|\x02x\x82\xf8\x00\x00\x01\x00\x03\x04\x1f\x18\x0e1|\x03x\x87\xf8\x07'),
                            bytearray(b'\x00\x00\xfc\xfc?\xe1\x81\x00\x0e\x0e??\xff\x7f\x9c\x1c\x00~\xfc\x03\xe1\x1e\x00\xff\x00\xff\x00\xff\x80\x7f\x80\x7f'),
                            bytearray(b"\x00\x00\x00\x00\xe0\xc0xx\x888v>.NG\x07\x00\x00\x00\x80\xd00x\x808\xc4>\xc0\x0e\xf1\'\xf8"),
                            bytearray(b'=\xc4:F9Gjw%\x06\x01\x01\x01\x01\x00\x00\xc4\x03F\x81G\x80w\x00\x068\x01\x06\x01\x01\x03\x03'),
                            bytearray(b'\xe0\x00\x1f`\x060c\xe3\xfc\x03|\x83f\xfe\xf3\xf3\x80\x1f\x1e\x81\x01\xcf\xe3\x1c\x03\x00\x83\x00\x7f\x81\xff\xff'),
                            bytearray(b'O\x01\x86\x18\x82<>\xfe\x04\xe0p\xc000\xc0\xc0!\xf0X\xe1<\xc1\xfe\x00\xe0\x1c\xc00\xf0\xf0\xc0\xc0'),
                            bytearray(b'\x07\x07\xc3;8F\x1c#3<\x03\x03\x00\x00\x00\x00\x7f\x7f\xff\xff\xff\xff\xff\xff??\x03\x03\x00\x00\x00\x00'),
                            bytearray(b'\xf3\xf3\xff\xff\xc7\xdfG_\x0f\x97\xcd\xd6LW<<\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\x7f\x7f??'),
                            bytearray(b'\x00\x00\xfe\xfe\xee\xf1\xbc\xc3q\x8f\x0e\xfe00\xc0\xc0\x00\x00\xff\xff\xff\xff\xff\xff\xff\xff\xfe\xfe\xf0\xf0\xc0\xc0'),
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
            ]
        )
    ),
    palette_id=SPAL008_MIMIC_FACE_STANDALONE,
    palette_offset=0,
    unknown_num=0
)
