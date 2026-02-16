# E2637_CASINO_GRATE_GUY
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
	ActionQueueSync(target=NPC_1, subscript=[
		A_SequenceLoopingOff()
	], identifier="EVENT_2637_action_queue_0"),
	ActionQueueAsync(target=MARIO, subscript=[
		A_OverwriteSolidity(),
		A_WalkToXYCoords(x=4, y=16),
		A_FaceNortheast()
	]),
	RunDialog(dialog_id=DI3304_AWAIT_LEFT_OR_RIGHT, above_object=BOWSER, closable=False, sync=True, multiline=True, use_background=False),
	Set7000ToPressedButton(identifier="EVENT_2637_set_7000_to_pressed_button_3"),
	Pause(1),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_2637_close_dialog_8"]),
	JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_2637_close_dialog_20"]),
	Jmp(["EVENT_2637_set_7000_to_pressed_button_3"]),
	CloseDialog(identifier="EVENT_2637_close_dialog_8"),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=11, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfRandom1of2(["EVENT_2637_action_queue_16"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
	Jmp(["EVENT_2637_play_sound_32"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	], identifier="EVENT_2637_action_queue_16"),
	Pause(30),
	RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
	Jmp(["EVENT_2637_play_sound_36"]),
	CloseDialog(identifier="EVENT_2637_close_dialog_20"),
	Pause(16),
	ActionQueueSync(target=MARIO, subscript=[
		A_SetSpriteSequence(index=10, is_mold=True, is_sequence=True, looping=True, mirror_sprite=True)
	]),
	JmpIfRandom1of2(["EVENT_2637_action_queue_28"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=3, is_sequence=True, looping=True)
	]),
	Pause(30),
	RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
	Jmp(["EVENT_2637_play_sound_36"]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetSpriteSequence(index=2, is_sequence=True, looping=True)
	], identifier="EVENT_2637_action_queue_28"),
	Pause(30),
	RunEventAsSubroutine(E2646_CASINO_GRATE_GUY_AWAIT_BUTTON),
	Jmp(["EVENT_2637_play_sound_32"]),
	PlaySound(sound=SO088_WRONG_SIGNAL, channel=6, identifier="EVENT_2637_play_sound_32"),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn()
	]),
	Jmp(["EVENT_2637_run_dialog_50"]),
	PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6, identifier="EVENT_2637_play_sound_36"),
	Pause(25),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ResetProperties(),
		A_SequenceLoopingOn()
	]),
	JmpIfBitSet(CASINO_PRIZE_WON, ["EVENT_2637_run_event_as_subroutine_45"]),
	Inc(UNKNOWN_70EF),
	CopyVarToVar(from_var=UNKNOWN_70EF, to_var=PRIMARY_TEMP_7000),
	RunEventAsSubroutine(E2650_CASINO_GRATE_GUY_CHECK_IF_SIDEQUEST_COMPLETED),
	JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2637_run_dialog_47"]),
	RunEventAsSubroutine(E2649_CASINO_GRATE_GUY_RANDOM_PRIZE_GRANTER, identifier="EVENT_2637_run_event_as_subroutine_45"),
	PlaySound(sound=SO027_FOUND_AN_ITEM, channel=6),
	RunDialog(dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=False),
	AddToInventory(ITEM_ID),
	Jmp(["EVENT_2637_run_dialog_50"]),
	RunDialog(dialog_id=DI3308_LOOK_THE_OTHER_WAY_PRIZE, above_object=BOWSER, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2637_run_dialog_47"),
	SetBit(CASINO_PRIZE_WON),
	RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
	RunDialog(dialog_id=DI3310_LOOK_THE_OTHER_WAY_RETRY, above_object=NPC_12, closable=True, sync=False, multiline=True, use_background=True, identifier="EVENT_2637_run_dialog_50"),
	JmpIfDialogOptionBSelected(["EVENT_2637_pause_55"]),
	Pause(10),
	SetAsyncActionScript(MARIO, A0670_NOD_YES),
	Jmp(["EVENT_2637_action_queue_0"]),
	Pause(10, identifier="EVENT_2637_pause_55"),
	SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
	Return()
])
