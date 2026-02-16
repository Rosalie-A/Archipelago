# E3479_MIDAS_RIVER_SCORE_SUBMISSION
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
	SetVarToConst(TEMP_70AE, 23),
	JmpIfBitSet(UNKNOWN_MIDAS_RIVER_7079_1, ["EVENT_3479_run_dialog_132"]),
	JmpIfBitClear(TEMP_7043_1, ["EVENT_3479_run_dialog_95"]),
	JmpIfVarNotEqualsConst(TEMP_702A, 0, ["EVENT_3479_copy_var_to_var_6"]),
	RunDialog(dialog_id=DI1086_MIDAS_EXCHANGE, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3479_run_dialog_95"]),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3479_copy_var_to_var_6"),
	JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 100, ["EVENT_3479_jmp_if_bit_clear_9"]),
	SetBit(TEMP_7043_3),
	JmpIfBitClear(TEMP_7043_2, ["EVENT_3479_copy_var_to_var_13"], identifier="EVENT_3479_jmp_if_bit_clear_9"),
	SetVarToConst(MIDAS_RIVER_70CA, 60),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	Jmp(["EVENT_3479_copy_var_to_var_32"]),
	CopyVarToVar(from_var=MIDAS_RIVER_70B3, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3479_copy_var_to_var_13"),
	SetVarToConst(MIDAS_RIVER_70CA, 80),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	CompareVarToConst(PRIMARY_TEMP_7000, 70),
	JmpIfComparisonResultIsLesser(["EVENT_3479_copy_var_to_var_32"]),
	SetVarToConst(MIDAS_RIVER_70CA, 75),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	CompareVarToConst(PRIMARY_TEMP_7000, 80),
	JmpIfComparisonResultIsLesser(["EVENT_3479_copy_var_to_var_32"]),
	SetVarToConst(MIDAS_RIVER_70CA, 70),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	CompareVarToConst(PRIMARY_TEMP_7000, 90),
	JmpIfComparisonResultIsLesser(["EVENT_3479_copy_var_to_var_32"]),
	SetVarToConst(MIDAS_RIVER_70CA, 60),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	CompareVarToConst(PRIMARY_TEMP_7000, 100),
	JmpIfComparisonResultIsLesser(["EVENT_3479_copy_var_to_var_32"]),
	SetVarToConst(MIDAS_RIVER_70CA, 50),
	SetVarToConst(SECONDARY_TEMP_7024, 1),
	CopyVarToVar(from_var=MIDAS_RIVER_70CA, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3479_copy_var_to_var_32"),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	RunDialog(dialog_id=DI1076_MIDAS_EXCHANGE, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3479_copy_var_to_var_43"]),
	CopyVarToVar(from_var=MIDAS_RIVER_70B3, to_var=PRIMARY_TEMP_7000),
	Compare7000ToVar(TEMP_702A),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3479_copy_var_to_var_43"]),
	RunDialog(dialog_id=DI1087_MIDAS_EXCHANGE, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=MIDAS_RIVER_70B3),
	CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3479_copy_var_to_var_43"),
	JmpIfBitSet(TEMP_7043_2, ["EVENT_3479_run_dialog_duration_47"]),
	RunDialogForDuration(dialog_id=DI1043_MIDAS_EXCHANGE, duration=0, sync=False),
	Jmp(["EVENT_3479_copy_var_to_var_48"]),
	RunDialogForDuration(dialog_id=DI1037_DUPLICATE, duration=0, sync=False, identifier="EVENT_3479_run_dialog_duration_47"),
	CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000, identifier="EVENT_3479_copy_var_to_var_48"),
	JmpIfVarEqualsConst(MIDAS_RIVER_70D4, 0, ["EVENT_3479_compare_7000_to_var_53"]),
	RunDialogForDuration(dialog_id=DI1044_MIDAS_EXCHANGE, duration=0, sync=False),
	CopyVarToVar(from_var=MIDAS_RIVER_70D4, to_var=PRIMARY_TEMP_7000),
	AddVarTo7000(TEMP_702A),
	Compare7000ToVar(TEMP_7026, identifier="EVENT_3479_compare_7000_to_var_53"),
	JmpIfComparisonResultIsLesser(["EVENT_3479_copy_var_to_var_76"]),
	RunDialogForDuration(dialog_id=DI1045_MIDAS_EXCHANGE, duration=0, sync=False),
	SetVarToConst(TEMP_7028, 0),
	Inc(TEMP_7028, identifier="EVENT_3479_inc_57"),
	DecVarFrom7000(TEMP_7026),
	Compare7000ToVar(TEMP_7026),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3479_inc_57"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=MIDAS_RIVER_70D4),
	SetVarToConst(PRIMARY_TEMP_7000, 0),
	SetObjectMemoryToVar(TEMP_7028),
	AddVarTo7000(SECONDARY_TEMP_7024),
	EndLoop(),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7028),
	RunDialogForDuration(dialog_id=DI1046_MIDAS_EXCHANGE, duration=1, sync=False),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3479_jmp_to_subroutine_72"]),
	RunDialog(dialog_id=DI1039_MIDAS_EXCHANGE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	AddConstToVar(PRIMARY_TEMP_7000, 5),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7028),
	JmpToSubroutine(["EVENT_3479_action_queue_135"], identifier="EVENT_3479_jmp_to_subroutine_72"),
	CopyVarToVar(from_var=MIDAS_RIVER_70D4, to_var=PRIMARY_TEMP_7000),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3479_jmp_if_bit_set_83"]),
	Jmp(["EVENT_3479_jmp_if_bit_set_83"]),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=MIDAS_RIVER_70D4, identifier="EVENT_3479_copy_var_to_var_76"),
	RunDialogForDuration(dialog_id=DI1042_MIDAS_EXCHANGE, duration=1, sync=False),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	JmpIfBitClear(TEMP_7043_3, ["EVENT_3479_jmp_if_bit_set_83"]),
	RunDialog(dialog_id=DI1038_MIDAS_EXCHANGE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	SetVarToConst(TEMP_7028, 5),
	JmpToSubroutine(["EVENT_3479_action_queue_135"]),
	JmpIfBitSet(MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED, ["EVENT_3479_jmp_if_bit_set_85"], identifier="EVENT_3479_jmp_if_bit_set_83"),
	JmpIfVarNotEqualsConst(TEMP_702A, 0, ["EVENT_3479_run_event_as_subroutine_88"]),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3479_action_queue_92"], identifier="EVENT_3479_jmp_if_bit_set_85"),
	Return(),
	Return(),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER, identifier="EVENT_3479_run_event_as_subroutine_88"),
	SetBit(MIDAS_RIVER_FIRST_VISIT_PRIZE_RECEIVED),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3479_action_queue_92"]),
	Return(),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkSouthwestSteps(4),
		A_Walk1StepSoutheast(),
		A_SetAllSpeeds(NORMAL)
	], identifier="EVENT_3479_action_queue_92"),
	ClearBit(TEMP_7043_1),
	Return(),
	RunDialog(dialog_id=DI1077_MIDAS_EXCHANGE, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False, identifier="EVENT_3479_run_dialog_95"),
	JmpIfBitSet(TEMP_7043_1, ["EVENT_3479_run_dialog_duration_101"]),
	CopyVarToVar(from_var=MIDAS_RIVER_70D4, to_var=PRIMARY_TEMP_7000),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
	CopyVarToVar(from_var=MIDAS_RIVER_70B3, to_var=PRIMARY_TEMP_7000),
	RunDialogForDuration(dialog_id=DI1075_MIDAS_EXCHANGE, duration=0, sync=False),
	RunDialogForDuration(dialog_id=DI1082_MIDAS_EXCHANGE, duration=1, sync=False, identifier="EVENT_3479_run_dialog_duration_101"),
	JmpIfDialogOptionBSelected(["EVENT_3479_pause_128"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	StoreCoinCountTo7000(),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_3479_set_var_to_const_121"]),
	RunDialog(dialog_id=DI1081_MIDAS_EXCHANGE, above_object=NPC_12, closable=False, sync=False, multiline=True, use_background=False),
	CopyVarToVar(from_var=MIDAS_RIVER_70D4, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 30),
	JmpIfComparisonResultIsLesser(["EVENT_3479_run_dialog_duration_119"]),
	RunDialogForDuration(dialog_id=DI1040_MIDAS_EXCHANGE, duration=1, sync=False),
	JmpIfDialogOptionBSelected(["EVENT_3479_pause_128"]),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	CopyVarToVar(from_var=MIDAS_RIVER_70D4, to_var=PRIMARY_TEMP_7000),
	AddConstToVar(PRIMARY_TEMP_7000, 65506),
	CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=MIDAS_RIVER_70D4),
	Jmp(["EVENT_3479_run_dialog_123"]),
	RunDialogForDuration(dialog_id=DI1079_MIDAS_EXCHANGE, duration=1, sync=False, identifier="EVENT_3479_run_dialog_duration_119"),
	Jmp(["EVENT_3479_jmp_if_bit_set_83"]),
	SetVarToConst(PRIMARY_TEMP_7000, 30, identifier="EVENT_3479_set_var_to_const_121"),
	Dec7000FromCoins(),
	RunDialog(dialog_id=DI1078_MIDAS_EXCHANGE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3479_run_dialog_123"),
	PlaySound(sound=SO055_LOSE_COINS_COIN_FOUNTAIN, channel=6),
	SetBit(TEMP_7043_0),
	SetBit(UNKNOWN_MIDAS_RIVER_7079_1),
	Jmp(["EVENT_3479_jmp_if_bit_set_83"]),
	Pause(10, identifier="EVENT_3479_pause_128"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1079_MIDAS_EXCHANGE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	Jmp(["EVENT_3479_jmp_if_bit_set_83"]),
	RunDialog(dialog_id=DI1080_MIDAS_EXCHANGE, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3479_run_dialog_132"),
	SetBit(TEMP_7043_0),
	Return(),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=9, sprite_offset=2, is_sequence=True, looping=True)
	], identifier="EVENT_3479_action_queue_135"),
	SetObjectMemoryToVar(TEMP_7028),
	ActionQueueAsync(target=NPC_5, subscript=[
		A_PlaySound(sound=SO094_FROG_COIN, channel=4),
		A_ShadowOn(),
		A_SetVRAMPriority(PRIORITY_3),
		A_SetPriority(3),
		A_SetSpriteSequence(index=1, is_sequence=True, looping=True),
		A_UnknownCommand(bytearray(b'\x97\x17')),
		A_SetAllSpeeds(FASTEST),
		A_ShiftZUpPixels(16),
		A_SetAllSpeeds(NORMAL),
		A_VisibilityOn(),
		A_FloatingOff(),
		A_JumpToHeight(height=80, silent=True),
		A_Walk1StepNortheast(),
		A_VisibilityOff()
	]),
	SetVarToConst(PRIMARY_TEMP_7000, 1),
	AddFrogCoins(PRIMARY_TEMP_7000),
	EndLoop(),
	ActionQueueSync(target=MARIO, subscript=[
		A_ResetProperties()
	]),
	Return()
])
