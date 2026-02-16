# E1709_BANDITS_WAY_5_LOADER_BACKGROUND_2
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
	SetVarToConst(TEMP_7030, 100),
	SetVarToConst(TEMP_7032, 0),
	StartLoopNTimes(239, identifier="EVENT_1709_start_loop_n_times_2"),
	Pause(1),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_1709_jmp_to_subroutine_17"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_1709_jmp_to_subroutine_22"]),
	EndLoop(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(108),
		A_Pause(27)
	]),
	JmpToSubroutine(["EVENT_1709_enable_controls_until_return_35"]),
	StopEmbeddedActionScript(NPC_5),
	StopEmbeddedActionScript(NPC_6),
	StopEmbeddedActionScript(NPC_7),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(TEMP_7044_4, identifier="EVENT_1709_clear_bit_13"),
	ClearBit(TEMP_7044_5),
	RunEventAsSubroutine(E1707_BANDITS_WAY_5_LOADER_BACKGROUND),
	Jmp(["EVENT_1709_start_loop_n_times_2"]),
	JmpToSubroutine(["EVENT_1709_enable_controls_until_return_35"], identifier="EVENT_1709_jmp_to_subroutine_17"),
	JmpToSubroutine(["EVENT_1709_action_queue_44"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
	Jmp(["EVENT_1709_clear_bit_13"]),
	JmpToSubroutine(["EVENT_1709_enable_controls_until_return_35"], identifier="EVENT_1709_jmp_to_subroutine_22"),
	Inc(TEMP_7032),
	JmpIfVarEqualsConst(TEMP_7032, 3, ["EVENT_1709_run_event_at_return_33"]),
	JmpToSubroutine(["EVENT_1709_action_queue_47"]),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 65486),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7030),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	PlaySound(sound=SO011_WHOOSH_AWAY, channel=6),
	Jmp(["EVENT_1709_clear_bit_13"]),
	RunEventAtReturn(E1710_BANDITS_WAY_5_LOADER_BACKGROUND_BOSS_FIGHT, identifier="EVENT_1709_run_event_at_return_33"),
	Return(),
	EnableControlsUntilReturn([], identifier="EVENT_1709_enable_controls_until_return_35"),
	SetVarToConst(TEMP_70AB, 25),
	StartLoopNTimes(2),
	PauseActionScript(MEM_70AB),
	JmpIfObjectInCurrentLevel(MEM_70AB, ["EVENT_1709_inc_41"]),
	StartSyncEmbeddedActionScript(target=MEM_70AB, prefix=0xF1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetAllSpeeds(FASTER),
		A_WalkSouthwestSteps(3),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_VisibilityOff()
	]),
	Inc(TEMP_70AB, identifier="EVENT_1709_inc_41"),
	EndLoop(),
	Return(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(108),
		A_Pause(27),
		A_FaceMario()
	], identifier="EVENT_1709_action_queue_44"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSouthwest7D(arg=0x1C)
	]),
	Return(),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_SetAllSpeeds(VERY_FAST),
		A_PlaySound(sound=SO030_SURPRISED_MONSTER, channel=4),
		A_StartLoopNTimes(3),
		A_ShiftZUpPixels(8),
		A_ShiftZDownPixels(8),
		A_EndLoop(),
		A_Pause(10),
		A_StopSound(),
		A_FaceMario(),
		A_Pause(10),
		A_PlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(108),
		A_Pause(27),
		A_SetWalkingSpeed(VERY_FAST),
		A_SetSequenceSpeed(NORMAL),
		A_FixedFCoordOn(),
		A_Walk1StepSouth()
	], identifier="EVENT_1709_action_queue_47"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_UnknownCommand(bytearray(b'\xc8\x1c')),
		A_AddConstToVar(X_COORD_2, 256),
		A_AddConstToVar(Y_COORD_2, 128),
		A_UnknownCommand(bytearray(b'\xfd\xc7')),
		A_UnknownCommand(bytearray(b'\x98')),
		A_FaceNorthwest(),
		A_SetWalkingSpeed(NORMAL),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_FixedFCoordOff(),
		A_FaceSoutheast()
	]),
	Return()
])
