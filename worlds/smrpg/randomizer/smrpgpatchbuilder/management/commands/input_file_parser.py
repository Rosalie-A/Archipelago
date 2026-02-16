"""Utility for parsing *_names.input files from the config directory."""

from pathlib import Path
import re
import string
import importlib

from smrpgpatchbuilder.datatypes.spells.classes import Spell

# Constants for name normalization
NAME_KEEP = {"-", "_"}
RE_SPACES = re.compile(r"[ \-_]+")
RE_LEADING_DIGITS = re.compile(r"^\d+")
RE_HEX = re.compile(r"^[0-9A-Fa-f]+$")
RE_FLAG_DIGIT = re.compile(r"^[0-9]$")

def normalize_label(raw: str) -> str:
    """Normalize a raw label string into a valid Python identifier.

    Args:
        raw: The raw label string to normalize

    Returns:
        A normalized label suitable for use as a Python identifier
    """
    s = RE_LEADING_DIGITS.sub("", raw)
    s = s.upper()
    keep = set(NAME_KEEP)
    trans_table = {ord(ch): None for ch in string.punctuation if ch not in keep}
    s = s.translate(trans_table)
    s = RE_SPACES.sub("_", s)
    s = s.strip("_ ")
    if s and s[0].isdigit():
        s = "_" + s
    return s or "_"

def parse_standard_lines(lines: list[str]) -> list[tuple[str, str]]:
    """Parse standard input file lines into (name, index) tuples.

    Args:
        lines: Lines from the input file

    Returns:
        List of (normalized_name, index) tuples
    """
    out = []
    for idx, raw in enumerate(lines):
        line = raw.rstrip("\n\r")
        if not line.strip():
            continue
        if line.strip().startswith("#"):
            continue
        name = normalize_label(line)
        out.append((name, str(idx)))
    return out

def parse_variable_names_lines(lines: list[str]) -> list[tuple[str, str]]:
    """Parse variable_names.input lines into (name, value) tuples.

    Handles special formats for flags and variables:
    - Lines ending with hex and digit: Flag(0xHEX, digit)
    - Lines ending with hex in 0x7000-0x703E, 0x71A0-0x71FE: ShortVar(0xHEX)
    - Lines ending with hex in 0x7040-0x719F: ByteVar(0xHEX)
    - Lines ending with other hex: 0xHEX
    - Lines without hex: 0

    Args:
        lines: Lines from the variable_names.input file

    Returns:
        List of (normalized_name, value_expression) tuples
    """
    out = []
    for raw in lines:
        line = raw.rstrip("\n\r")
        if not line.strip() or line.strip().startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2 and RE_FLAG_DIGIT.match(parts[-1]) and RE_HEX.match(parts[-2]):
            hex_str = parts[-2]
            digit = parts[-1]
            label_raw = " ".join(parts[:-2])
            label = normalize_label(label_raw)
            hex_val = int(hex_str, 16)
            out.append((label, f"Flag(0x{hex_val:04X}, {digit})"))
        elif parts and RE_HEX.match(parts[-1]):
            hex_str = parts[-1]
            label_raw = " ".join(parts[:-1])
            label = normalize_label(label_raw)
            hex_val = int(hex_str, 16)
            if 0x7000 <= hex_val <= 0x703E or 0x71A0 <= hex_val <= 0x71FE:
                out.append((label, f"ShortVar(0x{hex_val:04X})"))
            elif 0x7040 <= hex_val <= 0x719F:
                out.append((label, f"ByteVar(0x{hex_val:04X})"))
            else:
                out.append((label, f"0x{hex_val:04X}"))
        else:
            label = normalize_label(line)
            out.append((label, "0"))
    return out

def find_config_dir(start_path: Path | None = None) -> Path | None:
    """Find the config directory by searching up the directory tree.

    Args:
        start_path: Starting path for the search. If None, uses __file__.

    Returns:
        Path to the config directory, or None if not found
    """
    if start_path is None:
        start_path = Path(__file__)

    for p in start_path.resolve().parents:
        cand = p / "config"
        if cand.is_dir():
            return cand
    return None

