# E1852_SKY_BRIDGE_ADMIN_SHAMAN
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
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
	JmpIfMarioOnAnObjectOrNot(['EVENT_1852_set_action_script_20', 'EVENT_1852_set_action_script_57']),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_1852_stop_all_background_events_59"]),
	RunDialog(dialog_id=DI1300_DUPLICATE, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1852_pause_7"]),
	Jmp(["EVENT_1852_pause_12"]),
	Pause(10, identifier="EVENT_1852_pause_7"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ClearBit(TEMP_7044_7),
	SetSyncActionScript(MARIO, A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM),
	Return(),
	Pause(10, identifier="EVENT_1852_pause_12"),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ClearBit(TEMP_7044_7),
	RunDialog(dialog_id=DI1305_SKY_BRIDGE_5_COIN_PAY, above_object=NPC_17, closable=False, sync=False, multiline=True, use_background=True),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 5),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1852_play_sound_22"]),
	RunDialogForDuration(dialog_id=DI1306_SKY_BRIDGE_INSUFFICIENT_COINS, duration=1, sync=False),
	SetSyncActionScript(MARIO, A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM, identifier="EVENT_1852_set_action_script_20"),
	Return(),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6, identifier="EVENT_1852_play_sound_22"),
	SetVarToConst(PRIMARY_TEMP_7000, 5),
	Dec7000FromCoins(),
	JmpIfBitSet(SKY_BRIDGE_TUTORIAL_BIT, ["EVENT_1852_run_dialog_37"]),
	RunDialog(dialog_id=DI1302_SKY_BRIDGE_TUTORIAL_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	JmpIfDialogOptionBSelected(["EVENT_1852_pause_34"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ClearBit(TEMP_7044_7),
	SetBit(SKY_BRIDGE_TUTORIAL_BIT),
	RunDialog(dialog_id=DI1303_SKY_BRIDGE_TUTORIAL, above_object=NPC_17, closable=False, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_1852_run_dialog_37"]),
	Pause(10, identifier="EVENT_1852_pause_34"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ClearBit(TEMP_7044_7),
	RunDialog(dialog_id=DI1304_SKY_BRIDGE_LEVEL_SELECT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1852_run_dialog_37"),
	JmpIfDialogOptionBOrCSelected(['EVENT_1852_set_var_to_const_43', 'EVENT_1852_set_var_to_const_47']),
	SetVarToConst(TEMP_7026, 5),
	SetBit(SKY_BRIDGE_COURSE_CHOICE),
	SetBit(SKY_BRIDGE_COURSE_1_CHOSEN),
	Jmp(["EVENT_1852_set_var_to_const_50"]),
	SetVarToConst(TEMP_7026, 8, identifier="EVENT_1852_set_var_to_const_43"),
	SetBit(SKY_BRIDGE_COURSE_CHOICE),
	ClearBit(SKY_BRIDGE_COURSE_1_CHOSEN),
	Jmp(["EVENT_1852_set_var_to_const_50"]),
	SetVarToConst(TEMP_7026, 1, identifier="EVENT_1852_set_var_to_const_47"),
	ClearBit(SKY_BRIDGE_COURSE_CHOICE),
	ClearBit(SKY_BRIDGE_COURSE_1_CHOSEN),
	SetVarToConst(TEMP_702E, 48, identifier="EVENT_1852_set_var_to_const_50"),
	SetVarToConst(TEMP_702C, 100),
	RunDialog(dialog_id=DI1314_SKY_BRIDGE_GOOD_LUCK, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True),
	SetBit(TEMP_7043_2),
	SetVarToConst(TEMP_7028, 1),
	ActionQueueAsync(target=NPC_17, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO161_GHOST, channel=4),
		A_JumpToHeight(128),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_FloatingOff(),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True),
		A_TransferToXYZF(x=10, y=76, z=19, direction=EAST),
		A_FaceSouthwest()
	], identifier="EVENT_1852_action_queue_55"),
	RunBackgroundEvent(event_id=E1732_SKY_BRIDGE_BACKGROUND, return_on_level_exit=True),
	SetSyncActionScript(MARIO, A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM, identifier="EVENT_1852_set_action_script_57"),
	Return(),
	StopAllBackgroundEvents(identifier="EVENT_1852_stop_all_background_events_59"),
	ClearBit(TEMP_7043_0),
	ClearBit(TEMP_7044_3),
	JmpIfVarNotEqualsConst(TEMP_7028, 3, ["EVENT_1852_run_dialog_65"]),
	RunDialog(dialog_id=DI1308_SKY_BRIDGE_CONGRATS, above_object=NPC_17, closable=False, sync=False, multiline=True, use_background=True),
	Jmp(["EVENT_1852_run_dialog_83"]),
	RunDialog(dialog_id=DI1307_SKY_BRIDGE_DOUBLE_PROMPT, above_object=MEM_70A8, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_1852_run_dialog_65"),
	JmpIfDialogOptionBSelected(["EVENT_1852_pause_80"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	ClearBit(TEMP_7044_7),
	Inc(TEMP_7028),
	VarShiftLeft(TEMP_7026, 255),
	AddConstToVar(TEMP_702E, 65520),
	AddConstToVar(TEMP_702C, 65516),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetWalkingSpeed(FAST),
		A_ClearSolidityBits(cant_pass_walls=True),
		A_JumpToHeight(108),
		A_WalkToXYCoords(x=10, y=76),
		A_Pause(1, identifier="EVENT_1852_action_queue_74_SUBSCRIPT_pause_4"),
		A_JmpIfMarioInAir(["EVENT_1852_action_queue_74_SUBSCRIPT_pause_4"])
	]),
	Pause(1),
	ActionQueueSync(target=MARIO, subscript=[
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=20, y=104)
	]),
	ActionQueueAsync(target=NPC_17, subscript=[
		A_SetWalkingSpeed(SLOW),
		A_AddZCoord1Step(),
		A_SetWalkingSpeed(VERY_FAST),
		A_WalkToXYCoords(x=20, y=104)
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(NORMAL),
		A_FloatingOn(),
		A_SequencePlaybackOn(),
		A_SetSolidityBits(cant_pass_walls=True)
	]),
	Jmp(["EVENT_1852_action_queue_55"]),
	Pause(10, identifier="EVENT_1852_pause_80"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	ClearBit(TEMP_7044_7),
	ActionQueueAsync(target=NPC_17, subscript=[
		A_SetSpriteSequence(index=4, looping=False),
		A_Pause(40)
	], identifier="EVENT_1852_run_dialog_83"),
	JmpIfBitSet(SKY_BRIDGE_COURSE_CHOICE, ["EVENT_1852_play_sound_91"]),
	PlaySound(sound=SO094_FROG_COIN, channel=6),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	AddFrogCoins(PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1310_RECEIVED_X_FROG_COINS, above_object=TOADSTOOL, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_1852_action_queue_95"]),
	PlaySound(sound=SO013_COIN, channel=6, identifier="EVENT_1852_play_sound_91"),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
	AddCoins(PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1311_RECEIVED_X_COINS, above_object=TOADSTOOL, closable=True, sync=False, multiline=True, use_background=False),
	ActionQueueSync(target=NPC_18, subscript=[
		A_StartLoopNTimes(3),
		A_TurnClockwise45DegreesNTimes(2),
		A_Pause(1),
		A_EndLoop()
	], identifier="EVENT_1852_action_queue_95"),
	ActionQueueAsync(target=NPC_17, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_PlaySound(sound=SO161_GHOST, channel=4),
		A_JumpToHeight(128),
		A_StartLoopNTimes(4),
		A_VisibilityOff(),
		A_Pause(1),
		A_VisibilityOn(),
		A_Pause(2),
		A_EndLoop(),
		A_FloatingOff(),
		A_SetSolidityBits(bit_4=True, cant_walk_through=True),
		A_TransferToXYZF(x=20, y=104, z=18, direction=EAST),
		A_FaceSouthwest()
	]),
	ClearBit(TEMP_7043_2),
	SetSyncActionScript(MARIO, A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM),
	Return()
])
