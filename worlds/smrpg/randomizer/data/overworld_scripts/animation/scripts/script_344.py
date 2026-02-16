#A0344_SHIP_PUZZLE_AREA_GREAPERS
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
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_344_sequence_looping_on_4"]),
	A_ShiftXYPixels(x=9, y=8),
	A_SequenceLoopingOn(identifier="ACTION_344_sequence_looping_on_4"),
	A_FixedFCoordOn(),
	A_Set700CToPressedButton(),
	A_Mem700CAndConst(0x0007),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_344_pause_22"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_344_pause_21"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_344_pause_20"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_344_pause_19"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_344_pause_18"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_344_pause_17"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_344_pause_16"]),
	A_Pause(2),
	A_Pause(2, identifier="ACTION_344_pause_16"),
	A_Pause(2, identifier="ACTION_344_pause_17"),
	A_Pause(2, identifier="ACTION_344_pause_18"),
	A_Pause(2, identifier="ACTION_344_pause_19"),
	A_Pause(2, identifier="ACTION_344_pause_20"),
	A_Pause(2, identifier="ACTION_344_pause_21"),
	A_Pause(1, identifier="ACTION_344_pause_22"),
	A_Jmp(["ACTION_344_pause_22"])
])
