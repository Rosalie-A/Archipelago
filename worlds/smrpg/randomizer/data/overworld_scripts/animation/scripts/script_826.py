#A0826_ENEMY_FALL_ONTO_CONVEYOR
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
	A_SetPriority(3),
	A_Set700CToCurrentLevel(),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 473, ["ACTION_826_set_solidity_bits_61"]),
	A_Set700CToPressedButton(),
	A_CompareVarToConst(PRIMARY_TEMP_700C, 24),
	A_JmpIfComparisonResultIsGreaterOrEqual(["ACTION_826_shift_f_direction_steps_55"]),
	A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 22, ["ACTION_826_shadow_off_34"]),
	A_ShadowOff(identifier="ACTION_826_shadow_off_7"),
	A_VisibilityOff(),
	A_FloatingOff(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_Pause(20),
	A_TransferToXYZF(x=7, y=38, z=2, direction=SOUTHEAST),
	A_FaceSouthwest(),
	A_JumpToHeight(96),
	A_Pause(20),
	A_FloatingOn(),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(24),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_Pause(30),
	A_JumpToHeight(64),
	A_Walk1StepSouthwest(),
	A_Pause(5),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_Pause(58),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_JumpToHeight(96),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_Walk1StepSoutheast(),
	A_ShadowOn(),
	A_Walk1StepSoutheast(),
	A_Jmp(["ACTION_826_shadow_off_7"]),
	A_ShadowOff(identifier="ACTION_826_shadow_off_34"),
	A_VisibilityOff(),
	A_FloatingOff(),
	A_SetSolidityBits(cant_pass_walls=True),
	A_Pause(20),
	A_TransferToXYZF(x=14, y=24, z=0, direction=SOUTHEAST),
	A_JumpToHeight(96),
	A_Pause(20),
	A_FloatingOn(),
	A_VisibilityOn(),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_Pause(24),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_Pause(42),
	A_PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
	A_Pause(2),
	A_JumpToHeight(96),
	A_ClearSolidityBits(cant_pass_walls=True),
	A_ShadowOn(),
	A_WalkSouthwestSteps(2),
	A_Jmp(["ACTION_826_shadow_off_34"]),
	A_WalkFDirectionSteps(4, identifier="ACTION_826_shift_f_direction_steps_55"),
	A_Pause(8),
	A_TurnClockwise45DegreesNTimes(2),
	A_Pause(8),
	A_TurnClockwise45DegreesNTimes(2),
	A_Jmp(["ACTION_826_shift_f_direction_steps_55"]),
	A_SetSolidityBits(cant_pass_walls=True, identifier="ACTION_826_set_solidity_bits_61"),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65517),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(2),
	A_EndLoop(),
	A_SetWalkingSpeed(NORMAL),
	A_FixedFCoordOn(),
	A_StartLoopNTimes(2, identifier="ACTION_826_start_loop_n_times_69"),
	A_Walk1StepSoutheast(),
	A_Pause(30),
	A_EndLoop(),
	A_StartLoopNTimes(2),
	A_Walk1StepNorthwest(),
	A_Pause(30),
	A_EndLoop(),
	A_Jmp(["ACTION_826_start_loop_n_times_69"])
])
