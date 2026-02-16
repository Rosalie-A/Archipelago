# E0081_MARIO_LANDS_SUBROUTINE
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
		A_Pause(1, identifier="EVENT_81_action_queue_4_SUBSCRIPT_pause_1"),
		A_JmpIfMarioInAir(["EVENT_81_action_queue_4_SUBSCRIPT_pause_1"]),
		A_ObjectMemorySetBit(arg_1=0x30, bits=[4]),
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True),
		A_JumpToHeight(108),
		A_ShadowOff(),
		A_Walk1StepSouth(),
		A_Pause(1, identifier="EVENT_81_action_queue_4_SUBSCRIPT_pause_8"),
		A_JmpIfMarioInAir(["EVENT_81_action_queue_4_SUBSCRIPT_pause_8"]),
		A_ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
		A_SetSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
	ClearBit(TEMP_7044_7),
	Return(identifier="EVENT_81_ret_9")
])
