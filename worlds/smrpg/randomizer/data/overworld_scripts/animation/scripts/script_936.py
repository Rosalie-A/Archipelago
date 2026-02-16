#A0936_VOLCANO_1ST_BOSS_HENCHMAN
# pyright: reportWildcardImportFromLibrary=false

from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.commands import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.coords import *
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import *
from smrpgpatchbuilder.datatypes.overworld_scripts.action_scripts.arguments import *
from ....variables.action_script_names import *
from ....variables.event_script_names import *
from ....variables.overworld_sfx_names import *
from ....variables.room_names import *
from ....variables.variable_names import *
from ....packets import *
from ....items import *

script = ActionScript([
	A_ShadowOn(),
	A_FixedFCoordOn(),
	A_SequenceLoopingOn(),
	A_SetPriority(3),
	A_UnknownCommand(bytearray(b' \x04')),
	A_EmbeddedAnimationRoutine(bytearray(b'(\x00\x00\x00\x00\x00\x00\x00\x08\x00\x01\x00\x00\x00\x02\x80')),
	A_SetWalkingSpeed(VERY_SLOW),
	A_Set700CToPressedButton(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_936_walk_to_xy_coords_12"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 23, ["ACTION_936_walk_to_xy_coords_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 24, ["ACTION_936_walk_to_xy_coords_23"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 25, ["ACTION_936_walk_to_xy_coords_26"]),
	A_WalkToXYCoords(x=5, y=27, identifier="ACTION_936_walk_to_xy_coords_12"),
	A_ShiftZDownPixels(4),
	A_WalkSouthPixels(8),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_Pause(1, identifier="ACTION_936_pause_16"),
	A_Jmp(["ACTION_936_pause_16"]),
	A_WalkToXYCoords(x=6, y=26, identifier="ACTION_936_walk_to_xy_coords_18"),
	A_ShiftZDownPixels(16),
	A_WalkEastPixels(3),
	A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
	A_Jmp(["ACTION_936_pause_16"]),
	A_WalkToXYCoords(x=5, y=25, identifier="ACTION_936_walk_to_xy_coords_23"),
	A_ShiftZDownPixels(12),
	A_Jmp(["ACTION_936_pause_16"]),
	A_WalkToXYCoords(x=5, y=26, identifier="ACTION_936_walk_to_xy_coords_26"),
	A_ShiftZDownPixels(12),
	A_Jmp(["ACTION_936_pause_16"])
])
