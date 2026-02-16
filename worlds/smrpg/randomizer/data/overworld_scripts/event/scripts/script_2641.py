# E2641_FACTORY_1ST_ROOM_LOADER_AFTER_FIGHT
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 1),
	JmpIfBitClear(FAST_TRAVEL_ENABLED, ["EVENT_2641_action_queue_3"]),
	SummonObjectToCurrentLevel(NPC_8),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_WalkSouthwestPixels(8)
	], identifier="EVENT_2641_action_queue_3"),
	SetSyncActionScript(NPC_7, A0978_RANDOMLY_FACE_SOUTHWEST),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetSpriteSequence(index=1, is_mold=True, is_sequence=True, looping=True),
		A_SetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES)
	]),
	RunEventAsSubroutine(E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2641_ret_12"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2641_ret_12"]),
	RunEventAsSubroutine(E3916_INNER_FACTORY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2641_ret_12")
])
