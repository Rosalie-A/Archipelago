# E3226_SHIP_GENERIC_LOADER
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import EventScript
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.colours import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.controller_inputs import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.intro_title_text import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.layers import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.palette_types import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.scenes import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.tutorials import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.battlefield_names import *
from ....variables.dialog_names import *
from ....variables.event_script_names import *
from ....variables.music_names import *
from ....variables.overworld_area_names import *
from ....variables.overworld_sfx_names import *
from ....variables.pack_names import *
from ....variables.room_names import *
from ....variables.shop_names import *
from ....variables.variable_names import *
from ....items import *
from ....packets import *
from ....spells.spells import *

script = EventScript([
	CloseDialog(),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 160, ["EVENT_3226_apply_tile_mod_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 162, ["EVENT_3226_apply_tile_mod_19"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 163, ["EVENT_3226_apply_tile_mod_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 165, ["EVENT_3226_apply_tile_mod_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 167, ["EVENT_3226_apply_tile_mod_30"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 172, ["EVENT_3226_apply_tile_mod_32"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R160_SUNKEN_SHIP_AREA_01, mod_id=34, identifier="EVENT_3226_apply_tile_mod_8"),
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 34),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_3226_run_event_as_subroutine_13"]),
	JmpToSubroutine(["EVENT_3225_set_bit_123"]),
	SetBit(TEMP_7042_0),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3226_run_event_as_subroutine_13"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3226_ret_18"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3226_ret_18"]),
	RunEventAsSubroutine(E3906_SHIP_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_3226_ret_18"),
	ApplyTileModToLevel(use_alternate=True, room_id=R162_SUNKEN_SHIP_AREA_04_GREAPERS_DRY_BONES, mod_id=33, identifier="EVENT_3226_apply_tile_mod_19"),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	ApplyTileModToLevel(use_alternate=True, room_id=R163_SUNKEN_SHIP_PUZZLE_ROOM_2, mod_id=32, identifier="EVENT_3226_apply_tile_mod_21"),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=39, identifier="EVENT_3226_apply_tile_mod_23"),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=40),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=41),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=42),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=43),
	ApplyTileModToLevel(use_alternate=True, room_id=R165_SUNKEN_SHIP_AREA_06_PUZZLE_ROOM_PASSAGEWAY, mod_id=44),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	ApplyTileModToLevel(use_alternate=True, room_id=R167_SUNKEN_SHIP_AREA_05_LONG_STAIRWELL_WITH_RUNNING_ALLEY_RATS, mod_id=32, identifier="EVENT_3226_apply_tile_mod_30"),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER),
	ApplyTileModToLevel(use_alternate=True, room_id=R172_SUNKEN_SHIP_PUZZLE_ROOM_5, mod_id=32, identifier="EVENT_3226_apply_tile_mod_32"),
	JmpToEvent(E0015_STANDARD_ROOM_LOADER)
])
