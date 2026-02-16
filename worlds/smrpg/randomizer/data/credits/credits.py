from __future__ import annotations
import random
from typing import TYPE_CHECKING

from ...types.flags import (
    RandomTadpolePondSong, RandomSunkenShipPassword,
    MarioPaletteChoice, MallowPaletteChoice, GenoPaletteChoice,
    BowserPaletteChoice, ToadstoolPaletteChoice,
)

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


"""
IMPORTANT NOTES ABOUT MODIFYING:
* The fontset is only UPPER CASE A-Z, space and period. Everything else looks like a space.
* The font/color is dependant on the Y position. Dunno why.
* Credits space is very limited. If we run out of cards, can't add more cards, but could add more titles to those cards.
** Changing this might be hard.
** Dunno if the length is hard coded in the code, or if moving the string table would solve the space problem.
* Watch the whole credits! There's a chance it can freeze at the end or corrupt the firework screen if you do it wrong.

"""

EMPTY_STRING = "                                       "

END_CREDITS_DELAY_1 = 34
END_CREDITS_DELAY_2 = 40
BEGIN_TITLES_DELAY = 50
END_TITLES_DELAY = 40

FINAL_DELAY = 0xFF


def to_str(string):
    return (
        "".join([chr(i + ord("A") - 1) for i in string])
        .replace("\\", " ")
        .replace("[", ".")
    )


def inv_str(string: str) -> bytes:
    """Convert a credits string to ROM bytes.

    Format: length byte followed by encoded characters where A=1, B=2, etc.
    Special characters: space='\\', period='[', underscore=']'
    """
    string = string.replace(" ", "\\").replace(".", "[").replace("_", "]")
    length_byte = bytes([len(string)])
    char_bytes = bytes([ord(c) - ord("A") + 1 for c in string])
    return length_byte + char_bytes

# There's a way to do perfect allocations with DYNAMIC PROGRAMMING,
# but I'm not doing that.
def allocate_string(string_length: int, free_list: dict[int, int]) -> int | None:
    for base in sorted(free_list, key=lambda x: free_list[x]):
        if free_list[base] >= string_length:
            size = free_list[base]
            del free_list[base]
            free_list[base + string_length] = size - string_length
            return base
    # If we get this far, we couldn't find space for the string.
    return None


