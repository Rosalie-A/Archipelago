"""Disassembler for world map locations.

This disassembler reads world map location data from a Super Mario RPG ROM and outputs a Python file
containing all 56 world map locations with their coordinates, flags, and navigation data.

Usage:
    PYTHONPATH=src python src/smrpgpatchbuilder/manage.py worldmaplocationdisassembler --rom "/path/to/your/smrpg/rom"

This will produce:
    ./src/disassembler_output/world_map_locations/world_map_locations.py

Prerequisites:
    - Variable names should be parsed (variableparser)
    - Overworld area names should be parsed

The output file will contain:
    - A world_map_locations array of size 56
    - Each location assigned to its index using overworld_area_names variables
    - A WorldMapLocationCollection instance initialized with the array
"""

import os
import shutil
from django.core.management.base import BaseCommand
from smrpgpatchbuilder.utils.disassembler_common import writeline
from .input_file_parser import load_arrays_from_input_files
from smrpgpatchbuilder.datatypes.world_map_locations.classes import (
    WORLD_MAP_LOCATION_BASE_ADDRESS,
    WORLD_MAP_NAME_POINTER_BASE_ADDRESS,
    WORLD_MAP_NAME_DATA_BASE_ADDRESS,
    TOTAL_WORLD_MAP_LOCATIONS,
)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.types.flag import Flag

