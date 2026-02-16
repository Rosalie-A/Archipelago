"""Disassembler for ROM's PackCollection (formation packs).

This disassembler reads the formation pack data from a Super Mario RPG ROM
and outputs Python files containing formations and packs as separate declarations.

Usage:
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py packdisassembler --rom "/path/to/your/smrpg/rom"

This will produce:
    ./src/disassembler_output/packs/pack_collection.py
    ./src/disassembler_output/variables/formation_names.py

Prerequisites:
    - Enemy classes must be disassembled first (enemydisassembler)
    - Variable names should be parsed (variableparser)

The output file will contain:
    - Formation declarations with IDs (FORM0000 = Formation(id=0, ...))
    - FormationPack definitions referencing formations by name
    - A PackCollection instance containing all packs

Note:
    - Music is output as Music class instances (NormalBattleMusic(), MidbossMusic(), etc.)
      rather than BattleMusic enum values
    - Both Music instances and BattleMusic enum values are accepted by Formation
"""

import os
import shutil
from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import shortify, writeline
from .input_file_parser import load_arrays_from_input_files, load_class_names_from_config
from smrpgpatchbuilder.datatypes.battles.ids.misc import (
    PACK_BASE_ADDRESS,
    BASE_FORMATION_ADDRESS,
    BASE_FORMATION_META_ADDRESS,
    TOTAL_PACKS,
    TOTAL_FORMATIONS,
)