def parse_input_files(config_dir: Path | None = None) -> dict[str, list[tuple[str, str]]]:
    """Parse all *_names.input files in the config directory.

    Args:
        config_dir: Path to the config directory. If None, will search for it.

    Returns:
        Dictionary mapping file stem (without .input extension) to list of (name, value) tuples

    Raises:
        ValueError: If config directory is not found or contains no input files
    """
    if config_dir is None:
        config_dir = find_config_dir()

    if config_dir is None:
        raise ValueError("Could not find a config directory")

    files = sorted(config_dir.glob("*_names.input"))
    # Also include item_prefixes.input
    prefix_file = config_dir / "item_prefixes.input"
    if prefix_file.exists():
        files.append(prefix_file)

    if not files:
        raise ValueError("No input files found in config directory")

    parsed = {}

    for f in files:
        key = f.stem  # e.g., variable_names, item_prefixes
        content = f.read_text(encoding="utf-8").splitlines()
        if f.name == "variable_names.input" or key == "variable_names":
            parsed[key] = parse_variable_names_lines(content)
        else:
            parsed[key] = parse_standard_lines(content)

    return parsed

def load_arrays_from_input_files() -> dict[str, list[str]]:
    """load sound, effect, screen effect, and music arrays from .input files.

    returns:
        dictionary with keys 'sounds', 'effects', 'screen_effects', 'music'
    """
    config_dir = Path(__file__).resolve().parents[4] / "config"

    # load the input files
    parsed = parse_input_files(config_dir)

    # build arrays from parsed data
    result = {}

    if "action_script_names" in parsed:
        action_scripts = [""] * 1024
        for name, idx in parsed["action_script_names"]:
            action_scripts[int(idx)] = name
        result["action_scripts"] = action_scripts
    else:
        result["action_scripts"] = [""] * 1024

    if "battle_effect_names" in parsed:
        effects = [""] * 128
        for name, idx in parsed["battle_effect_names"]:
            effects[int(idx)] = name
        result["effects"] = effects
    else:
        result["effects"] = [""] * 128

    if "battle_event_names" in parsed:
        events = [""] * 103
        for name, idx in parsed["battle_event_names"]:
            events[int(idx)] = name
        result["events"] = events
    else:
        result["events"] = [""] * 103

    if "battle_sfx_names" in parsed:
        sounds = [""] * 211
        for name, idx in parsed["battle_sfx_names"]:
            sounds[int(idx)] = name
        result["sounds"] = sounds
    else:
        result["sounds"] = [""] * 211

    if "battle_variable_names" in parsed:
        battle_vars = [""] * 16
        for name, idx in parsed["battle_variable_names"]:
            battle_vars[int(idx)] = name
        result["battle_vars"] = battle_vars

    if "battlefield_names" in parsed:
        battlefields = [""] * 64
        for name, idx in parsed["battlefield_names"]:
            battlefields[int(idx)] = name
        result["battlefields"] = battlefields
    else:
        result["battlefields"] = [""] * 64

    if "dialog_names" in parsed:
        dialogs = [""] * 4096
        for name, idx in parsed["dialog_names"]:
            dialogs[int(idx)] = name
        result["dialogs"] = dialogs
    else:
        result["dialogs"] = [""] * 4096

    if "event_script_names" in parsed:
        event_scripts = [""] * 4096
        for name, idx in parsed["event_script_names"]:
            event_scripts[int(idx)] = name
        result["event_scripts"] = event_scripts
    else:
        result["event_scripts"] = [""] * 4096

    if "formation_names" in parsed:
        formations = [""] * 512
        for name, idx in parsed["formation_names"]:
            formations[int(idx)] = name
        result["formations"] = formations
    else:
        result["formations"] = [""] * 512

    if "music_names" in parsed:
        music = [""] * 74
        for name, idx in parsed["music_names"]:
            music[int(idx)] = name
        result["music"] = music
    else:
        result["music"] = [""] * 74

    if "overworld_area_names" in parsed:
        areas = [""] * 56
        for name, idx in parsed["overworld_area_names"]:
            areas[int(idx)] = name
        result["areas"] = areas
    else:
        result["areas"] = [""] * 56

    if "overworld_sfx_names" in parsed:
        overworld_sfx = [""] * 256
        for name, idx in parsed["overworld_sfx_names"]:
            overworld_sfx[int(idx)] = name
        result["overworld_sfx"] = overworld_sfx
    else:
        result["overworld_sfx"] = [""] * 256

    if "pack_names" in parsed:
        packs = [""] * 256
        for name, idx in parsed["pack_names"]:
            packs[int(idx)] = name
        result["packs"] = packs
    else:
        result["packs"] = [""] * 256

    if "packet_names" in parsed:
        packets = [""] * 256
        for name, idx in parsed["packet_names"]:
            packets[int(idx)] = name
        result["packets"] = packets
    else:
        result["packets"] = [""] * 256

    if "room_names" in parsed:
        rooms = [""] * 510
        for name, idx in parsed["room_names"]:
            rooms[int(idx)] = name
        result["rooms"] = rooms
    else:
        result["rooms"] = [""] * 510

    if "screen_effect_names" in parsed:
        screen_effects = [""] * 21
        for name, idx in parsed["screen_effect_names"]:
            screen_effects[int(idx)] = name
        result["screen_effects"] = screen_effects
    else:
        result["screen_effects"] = [""] * 21

    if "shop_names" in parsed:
        shops = [""] * 33
        for name, idx in parsed["shop_names"]:
            shops[int(idx)] = name
        result["shops"] = shops
    else:
        result["shops"] = [""] * 33

    if "sprite_names" in parsed:
        sprites = [""] * 1024
        for name, idx in parsed["sprite_names"]:
            sprites[int(idx)] = name
        result["sprites"] = sprites
    else:
        result["sprites"] = [""] * 1024

    return result

