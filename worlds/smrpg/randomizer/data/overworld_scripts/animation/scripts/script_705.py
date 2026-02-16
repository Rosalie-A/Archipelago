#A0705_BOOSTER_HILL_LAYER_3
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
	A_SetVarToRandom(PRIMARY_TEMP_700C, 16, identifier="ACTION_705_set_var_to_random_0"),
	A_AddConstToVar(PRIMARY_TEMP_700C, 15),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(2),
	A_EndLoop(),
	A_JmpIfRandom2of3(['ACTION_705_set_animation_speed_14', 'ACTION_705_set_animation_speed_19']),
	A_Pause(31),
	A_JmpIfRandom2of3(['ACTION_705_set_animation_speed_14', 'ACTION_705_set_animation_speed_19']),
	A_SetWalkingSpeed(VERY_FAST),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	A_WalkSoutheastSteps(32),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	A_Pause(71),
	A_Jmp(["ACTION_705_set_var_to_random_0"]),
	A_SetWalkingSpeed(FASTEST, identifier="ACTION_705_set_animation_speed_14"),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	A_WalkSouthSteps(16),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	A_Pause(41),
	A_SetWalkingSpeed(VERY_FAST, identifier="ACTION_705_set_animation_speed_19"),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	A_WalkNorthwestSteps(32),
	A_JmpIfBitSet(TEMP_7043_4, ["ACTION_705_ret_25"]),
	A_Pause(71),
	A_Jmp(["ACTION_705_set_var_to_random_0"]),
	A_ReturnQueue(identifier="ACTION_705_ret_25")
])
