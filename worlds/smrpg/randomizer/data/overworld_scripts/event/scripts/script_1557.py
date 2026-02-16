# E1557_FOREST_MAZE_PAST_TRUNK_AREA_ROOM_LOADER
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
	JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_1557_jmp_if_bit_clear_10"]),
	ActionQueueAsync(target=MARIO, subscript=[
		A_VisibilityOff()
	]),
	FreezeAllNPCsUntilReturn(),
	FadeInFromBlack(sync=False),
	FreezeCamera(),
	SetAsyncActionScript(MARIO, A0482_FOREST_PLAYER_FALLS_TO_UNDERGROUND),
	SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
	UnfreezeCamera(),
	UnfreezeAllNPCs(),
	Return(),
	JmpIfBitClear(WIGGLER_GOES_DOWN_TRUNK, ["EVENT_1557_set_action_script_13"], identifier="EVENT_1557_jmp_if_bit_clear_10"),
	FadeInFromBlack(sync=False),
	Return(),
	SetSyncActionScript(NPC_0, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP, identifier="EVENT_1557_set_action_script_13"),
	SetSyncActionScript(NPC_1, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP),
	SetSyncActionScript(NPC_2, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP),
	SetSyncActionScript(NPC_3, A0036_WIGGLER_GOING_TO_STUMP_TO_SLEEP),
	Pause(24),
	FadeInFromBlack(sync=True),
	ActionQueueAsync(target=SCREEN_FOCUS, subscript=[
		A_Walk1StepWest()
	]),
	SetBit(WIGGLER_GOES_DOWN_TRUNK),
	Return()
])
