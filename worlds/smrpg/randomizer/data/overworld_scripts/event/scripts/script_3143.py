# E3143_ROSE_WAY_MAIN_ROOM_PLATFORMS
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
	FreezeCamera(),
	CopyVarToVar(from_var=TEMP_70AA, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3143_copy_var_to_var_1"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7034),
	EnableControlsUntilReturn([X, B]),
	StartSyncEmbeddedActionScript(target=SCREEN_FOCUS, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_UnknownCommand(bytearray(b'\xc8\x92')),
		A_AddConstToVar(X_COORD_2, 65532),
		A_AddConstToVar(Y_COORD_2, 65522),
		A_WalkTo70167018()
	]),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST)
	]),
	ActionQueueSync(target=MEM_70AA, subscript=[
		A_SetWalkingSpeed(FAST)
	]),
	JmpIfMarioInAir(["EVENT_3143_set_7000_to_pressed_button_11"]),
	Set7000ToTappedButton(),
	JmpIf7000AllBitsClear(bits=[7], destinations=["EVENT_3143_set_7000_to_pressed_button_11"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_UnknownCommand(bytearray(b'\xfd\x9c\x04')),
		A_JumpToHeight(height=108, silent=True)
	]),
	Set7000ToPressedButton(identifier="EVENT_3143_set_7000_to_pressed_button_11"),
	Mem7000AndConst(0x000F),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_3143_set_var_to_const_23"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 5, ["EVENT_3143_set_var_to_const_25"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_3143_set_var_to_const_27"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_3143_set_var_to_const_29"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_3143_set_var_to_const_31"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 10, ["EVENT_3143_set_var_to_const_33"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 8, ["EVENT_3143_set_var_to_const_35"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 9, ["EVENT_3143_set_var_to_const_37"]),
	CopyVarToVar(from_var=TEMP_7032, to_var=PRIMARY_TEMP_700C),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 0, identifier="EVENT_3143_set_var_to_const_23"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 1, identifier="EVENT_3143_set_var_to_const_25"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 2, identifier="EVENT_3143_set_var_to_const_27"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 3, identifier="EVENT_3143_set_var_to_const_29"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 4, identifier="EVENT_3143_set_var_to_const_31"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 5, identifier="EVENT_3143_set_var_to_const_33"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 6, identifier="EVENT_3143_set_var_to_const_35"),
	Jmp(["EVENT_3143_copy_var_to_var_38"]),
	SetVarToConst(PRIMARY_TEMP_700C, 7, identifier="EVENT_3143_set_var_to_const_37"),
	CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7032, identifier="EVENT_3143_copy_var_to_var_38"),
	ClearBit(TEMP_7043_4),
	Set7016701BToObjectXYZ(target=MEM_70AA),
	StartSyncEmbeddedActionScript(target=MARIO, prefix=0xF1, subscript=[
		A_SetPriority(3),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_SequencePlaybackOff(),
		A_ShadowOn(),
		A_FaceEast7C(),
		A_AddConstToVar(X_COORD_2, 48),
		A_TransferTo70167018()
	]),
	Pause(1),
	JmpIfBitSet(TEMP_7043_0, ["EVENT_3143_copy_var_to_var_1"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO051_MOVING_YELLOW_SWITCH, channel=4),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	SetVarToConst(TEMP_7034, 0),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	StartLoopNTimes(47),
	JmpIfMarioInAir(["EVENT_3143_enable_controls_until_return_54"]),
	Pause(1),
	EndLoop(),
	JmpIfMarioInAir(["EVENT_3143_enable_controls_until_return_54"]),
	ActionQueueSync(target=MARIO, subscript=[
		A_PlaySound(sound=SO051_MOVING_YELLOW_SWITCH, channel=4),
		A_ClearSolidityBits(cant_pass_walls=True)
	]),
	Jmp(["EVENT_3143_copy_var_to_var_1"]),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B], identifier="EVENT_3143_enable_controls_until_return_54"),
	CopyVarToVar(from_var=TEMP_70AE, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
	EnableObjectTrigger(MEM_70AA),
	UnfreezeCamera(),
	StartSyncEmbeddedActionScript(target=SCREEN_FOCUS, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(NORMAL)
	]),
	StartSyncEmbeddedActionScript(target=MEM_70AA, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4])
	]),
	SetVarToConst(TEMP_70AA, 0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SequencePlaybackOn(),
		A_ObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
		A_SetSolidityBits(cant_pass_walls=True),
		A_ShadowOff()
	]),
	Return()
])
