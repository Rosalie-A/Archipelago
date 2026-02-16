#A0286_KEEP_THWOMPS
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
	A_FloatingOff(),
	A_ObjectMemorySetBit(arg_1=0x0B, bits=[3]),
	A_ObjectMemorySetBit(arg_1=0x0D, bits=[6]),
	A_SetWalkingSpeed(FAST),
	A_SetPriority(2),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_VarShiftLeft(PRIMARY_TEMP_700C, 255),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(23),
	A_EndLoop(),
	A_FloatingOn(identifier="ACTION_286_floating_on_11"),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(1, identifier="ACTION_286_pause_13"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_286_pause_13"]),
	A_ShadowOn(),
	A_PlaySound(sound=SO073_THWOMP_STOMP, channel=4),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 4),
	A_SetMem704XAt700CBit(),
	A_Pause(20),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 4),
	A_ClearMem704XAt700CBit(),
	A_ShadowOff(),
	A_SetWalkingSpeed(VERY_FAST, identifier="ACTION_286_set_animation_speed_25"),
	A_ShiftZUpPixels(2),
	A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True, bit_7=True),
	A_JmpIfVarNotEqualsConst(PRIMARY_TEMP_700C, 16, ["ACTION_286_set_animation_speed_25"]),
	A_Pause(110),
	A_Jmp(["ACTION_286_floating_on_11"])
])
