from django.core.management.base import BaseCommand
from smrpgpatchbuilder.datatypes.graphics.classes import (
    Sprite,
    ImagePack,
    AnimationPack,
    AnimationPackProperties,
    AnimationSequence,
    AnimationSequenceFrame,
    AnimationBank,
    Mold,
    Tile,
    Clone,
)
from smrpgpatchbuilder.utils.disassembler_common import (
    shortify,
    writeline,
)
from smrpgpatchbuilder.management.commands.input_file_parser import (
    load_arrays_from_input_files,
)
from concurrent.futures import ThreadPoolExecutor, as_completed
import multiprocessing
import string, random, shutil, os

PALETTE_OFFSET = 0x253000

def get_animation_pack_data_offset_from_third_byte(short, b):
    return ((b - 0xC0) << 16) + short

alphabet = string.ascii_lowercase + string.digits

def random_tile_id():
    return "".join(random.choices(alphabet, k=8))

def load_animation_banks(filename: str) -> list[AnimationBank]:
    animation_banks = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                start_str, end_str = line.split()
                start_addr = int(start_str, 16)
                end_addr = int(end_str, 16)
                animation_banks.append(AnimationBank(start_addr, end_addr))
            except ValueError:
                print(f"Skipping malformed line: {line}")

    return animation_banks

