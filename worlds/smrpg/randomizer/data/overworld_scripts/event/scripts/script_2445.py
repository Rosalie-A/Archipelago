# E2445_TOWER_SMALL_SAVE_ROOM_LOADER
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
	PlaySound(sound=SO000_SILENCE, channel=6),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2445_fade_in_from_black_async_15"]),
	EnableControlsUntilReturn([]),
	FreezeCamera(),
	ActionQueueAsync(target=MARIO, subscript=[
		A_ShadowOn(),
		A_ResetProperties(),
		A_FaceSouth(),
		A_FloatingOff(),
		A_SequencePlaybackOff(),
		A_SetPriority(3)
	]),
	FadeInFromBlack(sync=False),
	ActionQueueAsync(target=MARIO, subscript=[
		A_FloatingOn(),
		A_Pause(1, identifier="EVENT_2445_action_queue_6_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_2445_action_queue_6_SUBSCRIPT_pause_1"]),
		A_JumpToHeight(108),
		A_ShadowOff(),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_2445_action_queue_6_SUBSCRIPT_pause_6"),
		A_JmpIfMarioInAir(["EVENT_2445_action_queue_6_SUBSCRIPT_pause_6"])
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(TEMP_7044_7),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2445_ret_14"]),
	RunEventAsSubroutine(E3899_BOOSTER_TOWER_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2445_ret_14"),
	FadeInFromBlack(sync=False, identifier="EVENT_2445_fade_in_from_black_async_15"),
	Return()
])
