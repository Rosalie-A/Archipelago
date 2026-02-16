from .types import MarioPalette
from randomizer.types.flags import MarioPaletteOptions


# mario palettes
class MarioDefault(MarioPalette):
    pass


class MarioJumpman(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C880,
        0xC08848,
        0xA86848,
        0x783830,
        0x3838E0,
        0x0000D8,
        0x101090,
        0x600000,
        0xB83838,
        0xA00000,
        0x581818,
        0xD8D8E0,
        0x888898,
        0x181818,
    ]
    poison_colours = [
        0xA8A8F8,
        0xA888A8,
        0x805050,
        0x683050,
        0x400828,
        0x0808F8,
        0x0000F8,
        0x0000C0,
        0x300000,
        0x700838,
        0x600000,
        0x280000,
        0x9090F8,
        0x5050D0,
        0x000000,
    ]
    underwater_colours = [
        0x8989B4,
        0x897178,
        0x6D515C,
        0x61415C,
        0x492950,
        0x2929A8,
        0x0D0DA4,
        0x151580,
        0x3D0D38,
        0x692954,
        0x5D0D38,
        0x391944,
        0x7979A8,
        0x515184,
        0x191944,
    ]
    id = MarioPaletteOptions.JUMPMAN
    name = "Jumpman"
    author = "DEVILING"