class Credits(object):
    def __init__(self, table_offset=0):
        self.strings = {}
        self.inv_strings = {}
        self.acc = []
        self.table_offset = table_offset
        self.current_credits = []
        self.current_titles = []

    def add(self, x, y, font, string, scroll=0):
        assert len(string) <= len(EMPTY_STRING)
        if string in self.inv_strings:
            dex = self.inv_strings[string]
        else:
            dex = len(self.strings) + self.table_offset
            self.strings[dex] = string
            self.inv_strings[string] = dex
        self.acc += [0xE3, 0x12, dex, x, y, font, scroll]

    def end_thing(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x0B,
            0x16,
            0x00,
            0x01,
            0x03,
            0x04,
            0x10,
            delay,
            0x01,
        ]

    def end_thing_2(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x16,
            0x0B,
            0x00,
            0x01,
            0x03,
            0x04,
            0x10,
            delay,
            0x00,
        ]

    def end_thing_3(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x16,
            0x0B,
            0x00,
            0x09,
            0x0B,
            0x04,
            0x10,
            delay,
            0x00,
        ]

    def end_thing_4(self, delay):
        self.acc += [
            0xE3,
            0x00,
            0x0F,
            0x02,
            0x0B,
            0x16,
            0x00,
            0x09,
            0x0B,
            0x04,
            0x10,
            delay,
            0x00,
        ]

    def clear(self, words):
        for x, y, font in words:
            self.add(x, y, font, EMPTY_STRING)
        del words[:]

    # Yeah, got into a OpenGL vibe here.
    def begin_credits(self):
        pass

    def add_credit(self, x, y, font, string, scroll=0):
        self.current_credits.append((x, y, font))
        self.add(x, y, font, string, scroll)  # 7

    def end_credits(self, delay_1, delay_2):  # 26
        self.end_thing(delay_1)
        self.end_thing_2(delay_2)
        self.clear(self.current_credits)

    def begin_titles(self, delay):
        self.end_thing_3(delay)  # 13
        self.clear(self.current_titles)  # 7

    def add_title(self, x, y, font, string, scroll=0):
        self.current_titles.append((x, y, font))
        self.add(x, y, font, string, scroll)  # 7

    def end_titles(self, delay):
        self.end_thing_4(delay)  # 13

    def empty_title(self):
        self.acc += [0xE3, 0, 0, 0, 0, 0, 0]

    def finalize(self) -> dict[int, bytearray]:
        # Return a patch next time...
        credit_start = 0x3FDBB0
        credit_len = 3380
        # print(len(self.acc))

        # empty_string = ' ' * (remaining_space // 3)
        # space_filler = []

        # while remaining_space >= 73:
        #     remaining_space -= 73
        #     space_filler.append((self.begin_titles, [BEGIN_TITLES_DELAY]))
        #     space_filler.append((self.add_title, [0x80, 0x00, 0x08, EMPTY_STRING]))
        #     space_filler.append((self.end_titles, [END_TITLES_DELAY]))
        #     space_filler.append((self.begin_credits, []))
        #     space_filler.append((self.add_credit, [0x80, 0x80, 0xc0, EMPTY_STRING]))
        #     space_filler.append((self.add_credit, [0x80, 0x40, 0x81, EMPTY_STRING]))
        #     space_filler.append((self.add_credit, [0x80, 0x00, 0xc2, EMPTY_STRING]))
        #     space_filler.append((self.end_credits, [END_CREDITS_DELAY_1, END_CREDITS_DELAY_2]))

        # for i, (cmd, args) in enumerate(space_filler):
        #     if i == len(space_filler) - 1 and cmd == self.add_credit:
        #         args[3] == empty_string
        #     cmd(*args)

        # fill remaining space with pointers to empty text
        # print("initial:", len(self.acc))
        if credit_len - len(self.acc) >= 101:
            self.begin_titles(BEGIN_TITLES_DELAY)
            self.add_title(0x80, 0x00, 0x08, " ")
            self.end_titles(END_TITLES_DELAY)
            self.begin_credits()
            self.add_credit(0x80, 0x80, 0xC0, " ")
            self.add_credit(0x80, 0x40, 0x81, " ")
            self.add_credit(0x80, 0x00, 0xC2, " ")
            self.end_credits(FINAL_DELAY, END_CREDITS_DELAY_2)
            # print("first:", len(self.acc))
        while credit_len - len(self.acc) >= 108:
            self.begin_titles(BEGIN_TITLES_DELAY)
            self.add_title(0x80, 0x00, 0x08, " ")
            self.end_titles(END_TITLES_DELAY)
            self.begin_credits()
            self.add_credit(0x80, 0x80, 0xC0, " ")
            self.add_credit(0x80, 0x40, 0x81, " ")
            self.add_credit(0x80, 0x00, 0xC2, " ")
            self.end_credits(FINAL_DELAY, END_CREDITS_DELAY_2)
            # print("ptr:", len(self.acc))

        # print("final:", credit_len - len(self.acc), "out of", credit_len)
        assert len(self.acc) <= credit_len

        string_table_start = 0x3FE8E4
        string_table_size = len(self.strings) * 2

        # Fill the unused section of credits script with 0.
        # This is very important.
        self.acc += (credit_len - len(self.acc)) * [0]

        free_list: dict[int, int] = {
            0x3F9C40: 952,
            credit_start + len(self.acc): credit_len - len(self.acc),
            string_table_start + string_table_size: 2080 - string_table_size,
        }

        patch: dict[int, bytearray] = {}
        patch[credit_start] = bytearray(self.acc)
        for i in range(len(self.strings)):
            string_bytes = inv_str(self.strings[i])
            base = allocate_string(len(string_bytes), free_list)
            if base is None:
                raise Exception("Ran out of space for credits strings!")
            patch[base] = bytearray(string_bytes)
            patch[string_table_start + i * 2] = bytearray((base & 0xFFFF).to_bytes(length=2, byteorder='little'))

        # Underscore
        patch[0x3FFDDA] =  bytearray(b"\x3f\xc0\x7f\x80")
        return patch


# LINE 1, LINE 2, LINE 3. put EMPTY_STRING if you don't have anything.
DEV_MESSAGES = [
    ("DONT TRY IT...ALANIM.", "I ALREADY DID IT.", "   PAST ALANIM"),
    ("NOW TRY IT", "BLINDFOLDED", "     PATCDR"),
    ("IF YOU CAN READ THIS", "IT MEANS I FIXED IT", "       PIDGEZERO_ONE"),
    ("OHH I GOTTA THINK", "OF SOMETHING FUNNY", "       YAKI"),
    ("WHY ARE YOU", "USING ZSNES", "    DORKMASTER FLEK"),
]


