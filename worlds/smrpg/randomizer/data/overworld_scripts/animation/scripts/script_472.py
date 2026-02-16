#A0472_BANDITS_WAY_5_GOOMBA
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
	A_VisibilityOff(),
	A_UnknownCommand(bytearray(b'\xfd\x12')),
	A_FaceNortheast(),
	A_Set700CToPressedButton(),
	A_AddConstToVar(PRIMARY_TEMP_700C, 65512),
	A_LoadMemory(PRIMARY_TEMP_700C),
	A_Pause(1),
	A_EndLoop(),
	A_Pause(3, identifier="ACTION_472_pause_8"),
	A_JmpIfObjectWithinRange(comparing_npc=MARIO, usually=128, tiles=3, destinations=["ACTION_472_unknown_jmp_3C_11"]),
	A_Jmp(["ACTION_472_pause_8"]),
	A_UnknownJmp3C(0x00, 0x40, ["ACTION_472_visibility_on_13"], identifier="ACTION_472_unknown_jmp_3C_11"),
	A_Jmp(["ACTION_472_pause_8"]),
	A_VisibilityOn(identifier="ACTION_472_visibility_on_13"),
	A_SequenceLoopingOn(),
	A_SetSolidityBits(bit_4=True),
	A_SetSolidityBits(cant_walk_through=True),
	A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
	A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
	A_SetAllSpeeds(FASTER),
	A_JumpToHeight(108),
	A_WalkNortheastSteps(3),
	A_Pause(15),
	A_FaceNorthwest(),
	A_SetWalkingSpeed(FAST),
	A_SetSequenceSpeed(VERY_FAST),
	A_Walk1StepFDirection(identifier="ACTION_472_walk_1_step_f_direction_26"),
	A_Pause(15),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(5),
	A_TurnClockwise45DegreesNTimes(6),
	A_Pause(15),
	A_Jmp(["ACTION_472_walk_1_step_f_direction_26"])
])
