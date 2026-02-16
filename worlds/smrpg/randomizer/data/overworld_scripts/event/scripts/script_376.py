# E0376_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_LOADER
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
	Set0158Bit7Offset(0x0158),
	RunBackgroundEvent(event_id=E0392_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_REPEATING_SHYSTERS_POSITION, return_on_level_exit=True),
	JmpIfObjectInSpecificLevel(NPC_5, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, ["EVENT_376_jmp_if_object_in_level_6"]),
	PauseActionScript(NPC_9),
	ActionQueueAsync(target=NPC_9, subscript=[
		A_ShadowOn(),
		A_TransferToXYZF(x=20, y=118, z=4, direction=EAST),
		A_FaceSouthwest(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	SetSyncActionScript(NPC_9, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
	JmpIfObjectInSpecificLevel(NPC_6, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, ["EVENT_376_jmp_if_object_in_level_10"], identifier="EVENT_376_jmp_if_object_in_level_6"),
	PauseActionScript(NPC_7),
	ActionQueueAsync(target=NPC_7, subscript=[
		A_ShadowOn(),
		A_SetSolidityBits(cant_walk_through=True),
		A_SetSolidityBits(bit_4=True)
	]),
	SetSyncActionScript(NPC_7, A0128_WALK_RANDOM_DIRECTIONS),
	JmpIfObjectInSpecificLevel(NPC_4, R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE, ["EVENT_376_action_queue_12"], identifier="EVENT_376_jmp_if_object_in_level_10"),
	ActionQueueAsync(target=NPC_8, subscript=[
		A_ShadowOn(),
		A_FaceSouthwest(),
		A_SetSolidityBits(cant_walk_through=True)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetPriority(3)
	], identifier="EVENT_376_action_queue_12"),
	ActionQueueAsync(target=NPC_4, subscript=[
		A_SetPriority(3)
	]),
	PlaySound(sound=SO000_SILENCE, channel=4),
	FadeOutMusicToVolume(duration=1, volume=127),
	RunEventAsSubroutine(E0762_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_SHUFFLED_NPC_ANIMATION_LOADER),
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_376_ret_22"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_376_ret_22"]),
	RunEventAsSubroutine(E3889_MUSHROOM_KINGDOM_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_376_ret_22")
])
