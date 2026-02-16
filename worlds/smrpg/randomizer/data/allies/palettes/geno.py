from .types import GenoPalette
from randomizer.types.flags import GenoPaletteOptions


class GenoDefault(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF0D860,
        0xC08030,
        0x804818,
        0x402810,
        0x00C0F8,
        0x0090E0,
        0x0070D0,
        0x004878,
        0xF8C000,
        0xF85000,
        0x682018,
        0xB0A090,
        0x686070,
        0x181818,
    ]
    classic_colours = [
        0x804818,
        0x0090E0,
        0xF0D860,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
        0x000000,
    ]
    overworld_map_colours = [
        0xF8F8F8,
        0xF0D860,
        0xC08030,
        0x804818,
        0x402810,
        0x00C0F8,
        0x0090E0,
        0x0070D0,
        0x004878,
        0xF8C000,
        0xF85000,
        0x682018,
        0xB0A090,
        0x686070,
        0x181818,
    ]


# geno palettes
class GenoPink(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF8E8B0,
        0xE09870,
        0x985010,
        0x502818,
        0xF898F8,
        0xE848B0,
        0xB02080,
        0x700000,
        0xF8D038,
        0xF88820,
        0x603000,
        0xD0C8C8,
        0x786860,
        0x181818,
    ]
    poison_colours = [
        0xF8F8F8,
        0xF8E8B0,
        0xA8A8D8,
        0x986030,
        0x502828,
        0xF8A8F8,
        0xA878C8,
        0x704890,
        0x581820,
        0xE0D028,
        0xB0A018,
        0x603000,
        0xC8C8C8,
        0x888888,
        0x181818,
    ]
    underwater_colours = [
        0xB0B0D0,
        0xB0A8A0,
        0xA07070,
        0x704030,
        0x402828,
        0xB050D0,
        0xA830A0,
        0x802080,
        0x581028,
        0xB09850,
        0xB06840,
        0x301832,
        0x9890B0,
        0x605068,
        0x181818,
    ]
    id = GenoPaletteOptions.PINK
    name = "Millnium"
    author = "PIDGEZERO_ONE"


class GenoMagikoopa(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF0D860,
        0xF8B000,
        0xB06028,
        0x481000,
        0x3008F8,
        0x1800B0,
        0x080068,
        0x300040,
        0x007800,
        0xF8F800,
        0x602000,
        0x000000,
        0x686070,
        0x181818,
    ]
    poison_colours = [
        0xF8F8F8,
        0xE0A0A8,
        0xE05878,
        0xA84868,
        0x400820,
        0x8008F8,
        0x5800B0,
        0x300068,
        0x300040,
        0x304038,
        0xE08078,
        0x581030,
        0x000000,
        0x686070,
        0x181818,
    ]
    underwater_colours = [
        0x7878B0,
        0x786860,
        0x785830,
        0x583048,
        0x200830,
        0x180050,
        0x080088,
        0x000068,
        0x180050,
        0x003830,
        0x787830,
        0x301030,
        0x000030,
        0x303068,
        0x080840,
    ]
    id = GenoPaletteOptions.MAGIKOOPA
    name = "Magikoopa"
    author = "AARONDOBBE"


class GenoMagikoopaRed(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF0D860,
        0xC08030,
        0x804818,
        0x402810,
        0xB80000,
        0xA80000,
        0x880000,
        0x800000,
        0xF8C000,
        0xF85000,
        0x682018,
        0xB0A090,
        0x686070,
        0x181818,
    ]
    poison_colours = [
        0xA8F8F8,
        0xA0E070,
        0x808028,
        0x503800,
        0x181800,
        0x700000,
        0x680000,
        0x500000,
        0x500000,
        0xA8C800,
        0xA84800,
        0x301000,
        0x70A0C0,
        0x305890,
        0x000000,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x786C61,
        0x604049,
        0x40243D,
        0x201439,
        0x5C0031,
        0x540031,
        0x440031,
        0x400031,
        0x7C6031,
        0x7C2831,
        0x341C3D,
        0x585079,
        0x343069,
        0x0C0C3D,
    ]
    id = GenoPaletteOptions.MAGIKOOPARED
    name = "Magikoopa"
    author = "EGGTALK"


