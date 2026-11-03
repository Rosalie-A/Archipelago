import warnings
import logging

logger = logging.getLogger("Client")

# The string table has room for 1,442 characters and the extended table (a chunk
# in bank 1 that appears unused) has room for 1,934 characters for a total of
# 3,376 characters. May lose some characters to table alignment!
# If all character lines use the maximum 24*3 = 72 characters, the whole table
# would be 2,664 characters
string_table_index_offset = 0x4010
string_table_end = 0x45B2
extended_table_offset = 0x77D2
extended_table_end = 0x7F60
# Divide by 2 to get the table index!
hint_offsets = (
    0x00,  # __IT'S DANGEROUS TO GO____ALONE! TAKE THIS.
    0x02,  # __MASTER USING IT AND___YOU CAN HAVE THIS.
    0x04,  # _TAKE ANY ROAD YOU WANT.
    0x06,  # _SECRET IS IN THE TREE____AT THE DEAD-END.
    0x08,  # ___LET'S PLAY MONEY___MAKING GAME.
    0x0A,  # __PAY ME FOR THE DOOR_____REPAIR CHARGE.
    0x0C,  # ____SHOW THIS TO THE_______OLD WOMAN.
    0x0E,  # ____MEET THE OLD MAN______AT THE GRAVE.
    0x10,  # __BUY MEDICINE BEFORE__YOU GO.
    0x12,  # __PAY ME AND I'LL TALK.                                Hint woman greeting
    0x14,  # ___THIS AIN'T ENOUGH________TO TALK.                   Hint woman -10
    0x16,  # _______GO UP,UP,___THE MOUNTAIN AHEAD.                 Hint woman -30
    0x18,  # __GO NORTH,WEST,SOUTH,__WEST TO THE FOREST  OF MAZE.   Hint woman -30
    0x1A,  # ____BOY, YOU'RE RICH!                                  Hint woman -50
    0x1C,  # _BUY SOMETHIN' WILL YA!
    0x1E,  # _____BOY, THIS IS___REALLY EXPENSIVE!
    0x20,  # _TAKE ANY ONE YOU WANT.
    0x22,  # _____IT'S A SECRET_____TO EVERYBODY.
    0x24,  # ___GRUMBLE,GRUMBLE...
    0x26,  # __EASTMOST PENNINSULA_____IS THE SECRET.
    0x28,  # _DODONGO DISLIKES SMOKE.
    0x2A,  # _DID YOU GET THE SWORD_FROM THE OLD MAN ON_TOP OF THE WATERFALL?
    0x2C,  # _____WALK INTO THE_______WATERFALL.
    0x2E,  # __SECRET POWER IS SAID___TO BE IN THE ARROW.
    0x30,  # ____DIGDOGGER HATES_CERTAIN KIND OF SOUND.
    0x32,  # ____I BET YOU'D LIKE___TO HAVE MORE BOMBS.
    0x34,  # ____IF YOU GO IN THE_DIRECTION OF THE ARROW.
    0x36,  # ____LEAVE YOUR LIFE_______OR MONEY.
    0x38,  # _THERE ARE SECRETS WHERE___FAIRIES DON'T LIVE.
    0x3A,  # ____AIM AT THE EYES_______OF GOHMA.
    0x3C,  # __SOUTH OF ARROW MARK____HIDES A SECRET.
    0x3E,  # __THERE'S A SECRET IN__THE TIP OF THE NOSE.
    0x40,  # ___SPECTACLE ROCK IS__AN ENTRANCE TO DEATH.
    0x42,  # 10TH ENEMY HAS THE BOMB.
    0x44,  # _ONES WHO DOES NOT HAVE_TRIFORCE CAN'T GO IN.
    0x46,  # ___PATRA HAS THE MAP.
    0x48,  # __GO TO THE NEXT ROOM.
    0x4A   # _____EYES OF SKULL_____HAS A SECRET.
)

