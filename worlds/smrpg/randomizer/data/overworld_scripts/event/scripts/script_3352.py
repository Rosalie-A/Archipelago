# E3352_DR_TOPPER_QUIZ
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
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetPriority(3),
		A_WalkToXYCoords(x=5, y=102),
		A_FaceNortheast()
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkToXYCoords(x=1, y=75)
	]),
	SetBit(TEMP_7044_7),
	FadeOutMusicToVolume(duration=4, volume=0),
	Pause(8),
	PlayMusicAtDefaultVolume(M0036_EXPLANATION),
	SetVarToConst(ROSE_WAY_7038, 0),
	SetVarToConst(ROSE_WAY_703A, 0),
	SetVarToConst(ROSE_WAY_703C, 0),
	SetVarToConst(SECONDARY_TEMP_7024, 12),
	Jmp(["EVENT_3352_clear_bit_29"], identifier="EVENT_3352_jmp_12"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, identifier="EVENT_3352_set_7000_to_object_coord_13"),
	CompareVarToConst(PRIMARY_TEMP_7000, 1024),
	JmpIfLoadedMemoryIsBelow0(["EVENT_3352_clear_bit_108"]),
	Dec(SECONDARY_TEMP_7024),
	JmpIfLoadedMemoryIsNot0(["EVENT_3352_jmp_12"]),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	PlayMusicAtDefaultVolume(M0066_BOWSER_SCASTLE_2NDTIME),
	SlowDownMusic(),
	RunDialog(dialog_id=DI1887_QUIZ_FAILED, above_object=NPC_12, closable=True, sync=True, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_ShiftZDownSteps(4)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=12, sprite_offset=2, is_sequence=True, looping=True),
		A_Pause(2)
	]),
	Pause(180),
	FadeOutToBlack(sync=False),
	JmpToEvent(E3356_KEEP_RESPAWN_IN_LOBBY_UPON_FAILURE),
	ClearBit(TEMP_7044_5, identifier="EVENT_3352_clear_bit_29"),
	JmpIfRandom2of3(['EVENT_3352_set_var_to_const_40', 'EVENT_3352_set_var_to_const_49']),
	SetVarToConst(TEMP_7034, 1842),
	CopyVarToVar(from_var=ROSE_WAY_7038, to_var=UNKNOWN_7036),
	SetVarToConst(TEMP_7032, 16),
	JmpToSubroutine(["EVENT_3352_set_var_to_const_58"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3352_clear_bit_29"]),
	CopyVarToVar(from_var=UNKNOWN_7036, to_var=ROSE_WAY_7038),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3352_pause_104"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3352_pause_100', 'EVENT_3352_pause_100']),
	Jmp(["EVENT_3352_pause_96"]),
	SetVarToConst(TEMP_7034, 1858, identifier="EVENT_3352_set_var_to_const_40"),
	CopyVarToVar(from_var=ROSE_WAY_703A, to_var=UNKNOWN_7036),
	SetVarToConst(TEMP_7032, 16),
	JmpToSubroutine(["EVENT_3352_set_var_to_const_58"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3352_clear_bit_29"]),
	CopyVarToVar(from_var=UNKNOWN_7036, to_var=ROSE_WAY_703A),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3352_pause_104"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3352_pause_96', 'EVENT_3352_pause_100']),
	Jmp(["EVENT_3352_pause_100"]),
	SetVarToConst(TEMP_7034, 1874, identifier="EVENT_3352_set_var_to_const_49"),
	CopyVarToVar(from_var=ROSE_WAY_703C, to_var=UNKNOWN_7036),
	SetVarToConst(TEMP_7032, 8),
	JmpToSubroutine(["EVENT_3352_set_var_to_const_58"]),
	JmpIfBitSet(TEMP_7044_5, ["EVENT_3352_clear_bit_29"]),
	CopyVarToVar(from_var=UNKNOWN_7036, to_var=ROSE_WAY_703C),
	JmpIfBitSet(TEMP_7044_6, ["EVENT_3352_pause_104"]),
	JmpIfDialogOptionBOrCSelected(['EVENT_3352_pause_100', 'EVENT_3352_pause_96']),
	Jmp(["EVENT_3352_pause_100"]),
	SetVarToConst(TEMP_7026, 1, identifier="EVENT_3352_set_var_to_const_58"),
	GenerateRandomNumFromRangeVar(TEMP_7032),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3352_copy_var_to_var_65"]),
	SetObjectMemoryToVar(PRIMARY_TEMP_7000),
	VarShiftLeft(TEMP_7026, 255),
	EndLoop(),
	CopyVarToVar(from_var=UNKNOWN_7036, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3352_copy_var_to_var_65"),
	Mem7000AndVar(TEMP_7026),
	CompareVarToConst(PRIMARY_TEMP_7000, 0),
	JmpIfLoadedMemoryIsNot0(["EVENT_3352_set_bit_94"]),
	CopyVarToVar(from_var=UNKNOWN_7036, to_var=PRIMARY_TEMP_7000),
	Mem7000OrVar(TEMP_7026),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=UNKNOWN_7036),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(TEMP_7034),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	RunDialog(dialog_id=PRIMARY_TEMP_7000, above_object=NPC_12, closable=False, sync=True, multiline=True, use_background=False),
	ClearBit(TEMP_7044_6),
	PauseScriptResumeOnNextDialogPageB(),
	SetBit(TEMP_7044_7),
	SetVarToConst(TEMP_7028, 30),
	StartLoopNFrames(299),
	Pause(1),
	SetVarToRandom(PRIMARY_TEMP_7000, 256),
	Inc(TEMP_7028),
	JmpIfVarNotEqualsConst(TEMP_7028, 60, ["EVENT_3352_if_0210_bits_012_clear_do_not_jump_88"]),
	PlaySound(sound=SO144_CLICK, channel=4),
	SetVarToConst(TEMP_7028, 0),
	If0210Bits012ClearDoNotJump(["EVENT_3352_end_loop_90"], identifier="EVENT_3352_if_0210_bits_012_clear_do_not_jump_88"),
	Jmp(["EVENT_3352_close_dialog_92"]),
	EndLoop(identifier="EVENT_3352_end_loop_90"),
	SetBit(TEMP_7044_6),
	CloseDialog(identifier="EVENT_3352_close_dialog_92"),
	Return(),
	SetBit(TEMP_7044_5, identifier="EVENT_3352_set_bit_94"),
	Return(),
	Pause(4, identifier="EVENT_3352_pause_96"),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftZUpPixels(7)
	]),
	Jmp(["EVENT_3352_set_7000_to_object_coord_13"]),
	Pause(4, identifier="EVENT_3352_pause_100"),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftZDownPixels(14)
	]),
	Jmp(["EVENT_3352_set_7000_to_object_coord_13"]),
	Pause(4, identifier="EVENT_3352_pause_104"),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	ActionQueueAsync(target=NPC_1, subscript=[
		A_ShiftZDownPixels(7)
	]),
	Jmp(["EVENT_3352_set_7000_to_object_coord_13"]),
	ClearBit(TEMP_7044_7, identifier="EVENT_3352_clear_bit_108"),
	SetSyncActionScript(NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS),
	Pause(8),
	PlayMusicAtDefaultVolume(M0009_VICTORY),
	RunDialog(dialog_id=DI1886_DUPLICATE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetBit(TEMP_7044_7),
	Pause(32),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=3, looping=False)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_Pause(38),
		A_SetWalkingSpeed(VERY_FAST),
		A_AddZCoord1Step(),
		A_StartLoopNTimes(7),
		A_ShiftZDownPixels(4),
		A_ShiftZUpPixels(4),
		A_EndLoop()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_Pause(38),
		A_JumpToHeight(256),
		A_WalkNortheastSteps(4),
		A_Pause(1, identifier="EVENT_3352_action_queue_117_SUBSCRIPT_pause_3"),
		A_JmpIfMarioInAir(["EVENT_3352_action_queue_117_SUBSCRIPT_pause_3"]),
		A_PlaySound(sound=SO058_INSERT, channel=4),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetBit(TEMP_7044_6),
		A_Pause(8),
		A_WalkNortheastSteps(2),
		A_SetBit(TEMP_7044_5)
	]),
	Pause(1, identifier="EVENT_3352_pause_118"),
	JmpIfBitClear(TEMP_7044_6, ["EVENT_3352_pause_118"]),
	PlaySound(sound=SO016_OPEN_DOOR, channel=4),
	ApplyTileModToLevel(use_alternate=True, room_id=R464_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_1A_QUIZ, mod_id=0),
	Pause(1, identifier="EVENT_3352_pause_122"),
	JmpIfBitClear(TEMP_7044_5, ["EVENT_3352_pause_122"]),
	JmpToEvent(E1953_KEEP_QUIZ_ROOM_EXIT_CONTAINER),
	Return()
])
