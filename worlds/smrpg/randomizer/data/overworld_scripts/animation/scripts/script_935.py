#A0935_EJECTING_AN_OERLIKON
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
	A_SetSolidityBits(cant_pass_walls=True),
	A_SetWalkingSpeed(FASTEST),
	A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_ShiftZUpSteps(8),
	A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
	A_FloatingOff(),
	A_SetVarToRandom(PRIMARY_TEMP_700C, 8, identifier="ACTION_935_set_var_to_random_6"),
	A_FaceEast7C(),
	A_WalkFDirectionSteps(2),
	A_JmpIfRandom1of2(["ACTION_935_set_var_to_random_6"]),
	A_JmpIfRandom1of2(["ACTION_935_set_var_to_random_6"]),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_FloatingOn(),
	A_SetBit(TEMP_7043_2),
	A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
	A_SetAllSpeeds(SLOW),
	A_JumpToHeight(height=0, silent=True),
	A_Pause(1, identifier="ACTION_935_pause_18"),
	A_JmpIfObjectInAir(DUMMY_0X07, ["ACTION_935_pause_18"]),
	A_SetWalkingSpeed(SLOW, identifier="ACTION_935_set_animation_speed_20"),
	A_SetSequenceSpeed(FAST),
	A_Walk1StepFDirection(),
	A_JumpToHeight(height=0, silent=True),
	A_TurnRandomDirection(),
	A_Walk1StepFDirection(),
	A_JmpIfRandom1of2(["ACTION_935_set_animation_speed_20"]),
	A_FaceMario(),
	A_SetWalkingSpeed(NORMAL),
	A_SetSequenceSpeed(VERY_FAST),
	A_Walk1StepFDirection(),
	A_Jmp(["ACTION_935_set_animation_speed_20"])
])