# We can hint in two ways that we care about:
# What is at screen __?
# What is at check __?
# screen hints aren't implemented yet, just check hints
# (hinted_location, string_offset)
hint_early_dungeons_data = {
    0x00: ("Screen 0A", 0x2C),          # Level 4: Walk into the waterfall
    0x0B: ("Screen 42", 0x38),          # Level 6: There are secrets where fairies don't live
    0x15: (None, 0x2E),                 # Level 5: Secret power is said to be in the arrow
    0x1F: ("Level 2 Boss", 0x28),       # Level 2: Dodongo dislikes smoke
    0x2B: ("White Sword Pond", 0x2A),   # Level 3: Did you get the sword from the old man on top of the waterfall?
    0x41: ("Screen 2F", 0x26),          # Level 1: Eastmost penninsula is the secret.
    0x67: ("Level 5 Boss", 0x30),       # Level 5: Digdogger hates certain kinds of sound.
    0x6A: ("Level 6 Boss", 0x3A),       # Level 6: Aim at the eyes of Gohma
}
hint_late_dungeons_data = {
    0x02: ("Level 9 Compass", 0x4A),    # Level 9: Eyes of skull has a secret
    0x06: (None, 0x48),                 # Level 9: Go to the next room
    0x3B: (None, 0x42),                 # Level 8: 10th enemy has the bomb
    0x3D: ("Screen 05", 0x40),          # Level 8: Spectacle rock is an entrance to death
    0x5B: ("Level 7 Boss", 0x3E),       # Level 7: There's a secret in the tip of the nose
}

hint_caves_data = {
    # These first two hints refer to the woman you pay for a hint. These offsets
    # go to the -30 option that actually grants a hint, not the greeting or
    # other two options. Currently, they won't wait until you pay for the hint to
    # location scout (if these are set to something other than a None or Screen hint)
    "Go Up The Mountain Hint":  ("Screen 0B", 0x16),
    "Lost Woods Hint":          (None, 0x18),
    "Secret Is In Tree Hint":   ("Screen 1F", 0x06),
    "Old Man Grave Hint":       ("Magical Sword Grave", 0x0E),
    "Starting Sword Cave":      (None, 0x00),
}

# Format strings that expects arguments:
# item_player, item_name, extra_hint_info
location_hint_sugar = {
    "Level 1 Boss": "Aquamentus has {}'s {}{}",
    "Level 1 Triforce": "Aquamentus guards {}'s {}{}",
    "Level 2 Boss": "Dodongo has {}'s {}{}",
    "Level 2 Triforce": "Dodongo guards {}'s {}{}",
    "Level 3 Boss": "Manhandla has {}'s {}{}",
    "Level 3 Triforce": "Manhandla guards {}'s {}{}",
    "Level 4 Boss": "Gleeok has {}'s {}{}",
    "Level 4 Triforce": "Gleeok guards {}'s {}{}",
    "Level 5 Boss": "Digdogger has {}'s {}{}",
    "Level 5 Triforce": "Digdogger guards {}'s {}{}",
    "Level 6 Boss": "Gohma has {}'s {}{}",
    "Level 6 Triforce": "Gohma guards {}'s {}{}",
    "Level 7 Boss": " Aquamentus has {}'s {}{}",
    "Level 7 Triforce": "Aquamentus guards {}'s {}{}",
    "Level 8 Boss": "Gleeok has {}'s {}{}",
    "Level 8 Triforce": "Gleeok guards {}'s {}{}",
}

# The ROM is chopped up into banks that are loaded into memory at 0x8000, translate between them!
def rom_addr_to_memory_addr(address):
    if address < 0x10: return None
    elif address < 0x1C010:
        # Header length
        address -= 0x10
        # Bank size
        address %= 0x4000
        return address + 0x8000
    else:
        return address - 0x10 - 0x1C000 + 0xC000