def get_palette_authors(world: GameWorld) -> list[str]:
    """Collect unique palette authors from the world's selected palettes.

    Returns a list of unique author names (no duplicates), excluding palettes
    that have no author attribute (i.e., defaults).
    """
    authors = []
    palettes = [
        getattr(world, 'mario_palette', None),
        getattr(world, 'mallow_palette', None),
        getattr(world, 'geno_palette', None),
        getattr(world, 'bowser_palette', None),
        getattr(world, 'toadstool_palette', None),
    ]

    for palette in palettes:
        if palette is not None and hasattr(palette, 'author') and palette.author:
            if palette.author not in authors:
                authors.append(palette.author)

    return authors


def pad_author_line(author1: str, author2: str, total_length: int = 25) -> str:
    """Combine two author names into a single line with space padding.

    The line will be exactly total_length characters, with spaces between
    the two names (not at the beginning or end).
    """
    combined_len = len(author1) + len(author2)
    padding_needed = total_length - combined_len
    if padding_needed < 1:
        padding_needed = 1  # At least one space between names
    return author1 + " " * padding_needed + author2


def find_best_author_pairs(authors: list[str], max_line_length: int = 25) -> list[tuple[str, str]]:
    """Find the best pairing of authors so each combined line fits within max_line_length.

    Returns a list of (author1, author2) tuples. For odd numbers of authors,
    the longest name is placed alone at the end.
    """
    if len(authors) <= 1:
        return [(authors[0], "")] if authors else []

    # Sort by length for easier pairing (shortest with longest)
    sorted_authors = sorted(authors, key=len)

    # For odd number, put the longest on its own line (last)
    if len(sorted_authors) % 2 == 1:
        longest = sorted_authors.pop()  # Remove longest
    else:
        longest = None

    pairs = []
    # Pair shortest with longest remaining, working inward
    while len(sorted_authors) >= 2:
        short = sorted_authors.pop(0)
        long = sorted_authors.pop()

        # Check if they fit together (need at least 1 space between)
        if len(short) + len(long) + 1 <= max_line_length:
            pairs.append((short, long))
        else:
            # If they don't fit, try to find a better match
            # This is a simple greedy approach; could be improved
            pairs.append((short, long))

    # Add the longest name alone if odd number of authors
    if longest:
        pairs.append((longest, ""))

    return pairs


def add_palette_author_credits(credits: Credits, authors: list[str]) -> None:
    """Add palette author credits based on the number of authors.

    Layout varies by count:
    - 1 author: single centered line
    - 2 authors: two separate lines
    - 3 authors: three separate lines
    - 4 authors: two lines with paired names
    - 5 authors: three lines, first two paired, third alone (longest name)
    """
    if not authors:
        return

    credits.begin_credits()

    if len(authors) == 1:
        credits.add_credit(0x80, 0x40, 0x81, authors[0])

    elif len(authors) == 2:
        credits.add_credit(0x80, 0xC0, 0xC0, authors[0])
        credits.add_credit(0x80, 0x80, 0x81, authors[1])

    elif len(authors) == 3:
        credits.add_credit(0x80, 0x80, 0xC0, authors[0])
        credits.add_credit(0x80, 0x40, 0x81, authors[1])
        credits.add_credit(0x80, 0x00, 0xC2, authors[2])

    elif len(authors) == 4:
        pairs = find_best_author_pairs(authors)
        line1 = pad_author_line(pairs[0][0], pairs[0][1])
        line2 = pad_author_line(pairs[1][0], pairs[1][1])
        credits.add_credit(0x80, 0xC0, 0xC0, line1)
        credits.add_credit(0x80, 0x80, 0x81, line2)

    elif len(authors) >= 5:
        # Take first 5 authors only
        authors_to_use = authors[:5]
        pairs = find_best_author_pairs(authors_to_use)
        # pairs will be [(short1, long1), (short2, long2), (longest, "")]
        line1 = pad_author_line(pairs[0][0], pairs[0][1])
        line2 = pad_author_line(pairs[1][0], pairs[1][1])
        line3 = pairs[2][0]  # Longest name alone
        credits.add_credit(0x80, 0x80, 0xC0, line1)
        credits.add_credit(0x80, 0x40, 0x81, line2)
        credits.add_credit(0x80, 0x00, 0xC2, line3)

    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)