def load_variables_from_input_files() -> dict[int, str]:
    config_dir = Path(__file__).resolve().parents[4] / "config"

    # load the input files
    parsed = parse_input_files(config_dir)

    # build arrays from parsed data
    result = {}
    # Parse variable_names into lookup dictionaries
    if "variable_names" in parsed:
        # Create lookup dictionaries for variables

        for name, value_expr in parsed["variable_names"]:
            # Parse the value expression to determine type
            if value_expr.startswith("ShortVar(") or value_expr.startswith("ByteVar("):
                # Extract hex from "ShortVar(0xHEX)" or "ByteVar(0xHEX)"
                import re
                match = re.match(r"(?:ShortVar|ByteVar)\(0x([0-9A-Fa-f]+)\)", value_expr)
                if match:
                    hex_val = int(match.group(1), 16)
                    result[hex_val] = name
            elif value_expr.startswith("0x"):
                # Plain hex value
                hex_val = int(value_expr, 16)
                result[hex_val] = name

    return result

def load_flags_from_input_files() -> dict[tuple[int, int], str]:
    config_dir = Path(__file__).resolve().parents[4] / "config"

    # load the input files
    parsed = parse_input_files(config_dir)

    # build arrays from parsed data
    result = {}
    # Parse variable_names into lookup dictionaries
    if "variable_names" in parsed:
        # Create lookup dictionaries for variables

        for name, value_expr in parsed["variable_names"]:
            # Parse the value expression to determine type
            if value_expr.startswith("Flag("):
                # Extract hex and bit from "Flag(0xHEX, bit)"
                import re
                match = re.match(r"Flag\(0x([0-9A-Fa-f]+),\s*(\d+)\)", value_expr)
                if match:
                    hex_val = int(match.group(1), 16)
                    bit = int(match.group(2))
                    result[(hex_val, bit)] = name

    return result