class Command(BaseCommand):
    help = "Disassembles formation packs from a ROM file"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom", required=True)

    def handle(self, *args, **options):
        # Load variable names and class names from disassembler output
        varnames = load_arrays_from_input_files()
        classnames = load_class_names_from_config()

        # Get enemy class names
        ENEMIES = classnames["enemies"]

        # Get pack names from variable output
        PACK_NAMES = varnames.get("packs", [])

        # Get formation names from variable output (if available)
        FORMATION_NAMES = varnames.get("formations", [])

        # Load ROM
        rom = bytearray(open(options["rom"], "rb").read())

        # Create output directory
        output_path = "./src/disassembler_output/packs"
        shutil.rmtree(output_path, ignore_errors=True)
        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w").close()

        # First, disassemble all formations
        formations_data = []
        for formation_id in range(TOTAL_FORMATIONS):
            formation_data = self.read_formation(rom, formation_id, ENEMIES)
            formations_data.append(formation_data)

        # Then, disassemble all packs
        packs_data = []
        for pack_id in range(256):  # Only 256 packs (0-255)
            pack_data = self.read_pack(rom, pack_id)
            packs_data.append(pack_data)

        # Determine which formations are actually used by packs
        used_formation_ids = set()
        for pack in packs_data:
            used_formation_ids.update(pack['formations'])

        # Generate formation variable names
        formation_var_names = self.generate_formation_var_names(formations_data, FORMATION_NAMES)

        # Generate the formation_names.py file
        self.generate_formation_names_file(formation_var_names, used_formation_ids)

        # Generate the output file
        self.generate_output_file(output_path, packs_data, formations_data, PACK_NAMES, formation_var_names, used_formation_ids)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully disassembled {len(packs_data)} packs and {len(used_formation_ids)} formations to {output_path}/"
            )
        )

    def generate_formation_var_names(self, formations_data, formation_names):
        """Generate variable names for all formations."""
        var_names = []
        for i, formation in enumerate(formations_data):
            # Check if we have a descriptive name
            if i < len(formation_names) and formation_names[i]:
                # Clean the name for use as a Python identifier
                clean_name = self._normalize_name(formation_names[i])
                var_name = f"FORM{i:04d}_{clean_name}"
            else:
                var_name = f"FORM{i:04d}"
            var_names.append(var_name)
        return var_names

    def _normalize_name(self, name):
        """Normalize a name to be a valid Python identifier part."""
        # Convert to uppercase, replace spaces/hyphens with underscores
        result = name.upper().replace(" ", "_").replace("-", "_")
        # Remove any characters that aren't alphanumeric or underscore
        result = ''.join(c for c in result if c.isalnum() or c == '_')
        # Remove consecutive underscores
        while '__' in result:
            result = result.replace('__', '_')
        # Strip leading/trailing underscores
        result = result.strip('_')
        return result

    def generate_formation_names_file(self, formation_var_names, used_formation_ids):
        """Generate the formation_names.py file in variables output."""
        output_path = "./src/disassembler_output/variables"
        os.makedirs(output_path, exist_ok=True)

        file_path = f"{output_path}/formation_names.py"
        with open(file_path, "w") as f:
            writeline(f, '"""Formation name constants for use with formations and packs."""')
            writeline(f, "")
            writeline(f, "# Formation IDs - only formations used by packs are included")
            writeline(f, "")

            for i, var_name in enumerate(formation_var_names):
                if i in used_formation_ids:
                    writeline(f, f"{var_name} = {i}")

    def read_formation(self, rom, formation_id, enemies):
        """Read a single formation from ROM."""
        # Read formation data (26 bytes)
        base_addr = BASE_FORMATION_ADDRESS + (formation_id * 26)
        data = rom[base_addr:base_addr + 26]

        # Read formation metadata (3 bytes)
        meta_addr = BASE_FORMATION_META_ADDRESS + (formation_id * 3)
        meta_data = rom[meta_addr:meta_addr + 3]

        # Parse monsters present bitmap (1 byte)
        monsters_present = data[0]

        # Parse monsters hidden bitmap (1 byte)
        monsters_hidden = data[1]

        # Parse member data (8 members * 3 bytes each = 24 bytes)
        members = []
        for i in range(8):
            offset = 2 + (i * 3)
            enemy_index = data[offset]
            x_pos = data[offset + 1]
            y_pos = data[offset + 2]

            # Check if this member is present
            is_present = (monsters_present & (1 << (7 - i))) != 0
            is_hidden = (monsters_hidden & (1 << (7 - i))) != 0

            if is_present:
                members.append({
                    'enemy': enemies[enemy_index] if enemy_index < len(enemies) else f"ENEMY_{enemy_index}",
                    'x_pos': x_pos,
                    'y_pos': y_pos,
                    'hidden_at_start': is_hidden,
                })
            else:
                members.append(None)

        # Parse metadata
        unknown_byte = meta_data[0]
        run_event = meta_data[1]
        music_byte = meta_data[2]

        # Parse music_byte
        # Bit 0: music bit 0
        # Bit 1: cannot run away
        # Bit 2-7: music bits 1-6 and unknown bit
        music_value = 8 if (music_byte & 0xC0 == 0xC0) else (music_byte >> 2)
        can_run_away = (music_byte & 0x02) == 0
        unknown_bit: bool = (music_byte & 0x01) == 0x01

        # Map music value to Music class instances
        music_map = {
            0: "NormalBattleMusic()",
            1: "MidbossMusic()",
            2: "BossMusic()",
            3: "Smithy1Music()",
            4: "CorndillyMusic()",
            5: "BoosterHillMusic()",
            6: "VolcanoMusic()",
            7: "CulexMusic()",
        }
        music_str = music_map.get(music_value, "None")

        return {
            'id': formation_id,
            'members': members,
            'run_event': run_event if run_event != 0xFF else None,
            'music': music_str,
            'can_run_away': can_run_away,
            'unknown_byte': unknown_byte,
            'unknown_bit': unknown_bit,
        }

    def read_pack(self, rom, pack_id):
        """Read a single pack from ROM."""
        base_addr = PACK_BASE_ADDRESS + (pack_id * 4)
        data = rom[base_addr:base_addr + 4]

        formation_1 = data[0]
        formation_2 = data[1]
        formation_3 = data[2]
        hi_bank = data[3]
        if (hi_bank & 0x01 == 0x01):
           formation_1 += 0x100
        if (hi_bank & 0x02 == 0x02):
           formation_2 += 0x100
        if (hi_bank & 0x04 == 0x04):
           formation_3 += 0x100

        return {
            'id': pack_id,
            'formations': [formation_1, formation_2, formation_3]
        }

    def generate_output_file(self, output_path, packs_data, formations_data, pack_names, formation_var_names, used_formation_ids):
        """Generate the Python file with formations and PackCollection."""
        file_path = f"{output_path}/pack_collection.py"

        with open(file_path, "w") as f:
            # Write imports
            writeline(f, '"""ROM\'s PackCollection disassembled from the original game."""')
            writeline(f, "")
            writeline(f, "from smrpgpatchbuilder.datatypes.battles.formations_packs.types.classes import (")
            writeline(f, "    Formation,")
            writeline(f, "    FormationMember,")
            writeline(f, "    FormationPack,")
            writeline(f, "    PackCollection,")
            writeline(f, ")")
            writeline(f, "from smrpgpatchbuilder.datatypes.battles.music import (")
            writeline(f, "    NormalBattleMusic,")
            writeline(f, "    MidbossMusic,")
            writeline(f, "    BossMusic,")
            writeline(f, "    Smithy1Music,")
            writeline(f, "    CorndillyMusic,")
            writeline(f, "    BoosterHillMusic,")
            writeline(f, "    VolcanoMusic,")
            writeline(f, "    CulexMusic,")
            writeline(f, ")")
            writeline(f, "from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types import Battlefield")
            writeline(f, "from ..enemies.enemies import *")
            writeline(f, "from ..variables.pack_names import *")
            writeline(f, "from ..variables.formation_names import *")
            writeline(f, "")
            writeline(f, "")

            # Write formation declarations
            writeline(f, "# ============================================================================")
            writeline(f, "# Formation Declarations")
            writeline(f, "# ============================================================================")
            writeline(f, "")

            for formation_id in sorted(used_formation_ids):
                formation = formations_data[formation_id]
                var_name = formation_var_names[formation_id]
                self.write_formation_declaration(f, formation, var_name)
                writeline(f, "")

            writeline(f, "")
            writeline(f, "# ============================================================================")
            writeline(f, "# Pack Definitions")
            writeline(f, "# ============================================================================")
            writeline(f, "")

            writeline(f, "# Initialize packs array with None values")
            writeline(f, "packs: list[FormationPack] = [None] * 256  # type: ignore")
            writeline(f, "")

            # Generate pack definitions referencing formations by name
            for pack in packs_data:
                self.write_pack_definition(f, pack, formation_var_names, pack_names)

            writeline(f, "")
            writeline(f, "# Pack Collection")
            writeline(f, "pack_collection = PackCollection(packs[:256])")

    def write_formation_declaration(self, f, formation, var_name):
        """Write a formation declaration with its ID."""
        writeline(f, f"{var_name} = Formation(")
        writeline(f, f"    id={formation['id']},")
        writeline(f, "    members=[")

        # Find the last non-None member
        last_member_index = -1
        for i in range(len(formation['members']) - 1, -1, -1):
            if formation['members'][i] is not None:
                last_member_index = i
                break

        # Only write members up to the last non-None member
        for i, member in enumerate(formation['members']):
            if i > last_member_index:
                break

            if member is None:
                writeline(f, "        None,")
            else:
                enemy = member['enemy']
                x = member['x_pos']
                y = member['y_pos']
                hidden = member['hidden_at_start']

                if hidden:
                    writeline(f, f"        FormationMember({enemy}, {x}, {y}, hidden_at_start=True),")
                else:
                    writeline(f, f"        FormationMember({enemy}, {x}, {y}),")

        writeline(f, "    ],")

        if formation['run_event'] is not None:
            writeline(f, f"    run_event_at_load={formation['run_event']},")

        writeline(f, f"    music={formation['music']},")

        if not formation['can_run_away']:
            writeline(f, "    can_run_away=False,")

        if formation['unknown_byte'] != 0:
            writeline(f, f"    unknown_byte={formation['unknown_byte']},")

        if formation['unknown_bit'] != 0:
            writeline(f, f"    unknown_bit={formation['unknown_bit']},")

        writeline(f, ")")

    def write_pack_definition(self, f, pack, formation_var_names, pack_names):
        """Write a pack definition referencing formations by name."""
        pack_id = pack['id']
        formation_ids = pack['formations']

        # Get pack name from pack_names array, or use generic name
        pack_name = pack_names[pack_id] if pack_id < len(pack_names) and pack_names[pack_id] else f"PACK_{pack_id}"

        # Get formation variable names
        form_names = [formation_var_names[fid] for fid in formation_ids]

        # Check if all three formations are the same
        if formation_ids[0] == formation_ids[1] == formation_ids[2]:
            writeline(f, f"packs[{pack_name}] = FormationPack({form_names[0]})")
        else:
            writeline(f, f"packs[{pack_name}] = FormationPack({form_names[0]}, {form_names[1]}, {form_names[2]})")
