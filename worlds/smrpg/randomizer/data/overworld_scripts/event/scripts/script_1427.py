# E1427_MUSHROOM_WAY_1_LOADER
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
	RunEventAsSubroutine(E0202_UNLOCK_FOREST_IF_GATED_BY_MUSHROOM_WAY_CHARACTER),
	ActionQueueAsync(target=NPC_0, subscript=[
		A_SetPriority(3),
		A_ReturnQueue()
	]),
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_1, ["EVENT_1427_remove_from_current_level_6"]),
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_2, ["EVENT_1427_remove_from_current_level_6"]),
	JmpIfBitSet(TOAD_IN_MUSHROOM_WAY_3, ["EVENT_1427_remove_from_current_level_6"]),
	Jmp(["EVENT_1427_run_event_as_subroutine_8"]),
	RemoveObjectFromCurrentLevel(NPC_8, identifier="EVENT_1427_remove_from_current_level_6"),
	RemoveObjectFromCurrentLevel(NPC_9),
	RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_1427_run_event_as_subroutine_8"),
	JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_1427_ret_13"]),
	RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
	JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_1427_ret_13"]),
	RunEventAsSubroutine(E3888_MUSHROOM_WAY_STAR_PIECE_SIGNAL),
	Return(identifier="EVENT_1427_ret_13")
])