class MarioFireMario(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8D0A0,
        0xC09868,
        0xA87858,
        0x785030,
        0xF0F0F0,
        0xD0D0D0,
        0x989898,
        0x484848,
        0xD03838,
        0xA00000,
        0x680000,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8C0F8,
        0xF898F8,
        0xD870C0,
        0xC058A0,
        0x883050,
        0xF8B0F8,
        0xE898F8,
        0xA870F8,
        0x503080,
        0xE82060,
        0xB00000,
        0x700000,
        0xF8A0F8,
        0xA860F8,
        0x181020,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C6881,
        0x604C65,
        0x543C5E,
        0x3C284A,
        0x7878A9,
        0x686899,
        0x4C4C7D,
        0x242456,
        0x681C4E,
        0x500032,
        0x340032,
        0x706C9D,
        0x4C4475,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.FIREMARIO
    name = "Fire Mario"
    author = "HERRSHAUN"


class MarioLuigi(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C880,
        0xC08848,
        0xA86848,
        0x783830,
        0x68F850,
        0x00A800,
        0x004800,
        0x001000,
        0x3838E0,
        0x0000D8,
        0x000060,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8B8F8,
        0xF89880,
        0xF86848,
        0xF85048,
        0x701810,
        0x507820,
        0x305818,
        0x405020,
        0x200000,
        0x7028E0,
        0x0000D8,
        0x000060,
        0xF8A0D8,
        0xF86888,
        0x101808,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C6471,
        0x604456,
        0x543456,
        0x1C143A,
        0x145042,
        0x0C3C3E,
        0x103842,
        0x080432,
        0x1C1CA1,
        0x00009D,
        0x000062,
        0x706C9D,
        0x4C4475,
        0x080C36,
    ]
    id = MarioPaletteOptions.LUIGI
    name = "Luigi"
    author = "SMRPG ARMAGEDDON"


class MarioFireLuigi(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C880,
        0xC08848,
        0xA86848,
        0x783830,
        0xF8F8F8,
        0xE8E8E8,
        0xB8B8B8,
        0x600000,
        0x389830,
        0x388838,
        0x207820,
        0xD8D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xA8A8F8,
        0xA888A8,
        0x805050,
        0x683050,
        0x481028,
        0xA8A8F8,
        0x9898F8,
        0x7070F8,
        0x300000,
        0x106028,
        0x105038,
        0x004818,
        0x9090F8,
        0x6050B0,
        0x000000,
    ]
    underwater_colours = [
        0x8989B4,
        0x897178,
        0x6D515C,
        0x61415C,
        0x492950,
        0x8989B4,
        0x8181AC,
        0x696994,
        0x3D0D38,
        0x295950,
        0x295154,
        0x1D4948,
        0x7979A4,
        0x59517C,
        0x191944,
    ]
    id = MarioPaletteOptions.FIRELUIGI
    name = "Fire Luigi"
    author = "DEVILING"


class MarioWario(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF0B8A8,
        0xC08870,
        0xA86860,
        0x783830,
        0xF8D848,
        0xD0B020,
        0xA88010,
        0x604800,
        0x9038B0,
        0x780090,
        0x480060,
        0xF0E8D8,
        0x989078,
        0x181818,
    ]
    poison_colours = [
        0xF8C0F8,
        0xF888F8,
        0xD860C8,
        0xC048A8,
        0x882050,
        0xF8A080,
        0xE88830,
        0xC06018,
        0x683000,
        0xA020F8,
        0x8800F8,
        0x5000A8,
        0xF8A8F8,
        0xA868D8,
        0x181020,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x785C85,
        0x604469,
        0x543462,
        0x3C1C4A,
        0x7C6C56,
        0x685842,
        0x54403A,
        0x302432,
        0x481C89,
        0x3C0079,
        0x240062,
        0x78749D,
        0x4C486D,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.WARIO
    name = "Wario"
    author = "HERRSHAUN"


class MarioWaluigi(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8D090,
        0xC89058,
        0xB07058,
        0x783830,
        0x9040E0,
        0x6818C0,
        0x380888,
        0x100060,
        0x505050,
        0x383840,
        0x000000,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8A8F8,
        0xF888E8,
        0xC86090,
        0xB04890,
        0x782048,
        0x9028F8,
        0x6810F8,
        0x6810F8,
        0x100098,
        0x503080,
        0x382068,
        0x000000,
        0xE090F8,
        0x9858D8,
        0x181020,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C6879,
        0x64485E,
        0x58385E,
        0x3C1C4A,
        0x4820A1,
        0x340C91,
        0x340C91,
        0x080060,
        0x28285A,
        0x1C1C52,
        0x000032,
        0x706C9D,
        0x4C4475,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.WALUIGI
    name = "Waluigi"
    author = "HERRSHAUN"


class MarioBuilder(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C880,
        0xC08848,
        0xA86848,
        0x783830,
        0xC89030,
        0xB07820,
        0xA06820,
        0x885820,
        0xC85038,
        0x984030,
        0x702820,
        0xE0D8D8,
        0x988888,
        0x201010,
    ]
    poison_colours = [
        0xF8F8F8,
        0xF0A8B8,
        0xB86880,
        0xA05878,
        0x703850,
        0xB86078,
        0xA85068,
        0xA04860,
        0x804050,
        0xC04880,
        0x903860,
        0x682848,
        0xE0D8D8,
        0x988890,
        0x201018,
    ]
    underwater_colours = [
        0x7878B0,
        0x786070,
        0x604058,
        0x503058,
        0x381848,
        0x604848,
        0x583840,
        0x503040,
        0x402840,
        0x602850,
        0x482048,
        0x381040,
        0x7068A0,
        0x484078,
        0x100838,
    ]
    id = MarioPaletteOptions.BUILDER
    name = "Builder"
    author = "AARONDOBBE"


class MarioMegaman(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C880,
        0xC08848,
        0xA86848,
        0x783830,
        0x18A0F8,
        0x1018F8,
        0x0018E0,
        0x000088,
        0x3838E0,
        0x0000D8,
        0x000060,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8F8F8,
        0xB870E0,
        0x8848C8,
        0x502858,
        0x783830,
        0x380838,
        0x501850,
        0x281858,
        0x9018B0,
        0x500058,
        0x280058,
        0x000028,
        0x9890D8,
        0x6858A0,
        0x181818,
    ]
    underwater_colours = [
        0xF8F8F8,
        0xB8D0F8,
        0x98B0F8,
        0x6870C8,
        0x000068,
        0x0050B0,
        0x0000A0,
        0x000060,
        0x000050,
        0x101080,
        0x000030,
        0x000028,
        0x4000A8,
        0x886088,
        0x181818,
    ]
    id = MarioPaletteOptions.MEGAMAN
    name = "Mega Mar"
    author = "MYOHMYKE"


class MarioGrey(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C880,
        0xC08848,
        0xA86848,
        0x783830,
        0xD0D0D0,
        0xB0B8B8,
        0x989898,
        0x600000,
        0x283848,
        0x203040,
        0x182830,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xA8A8F8,
        0xA888A8,
        0x805850,
        0x684050,
        0x481828,
        0x8890F8,
        0x7080F8,
        0x6068D0,
        0x300000,
        0x001850,
        0x001048,
        0x001028,
        0x9898F8,
        0x6058B0,
        0x000000,
    ]
    underwater_colours = [
        0x82829A,
        0x826A5E,
        0x664A42,
        0x5A3A42,
        0x422236,
        0x6E6E86,
        0x5E627A,
        0x52526A,
        0x36051E,
        0x1A2242,
        0x161E3E,
        0x121A36,
        0x76728A,
        0x524A62,
        0x12122A,
    ]
    id = MarioPaletteOptions.GREY
    name = "Grey"
    author = "SMBAI"
    rename_character = False


class MarioZombie(MarioPalette):
    colours = [
        0xE8E0B8,
        0x98A860,
        0x607048,
        0x484828,
        0x383830,
        0xA88050,
        0x886848,
        0x704000,
        0x602000,
        0x781818,
        0x600000,
        0x200000,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8A8F8,
        0xA880A8,
        0x685080,
        0x503048,
        0x382050,
        0xC06090,
        0x984880,
        0x802800,
        0x481000,
        0x881020,
        0x680000,
        0x200000,
        0xF8A0F8,
        0xA860F8,
        0x181020,
    ]
    underwater_colours = [
        0x74708D,
        0x4C5462,
        0x303856,
        0x242446,
        0x1C1C4A,
        0x54405A,
        0x443456,
        0x382032,
        0x201032,
        0x3C103E,
        0x300032,
        0x100032,
        0x706C9D,
        0x4C4475,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.ZOMBIE
    name = "Zombio"
    author = "HERRSHAUN"


class MarioSponge(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8C8A0,
        0xC09868,
        0xA86848,
        0x785848,
        0xE88038,
        0xC06000,
        0x984800,
        0x600000,
        0x505050,
        0x303030,
        0x000000,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8C0F8,
        0xF898F8,
        0xD870C0,
        0xC04880,
        0x883880,
        0xF86060,
        0xD84800,
        0xA83000,
        0x680000,
        0x583090,
        0x302050,
        0x000000,
        0xF8A0F8,
        0xA860F8,
        0x181020,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C6481,
        0x604C65,
        0x543456,
        0x3C2C56,
        0x74404E,
        0x603032,
        0x4C2432,
        0x300032,
        0x28285A,
        0x18184A,
        0x000032,
        0x706C9D,
        0x4C4475,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.SPONGE
    name = "Sponge"
    author = "HERRSHAUN"


class MarioPretzel(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8E0C8,
        0xB8A898,
        0xA88078,
        0x785848,
        0x905818,
        0x703800,
        0x402000,
        0x300000,
        0x505050,
        0x303030,
        0x000000,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF8C0F8,
        0xF8A8F8,
        0xD080F8,
        0xC060D8,
        0x883880,
        0xA03820,
        0x802000,
        0x481000,
        0x300000,
        0x583090,
        0x302050,
        0x000000,
        0xF8A0F8,
        0xA860F8,
        0x181020,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7C7095,
        0x5C547D,
        0x54406D,
        0x3C2C56,
        0x482C3E,
        0x381C32,
        0x201032,
        0x180032,
        0x28285A,
        0x18184A,
        0x000032,
        0x706C9D,
        0x4C4475,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.PRETZEL
    name = "Pretzel"
    author = "HERRSHAUN"


class MarioMarlon(MarioPalette):
    colours = [
        0xF8F8F8,
        0xA06830,
        0x805818,
        0x684018,
        0x402000,
        0xC03098,
        0xA03068,
        0x701048,
        0x480020,
        0x404058,
        0x303048,
        0x202038,
        0xE0D8D8,
        0x988888,
        0x181818,
    ]
    poison_colours = [
        0xF0A0F8,
        0x903850,
        0x683030,
        0x602020,
        0x300800,
        0xB810F8,
        0x9010B8,
        0x600080,
        0x380030,
        0x302098,
        0x281080,
        0x100858,
        0xD090F8,
        0x9058F0,
        0x080020,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x50344A,
        0x3C2842,
        0x34203E,
        0x201032,
        0x60187D,
        0x501865,
        0x380856,
        0x240042,
        0x20205E,
        0x181856,
        0x10104E,
        0x706C9D,
        0x4C4475,
        0x0C0C3E,
    ]
    id = MarioPaletteOptions.MARLON
    name = "Marlon"
    author = "HERRSHAUN"


class MarioGrandDad(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF0F0F0,
        0xB0B0B8,
        0x787878,
        0x2058F8,
        0xA80000,
        0x880000,
        0x600000,
        0x200000,
        0xE86830,
        0xC04018,
        0x780800,
        0x80B8D8,
        0x80A8D8,
        0x1818B8,
    ]
    poison_colours = [
        0xF8C0F8,
        0xF8B0F8,
        0xC888F8,
        0x8858D8,
        0x2038F8,
        0xC00000,
        0x980000,
        0x680000,
        0x200000,
        0xF84850,
        0xD82820,
        0x880000,
        0x9088F8,
        0x9080F8,
        0x1810F8,
    ]
    underwater_colours = [
        0x7C7CAD,
        0x7878A9,
        0x58588D,
        0x3C3C6D,
        0x102CAD,
        0x540032,
        0x440032,
        0x300032,
        0x100032,
        0x74344A,
        0x60203E,
        0x3C0432,
        0x405C9D,
        0x40549D,
        0x0C0C8D,
    ]
    id = MarioPaletteOptions.GRANDDAD
    name = "Grand Dad"
    author = "HERRSHAUN"


class MarioBlue2(MarioPalette):
    colours = [
        0xF8F8F8,
        0xF8D090,
        0xC89058,
        0x4868A8,
        0x303878,
        0x3840E8,
        0x0008F8,
        0x0008B0,
        0x000060,
        0x505050,
        0x383840,
        0x000000,
        0xD8D8E0,
        0x888898,
        0x181818,
    ]
    poison_colours = [
        0xF0F8F8,
        0xA0D0E0,
        0x58A8C0,
        0x6838B0,
        0x482878,
        0x8058C0,
        0x6838B8,
        0x482880,
        0x000060,
        0x083020,
        0x001008,
        0x000000,
        0x80D0B8,
        0x289068,
        0x181818,
    ]
    underwater_colours = [
        0xC0C0C0,
        0xC09858,
        0x905820,
        0x103070,
        0x000040,
        0x0008B0,
        0x0000C0,
        0x000078,
        0x000028,
        0x181818,
        0x000008,
        0x000000,
        0xA0A0A8,
        0x505060,
        0x000000,
    ]
    id = MarioPaletteOptions.BLUE2
    name = "Blue2"
    author = "SWINCH"
    rename_character = False


all_palettes: list[MarioPalette] = [
    MarioDefault(),
    MarioJumpman(),
    MarioFireMario(),
    MarioLuigi(),
    MarioFireLuigi(),
    MarioWario(),
    MarioWaluigi(),
    MarioBuilder(),
    MarioMegaman(),
    MarioGrey(),
    MarioZombie(),
    MarioSponge(),
    MarioPretzel(),
    MarioMarlon(),
    MarioGrandDad(),
    MarioBlue2(),
]
