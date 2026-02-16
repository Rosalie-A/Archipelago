# E3210_SHIP_TRAMPOLINE_PUZZLE_BLOCK
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
	PlaySound(sound=SO005_BLOCK_SWITCH, channel=4),
	DisableObjectTrigger(MEM_70A8),
	SetTempSyncActionScript(MEM_70A8, A0337_VARIOUS_SHIP_OBJECTS),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 65533),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70A9),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 1),
	JmpIfMem704XAt7000BitSet(["EVENT_3210_resume_action_script_82"]),
	PauseActionScript(MEM_70A9),
	SetMem704XAt7000Bit(),
	Set7000ToObjectCoord(target_npc=MEM_70A9, coord=COORD_X, pixel=True),
	JmpIfVarEqualsConst(TEMP_70A9, 20, ["EVENT_3210_copy_var_to_var_15"]),
	JmpIfVarEqualsConst(TEMP_70A9, 21, ["EVENT_3210_copy_var_to_var_17"]),
	JmpIfVarEqualsConst(TEMP_70A9, 22, ["EVENT_3210_copy_var_to_var_19"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024, identifier="EVENT_3210_copy_var_to_var_15"),
	Jmp(["EVENT_3210_jmp_if_bit_clear_21"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026, identifier="EVENT_3210_copy_var_to_var_17"),
	Jmp(["EVENT_3210_jmp_if_bit_clear_21"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7028, identifier="EVENT_3210_copy_var_to_var_19"),
	Jmp(["EVENT_3210_jmp_if_bit_clear_21"]),
	JmpIfBitClear(TEMP_7043_0, ["EVENT_3210_ret_72"], identifier="EVENT_3210_jmp_if_bit_clear_21"),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3210_ret_72"]),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_3210_ret_72"]),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_SetWalkingSpeed(FAST),
		A_BounceToXYWithHeight(x=0, y=103, height=10)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(FAST),
		A_TransferToXYZF(x=2, y=121, z=0, direction=SOUTHEAST),
		A_SetSpriteSequence(index=2, is_sequence=True, looping=False),
		A_SetPaletteRow(row=5),
		A_VisibilityOn(),
		A_FloatingOn(),
		A_WalkNortheastPixels(1, identifier="EVENT_3210_action_queue_25_SUBSCRIPT_shift_northeast_pixels_6"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3210_action_queue_25_SUBSCRIPT_shift_northeast_pixels_6"])
	]),
	Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_X, pixel=True),
	DecVarFrom7000(SECONDARY_TEMP_7024),
	JmpIfLoadedMemoryIsBelow0(["EVENT_3210_compare_var_to_const_31"]),
	Mem7000XorConst(0xFFFF),
	Inc(PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 192, identifier="EVENT_3210_compare_var_to_const_31"),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3210_action_queue_73"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(VERY_FAST),
		A_FloatingOff(),
		A_ShiftZDownPixels(12),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=240, silent=True),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkNortheastPixels(1, identifier="EVENT_3210_action_queue_35_SUBSCRIPT_shift_northeast_pixels_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3210_action_queue_35_SUBSCRIPT_shift_northeast_pixels_10"])
	]),
	Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_X, pixel=True),
	DecVarFrom7000(TEMP_7026),
	JmpIfLoadedMemoryIsBelow0(["EVENT_3210_compare_var_to_const_41"]),
	Mem7000XorConst(0xFFFF),
	Inc(PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 192, identifier="EVENT_3210_compare_var_to_const_41"),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3210_action_queue_73"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(VERY_FAST),
		A_FloatingOff(),
		A_ShiftZDownPixels(12),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=192, silent=True),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkNortheastPixels(1, identifier="EVENT_3210_action_queue_45_SUBSCRIPT_shift_northeast_pixels_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3210_action_queue_45_SUBSCRIPT_shift_northeast_pixels_10"])
	]),
	Set7000ToObjectCoord(target_npc=NPC_7, coord=COORD_X, pixel=True),
	DecVarFrom7000(TEMP_7028),
	JmpIfLoadedMemoryIsBelow0(["EVENT_3210_compare_var_to_const_51"]),
	Mem7000XorConst(0xFFFF),
	Inc(PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 192, identifier="EVENT_3210_compare_var_to_const_51"),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3210_action_queue_73"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetSequenceSpeed(VERY_FAST),
		A_SetSpriteSequence(index=0, is_sequence=True, looping=False),
		A_PlaySound(sound=SO010_TRAMPOLINE, channel=4)
	]),
	ActionQueueSync(target=SCREEN_FOCUS, subscript=[
		A_WalkNortheastSteps(3)
	]),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ClearSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
		A_SetWalkingSpeed(VERY_FAST),
		A_FloatingOff(),
		A_ShiftZDownPixels(12),
		A_SetWalkingSpeed(FAST),
		A_JumpToHeight(height=144, silent=True),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_npcs=True),
		A_SetVRAMPriority(NORMAL_PRIORITY),
		A_WalkNortheastPixels(1, identifier="EVENT_3210_action_queue_55_SUBSCRIPT_shift_northeast_pixels_10"),
		A_JmpIfObjectInAir(DUMMY_0X07, ["EVENT_3210_action_queue_55_SUBSCRIPT_shift_northeast_pixels_10"])
	]),
	JmpIfObjectsAreLessThanXYStepsApartSameZCoord(NPC_7, NPC_6, 0, 1, ["EVENT_3210_set_bit_58"]),
	Jmp(["EVENT_3210_action_queue_73"]),
	SetBit(TEMP_7043_3, identifier="EVENT_3210_set_bit_58"),
	SetSyncActionScript(NPC_3, A0316_SHIP_TRAMPOLINE_PUZZLE_BLOCK_FREEZE),
	SetSyncActionScript(NPC_4, A0316_SHIP_TRAMPOLINE_PUZZLE_BLOCK_FREEZE),
	SetSyncActionScript(NPC_5, A0316_SHIP_TRAMPOLINE_PUZZLE_BLOCK_FREEZE),
	Pause(8),
	SetSyncActionScript(NPC_8, A0338_SHIP_TRAMPOLINE_PUZZLE_SCROLL),
	JmpIfBitSet(UNKNOWN_707D_1, ["EVENT_3210_action_queue_71"]),
	SetVarToConst(X_COORD_1, 6),
	SetVarToConst(Y_COORD_1, 120),
	SetVarToConst(Z_COORD_1, 16),
	UnknownCommand(bytearray(b'\xfd\xc4')),
	Pause(1, identifier="EVENT_3210_pause_69"),
	JmpToEvent(E3383_SHIP_TRAMPOLINE_PRIZE_PACKET_GRANT),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_UnknownCommand(bytearray(b'\xc8\x80')),
		A_AddConstToVar(X_COORD_2, 65532),
		A_CompareVarToConst(X_COORD_2, 0),
		A_JmpIfLoadedMemoryIsBelow0(["EVENT_3210_action_queue_71_SUBSCRIPT_add_5"]),
		A_SetVarToConst(X_COORD_2, 0),
		A_AddConstToVar(Y_COORD_2, 65520, identifier="EVENT_3210_action_queue_71_SUBSCRIPT_add_5"),
		A_UnknownCommand(bytearray(b'\x98')),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_3210_action_queue_71"),
	Return(identifier="EVENT_3210_ret_72"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_JumpToHeight(height=64, silent=True),
		A_Pause(20),
		A_JumpToHeight(height=32, silent=True),
		A_Pause(10),
		A_JumpToHeight(height=8, silent=True),
		A_Pause(8),
		A_VisibilityOff()
	], identifier="EVENT_3210_action_queue_73"),
	ResumeActionScript(NPC_0),
	ResumeActionScript(NPC_1),
	ResumeActionScript(NPC_2),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7043_1),
	ClearBit(TEMP_7043_2),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
	Jmp(["EVENT_3210_action_queue_71"]),
	ResumeActionScript(MEM_70A9, identifier="EVENT_3210_resume_action_script_82"),
	ClearMem704XAt7000Bit(),
	Return()
])