class GenoLink(GenoPalette):
    colours = [
        0xF8F8F8,
        0xf0a068,
        0xb86820,
        0x8E3D3D,
        0x402810,
        0x78B820,
        0x509010,
        0x38650B,
        0x274707,
        0xf87800,
        0xE860B0,
        0x682018,
        0xB0A090,
        0x686070,
        0x181818,
    ]
    poison_colours = [
        0xF8C0F8,
        0xF870D0,
        0xC84828,
        0x902070,
        0x300000,
        0x708828,
        0x486000,
        0x284800,
        0x182000,
        0xF85000,
        0xF838F8,
        0x600018,
        0xC070F8,
        0x6038E0,
        0x000018,
    ]
    underwater_colours = [
        0x7c7cad,
        0x785065,
        0x5c3442,
        0x482052,
        0x20143a,
        0x3c5c42,
        0x28483a,
        0x1c3436,
        0x142436,
        0x7c3c32,
        0x743089,
        0x34103e,
        0x585079,
        0x343069,
        0x0c0c3e,
    ]
    id = GenoPaletteOptions.LINK
    name = "Zelda"
    author = "PIDGEZERO_ONE"


class GenoVlador(GenoPalette):
    colours = [
        0xF8E0E0,
        0xB0B0B0,
        0x808080,
        0x606060,
        0x202018,
        0xB01818,
        0x800000,
        0x680000,
        0x200000,
        0xD0C8D0,
        0xD0C8D0,
        0x383838,
        0xB0A090,
        0x686868,
        0x181818,
    ]
    poison_colours = [
        0xE8A8F8,
        0xA088F8,
        0x7060E8,
        0x5848A8,
        0x181020,
        0xA01020,
        0x700000,
        0x600000,
        0x180000,
        0xC098F8,
        0x9068F8,
        0x302060,
        0xA070F8,
        0x6048C0,
        0x101020,
    ]
    underwater_colours = [
        0x7C70A1,
        0x585889,
        0x404071,
        0x303062,
        0x10103E,
        0x580C3E,
        0x400032,
        0x340032,
        0x100032,
        0x686499,
        0x4C487D,
        0x1C1C4E,
        0x585079,
        0x343465,
        0x0C0C3E,
    ]
    id = GenoPaletteOptions.VLADOR
    name = "Vlador"
    author = "HERRSHAUN"


class GenoLight(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF0D8D8,
        0xC08030,
        0x804818,
        0x402810,
        0x00C0C0,
        0x009090,
        0x007070,
        0x004848,
        0xF8C0C0,
        0xF85050,
        0x682020,
        0xA06838,
        0x686060,
        0x181818,
    ]
    poison_colours = [
        0xD8A0F8,
        0xD090E8,
        0xA85038,
        0x703020,
        0x382018,
        0x0880D0,
        0x0858A0,
        0x084880,
        0x083050,
        0xD880D0,
        0xD83858,
        0x581828,
        0x904040,
        0x584068,
        0x181020,
    ]
    underwater_colours = [
        0x8989b4,
        0x8579a4,
        0x6d4d50,
        0x4d3144,
        0x2d2140,
        0x0d6d98,
        0x0d5580,
        0x0d4570,
        0x0d315c,
        0x896d98,
        0x893560,
        0x411d48,
        0x5d4154,
        0x413d68,
        0x191944,
    ]
    id = GenoPaletteOptions.LIGHT
    name = "Light"
    rename_character = False
    author = "DEVILING"


class GenoPurple(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF8E8B0,
        0xE09870,
        0x985010,
        0x502818,
        0xA848F8,
        0x8828D8,
        0x6818B8,
        0x481878,
        0xC08870,
        0xF87800,
        0x603000,
        0x908888,
        0x686060,
        0x181818,
    ]
    poison_colours = [
        0xA8F8F8,
        0xA8F0F0,
        0x989890,
        0x604800,
        0x201808,
        0x6840F8,
        0x5018F8,
        0x3008F8,
        0x200898,
        0x808890,
        0xA87000,
        0x302000,
        0x5888B0,
        0x305870,
        0x000808,
    ]
    underwater_colours = [
        0x8989b4,
        0x898190,
        0x7d5970,
        0x593540,
        0x352144,
        0x6131b4,
        0x5121a4,
        0x411994,
        0x311974,
        0x6d5170,
        0x894938,
        0x3d2538,
        0x55517c,
        0x413d68,
        0x191944,
    ]
    id = GenoPaletteOptions.PURPLE
    name = "Purple"
    rename_character = False
    author = "DEVILING"