def load_class_names_from_config() -> dict[str, list[str]]:
    """Load class name lists from disassembler_output files.

    Returns:
        dict with keys for each type of class names needed, sorted by _index/_item_id ascending
    """
    import inspect
    import importlib.util
    import sys

    result = {
        "ally_spells": [],
        "monster_spells": [],
        "all_spells": [],
        "monster_attacks": [],
        "items": [],
        "weapons": [],
        "weapon_misses": [],
        "weapon_sounds": [],
        "all_items": [],
        "enemies": [],
    }

    # Get path to disassembler_output directory (4 levels up from this file, then into src/disassembler_output)
    disassembler_output_dir = Path(__file__).resolve().parents[4] / "src" / "disassembler_output"

    # Load spells.py for ally_spells and monster_spells
    spells_file = disassembler_output_dir / "spells" / "spells.py"
    if spells_file.exists():
        spec = importlib.util.spec_from_file_location("disassembler_output.spells.spells", spells_file)
        if spec and spec.loader:
            spells_module = importlib.util.module_from_spec(spec)
            sys.modules["disassembler_output.spells.spells"] = spells_module
            spec.loader.exec_module(spells_module)

            # Get CharacterSpell and EnemySpell base classes
            CharacterSpellc = getattr(spells_module, "CharacterSpell", None)
            EnemySpellc = getattr(spells_module, "EnemySpell", None)

            # Collect CharacterSpell subclasses with their indices
            ally_spells_with_index = []
            all_spells_with_index = []
            monster_spells_with_index = []

            for name, obj in inspect.getmembers(spells_module, inspect.isclass):
                if not issubclass(obj, Spell):
                    continue
                index = obj._index
                if CharacterSpellc and obj != CharacterSpellc and issubclass(obj, CharacterSpellc):
                    index = getattr(obj, '_index', 9999)
                    ally_spells_with_index.append((index, name))
                    all_spells_with_index.append((index, name))
                if EnemySpellc and obj != EnemySpellc and issubclass(obj, EnemySpellc):
                    index = obj._index
                    monster_spells_with_index.append((index, name))
                    all_spells_with_index.append((index, name))

            # Sort by index and extract names
            result["ally_spells"] = [name for _, name in sorted(ally_spells_with_index)]

            # Sort by index and extract names
            result["monster_spells"] = [name for _, name in sorted(monster_spells_with_index)]

            result["all_spells"] = [name for _, name in sorted(all_spells_with_index)]

    # Load items.py for items and weapons
    items_file = disassembler_output_dir / "items" / "items.py"
    if items_file.exists():
        spec = importlib.util.spec_from_file_location("disassembler_output.items.items", items_file)
        if spec and spec.loader:
            items_module = importlib.util.module_from_spec(spec)
            sys.modules["disassembler_output.items.items"] = items_module
            spec.loader.exec_module(items_module)

            # Get Weapon base class
            Weapon = getattr(items_module, "Weapon", None)

            # Collect items with their indices
            all_items_with_index = []
            items_with_index = []
            weapons_with_index = []

            # Find all classes with _item_id attribute
            for name, obj in inspect.getmembers(items_module, inspect.isclass):
                if hasattr(obj, '_item_id') and obj.__module__ == items_module.__name__:
                    index = obj._item_id

                    all_items_with_index.append((index, name))

                    # Items with index 96+
                    if index >= 96:
                        items_with_index.append((index, name))

                    # Weapon subclasses
                    if Weapon and obj != Weapon and issubclass(obj, Weapon):
                        weapons_with_index.append((index, name))

            # Sort by index and extract names
            result["all_items"] = [name for _, name in sorted(all_items_with_index)]
            result["items"] = [name for _, name in sorted(items_with_index)]
            result["weapons"] = [name for _, name in sorted(weapons_with_index)]
            result["weapon_misses"] = [name for _, name in sorted(weapons_with_index)]
            result["weapon_sounds"] = [name for _, name in sorted(weapons_with_index)]

    # Load attacks.py for monster_attacks
    attacks_file = disassembler_output_dir / "enemy_attacks" / "attacks.py"
    if attacks_file.exists():
        spec = importlib.util.spec_from_file_location("disassembler_output.enemy_attacks.attacks", attacks_file)
        if spec and spec.loader:
            attacks_module = importlib.util.module_from_spec(spec)
            sys.modules["disassembler_output.enemy_attacks.attacks"] = attacks_module
            spec.loader.exec_module(attacks_module)

            # Get EnemyAttack base class
            EnemyAttack = getattr(attacks_module, "EnemyAttack", None)

            # Collect EnemyAttack subclasses with their indices
            attacks_with_index = []
            for name, obj in inspect.getmembers(attacks_module, inspect.isclass):
                if EnemyAttack and obj != EnemyAttack and issubclass(obj, EnemyAttack):
                    index = getattr(obj, '_index', 9999)
                    attacks_with_index.append((index, name))

            # Sort by index and extract names
            result["monster_attacks"] = [name for _, name in sorted(attacks_with_index)]

    # Load enemies.py for enemies
    enemies_file = disassembler_output_dir / "enemies" / "enemies.py"
    if enemies_file.exists():
        spec = importlib.util.spec_from_file_location("disassembler_output.enemies.enemies", enemies_file)
        if spec and spec.loader:
            enemies_module = importlib.util.module_from_spec(spec)
            sys.modules["disassembler_output.enemies.enemies"] = enemies_module
            spec.loader.exec_module(enemies_module)

            # Get Enemy base class
            Enemy = getattr(enemies_module, "Enemy", None)

            # Collect Enemy subclasses with their monster_ids
            enemies_with_index = []
            for name, obj in inspect.getmembers(enemies_module, inspect.isclass):
                if Enemy and obj != Enemy and issubclass(obj, Enemy):
                    monster_id = getattr(obj, '_monster_id', 9999)
                    enemies_with_index.append((monster_id, name))

            # Sort by monster_id and extract names
            result["enemies"] = [name for _, name in sorted(enemies_with_index)]

    return result

