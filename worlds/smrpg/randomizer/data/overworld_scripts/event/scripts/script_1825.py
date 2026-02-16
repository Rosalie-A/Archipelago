# E1825_KEEP_ROTATING_ROOM_LOADER
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
	JmpIfBitSet(TEMP_7044_6, ["EVENT_1825_priority_set_2"]),
	ClearBit(TEMP_7095_4),
	PrioritySet(mainscreen=[LAYER_L1, LAYER_L2, NPC_SPRITES], subscreen=[LAYER_L3], colour_math=[NPC_SPRITES, BACKGROUND, HALF_INTENSITY], identifier="EVENT_1825_priority_set_2"),
	RemoveObjectFromCurrentLevel(NPC_0),
	SetVarToConst(ROSE_WAY_7038, 3200),
	SetVarToConst(ROSE_WAY_703A, 6016),
	SetVarToConst(ROSE_WAY_703C, 256),
	SetVarToConst(TEMP_70A9, 27),
	StartLoopNTimes(3),
	ActionQueueSync(target=MEM_70A9, subscript=[
		A_ShiftZUpPixels(4)
	]),
	Inc(TEMP_70A9),
	EndLoop(),
	Pause(2),
	JmpIfBitClear(TEMP_7095_4, ["EVENT_1825_set_var_to_const_46"]),
	CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 9),
	JmpIfComparisonResultIsLesser(["EVENT_1825_inc_21"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 19),
	JmpIfComparisonResultIsLesser(["EVENT_1825_copy_var_to_var_25"]),
	Dec(PRIMARY_TEMP_7000),
	Jmp(["EVENT_1825_copy_var_to_var_22"]),
	Inc(PRIMARY_TEMP_7000, identifier="EVENT_1825_inc_21"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_2, identifier="EVENT_1825_copy_var_to_var_22"),
	CopyVarToVar(from_var=TEMP_7030, to_var=Y_COORD_2),
	Jmp(["EVENT_1825_action_queue_35"]),
	CopyVarToVar(from_var=TEMP_702E, to_var=X_COORD_2, identifier="EVENT_1825_copy_var_to_var_25"),
	CopyVarToVar(from_var=TEMP_7030, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 29),
	JmpIfComparisonResultIsLesser(["EVENT_1825_add_const_to_var_33"]),
	CompareVarToConst(PRIMARY_TEMP_7000, 38),
	JmpIfComparisonResultIsLesser(["EVENT_1825_copy_var_to_var_34"]),
	AddConstToVar(PRIMARY_TEMP_7000, 65534),
	Jmp(["EVENT_1825_copy_var_to_var_34"]),
	AddConstToVar(PRIMARY_TEMP_7000, 2, identifier="EVENT_1825_add_const_to_var_33"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_2, identifier="EVENT_1825_copy_var_to_var_34"),
	ActionQueueSync(target=NPC_7, subscript=[
		A_RunAwayShift()
	], identifier="EVENT_1825_action_queue_35"),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_RunAwayShift()
	]),
	AddConstToVar(X_COORD_2, 65535),
	ActionQueueSync(target=NPC_8, subscript=[
		A_RunAwayShift()
	]),
	ActionQueueAsync(target=NPC_10, subscript=[
		A_RunAwayShift()
	]),
	SetVarToConst(ROSE_WAY_703E, 29),
	JmpToSubroutine(["EVENT_1830_pause_75"]),
	SetBit(UNKNOWN_PAN),
	SetVarToConst(TEMP_70AB, 0),
	RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
	ClearBit(UNKNOWN_PAN),
	SetVarToConst(TEMP_702C, 27, identifier="EVENT_1825_set_var_to_const_46"),
	SetVarToConst(TEMP_70A9, 27),
	SetVarToConst(TEMP_70AA, 28),
	ActionQueueAsync(target=MEM_70A9, subscript=[
		A_BPL262728(),
		A_UnknownCommand(bytearray(b'\xfd$\x11\x12')),
		A_CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_702A)
	]),
	PauseActionScript(NPC_10),
	SetSyncActionScript(MEM_70AA, A0479_BANDITS_WAY_CHEST_PLATFORMS_ON_MOUNT),
	Pause(2),
	SetSyncActionScript(NPC_10, A0653_SLOW_ROTATING_PLATFORM),
	RunBackgroundEvent(event_id=E1828_KEEP_MARIO_FALLS_IN_LAVA, return_on_level_exit=True),
	RunBackgroundEvent(event_id=E1877_KEEP_ROTATING_ROOM_LOADER_CONTD, return_on_level_exit=True, bit_6=True),
	JmpToEvent(E1829_KEEP_DISPLAY_REMAINING_TRIES)
])
