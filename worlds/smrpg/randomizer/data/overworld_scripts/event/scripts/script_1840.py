# E1840_PLATFORM_SUBROUTINE
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
	JmpIfMarioOnAnObjectOrNot(['EVENT_1840_copy_var_to_var_2', 'EVENT_1840_ret_24']),
	Jmp(["EVENT_1840_ret_24"]),
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000, identifier="EVENT_1840_copy_var_to_var_2"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
	SetBit(TEMP_7095_4),
	ResumeActionScript(MEM_70A8),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 321, ["EVENT_1840_play_sound_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_1840_play_sound_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 458, ["EVENT_1840_play_sound_25"]),
	PlaySound(sound=SO058_INSERT, channel=6),
	EnableControlsUntilReturn([B]),
	Pause(1),
	JmpIfMarioInAir(["EVENT_1840_ret_24"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Pause(1),
	JmpIfMarioInAir(["EVENT_1840_ret_24"]),
	EnableControlsUntilReturn([B]),
	StartLoopNTimes(5),
	Pause(1),
	JmpIfMarioInAir(["EVENT_1840_ret_24"]),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[0, 1, 2, 3, 4, 5, 6, 7], destinations=["EVENT_1840_ret_24"]),
	EndLoop(),
	Return(identifier="EVENT_1840_ret_24"),
	PlaySound(sound=SO058_INSERT, channel=6, identifier="EVENT_1840_play_sound_25"),
	EnableControlsUntilReturn([Y, B]),
	Pause(1),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1840_set_7000_to_current_level_53"]),
	JmpIfMarioInAir(["EVENT_1840_set_bit_70"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Pause(1),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1840_set_7000_to_current_level_53"]),
	JmpIfMarioInAir(["EVENT_1840_set_bit_70"]),
	EnableControlsUntilReturn([Y, B]),
	StartLoopNTimes(5),
	Pause(1),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1840_set_7000_to_current_level_53"]),
	JmpIfMarioInAir(["EVENT_1840_set_bit_70"]),
	Set7000ToPressedButton(),
	JmpIf7000AllBitsClear(bits=[0, 1, 2, 3, 4, 5, 6, 7], destinations=["EVENT_1840_enable_controls_until_return_45"]),
	EndLoop(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_1840_enable_controls_until_return_45"),
	Pause(1, identifier="EVENT_1840_pause_46"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1840_set_7000_to_current_level_53"]),
	JmpIfMarioInAir(["EVENT_1840_set_bit_70"]),
	JmpIfMarioOnObject(MEM_70A8, ["EVENT_1840_pause_46"]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(),
	Return(),
	Set7000ToCurrentLevel(identifier="EVENT_1840_set_7000_to_current_level_53"),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 321, ["EVENT_1840_enable_controls_until_return_56"]),
	Return(),
	EnableControlsUntilReturn([B], identifier="EVENT_1840_enable_controls_until_return_56"),
	Set7000ToPressedButton(identifier="EVENT_1840_set_7000_to_pressed_button_57"),
	JmpIf7000AnyBitsSet(bits=[0, 3], destinations=["EVENT_1840_action_queue_63"]),
	JmpIf7000AnyBitsSet(bits=[1, 2], destinations=["EVENT_1840_action_queue_65"]),
	Pause(1),
	JmpIfMarioInAir(["EVENT_1840_set_7000_to_pressed_button_57"]),
	Jmp(["EVENT_1840_enable_controls_until_return_67"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNortheastPixels(2, identifier="EVENT_1840_action_queue_63_SUBSCRIPT_shift_northeast_pixels_1"),
		A_JmpIfMarioInAir(["EVENT_1840_action_queue_63_SUBSCRIPT_shift_northeast_pixels_1"]),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_1840_action_queue_63"),
	Jmp(["EVENT_1840_enable_controls_until_return_67"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkSouthwestPixels(2, identifier="EVENT_1840_action_queue_65_SUBSCRIPT_shift_southwest_pixels_1"),
		A_JmpIfMarioInAir(["EVENT_1840_action_queue_65_SUBSCRIPT_shift_southwest_pixels_1"]),
		A_SetWalkingSpeed(NORMAL)
	], identifier="EVENT_1840_action_queue_65"),
	Jmp(["EVENT_1840_enable_controls_until_return_67"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_1840_enable_controls_until_return_67"),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(),
	Return(),
	SetBit(UNKNOWN_704D_1, identifier="EVENT_1840_set_bit_70"),
	EnableControlsUntilReturn([]),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_1840_action_queue_75"]),
	FreezeAllNPCsUntilReturn(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_ShiftZUpPixels(1)
	], identifier="EVENT_1840_action_queue_75"),
	CopyVarToVar(from_var=ROSE_WAY_703E, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ACTIVE_NPC),
	Set7016701BToObjectXYZ(target=MEM_70A8),
	JmpToSubroutine(["EVENT_1834_action_queue_55"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	Set7000ToCurrentLevel(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 455, ["EVENT_1840_reactivate_trigger_if_mario_on_top_of_object_85"]),
	UnfreezeAllNPCs(),
	ClearBit(UNKNOWN_704D_1),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1840_reactivate_trigger_if_mario_on_top_of_object_85"),
	Return()
])
