# E1556_WIGGLER_JUMP
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
	SetVarToConst(BATTLE_PACK_ID, 24),
	JmpIfRandom1of2(["EVENT_1556_jmp_if_bit_set_3"]),
	SetVarToConst(BATTLE_PACK_ID, 25),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1556_ret_87"], identifier="EVENT_1556_jmp_if_bit_set_3"),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_1556_ret_87"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	SetVarToConst(SECONDARY_TEMP_7024, 20),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	JmpIf7000AnyBitsSet(bits=[2], destinations=["EVENT_1556_set_bit_13"]),
	SetBit(TEMP_7043_5),
	ClearBit(TEMP_7043_4),
	Jmp(["EVENT_1556_mem_7000_and_const_15"]),
	SetBit(TEMP_7043_6, identifier="EVENT_1556_set_bit_13"),
	SetBit(TEMP_7043_4),
	Mem7000AndConst(0x0004, identifier="EVENT_1556_mem_7000_and_const_15"),
	AddVarTo7000(SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	Set7000ToObjectCoord(target_npc=MEM_70AA, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfBitClear(TEMP_7076_0, ["EVENT_1556_start_loop_n_times_28"]),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1556_start_loop_n_times_23', 'EVENT_1556_ret_87']),
	StartLoopNTimes(3, identifier="EVENT_1556_start_loop_n_times_23"),
	PauseActionScript(MEM_70AA),
	Inc(TEMP_70AA),
	EndLoop(),
	Jmp(["EVENT_1556_copy_var_to_var_52"]),
	StartLoopNTimes(3, identifier="EVENT_1556_start_loop_n_times_28"),
	PauseActionScript(MEM_70AA),
	Inc(TEMP_70AA),
	EndLoop(),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1556_copy_var_to_var_52', 'EVENT_1556_start_battle_700E_33']),
	StartBattleWithPackAt700E(identifier="EVENT_1556_start_battle_700E_33"),
	JmpIfBitSet(GAME_OVER, ["EVENT_1556_reset_and_choose_game_50"]),
	SetVarToConst(TEMP_70AF, 0),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	StartLoopNTimes(3),
	ResetCoords(MEM_70AA),
	SetSyncActionScript(MEM_70AA, A0652_FOREST_FIRST_WIGGLER_AFTER_RUNNING_AWAY),
	Inc(TEMP_70AA),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(1),
		A_JumpToHeight(height=0, silent=True)
	]),
	FadeInFromBlack(sync=False),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1556_clear_bit_48"]),
	ClearBit(TEMP_7043_5),
	Return(),
	ClearBit(TEMP_7043_6, identifier="EVENT_1556_clear_bit_48"),
	Return(),
	ResetAndChooseGame(identifier="EVENT_1556_reset_and_choose_game_50"),
	Return(),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1556_copy_var_to_var_52"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C),
	ActionQueueSync(target=MARIO, subscript=[
		A_FaceEast7C(),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(144),
		A_Walk1StepFDirection(),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	Inc(TEMP_70AF),
	JmpIfVarNotEqualsConst(TEMP_70AF, 10, ["EVENT_1556_add_coins_64"]),
	Inc(TEMP_70AB),
	SummonObjectToCurrentLevelAtMariosCoords(MEM_70AB),
	StartSyncEmbeddedActionScript(target=MEM_70AB, prefix=0xF1, subscript=[
		A_PlaySound(sound=SO094_FROG_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0004),
		A_Mem700CXorConst(0x0004),
		A_FaceEast7C(),
		A_FloatingOff(),
		A_JumpToHeight(160),
		A_WalkFDirectionSteps(2),
		A_VisibilityOff()
	]),
	Dec(TEMP_70AB),
	RunDialog(dialog_id=DI1049_FOUND_A_FROG_COIN, above_object=TOADSTOOL, closable=False, sync=True, multiline=False, use_background=False, bit_6=True),
	AddFrogCoins(1),
	Jmp(["EVENT_1556_pause_67"]),
	AddCoins(1, identifier="EVENT_1556_add_coins_64"),
	SummonObjectToCurrentLevelAtMariosCoords(MEM_70AB),
	StartSyncEmbeddedActionScript(target=MEM_70AB, prefix=0xF1, subscript=[
		A_PlaySound(sound=SO013_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True),
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_AddConstToVar(PRIMARY_TEMP_700C, 2),
		A_Mem700CAndConst(0x0004),
		A_Mem700CXorConst(0x0004),
		A_FaceEast7C(),
		A_FloatingOff(),
		A_UnknownCommand(bytearray(b' \x04')),
		A_UnknownCommand(bytearray(b'%\x00\x08\xb0\xff')),
		A_Walk1StepFDirection(),
		A_VisibilityOff(),
		A_BPL262728()
	]),
	Pause(1, identifier="EVENT_1556_pause_67"),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	StartLoopNTimes(3),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ShiftZUpPixels(16),
		A_ShiftZDownPixels(16)
	]),
	Inc(TEMP_70AA),
	Pause(3),
	EndLoop(),
	Dec(TEMP_70AA),
	StopEmbeddedActionScript(MEM_70AA),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	StartLoopNTimes(3),
	ResumeActionScript(MEM_70AA),
	Inc(TEMP_70AA),
	EndLoop(),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1556_clear_bit_86"]),
	ClearBit(TEMP_7043_5),
	Return(),
	ClearBit(TEMP_7043_6, identifier="EVENT_1556_clear_bit_86"),
	Return(identifier="EVENT_1556_ret_87")
])