class GenoGrey(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF0D860,
        0xC08030,
        0x804818,
        0x402810,
        0xA8B8B8,
        0x98A8A8,
        0x809090,
        0x606868,
        0xF8C000,
        0xF85000,
        0x682018,
        0xB0A090,
        0x686070,
        0x181818,
    ]
    poison_colours = [
        0xA878F8,
        0xA07058,
        0x804020,
        0x501800,
        0x180800,
        0x6860C0,
        0x6050A8,
        0x504890,
        0x303060,
        0xA86000,
        0xA82000,
        0x300800,
        0x705090,
        0x302868,
        0x000000,
    ]
    underwater_colours = [
        0x7c7cad,
        0x786c61,
        0x604049,
        0x40243d,
        0x201439,
        0x545c8d,
        0x4c5485,
        0x404879,
        0x303465,
        0x7c6031,
        0x7c2831,
        0x34103d,
        0x585079,
        0x343069,
        0x0c0c3d,
    ]
    id = GenoPaletteOptions.GREY
    name = "Grey"
    rename_character = False
    author = "SMBAI"


class GenoGreen(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF0D860,
        0xC08030,
        0x804818,
        0x402810,
        0x68F850,
        0x00A800,
        0x004800,
        0x004000,
        0xF8C000,
        0xF85000,
        0x682018,
        0xB0A090,
        0x686070,
        0x181818,
    ]
    poison_colours = [
        0xA878F8,
        0xA07058,
        0x804020,
        0x501800,
        0x180800,
        0x507820,
        0x305818,
        0x405020,
        0x001800,
        0xA86000,
        0xA82000,
        0x300800,
        0x705090,
        0x302868,
        0x000000,
    ]
    underwater_colours = [
        0x7c7cad,
        0x786c61,
        0x604049,
        0x40243d,
        0x201439,
        0x145042,
        0x0c3c3e,
        0x103842,
        0x05261E,
        0x7c6031,
        0x7c2831,
        0x34103d,
        0x585079,
        0x343069,
        0x0c0c3d,
    ]
    id = GenoPaletteOptions.GREEN
    name = "Green"
    rename_character = False
    author = "MINAMIYO"




class GenoDark(GenoPalette):
    colours = [
        0xF8F8F8,
        0xF8E8B0,
        0xE09870,
        0x985010,
        0x181818,
        0x284050,
        0x203040,
        0x182028,
        0x000000,
        0xF8D038,
        0xF88820,
        0x383838,
        0xD0C8C8,
        0x786860,
        0x181818,
    ]
    poison_colours = [
        0xA8F8F8,
        0xA8F8B0,
        0x989868,
        0x604800,
        0x000000,
        0x003048,
        0x002030,
        0x001018,
        0x380000,
        0xA8D828,
        0xA88810,
        0x102850,
        0x88D0D0,
        0x486058,
        0x000000,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C7489,
        0x704C69,
        0x4C2839,
        0x0C0C3D,
        0x142059,
        0x101851,
        0x0C1045,
        0x380031,
        0x7C684D,
        0x7C4441,
        0x1C1C99,
        0x686495,
        0x3C3461,
        0x0C0C3D,
    ]
    id = GenoPaletteOptions.DARK
    name = "Dark"
    rename_character = False
    author = "SMBAI"


all_palettes: list[GenoPalette] = [
    GenoDefault(),
    GenoPink(),
    GenoMagikoopa(),
    GenoMagikoopaRed(),
    GenoLink(),
    GenoVlador(),
    GenoLight(),
    GenoPurple(),
    GenoGrey(),
    GenoGreen(),
    GenoDark(),
]