class Command(BaseCommand):
    help = "Disassembles world map locations from a ROM file"

    def add_arguments(self, parser):
        parser.add_argument("-r", "--rom", dest="rom", help="Path to a Mario RPG rom", required=True)

    def handle(self, *args, **options):
        # Load variable names from disassembler output
        varnames = load_arrays_from_input_files()

        # Get overworld area names
        AREA_NAMES = varnames.get("areas", [])

        # Get event script names
        EVENT_SCRIPT_NAMES = varnames.get("event_scripts", [])

        # Get all Flag variables for lookup
        FLAG_VARS = self.load_flag_variables()

        # Load ROM
        rom = bytearray(open(options["rom"], "rb").read())

        # Create output directory
        output_path = "./src/disassembler_output/world_map_locations"
        shutil.rmtree(output_path, ignore_errors=True)
        os.makedirs(output_path, exist_ok=True)
        open(f"{output_path}/__init__.py", "w").close()

        # Disassemble all world map locations
        locations_data = []
        for location_id in range(TOTAL_WORLD_MAP_LOCATIONS):
            location_data = self.read_location(rom, location_id, FLAG_VARS, EVENT_SCRIPT_NAMES)
            locations_data.append(location_data)

        # Generate the output file
        self.generate_output_file(output_path, locations_data, AREA_NAMES)

        self.stdout.write(
            self.style.SUCCESS(
                f"Successfully disassembled {len(locations_data)} world map locations to {output_path}/"
            )
        )

    def load_flag_variables(self):
        """Load all Flag variables from variable_names.py for lookup."""
        try:
            # Import the variable_names module
            import importlib
            module = importlib.import_module("disassembler_output.variables.variable_names")

            # Find all Flag variables
            flag_vars = {}
            for name in dir(module):
                obj = getattr(module, name)
                if isinstance(obj, Flag):
                    flag_vars[(obj.byte, obj.bit)] = name

            return flag_vars
        except Exception:
            # If we can't load the module, return empty dict
            return {}

    def get_flag_name(self, flag_vars, flag):
        """Get the variable name for a Flag, or return the Flag constructor if not found."""
        if flag is None:
            return None
        key = (flag.byte, flag.bit)
        if key in flag_vars:
            return flag_vars[key]
        else:
            return f"Flag(0x{flag.byte:04X}, {flag.bit})"

    def read_location(self, rom, location_id, flag_vars, event_script_names):
        """Read a single world map location from ROM."""
        offset = WORLD_MAP_LOCATION_BASE_ADDRESS + (location_id * 16)

        # Byte 0: X coordinate
        x = rom[offset]
        offset += 1

        # Byte 1: Y coordinate
        y = rom[offset]
        offset += 1

        # Bytes 2-3: Show check flag (packed as 9-bit address + 3-bit bit index)
        show_check_raw = rom[offset] | ((rom[offset + 1] & 0x01) << 8)
        show_check_bit = show_check_raw & 0x07
        show_check_address = ((show_check_raw >> 3) & 0x1FF) + 0x7045
        show_check_flag = Flag(show_check_address, show_check_bit)
        show_check_flag_name = self.get_flag_name(flag_vars, show_check_flag)

        # Byte 3 bit 6: go_location flag
        go_location = (rom[offset + 1] & 0x40) == 0x40
        offset += 2

        # Bytes 4-7: Either event (2 bytes) + padding or location data (4 bytes)
        run_event = None
        which_location_check_flag_name = None
        go_location_a = None
        go_location_b = None

        if not go_location:
            # Run event mode
            run_event_id = rom[offset] | (rom[offset + 1] << 8)
            # Look up event script name
            if run_event_id < len(event_script_names) and event_script_names[run_event_id]:
                run_event = event_script_names[run_event_id]
            else:
                run_event = f"0x{run_event_id:04X}"
            offset += 4
        else:
            # Go location mode
            which_loc_raw = rom[offset] | ((rom[offset + 1] & 0x01) << 8)
            which_loc_bit = which_loc_raw & 0x07
            which_loc_address = ((which_loc_raw >> 3) & 0x1FF) + 0x7045
            which_location_check_flag = Flag(which_loc_address, which_loc_bit)
            which_location_check_flag_name = self.get_flag_name(flag_vars, which_location_check_flag)
            offset += 2
            go_location_a = rom[offset]
            offset += 1
            go_location_b = rom[offset]
            offset += 1

        # Bytes 8-9: East direction
        enabled_to_east = False
        check_flag_to_east_name = None
        location_to_east = None
        if rom[offset] != 0xFF or rom[offset + 1] != 0xFF:
            enabled_to_east = True
            east_check_raw = rom[offset] | ((rom[offset + 1] & 0x01) << 8)
            east_check_bit = east_check_raw & 0x07
            east_check_address = ((east_check_raw >> 3) & 0x1FF) + 0x7045
            check_flag_to_east = Flag(east_check_address, east_check_bit)
            check_flag_to_east_name = self.get_flag_name(flag_vars, check_flag_to_east)
            location_to_east = rom[offset + 1] >> 1
        offset += 2

        # Bytes 10-11: South direction
        enabled_to_south = False
        check_flag_to_south_name = None
        location_to_south = None
        if rom[offset] != 0xFF or rom[offset + 1] != 0xFF:
            enabled_to_south = True
            south_check_raw = rom[offset] | ((rom[offset + 1] & 0x01) << 8)
            south_check_bit = south_check_raw & 0x07
            south_check_address = ((south_check_raw >> 3) & 0x1FF) + 0x7045
            check_flag_to_south = Flag(south_check_address, south_check_bit)
            check_flag_to_south_name = self.get_flag_name(flag_vars, check_flag_to_south)
            location_to_south = rom[offset + 1] >> 1
        offset += 2

        # Bytes 12-13: West direction
        enabled_to_west = False
        check_flag_to_west_name = None
        location_to_west = None
        if rom[offset] != 0xFF or rom[offset + 1] != 0xFF:
            enabled_to_west = True
            west_check_raw = rom[offset] | ((rom[offset + 1] & 0x01) << 8)
            west_check_bit = west_check_raw & 0x07
            west_check_address = ((west_check_raw >> 3) & 0x1FF) + 0x7045
            check_flag_to_west = Flag(west_check_address, west_check_bit)
            check_flag_to_west_name = self.get_flag_name(flag_vars, check_flag_to_west)
            location_to_west = rom[offset + 1] >> 1
        offset += 2

        # Bytes 14-15: North direction
        enabled_to_north = False
        check_flag_to_north_name = None
        location_to_north = None
        if rom[offset] != 0xFF or rom[offset + 1] != 0xFF:
            enabled_to_north = True
            north_check_raw = rom[offset] | ((rom[offset + 1] & 0x01) << 8)
            north_check_bit = north_check_raw & 0x07
            north_check_address = ((north_check_raw >> 3) & 0x1FF) + 0x7045
            check_flag_to_north = Flag(north_check_address, north_check_bit)
            check_flag_to_north_name = self.get_flag_name(flag_vars, check_flag_to_north)
            location_to_north = rom[offset + 1] >> 1

        # Read location name from name table
        name_pointer = rom[WORLD_MAP_NAME_POINTER_BASE_ADDRESS + (location_id * 2)] | \
                      (rom[WORLD_MAP_NAME_POINTER_BASE_ADDRESS + (location_id * 2) + 1] << 8)
        name_offset = WORLD_MAP_NAME_DATA_BASE_ADDRESS + name_pointer
        name_chars = []
        while rom[name_offset] != 0x06 and rom[name_offset] != 0x00:
            name_chars.append(chr(rom[name_offset]))
            name_offset += 1
        name = ''.join(name_chars)

        return {
            'id': location_id,
            'name': name,
            'x': x,
            'y': y,
            'show_check_flag': show_check_flag_name,
            'go_location': go_location,
            'run_event': run_event,
            'which_location_check_flag': which_location_check_flag_name,
            'go_location_a': go_location_a,
            'go_location_b': go_location_b,
            'enabled_to_east': enabled_to_east,
            'enabled_to_south': enabled_to_south,
            'enabled_to_west': enabled_to_west,
            'enabled_to_north': enabled_to_north,
            'check_flag_to_east': check_flag_to_east_name,
            'check_flag_to_south': check_flag_to_south_name,
            'check_flag_to_west': check_flag_to_west_name,
            'check_flag_to_north': check_flag_to_north_name,
            'location_to_east': location_to_east,
            'location_to_south': location_to_south,
            'location_to_west': location_to_west,
            'location_to_north': location_to_north,
        }

    def generate_output_file(self, output_path, locations_data, area_names):
        """Generate the Python file with world map location data."""
        file_path = f"{output_path}/world_map_locations.py"

        with open(file_path, "w") as f:
            # Write imports
            writeline(f, "from smrpgpatchbuilder.datatypes.world_map_locations.classes import (")
            writeline(f, "    WorldMapLocation,")
            writeline(f, "    WorldMapLocationCollection,")
            writeline(f, ")")
            writeline(f, "from ..variables.variable_names import *")
            writeline(f, "from ..variables.overworld_area_names import *")
            writeline(f, "from ..variables.event_script_names import *")
            writeline(f, "")
            writeline(f, "")

            writeline(f, "world_map_locations: list[WorldMapLocation] = [None] * 56 # type: ignore")
            writeline(f, "")

            # Generate location definitions
            for location in locations_data:
                self.write_location(f, location, area_names)

            writeline(f, "")
            writeline(f, "# World Map Location Collection")
            writeline(f, "world_map_location_collection = WorldMapLocationCollection(world_map_locations)")

    def write_location(self, f, location, area_names):
        """Write a location definition to the file."""
        location_id = location['id']

        # Get location name from area_names array, or use generic name
        location_name = area_names[location_id] if location_id < len(area_names) and area_names[location_id] else f"OW{location_id:02d}"

        writeline(f, f"world_map_locations[{location_name}] = WorldMapLocation(")
        writeline(f, f"    index={location_id},")

        # Write name if present
        if location['name']:
            # Escape special characters in name
            escaped_name = location['name'].replace('\\', '\\\\').replace('"', '\\"')
            writeline(f, f'    name="{escaped_name}",')

        writeline(f, f"    x={location['x']},")
        writeline(f, f"    y={location['y']},")

        # Write show_check_flag
        if location['show_check_flag']:
            writeline(f, f"    show_check_flag={location['show_check_flag']},")

        writeline(f, f"    go_location={location['go_location']},")

        # Write event or location data depending on go_location
        if not location['go_location']:
            if location['run_event'] is not None:
                writeline(f, f"    run_event={location['run_event']},")
        else:
            if location['which_location_check_flag']:
                writeline(f, f"    which_location_check_flag={location['which_location_check_flag']},")
            if location['go_location_a'] is not None:
                # Use area name constant
                loc_a_name = area_names[location['go_location_a']] if location['go_location_a'] < len(area_names) and area_names[location['go_location_a']] else location['go_location_a']
                writeline(f, f"    go_location_a={loc_a_name},")
            if location['go_location_b'] is not None:
                loc_b_name = area_names[location['go_location_b']] if location['go_location_b'] < len(area_names) and area_names[location['go_location_b']] else location['go_location_b']
                writeline(f, f"    go_location_b={loc_b_name},")

        # Write directional navigation (only if enabled)
        if location['enabled_to_east']:
            writeline(f, "    enabled_to_east=True,")
            if location['check_flag_to_east']:
                writeline(f, f"    check_flag_to_east={location['check_flag_to_east']},")
            if location['location_to_east'] is not None:
                loc_east_name = area_names[location['location_to_east']] if location['location_to_east'] < len(area_names) and area_names[location['location_to_east']] else location['location_to_east']
                writeline(f, f"    location_to_east={loc_east_name},")

        if location['enabled_to_south']:
            writeline(f, "    enabled_to_south=True,")
            if location['check_flag_to_south']:
                writeline(f, f"    check_flag_to_south={location['check_flag_to_south']},")
            if location['location_to_south'] is not None:
                loc_south_name = area_names[location['location_to_south']] if location['location_to_south'] < len(area_names) and area_names[location['location_to_south']] else location['location_to_south']
                writeline(f, f"    location_to_south={loc_south_name},")

        if location['enabled_to_west']:
            writeline(f, "    enabled_to_west=True,")
            if location['check_flag_to_west']:
                writeline(f, f"    check_flag_to_west={location['check_flag_to_west']},")
            if location['location_to_west'] is not None:
                loc_west_name = area_names[location['location_to_west']] if location['location_to_west'] < len(area_names) and area_names[location['location_to_west']] else location['location_to_west']
                writeline(f, f"    location_to_west={loc_west_name},")

        if location['enabled_to_north']:
            writeline(f, "    enabled_to_north=True,")
            if location['check_flag_to_north']:
                writeline(f, f"    check_flag_to_north={location['check_flag_to_north']},")
            if location['location_to_north'] is not None:
                loc_north_name = area_names[location['location_to_north']] if location['location_to_north'] < len(area_names) and area_names[location['location_to_north']] else location['location_to_north']
                writeline(f, f"    location_to_north={loc_north_name},")

        writeline(f, ")")
        writeline(f, "")