# Takes world because everything does.
# If we every implement stats, we'll need it, probably.
def update_credits(world: GameWorld) -> dict[int, bytearray]:
    credits = Credits()

    # Don't need this for the first title.
    # credits.begin_title(BEGIN_TITLES_DELAY)

    # This is what the remake does. We can do it too to make room for randomizer credits.
    credits.add_title(0x80, 0x00, 0x08, "SINCE MCMXCVI")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "BASED ON THE WORK OF")
    credits.add_credit(0x80, 0x40, 0x81, "THE ORIGINAL")
    credits.add_credit(0x80, 0x00, 0xC2, "DEVELOPMENT STAFF")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Randomizer credits strt here.
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ORIGINAL CONCEPT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "ABYSSONYM")
    credits.add_credit(0x80, 0x80, 0x81, "LACKATTACK")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 25
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "CORE DEVELOPMENT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "ALANIM    DORKMASTER FLEK")
    credits.add_credit(0x80, 0x80, 0xC2, "PATCDR      PIDGEZERO_ONE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "DEVELOPMENT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "YAKIBOMB         FORALIAS")
    credits.add_credit(0x80, 0x80, 0xC2, "WEFFJEBSTER        SWINCH")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "ABYSSONYM        CHAOSICX")
    credits.add_credit(0x80, 0x40, 0x81, "CODANTHEBARBARIAN")
    credits.add_credit(0x80, 0x00, 0xC2, "AMAZING AMPHAROS")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "POSTGAME DEMAKE DEVELOPMENT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "ANAXEMRANGER")
    credits.add_credit(0x80, 0x40, 0x81, "CLEARTONIC")
    credits.add_credit(0x80, 0x00, 0xC2, "PIDGEZERO_ONE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ARCHIPELAGO DEVELOPMENT LEAD")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x40, 0x81, "ROSALIE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ARCHIPELAGO DEVELOPMENT")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "SOLIDUS SNAKE")
    credits.add_credit(0x80, 0x80, 0x81, "BIGMALLETMAN")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "TEST WRITING")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "SERAPHIN EVELES")
    credits.add_credit(0x80, 0x80, 0x81, "WONDERJ")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "ARTWORK")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "XIRR")
    credits.add_credit(0x80, 0x40, 0x81, "SYSL")
    credits.add_credit(0x80, 0x00, 0xC2, "MR DEAN")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "SMBAI            SEANCASS")
    credits.add_credit(0x80, 0x40, 0x81, "ALANIM            EGGTALK")
    credits.add_credit(0x80, 0x00, 0xC2, "MINAMIYO           NIMBUS")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Show palette credits if any non-default palette is selected
    palette_flags = [
        MarioPaletteChoice, MallowPaletteChoice, GenoPaletteChoice,
        BowserPaletteChoice, ToadstoolPaletteChoice,
    ]
    if any(world.settings.get_flag(f).selected.name != "DEFAULT" for f in palette_flags):
        palette_authors = get_palette_authors(world)
        if palette_authors:
            credits.begin_titles(BEGIN_TITLES_DELAY)
            credits.add_title(0x80, 0x00, 0x08, "SELECTED ALLY PALETTES")
            credits.end_titles(END_TITLES_DELAY)

            add_palette_author_credits(credits, palette_authors)

    # 26
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "WRITING")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0xC0, 0xC0, "CYNAS       PIDGEZERO_ONE")
    credits.add_credit(0x80, 0x80, 0x81, "BROATMEAL            SYSL")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 27
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "QA AND RESEARCH")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "FLARE       INTHENAMEOFDT")
    credits.add_credit(0x80, 0x40, 0x81, "LOCKECOLELIVE  GOZENGATTA")
    credits.add_credit(0x80, 0x00, 0xC2, "CAVIN               SMBAI")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "TINYWETBLANKET   SEANCASS")
    credits.add_credit(0x80, 0x40, 0x81, "WEFFJEBSTER     BROATMEAL")
    credits.add_credit(0x80, 0x00, 0xC2, "CYNAS        SNESCHALMERS")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "GUNTHERRIDEL     XELECIUM")
    credits.add_credit(0x80, 0x40, 0x81, "MINAMIYO       CALERELIYA")
    credits.add_credit(0x80, 0x00, 0xC2, "SPACE COW      SAXXON FOX")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "ATEATREE         INVARIEL")
    credits.add_credit(0x80, 0x40, 0x81, "GOODMORNINGCRONO  LYLOVIR")
    credits.add_credit(0x80, 0x00, 0xC2, "ANTHONY MULBERRY")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 29
    if world.settings.isflag_enabled(RandomTadpolePondSong):

        credits.begin_titles(BEGIN_TITLES_DELAY)
        credits.add_title(0x80, 0x00, 0x08, "SELECTED MELODY BAY TUNES")
        credits.end_titles(END_TITLES_DELAY)

        credits.begin_credits()
        tadpole_submitters = world.song_authors
        if len(tadpole_submitters) == 1:
            credits.add_credit(0x80, 0x80, 0xC0, EMPTY_STRING)
            credits.add_credit(0x80, 0x40, 0x81, tadpole_submitters[0])
            credits.add_credit(0x80, 0x00, 0xC2, EMPTY_STRING)
        elif len(tadpole_submitters) == 2:
            credits.add_credit(0x80, 0x80, 0xC0, EMPTY_STRING)
            credits.add_credit(0x80, 0xC0, 0xC0, tadpole_submitters[0])
            credits.add_credit(0x80, 0x80, 0x81, tadpole_submitters[1])
        else:
            credits.add_credit(0x80, 0x80, 0xC0, tadpole_submitters[0])
            credits.add_credit(0x80, 0x40, 0x81, tadpole_submitters[1])
            credits.add_credit(0x80, 0x00, 0xC2, tadpole_submitters[2])
        credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 30
    if world.settings.isflag_enabled(RandomSunkenShipPassword):

        credits.begin_titles(BEGIN_TITLES_DELAY)
        credits.add_title(0x80, 0x00, 0x08, "SELECTED SHIP PASSWORD")
        credits.end_titles(END_TITLES_DELAY)

        credits.begin_credits()
        credits.add_credit(0x80, 0x40, 0x81, world.password_author)
        credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 31
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "SPECIAL THANKS")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "DARKKEFKA       DOOMSDAY")
    credits.add_credit(0x80, 0x40, 0x81, "GIANGURGOLO        OMEGA")
    credits.add_credit(0x80, 0x00, 0xC2, "WILL")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 32
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "INSPIRATION")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "ALTTP AND OOT RANDOMIZER")
    credits.add_credit(0x80, 0x40, 0x81, "FFIV FREE ENTERPRISE")
    credits.add_credit(0x80, 0x00, 0xC2, "GOOD QUOTATIONS")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # new
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "IF YOU WANT YOUR NAME HERE...")
    credits.end_titles(END_TITLES_DELAY)

    dev_line1, dev_line2, dev_line3 = random.choice(DEV_MESSAGES)
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "VISIT")
    credits.add_credit(0x80, 0x40, 0x81, "RANDOMIZER.SMRPGSPEEDRUNS.COM")
    credits.add_credit(0x80, 0x00, 0xC2, "TO CONTRIBUTE")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 38
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "SPECIAL DEV MESSAGE")
    credits.end_titles(END_TITLES_DELAY)

    dev_line1, dev_line2, dev_line3 = random.choice(DEV_MESSAGES)
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, dev_line1)
    credits.add_credit(0x80, 0x40, 0x81, dev_line2)
    credits.add_credit(0x80, 0x00, 0xC2, dev_line3)
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Clear the titles
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    # 33
    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "THANK YOU SMRPG COMMUNITY.")
    credits.add_credit(0x80, 0x40, 0x81, "WITHOUT YOU...")
    credits.add_credit(0x80, 0x00, 0xC2, "NONE OF THIS WOULD BE POSSIBLE.")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # 38
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.add_title(0x80, 0x00, 0x08, "DEDICATED TO")
    credits.end_titles(END_TITLES_DELAY)

    credits.begin_credits()
    credits.add_credit(0x80, 0x80, 0xC0, "TINYWETBLANKET")
    credits.add_credit(0x80, 0x40, 0x81, "THANK YOU MIKAYLA")
    credits.add_credit(0x80, 0x00, 0xC2, "WE MISS YOU")
    credits.end_credits(END_CREDITS_DELAY_1, END_CREDITS_DELAY_2)

    # Clear the titles
    credits.begin_titles(BEGIN_TITLES_DELAY)
    credits.end_titles(END_TITLES_DELAY)

    credits.end_thing(END_CREDITS_DELAY_1)  # Yeah, my abstraction breaks at the end.

    return credits.finalize()
