# E1775_SKY_TROOPA_PLATFORM
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
	CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 23, ["EVENT_1775_jmp_if_bit_set_15"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 24, ["EVENT_1775_jmp_if_bit_set_21"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 25, ["EVENT_1775_jmp_if_bit_set_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 26, ["EVENT_1775_jmp_if_bit_set_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 27, ["EVENT_1775_jmp_if_bit_set_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 28, ["EVENT_1775_jmp_if_bit_set_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 29, ["EVENT_1775_jmp_if_bit_set_51"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_13"]),
	SetBit(TEMP_7043_1),
	SetBit(TEMP_7044_1),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(2),
		A_ShiftZUpSteps(2),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_ShiftZDownSteps(2),
		A_WalkNorthwestSteps(2),
		A_ClearBit(TEMP_7043_1)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_13"),
	Return(),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_19"], identifier="EVENT_1775_jmp_if_bit_set_15"),
	SetBit(TEMP_7043_2),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(5),
		A_AddZCoord1Step(),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_DecZCoord1Step(),
		A_WalkNorthwestSteps(5),
		A_ClearBit(TEMP_7043_2)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_19"),
	Return(),
	JmpIfBitSet(TEMP_7043_3, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_25"], identifier="EVENT_1775_jmp_if_bit_set_21"),
	SetBit(TEMP_7043_3),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(2),
		A_WalkNorthwestSteps(2),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(2),
		A_ShiftZDownSteps(2),
		A_ClearBit(TEMP_7043_3)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_25"),
	Return(),
	JmpIfBitSet(TEMP_7043_4, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_31"], identifier="EVENT_1775_jmp_if_bit_set_27"),
	SetBit(TEMP_7043_4),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(4),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(4),
		A_ClearBit(TEMP_7043_4)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_31"),
	Return(),
	JmpIfBitSet(TEMP_7043_5, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_37"], identifier="EVENT_1775_jmp_if_bit_set_33"),
	SetBit(TEMP_7043_5),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkNorthwestSteps(2),
		A_ShiftZUpSteps(2),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_WalkSoutheastSteps(3),
		A_ShiftZDownSteps(2),
		A_Walk1StepNorthwest(),
		A_ClearBit(TEMP_7043_5)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_37"),
	Return(),
	JmpIfBitSet(TEMP_7043_6, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_43"], identifier="EVENT_1775_jmp_if_bit_set_39"),
	SetBit(TEMP_7043_6),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_ShiftZUpSteps(4),
		A_Walk1StepSoutheast(),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_Walk1StepNorthwest(),
		A_ShiftZDownSteps(4),
		A_ClearBit(TEMP_7043_6)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_43"),
	Return(),
	JmpIfBitSet(TEMP_7043_7, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_49"], identifier="EVENT_1775_jmp_if_bit_set_45"),
	SetBit(TEMP_7043_7),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(2),
		A_ShiftZDownSteps(3),
		A_Walk1StepSoutheast(),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(30),
		A_SetAllSpeeds(NORMAL),
		A_Walk1StepNorthwest(),
		A_ShiftZUpSteps(3),
		A_WalkNorthwestSteps(2),
		A_ClearBit(TEMP_7043_7)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_49"),
	Return(),
	JmpIfBitSet(TEMP_7044_0, ["EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_55"], identifier="EVENT_1775_jmp_if_bit_set_51"),
	SetBit(TEMP_7044_0),
	JmpToSubroutine(["EVENT_1775_jmp_if_bit_set_57"]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_WalkSoutheastSteps(3),
		A_ShiftZUpSteps(3),
		A_Pause(60),
		A_SetSequenceSpeed(VERY_FAST),
		A_Pause(60),
		A_SetAllSpeeds(NORMAL),
		A_ShiftZDownSteps(3),
		A_WalkNorthwestSteps(3),
		A_ClearBit(TEMP_7044_0)
	]),
	ReactivateObject70A8TriggerIfMarioOnTopOfIt(identifier="EVENT_1775_reactivate_trigger_if_mario_on_top_of_object_55"),
	Return(),
	JmpIfBitSet(TEMP_707C_0, ["EVENT_1775_clear_bit_60"], identifier="EVENT_1775_jmp_if_bit_set_57"),
	Set7016701BToObjectXYZ(target=MEM_70A8, bit_7=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_Set700CToObjectCoord(target_npc=MARIO, coord=COORD_F),
		A_FixedFCoordOn(),
		A_FloatingOff(),
		A_WalkTo70167018(),
		A_FloatingOn(),
		A_FixedFCoordOff(),
		A_FaceEast7C()
	]),
	ClearBit(TEMP_707C_0, identifier="EVENT_1775_clear_bit_60"),
	Return()
])
