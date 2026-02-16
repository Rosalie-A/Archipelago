# E0610_MARRYMORE_OCCUPIED_EXTERIOR_LOADER
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
	SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 28),
	Set0158Bit7Offset(0x0158),
	ClearBit(TEMP_7042_0),
	ClearBit(TEMP_7042_1),
	ClearBit(TEMP_7042_2),
	ClearBit(TEMP_7042_3),
	ClearBit(TEMP_7042_4),
	ClearBit(TEMP_7042_5),
	ClearBit(TEMP_7042_6),
	ClearBit(TEMP_7042_7),
	SetVarToConst(TEMP_70AC, 0),
	SetVarToConst(TEMP_70B8, 0),
	ClearBit(TEMP_704C_0),
	ClearBit(GUEST_DROPPED_OFF),
	ClearBit(EMPLOYMENT_704C_2),
	ClearBit(EMPLOYMENT_704C_3),
	ClearBit(BELLHOP_CALLED),
	ClearBit(MARRYMORE_UNKNOWN_709F_6),
	FadeOutMusicToVolume(duration=1, volume=127),
	JmpIfBitSet(MARRYMORE_BACKDOOR_OPEN, ["EVENT_610_action_queue_29"]),
	SetSyncActionScript(NPC_7, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_8, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	SetSyncActionScript(NPC_0, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_1, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_2, A0098_WALK_RANDOM_DIRECTIONS_NO_SOLIDITY_CHANGE),
	SetSyncActionScript(NPC_3, A0376_TURN_RANDOMLY_IN_PLACE),
	ActionQueueSync(target=NPC_5, subscript=[
		A_TransferToXYZF(x=17, y=113, z=0, direction=EAST),
		A_ShadowOn()
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_TransferToXYZF(x=18, y=113, z=0, direction=EAST),
		A_ShadowOn()
	]),
	Jmp(["EVENT_610_fade_in_from_black_async_38"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=15, y=72, z=8, direction=EAST)
	], identifier="EVENT_610_action_queue_29"),
	ActionQueueSync(target=NPC_0, subscript=[
		A_TransferToXYZF(x=16, y=68, z=8, direction=EAST),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_TransferToXYZF(x=16, y=69, z=8, direction=EAST),
		A_FaceSouthwest()
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferToXYZF(x=16, y=72, z=8, direction=EAST),
		A_FaceNorthwest()
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_FaceSoutheast()
	]),
	RememberLastObject(),
	SetSyncActionScript(NPC_5, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_6, A0376_TURN_RANDOMLY_IN_PLACE),
	SetSyncActionScript(NPC_8, A0113_HENCHMAN_BOUNCING_IN_PLACE),
	FadeInFromBlack(sync=False, identifier="EVENT_610_fade_in_from_black_async_38"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_610_ret_43"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_610_ret_43"]),
	RunEventAsSubroutine(E3902_MARRYMORE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_610_ret_43")
])
