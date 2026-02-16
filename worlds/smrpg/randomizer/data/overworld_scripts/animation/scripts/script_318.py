#A0318_COIN_SNAKE_TAIL_BASE
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
	A_VisibilityOff(identifier="ACTION_318_visibility_off_0"),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_Pause(1, identifier="ACTION_318_pause_2"),
	A_Set700CToPressedButton(),
	A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=SECONDARY_TEMP_7024),
	A_CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_700C),
	A_Compare700CToVar(SECONDARY_TEMP_7024),
	A_JmpIfLoadedMemoryIsNot0(["ACTION_318_pause_2"]),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(60),
	A_StartLoopNTimes(7),
	A_VisibilityOff(),
	A_Pause(2),
	A_VisibilityOn(),
	A_Pause(2),
	A_EndLoop(),
	A_VisibilityOff(),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_ReturnQueue()
])
