# E3372_KEEP_GET_CRUSHED_BY_HUGE_THWOMP
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
	MoveScriptToBackgroundThread2(),
	JmpIfMarioOnAnObjectOrNot(['EVENT_3372_ret_29', 'EVENT_3372_set_bit_7']),
	SetBit(TEMP_7044_7),
	ResumeActionScript(MEM_70A8),
	ActionQueueAsync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9ci')),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_10"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_10"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_12"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_16"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_16"]),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_10"),
		A_Jmp(["EVENT_3372_action_queue_4_SUBSCRIPT_fixed_f_coord_on_18"]),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True, identifier="EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_12"),
		A_Jmp(["EVENT_3372_action_queue_4_SUBSCRIPT_fixed_f_coord_on_18"]),
		A_SetSpriteSequence(index=7, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_14"),
		A_Jmp(["EVENT_3372_action_queue_4_SUBSCRIPT_fixed_f_coord_on_18"]),
		A_SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True, identifier="EVENT_3372_action_queue_4_SUBSCRIPT_set_sprite_sequence_16"),
		A_Jmp(["EVENT_3372_action_queue_4_SUBSCRIPT_fixed_f_coord_on_18"]),
		A_FixedFCoordOn(identifier="EVENT_3372_action_queue_4_SUBSCRIPT_fixed_f_coord_on_18"),
		A_SetWalkingSpeed(FAST),
		A_TurnClockwise45DegreesNTimes(4),
		A_WalkFDirectionSteps(2),
		A_TurnClockwise45DegreesNTimes(4),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL),
		A_ResetProperties()
	]),
	ClearBit(TEMP_7044_7),
	Return(),
	SetBit(TEMP_7044_7, identifier="EVENT_3372_set_bit_7"),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AB),
	ActionQueueSync(target=MEM_70AB, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_walk_through=True),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownSteps(4),
		A_SetWalkingSpeed(FAST),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[1]),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
		A_ClearSolidityBits(cant_pass_npcs=True, bit_7=True),
		A_SetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
		A_SetWalkingSpeed(VERY_FAST),
		A_ShiftZDownSteps(4),
		A_Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 0, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_14"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_20"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_20"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_18"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_18"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_16"]),
		A_JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_16"]),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, identifier="EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_14"),
		A_Jmp(["EVENT_3372_resume_action_script_12"]),
		A_SetSpriteSequence(index=8, sprite_offset=2, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_16"),
		A_Jmp(["EVENT_3372_resume_action_script_12"]),
		A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True, identifier="EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_18"),
		A_Jmp(["EVENT_3372_resume_action_script_12"]),
		A_SetSpriteSequence(index=1, sprite_offset=3, is_sequence=True, looping=True, mirror_sprite=True, identifier="EVENT_3372_action_queue_11_SUBSCRIPT_set_sprite_sequence_20"),
		A_Jmp(["EVENT_3372_resume_action_script_12"])
	]),
	ResumeActionScript(MEM_70AB, identifier="EVENT_3372_resume_action_script_12"),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	Pause(1, identifier="EVENT_3372_pause_14"),
	Set7000ToTappedButton(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3372_inc_19"]),
	Inc(SECONDARY_TEMP_7024),
	JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 0, ["EVENT_3372_action_queue_23"]),
	Inc(SECONDARY_TEMP_7024, identifier="EVENT_3372_inc_19"),
	Inc(SECONDARY_TEMP_7024),
	CompareVarToConst(SECONDARY_TEMP_7024, 120),
	JmpIfComparisonResultIsLesser(["EVENT_3372_pause_14"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_SetWalkingSpeed(VERY_FAST),
		A_ResetProperties(),
		A_FixedFCoordOn(),
		A_TurnClockwise45DegreesNTimes(4),
		A_Walk1StepFDirection(),
		A_TurnClockwise45DegreesNTimes(4),
		A_FixedFCoordOff(),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3372_action_queue_23"),
	CopyVarToVar(from_var=TEMP_70AB, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSolidityBits(cant_pass_npcs=True, bit_7=True)
	]),
	ClearBit(TEMP_7044_7),
	Return(identifier="EVENT_3372_ret_29")
])
