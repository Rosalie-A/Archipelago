# E0670_MARRYMORE_UNOCCUPIED_EXTERIOR_LOADER
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
	ActionQueueSync(target=NPC_0, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_1, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_2, subscript=[
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_5, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_6, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_7, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_8, subscript=[
		A_SetPriority(3)
	]),
	ActionQueueSync(target=NPC_9, subscript=[
		A_SetPriority(3)
	]),
	RememberLastObject(),
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
	FadeInFromBlack(sync=False),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_670_ret_33"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_670_ret_33"]),
	RunEventAsSubroutine(E3902_MARRYMORE_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_670_ret_33")
])
