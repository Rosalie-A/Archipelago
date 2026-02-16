# E2476_BEAN_VALLEY_5_PIPE_AREA_LOADER
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
	SummonObjectToSpecificLevel(NPC_2, R335_BEAN_VALLEY_PIPE_ROOM_RIGHTMOST_PIPE_LARGE_ROOM),
	ActionQueueSync(target=NPC_0, subscript=[
		A_WalkSouthPixels(1),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ShiftZDownPixels(1),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_ShiftZDownPixels(1),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_ShiftZDownPixels(1),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_ShiftZDownPixels(1),
		A_WalkSouthwestPixels(4)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_WalkSoutheastPixels(7),
		A_WalkSouthwestPixels(1),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_WalkSoutheastPixels(7),
		A_WalkSouthwestPixels(1),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_WalkSoutheastPixels(7),
		A_WalkSouthwestPixels(1),
		A_VisibilityOff()
	]),
	ActionQueueSync(target=NPC_10, subscript=[
		A_WalkSoutheastPixels(7),
		A_WalkSouthwestPixels(1),
		A_VisibilityOff()
	]),
	ActionQueueAsync(target=NPC_11, subscript=[
		A_WalkSoutheastPixels(7),
		A_WalkSouthwestPixels(1),
		A_VisibilityOff()
	]),
	RunBackgroundEvent(event_id=E2477_BEAN_VALLEY_PIRANHA_PLANT_ANIMATIONS, return_on_level_exit=True),
	JmpIfBitClear(TEMP_7044_7, ["EVENT_2476_fade_in_from_black_async_18"]),
	RunEventAsSubroutine(E0081_MARIO_LANDS_SUBROUTINE),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2476_ret_17"]),
	RunEventAsSubroutine(E3911_BEAN_VALLEY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_2476_ret_17"),
	FadeInFromBlack(sync=False, identifier="EVENT_2476_fade_in_from_black_async_18"),
	JmpIfBitClear(DIRECTIONAL_7047_0, ["EVENT_2476_ret_24"]),
	ClearBit(DIRECTIONAL_7047_0),
	FreezeCamera(),
	SetAsyncActionScript(MARIO, A0010_FALL_ON_TRAMPOLINE),
	UnfreezeCamera(),
	Return(identifier="EVENT_2476_ret_24")
])
