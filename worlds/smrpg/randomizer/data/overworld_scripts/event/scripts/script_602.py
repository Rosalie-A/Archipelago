# E0602_MARRYMORE_INN_MANAGER
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
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_602_jmp_if_bit_set_58"]),
	JmpIfBitSet(EMPLOYMENT_704C_2, ["EVENT_602_jmp_if_bit_set_58"]),
	JmpIfBitSet(TEMP_704C_0, ["EVENT_602_run_dialog_56"]),
	JmpIfBitSet(TEMP_7042_5, ["EVENT_602_run_dialog_54"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_602_run_dialog_54"]),
	JmpIfBitSet(TEMP_7042_0, ["EVENT_602_run_dialog_52"]),
	RunDialog(dialog_id=DI2470_MARRYMORE_HOTEL_MENU, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBOrCSelected(['EVENT_602_run_dialog_10', 'EVENT_602_run_dialog_50']),
	CloseDialog(),
	JmpToEvent(E0646_MARRYMORE_SHOP_EVENT_CONTAINER),
	RunDialog(dialog_id=DI2508_MARRYMORE_HOTEL_ROOM_CHOICE, above_object=MEM_70A8, closable=False, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_10"),
	JmpIfDialogOptionBOrCSelected(["EVENT_602_hotel_check_for_voucher", 'EVENT_602_run_dialog_50']),
	SetVarToConst(SECONDARY_TEMP_7024, 10),
	ClearBit(UNKNOWN_7049_4),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_602_run_dialog_21"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	RunDialog(dialog_id=DI0974_ENJOY_YOUR_STAY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(MARRYMORE_REGULAR_INN),
	Jmp(["EVENT_273_fade_out_music_to_volume_17"]),
	RunDialog(dialog_id=DI2475_CANT_AFFORD_MARRYMORE_HOTEL, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_21"),
	Return(),

	StoreItemAmountTo7000(StayVoucherItem, identifier="EVENT_602_hotel_check_for_voucher"),
    JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["run_stay_voucher_dialog"]),
    

	SetVarToConst(SECONDARY_TEMP_7024, 200, identifier="EVENT_602_set_var_to_const_23"),
	ClearBit(UNKNOWN_7049_4),
	RunEventAsSubroutine(E0274_CHECK_IF_HAVE_ENOUGH_COINS),
	JmpIfBitSet(INSUFFICIENT_COINS, ["EVENT_602_run_dialog_21"]),
	CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
	Dec7000FromCoins(),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
    
	RunDialog(dialog_id=DI2122_STAY_VOUCHER_DIALOG, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="run_stay_voucher_dialog"),
    RunDialog(dialog_id=DI2123_STAY_VOUCHER_USE, above_object=BOWSER, closable=True, sync=False, multiline=False, use_background=False),
    RemoveOneOfItemFromInventory(StayVoucherItem),
	SetBit(STAY_VOUCHER_USED),
    # put culex's door back
    JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["hotel_check_prize_count"]),
	ApplyTileModToLevel(use_alternate=False, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=33),
	SummonObjectToSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
	

	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_602_set_bit_32"], identifier="hotel_check_prize_count"),
	Inc(MARRYMORE_SUITE_LEGAL_COUNT),
	SetBit(TEMP_7043_0, identifier="EVENT_602_set_bit_32"),
	CopyVarToVar(from_var=MARRYMORE_SUITE_LEGAL_COUNT, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI2473_STAYED_X_TIMES_IN_SUITE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	UnsyncDialog(),
	RememberLastObject(),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 255, ["EVENT_602_set_7010_to_object_xyz_39"]),
	RunEventAsSubroutine(E0708_MARRYMORE_TIP_DECISION_SUBROUTINE),
	Set70107015ToObjectXYZ(target=NPC_5, bit_7=True, identifier="EVENT_602_set_7010_to_object_xyz_39"),
	CompareVarToConst(X_COORD_1, 5),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_602_start_embedded_action_script_45"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_FaceNortheast(),
		A_Pause(30),
		A_FaceSoutheast()
	]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_Pause(30),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOff(),
		A_WalkNortheastSteps(2),
		A_WalkSoutheastSteps(4),
		A_WalkSouthwestSteps(2),
		A_SetSequenceSpeed(SLOW)
	]),
	Jmp(["EVENT_602_set_bit_46"]),
	StartSyncEmbeddedActionScript(target=NPC_5, prefix=0xF1, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_SetSequenceSpeed(FAST),
		A_FixedFCoordOff(),
		A_Walk1StepNorthwest(),
		A_WalkToXYCoords(x=6, y=61),
		A_WalkNorthwestSteps(2),
		A_FaceSouthwest(),
		A_SetSequenceSpeed(SLOW)
	], identifier="EVENT_602_start_embedded_action_script_45"),
	SetBit(TEMP_7042_0, identifier="EVENT_602_set_bit_46"),
	SetAsyncActionScript(NPC_5, A0636_54_VELOCITY_SINGLE_JUMP),
	SetSyncActionScript(NPC_5, A0301_MARRYMORE_BELLHOP_WHILE_PLAYER_WORKING),
	Return(),
	RunDialog(dialog_id=DI0976_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_50"),
	Return(),
	RunDialog(dialog_id=DI0973_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_52"),
	Return(),
	RunDialog(dialog_id=DI0998_THANK_YOU_VERY_MUCH, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_54"),
	Return(),
	RunDialog(dialog_id=DI1004_BREAK_EVERY_BONE_IN_YOUR_BODY, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_56"),
	Return(),
	JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_602_run_dialog_78"], identifier="EVENT_602_jmp_if_bit_set_58"),
	Set7000ToObjectCoord(target_npc=NPC_1, coord=COORD_F, pixel=True),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_602_run_dialog_83"]),
	CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
	Dec(PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_602_run_dialog_70"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
	RunDialog(dialog_id=DI1019_NOT_OFF_THE_HOOK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_WalkToXYCoords(x=3, y=55),
		A_FaceSoutheast(),
		A_Pause(30),
		A_SetSpriteSequence(index=6, is_sequence=True, looping=True, mirror_sprite=True),
		A_Pause(60),
		A_ResetProperties(),
		A_SetSequenceSpeed(SLOW),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_SetSolidityBits(cant_pass_walls=True),
		A_SequenceLoopingOn()
	]),
	ClearBit(EMPLOYMENT_704C_2),
	RunBackgroundEvent(event_id=E0617_MARIO_AS_BELLHOP_MAIN_EVENT, return_on_level_exit=True),
	Return(),
	RunDialog(dialog_id=DI1020_FINISHED_WORKING_AT_MARRYMORE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_70"),
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	ClearBit(EMPLOYMENT_704C_2),
	SetVarToConst(TEMP_70AC, 0),
	SetVarToConst(TEMP_70B8, 0),
	SetBit(EMPLOYMENT_704C_3),
	Return(),
	RunDialog(dialog_id=DI1014_SEE_GUEST_OUT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_78"),
	JmpIfBitSet(TEMP_7044_4, ["EVENT_256_ret_0"]),
	RunBackgroundEvent(event_id=E0623_MARRYMORE_INN_EMPLOYED_GUEST_LEAVES, return_on_level_exit=True),
	SetBit(TEMP_7044_4),
	Return(),
	RunDialog(dialog_id=DI1021_MARRYMORE_INNKEEPER_TELLS_YOU_TO_GO_BEHIND_COUNTER, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_602_run_dialog_83"),
	Return()
])
