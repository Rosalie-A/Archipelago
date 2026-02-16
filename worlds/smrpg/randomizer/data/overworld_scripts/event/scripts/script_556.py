# E0556_ROSE_TOWN_LIBERATED_LOADER
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
	FadeOutMusicToVolume(duration=1, volume=127),
	JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_556_action_queue_4"]),
	ApplyTileModToLevel(use_alternate=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=4),
	ApplySolidityModToLevel(permanent=True, room_id=R084_ROSE_TOWN_OUTSIDE, mod_id=4),
	ActionQueueSync(target=NPC_2, subscript=[
		A_SetPriority(3)
	], identifier="EVENT_556_action_queue_4"),
	ActionQueueSync(target=NPC_3, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_4, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetPriority(3)
	]),
	RememberLastObject(),
	SummonObjectToSpecificLevel(NPC_2, R087_ROSE_TOWN_ITEM_SHOP),
	SummonObjectToSpecificLevel(NPC_3, R087_ROSE_TOWN_ITEM_SHOP),
	SummonObjectToSpecificLevel(NPC_1, R091_ROSE_TOWN_COUPLES_HOUSE),
	RunBackgroundEvent(event_id=E0557_ROSE_TOWN_LIBERATED_LOADER_BACKGROUND, return_on_level_exit=True),
	FadeInFromBlack(sync=False),
	SetBit(TEMP_709F_5),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_556_ret_22"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_556_ret_22"]),
	RunEventAsSubroutine(E3895_ROSE_TOWN_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_556_ret_22")
])
