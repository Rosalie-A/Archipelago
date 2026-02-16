# E0608_MARRYMORE_INN_3F_HALLWAY_LOADER
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
	JmpIfBitSet(TEMP_7042_0, ["EVENT_608_jmp_if_bit_set_4"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_608_jmp_if_bit_set_4"]),
	FadeInFromBlack(sync=False),
	Return(),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_608_action_queue_8"], identifier="EVENT_608_jmp_if_bit_set_4"),
	JmpIfBitSet(TEMP_7042_3, ["EVENT_608_action_queue_8"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_608_action_queue_8"]),
	ActionQueueSync(target=NPC_3, subscript=[
		A_TransferToXYZF(x=15, y=71, z=4, direction=EAST),
		A_TransferXYZFPixels(x=0, y=4, z=0, direction=EAST)
	]),
	ActionQueueSync(target=NPC_0, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	], identifier="EVENT_608_action_queue_8"),
	ActionQueueSync(target=NPC_1, subscript=[
		A_ClearSolidityBits(bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True)
	]),
	ApplySolidityModToLevel(permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0),
	JmpIfBitSet(BELLHOP_CALLED, ["EVENT_608_remove_from_current_level_22"]),
	FadeInFromBlack(sync=False),
	EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
	JmpIfBitSet(TEMP_7042_2, ["EVENT_608_ret_21"]),
	JmpIfBitSet(TEMP_7042_4, ["EVENT_608_ret_21"]),
	SetBit(TEMP_7042_2),
	ApplyTileModToLevel(use_alternate=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0),
	ApplySolidityModToLevel(permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=1),
	PlaySound(sound=SO016_OPEN_DOOR, channel=6),
	ActionQueueAsync(target=NPC_3, subscript=[
		A_SetSequenceSpeed(FAST),
		A_Walk1StepNortheast(),
		A_VisibilityOff(),
		A_TransferToXYZF(x=16, y=101, z=0, direction=EAST)
	]),
	Return(identifier="EVENT_608_ret_21"),
	RemoveObjectFromCurrentLevel(NPC_2, identifier="EVENT_608_remove_from_current_level_22"),
	FadeInFromBlack(sync=False),
	Return()
])
