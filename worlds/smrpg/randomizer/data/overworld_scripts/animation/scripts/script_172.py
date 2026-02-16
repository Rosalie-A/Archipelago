#A0172_ENDING_CUTSCENE_SPARKLES
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
	A_FixedFCoordOn(),
	A_SetSpriteSequence(index=0, is_sequence=True, looping=True),
	A_LoadMemory(TEMP_702E),
	A_Pause(1),
	A_JmpIfMarioInAir(["ACTION_172_ret_28"]),
	A_EndLoop(),
	A_StartLoopNTimes(11),
	A_SetWalkingSpeed(FAST),
	A_ShiftZDownPixels(2),
	A_ShiftZUpPixels(2),
	A_JmpIfMarioInAir(["ACTION_172_ret_28"]),
	A_EndLoop(),
	A_JumpToHeight(height=0, silent=True),
	A_FloatingOn(),
	A_Pause(1, identifier="ACTION_172_pause_14"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_172_pause_14"]),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ShiftZUpSteps(9),
	A_StartLoopNTimes(4),
	A_Pause(1),
	A_VisibilityOff(),
	A_Pause(1),
	A_VisibilityOn(),
	A_EndLoop(),
	A_SetSolidityBits(cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue(identifier="ACTION_172_ret_28")
])