def load_tuples(filename: str) -> list[tuple[int, int]]:
    tuples: list[tuple[int, int]] = []
    with open(filename, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            try:
                start_str, end_str = line.split()
                start_addr = int(start_str, 16)
                end_addr = int(end_str, 16)
                tuples.append((start_addr, end_addr))
            except ValueError:
                print(f"Skipping malformed line: {line}")

    return tuples

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom")

        parser.add_argument(
            "-d",
            "--debug",
            action="store_true",
            help="If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer",
        )

    def handle(self, *args, **options):
        output_path = "./src/disassembler_output/sprites"

        shutil.rmtree(output_path, ignore_errors=True)

        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w")

        os.makedirs(f"{output_path}/objects", exist_ok=True)
        open(f"{output_path}/objects/__init__.py", "w")

        # Load sprite names from input files
        arrays = load_arrays_from_input_files()
        sprite_names = arrays.get("sprites", [])

        tile_write_banks = load_animation_banks("./config/tiles_write.input")
        animation_write_banks = load_animation_banks("./config/animationdata_write.input")

        tile_read_banks = load_tuples("./config/tiles_read.input")
        animation_read_banks = load_tuples("./config/animationpack_read.input")
        toplevelsprite_read = load_tuples("./config/toplevelsprite_read.input")
        imagepack_read = load_tuples("./config/imagepack_read.input")

        global rom
        rom = bytearray(open(options["rom"], "rb").read())

        sprites = []
        images = []
        packs = []
        all_tiles = []
        tile_ids = []

        for _, (bank_start, bank_end) in enumerate(tile_read_banks):
            for _, offset in enumerate(range(bank_start, bank_end, 0x20)):
                tile = rom[offset : offset + 0x20]
                dupe = False
                for t in all_tiles:
                    if t[1] == tile:
                        dupe = True
                if not dupe:
                    tile_id = random_tile_id()
                    while tile_id in tile_ids:
                        tile_id = random_tile_id()
                    all_tiles.append((tile_id, tile))

        for index, offset in enumerate(
            range(
                toplevelsprite_read[0][0],
                toplevelsprite_read[0][1],
                4,
            )
        ):
            if shortify(rom, offset + 2) > 443:
                sprite = Sprite(index, 0, 0, 0, 0)
            else:
                img = shortify(rom, offset) & 0x1FF
                pal_off = (rom[offset + 1] & 0x0E) >> 1
                unknown = rom[offset + 1] >> 4
                sprite = Sprite(index, img, shortify(rom, offset + 2), pal_off, unknown)
            sprites.append(sprite)

        for index, offset in enumerate(
            range(
                imagepack_read[0][0],
                imagepack_read[0][1],
                4,
            )
        ):
            gfx_ptr_short = shortify(rom, offset)
            bank = ((rom[offset] & 0x0F) << 16) + 0x280000
            gfx_ptr = (gfx_ptr_short & 0xFFF0) + bank
            images.append(
                ImagePack(index, gfx_ptr, 0x250000 + shortify(rom, offset + 2))
            )

        for _, (bank_start, bank_end) in enumerate(animation_read_banks):
            for index, property_offset_ptr_offset in enumerate(
                range(
                    bank_start,
                    bank_end,
                    3,
                )
            ):
                # if index > 316:
                if index > 465:
                    break
                property_offset_ptr_offset = bank_start + (index * 3)
                property_offset = get_animation_pack_data_offset_from_third_byte(
                    shortify(rom, property_offset_ptr_offset),
                    rom[property_offset_ptr_offset + 2],
                )
                if property_offset == -0xC00000:
                    continue

                molds = []
                sequences = []

                length = shortify(rom, property_offset)
                sequence_packet_ptr_relative_offset = shortify(rom, property_offset + 2)
                mold_packet_ptr_relative_offset = shortify(rom, property_offset + 4)
                sequence_count = rom[property_offset + 6]
                mold_count = rom[property_offset + 7]
                vram_size = shortify(rom, property_offset + 8) << 8
                unknown = shortify(rom, property_offset + 10)

                for i in range(0, sequence_count):
                    sequence_offset = (
                        property_offset + sequence_packet_ptr_relative_offset + i * 2
                    )
                    frames = []
                    if shortify(rom, sequence_offset) != 0xFFFF:
                        relative_offset = shortify(rom, sequence_offset) & 0x7FFF
                        offset = relative_offset + property_offset
                        while rom[offset] != 0 and relative_offset != 0x7FFF:
                            frames.append(
                                AnimationSequenceFrame(rom[offset], rom[offset + 1])
                            )
                            relative_offset += 2
                            offset = relative_offset + property_offset
                    sequences.append(AnimationSequence(frames))

                for i in range(0, mold_count):
                    mold_offset = property_offset + mold_packet_ptr_relative_offset + i * 2
                    relative_offset = mold_offset
                    if shortify(rom, relative_offset) != 0xFFFF:
                        gridplane = (rom[relative_offset + 1] & 0x80) == 0x80
                        tile_packet_pointer = shortify(rom, relative_offset) & 0x7FFF
                        relative_offset = tile_packet_pointer + property_offset
                        if gridplane:
                            tile_length = 0
                            format = rom[relative_offset]
                            relative_offset += 1
                            is_16bit = (format & 0x08) == 0x08
                            y_plus = 1 if (format & 0x10) == 0x10 else 0
                            y_minus = 1 if (format & 0x20) == 0x20 else 0
                            mirror = (format & 0x40) == 0x40
                            invert = (format & 0x80) == 0x80
                            tile_length += 1
                            format &= 3
                            if is_16bit:
                                subtiles_16bit = shortify(rom, relative_offset)
                                relative_offset += 2
                                tile_length += 2
                            else:
                                subtiles_16bit = 0
                            copy_length = 9
                            if format == 1 or format == 2:
                                copy_length = 12
                            elif format == 3:
                                copy_length = 16
                            tile_length += copy_length
                            subtile_bytes = [1] * copy_length
                            subtile_bytes[0:copy_length] = rom[
                                relative_offset : relative_offset + copy_length
                            ]
                            if is_16bit:
                                for j in range(0, copy_length):
                                    if (subtiles_16bit & (2**j)) == (2**j):
                                        subtile_bytes[j] += 0x100
                            molds.append(
                                Mold(
                                    i,
                                    gridplane,
                                    [
                                        Tile(
                                            mirror=mirror,
                                            invert=invert,
                                            format=format,
                                            length=tile_length,
                                            subtile_bytes=subtile_bytes,
                                            is_16bit=is_16bit,
                                            y_plus=y_plus,
                                            y_minus=y_minus,
                                            is_clone=False,
                                        )
                                    ],
                                )
                            )
                        else:
                            tiles = []
                            while rom[relative_offset] != 0:
                                temp_offset = relative_offset
                                is_clone = False
                                if (rom[relative_offset] & 0x03) == 2:
                                    is_clone = True
                                    y = rom[relative_offset + 1]
                                    x = rom[relative_offset + 2]
                                    mirror = (rom[relative_offset] & 0x04) == 0x04
                                    invert = (rom[relative_offset] & 0x08) == 0x08
                                    within_buffer_offset = shortify(
                                        rom, relative_offset + 3
                                    )
                                    if within_buffer_offset >= 0x7FFF:
                                        raise Exception(
                                            "bad mold offset at %06x, mold %i of animation %i"
                                            % (relative_offset, i, index)
                                        )
                                    relative_offset = within_buffer_offset + property_offset
                                    clone_tiles = []
                                    for _ in range(0, rom[temp_offset] >> 4):
                                        if within_buffer_offset > length:
                                            raise Exception(
                                                "bad data at %06x, mold %i of animation %i: 0x%04x is larger than length %i"
                                                % (
                                                    relative_offset,
                                                    i,
                                                    index,
                                                    relative_offset - property_offset,
                                                    length,
                                                )
                                            )
                                        tile_length = 0
                                        if (rom[relative_offset] & 0x03) == 2:
                                            raise Exception(
                                                "bad tile data at %06x, mold %i of animation %i"
                                                % (relative_offset, i, index)
                                            )
                                        else:
                                            temp_offset_2 = relative_offset
                                            format = rom[relative_offset] & 0x0F
                                            mi = (format & 0x04) == 0x04
                                            inv = (format & 0x08) == 0x08
                                            format &= 3
                                            quadrants = [False] * 4
                                            for j in range(0, 4):
                                                div = 128 // (2**j)
                                                quadrants[j] = (
                                                    rom[relative_offset] & div
                                                ) == div
                                            relative_offset += 1
                                            tile_length += 1
                                            tile_y = rom[relative_offset] ^ 0x80  # + y
                                            relative_offset += 1
                                            tile_length += 1
                                            tile_x = rom[relative_offset] ^ 0x80  # + x
                                            relative_offset += 1
                                            tile_length += 1
                                            subtile_bytes = [0] * 4
                                            for j in range(0, 4):
                                                if quadrants[j]:
                                                    if format == 1:
                                                        subtile_bytes[j] = (
                                                            shortify(rom, relative_offset)
                                                            & 0x1FF
                                                        )
                                                        relative_offset += 1
                                                        tile_length += 1
                                                    else:
                                                        subtile_bytes[j] = rom[
                                                            relative_offset
                                                        ]
                                                    relative_offset += 1
                                                    tile_length += 1
                                            relative_offset = temp_offset_2 + tile_length
                                            clone_tiles.append(
                                                Tile(
                                                    mirror=mi,
                                                    invert=inv,
                                                    format=format,
                                                    length=tile_length,
                                                    subtile_bytes=subtile_bytes,
                                                    x=tile_x,
                                                    y=tile_y,
                                                    is_clone=is_clone,
                                                )
                                            )
                                    tiles.append(Clone(x, y, mirror, invert, clone_tiles))
                                    relative_offset = temp_offset + 5
                                else:
                                    tile_length = 0
                                    format = rom[relative_offset] & 0x0F
                                    mirror = (format & 0x04) == 0x04
                                    invert = (format & 0x08) == 0x08
                                    format &= 3
                                    quadrants = [False] * 4
                                    for j in range(0, 4):
                                        quadrants[j] = (
                                            rom[relative_offset] & (128 // (2**j))
                                        ) == (128 // (2**j))
                                    relative_offset += 1
                                    tile_length += 1
                                    tile_y = rom[relative_offset] ^ 0x80
                                    relative_offset += 1
                                    tile_length += 1
                                    tile_x = rom[relative_offset] ^ 0x80
                                    relative_offset += 1
                                    tile_length += 1
                                    subtile_bytes = [0] * 4
                                    for j in range(0, 4):
                                        if quadrants[j]:
                                            if format == 1:
                                                subtile_bytes[j] = (
                                                    shortify(rom, relative_offset) & 0x1FF
                                                )
                                                relative_offset += 1
                                                tile_length += 1
                                            else:
                                                subtile_bytes[j] = rom[relative_offset]
                                            relative_offset += 1
                                            tile_length += 1
                                    tiles.append(
                                        Tile(
                                            mirror=mirror,
                                            invert=invert,
                                            format=format,
                                            length=tile_length,
                                            subtile_bytes=subtile_bytes,
                                            x=tile_x,
                                            y=tile_y,
                                            is_clone=is_clone,
                                        )
                                    )
                                    relative_offset = temp_offset + tile_length
                            molds.append(Mold(i, gridplane, tiles))
                    else:
                        molds.append(Mold(i, False, []))

                packs.append(AnimationPack(index, AnimationPackProperties(sequences, molds, vram_size), length, unknown))

        used_images = [False] * 512
        used_packs = [False] * 1024
        used_palettes = [False] * 819

        # Parallel processing of sprite files
        def write_sprite_file(index, s):
            """Write a single sprite file and return usage information."""
            palette_offset = s.palette_offset
            unknown = s.unknown
            i = images[s.image_num]
            if s.animation_num >= len(packs):
                return None  # Skip this sprite
            p = packs[s.animation_num]

            palette_id_original = (i.palette_pointer - PALETTE_OFFSET) // 30
            palette_id = palette_id_original + palette_offset

            gfx_offset = i.graphics_pointer

            dest = f"{output_path}/objects/sprite_%i.py" % index
            file = open(dest, "w")

            # Write sprite name as a comment if available
            if index < len(sprite_names) and sprite_names[index]:
                writeline(file, f"# {sprite_names[index]}")
                writeline(file, "")

            writeline(
                file,
                "from smrpgpatchbuilder.datatypes.graphics.classes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone",
            )
            writeline(file, "sprite = CompleteSprite(")
            writeline(
                file,
                "    animation=AnimationPack(%i, length=%i, unknown=0x%04x,"
                % (p.index, p.length, p.unknown),
            )
            writeline(
                file,
                "        properties=AnimationPackProperties(vram_size=%i,"
                % p.properties.vram_size,
            )
            writeline(file, "            molds=[")
            for m in p.properties.molds:
                writeline(
                    file,
                    "                Mold(%i, gridplane=%r," % (m.index, m.gridplane),
                )
                writeline(file, "                    tiles=[")
                for t in m.tiles:
                    if not t.is_clone:
                        writeline(
                            file,
                            "                        Tile(mirror=%r, invert=%r, format=%i, length=%i, subtile_bytes=["
                            % (t.mirror, t.invert, t.format, t.length),
                        )
                        for sb in t.subtile_bytes:
                            if sb == 0:
                                writeline(file, "                            None,")
                            else:
                                sb_offset = gfx_offset + (0x20 * (sb - 1))
                                writeline(
                                    file,
                                    "                            %r,"
                                    % rom[sb_offset : sb_offset + 0x20],
                                )
                        writeline(
                            file,
                            "                        ], is_16bit=%r, y_plus=%i, y_minus=%i, x=%i, y=%i),"
                            % (t.is_16bit, t.y_plus, t.y_minus, t.x, t.y),
                        )
                    else:
                        for subt in t.tiles:
                            writeline(
                                file,
                                "                        Tile(mirror=%r, invert=%r, format=%i, length=%i, subtile_bytes=["
                                % (subt.mirror, subt.invert, subt.format, subt.length),
                            )
                            for sb in subt.subtile_bytes:
                                if sb == 0:
                                    writeline(file, "                            None,")
                                else:
                                    sb_offset = gfx_offset + (0x20 * (sb - 1))
                                    writeline(
                                        file,
                                        "                            %r,"
                                        % rom[sb_offset : sb_offset + 0x20],
                                    )
                            writeline(
                                file,
                                "                        ], is_16bit=%r, y_plus=%i, y_minus=%i, x=%i, y=%i),"
                                % (
                                    subt.is_16bit,
                                    subt.y_plus,
                                    subt.y_minus,
                                    t.x + subt.x,
                                    t.y + subt.y,
                                ),
                            )
                writeline(file, "                    ]")
                writeline(file, "                ),")
            writeline(file, "            ],")
            writeline(file, "            sequences=[")
            for seq in p.properties.sequences:
                writeline(file, "                AnimationSequence(")
                writeline(file, "                    frames=[")
                for f in seq.frames:
                    writeline(
                        file,
                        "                        AnimationSequenceFrame(duration=%i, mold_id=%i),"
                        % (f.duration, f.mold_id),
                    )
                writeline(file, "                    ]")
                writeline(file, "                ),")
            writeline(file, "            ]")
            writeline(file, "        )")
            writeline(file, "    ),")
            writeline(file, "    palette_id=%i," % palette_id_original)
            writeline(file, "    palette_offset=%i," % palette_offset)
            writeline(file, "    unknown_num=%i" % unknown)
            writeline(file, ")")
            file.close()

            # Return usage information
            return (s.image_num, s.animation_num, palette_id)

        # Execute sprite writing in parallel
        num_workers = min(multiprocessing.cpu_count(), len(sprites))
        with ThreadPoolExecutor(max_workers=num_workers) as executor:
            futures = [executor.submit(write_sprite_file, idx, sprite)
                      for idx, sprite in enumerate(sprites)]
            for future in as_completed(futures):
                result = future.result()
                if result is not None:
                    image_num, animation_num, palette_id = result
                    used_images[image_num] = True
                    used_packs[animation_num] = True
                    used_palettes[palette_id] = True

        file = open(f"{output_path}/sprites.py", "w", encoding="utf-8")
        writeline(
            file,
            "from smrpgpatchbuilder.datatypes.graphics.classes import SpriteCollection, AnimationBank",
        )
        for i in range(len(sprites)):
            writeline(
                file,
                "from .objects.sprite_%i import sprite as sprite_%i"
                % (i, i),
            )
        writeline(file, "sprites = SpriteCollection(")
        writeline(file, "    [")
        for i in range(len(sprites)):
            writeline(file, "        sprite_%i," % (i))
        writeline(file, "    ],")
        writeline(file, f"    animation_data_banks=[{", ".join(f"AnimationBank(0x{bank.start:06x}, 0x{bank.end:06x})" for bank in animation_write_banks)}],")
        writeline(file, f"    uncompressed_tile_banks=[{", ".join(f"AnimationBank(0x{bank.start:06x}, 0x{bank.end:06x})" for bank in tile_write_banks)}],")
        writeline(file, f"    sprite_data_begins=0x{toplevelsprite_read[0][0]:06x},")
        writeline(file, f"    image_and_animation_data_begins=0x{imagepack_read[0][0]:06x}")
        writeline(file, ")")
        file.close()

        self.stdout.write(
            self.style.SUCCESS(
                "Successfully disassembled sprite graphics data to ./src/disassembler_output/sprites/"
            )
        )