def write_hints(rom_data, placements):
    # Build a set of locations that can be hinted, and the string offset that
    # hint should overwrite
    hint_offsets_set = {}
    for hint_data in [hint_caves_data, hint_early_dungeons_data, hint_late_dungeons_data]:
        for location, (hint_location, offset) in hint_data.items():
            if hint_location is None:
                continue
            if hint_location[:6] == "Screen":
                continue
            hint_offsets_set[hint_location] = offset

    string_table = read_string_table(rom_data)
    num_truncated, num_omitted, num_hints = (0,0,0)
    for location, item in placements["locations"].items():
        if location not in hint_offsets_set:
            continue
        offset = hint_offsets_set[location]
        encoded_string, truncated, omitted = align_string(item["hint"])
        # If we truncate the screen characters, it's probably fine?
        # Assumes omitted characters are totally okay
        if truncated <= 3:
            string_table[offset // 2] = encoded_string
            num_hints += 1
            if truncated:
                num_truncated += truncated
            if omitted:
                num_omitted += omitted
    write_string_table(rom_data, string_table)
    logger.info(f"Patch wrote {num_hints} of {len(hint_offsets_set)} hints with {num_truncated} truncated and {num_omitted} omitted characters")

# Converts a Python string to a ROM-encoded string. Returns a tuple with the resulting byte string and a count of how any characters were omitted
# (bytes, omitted)
def string_to_bytes(string):
    res = []
    char_byte_table = {
        '0': 0x00, '1': 0x01, '2': 0x02, '3': 0x03, '4': 0x04, '5': 0x05, '6': 0x06, '7': 0x07, '8': 0x08, '9': 0x09,
        'a': 0x0A, 'b': 0x0B, 'c': 0x0C, 'd': 0x0D, 'e': 0x0E, 'f': 0x0F, 'g': 0x10, 'h': 0x11, 'i': 0x12, 'j': 0x13, 'k': 0x14, 'l': 0x15, 'm': 0x16, 'n': 0x17, 'o': 0x18, 'p': 0x19, 'q': 0x1A, 'r': 0x1B, 's': 0x1C, 't': 0x1D, 'u': 0x1E, 'v': 0x1F, 'w': 0x20, 'x': 0x21, 'y': 0x22, 'z': 0x23,
        ' ': 0x24,
        # '~': 0x25, # This is actually a spacing character, not a tilde
        ',': 0x28, '!': 0x29, '\'': 0x2A, '&': 0x2B,
        '.': 0x2C, '"': 0x2D, '?': 0x2E, '-': 0x2F
    }
    # Keep track of line numbers to encode \n properly
    line_num = 0
    omitted = 0
    for char in string.lower():
        if char == '\n':
            if line_num == 0:
                res[-1] |= 0x80
                line_num += 1
                continue
            elif line_num == 1:
                res[-1] |= 0x40
                line_num += 1
                continue
            else:
                res[-1] |= 0xC0
                break
        byte = char_byte_table.get(char)
        if None != byte:
            res.append(byte)
        else:
            omitted += 1
    return (res, omitted)

# Returns a list of ROM-encoded strings from the string table
def read_string_table(rom_data):
    string_table_offset = string_table_index_offset + 0x4C
    res = []
    cur_str = []
    for offset in range(string_table_end - string_table_offset):
        cur_str.append(rom_data[string_table_offset + offset])
        if (cur_str[-1] & 0xC0 == 0xC0):
            res.append(cur_str)
            cur_str = []
    return res

# Writes a list of ROM-encoded strings to the string table
def write_string_table(rom_data, string_table):
    string_table_offset = string_table_index_offset + 0x4C
    # Ensure there are fewer strings than entries in the table
    assert len(string_table) <= ( 0x4C >> 1 ), "Attempting to write too many strings to the string table! {} <= {}".format(len(string_table), 0x4C >> 1)

    string_write_offset = string_table_offset
    string_write_end = string_table_end
    for string_num, string in enumerate(string_table):
        # Check if the string can fit in the table, otherwise fall back to the
        # extended table and try to write there. If we're already pointing to
        # the extended table, the check below with the early exit will
        # gracefully catch and truncate it
        if (len(string) > string_write_end - string_write_offset):
            # Only overwrite the current string offset if we haven't switched
            # to the extended table.
            if string_write_end != extended_table_end:
                string_write_offset = extended_table_offset
                string_write_end = extended_table_end

        memory_string_offset = rom_addr_to_memory_addr(string_write_offset)
        rom_data[string_table_index_offset + string_num * 2] = memory_string_offset & 0xFF
        rom_data[string_table_index_offset + string_num * 2 + 1] = (memory_string_offset >> 8) & 0xFF
        for char in string:
            # If we ever try to write past the string table, STOP
            # immediately and warn. Stopping here prevents us from
            # corrupting the rest of the game, just the text will be funky
            if False and string_write_offset >= string_write_end:
                # Ensure the string is terminated
                rom_data[string_write_offset - 1] |= 0xC0
                warnings.warn("TLOZ: Attempted to write past the ROM player string table! Truncating string")
                return

            rom_data[string_write_offset] = char
            string_write_offset += 1

        # Ensure the string is terminated
        rom_data[string_write_offset - 1] |= 0xC0

# Returns a tuple where the first item is the string centered (unless specified)
# and split across lines, the second item is how many characters were truncated,
# the third is how many characters were omitted.
def align_string(string, center=True):
    line_width = 24
    # Appending a space here forces the following for loop to add the last token to the lines
    encoded_string, omitted = string_to_bytes(string + ' ')
    lines = []
    cur_line = []
    cur_tok = []
    ending_space = 0
    for char_num, char in enumerate(encoded_string):
        # Exit early if we reach the line limit
        if len(lines) >= 3:
            break

        # If newlines are already encoded, blindly trust them
        if char & 0xC0:
            cur_tok.append(char)
            cur_line.extend(cur_tok)
            lines.append(cur_line)
            cur_tok = []
            cur_line = []
            if char & 0xC0 == 0xC0:
                break
            else:
                continue

        # Wait to append spaces until we know if the next token can fit on this line
        if char != 0x24:
            cur_tok.append(char)
        # tokenize on ' ' and '-' to see if we should put a newline here
        if char == 0x24 or char == 0x2F:
            if len(cur_line) + ending_space + len(cur_tok) < line_width:
                if ending_space > 0:
                    cur_line.append(0x24)
                cur_line.extend(cur_tok)
            else:
                if len(lines) == 0:
                    # Starting next character, write to line 2
                    cur_line[-1] |= 0x80
                elif len(lines) == 1:
                    # Starting next character, write to line 3
                    cur_line[-1] |= 0x40
                lines.append(cur_line)
                cur_line = cur_tok
            cur_tok = []
            ending_space = 1 if char == 0x24 else 0

        # My, what a long token you have! Let's chop it up!
        if len(cur_tok) >= line_width:
            if ending_space > 0:
                cur_line.append(0x24)
            # Leave room for the hyphen after the token
            remaining_chars = line_width - len(cur_line) - 1
            cur_line.extend(cur_tok[0:remaining_chars])
            cur_line.append(0x2F)
            if len(lines) == 0:
                # Starting next character, write to line 2
                cur_line[-1] |= 0x80
            elif len(lines) == 1:
                # Starting next character, write to line 3
                cur_line[-1] |= 0x40
            lines.append(cur_line)
            cur_tok = cur_tok[remaining_chars:]

    # Append the final line if it wasn't finished
    if len(cur_line) > 0 and len(lines) < 3:
        lines.append(cur_line)

    res = []
    for line in lines:
        if center:
            spacers = ( line_width - len(line) ) // 2
            res.extend([0x25]*spacers)
        res.extend(line)
    # Terminate the string
    res[-1] |= 0xC0
    is_truncated = char_num < len(encoded_string) - 1
    return (res, is_truncated, omitted)

def print_encoded_string(string):
    char_byte_table = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ', '~', '*', '*', ',', '!', '\'', '&', '.', '"', '?', '-' ]

    line = ''
    for char in string:
        i = char & 0x3F
        line += char_byte_table[i]
        if char & 0xC0 > 0:
            print(line)
            line = ''

