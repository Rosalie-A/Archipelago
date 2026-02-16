# E1834_KEEP_CANNONBALL
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
	JmpIfBitClear(TEMP_7043_0, ["EVENT_1834_set_bit_2"]),
	Return(),
	SetBit(TEMP_7043_0, identifier="EVENT_1834_set_bit_2"),
	SetVarToConst(TEMP_7026, 0),
	Set7016701BToObjectXYZ(target=NPC_0),
	JmpToSubroutine(["EVENT_1834_action_queue_55"]),
	MoveScriptToBackgroundThread2(),
	Pause(1, identifier="EVENT_1834_pause_7"),
	Set7000ToTappedButton(),
	JmpIf7000AnyBitsSet(bits=[7], destinations=["EVENT_1834_action_queue_50"]),
	Set7000ToPressedButton(),
	Mem7000AndConst(0x000F),
	Compare7000ToVar(TEMP_7026),
	JmpIfLoadedMemoryIsNot0(["EVENT_1834_clear_bit_17"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1834_pause_7"]),
	SetBit(TEMP_7043_1),
	Jmp(["EVENT_1834_action_queue_48"]),
	ClearBit(TEMP_7043_1, identifier="EVENT_1834_clear_bit_17"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_1834_set_var_to_const_31"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_1834_set_var_to_const_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_1834_set_var_to_const_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1834_set_var_to_const_37"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1834_set_var_to_const_43"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_1834_set_var_to_const_45"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1834_set_var_to_const_39"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_1834_set_var_to_const_41"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOff()
	]),
	StopSound(),
	Jmp(["EVENT_1834_pause_7"]),
	SetVarToConst(Z_COORD_1, 3, identifier="EVENT_1834_set_var_to_const_31"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 5, identifier="EVENT_1834_set_var_to_const_33"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 1, identifier="EVENT_1834_set_var_to_const_35"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 7, identifier="EVENT_1834_set_var_to_const_37"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 0, identifier="EVENT_1834_set_var_to_const_39"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 2, identifier="EVENT_1834_set_var_to_const_41"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 4, identifier="EVENT_1834_set_var_to_const_43"),
	Jmp(["EVENT_1834_action_queue_47"]),
	SetVarToConst(Z_COORD_1, 6, identifier="EVENT_1834_set_var_to_const_45"),
	Jmp(["EVENT_1834_action_queue_47"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO048_MINECART_START, channel=4),
		A_CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C(),
		A_SetSequenceSpeed(FAST),
		A_SequenceLoopingOn()
	], identifier="EVENT_1834_action_queue_47"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_JmpIfBitSet(TEMP_7043_1, ["EVENT_1834_action_queue_48_SUBSCRIPT_copy_var_to_var_2"]),
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True),
		A_CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_700C, identifier="EVENT_1834_action_queue_48_SUBSCRIPT_copy_var_to_var_2"),
		A_FaceEast7C(),
		A_WalkFDirectionPixels(1)
	], identifier="EVENT_1834_action_queue_48"),
	Jmp(["EVENT_1834_pause_7"]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=0, is_sequence=True, looping=True)
	], identifier="EVENT_1834_action_queue_50"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetSequenceSpeed(NORMAL),
		A_SequenceLoopingOff(),
		A_JumpToHeight(128)
	]),
	MoveScriptToMainThread(),
	ClearBit(TEMP_7043_0),
	Return(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SetAllSpeeds(FAST),
		A_SetSpriteSequence(index=4, is_sequence=True, looping=True),
		A_StartLoopNTimes(3),
		A_PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=4),
		A_Pause(4),
		A_EndLoop()
	], identifier="EVENT_1834_action_queue_55"),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_F, pixel=True),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Z_COORD_1),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_X, pixel=True),
	Compare7000ToVar(X_COORD_2),
	JmpIfLoadedMemoryIs0(["EVENT_1834_set_7000_to_object_coord_70"]),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1834_set_var_to_const_65"]),
	SetVarToConst(PRIMARY_TEMP_700C, 0),
	SwapVars(X_COORD_2, PRIMARY_TEMP_7000),
	Jmp(["EVENT_1834_dec_var_from_7000_66"]),
	SetVarToConst(PRIMARY_TEMP_700C, 4, identifier="EVENT_1834_set_var_to_const_65"),
	DecVarFrom7000(X_COORD_2, identifier="EVENT_1834_dec_var_from_7000_66"),
	VarShiftLeft(PRIMARY_TEMP_7000, 4),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=X_COORD_1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=4),
		A_FaceEast7C(),
		A_CopyVarToVar(from_var=X_COORD_1, to_var=PRIMARY_TEMP_700C),
		A_WalkFDirection16Pixels()
	]),
	Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, identifier="EVENT_1834_set_7000_to_object_coord_70"),
	Compare7000ToVar(Y_COORD_2),
	JmpIfLoadedMemoryIs0(["EVENT_1834_action_queue_82"]),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1834_set_var_to_const_77"]),
	SetVarToConst(PRIMARY_TEMP_700C, 2),
	SwapVars(Y_COORD_2, PRIMARY_TEMP_7000),
	Jmp(["EVENT_1834_dec_var_from_7000_78"]),
	SetVarToConst(PRIMARY_TEMP_700C, 6, identifier="EVENT_1834_set_var_to_const_77"),
	DecVarFrom7000(Y_COORD_2, identifier="EVENT_1834_dec_var_from_7000_78"),
	VarShiftLeft(PRIMARY_TEMP_7000, 4),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=Y_COORD_1),
	ActionQueueAsync(target=MARIO, subscript=[
		A_PlaySound(sound=SO043_POP_UP_FROM_WATER, channel=4),
		A_FaceEast7C(),
		A_CopyVarToVar(from_var=Y_COORD_1, to_var=PRIMARY_TEMP_700C),
		A_WalkFDirection16Pixels()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkWestPixels(1),
		A_ResetProperties(),
		A_CopyVarToVar(from_var=Z_COORD_1, to_var=PRIMARY_TEMP_700C),
		A_FaceEast7C(),
		A_SetAllSpeeds(NORMAL),
		A_FloatingOn(),
		A_SetSolidityBits(cant_pass_walls=True)
	], identifier="EVENT_1834_action_queue_82"),
	Return()
])
