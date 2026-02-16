# E3507_BOOSTER_HILL_2ND_PASS_LOADER
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
	SetVarToConst(TEMP_7032, 0),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ObjectMemorySetBit(arg_1=0x0B, bits=[3])
	]),
	SetVarToConst(SECONDARY_TEMP_7024, 0),
	SetVarToConst(TEMP_7034, 16),
	SetVarToConst(TEMP_7026, 1),
	SetVarToRandom(TEMP_702C, 6),
	Inc(TEMP_702C),
	SetVarToConst(TEMP_70AF, 3),
	FreezeCamera(),
	ActionQueueSync(target=MARIO, subscript=[
		A_TransferToXYZF(x=11, y=67, z=0, direction=EAST)
	]),
	ActionQueueSync(target=LAYER_3, subscript=[
		A_SetWalkingSpeed(FAST),
		A_WalkNorthwestSteps(18)
	]),
	FadeInFromBlack(sync=False),
	SetVarToConst(TEMP_70AE, 26),
	ActionQueueAsync(target=MARIO, subscript=[
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(8)
	]),
    RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3819_no_star"]),
	RunEventAsSubroutine(E3842_BOOSTER_HILL_STAR_PIECE_SIGNAL),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=11, y=67, z=0, direction=EAST),
		A_SetPriority(3),
		A_VisibilityOn(),
		A_SetAllSpeeds(FAST),
		A_WalkNorthwestSteps(7),
		A_JumpToHeight(64)
	], identifier="EVENT_3819_no_star"),
    
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceSoutheast()
	]),
    
	JmpIfBitClear(BOOSTER_HILL_CLOSED, ["booster_hill_already_done"]),
	RunDialog(dialog_id=DI1197_BOOSTER_HILL_NOT_UNLOCKED_YET, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3507_copy_var_to_var_26"]),
    Jmp(["EVENT_3507_pause_18"]),

	RunDialog(dialog_id=DI1199_TOAD_WARNS_YOU_TO_LEAVE_EMPTY_HILL, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="booster_hill_already_done"),
	JmpIfDialogOptionBSelected(["EVENT_3507_copy_var_to_var_26"]),
	Pause(10, identifier="EVENT_3507_pause_18"),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	RunDialog(dialog_id=DI1200_TOAD_TAKES_YOU_OUT_OF_HILL, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkSoutheastSteps(7),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_WalkSoutheastSteps(7),
		A_VisibilityOff()
	]),
	RunEventAtReturn(E3510_BOOSTER_HILL_EXIT_TO_WORLD_MAP),
	Return(),
	JmpIfBitSet(BOOSTER_HILL_CLOSED, ["EVENT_3507_pause_38"], identifier="EVENT_3507_copy_var_to_var_26"),
	CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
	CompareVarToConst(PRIMARY_TEMP_7000, 8),
	JmpIfComparisonResultIsLesser(["EVENT_3507_pause_38"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	JmpIfBitSet(UNKNOWN_704E_2, ["EVENT_3507_run_dialog_35"]),
	RunDialog(dialog_id=DI1203_TOAD_TELLS_YOU_THERES_NOTHING_LEFT, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	JmpIfDialogOptionBSelected(["EVENT_3507_pause_38"]),
	Jmp(["EVENT_3507_pause_18"]),
	RunDialog(dialog_id=DI1202_TOAD_TELLS_YOU_THERES_NO_FLOWERS, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False, identifier="EVENT_3507_run_dialog_35"),
	JmpIfDialogOptionBSelected(["EVENT_3507_pause_38"]),
	Jmp(["EVENT_3507_pause_18"]),
	Pause(10, identifier="EVENT_3507_pause_38"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	RunDialog(dialog_id=DI1201_WHATEVER, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=False),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
	ActionQueueAsync(target=NPC_6, subscript=[
		A_ResetProperties(),
		A_WalkSoutheastSteps(6),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FaceNorthwest(),
		A_FixedFCoordOn(),
		A_SetWalkingSpeed(NORMAL),
		A_SequenceLoopingOn()
	]),
	RunBackgroundEvent(event_id=E3511_BOOSTER_HILL_2ND_PASS_BACKGROUND, return_on_level_exit=True, bit_6=True),
	SetSyncActionScript(LAYER_1, A0704_BOOSTER_HILL_LAYER_1),
	SetSyncActionScript(LAYER_2, A0655_BOOSTER_HILL_LAYER_2),
	SetSyncActionScript(LAYER_3, A0705_BOOSTER_HILL_LAYER_3),
	SetBit(UNKNOWN_707B_4),
	RunEventAtReturn(E3502_BOOSTER_HILL_END),
	Return()
])
